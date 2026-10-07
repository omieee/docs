# Claude state (cache only, max 20 lines)
Reflects omieee/docs @ 58c4ff8 · 2026-10-07 18:40 IST. Before a verdict, gate or plan change, read the canonical logs and outboxes.
- Plan: v3.3, master in plan/ (sha c4b4cf6d33a05be1). Week: W1, Oct 5-11.
- W1 done: LC20 D1 cold (open: D1 tests miss an unclosed-opener assert); Y2 baseline 0 solid / 6 shaky / 13 missing.
- W1 open: MC1 (clean 90-min block; Claude gives the change at minute 60), G1 in progress (PR #2 learning-go-sandbox: Add + test green; fix: package main to package integers, add a 2nd test case; Hello World and Iteration chapters still to do), R1 resume draft + Naukri/LinkedIn, L1, P1 Python prereqs then psycopg; NEW 155, 739.
- LC141 D14: FAIL then repaired 566dea4 (ChatGPT record); next 141 is D28 Oct 20.
- 19 D14 PASS Oct 7 (ChatGPT record). Colds due: 20 D3 Oct 7 · 143 D14 Oct 8 · 20 D7 Oct 11.
- Weak spots to aim at: context managers, pytest fixtures, dataclass == (teach at P1 start); why set lookup is O(1); iterators, generators, decorators; mutable examples (str, int).
- Operating model (Om approved Oct 5, plan text at next revision): owner = coach Om starts with; a miss is repaired on the spot by that coach; the other coach runs later retention (concept gaps to ChatGPT voice, code gaps to Claude); one-line packets UNIT | STATUS | EVIDENCE | GAP | ASK; one gate verdict from the gate owner; Sunday: Claude facts, ChatGPT voice check, one close.
- DSA rule (Om approved Oct 6, plan text pending): label NEW/DRILL/COLD first. COLD = approach + complexity first, problem-derived asserts, 10m Easy / 15m Medium + 5m verify, no interview. Miss: score once, record bug class, queue one repair for a later DSA slot (15m Easy / 20m Medium), never retry same session. Untaught = TEACHING GAP. Due colds beat repairs; repairs never take other tracks' hours. Read as DSA only until the plan says otherwise.
- Go second pass: Go in Action 2e (Om owns), contents and unit map in claude/resources/go-in-action-2e.md. LGWT stays primary. New recommendation until the plan names it.
