"""Offline filesystem regressions for this project's disabled provisioner."""
import os
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch

from sciv_disabled_provision import safe, compose, apply, BEGIN, END


class FilesystemTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)

    def test_path_traversal_and_ambiguous_windows_names(self):
        for name in ("../escape", "/absolute", "a//b", "a/../b", "C:/x", "a\\b", "a./b"):
            with self.subTest(path=name), self.assertRaises(ValueError):
                safe(self.root, name)

    def test_hardlink_physical(self):
        (self.root / "original").write_bytes(b"preserve")
        os.link(self.root / "original", self.root / "linked")
        with self.assertRaisesRegex(ValueError, "HARDLINK_DENIED"):
            safe(self.root, "linked")
        self.assertEqual((self.root / "original").read_bytes(), b"preserve")

    def test_symlink_physical(self):
        (self.root / "original").write_bytes(b"preserve")
        try:
            os.symlink(self.root / "original", self.root / "linked")
        except OSError as exc:
            self.skipTest(f"OS_SYMLINK_UNAVAILABLE winerror={getattr(exc, 'winerror', None)}")
        with self.assertRaisesRegex(ValueError, "LINK_OR_REPARSE_DENIED"):
            safe(self.root, "linked")

    def test_junction_physical(self):
        if os.name != "nt":
            self.skipTest("WINDOWS_ONLY")
        target = self.root / "target"
        target.mkdir()
        link = self.root / "junction"
        result = subprocess.run(["cmd", "/c", "mklink", "/J", str(link), str(target)], capture_output=True)
        if result.returncode:
            self.skipTest("OS_JUNCTION_UNAVAILABLE")
        self.addCleanup(lambda: os.rmdir(link))
        with self.assertRaisesRegex(ValueError, "LINK_OR_REPARSE_DENIED"):
            safe(self.root, "junction/file")

    def test_reparse_flag_fail_closed(self):
        (self.root / "file").write_bytes(b"x")
        original = Path.lstat
        def reparse(path):
            value = original(path)
            if path == self.root / "file":
                from types import SimpleNamespace
                return SimpleNamespace(st_file_attributes=0x400, st_nlink=1)
            return value
        with patch.object(Path, "lstat", reparse):
            with self.assertRaisesRegex(ValueError, "LINK_OR_REPARSE_DENIED"):
                safe(self.root, "file")

    def test_idempotence_and_byte_readback(self):
        files = {"nested/a": b"\x00\xff\r\n", "nested/b": b"second"}
        apply(self.root, files)
        times = {n: (self.root / n).stat().st_mtime_ns for n in files}
        apply(self.root, files)
        self.assertEqual(times, {n: (self.root / n).stat().st_mtime_ns for n in files})
        self.assertTrue(all((self.root / n).read_bytes() == raw for n, raw in files.items()))

    def test_interruption_and_reconciliation(self):
        files = {"a": b"one", "b": b"two"}
        original = os.replace
        def interrupted(source, target):
            if Path(target).name == "b":
                raise OSError("SIMULATED_INTERRUPTION")
            return original(source, target)
        with patch("os.replace", interrupted):
            with self.assertRaises(OSError):
                apply(self.root, files)
        self.assertEqual((self.root / "a").read_bytes(), b"one")
        self.assertFalse((self.root / "b").exists())
        apply(self.root, files)
        self.assertEqual((self.root / "b").read_bytes(), b"two")

    def test_parent_file_rejected_before_mutation(self):
        (self.root / "parent").write_bytes(b"unchanged")
        with self.assertRaises(ValueError):
            apply(self.root, {"first": b"never", "parent/child": b"never"})
        self.assertFalse((self.root / "first").exists())

    def test_external_adapter_bytes_and_idempotence(self):
        original = b"prefix\r\n**Bootstrap:**\r\nlegal mission\xff"
        block = BEGIN + b"\nSCIV disabled\n" + END + b"\n\n"
        new = compose(original, block)
        self.assertEqual(new.replace(block, b""), original)
        self.assertEqual(compose(new, block), new)
        with self.assertRaises(ValueError):
            compose(new + BEGIN, block)


if __name__ == "__main__":
    unittest.main()
