# Proposal: weekly machine coding practice plus a monthly timed test

- Status: PROPOSAL, not plan content. Om's idea (Oct 20, 23:12 and 23:16 IST), thought through by Claude. Om decides; ChatGPT asked to challenge it (up to 5 findings) before the Sun Oct 25 close.
- Label: IDEA (Om) plus GAP (MC1 evidence). Section 9 format at the end.

## 1. Om's idea, in his words

- 23:12: "each week one question practice start with easy in 6 month i will kill all ... question"
- 23:16: "these wont be 90 minutes only basic ones lets target 60 min bits of learning-doing kind of activity rather first doing-then learning ... every time a problem that is concentrating on one part .. you have to devise a proper problem for that .. or we can keep 1 day per week for this machine coding practice and real test will be 1 question per month like this snake and ladder one"

## 2. Why this is a good idea (evidence, not opinion)

1. MC1 (Oct 20) failed for reasons that are skills, not knowledge of the problem: about 60 of 90 minutes went into reading input by trial and error; the loop decided before checking every item (MC1 `else` overwrite, then `return` on the first non-match in the review code); the player's position had no single owner; no tests; no thin working version at any point (claude/tests/lld/2026-10-20-MC1-snake-and-ladder.md; chatgpt/tests/lld/2026-10-20-MC1-guided-review-diagnosis.md).
2. Skills like these improve with many short repetitions, not with one long attempt every few months. In v3.4 the next timed rep (MC2) is W14 (Jan 4), 11 weeks away, and MC2 to MC3 is another 14 weeks. The gaps found on Oct 20 would sit unused for months.
3. The same habits feed other tracks: looking at every item before deciding (DSA, PRCP repositories), one owner of state (PRCP, Go agent), tests from the rules (every track).
4. Machine coding is in the plan's never-cut list, and the plan's own loop table shows it decides at build-round companies (Flipkart SDE3 machine coding round; Razorpay machine coding with a new requirement mid-session; Nutanix thread-safe job scheduler). Gate B needs the latest two reps to pass at 8/12 (7/10 under the Oct 20 rule); today's score is 2/10.

## 3. What one weekly practice session looks like (60 minutes, learn then do)

| Minutes | Step | What happens |
| --- | --- | --- |
| 0-5 | Name it | Coach names the ONE skill and shows the MC1 line where it went wrong |
| 5-15 | Learn | One idea, one tiny runnable example Om runs, one counterexample that breaks the wrong idea (s0 safeguard 4) |
| 15-50 | Do | A small problem built for that one skill only. Hard-coded data, no input reading unless input is the skill. Om writes the code and 2-3 asserts. No AI |
| 50-60 | Check | Om pushes. Coach runs the asserts fresh and makes 1-2 deliberate mistakes in a copy to see if the asserts catch them. One finding, one "why" question. Save line |

Rules:
- Low stakes: no 0-10 score. The result is "skill shown" or "not yet", with the commit and [NNm] logged. "Not yet" means the same skill again next week with a NEW problem, never the same one.
- Box 60, hard stop 90 (safeguard 6). Unfinished = save line.
- Coach designs a fresh problem for each session. Never a planned rep problem, never a workat.tech editorial.
- One fixed day a week, Om's choice. Om's usual office days are Mon, Wed and Fri, so Tue, Thu or Sat fits better.
- Claude runs these by default (repo work, and Claude leads the next MC repair block under Om's Oct 18 rule). ChatGPT can take any session Om gives it; the coach who runs it logs it.

## 4. The first eight sessions (each one isolates one MC1 gap)

| # | Skill | MC1 evidence | Practice problem (designed fresh, small) | What the asserts must prove |
| --- | --- | --- | --- | --- |
| 1 | Look at every item before deciding | `else` overwrote earlier snake matches; review code returned on the first non-match | Shop discount rules: a list of (minimum bill, discount); find the best discount for a bill, and the first rule for a category | The match is the 2nd item; the match is the last item; no match at all |
| 2 | Read counted input with one moving pointer | ~60 min on input; review parser read 6 of 8 ladders | School timetable input: N teachers, M rooms, K classes, each section after its count. Read exactly the counted lines, no empty-line trick | Counts are right (N, M, K), the last item of each section is right, works when a section count is 0 |
| 3 | Make random things testable | No tests; could not test dice | Coin-toss race for two players: heads +1, tails +2, first to 10. The tosses are passed in as a list | A fixed toss list gives a known winner; overshoot rule; turn order |
| 4 | One owner of state | Review code moved the player twice | Wallet transfers: `transfer()` either returns new balances or changes the wallets. Pick one and write it in the docstring | Returned value and stored value agree after a transfer, a failed transfer and two transfers in a row |
| 5 | Thin working version first | No running version at any minute of the 90 | Ticket counter queue: people arrive and are served in order; one event printed by minute 10, then add the rules | A commit by minute 20 that runs and prints; final asserts on the order of service |
| 6 | Who owns which behaviour (uses L1) | Rules sat in loose functions in main.py; Snake and Ladder files empty | Coach gives a 40-line script; Om moves it into 2-3 classes, each owning its own rules | Same output before and after; each rule lives in one class |
| 7 | Absorb a change in one place | Minute-60 change not started | Taxi fare calculator; at minute 35 a new rule arrives (night charge) | New rule tested; nothing outside the pricing part changed |
| 8 | Dress rehearsal, all skills together | Whole MC1 | A tiny vending machine, 60 min, full flow at small size | Runs end to end on fixed data; 3 asserts; one change absorbed |

After session 8 the slot follows a simple loop: each monthly test's weakest rubric part chooses the next month's weekly sessions. In weeks where L2, L3 or L4 run, that unit's kata IS the weekly session (same hours, no extra cost).

## 5. The monthly timed test

- Same as MC1: 90 minutes, no AI, notes committed before code, a new requirement at minute 60, Claude invigilates and gives one verdict on the s7 rubric, then a 60-min review.
- The six named reps in s6.5 stay, in order (Splitwise, in-memory datastore, key-value store with TTL or job scheduler, reservation AI-assisted, cab or gym booking). Extra monthly tests in between use other workat.tech practice problems (problem page only).
- Spacing about every 4-5 weeks instead of v3.4's W3, W14, W28, W29, W30, W50. First monthly test after session 8, around W9-W10 (early December): MC2 Splitwise moves there from W14.
- Gate bars unchanged: Gate A reps 1 and 2 scored; Gate B latest two pass; Gate C 6 reps minimum.

## 6. Cost and how to fund it

Rough estimate, before a check_plan rebuild (12-hour normal weeks; light weeks W5, W12, W13 and gate weeks skipped; L-unit kata weeks cost nothing extra):

| Version | Weekly practice | Monthly tests | Extra hours | Effect |
| --- | --- | --- | --- | --- |
| Full (Om's idea) | 1h every normal week to W47 | about every 4-5 weeks, about 11 reps in total instead of 6 | about +35h | about 25h over the 575 ceiling; gates about 3 weeks later |
| Lighter | 1h weekly to Gate A, then every 2 weeks | about every 6 weeks, about 9 reps | about +20h | about 10h over the ceiling; gates about 2 weeks later |

Only 9.5h are left under the 575 ceiling, so either version needs Om's call: raise the ceiling, or let the gates move (Om's stated principle: scope first, honest effort second, calendar last). Nothing on the never-cut list is touched.

## 7. Recommendation: pilot first, amend with real numbers

1. **Now, no plan edit:** sessions 1-4 run in W4, W6, W7 and W8 (W5 is the Diwali light week), 1h each, as MC1's repair. The plan allows a unit that runs long to take its time from contingency (s5), so 4h come from contingency (48 left on Oct 18, before this week's coach-error minutes).
2. **Nov 15 re-forecast (already scheduled):** with the pilot's logged minutes and "skill shown / not yet" results, Claude drafts the s9 amendment (full or lighter, Om picks), rebuilds the week map, check_plan must PASS, Om uploads to both projects.
3. If the pilot shows the sessions do not move the skills, drop the idea at Nov 15 with that evidence.

## 8. Section 9 summary

- What: a 1h weekly learn-then-do machine coding practice on one skill at a time, plus a monthly 90-min timed test; pilot of 4 sessions first.
- Why: MC1 diagnostic FAIL 2/10 on execution skills; next timed rep 11 weeks away; Gate B needs the latest two reps to pass.
- Evidence: MC1 record and run (d78048e), ChatGPT review diagnosis (56ac481), s3 loop table, s6.5 rep spacing.
- Time cost: pilot 4h from contingency; full about +35h or lighter about +20h, exact figure from the Nov 15 rebuild.
- What is removed: nothing; the calendar moves or Om raises the ceiling.
- Risk reduced: repeating MC1's failures at MC2 and beyond; Gate B rep bar missed; the same loop and state habits leaking into DSA and PRCP work.
- Open risk: 12-hour weeks are already full; if logged hours show Om cannot sustain the extra hour, the lighter version or a later start is the fallback.
