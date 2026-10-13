# Claude state (cache only, max 20 lines)
Reflects omieee/docs @ 2360086 + this commit · 2026-10-13 11:28 IST. Before a verdict, gate or plan change, read the canonical logs and outboxes.
- Plan: v3.3, master in plan/ (sha c4b4cf6d33a05be1). Week: W1 closing Oct 11 (proposed PARTIAL, ChatGPT spoken check pending); W2 Oct 12-18.
- W1 done: Y2 baseline 0 solid / 6 shaky / 13 missing. Colds 20 D1, 141 D14 (FAIL, repaired), 19 D14, 20 D3, 143 D14 (PARTIAL). NEW 155 PASS Oct 11 (PARTIAL Oct 10, repair correct). MC1, R1, L1, P1 not started. G1 PR #2 at 087baf3: code complete, planted bugs 5/5; left: G1 unit interview (Claude).
- DSA 23 / 16. Repair queue: empty.
- Oct 11: 20 D7 PARTIAL (ChatGPT; Claude PASS withdrawn, complexity missing). 155 D1 PASS (42c157e). 155 repair correct, NEW PASS. 155 D3 Oct 13, D7 Oct 17, D14 Oct 24, D28 Nov 7. 141 D28 Oct 20, 19 D28 Oct 21, 143 D28 Oct 22, 20 D14 Oct 18.
- Om pattern (155 interview): executes and traces right, leaves out the "why". Ask for the reason at every step. Om sends some submissions to both coaches: check the other log before any verdict.
- Oct 10: Sev 1 Oct 9 (zero day), on-call Oct 10-11; Om says W1-level hours are his normal week. Floor days per plan s9; never two zero days (Oct 10 has 155).
- MC1 slipped W0 and W1. Default day Sat Oct 17 (Om: no preference). Never fragments.
- Capacity: plan assumes 15 hrs/week. W2 check Oct 18 (s5): under 10 avg since Oct 1 means re-forecast that Sunday. Asked Om for W1 actual hours incl. bedside, on-call/Sev frequency per month, cue time.
- W2 scope (in phase1-log W1 close): colds 155 D3 Oct 13, 155 D7 Oct 17, 20 D14 Oct 18; NEW 739; MC1 on a named day; G1 close; R1; L1 1h; P1 prereqs. Rest slips to W3. Hours logging from W2 (proposed: [NNm] in commit messages, bedside minutes at Sunday close).
- Weak spots to aim at: context managers, pytest fixtures, dataclass == (teach at P1 start); why set lookup is O(1); iterators, generators, decorators; mutable examples (str, int).
- Operating model (Om approved Oct 5): owner = coach Om starts with; misses repaired by that coach; other coach runs later retention; packets UNIT | STATUS | EVIDENCE | GAP | ASK; one gate verdict; Sunday: Claude facts, ChatGPT voice check, one close.
- DSA rule (Om approved Oct 6): label NEW/DRILL/COLD first. COLD = approach + complexity first, problem-derived asserts, 10m Easy / 15m Medium + 5m verify, no interview. Any miss (NEW or COLD): score once, teach, queue one repair for a later DSA slot. NEVER retry same session (Claude broke this Oct 10).
- Go second pass: Go in Action 2e (claude/resources/go-in-action-2e.md). Boot.dev Learn Go optional desk practice inside G hours. Both NEW RECOMMENDATION until the plan names them. Bedside no-audio map W1-W14: claude/resources/bedside-reading.md.
- Oct 1 items still open: cue time (Om Oct 13: discuss later; agenda for the Oct 18 close, do not re-ask before; W1 commits cluster 16:39-18:38 IST on 5 days), gap diagnosis, office-Go result. On-call now ~1 weekday/month, ~2 weekends/year.
