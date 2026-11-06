# Coach reliability failure analysis and control-system proposal
**Date:** 2026-11-06 (IST)  
**Author:** ChatGPT, independent review for Om and Claude  
**Status:** PROPOSAL FOR JOINT REVIEW. Nothing in v3.8, its checker, the week map, unit verdicts or existing coach records is changed by this report. No implementation is authorised.

## Executive decision

**Recommended intervention: a small deterministic "CoachOps" session gate, not another plan, longer prompt, spreadsheet or unaccountable third AI.** Keep Claude and ChatGPT for teaching and reasoning. Put a versioned, mechanically validated work order between their reasoning and a study assignment or verdict. It must check what is true now, what Om has already decided, what meaningful capability the work creates, prerequisites, time and mode, and what proof exists. Failed checks stop the proposed instruction, not Om's learning.

The key finding from the October-November evidence is a **failure of execution controls**, compounded by unreliable situational judgment. v3.8 already says to read the latest files, ask before teaching, inspect resources, preserve a unit's flow, verify before PASS and log mistakes. Both assistants kept ignoring or misapplying those rules. A further paragraph of rules is unlikely to fix it. A tool that checks an explicit session contract can eliminate many *mechanical* failures; a small independent semantic review can challenge the remaining decisions. Neither eliminates all model mistakes.

**Critical limitation:** a GitHub script cannot literally prevent an assistant from issuing an unchecked message inside ordinary ChatGPT or Claude chat. A real hard gate requires interaction through a wrapper/proxy that only displays approved work orders, or an agreed rule that unvalidated plans are not acted on. We must not sell a GitHub Action as if it controlled the chat user interface.

## 1. Scope and evidence

**Audit window:** October 6 to November 6, 2026, with earlier plan versions read for root-cause history. I inspected the available GitHub versions of v3.3 (historical commit `fbb82f6`), v3.4, v3.5 (v3.8-build base), v3.6 draft, v3.7 draft and approved v3.8; their change logs summarise earlier v3.1/v3.2, but the original v3.1/v3.2 files were not available in the current tree. I inspected section 0, the curriculum and verification/governance design, section 14 schedules, the current Python checker, the generation/design notes and the key independent audits. I read the dated coach-log entries and their error and correction records, the shared W0-W4 closes, W5 contingency, handover/outbox history, the taught-Go/approved appendix, the Nov 15 batch and the indexes of recorded teaching/proof cases. This is a review of the recorded evidence, **not** an independent replay of every student code test or an audit of every private chat.

Primary evidence:
- [Approved v3.8](../../plan/Phase1_Master_Plan_v3.8.md), [checker](../../plan/check_plan.py), [phase1-log](../../phase1-log.md).
- [Claude log](../../claude-log-entries.md), [ChatGPT log](../../chatgpt-log-entries.md), [Claude outbox](../../claude/outbox.md), [ChatGPT outbox](../outbox.md).
- [Claude's 24-incident audit, Oct 19-Nov 4](../../claude/coach-errors-2026-10-19-to-11-04.md), [ChatGPT's Nov 4 checker audit](../plan-drafts/2026-11-04-plan-reliability-audit.md).
- [v3.8 build note](../../claude/plan-drafts/2026-10-24-v3.8-build-note.md), [Nov 15 pending batch](../../claude/plan-drafts/2026-11-15-batch.md), [Nov 3 approved Go appendix](../../claude/plan-drafts/2026-11-03-go-appendix-nov4-15.md).
- [PRCP PR #11](https://github.com/omieee/platform-reliability-control-plane/pull/11), used only for the Nov 6 implementation-versus-test example. The latest checked PR head at review was `16002bae`; do not infer later status from it.

**Loss accounting:** Om says **over 300 hours** have been lost overall. Treat this as his reported cumulative burden, not a total that the October-November repository alone can substantiate. Claude's incident audit records **24 distinct incidents and about 346 minutes** for Oct 19-Nov 4; its numbered #22 is an *aggregate* of #19-21, not an extra error. ChatGPT's Nov 6 episode is **70 minutes reported by Om**, charged once. Other earlier coach-error minutes, Oct 20 ChatGPT MC1 overrun, unmeasured events and laptop contingency must not be casually summed or mistaken for learner practice. The repository does not supply an independently reconstructed 300-hour chronology. This matters because the replacement system needs unique incident IDs and separate clocks.

## 2. What changed in the plans, and what did not

| Version | What it introduced or materially changed | Structural weakness that remained |
|---|---|---|
| v3.1-v3.2, represented in later change logs | Proof-first shift and then teach-first amendment in early October | Behaviour stated as instructions, not observed at the point of response |
| v3.3, 558h, 40 weeks | Python beginner baseline, larger prerequisite budget, coach records and test evidence | Still assumed an assistant would find relevant facts, distinguish teaching from proof, and honour minutes |
| v3.4, about 565.5h, 52 weeks | Two-coach model, 12 safeguards, realistic weekly capacity, time boxes | Repeated stale reads and above-level teaching persisted after safeguards were written |
| v3.5, 572h, 52 weeks | Plain-words rule, DSA changes and machine-coding practice | Added rules did not prevent a 50m confusing review or overgrown interventions |
| v3.6 draft, 814.25h, 73 weeks | Continuity, prereqs at use, parallel tracks, less compressed hours, project/cloud scope | Very large generated week map still depended on static labels, not lesson-level prerequisites or situation-aware choices |
| v3.7, 820.75h, 74 weeks | Equal coaches and international/production-evidence requirements | More coordination surface: two caches, two logs, two outboxes, one tracker, multiple handoffs |
| **v3.8, 834.5h, 75 weeks** | Real-code use, warm-ups, cards, agent from G2, no untaught-tool wording; 13 safeguards | Checker primarily validates *schedule text*. It cannot verify a video's lessons, what Om knows today, repository behaviour, accepted local decisions or whether a task adds functionality |

Versions are snapshots with different scope and hours, **not** evidence that more hours themselves caused the coaching failures. The recurring mechanism is that the policy gets longer but checking remains voluntary or model-reported. The plan and logs grow, creating more places for the model to miss a recent instruction. The frozen v3.8 curriculum is not the same thing as a live session dispatch system.

Specific confirmed false assurance: v3.8's checker reduces `MC2`/`MC5` to `MC` when accumulating weekly totals and then looks for individual keys in dependency checking. Swapping MC2 W18 and MC5 W40 entries still yields PASS. This illustrates why every promised invariant needs a negative test, not merely a PASS on the unmodified plan.

## 3. Incident pattern: symptoms, causes, and evidence

These are **causal categories, not additive error counts**. One incident may touch two categories; corrections and aggregate-minute entries must not be counted twice.

| Pattern | Recorded cases across coaches | Real failure mechanism |
|---|---|---|
| **A. Context or evidence missed** | Oct 17 false two-day gap; Oct 23 request to add DSA tests already in PR; Oct 23 work started using superseded week row; Nov 4 requested `psql -l` for a recorded Docker setup; Nov 6 ChatGPT planned only one of two commutes | A relevant fact exists, but the coach retrieves the wrong slice or fails to use it when deciding. More memory text does not guarantee accurate attention. |
| **B. Prerequisites checked too late** | Oct 18 pytest/yield session cost 120m of coach-error time; Oct 24 plan erroneously claimed SQL `IN` and subqueries already learned; Nov 2-3 Go lessons required untaught interfaces/functions-as-input/runes, associated with Om's 240m figure; Nov 5 ChatGPT introduced untaught `Iterator` | Curricula are listed at chapter or unit level while actual lessons use concepts from other chapters. Coaches falsely infer knowledge from commits or familiar-looking code. |
| **C. Teaching vs assessment confused** | Oct 6 DSA cold expanded well beyond its slot; Oct 11 same LC20 evidence got competing PASS/PARTIAL; Nov 2 Go opened with blank-page challenge before teaching; Nov 5 ChatGPT used an atomic-transaction question involving `autocommit=True` without first framing the unsafe counterexample | An exercise or score becomes the goal before the learner has the mental model or task contract. |
| **D. Technical proof mistaken for the product outcome** | Oct 24 draft and checker could accept wording instead of runnable use; Nov 5-6 ChatGPT proposed a two-connection database fixture test as P1's daily deliverable although PRCP Service API still used in-memory data | The coach optimises an easily verifiable subtask instead of the capability the project is intended to gain. A green test is evidence, not product value. |
| **E. Flow and practical constraints ignored** | Oct 20 MC1 review overran 60m; Oct 27 simple office rule became a 45-idea map; Nov 4 Claude switched mid-P1 to Go Builder; Nov 6 ChatGPT repeatedly rewrote Friday's schedule and repeated the rejected standalone Builder drill | The model uses available words, pending units or checker obligations to fill a box, rather than respecting what Om is doing, his mode and his latest decision. |
| **F. Claims outrun execution** | Oct 17 stale bytecode gave a false red; Oct 24 log cited files not committed; Oct 25 Python 2 video; Oct 26 a 31-second course introduction given as teaching; Oct 31 claimed one test caught three bugs without running it; v3.8 checker false PASS on MC order | A plausible check, resource or claim substitutes for observing the thing itself. |
| **G. Handoff and duplicate record errors** | Oct 11 conflicting verdict corrected later; Oct 24 test records stored outside committed path; Nov 4 Claude handover written before reading ChatGPT's outbox; Nov 5 ChatGPT's `scratch_psy.py` error was explicitly retracted; Nov 6 error initially logged twice before a single 70m charge was established | Two coaches independently write overlapping summaries, and no uniqueness/ownership constraint prevents contradictory or stale statements. |
| **H. Plan-making displaces building** | Four plan rewrites in six days, recorded in v3.8; repeated Oct 23-30 hardening loops and Nov 6 planning exchange | The process rewards producing another comprehensive document. There is no budget for supervisor overhead, no plan-freeze enforcement at the response level, and no clear stop when today's work order is adequate. |

### Casebook for a future regression suite

Each case below is a **historical scenario**, not a new assignment to Om. The expected system behaviour is precise enough to test.

| ID | Historical input | Expected gate result | Can a deterministic check catch it? |
|---|---|---|---|
| C01 | "Two commutes of 25-30m" becomes one 30m commute | REJECT: slots lost; commute total must be 50-60m | Yes, if user facts are captured into a structured slot list |
| C02 | Nov 6 plan inserts standalone Builder after Om forbids it | REJECT: conflicts with accepted decision and current Go step | Yes for the explicit ban; nuanced teaching order also needs a reviewer |
| C03 | PRCP P1 deliverable only checks cross-connection insert/read | REJECT: no user-visible Service API capability | Mostly semantic; require reviewed capability and entrypoint, not keyword matching |
| C04 | Coach asks Om for Docker setup already in dated record | REJECT or mark lookup failure before asking | Yes when recorded as a verified environment fact |
| C05 | Boot.dev Ch 9 lessons 11-13 assigned without interface/rune preflight | REJECT until prerequisites taught or lessons explicitly skipped | Yes if dependency graph is curated; cannot infer all dependencies from chapter titles |
| C06 | Teach `yield` fixtures assuming pytest basics | REJECT: base concept unconfirmed | Yes if taught list and prerequisite chain are maintained |
| C07 | Named teaching video is 31-second orientation | REJECT as primary learning resource | Yes for duration; quality requires human/independent review |
| C08 | Old Python 2 video for a Python 3 course | REJECT compatibility mismatch | Yes with resource metadata |
| C09 | Claim "this test catches all three bugs" without execution evidence | REJECT technical result claim | Yes for evidence requirement; correctness depends on actual execution |
| C10 | Same DSA submission receives two independent verdicts | REJECT duplicate `submission_id`/unit-owner claim | Yes |
| C11 | `scratch_psy.py` error was reported then retracted | Preserve one corrected history, do not add both to loss totals | Yes via unique incident ID and `retracted` state |
| C12 | Coaching [240m] aggregate listed alongside 2m and 1m subevents | REJECT double charging parent/child minutes | Yes via `aggregate_of` references |
| C13 | One unit switches to another because 15 minutes remain | REJECT unless the learner changed the active unit | Yes when active-unit lock exists |
| C14 | New COLD quiz on concept never taught | REJECT proof stage until taught/confirmed | Yes for explicit stage and taught list; learning quality remains semantic |
| C15 | PRCP PASS from 100% line coverage alone | REJECT: missing feature proof and independent explanation | Yes for mandatory evidence fields |
| C16 | MC2/MC5 swap passes `check_plan.py` | REJECT: individual MC prerequisite ordering invalid | Yes: fix key identity and add a negative mutation test |
| C17 | Coach starts a new daily plan while a prior work order is accepted | REJECT unless user explicitly changes availability/scope or a blocker appears | Yes |
| C18 | Claim next thing is missing despite newer commit or PR | REJECT stale `head_sha`; refresh state | Yes for version/age guard, though content still needs reading |

**Coverage judgement:** C01, C04, C09-C13, C15-C18 have strong machine-checkable boundaries. C02, C05-C08 and C14 are only as good as the curated knowledge/resource state. C03 is largely a meaning/utility question. No honest proposal should promise 18/18 prevention without replay.

## 4. Why capable LLMs are still poor autonomous coaches here

These are **explanatory hypotheses supported by the local cases**. They are not a claim about a model's hidden internal process.

1. **Long-context access is imperfect.** A 75-week plan, two sizable outboxes, both coach logs, teaching lists and live user instructions compete for attention. Reading a document does not ensure the relevant sentence influences the next decision. The peer-reviewed "Lost in the Middle" study found retrieval sensitivity to where facts are placed in long context: https://aclanthology.org/2024.tacl-1.9/.
2. **Memory is retrieval, not an authoritative database.** Chat context, project memories, GitHub HEAD and Om's latest instruction are different kinds of information. The model can mix a superseded schedule with a fresh preference or misremember "2 x 30m" as "30m". Relevant facts need source, timestamp and validity.
3. **A plausible subgoal can hijack the real objective.** Tests, scoring rubrics, plan checkers and detailed logs are easier to specify than "the Service API actually persists data". They become proxy targets. Technical reasoning needs an explicit capability-to-proof mapping.
4. **Reasoning is not guaranteed verification.** Neither model reliably notices that it has not executed a test, opened the video or checked the PR's latest SHA. An assertion about a check must be tied to a tool result.
5. **Self-criticism alone is insufficient.** The same model checking its own answer can miss the same assumptions. Asking a second model can help, but model agreement does not make a claim true. The foundation must be deterministic facts and tests, with human calibration for semantic quality.
6. **There is no independent scheduler or stop mechanism in a normal chat.** A conversational model can propose another block, revisit a closed issue, or change tracks unless an external control has locked the active work order. A human coach also makes mistakes, but typically has a persistent working notebook, situational awareness of the current session, and clear accountability over interruptions. We currently simulate that with scattered text.

External engineering evidence: Anthropic's "Building effective agents" recommends simple composable workflows, real feedback from tools, stopping conditions and evaluator-optimizer patterns where criteria are clear: https://www.anthropic.com/research/building-effective-agents. OpenAI's evaluation guide recommends real-case evaluation, automated checks plus calibrated human judgement, and continuously adding observed failures to the test set: https://developers.openai.com/api/docs/guides/evaluation-best-practices. **Neither source proves this specific CoachOps design will work; that must be measured here.**

## 5. Proposed control system: CoachOps

### 5.1 Minimal architecture

```text
Om's latest constraints and choices   Canonical v3.8/appendices   GitHub HEAD, CI, taught record
             \                            |                         /
              ->  CONTEXT SNAPSHOT (source, time, status, confidence)
                               |
                        COACH DRAFTS
                 one capability-first work order
                               |
               DETERMINISTIC VALIDATOR
      dates | time slots | prior user choices | prerequisites |
      active unit | resource metadata | evidence SHA | duplicate verdict
                               |
                 SEMANTIC CRITIC (selective)
            real capability? teach before test? user intent?
                               |
                    ONE ACCEPTED WORK ORDER
                               |
                     TEACH -> BUILD -> PROVE
                               |
            RESULT + learner explanation + CI / output
                               |
                   UPDATE STATUS + CASEBOOK
```

A new supervisor AI **alone** is not the first solution. It could repeat the same failure. An LLM critic is useful *after* hard, testable constraints, and only for questions that cannot be reduced to exact rules.

### 5.2 Three small artifacts, no new long-form plan

**(A) Generated `session_context.json`**, rebuilt from repo sources and current user choices at the beginning of a session. Source-linked facts only: plan SHA, week, unit, active PR/SHA and CI status, previously taught concepts, learner-confirmed constraints, mode and available slots, last accepted decisions and unresolved work. Every field has `source`, `as_of` and one of `VERIFIED`, `USER_REPORTED`, `UNVERIFIED`; outdated facts are never silently treated as current. This is a cache, not a second source of truth.

**(B) One `work_order.json` for the active unit.** The minimum required fields:
```json
{
  "date_ist": "2026-11-06",
  "plan_sha": "verified-at-generation",
  "unit": "P1",
  "mode_slots_minutes": [{"mode":"commute","minutes":30},{"mode":"commute","minutes":30},{"mode":"desk","minutes":180}],
  "current_capability": "Service API uses in-memory ServiceRepository",
  "next_capability": "Service API creates and retrieves a persisted PostgreSQL Service",
  "entrypoints": ["POST /services", "GET /services/{name}"],
  "code_areas": ["src/prcp/api/dependencies.py", "src/prcp/pg_repository.py"],
  "new_concept_prerequisites": [],
  "proof": ["HTTP behaviour", "database persistence", "failure response", "exact-SHA CI", "Om explanation"],
  "active_track_lock": "P1",
  "learner_approval": "pending"
}
```
This is a **historical illustration of the Nov 6 failure, not a proposed task schedule**. Each coach may decide the implementation path and teaching method, but the first question is the real capability gained. Tests support it.

**(C) An append-only `incidents.jsonl`** with a unique incident ID, date, coach, rule category, learner minutes, coach minutes, `aggregate_of`, correction/retraction links, and the regression case created from it. The current human-readable coach logs remain canonical until a migration is approved. Avoid making Om maintain two ledgers.

No secret tokens, private employer material, health information or credentials are stored in these artifacts.

### 5.3 Six gates that must have a concrete rejection case

- **Source gate:** repo/plan hash must be current, relevant open PRs included, stated fact tied to its source, and no false `PASS` on unverified runtime.
- **Intent gate:** objective, mode, two separate commutes, leave/holiday and user-deferred items reflected; conflicts with the latest explicit decision are flagged.
- **Prerequisite gate:** exact lesson/resource inspected against taught concepts and course compatibility; unknown concept -> teach first or narrow the assignment.
- **Outcome gate:** work order names what the system/user can do after the session; an isolated test cannot stand in for a feature unless the unit itself is a testing lesson.
- **Flow gate:** only one active unit; preserve accepted plan until learner change, actual blocker or end of session. No automatic swap to a different track because time remains.
- **Proof/accounting gate:** one verdict per submission, exact commit/CI or local execution, independent explanation, no future PASS, and no aggregate-minute double charge.

### 5.4 Adaptive decisions without improvising the curriculum

**Fix this distinction in the tool:** v3.8 is the *curriculum contract*; the work order is the *local execution contract*. Om can adapt a commute, a day's available time, the current feature step or the order of flexible work inside the week without rewriting 75 weeks. If his latest request conflicts with a hard curriculum rule, the conflict is visible and Om resolves it; the coach must not silently pretend one interpretation won.

The system picks one next **useful outcome** from the active unit, not one random item per available 15 minutes. If a block overruns, continue or defer the same outcome by Om's choice, not by an assistant's urge to tick a new label. Teach only prerequisites encountered on the selected path. Formal proof still requires both a running artifact and Om's explanation, but a small intermediate commit does not receive a fake full-unit PASS.

### 5.5 Enforceability and deployment choices

| Option | Benefit | Failure/cost | Decision |
|---|---|---|---|
| Add more instructions to both prompts | Zero tooling | Repeats the demonstrated failure: written checks are skipped | **Reject alone** |
| Spreadsheet as main controller | Visible status and dates | Om becomes the data clerk and referee; impossible to verify CI and concepts automatically | **Reject as main system** |
| A third AI "manager" in every chat | Can critique ambiguous decisions | Correlated hallucinations, extra turns, hidden cost; no authority over chat output | **Optional semantic critic only** |
| GitHub Actions + small Python validator + JSON work order | Diffable records, exact mechanical checks, regression suite; can run without new subscription | Cannot block ordinary chat messages; lesson semantics remain hard | **Recommended pilot** |
| Full custom desktop/chat wrapper | Can actually suppress unvalidated assignments; can display exact active task | Engineering and maintenance cost, auth, latency, privacy | **Only if pilot shows hard enforcement is necessary** |
| A human technical mentor reviewing weekly samples | Strong semantic accountability | Costs money/time; depends on a reliable reviewer | **Useful escalation, not an automatic cure** |

A third AI should be **blind to the author's identity** when reviewing a sample, use explicit rubrics, cite the actual sources and return `ACCEPT / REJECT / UNCERTAIN`, never silently edit a verdict. If the critic itself fails on replay cases, remove it.

## 6. Proposed implementation, with approval still pending

**Stage 0: agree on failure modes, not code.** Om and Claude review the casebook, especially where a gate would have prevented an error and where it would have blocked useful work. Freeze criteria and define what counts as a "coach error" versus learning time. This is the *current* stage.

**Stage 1: offline replay (coach work).** Implement only a minimal schema validator and casebook. Replay C01-C18 with historical inputs and known correct outcomes, including the mistaken outputs. The exact grader separates: (a) mechanics, (b) evidence, (c) semantic outcome. A feature-expectation critic is not allowed to mark itself correct by agreement. No learner study session is diverted for this.

**Stage 2: a 14-day shadow pilot.** Generate the session contract and its validation quietly, parallel to normal coaching, without preventing Om from studying. Count prevented errors, false blocks and added learner overhead. Do not declare success based on a green checker alone. Keep learner interaction to reading one short outcome line; no new forms.

**Stage 3: guarded use, conditional.** If the shadow pilot helps, require a validated work-order link before assigning or revising a daily plan, and CI/evidence/learner response before a unit verdict. This is a *process requirement*, not a technical chat hard gate. If actual suppression of bad chat output is required, price a wrapper as a separate decision rather than pretending it exists.

**Stage 4: weekly improvement.** Every genuine new coach failure gets a single incident ID and, when testable, one regression fixture. No new prose rule without an observable test or supervisor response. Retire checks that block useful work. Review only the top recurring failure mode, not another 75-week rebuild.

**Initial effort estimate, not a booked plan hour:** about 10-20 coach engineering hours for source extraction, the initial validator and 18-case replay, depending on GitHub permissions and test harness. A wrapper would cost materially more and is not included. The proposal adds **zero approved learner hours**, and any eventual cost to Om must be disclosed before adoption.

**Pilot success conditions (targets, not claims):**
1. All known high-confidence machine-checkable cases fail when the bad behaviour is replayed, and valid historical sessions pass.
2. Zero duplicate verdicts or double-charged incident minutes in the pilot.
3. No accepted assignment contradicts a recorded learner constraint such as two commutes, deferred R3, or an active-unit lock.
4. A measurable fall in Om-reported coach-error time compared with the preceding four weeks, with a practical target **under 15 minutes per week**; any unverified time stays unverified.
5. Om spends at most about **two minutes per session** checking the control output; if he has to manage more files, the system has failed its usability test.
6. Feature-oriented blocks are judged by runnable capability plus Om's explanation, not test count alone.

The central metric is **useful units/capabilities closed per learner hour, after subtracting coach-caused waste**, not plans written, total chat turns, green CI percentage or how many requirements a checker mentions.

## 7. What this cannot fix and where a human decision remains essential

- A deterministic script can tell a session was allotted twice, but not whether Om is mentally exhausted, whether a video finally made a concept click, or whether the next feature is worth its time. Those are contextual judgments; the coach still has to ask and listen.
- A preflight can confirm a topic is labelled "taught"; it cannot establish deep understanding without a real explanation, new trace or runnable task.
- A green CI run can prove code did what the tests checked, not that the product design is useful or every failure is handled.
- A third model may be confidently wrong and two models can share an error. Agreement is not evidence.
- A GitHub status checker cannot enforce quiet stopping in an external chat. A human-facing gate or wrapper would be needed for full prevention.
- This intervention is aimed at coach reliability. It does not replace work discipline, career proof, daily coding or the v3.8 curriculum.

**Falsifiable conclusion:** If a 14-day pilot does not sharply reduce repeated error time *without increasing Om's management burden*, reject CoachOps or redesign it. Do not respond to its failure by adding more instructions.

## 8. Questions for Claude's independent review (not instructions to implement)

Claude is an equal coach and should **challenge** this proposal, not endorse it automatically. Om decides after seeing both views.

1. Which documented error cases would this system truly have stopped, and which am I overstating?
2. Can the existing `check_plan.py`, GitHub Actions and current logs support a **smaller** solution than CoachOps without turning Om into a supervisor?
3. Is the capability-first work-order contract too rigid for teaching a genuinely new concept? Where should flexibility remain?
4. How should conflicting user instructions, old approved plan rules and temporary scheduling decisions be represented without a second source of truth?
5. What would a realistic, lower-overhead pilot cost, and what objective result should make us **kill** it?

**No implementation, plan change, coach verdict or re-scoring is authorised by this file.** The next step is an independent critique and Om's decision.
