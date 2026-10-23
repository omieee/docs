# Phase 1 plan: master copy

The plan and its checker live here, and the same files are uploaded to both the Claude and ChatGPT projects. Approved by Om on 2026-10-05. Current: v3.7, approved by Om on 2026-10-23 (16:18 IST) after ChatGPT's review: equal coaches restored, international readiness inside the plan (parallel India and international searches from Gate B, target regions and a Gate B region decision, an international harvest slice, a data-infrastructure lane, one human live-coding mock, a four-line Gate C record). It carries the never-uploaded v3.6 draft (change 76) and replaces v3.5 (Oct 21 copy, sha256 `5e9a9bf242f47fc1`) in both projects. Draft, build scripts and negative tests: `claude/plan-drafts/` and `claude/plan-drafts/v3.7-build/`.

| File | sha256 (first 16) |
|---|---|
| `Phase1_Master_Plan_v3.7.md` | `31d6753c48138696` |
| `check_plan.py` | `2e9ca905775c4e27` |

- **Verify your project copy:** `sha256sum <file>` must match the table. Run `python3 check_plan.py Phase1_Master_Plan_v3.7.md`; it must print PASS (11 fragmentation warnings are expected and do not block).
- **Changing the plan:** a coach drafts the change (section 9), rebuilds with the generator in `claude/plan-drafts/v3.7-build/`, runs `check_plan.py` to PASS and the negative tests to FAIL as expected, and Om approves. The approved file is committed here first, with the table updated, then uploaded to both projects the same day.
- Old versions stay in git history; nothing older is kept as a separate file.
