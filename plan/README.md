# Phase 1 plan: master copy

The plan and its checker live here, and the same files are uploaded to both the Claude and ChatGPT projects. Approved by Om on 2026-10-05. Current: **v3.9**, approved by Om on 2026-11-15 (19:10 IST: "lets create final plan now and will freeze that"). It is the Nov 15 re-forecast, built by Claude and verified twice by ChatGPT the same day: dates at 12 hours a week with slower-pace illustrations, no scope shrink, warm-ups funded, Go on the Learning Go 2e order, Kubernetes on the KodeKloud course order, P1 re-sized against PRCP PR #11, release evidence (E1), the finalizer fix, a distributed-systems proof (DS1), recognition-first DSA, dated DSA reviews, short-week rules with a W7-W12 run sheet, token rules, and a four-line Gate A record. Gates: A Jun 6 2027, B Apr 30 2028, C May 28 2028; 969 scheduled hours, 87 weeks. It replaces v3.8 (sha256 `25bb309e79a610f2`) in both projects. Build scripts, negative tests and notes: `claude/plan-drafts/v3.9-build/`, `claude/plan-drafts/2026-11-15-v3.9-r2-build-note.md` and `claude/plan-drafts/2026-11-15-v3.9-final-note.md`.

| File | sha256 (first 16) |
|---|---|
| `Phase1_Master_Plan_v3.9.md` | `5301551d30cee7b9` |
| `check_plan.py` | `ad0d3efdbe10444b` |

- **Verify your project copy:** `sha256sum <file>` must match the table. Run `python3 check_plan.py Phase1_Master_Plan_v3.9.md`; it must print PASS (14 fragmentation warnings are expected and do not block).
- **Changing the plan:** frozen until the Dec 6 2026 re-forecast, then between monthly re-forecasts, except for the three triggers in section 9 (an untaught prerequisite blocking this week's work, repeated failed learning on one unit, a real market change with dated evidence). One coach drafts the change (section 9) and the other verifies it; whoever edits rebuilds with the generator in `claude/plan-drafts/v3.9-build/`, runs `check_plan.py` to PASS and the negative tests to FAIL as expected, and Om approves. The approved file is committed here first, with the table updated, then uploaded to both projects the same day. Coach research and rebuilds run outside Om's study block.
- Old versions stay in git history; nothing older is kept as a separate file here (`claude/plan-drafts/` keeps the v3.8 copy that the negative tests read).
