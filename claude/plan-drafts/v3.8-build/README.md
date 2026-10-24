# v3.8 build scripts (draft, Claude, Oct 24 2026)

How the v3.8 week map and plan file are made, so either coach can rebuild them after a change. Run from this folder, with plain `python3` (not `-I`, or the local imports fail).

- `units.py`: every unit with its parts (hours, text, resources) and dependencies. v3.8: each teaching part ends with its **Use in** step; K3 depends on D1.
- `spec.py`: the week-by-week lane hours, gate weeks, rep and mock weeks. v3.8: a second week before Gate B (W69), Gate B W70, Gate C W74; Go +0.25h in W12-W25 and LLD +0.25h in W8, W9, W10, W11 and W13.
- `gen.py`: fills each week from the lanes, adds DSA, proofs, campaign and practice sessions, and places retrieval reps by the continuity rule. v3.8: D1 right after P1; P3, P4 and S5 before Y3's last four topics; R2 split so the first stories are told in W10; the Go rep text names no untaught tool. `python3 gen.py --report` prints every week.
- `emit.py`: writes section 14's rows: `python3 emit.py sec14.md`.
- `build_plan.py`: assembles the plan from `base/Phase1_Master_Plan_v3.5.md` (sha256 `5e9a9bf242f47fc1`) plus the v3.6 edits, `v37_edits.py`, `change77.md`, then `v38_edits.py` and `change78.md`: `python3 build_plan.py ../Phase1_Master_Plan_v3.8.md`.
- Check: `python3 ../check_plan_v3.8.py ../Phase1_Master_Plan_v3.8.md` must print PASS. The v3.7 checker also passes v3.8; the v3.8 checker fails v3.7 on its new rules, as it should.
- Negative tests: `python3 negative_tests.py ../Phase1_Master_Plan_v3.8.md ../check_plan_v3.8.py` must print ALL NEGATIVE TESTS FAIL AS EXPECTED.

On Om's approval: copy `Phase1_Master_Plan_v3.8.md` and `check_plan_v3.8.py` (renamed `check_plan.py`) into `plan/`, update `plan/README.md` with both sha256 values, and Om uploads both files to both projects the same day.
