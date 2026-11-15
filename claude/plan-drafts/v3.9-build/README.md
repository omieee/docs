# v3.9 build scripts (final, approved by Om Nov 15 2026; Claude)

v3.9 is the Nov 15 2026 re-forecast, built on v3.8's scripts. Om's instruction (Nov 15, 13:14 IST): one coach builds, the other verifies. Claude built it; ChatGPT verified it (`chatgpt/outbox.md`, 14:54) and proposed five changes (`chatgpt/plan-drafts/2026-11-15-v3.9-execution-proposal.md`, `05b3735`). Revision 2 fixes the five bugs and carries the accepted and modified proposals; the decisions and the before-and-after numbers are in `../2026-11-15-v3.9-r2-build-note.md`. Run from this folder with plain `python3` (not `-I`, or the local imports fail).

## Build, in this order

1. `python3 emit.py sec14.md` (the week rows, from `gen.py`).
2. `python3 scenarios.py runsheet > runsheet.md` (the W7-W12 run sheet, r2).
3. `python3 build_plan.py ../Phase1_Master_Plan_v3.9.md` (v3.5 base, the v3.6 to v3.8 layers, then `v39_edits.py`; sections 4-6 and 14 come from the `sec*.md` files and `runsheet.md`).
4. `python3 ../check_plan_v3.9.py ../Phase1_Master_Plan_v3.9.md` must print PASS (14 fragmentation warnings are expected: 15-minute tails of parts that started earlier).
5. `python3 negative_tests.py ../Phase1_Master_Plan_v3.9.md ../check_plan_v3.9.py` must print ALL NEGATIVE TESTS FAIL AS EXPECTED (57 mutations, plus a check that the unmodified plan passes; 4 are new in the final revision).
6. `python3 ../check_plan_v3.9.py ../Phase1_Master_Plan_v3.8.md` must FAIL (the v3.8 copy kept in `claude/plan-drafts/`, sha256 `25bb309e79a610f2`, the same as the one approved on Oct 24): MC2 before L3 ends, CL3 before K6b, CL3 in slivers, the missing v3.9 rules, plus the r2 and final rules (E1 missing, P4 and K7a not before Gate A, the missing week-reference sentences, the run sheet, the hiring dates, the Gate A record).

## Files

- `units.py`: every unit and its parts. r2: P1's remaining work split into two parts sized against PRCP PR #11 (+6h); E1, release evidence and the gate endpoint (7.5h); C1's missing-probe case (+0.5h); G2's loops and control part (+3h) and the Builder drill dropped (-0.25h); K1's kubelet line; Y6's property; H3 and O1 numbers; A3 names the release.
- `spec.py`: the week spec. r2: `K1_INS = 5`, `K2_INS = 7`; the dated DSA reviews (`REVIEWS`, from the tracker in `phase1-log.md`); harvest part 1 in W7 and part 2 in W8; MC2 in W22; the added weeks before Gate A carry Kubernetes too; the CL3, K6b and K-hold weeks kept relative to `K1_INS`.
- `gen.py`: the lanes. r2: dated reviews first in their week; in 1a the Go and Kubernetes lanes stop at their first 1b unit (A1, K6a); the Gate A week starts no new unit; DS1 counts as Go and HLD contact (it is Go code on Maelstrom); E1 runs in the Python lane right after S5. `python3 gen.py --report` prints every week.
- `scenarios.py`: `runsheet` (the short-week replay, with the hand-written first block and proof of each week, checked against the rows) and `dates` (available-time scenarios at 14, 12, 9 and 6 hours).
- `facts.py`: prints the numbers the text quotes (totals, phase hours, gate weeks, the weeks of the unseen sets, blind sets, Naukri, mocks and so on), straight from the build.
- `gate_cases.py <PRCP src>`: runs PRCP's `decide()` on the seven release-evidence cases of section 6.1, today and with a reference evidence step. Checked on PRCP PR #11 at `ae974b0`: ALL CASES MATCH.
- `sec04_05.md`, `sec06.md`, `sec14_head.md`, `sec14_tail.md`: sections 4, 5, 6 and the section 14 text, edited in place.
- `negative_tests.py`: 57 mutations, 22 new in r2 and 4 in the final revision. A case may change all occurrences or apply several replacements in turn.

Promoted to `plan/` on Nov 15 2026 after Om's approval (19:10): `plan/Phase1_Master_Plan_v3.9.md` and `plan/check_plan.py` (this folder's `check_plan_v3.9.py`), sha256 in `plan/README.md`. Om uploads both files to both projects the same day.
