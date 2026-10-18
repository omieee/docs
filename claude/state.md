# Claude state (cache only, max 20 lines)
Reflects omieee/docs @ 898f4ae + this commit · 2026-10-18 22:50 IST. Before a verdict, gate or plan change, read the canonical logs and outboxes.
- Plan: v3.3, master in plan/. W2 closed PARTIAL (proposed, phase1-log); ChatGPT spoken check for W1 and W2 still pending. W3 = Oct 19-25.
- CAPACITY (Oct 18): Om picked 12h weeks. v3.4 FINAL DRAFT 22:50 (ChatGPT's 3 fixes, pytest basics +1.5h, 12 coach safeguards in s0): claude/plan-drafts/ sha a8717a0d890e199b, check_plan PASS, 52 weeks, 565.5h, gates Mar 21, Sep 5, Sep 26 2027. PENDING Om's upload to both projects; then commit to plan/ with README hashes.
- v3.4 contents: 12/7/9 caps, W1-W2 as done, R1 (LinkedIn now, Naukri W22, no Premium), cue 10:30, DSA session rule s6.6 #11, two-coach model + per-block minutes in s0, office-Go FAIL in s10, Phase 2 dates follow Gate C.
- DSA 24 / 17. 20 D14 PASS Oct 18 (7d3c30e, assert fix 291dfad). Due: 739 D7 and 141 D28 Oct 20 (one may slide a day under the cap), 19 D28 Oct 21, 143 D28 Oct 22, 155 D14 Oct 24, 20 D28 Nov 1. Carried: binary search lessons 14-15, NEW 704.
- DSA rule APPROVED Oct 18: 45 min a day max, one item per session, clock paused on interruptions; a miss: teach in a separate later slot, retry in another. Label NEW/DRILL/COLD first. Never same-session retry.
- Om pattern (155, 739): executes and traces right, leaves out the "why"; asserts miss the one case that isolates a bug (20: "(])"). Ask for the reason and the isolating case.
- MC1: NOT Mon Oct 19 (Om, Oct 18 23:05). Plan GAP: no lesson on how a machine coding round runs; method lesson first (s9 GAP ~1.5h, pending Om), then MC1 inside W3, 90 min timed, no AI, "60" at minute 60, raw notes first. Ask Om first: ever sat one? Never fragments. Never the S&L editorial before the rep.
- Cue 10:30 AM daily (Om to calendar it). Office 1-2 days a week from now; Om flags short days.
- P1 prereqs: Block 1 PASS Oct 17 (PR #1 7b450d4, merged c39ca00). Block 2 RESTART from zero (Oct 18 coach error, Om had never seen pytest): step 1 what pytest is, step 2 fixture with return, step 3 fixture with yield; one runnable example each; nothing beyond the plan line (no xfail, no tricks). Resource PCC 3e ch 11. Then Block 3 (dataclass ==), then psycopg.
- Open PRs to merge (all passed): dsa-python #9, learning-go-sandbox #2, learning-python-sandbox #1.
- R1: resume v1 draft (975886e6) blanks for Om; LinkedIn live in October; Naukri later.
- Office-Go test FAIL (Oct 18): no Go work, AI writes what comes. Go = study track only. Office Go counts only via the office proof path, never AI-written.
- Gap diagnosis: Claude drafted "no fixed cue or protected slot, time set by son and office; fix = 10:30 cue + minutes logged per block"; Om's yes pending.
- Contingency: 2 used (laptop), 48 left.
- Token rule (Om, Oct 18): use the docs token only with Om's explicit OK each time. Ask when stuck.
- Own process rules: follow the 12 s0 coach safeguards (v3.4) every session; plant bugs with PYTHONDONTWRITEBYTECODE=1; check IST time with the clock tool before any timestamp.
- Operating model: owner = coach Om starts with; misses repaired by that coach; packets UNIT | STATUS | EVIDENCE | GAP | ASK; one gate verdict.
