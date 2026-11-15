"""Negative tests for check_plan_v3.9.py: each mutation of the v3.9 plan must FAIL with the named error.

Run from this folder: python3 negative_tests.py ../Phase1_Master_Plan_v3.9.md ../check_plan_v3.9.py
A target that appears several times is mutated at its first occurrence only, unless the case says "all".
A case's target may also be a list of (old, new) pairs, applied in order (v3.9 r2).
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
    ("section 1 stale date", "Forecast (v3.9): Gate A Jun 6 2027, Gate B Apr 30 2028", "Forecast (v3.9): Gate A Jun 6 2027, Gate B Apr 23 2028", "Section 1 decision 4: forecast should read"),
    ("section 4 stale date", "the v3.9 forecast is Gate A Jun 6 2027, Gate B Apr 30 2028", "the v3.9 forecast is Gate A Jun 6 2027, Gate B Apr 23 2028", "Section 4 intro: forecast should read"),
    ("section 11 stale date", "Phase 2 starts after Gate C, now forecast May 28 2028", "Phase 2 starts after Gate C, now forecast May 21 2028", "Section 11: Phase 2 should start"),
    ("section 14 stale hours", "969 scheduled hours", "934 scheduled hours", "Section 14 intro: scheduled hours"),
    ("section 14 stale DSA", "DSA totals 169.5,", "DSA totals 163.25,", "Section 14 intro: DSA total"),
    ("DSA header off (v3.6 rule)", "### 6.6 DSA (169.5 hrs, daily)", "### 6.6 DSA (163.25 hrs, daily)", "DSA: section 6.6 says"),
    ("week label off (v3.6 rule)", "| W61 · Nov 29-Dec 5 · 12h |", "| W61 · Nov 29-Dec 5 · 12.5h |", "W61: items sum to"),
    # ---- v3.8 rules ----
    ("use step removed from a Go part", "Use in the agent (code): `Probe` and `Result` structs", "Then `Probe` and `Result` structs", "Use step: W"),
    ("use step removed from a Python part", "Use in PRCP (code): a frozen dataclass key", "Then a frozen dataclass key", "Use step: W"),
    ("use step removed from a Kubernetes part", "Use on kind (code): a Service in front of PRCP", "Then a Service in front of PRCP", "Use step: W"),
    ("use step without its type (A2)", "Use in the agent (code): `Probe` and `Result` structs", "Use in the agent: `Probe` and `Result` structs", "Use step: W"),
    ("part starts with 15 minutes (A3)", "fix or log what you cannot defend [section 6.1] (continued)", "fix or log what you cannot defend [section 6.1]", "Small start: W5 Y7a"),
    ("untaught SQL in P1 (A1)", "the rollback fixture is a `yield` fixture and each transaction uses `with`", "the rollback fixture is a `yield` fixture, each transaction uses `with` and one query uses `IN`", "Taught before named: W7 P1"),
    ("untaught term named early", "rewrite one closed Go kata and its tests as that unit wrote them, and add one changed case", "rewrite one closed Go kata and its table-driven test, and add one changed case", "Taught before named: W4 RR names table-driven"),
    ("asyncio note back in G7", "collect results over a channel; run `go test -race`", "collect results over a channel; note goroutines vs asyncio tasks", "Taught before named: W"),
    ("spaced review limited to DSA again", "DSA keeps its spaced re-solves; every other topic", "DSA alone keeps continuous spaced review; every other topic", "Section 7: spaced review is limited to DSA"),
    ("use rule removed", "**Use in real code within 7 days (v3.8, Om, Oct 24).**", "**Practice note.**", "Section 6: the use rule"),
    ("warm-up rule removed", "**Warm-up (v3.8).**", "**Warm-up.**", "Section 6.12: the warm-up rule"),
    # ---- v3.9 rules ----
    ("token rules removed", "**Token rules (v3.9", "**Token notes (v3.9", "Section 0: the v3.9 token rules are missing"),
    ("recognition rule removed", "14. **Recognition first (v3.9", "14. **Practice (v3.9", "Section 6.6: the recognition-first rule"),
    ("measured pace removed", "**Measured pace at the Nov 15 re-forecast (v3.9):**", "**Pace:**", "Section 4: the measured-pace forecast is missing"),
    ("DS1 dropped from section 6", "| DS1 Distributed-systems proof (v3.9) | 13 |", "| Distributed-systems proof (v3.9) | 13 |", "Unit inventory: DS1 is missing"),
    ("CL3 session cut to 2 hours", "**CL3** 3h", "**CL3** 2h", "CL3: W59 has 2h of CL3"),
    ("DS1 use step removed", "Use in the agent (code): the agent's result IDs", "Then the agent's result IDs", "Use step: W"),
    ("cards rule removed", "**Bedside cards (v3.8, optional).**", "**Cards.**", "Section 6.12: the bedside cards rule"),
    # ---- v3.9 r2 rules (ChatGPT's five findings and five proposals, Nov 15) ----
    ("E1 dropped from section 6", "| E1 Release evidence and the gate endpoint (v3.9 r2) | 7.5 |", "| Release evidence and the gate endpoint (v3.9 r2) | 7.5 |", "Unit inventory: E1 is missing"),
    ("dated review moved out of its week (finding 2)", "74 D28 Mon Nov 16", "74 D28 Thu Nov 26", "Dated review: W7 names Thu Nov 26, outside the week"),
    ("dated review on the wrong weekday", "704 D28 Mon Nov 16", "704 D28 Tue Nov 16", "Dated review: W7 names Tue Nov 16, but that date is a Mon"),
    ("r1's W7 DSA text back (finding 2)", "Sorting lessons 10-12: insertion", "875 D28 on Thu Nov 26 first; then sorting lessons 10-12: insertion", "Dated review: W7 names Thu Nov 26, outside the week"),
    ("stories aloud stale in 6.8 (finding 5)", "told aloud in voice mode in W15-W17", "told aloud in voice mode in W10-W11", "Week reference (6.8 R2 aloud)"),
    ("unseen set 2 stale in 6.6 (finding 5)", "Set 2 runs in the Gate B week (W82)", "Set 2 runs in the Gate B week (W70)", "Week reference (6.6 #12 set 2)"),
    ("unseen set 2 stale in the Gate B list", "Plus unseen set 2 (W82,", "Plus unseen set 2 (W70,", "Week reference (4 unseen set 2)"),
    ("blind sets stale in the Gate B list", "before the gate (W80-W81) at 80%", "before the gate (W68-W69) at 80%", "Week reference (4 blind sets)"),
    ("Naukri week stale in 6.8", "Naukri live by W33;", "Naukri live by W28;", "Week reference (6.8 R1 proof)"),
    ("mock 2 week stale in 6.4", "(mock 2 is in W54)", "(mock 2 is in W49)", "Week reference (6.4 mock 2)"),
    ("1c note stale in section 14", "(W83 8.25h, W84 10.5h,", "(W71 8.25h, W72 10.5h,", "Week reference (14 1c note)"),
    ("a week reference sentence removed", "Also in the Gate A week (W35), but never a Gate A item: unseen set 1", "Unseen set 1", "Week reference (4 unseen set 1): the sentence is missing"),
    ("Go text and key disagree (ChatGPT's mutation)", "then Learning Go 2e chapter 5 (functions as values", "then Learning Go 2e chapter 14 (functions as values", "Go map: W"),
    ("Go key outside the declared map", "LG2 (ch 6)]", "LG2 (ch 13)]", "outside G3's declared chapters"),
    ("G2 loses chapter 4 (finding 3)", [("Learning Go 2e chapter 4 (blocks", "Learning Go 2e chapter 5 (blocks", "all"), ("LG2 (ch 4)]", "LG2 (ch 5)]", "all")], None, "Go map: G2 never cites Learning Go chapter [4]"),
    ("Gate A item after the gate", [("**P4** 2h:", "**A1** 2h:"), ("**A1** 2h: Sequential agent", "**P4** 2h: Sequential agent")], None, "Gate A item P4 ends in W36"),
    ("run sheet hours do not add up", "| 6h: P1 0.5h,", "| 5h: P1 0.5h,", "Run sheet: W7 at 6h moves 5.0h"),
    ("run sheet week missing", "| W12 (Dec 21-27, 7h row) |", "| W 12 (Dec 21-27, 7h row) |", "Run sheet: W12 is missing"),
    ("run sheet removed", "**Run sheet, W7 to W12", "**Plan for the leave", "Section 14: the W7-W12 run sheet is missing"),
    ("scenario label removed (finding 1)", "**Available-time scenarios (v3.9 r2)", "**Pace scenarios", "Section 4: the available-time scenarios"),
    ("short-week rule removed", "**Short weeks (v3.9 r2", "**Weeks (v3.9 r2", "Section 14: the short-week rule"),
    # ---- v3.9 final (ChatGPT's 16:22 review) ----
    ("stale Gate A month in applications (finding 1)", "- After Gate A (Jun 6 2027): normal application volume.", "- After Gate A (May 2027): normal application volume.", "Applications: normal volume should start after Gate A"),
    ("stale joining month (finding 1)", "means joining around August 2028", "means joining around May 2028", "Applications: an offer after Gate B"),
    ("Gate A record removed (idea 4)", "**Gate A record (v3.9 final", "**Gate A notes (v3.9 final", "Section 4: the four-line Gate A record"),
    ("slower dates read as a forecast again (finding 2)", "fixed-work illustrations (v3.9 final)", "forecast at the measured pace", "Section 4: the slower-pace dates are not labelled"),
    ("release-evidence table removed", "**Release evidence (v3.9 r2", "**Evidence (v3.9 r2", "Section 6.1: the release-evidence case table"),
]

fails = 0
for name, old, new, expect in CASES:
    pairs = old if isinstance(old, list) else [(old, new)]
    text_, setup_ok = base, True
    for pr in pairs:
        o, nw = pr[0], pr[1]
        if text_.count(o) < 1:
            setup_ok = False
            break
        text_ = text_.replace(o, nw) if (len(pr) > 2 and pr[2] == "all") else text_.replace(o, nw, 1)
    if not setup_ok:
        print(f"SETUP ERROR [{name}]: target not found")
        fails += 1
        continue
    with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False, encoding="utf-8") as f:
        f.write(text_)
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
