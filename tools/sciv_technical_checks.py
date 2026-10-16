"""Run offline suites and structural gates; retain separate outcomes, including SKIP."""
import argparse
import json
import os
from pathlib import Path
import re
import subprocess
import sys


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--generator", type=Path, required=True)
    parser.add_argument("--governance", type=Path, required=True)
    parser.add_argument("--only", nargs="+")
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    generator, governance = args.generator.resolve(), args.governance.resolve()
    output = root / "auditorias/EA-000008-000003-evidencias"
    output.mkdir(exist_ok=True)
    commands = {
        "filesystem": (root, ["-m", "unittest", "discover", "-s", "tools", "-p", "test_sciv_disabled_provision.py", "-v"]),
        "generator-regression": (generator / "tools", ["-m", "unittest", "test_project_creation_gate", "test_legacy_bootstrap_gate", "test_validate_execution_action_plan", "test_sciv_bootstrap", "-v"]),
        "sciv-regression": (governance / "runtime", ["-m", "unittest", "test_sciv_mailbox", "test_sciv_essential", "test_sciv_archive", "test_sciv_per_project", "test_sciv_publication", "test_sciv_security", "-v"]),
        "pep-offline": (governance / "tools", ["-m", "unittest", "test_r2_pep_offline", "-v"]),
        "current-matrix": (root, [str(generator / "tools/validate_execution_action_plan.py"), "--project-root", str(root), "--strategy-code", "EA-000008-000003", "--plan-ref", "estrategias/EA-000008-000003-sciv-sob-demanda.md"]),
        "rota-b-sciv": (root, [str(generator / "tools/project_creation_gate.py"), "--project-root", str(root), "--route", "B", "--gate", "sciv"]),
        "provision-readback": (root, [str(root / "tools/sciv_disabled_provision.py"), "--generator", str(generator), "--apply"]),
    }
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", PYTHONIOENCODING="utf-8")
    result_path = output / "results.json"
    results = json.loads(result_path.read_text(encoding="utf-8")) if args.only and result_path.exists() else {}
    for name, (cwd, arguments) in commands.items():
        if args.only and name not in args.only:
            continue
        result = subprocess.run([sys.executable, "-B", *arguments], cwd=cwd, env=env,
                                capture_output=True, encoding="utf-8", errors="replace", timeout=180)
        log = result.stdout + result.stderr
        for path, label in ((str(root), "<PROJECT>"), (str(generator), "<GENERATOR>"),
                            (str(governance), "<GOVERNANCE>"), (str(Path.home()), "<USER_HOME>")):
            log = log.replace(path, label)
        (output / (name + ".log")).write_text(log, encoding="utf-8")
        cases = re.findall(r"^test_.*? \.\.\. (ok|FAIL|ERROR|skipped[^\n]*)$", log, re.M)
        counts = {"PASS": cases.count("ok"), "FAIL": cases.count("FAIL"),
                  "ERROR": cases.count("ERROR"), "SKIP": sum(c.startswith("skipped") for c in cases)}
        results[name] = {"exit_code": result.returncode,
                         "status": "PASS_WITH_SKIPS" if result.returncode == 0 and counts["SKIP"] else "PASS" if result.returncode == 0 else "FAIL",
                         "counts": counts, "command": ["python", "-B", *arguments]}
        # Commands are public and reproducible without disclosing workstation paths.
        results[name]["command"] = [x.replace(str(root), "<PROJECT>").replace(str(generator), "<GENERATOR>").replace(str(governance), "<GOVERNANCE>") for x in results[name]["command"]]
        print(name, results[name]["status"], counts)
    (output / "results.json").write_text(json.dumps(results, indent=2) + "\n", encoding="utf-8")
    return int(any(r["exit_code"] for r in results.values()))


if __name__ == "__main__":
    raise SystemExit(main())
