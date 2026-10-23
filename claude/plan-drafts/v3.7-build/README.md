# v3.7 build scripts (draft, Claude, Oct 23 2026)

How the v3.7 week map and plan file are made, so either coach can rebuild them after a change. Run from this folder, with plain `python3` (not `-I`, or the local imports fail).

- `units.py`: every unit with its parts (hours, text, resources) and dependencies.
- `spec.py`: the week-by-week lane hours, gate weeks, rep and mock weeks. v3.7: one week added before Gate B (W68), Gate B W69, Gate C W73; W7 and W58 harvest +0.5h each; the human live-coding mock in W61 (`dsa_extra`).
- `gen.py`: fills each week from the lanes, adds DSA, proofs, campaign and practice sessions, and places retrieval reps by the continuity rule. `python3 gen.py --report` prints every week.
- `emit.py`: writes section 14's rows: `python3 emit.py sec14.md`.
- `build_plan.py`: assembles the plan from `plan/Phase1_Master_Plan_v3.5.md` plus the v3.6 edits, then `v37_edits.py` (the v3.7 layer) and `change77.md`: `python3 build_plan.py ../Phase1_Master_Plan_v3.7.md`.
- Check: `python3 ../check_plan_v3.7.py ../Phase1_Master_Plan_v3.7.md` must print PASS.
- Negative tests: `python3 negative_tests.py ../Phase1_Master_Plan_v3.7.md ../check_plan_v3.7.py` must print ALL NEGATIVE TESTS FAIL AS EXPECTED.

On Om's approval: copy `Phase1_Master_Plan_v3.7.md` and `check_plan_v3.7.py` (renamed `check_plan.py`) into `plan/`, update `plan/README.md` with both sha256 values, and Om uploads both files to both projects the same day.
