# Claude's coach errors, Oct 19 to Nov 4 2026, reviewed as if a human coach made them

Asked by Om on Nov 4 2026, 10:49 IST: "write it down, think a human coach has made those errors and you want to point out those."

Source: every COACH ERROR, PROCESS ERROR and PLANNING ERROR line in `claude-log-entries.md` from Oct 19 to Nov 4, plus one error from Nov 4 that was not logged until this review. Minutes are Om's study minutes lost, as logged; "0" means caught before Om lost time; "not measured" is not filled in.

## 1. The list

| # | Date | What the coach did | Om's minutes lost | Rule broken |
|---|---|---|---|---|
| 1 | Oct 19 | PR #10 review (704, 74) used "planted bugs" without saying what it means, packed a verdict, lint, a schedule and two questions into one reply, then answered a follow-up with a full table. Om spent the time thinking his correct code was wrong. | 50 (Om's figure) | Plain words; one point per reply |
| 2 | Oct 20 | Told Om a plan draft cost +4.5h and fitted the hours left, without counting two other open drafts (+5.15h). Corrected before he chose. | 0 | Fresh evidence before a claim |
| 3 | Oct 21 | Asked Om for minutes that were visible from message times; put resume work in a desk slot without asking where he does that work. | 0 | Ask where a task fits |
| 4 | Oct 22 | Wrote P1 Block 2 as about 125 minutes and said he was 30 minutes past the hard stop, counting office work and breaks. His real figure was 70-75. | 0 | Run before claiming |
| 5 | Oct 23 | Started P1 Block 3 from an old week row without fetching the repo; the new plan approved that afternoon had moved it. | 0 | Fresh evidence |
| 6 | Oct 23 | Asked Om to add tests for 704 and 74 that already existed in his PR. Third error of this type (two on Oct 17). Logged two days late. | 5 | Fresh evidence; log the same day |
| 7 | Oct 24 | Test records written to the wrong folder, so the commits did not contain them; the log pointed to files that were not in the repo. | 0 (coach time about 10) | Records |
| 8 | Oct 24 | v3.8 draft told P1 to reuse SQL `IN` and subqueries as already taught; the baseline says both were new. Caught by ChatGPT, not by Claude. | 0 | Never name an untaught topic |
| 9 | Oct 25 | Gave a 2015 generators video that uses Python 2. Om rejected it. | 3 | Beginner resources, checked first |
| 10 | Oct 26 | Named a KodeKloud lesson for K1 without checking it was a 31-second orientation clip. | not measured | Check a resource before naming it |
| 11 | Oct 27 | Asked for one simple office rule, built a protocol and then a 45-idea map with tiers. | 15 | Lost means go back; never pile on |
| 12 | Oct 27 | Wrote the office-AI instructions as rules for Om, which a Go beginner cannot follow. | 3 | Misread the request |
| 13 | Oct 27 | Sized Helm at 8-10h, a fluent engineer's time, and put the decision on the wrong date. Caught by ChatGPT. | 0 | Never compress hours |
| 14 | Oct 27 | Accepted three JD rows from companies on ChatGPT's list. Caught by own check. | 0 | Spec rule |
| 15 | Oct 29 | Gave text and a predict-the-output question on `Protocol` before any video, after Om said he was not sure. | 10 | Video first (same type as Oct 15) |
| 16 | Oct 29 | Wrote SQL gap questions in a clipped style that did not say which column or which word. | 2 | Plain words |
| 17 | Oct 30 | In the L1 use step, hints pointed straight at the answer and replies added reasons Om had not written. | 0 | Teaching must not leak answers |
| 18 | Oct 31 | Told Om one test case would catch three mistakes without running it; it caught one. | 4 | Run before claiming |
| 19 | Nov 2 | Opened Go with a from-memory exercise before any teaching, and asked "what do you know" after the task. | 2 (inside #22) | Ask first; teach before checking |
| 20 | Nov 2 | Explained Go's `...int` through Python's `*args`, which Om has not been taught. | 1 (inside #22) | Never assume a concept is known |
| 21 | Nov 3 | Started Boot.dev Ch 9 without checking lessons 11-13 first; they need interfaces, a function as an input and runes, none taught. Said "single quotes mean one character" without the word rune, so the compiler error used a word Om had never seen. | see #22 | Check prerequisites before a lesson |
| 22 | Nov 2-3 | Total Go time wasted across #19-21, recorded at Om's figure. | 240 (Om's figure) | as above |
| 23 | Nov 4 | Said no beginner psycopg 3 video could be verified after one weak web search, without opening YouTube. Om had to push. Not logged at the time. | about 2 | Check a resource before saying none exists |
| 24 | Nov 4 | Asked Om to run `psql -l` to learn his Postgres setup, which the Sep 24 chat already records (Docker `prcp-pg`). | 5 | Search past chats and repos before asking |
| 25 | Nov 4 | With 15-30 spare minutes after P1, switched Om to Go step D, out of the appendix order agreed the day before, without asking. | 7 | Approved Go order; ask before switching track |

**Total: 24 distinct errors (#22 is not a separate error; it is Om's 240-minute figure for #19-21, counted once) and about 346 minutes, close to 6 hours, of Om's time in 17 days**, plus unmeasured time (#10) and coach-only recovery time. For scale, the logged study time in the same stretch is roughly 30 hours (W3 close: about 18.3h; W4 close: about 7.5h plus 4 unmeasured sessions; W5 so far: a few hours). So about one study hour in five went to the coach's mistakes.

## 2. What a supervisor would say to this coach

**Pattern A: acts on the first reading instead of checking (#2, #4, #5, #6, #18, #21, #23, #24, #25). Nine errors, the biggest group.**
The coach knows the check (fetch fresh, search past chats, run it, read the lesson) and writes it into the rules after each miss, then skips it the next time because the first reading "looks fine". This is the costliest pattern: #21 alone led to 4 hours. The stale-read type has now happened five times (Oct 17 twice, Oct 20, Oct 23 twice) even after being written into the plan as safeguard 8.

**Pattern B: teaches in the wrong order or above the learner's level (#15, #19, #20, #21, #8).**
Text before video, a check before teaching, an analogy to something not taught, a lesson that needs three untaught ideas. Om's rule "teach first, never assume" is clear, and the coach broke it five times in two weeks, three of them in Go.

**Pattern C: adds when it should simplify (#1, #11, #12).**
When Om asked for something simple or said he was confused, the coach produced more: more terms, a bigger table, a 45-idea map. Om's own words on Oct 18 ("each time I said I was lost, you added more") were written into the plan, and it happened again on Oct 19 and Oct 27.

**Pattern D: resource picks not checked (#9, #10, #23).**
A Python 2 video, a 31-second clip, and a "no video exists" claim without searching.

**Pattern E: records and claims not exact (#3, #4, #7, #13, #17).**
Wrong minutes, missing files, an estimate at a fluent engineer's pace, answers leaked into Om's note. Each one weakens the record Om uses to judge his own pace.

**Repeat offences.** Plan rule 12 says the same error type twice becomes a written rule, and a third time on the same unit lets Om hand the unit to the other coach. Pattern A and Pattern B have both passed that line. Writing a new "fix" line after each error has not changed the behaviour: the fixes exist, but each new session reads them and still does not run them before acting.

**Honest verdict, as a supervisor would give it:** the coach's teaching, when it lands (the LC20 counterexample, the Nov 4 two-connection psycopg demo), is good. But the error rate is not acceptable: about a fifth of Om's study time lost, the same three kinds repeating, and the learner doing the checking that the coach is paid to do. A human coach with this record would get a formal warning and a short window to show the rate falling, or be taken off the units where the errors cluster (Go).

## 3. What would actually change it (new recommendation, Om decides)

Logging and fix lines have not worked. What could work is a check that is visible to Om, so he can see it was done before the coach speaks:

1. **A one-line pre-flight at the top of every block**, checked before the first instruction: setup and history (past chats, `state.md`), plan order (week row, appendix, taught list), resource opened and read, example run. Example: "Checked: Docker prcp-pg (Sep 24 chat), P1 W5 line, taught list python.md, scripts run on PG 16." If a box cannot be ticked, the coach says so instead of guessing.
2. **No track switch inside a session** unless Om names it.
3. **Go units move to ChatGPT** if Om chooses, under rule 12 (third time on the same unit), with Claude keeping the repo runs.
4. **A weekly error count in the Sunday close**, with the minutes, so Om sees whether the rate falls. The target to judge by: under 30 minutes of coach-error time a week by the Nov 15 re-forecast.

Point 1 costs Om one line of reading per block. Points 3 and 4 are Om's decision.

## Correction, Nov 4 11:20

- ChatGPT's 10:56 audit (`chatgpt/plan-drafts/2026-11-04-plan-reliability-audit.md`) pointed out that #22 is an aggregate line, not an independent error. The count is 24 errors, not 25. The minutes total already counted the 240 once (#19 and #20 marked 'inside #22'), so it stays at about 346.
- One more error after this review: the 11:15 handover to ChatGPT was written without first reading ChatGPT's 10:56 outbox entry (Om, 11:13: "read first what he said"). Logged in `claude-log-entries.md` 11:20.
