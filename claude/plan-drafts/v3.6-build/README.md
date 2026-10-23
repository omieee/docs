# v3.6 build scripts (draft, Claude, Oct 23 2026)

How the v3.6 week map and plan file were made, so any coach can rebuild them after a change. Run from this folder.

- `units.py`: every unit with its parts (hours, text, resources) and dependencies.
- `spec.py`: the week-by-week lane hours, gate weeks, rep and mock weeks.
- `gen.py`: fills each week from the lanes, adds DSA, proofs, campaign and practice sessions, and places retrieval reps by the continuity rule. `python3 gen.py --report` prints every week.
- `emit.py`: writes section 14's rows: `python3 emit.py sec14.md`.
- `build_plan.py`: assembles the plan from v3.5 plus the edited sections: `python3 build_plan.py ../Phase1_Master_Plan_v3.6.md`.
- Check: `python3 ../check_plan_v3.6.py ../Phase1_Master_Plan_v3.6.md` must print PASS.

On Om's approval: copy `Phase1_Master_Plan_v3.6.md` and `check_plan_v3.6.py` (renamed `check_plan.py`) into `plan/`, update `plan/README.md` with both sha256 values, and upload both files to both projects the same day.
