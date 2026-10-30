"""Run the approved checker plus proposed v3.9 structural checks.

Usage (from omieee/docs):
  python3 chatgpt/plan-drafts/v3.9-proposal/check_plan_proposed.py PLAN.md

This read-only prototype does not create v3.9 or update plan/check_plan.py.
The approved v3.8 file is EXPECTED to fail the proposed stricter rules.
"""
import argparse
from pathlib import Path
import subprocess
import sys

from proposed_rules import check


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("plan", type=Path)
    parser.add_argument("--base-checker", type=Path,
                        default=Path(__file__).resolve().parents[3] / "plan/check_plan.py")
    args = parser.parse_args()
    try:
        text = args.plan.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        print(f"FAIL: cannot read plan: {exc}")
        return 1
    proposed = check(text)
    try:
        result = subprocess.run([sys.executable, str(args.base_checker), str(args.plan)],
                                text=True, capture_output=True, timeout=30)
    except (OSError, subprocess.TimeoutExpired) as exc:
        print(f"FAIL: cannot run approved checker: {exc}")
        return 1
    print("APPROVED CHECKER:", "PASS" if result.returncode == 0 else "FAIL")
    if result.returncode:
        print(result.stdout.strip())
        if result.stderr:
            print("Approved checker diagnostic:", result.stderr.strip())
    if proposed:
        print("PROPOSED RULES: FAIL")
        for error in proposed:
            print(" -", error)
    else:
        print("PROPOSED RULES: PASS")
    if result.returncode or proposed:
        return 1
    print("PASS: approved checks and proposed structural rules")
    return 0


if __name__ == "__main__":
    sys.exit(main())
