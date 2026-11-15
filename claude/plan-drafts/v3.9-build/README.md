# v3.9 build scripts (draft, Claude, Nov 15 2026)

v3.9 is the Nov 15 2026 re-forecast, built on v3.8's scripts. Om's instruction (Nov 15, 13:14 IST): one coach builds, the other verifies. Claude built it; ChatGPT verifies. Run from this folder with plain `python3` (not `-I`, or the local imports fail).

- `units.py`: v3.9 changes G2-G7 (Learning Go 2e order, G2 at the measured pace), K1-K5 and K7a (KodeKloud CKA course order, hours unchanged), A2, OP1, OP4, OP5, OP6, H3 (scale ADR), Y6 and Y7b text, and the new DS1 (distributed-systems proof).
- `spec.py`: v3.8's content weeks in the same order, plus `K1_INS = 3` weeks before Gate A and `K2_INS = 6` before the two Gate B repair weeks; light weeks stay on their calendar dates; CL3 in four whole 3-hour sessions after K6b (W54); Naukri placed by date in W31.
- `gen.py`: W4-W6 are done rows at plan hours (from `phase1-log.md` and both coach logs), each lane starts past them; a lane whose next unit waits for a prerequisite gives its hours to the PY lane that week; warm-ups funded inside "Proofs and weekly close" from W7 (0.5h normal, 0.25h light, none in gate weeks or 1c). `python3 gen.py --report` prints every week.
- `emit.py`: `python3 emit.py sec14.md` (week notes remapped to v3.9 weeks).
- `sec04_05.md`, `sec06.md`, `sec14_head.md`: sections 4, 5, 6 and the section 14 intro, edited in place.
- `build_plan.py`: v3.5 base, then the v3.6 to v3.8 layers, then `v39_edits.py` (sections 0, 1, 7, 8, 9, 11, 13): `python3 build_plan.py ../Phase1_Master_Plan_v3.9.md`.
- Check: `python3 ../check_plan_v3.9.py ../Phase1_Master_Plan_v3.9.md` must print PASS (17 fragmentation warnings are expected: 15-minute tails of parts that started earlier). The v3.9 checker fails v3.8 on the bugs v3.9 fixes (MC2 before L3 ends, CL3 before K6b, CL3 in slivers) and on its new presence rules, as it should. The v3.8 checker fails v3.9 only on the done W5 G2 row, which the v3.9 checker exempts.
- Negative tests: `python3 negative_tests.py ../Phase1_Master_Plan_v3.9.md ../check_plan_v3.9.py` must print ALL NEGATIVE TESTS FAIL AS EXPECTED (31 mutations, plus a check that the unmodified plan passes).

On Om's approval: copy `Phase1_Master_Plan_v3.9.md` and `check_plan_v3.9.py` (renamed `check_plan.py`) into `plan/`, update `plan/README.md` with both sha256 values, and Om uploads both files to both projects the same day.
