# Phase 1 plan: master copy

The plan and its checker live here, and the same files are uploaded to both the Claude and ChatGPT projects. Approved by Om on 2026-10-05. Current: v3.5, Oct 21 copy. Committed by Claude on 2026-10-20 after Om approved it in chat (unseen DSA sets in W24 and W48, the pattern-signal question, safeguard 13), then updated on 2026-10-21 with Om's Oct 20-21 decisions from other chats (change 75: machine coding practice trial, scoring when concurrency is not asked, two coach rules). It replaces the Oct 20 copy (sha256 `3aa6efedf5d2ae9e`) in both projects.

| File | sha256 (first 16) |
|---|---|
| `Phase1_Master_Plan_v3.5.md` | `5e9a9bf242f47fc1` |
| `check_plan.py` | `a79087bb8dcf039d` |

- **Verify your project copy:** `sha256sum <file>` must match the table. Run `python3 check_plan.py Phase1_Master_Plan_v3.5.md`; it must print PASS.
- **Changing the plan:** a coach drafts the change (section 9), runs `check_plan.py` to PASS, and Om approves. The approved file is committed here first, with the table updated, then uploaded to both projects the same day.
- Old versions stay in git history; nothing older is kept as a separate file.
