# Claude state (cache only, max 20 lines)
Reflects omieee/docs @ 7b41029 + this commit · 2026-10-10 22:20 IST. Before a verdict, gate or plan change, read the canonical logs and outboxes.
- Plan: v3.3, master in plan/ (sha c4b4cf6d33a05be1). Week: W1, Oct 5-11.
- W1 done: Y2 baseline 0 solid / 6 shaky / 13 missing. Colds 20 D1, 141 D14 (FAIL, repaired), 19 D14, 20 D3, 143 D14 (PARTIAL). NEW 155 PARTIAL Oct 10 (PR #8 f17e69b). MC1, R1, L1, P1 not started. G1 PR #2 still at ae56955, open (4 fixes listed in Oct 10 11:10 log line).
- DSA 23 / 15. Repair queue: 155 space-saving push/pop rules, one fresh question, Claude, next DSA slot after Oct 11 colds, max 5 min.
- Due: Oct 11 20 D7 + 155 D1 (colds first), then the 155 repair. 155 D3 Oct 13, D7 Oct 17, D14 Oct 24, D28 Nov 7. 141 D28 Oct 20, 19 D28 Oct 21, 143 D28 Oct 22, 20 D14 Oct 18.
- Om pattern (155 interview): executes and traces right, leaves out the "why". Ask for the reason at every step.
- Oct 10: Sev 1 Oct 9 (zero day), on-call Oct 10-11; Om says W1-level hours are his normal week. Floor days per plan s9; never two zero days (Oct 10 has 155).
- MC1 slipped W0 and W1. Needs a named clean 90-min day in W2; never fragments.
- Capacity: plan assumes 15 hrs/week. W2 check Oct 18 (s5): under 10 avg since Oct 1 means re-forecast that Sunday. Asked Om for W1 actual hours incl. bedside, on-call/Sev frequency per month, cue time.
- W2 order once floor days end: W1 carry in row order (colds and repair queue, MC1, G1 rest, R1, L1, P1), then W2 row, capped at Om's real weekly hours.
- Weak spots to aim at: context managers, pytest fixtures, dataclass == (teach at P1 start); why set lookup is O(1); iterators, generators, decorators; mutable examples (str, int).
- Operating model (Om approved Oct 5): owner = coach Om starts with; misses repaired by that coach; other coach runs later retention; packets UNIT | STATUS | EVIDENCE | GAP | ASK; one gate verdict; Sunday: Claude facts, ChatGPT voice check, one close.
- DSA rule (Om approved Oct 6): label NEW/DRILL/COLD first. COLD = approach + complexity first, problem-derived asserts, 10m Easy / 15m Medium + 5m verify, no interview. Any miss (NEW or COLD): score once, teach, queue one repair for a later DSA slot. NEVER retry same session (Claude broke this Oct 10).
- Go second pass: Go in Action 2e (claude/resources/go-in-action-2e.md). Boot.dev Learn Go optional desk practice inside G hours. Both NEW RECOMMENDATION until the plan names them. Bedside no-audio map W1-W14: claude/resources/bedside-reading.md.
- Oct 1 items still open: cue time, gap diagnosis, office-Go result.
