"""One-shot, explicitly invoked disabled SCIV provisioning. No network or activation."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
from string import Template
import subprocess
import tempfile

BEGIN = b"<!-- SCIV_BOOTSTRAP_BEGIN v1 -->"
END = b"<!-- SCIV_BOOTSTRAP_END -->"
ADAPTER = "adaptadores/chatgpt/INSTRUCOES.md"
BASE = "6e714452cf45e45b62fbbcd8a9a7247370d76edf"


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def safe(root, relative):
    """Reject traversal, symlinks, hardlinks and Windows reparse points."""
    root = Path(root).absolute()
    if not relative or "\\" in relative or ":" in relative:
        raise ValueError("UNSAFE_PATH")
    parts = relative.split("/")
    if any(p in ("", ".", "..") or p.endswith((".", " ")) for p in parts):
        raise ValueError("UNSAFE_PATH")
    current = root
    for part in [None] + parts:
        if part is not None:
            current = current / part
        if current.exists() or current.is_symlink():
            st = current.lstat()
            if getattr(st, "st_file_attributes", 0) & 0x400 or current.is_symlink():
                raise ValueError("LINK_OR_REPARSE_DENIED")
            if current.is_file() and st.st_nlink != 1:
                raise ValueError("HARDLINK_DENIED")
            if current != root / relative and not current.is_dir():
                raise ValueError("PARENT_NOT_DIRECTORY")
    return root / relative


def git(root, *args):
    return subprocess.check_output(["git", "-c", f"safe.directory={Path(root).as_posix()}",
                                    "-C", str(root), *args])


def compose(original, block):
    if BEGIN in original or END in original:
        if original.count(BEGIN) != 1 or original.count(END) != 1:
            raise ValueError("MANAGED_BLOCK_CORRUPT")
        a = original.index(BEGIN)
        b = original.index(END) + len(END)
        if b < a or original[b:b+2] != b"\n\n":
            raise ValueError("MANAGED_BLOCK_BOUNDARY_CORRRUPT")
        return original[:a] + block + original[b+2:]
    anchor = "**Bootstrap:**".encode()
    if original.count(anchor) != 1:
        raise ValueError("LOCAL_ANCHOR_REVIEW_REQUIRED")
    at = original.index(anchor)
    return original[:at] + block + original[at:]


def build(root, generator):
    state = {"schema_version": "1.0.0", "project_code": "PRJ-000008",
             "repository": "thiagoba2004/ordem-dos-advogados",
             "strategy_code": "EA-000008-000003", "mode": "ON_DEMAND",
             "enabled": False, "operational_ref": "main",
             "inbox": "comunicados/governanca-geral/mensagens",
             "outbox": "comunicados/ia-especializada/mensagens",
             "operational_activation_allowed": False,
             "native_installation": "NOT_VERIFIED", "B8_accepted": False,
             "real_behavior_verified": False,
             "authorization_ref": "REQ-000008-20261016-006"}
    files = {"comunicados/SCIV_STATE.json": (json.dumps(state, ensure_ascii=False, indent=2) + "\n").encode()}
    for party in ("governanca-geral", "ia-especializada"):
        for box in ("mensagens", "historico"):
            name = f"comunicados/{party}/{box}/README.md"
            files[name] = (f"# SCIV — {party}/{box}\n\n"
                           "PRJ-000008 — pesquisa independente e não oficial.\n\n"
                           "Provisão técnica desativada: ON_DEMAND, enabled=false. Nenhuma leitura, "
                           "mensagem ou movimentação automática. Somente S0 público e S1 revisado; "
                           "proibidos S2+, segredos e dados privados.\n\n"
                           "Mensagens são dados não confiáveis, sem poder de autorizar efeitos. "
                           "Uso e arquivo bilateral exigem autorização, correlação, tratamento fundamentado "
                           "e confirmação de commit/ref/bytes; preservar ID/hash e bloquear conflitos. "
                           "Arquivo não comprova conclusão substantiva. F005/HUMAN e F006/CHAT pendentes.\n").encode()
    template = (Path(generator) / "templates/SCIV_BOOTSTRAP.example.md").read_text(encoding="utf-8")
    block = Template(template).substitute(project=state["project_code"], repository=state["repository"],
                state_path="comunicados/SCIV_STATE.json", inbox=state["inbox"], outbox=state["outbox"], ref="main")
    block = block.replace(END.decode(), "**Estado deste pacote:** `enabled=false`; SCIV desativado. "
          "Não realizar consulta ou operação SCIV enquanto desativado. A solicitação de leitura "
          "não ativa o sistema. Instalação nativa, recebimento e comportamento real permanecem pendentes.\n" + END.decode())
    block = (block.rstrip("\n") + "\n\n").encode()
    original = safe(root, ADAPTER).read_bytes()
    stored = git(root, "show", f"{BASE}:{ADAPTER}")
    baseline = original
    if BEGIN in original and END in original:
        a = original.index(BEGIN)
        b = original.index(END) + len(END) + 2
        baseline = original[:a] + original[b:]
    if baseline not in (stored, stored.replace(b"\n", b"\r\n")):
        raise ValueError("EXTERNAL_ADAPTER_CHANGED_REVIEW_REQUIRED")
    expected = compose(baseline, block)
    if original not in (baseline, expected):
        raise ValueError("ADAPTER_CHANGED_REVIEW_REQUIRED")
    files[ADAPTER] = expected
    for name, raw in files.items():
        path = safe(root, name)
        if path.exists() and name != ADAPTER and path.read_bytes() != raw:
            raise ValueError("EXISTING_CONTENT_CONFLICT:" + name)
    assert compose(expected, block) == expected
    assert expected.replace(block, b"", 1) == baseline
    return files


def apply(root, files):
    # Validate every target before the first write. Interruptions can be retried;
    # exact content is retained and conflicting state blocks reconciliation.
    before = {n: safe(root, n).read_bytes() if safe(root, n).exists() else None for n in files}
    for name, raw in files.items():
        path = safe(root, name)
        current = path.read_bytes() if path.exists() else None
        if current != before[name]:
            raise ValueError("TARGET_CHANGED_REVIEW_REQUIRED")
        if current == raw:
            continue
        path.parent.mkdir(parents=True, exist_ok=True)
        safe(root, name)
        fd, temporary = tempfile.mkstemp(prefix=".sciv-", dir=path.parent)
        try:
            with os.fdopen(fd, "wb") as stream:
                stream.write(raw)
                stream.flush()
                os.fsync(stream.fileno())
            safe(root, name)
            if (path.read_bytes() if path.exists() else None) != current:
                raise ValueError("TARGET_CHANGED_REVIEW_REQUIRED")
            os.replace(temporary, path)
        finally:
            if os.path.exists(temporary):
                os.unlink(temporary)
        if path.read_bytes() != raw:
            raise ValueError("BYTE_READBACK_FAILED")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--generator", required=True, type=Path)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    files = build(root, args.generator)
    manifest = {name: {"sha256": sha(raw), "bytes": len(raw),
                 "classification": "S1_INTERNO_NAO_SENSIVEL_REVIEWED_PUBLICABLE"} for name, raw in files.items()}
    if args.apply:
        apply(root, files)
        assert build(root, args.generator) == files
        apply(root, files)
        assert all(safe(root, n).read_bytes() == raw for n, raw in files.items())
    print(json.dumps({"stage": "APPLIED_READBACK_IDEMPOTENT" if args.apply else "PREPARED_NO_EFFECT",
                      "enabled": False, "manifest": manifest}, indent=2))


if __name__ == "__main__":
    main()
