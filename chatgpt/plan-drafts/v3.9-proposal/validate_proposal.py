"""Validate this proposal without building or changing a master plan.

Run from any directory: python3 /path/to/v3.9-proposal/validate_proposal.py
"""
import difflib
import hashlib
from pathlib import Path
import subprocess
import sys
import tempfile

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
PLAN = ROOT / "plan/Phase1_Master_Plan_v3.8.md"
BASE = ROOT / "plan/check_plan.py"
HASHES = {
    PLAN: "25bb309e79a610f2b37651107d1b780cedd5e3897fd2c969fb0e2f3c4b0690a4",
    BASE: "6c55bf071327801342463b4ac58efa721444a60c10d884a2dd9640178157f816",
}


def patched_checker():
    original = BASE.read_text(encoding="utf-8")
    rules = (HERE / "proposed_rules.py").read_text(encoding="utf-8")
    insertion = "\ndef v39_check(text):\n" + "\n".join("    " + line for line in rules.splitlines())
    insertion += "\n    return check(text)\n\n"
    anchor = "if small:\n    warnings.append"
    assert original.count(anchor) == 1
    return original.replace(anchor, insertion + "errors.extend(v39_check(text))\n\n" + anchor, 1)


def run(args, expected=0):
    result = subprocess.run(args, cwd=ROOT, text=True, capture_output=True, timeout=60)
    if result.returncode != expected:
        raise AssertionError(f"Unexpected exit {result.returncode}, expected {expected}: {args}\n{result.stdout}\n{result.stderr}")
    return result


def main():
    for path, expected in HASHES.items():
        actual = hashlib.sha256(path.read_bytes()).hexdigest()
        if actual != expected:
            raise AssertionError(f"Base changed: {path}; rebase the proposal instead of trusting old results")
    print("PASS: source plan and checker hashes match the reviewed baseline")
    baseline = run([sys.executable, str(BASE), str(PLAN)])
    print(baseline.stdout.strip())
    negatives = run([sys.executable, str(ROOT / "claude/plan-drafts/v3.8-build/negative_tests.py"), str(PLAN), str(BASE)])
    assert "ALL NEGATIVE TESTS FAIL AS EXPECTED" in negatives.stdout
    print("PASS: 25 existing negative mutations rejected")
    unit = run([sys.executable, "-m", "unittest", "discover", "-s", str(HERE), "-p", "test_*.py", "-v"])
    print(unit.stderr.strip())
    candidate = run([sys.executable, str(HERE / "check_plan_proposed.py"), str(PLAN)], expected=1)
    expected_messages = ["Order: CL3 starts", "Order: MC2 starts", "Cloud labs:", "Core: explicitly protect"]
    issues = [line.strip() for line in candidate.stdout.splitlines() if line.startswith(" -")]
    assert len(issues) == 4 and all(any(msg in issue for issue in issues) for msg in expected_messages), candidate.stdout
    print("PASS: prototype rejects the four known v3.8 findings for the expected reasons")
    print(candidate.stdout.strip())
    patched = patched_checker()
    diff = "".join(difflib.unified_diff(BASE.read_text(encoding="utf-8").splitlines(keepends=True),
                    patched.splitlines(keepends=True), fromfile="a/plan/check_plan.py", tofile="b/plan/check_plan.py"))
    assert diff == (HERE / "check_plan.py.diff").read_text(encoding="utf-8"), "Patch differs from tested proposed rules"
    run(["git", "apply", "--check", str(HERE / "check_plan.py.diff")])
    with tempfile.TemporaryDirectory(prefix="phase1-checker-proposal-") as temp:
        checker = Path(temp) / "check_plan.py"
        checker.write_text(patched, encoding="utf-8")
        integrated = run([sys.executable, str(checker), str(PLAN)], expected=1)
        assert all(msg in integrated.stdout for msg in expected_messages), integrated.stdout
        assert len([l for l in integrated.stdout.splitlines() if l.startswith(" -")]) == 4
    print("PASS: single-file patch applies cleanly and reports the same four failures")
    for path, expected in HASHES.items():
        assert hashlib.sha256(path.read_bytes()).hexdigest() == expected
    print("PASS: approved master and checker remain unchanged")
    print("PROPOSAL VALIDATED. This is not a PASS for a v3.9 plan; no such plan was generated.")


if __name__ == "__main__":
    main()
