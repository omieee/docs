# Proposal: close the concept-recall gap in v3.9

**Status: NEW RECOMMENDATION. Om decides. No master-plan amendment or learner verdict.**
Revision 2, 2026-11-23. Replaces the earlier draft's estimates and scheduling details. Five findings in section 9 format. This is coach work; no learner minutes are inferred from this review.

**Decision:** Separate problem counts from retention. An uncounted exercise still teaches something that must be recalled. Give every named taught mechanism a dated, funded recall path, and allow existing independent work to satisfy that path only when the exact mechanism was checked.

## Evidence and limits

Fresh docs snapshot: `dc651bd1b0a03829cf6f773d48fdc3c78d3a55ae`. Read sections 0, 5, 6.6, 6.12, 7, 9, W7-W12, the W7 close, both coach logs, both outboxes, both state files, the taught lists, Claude's Nov 22 draft and pattern-drill record. Fresh heads fetched for all six repos; PRCP's actual repository name is `platform-reliability-control-plane`.

Canonical plan SHA256: `5301551d30cee7b993621275250ec0f82f21578bfd5a5953c538ab1538b75d4b`.
Checker SHA256: `ad0d3efdbe10444ba34fdf64dc9c3b34fd090b8afbfac8893bdef2a9af4e4044`.
Both match the attachments and plan/README.md. W8 is Nov 23-29.

Primary evidence:
- [Plan, pinned snapshot](https://github.com/omieee/docs/blob/dc651bd1b0a03829cf6f773d48fdc3c78d3a55ae/plan/Phase1_Master_Plan_v3.9.md): DSA labels and spacing L682-L691; sorting L712; recognition L716; continuity L814-L835; time accounting L459-L467; change control L1050-L1064; W8 L1392.
- [W7 close and tracker](https://github.com/omieee/docs/blob/dc651bd1b0a03829cf6f773d48fdc3c78d3a55ae/phase1-log.md): 7.75 plan hours closed, carry 4.25h, actual active time partly unknown.
- [Claude log](https://github.com/omieee/docs/blob/dc651bd1b0a03829cf6f773d48fdc3c78d3a55ae/claude-log-entries.md): insertion sort completed Nov 20; factorial Nov 21; Fibonacci Nov 22; ReplicaSets watched Nov 22; sliding-window teaching note supplied Nov 22.
- [Pre-plan DSA draft](https://github.com/omieee/docs/blob/dc651bd1b0a03829cf6f773d48fdc3c78d3a55ae/claude/plan-drafts/2026-11-22-dec6-preplan-dsa-review.md) and [W7 pattern drill](https://github.com/omieee/docs/blob/dc651bd1b0a03829cf6f773d48fdc3c78d3a55ae/claude/tests/dsa/2026-11-22-pattern-drill-W7.md).
- DSA PRs [22](https://github.com/omieee/dsa-python/pull/22), [23](https://github.com/omieee/dsa-python/pull/23), [24](https://github.com/omieee/dsa-python/pull/24) fetched fresh. Their existing coaching records stand; this review does not rerun or re-score those submissions.

## 1. BUG: uncounted DRILLs can leave the recall system

**What.** Amend section 6.6 #5 and the sorting paragraph: “DRILL does not count towards the numbered problem target. It still creates a concept-recall obligation.” Use **DRILL-RECALL**, separate from NEW (a new counted problem) and COLD (a counted problem re-solved without help). Neither drill practice nor drill recall changes the 27/20 totals.

For newly completed drills, schedule day 7, day 28 and day 90 after the actual completed practice date. These are coaching settings to measure, not scientific forgetting deadlines. Day 7 checks the taught mechanism; day 28 includes a blank-page implementation, tests and a changed input; day 90 checks transfer to a changed case. Insertion sort gets code at day 7 as well, because that is the specific uncovered concern.

A trace-only result proves the mechanism checked, not independent coding. Record that distinction. For code recall, HELD requires a fresh independent implementation, a verified run and a correct explanation of the taught mechanism. No full NEW interview is added. SLIPPED preserves the original miss; DSA teaching and retry each take separate later slots under section 6.6 #11.

A later counted problem may cover a drill concept only if the coach records the concept, the unassisted observation and the evidence. It must occur at the relevant delayed interval. A new lesson with hints is not recall. A future tree task is a booking, never completed evidence.

**Why.** The plan separates counts correctly but supplies no explicit drill-retention route. Section 6.6 #6 says “spaced re-solves” generally; the operational tracker applies it to counted problems, and section 6.12 excludes DSA from warm-ups.

**Evidence and coverage.**

| Taught mechanism | Existing work that could cover it | What remains necessary |
|---|---|---|
| Stack updates from 682 | Independent 20/155 checks | Verify the exact stack operation; never claim every part of 682 was covered |
| Search interval from 374 | Independent 704/74/875 checks | Verify bounds, progress and termination, not merely the phrase “binary search” |
| Insertion sort | No scheduled replacement identified | Sorted-prefix reasoning, moving across several positions, preserving the order of equal keys, taught complexity |
| Factorial recursion | Later tree work may check base cases and returns | Explicit evidence for stopping and unwinding; first-use tree teaching cannot clear the obligation |
| Fibonacci recursion | Tree recursion checks some shared ideas | Two branches, both base cases, repeated calls and time versus stack space remain separately identifiable |
| Merge sort and quicksort | Not completed at this snapshot | Register separately when taught; “sorting” alone cannot clear either |

Dates from the completion records, not from when the plan hoped the work would finish:

| Drill | Completed | Day 7 | Day 28 | Day 90 |
|---|---|---|---|---|
| Insertion sort | Nov 20 | Nov 27 | Dec 18 | Feb 18, 2027 |
| Factorial | Nov 21 | Nov 28 | Dec 19 | Feb 19, 2027 |
| Fibonacci | Nov 22 | Nov 29 | Dec 20 | Feb 20, 2027 |
| Merge / quicksort | Not yet | Completion +7 | Completion +28 | Completion +90 |

For 682 and 374, audit existing independent evidence first. If it does not cover the mechanism, book one current catch-up, not six backdated sessions. Preserve unknown historical checks as unknown. Their original day-90 dates are Jan 1 and Jan 26, 2027.

**Time cost.** Conservative first-cycle allowance before any verified substitution: insertion 30+30+15 = 75m; 682, 374, factorial and Fibonacci each 15+20+10 = 45m; merge and quicksort each 20+35+15 = 70m. Total **395m**, rounded to **7h** with 25m for setup/overrun. Old-drill catch-up replaces missed early checks; this is an upper allowance, not an instruction to duplicate proven work. Miss repair is additional measured work. The previous draft's 4h allowance was too tight for setup and the immediate insertion check.

**What moves.** Finding 5 funds the first hour by moving W8's sorting hour to the W9 queue. Later checks displace equal new DSA time in their actual due weeks. The full 7h is not added to W8.

**Risk reduced.** Correct code on a teaching day being treated as lasting knowledge, or drills inflating the counted-problem total.

## 2. GAP: older and bedside-taught concepts can disappear behind a busy track

**What.** Extend the existing progress record with one row per independently teachable mechanism, not one row per keyword or one row for an entire track. Include Python, SQL and bedside teaching. Keep three states separate: taught, independently proved, recalled after a delay.

Teaching creates a first-proof obligation within seven days. Independent proof starts day-7/day-28/day-90 recall dates. No completion date means “proof pending”, not an invented review anchor. For an already-proved concept repaired at bedside, preserve the miss and its scheduled retry; reading a repair note does not clear it.

Change the five-minute warm-up from “the lane's last session” to **the oldest due concept in the current lane**. Use the last-session recap only if nothing older is due. Keep the one-lane-after-DSA approach; do not force a Go session to start with an unrelated SQL task. If a concept is due in a lane with no session, the Sunday plan must name a funded slot, or report it overdue with a dated action. Do not reset its original due date to hide lateness.

Each obligation names the required evidence: explanation, trace, runnable code or lab behaviour. A five-minute verbal answer cannot clear a code/lab obligation. Existing work may clear several concepts only if each was independently observed; count its minutes once. Optional bedside cards remain optional.

After day 90, retain a next date through Gate C, at most 90 days after the last qualifying recall. A mapped gate, rep or project task can supply it. A final successful checkbox must not recreate the same hole later in a long plan.

**Why.** Lane activity and use during a lesson do not establish delayed recall of earlier ideas.

**Evidence.** Section 6.12 explicitly relies on the last session and optional cards. W7 records six warm-ups yet an older cohesion gap. The taught lists are incomplete: for example, the Go list still places the slices package under “not taught”, while the W7 close records it as taught. Therefore these lists need reconciliation with actual session records before any recall inventory is called complete.

Bedside cases need different treatment:
- 875 already has a dated Nov 26 cold; use its existing changed-constraint follow-up for the halving mechanism if independently demonstrated.
- The sliding-window note is repair teaching; retain the Nov 22 miss and check understanding before assigning the later independent coding slot.
- ReplicaSets was watched, not proved by a lab. Book its first proof before Nov 29, then schedule recall. Do not treat watching as real independent use.

**Time cost.** Replace questions inside the funded 35.75h warm-up allowance; no additional routine warm-up is proposed. That allowance is capacity, not proof that all concepts fit. Longer checks, repairs, inactive-lane slots and checks after day 90 need explicit minutes in the rebuilt map. Their total is **not yet established**.

**What moves.** The latest-session recap yields to the oldest due mechanism. A due check that cannot fit displaces a named piece of forward work; it cannot wait indefinitely for “sustained overflow”. At the rebuild, a complete inventory and demand calculation are required before declaring whole-plan coverage.

**Risk reduced.** Old Python, SQL or Go ideas, and bedside-only teaching, vanishing while the track still looks active.

## 3. GAP: recognising old DSA patterns is insufficient evidence of coding retention

**What.** Retain Claude's proposal to rotate old problems through the existing six-question weekly pattern drill. Use three old and three recent statements in W8-W13 until the 16 have appeared. This replaces prompts; it adds none.

Also sample independent coding from each of the four old families, regardless of whether their pattern names are recognised. Suggested representatives: 49 for arrays/hashing, 167 for two pointers, 3 for sliding window, and 707 for linked-list implementation. Existing recent independent evidence may replace a sample only for explicitly matching mechanisms. These are old-problem retention checks, not NEW work.

LC3's known miss gets its repair and separate retry first. Do not use a known failed item as a fresh baseline or score it twice. A slip widens the sample only to the affected mechanisms. Problems not sampled remain implementation-UNVERIFIED; a four-problem sample does not certify all 16.

**Why.** “I recognise sliding window” and “I can implement it without help” are different claims.

**Evidence.** Nov 22: 4.5/6, with “Dynamic Array” for Om's own LC3. Claude's draft lists 217, 242, 1, 49, 347, 238, 128; 125, 167, 11, 344, 977; 121, 3, 643; 707. Its estimate of about one hour based on one miss in six is not a reliable prediction of implementation retention.

**Time cost.** Reserve **2h** for the four first samples: 25m each for 49 and 167, 30m for LC3, 40m for 707, including setup and explanation. These are provisional older-work checks, not the standard short daily cold boxes. If all 16 need code checks, allow **up to 6h total for checks**, then revise from actuals. Repair teaching remains separately funded. Do not sell this as a maximum cost of relearning. The existing pattern drill has no added prompts, but mandatory bedside time still counts under section 5.

**What moves.** Provisional checks: LC3 Nov 30, 49 Dec 2, 167 Dec 4, 707 Dec 5, each its own slot and subject to readiness and the due-cold queue. They replace 2h of W9's 2.25h new DSA allocation. The remaining 15m cannot start a new unit; hold it for setup/overrun. Trees therefore move to the post-Dec-6 queue. If more fixed colds fall due, those take priority and the sampling dates move openly.

**Risk reduced.** Green pattern-recognition marks masking inability to build the solution.

## 4. GAP: the checker validates the map, not actual recall coverage

**What.** Keep the existing arithmetic and dependency checks. Add a structured concept/recall table to the existing shared record, with:
`concept ID | lane | taught date/source | first-proof status/date/evidence | required recall type | original due date | booked date/slot/minutes | observation/result/evidence | next action`.

The teaching coach creates the entry; the coach running a recall appends its evidence in its own test record and updates only the linked observation. Both coaches read one queue. The Sunday coach reconciles it with both logs and taught records. Do not create two competing completion ledgers.

The checker needs the structured inventory and an explicit as-of date. Static mode verifies future bookings against the plan's hours; execution mode checks actual proof and recall records. A past due check without evidence reports OVERDUE, never HELD. Missing coverage makes the recall audit incomplete. A queue audit must be required for a plan promotion or weekly close, not an optional check that nobody runs.

**Why.** A script can detect missing dates, evidence references and capacity. It cannot infer every concept from prose or decide that an answer proves understanding.

**Evidence, freshly run.** Canonical checker: PASS, 87 weeks, 969h, 14 fragmentation warnings. In a scratch copy, appended a named `RECALL_AUDIT_SENTINEL` DRILL with no scheduled recall to the sorting paragraph: checker still PASS, exit 0. At lines 314-322 it checks the presence of the warm-up/cards wording; it never reads the taught records. This demonstrates a coverage limitation, not that its arithmetic checks are worthless.

**Acceptance tests for the eventual implementation:** a passing fixture plus failures for (1) taught topic with no first-proof booking, (2) proved topic with no next recall, (3) overdue recall falsely completed without evidence, (4) optional card or guided work used as cold proof, (5) unrelated problem credited, (6) invented historical or future completion, (7) duplicate counting of one event's minutes, (8) a booked week exceeding its budget, (9) removal of a taught ID without an explicit merge/reason, and (10) a known miss cleared by changing its date. A valid mapped reuse must pass without adding duplicate time. Human review still judges whether the content proves the named mechanism.

**Time cost.** Coach implementation and record maintenance: zero learner study hours. The checks Om performs are charged under findings 1-3, not called administration.

**What moves.** No learner block. The builder updates the generator and checker, runs existing and new negative tests, and hands the generated amendment to the other coach. This proposal does not claim the new checker exists or passes.

**Risk reduced.** Mechanical PASS being read as “every taught topic has a real recall path”.

## 5. GAP: recall must displace work, not enlarge an already-full week

**What.** Use this bounded W8 bridge only if Om approves it before the slots below. It is the first hour of finding 1's 7h allowance, not another hour.

| W8 DSA allocation | Minutes | Booking |
|---|---:|---|
| Existing counted colds, setup and follow-ups | 45 | 875 Nov 26; 206 Nov 27; 21 Nov 28 |
| Insertion sort: blank-page code, run, trace and equal-key reasoning | 30 | Nov 27, separate from 206 |
| Factorial: cold base-case and return trace | 15 | Nov 28, separate from 21 |
| Fibonacci: cold branching/base-case/complexity trace | 15 | Nov 29 |
| Existing trees introduction, only its taught prerequisites | 30 | One earlier W8 slot |
| **Total** | **135 = 2.25h** | **Original W8 DSA budget** |

Insertion's full coding recall is checked immediately; the two recursion checks establish only their named mechanisms. Their later day-28 coding checks remain booked. Stop on time and record a slip; repair takes another funded slot. Keep each DSA item separate and the daily total within the plan's limit. If a fixed cold overruns, the tree introduction moves first.

**Why and evidence.** W8's execution list holds 12h plus 4.25h carried. The W7 close already moves harvest part 2 (2.5h), MP4 (1h) and R2 (0.75h) to W9 at the 12h baseline. Those moves stand. Adding recall on top would repeat the same capacity error.

**Time cost and what moves.** W8 sorting's **1h moves to the W9 queue**, replacing it with the 1h recall bridge. W9 therefore begins with 12 + 4.25 + 1 = **17.25h of queued scope**, not a 17.25h commitment. Finding 3 uses 2h inside W9 DSA and moves its new tree work onward. Apply section 14's existing priority rule and name the deferred items at the W8 close. None of this restores postponed work by assuming extra leave hours.

The known first-cycle addition is **9h minimum**: 7h drill allowance plus 2h old-family checks; up to **13h for checks** if the old-family sample expands to 6h. Verified reuse can reduce this. Repairs, non-DSA overflow and later maintenance are additional, not hidden in that number. Do not publish a revised gate date until the generator includes the actual inventory, carried work, recurring costs and light weeks.

Go's 105m and Kubernetes' roughly 200m were elapsed intervals with gaps, not measured active minutes. They justify better timing and caution, not a blanket 3.5x or 6.7x multiplier. W7's 7.75 closed plan hours also must not be relabelled as active study hours.

**Risk reduced.** A recall fix that works only by sacrificing sleep, skipping other core work, or moving debt invisibly.

## Approval boundary and build handoff

Om's request authorises this investigation and proposal; it does not approve an amendment. Do not label the bridge, the new intervals or the changed warm-up selection as existing plan content.

If approved, one coach incorporates sections 6.6, 6.12, 7, 9 and the affected rows through the current v3.9 generator; the other verifies the generated plan, ledger reconciliation, dated capacity, clean checker run and expected negative-test failures. Reconcile all taught mechanisms before claiming complete coverage. Om approves promotion to plan/ and uploads the final master and checker to both projects.

**Approval proposed:** adopt the recall principle, the bounded W8 bridge and the funded W9 sampling; commission the generated amendment with the complete recall inventory and honest date impact. No past learner verdict is reopened.
