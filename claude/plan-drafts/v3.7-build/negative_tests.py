"""Negative tests for check_plan_v3.7.py: each mutation of the v3.7 plan must FAIL with the named error.

Run from this folder: python3 negative_tests.py ../Phase1_Master_Plan_v3.7.md ../check_plan_v3.7.py
"""
import os
import subprocess
import sys
import tempfile

plan, checker = sys.argv[1], sys.argv[2]
base = open(plan, encoding="utf-8").read()

CASES = [
    ("coaching owner named", "**Two coaches, one repository.**", "**Two coaches, one repository.** The coaching owner runs every unit.", "Coaching owner: line"),
    ("human mock removed from the map", "**DSA** 2h: Human live-coding mock", "**DSA** 2h: Peer session", "Human live-coding mock (section 6.6 #13) is not in the week map"),
    ("rule 6.6 #13 removed", "13. **Human live-coding mock", "13. **Peer mock", "Section 6.6 has no rule 13"),
    ("1b harvest slice removed", "India and international slices, for resume v2 and the Gate B region decision; Om re-marks both top 5 lists", "for resume v2; Om re-marks his top 5", "International slice: no 1b harvest week"),
    ("1a harvest slice removed", "Om reads the international slice and marks his international top 5 (v3.7, +0.5h)", "Om reads the extra postings (v3.7, +0.5h)", "International slice: no 1a harvest week"),
    ("Gate C record broken", "Only line 1 decides Gate C.", "Line 1 matters most.", "Gate C: the four-line readiness record"),
    ("section 1 stale date", "Forecast (v3.7): Gate A May 2 2027, Gate B Jan 30 2028", "Forecast (v3.7): Gate A May 2 2027, Gate B Jan 23 2028", "Section 1 decision 4: forecast should read"),
    ("section 4 stale date", "the v3.7 forecast is Gate A May 2 2027, Gate B Jan 30 2028", "the v3.7 forecast is Gate A May 2 2027, Gate B Jan 23 2028", "Section 4 intro: forecast should read"),
    ("section 11 stale date", "Phase 2 starts after Gate C, now forecast Feb 27 2028", "Phase 2 starts after Gate C, now forecast Feb 20 2028", "Section 11: Phase 2 should start"),
    ("section 14 stale hours", "820.75 scheduled hours", "814.25 scheduled hours", "Section 14 intro: scheduled hours"),
    ("section 14 stale DSA", "DSA totals 144.25,", "DSA totals 140.5,", "Section 14 intro: DSA total"),
    ("DSA header off (v3.6 rule)", "### 6.6 DSA (144.25 hrs, daily)", "### 6.6 DSA (140.5 hrs, daily)", "DSA: section 6.6 says"),
    ("week label off (v3.6 rule)", "| W61 · Nov 29-Dec 5 · 12h |", "| W61 · Nov 29-Dec 5 · 12.5h |", "W61: items sum to"),
]

fails = 0
for name, old, new, expect in CASES:
    if base.count(old) != 1:
        print(f"SETUP ERROR [{name}]: target found {base.count(old)} times")
        fails += 1
        continue
    with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False, encoding="utf-8") as f:
        f.write(base.replace(old, new))
        tmp = f.name
    r = subprocess.run([sys.executable, checker, tmp], capture_output=True, text=True)
    os.unlink(tmp)
    ok = r.returncode != 0 and "FAIL" in r.stdout and expect in r.stdout
    print(("ok  " if ok else "BAD ") + name)
    fails += 0 if ok else 1
r = subprocess.run([sys.executable, checker, plan], capture_output=True, text=True)
clean = r.returncode == 0 and "PASS" in r.stdout
print(("ok  " if clean else "BAD ") + "unmodified plan passes")
fails += 0 if clean else 1
print("ALL NEGATIVE TESTS FAIL AS EXPECTED" if fails == 0 else f"{fails} PROBLEM(S)")
sys.exit(1 if fails else 0)
