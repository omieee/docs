# v3.7 audit: does the plan fit how a human remembers? (Claude, 2026-10-24)

Proposal only. No plan edit. Om decides each finding; an approved one goes through section 9 and a generator rebuild with `check_plan.py` PASS.

**Trigger.** Om, Oct 24 12:04, after Go retrieval rep 1 slipped on syntax (`t *testing.T`, `strings.Builder`) after 11 idle days: the plan gives DSA a full spaced-review system and almost nothing else; "verify the plan for a human". Claude drafted v3.3 to v3.5 and the v3.6 and v3.7 builds, so these misses are Claude's (logged in `claude-log-entries.md`, Oct 24 12:08).

**The root, in the plan's own words (section 7, Cadence):** "Each skill is tested at four points only: baseline, milestone, gate, and the day 7 and day 28 retention checks after a gate ... DSA alone keeps continuous spaced review." The section 6.12 gap rule only stops a whole track going idle; it does not stop one concept going cold inside a track that is busy with other concepts.

## Evidence from the v3.7 week map (section 14)

| Concept | Learned | Next time the map touches it | Gap |
|---|---|---|---|
| Go syntax (G1) | Oct 11-13 | RR Oct 24 (done early), then G2 W5 | 11 days: syntax lost, method kept (PR #3 `75d2507`) |
| Generators, `yield` | yield fixtures Oct 23; Y3 part 1 W4 | Y3 "Generators, rest" W16 (Jan 18) | about 12 weeks |
| SQL taught on Sep 27 (IN, CASE, subqueries, UNION needed hints) | Sep 27 | P2 SQL correction W16 (Jan 18); P1 W5-W8 uses only basic insert and select | about 16 weeks |
| Stories told aloud | first written W6 | first "tell each story aloud" W23 (Mar 8) | calibration interviews run every week from W5 (Nov 2) with stories never spoken |
| Untaught items named in a row | W4 RR line: "table-driven test", `go test -race` | G1 used only `t.Run` subtests; the race flag was run by the coach | wording error, found Oct 24 |

DSA, by contrast: 144.25 of 820.75 hours, and every problem re-solved at days 1, 3, 7, 14, 28 and 90.

Research the plan already cites (section 6.12): retrieval practice beats re-reading (Roediger and Karpicke, 2006); spacing holds knowledge best (Cepeda and others, 2008); skills not used decay (Arthur and others, 1998).

## Findings

**F1. BUG: no spaced recall for anything except DSA.**
- What: every desk session of a non-DSA lane (Python, PRCP, Go, Kubernetes, LLD, HLD, SQL, later operators and cloud) opens with a 5-minute warm-up. Om writes the previous session's core snippet, or answers two short questions, from a blank page with no notes and no AI. The result is "held" or "slipped: <what>", with no score, logged in one line. A slip is fixed in that same session, because it is that session's own material.
- Why: it gives each concept a recall about a week after it is learned, and again every time the lane meets, which is the spacing DSA already gets.
- Evidence: the table above, and today's Go rep.
- Time cost: 336 lane-sessions from W4 (4.8 a week on average) at 5 to 8 minutes, which is 28 to 45 hours.
- Removed or moved: first a measured trial in W4 and W5, about 50 minutes, paid from W4's 1.75 freed hours (P1's 1 hour and the RR's 0.75 hours were done early on Oct 23 and 24), so no date moves. At the Nov 15 re-forecast, the logged minutes set the real cost. Om then chooses: the gates move by about 2.5 to 4 weeks, or a named source pays for it (for example the 12 hours of DSA day-90 re-solves), or the warm-up runs every other session.
- Risk reduced: learning a topic, passing it, and losing it before the gate or the interview.

**F2. IDEA: bedside cards become the scheduled second layer (0 desk hours).**
- What: when a unit closes, the coach commits 5 to 8 answer-first cards (a question, and below it the answer or a small snippet) to `claude/cards/<track>/`. Om reads them on his phone in bedside time on day 1, day 7 and day 28 after the unit closes. He tries each answer before scrolling down. Unread cards still create no debt and block nothing, as in section 6.12.
- Why: Om has daily phone-only, dark-room time and wants to use it for learning. Some of these slots allow reading only, which suits cards.
- Evidence: Om's routine (stated Oct 10 and Oct 13), and the retrieval research above.
- Time cost: 0 Om desk hours; coach time only.
- Removed or moved: nothing.
- Risk reduced: concepts between lane sessions, and syntax such as today's.

**F3. GAP: the next units do not ask Om to reuse what he just learned (0 hours).**
- What: write the reuse into the rows. P1 W5-W8: the rollback tests use a `yield` fixture, and transactions use `with`. At least one repository query uses `IN` and one uses a subquery, both taught Sep 27. G2 W5: the first file is written with `t *testing.T` and a `strings.Builder` from a blank file, as the RR slip already requires.
- Why: using a concept in real work is the cheapest review there is. Today it happens only by luck.
- Evidence: the generators and SQL rows above.
- Time cost: 0 hours, since these are the natural ways to do those tasks.
- Removed or moved: nothing.
- Risk reduced: the 12-week and 16-week gaps above.

**F4. BUG: rows can name things that were never taught (0 hours).**
- What: (a) the RR template in `build_plan.py` changes to "rewrite one closed kata and its tests as that unit wrote them, add one changed case", which drops "table-driven" and `-race` until the units that teach them. (b) At each rebuild, the coach lists every tool, flag and term named in the next 4 weeks of rows and confirms each was taught before it is used, recorded in the build note.
- Why: safeguard 2 ("plan line only") cannot protect Om if the plan line itself names something untaught.
- Evidence: the W4 RR line.
- Time cost: 0 hours.
- Removed or moved: nothing.
- Risk reduced: untaught material tested as if it were known, which is the same class as the pytest error of Oct 18.

**F5. GAP: stories are first spoken in March, but calibration interviews start in November (0 hours net).**
- What: move R2's first "tell each story aloud" hour from W23 to the week after the first stories are written (about W8). Run it as a spoken check by ChatGPT in voice mode. A writing hour takes W23's place, which keeps R2's total the same; the generator places it.
- Why: telling a story aloud is a spoken skill, and it is tested at every calibration interview from W5.
- Evidence: the R2 and Campaign rows (W5 to W23).
- Time cost: 0 hours net.
- Removed or moved: nothing removed; one hour swapped between W8 and W23.
- Risk reduced: spending calibration interviews on stories that were never rehearsed.

## Not proposed

- Reopening whether DSA stays. That is settled with evidence (section 6.6), and it is not what this audit is about. F1 names DSA's day-90 hours only as one possible way to pay for the warm-ups; Om decides.
