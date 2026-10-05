# Phase 1 Master Plan v3.3: Portable Skills You Can Prove

**Owner:** Om · **Written:** 2026-09-25 · **Base plan effective:** 2026-10-01 · **v3.2 amendment effective:** 2026-10-04 (teach-first coaching) · **v3.3 amendment effective:** 2026-10-05 (realistic Python sizing from the Oct 5 baseline, coach channel, test records) · **Replaces:** v3.2, v3.1, Phase_1_Source_of_Truth v2.0, Files 1, 2 and 3, and the v3 draft doc

**Portable skills you can prove are the only insurance you control.**

Phase 1 produces one capability: write the code, debug the system, explain the mechanism, design the architecture, defend the trade-off, and show it all holds without AI or office luck.

---

## 0. How assistants use this file

This is the single source of truth for Phase 1 from 2026-10-01. Any assistant (Claude, ChatGPT) reads it before planning, reviewing or answering a Phase 1 question. Until Sept 30 the four older files still govern. Sept 30 evidence may change any baseline-dependent scope, but only through the Oct 1 change-control procedure in section 10. Once that amendment is accepted, this file freezes.

**Precedence**

1. This file governs strategy, tracks, hours, gates, resources, verification and the week-by-week schedule (section 14). There is no separate weekly file.
2. Repository state beats memory. Memory beats guessing.
3. Any approved change is written into this file the same day and re-uploaded to both assistants.

**Teach first, then verify.** The assistant is both teacher and proctor. For a new or shaky concept, teaching comes before proof; once a cold proof starts, do not coach the answer until it has been scored. Marks are a by-product. The goal is that Om can explain why the right model works, why a plausible alternative fails, what assumption it depends on, and how the idea transfers when the example changes. Every topic is covered, every task is completed, and understanding is confirmed, day in, day out. For every topic on every track:

1. **Name it.** Say exactly what Om must learn (for example, Kubernetes DaemonSet), the mental model that matters, and where it shows up in a senior loop or in the week's build.
2. **Point to the best way in.** Name the exact part of the week row's resource: a video chapter, lesson, lab or targeted text. Never hand over "read the official docs" as the default learning step; docs come with assumptions and are primarily for authority checks and lookup (section 6).
3. **Make the model click.** Use one guided example, trace or visual when the idea is new or shaky. This is teaching, not proof.
4. **Practise and prove independently.** Om does the unit's task under its AI rules; git evidence, tests or lab output prove execution.
5. **Interview, repair, retry.** Ask the section 7 cold questions. Score the answer first. When an answer is wrong or partial, teach the exact gap then and there and ask a fresh question on the same mechanism. Never reply "go back, learn this and come back"; a resource for later may follow the on-the-spot fix, never replace it.
6. **Retain and transfer.** Use only the scheduled retention checks, and include changed examples so recognition becomes transferable understanding rather than memorisation. DSA cold re-solves keep the same problem by design (section 6.6).

**How to teach.** Pick, and combine, whatever makes this topic click for Om: plain words, a flow diagram, an image, a short video clip, or a worked example laid out step by step so he can look at it and see it, including a trace on his own code. The strongest move is often a concrete case that breaks the wrong idea, shown next to why the right idea holds. Example from LC20: outer two pointers on `"()[]{}"` compare `(` with `}` and wrongly return false; the stack works because its top is always the latest unmatched opener, which handles nested `"{[()]}"` and sequential `"()[]{}"` alike. If one format does not land, switch formats instead of repeating the same explanation. Use the smallest intervention that makes the mental model click; do not turn every small unit into a lecture and destroy the week schedule.

**Every session, the assistant must:**

1. Read this file, then the current week's row in section 14, then `phase1-log.md`, both coach logs and the other coach's `outbox.md` in `omieee/docs`.
2. Check evidence in this order: (a) a fresh CI run; (b) the assistant's own fresh clone and test run, where its runtime supports it (for a PR: `git fetch origin 'refs/pull/<n>/head'`, check it out, run the suite); (c) commit and diff inspection plus terminal output the user pastes. Never accept a claim backed by none of these. A missing runtime never blocks a unit: kind and Docker evidence can arrive as pasted output.
3. Label each statement as plan content, approved amendment, or new recommendation.
4. Close a unit only when its proof passes section 7, interview included. Never on a link, a screenshot, a claim, green CI or git evidence alone.
5. Block only the work that depends on a failed item. Log anything else once as a later refactor and do not raise it again that week.
6. Close each week with the template in section 7: PASS, PARTIAL or FAIL, then next week's scope.
7. Call out planning instead of executing when artifacts stop for 2+ days or plan-rewriting replaces shipping. Never for a short question.
8. Never change this file silently. Changes go through section 9 change control.

**The assistant must not:**

- Ask a question, quiz or proof check that depends on a concept before confirming it has been studied (plan progress, past submissions) or asking Om directly. Never assume a concept is known, even a basic-sounding one.
- Close a unit on running code or passing tests alone. Working code does not prove understanding.
- Answer a wrong answer by sending Om away to re-study. Teach it on the spot, then re-check.
- Accept office work as proof unless it meets the office proof path in section 7.
- Invent resources or URLs. Every resource here was checked on 2026-09-25. Recheck before recommending a replacement.
- Reopen settled decisions on argument alone.
- Let a claim outrun the evidence. Beginner hours carry a beginner claim, said out loud.

**Two coaches, one repository.** Claude and ChatGPT are equal peers; Om decides. Their only channel is `omieee/docs` on GitHub:

- Each coach writes only in its own folder, `claude/` or `chatgpt/`, and reads both. Inside each: `tests/<track>/` for test records (section 7), `reviews/` for second opinions (only when Om asks), and `outbox.md` for messages to the other coach, newest on top, each with date and time in IST, subject, ask and an evidence link. A reply goes in the replying coach's own outbox.
- Shared files: `phase1-log.md` (weekly closes, DSA tracker, contingency, later-refactor log) and the two coach logs, `claude-log-entries.md` and `chatgpt-log-entries.md`. A coach writes only its own log and, in `phase1-log.md`, only the rows tied to its own verdicts.
- No interference: a coach never edits, re-scores, re-runs or redoes the other coach's test, verdict or files. One verdict per submission. A second opinion only when Om asks, five lines or fewer, in `reviews/`. A disagreement goes in the outbox with evidence, and Om decides.
- Tool strength sets only tool-bound work: Claude runs repo proofs (fresh clone, tests, planted bugs); ChatGPT runs spoken proofs in voice mode. Either covers any track when needed.

**Reply style:** short, blunt, action-first. Plain words, no em-dashes. Correctness is judged at 100%; polish at 90% is enough.

---

## 1. North star and decisions

**Goals**

- **Phase 1:** clear a five-round Indian senior loop at product companies and GCCs, IBM tier and above, excluding FAANG. Level: Senior (SDE3, MTS-3/4, Senior SE at a GCC). Compensation gate: at least ₹42-45L fixed cash, not CTC.
- **Phase 2:** FAANG-equivalent and Staff readiness, loops from Nov 2027 to Feb 2028 (section 11).
- **Beyond this file:** a senior or staff backend-heavy platform role abroad by March 2028, later AI infrastructure. Relocation is out of scope until the Phase 2 review.

**Role identity, stated exactly:** Senior Backend Infrastructure / backend-heavy Platform / distributed control-plane engineer. Python and Go, Kubernetes, Postgres, distributed systems, production reliability. Never a generic "Senior Platform Engineer", which pulls in DevOps, SRE and Terraform-operations roles.

**Why this exists.** A mass layoff does not read performance reviews. Om watched strong North America teammates get cut, and many were at Google Cloud about a month later. Their skills moved with them. Office work is a bonus; preparation is primary.

**Decisions adopted on Oct 1**

| # | Was (v2.0) | Now (v3.1) | Evidence |
| --- | --- | --- | --- |
| 1 | Go fundamentals learned in office hours at zero cost | Go is a study track: fundamentals, then a real app. Office Go is a bonus, never scheduled | Office Go is about one day a month, on operator code. Zero Go written in September |
| 2 | Kubernetes 13 hrs, hands-on in January | 36 hrs, local kind cluster from October | Cold audit 4.0/15 on 2026-09-24 |
| 3 | Staff as a selective stretch | Phase 1 targets Senior. Staff is an opportunistic stretch only: no Staff preparation, never a top referral spent on a Staff loop | Band 7B, ₹37L CTC and the skill audits all read Senior |
| 4 | Fixed end date Jan 31 2027 | Gates set the end. Forecast (v3.3): Gate A Feb 7 2027, Gate B Jun 20 2027, Gate C Jul 4 2027, at 15 hrs/week, re-forecast monthly from actual hours | 503 hrs from Oct 1: the 490-hour bottom-up estimate plus 13 from the Oct 1 handoff evidence (SQL correction, service repository restart, clean rep 1). 558 after the Oct 5 Python baseline (v3.3). Om authorized up to 575 |
| 5 | Separate `go-probe-runner` toy | The Go app is PRCP's probe agent (data plane) | One coherent system beats two unconnected repos |
| 6 | System design about 20 hrs scheduled | 63.5 hrs including 4 mocks | Top priority at 12 years; Nutanix ran three design rounds in a Jul 2026 loop |
| 7 | Units close on self-report | Units close on proof the assistant verifies (section 7) | Learn, prove, then move |
| 8 | Calibration from November, high-value Dec 20 | Calibration lane from November (2-3 low-stakes), normal volume after Gate A, good referrals after Gate B | Signal early, spend referrals late |

**Unchanged and still frozen**

- Python is the primary implementation and interview language. No Java in Phase 1.
- PRCP is the flagship. `decide(results) -> GateDecision` stays pure: no I/O, no clock, no globals.
- No AI features inside PRCP. AI-assisted engineering is a workflow skill, practised with line-by-line verification.
- No new paid courses, books or certifications without a proven gap. Free official docs and free online references are read by chapter for a named gap, never cover to cover.
- No support-heavy, ops-heavy or generic DevOps role as a target.
- Terraform and public-cloud depth stay conditional on the November JD harvest. Redis and Kafka hands-on stay out.
- CKA is not a Phase 1 study goal. It appears in IBM's Q4 objectives. KodeKloud's CKA course (already owned) is the Kubernetes track's main video and lab source, so if IBM requires CKA, the extra study scope is exam-specific practice only; certification preparation remains office work. Decide before November.

---

## 2. Verified baseline (2026-09-25)

Engineering judgement is at level; tool fluency in Go, Kubernetes and SQL is not. Plan the tracks separately and never slow PRCP, Go or design because DSA is behind.

| Track | Level | Evidence |
| --- | --- | --- |
| Execution | Restarted after long gaps | September: 10 of 30 days with an artifact (Sep 12 and 14 on a parking-lot attempt, then Sep 22-29). PRCP: no commits Aug 13 to Sep 25. `dsa-python`: none Aug 30 to Sep 22 |
| DSA | Early beginner | 21 total / 14 cold on Oct 1. Covered: arrays and hashing, two pointers, sliding window, linked lists. Nothing from stack onward |
| Python | Beginner on the language itself; PRCP code ahead of comprehension | Checklist D baseline Oct 5 (written, cold): 0 solid, 6 shaky, 13 missing (`omieee/docs` `claude/tests/python/2026-10-05-Y2-checklist-D-baseline.md`). PRCP uses pytest fixtures, `with` blocks, route decorators, Protocols and frozen dataclasses, and each of those items came back missing or shaky. PRCP itself, all pre-plan: pure `decide()`, FastAPI, RFC 9457 errors, DI via `dependency_overrides`, 87 tests, 100% coverage, no mypy config |
| Postgres / SQL | Beginner in practice | SQL measured Sep 27 on pgexercises Simple Queries (12 of 12 attempted): unaided on SELECT, WHERE, AND, LIKE, DISTINCT, ORDER BY, LIMIT; hints needed for CASE, date literals and UNION; `IN` and subqueries new; two question-reading misses; joins, GROUP BY, window functions and indexes not yet attempted. Never used a database from Python. Schema `68acbf6` merged to `main` via PR #8 (`7958798`); both databases match git on Postgres 18.6. Service repository not started |
| Go | Beginner | No Go written at CDP. `learning-go-sandbox` has two frozen exercises. Pointers and references not yet understood |
| Kubernetes | Mental model real, tooling and vocabulary missing | Cold audit 4.0/15 (debugging 2.5/10, architecture 1.5/5). Strong on the post-`kubectl apply` reconciliation chain. Missing: Service and kube-proxy, StatefulSet vs DaemonSet, RBAC, rollout commands, ConfigMap env vs volume, cluster DNS |
| Docker, CI, observability | Minimal | Postgres runs in a container. No Dockerfile in any repo. GitHub Actions exists, no self-gating. No metrics |
| System design, machine coding | Not started | Machine coding: one parking-lot attempt on Sep 28 (109 min, AI-written tests and one AI fix), logged as practice, not a rep. System design: no study, no mocks |
| Stories | 2-3 honest | IBM registry cost reduction (reconcile the savings figures first), IKS upgrade programme, Circuit Breaker plus deployment gate. The rest must be earned at work |
| Profile | 12 years, 5 at IBM | IBM Band 7B. CTC ₹37L. Notice period 3 months (IBM India) |

---

## 3. How the market reads you

Recruiters will slot the profile as Senior, and the loop sets the final level. Every senior loop found tests three things: coding, design, and a deep dive on your own work. Kubernetes questions come up directly inside those rounds; Go is tested through language questions and your own system.

**HR and recruiter screen**

- Naukri recruiters search by keyword, then filter by experience range, location, salary budget and notice period ([Naukri](https://www.naukri.com/blog/recruiter-resdex/)). Blank or out-of-range fields drop a profile before anyone reads it.
- Bengaluru Senior engineer pay on Levels.fyi: 25th percentile ₹36.3L, median ₹53.5L, 75th percentile ₹77.4L (Dec 2025 snapshot, to be refreshed in the November harvest, [Levels.fyi](https://www.levels.fyi/t/software-engineer/levels/senior/locations/bengaluru-ind)). ₹37L CTC at 12 years sits near the 25th percentile of Senior pay.
- Recruiters who know IBM bands may read 7B at 12 years as mid-level. Answer with scope and proof, not the band.
- A normal lateral switch is quoted at 20-35%, less in percentage terms for seniors ([Pathwise](https://www.pathwisecareer.com/resources/salary-hike-switching-jobs-india)). On ₹37L that is ₹44-50L CTC, so fixed cash lands near the gate. Price against the role's band, not against current CTC.
- Years alone point to Staff: Nutanix posts Staff roles at 12+ years ([Nutanix NKP Staff](https://careers.nutanix.com/en/jobs/32362/staff-engineer-nutanix-kubernetes-platform-nkp/)). Pay, band and skills point to Senior. **Target Senior.**
- The loop moves the level. One Intuit candidate interviewed for SE-2 and was offered Senior on performance ([LeetCode](https://leetcode.com/discuss/interview-experience/1744259/intuit-senior-software-engineer-bangalore-offer)).

**Hiring manager view at 12 years.** They grade ownership, not tasks: what you decided, what you rejected and why, how you ran an incident, whom you mentored, what changed because of you. "I executed assigned tickets" gets levelled down.

**Recent loops, India, non-FAANG**

| Company | Reported loop | Source |
| --- | --- | --- |
| Razorpay, Jul 2026 | Agentic coding (90 min), LLD + HLD (90 min), hiring manager on delivery and leadership, leadership rounds, HR. Every round eliminates | [Glassdoor](https://www.glassdoor.co.in/Interview/Razorpay-Interview-Questions-E1146550.htm) |
| Razorpay, machine coding | Often an in-memory relational datastore with keys, indexes and constraints; a new requirement arrives mid-session | [DesignGurus](https://www.designgurus.io/answers/detail/what-is-the-razorpay-interview-process-like-round-by-round) |
| Nutanix Bengaluru, Jul 2026 | Coding, three system design rounds, hiring manager; distributed systems and infrastructure focus | [Glassdoor](https://www.glassdoor.com/Interview/Nutanix-Interview-Questions-E429159.htm) |
| Nutanix, Apr 2026 | Hiring manager, two DSA, one design | [Glassdoor](https://www.glassdoor.co.in/Interview/Nutanix-Bangalore-Interview-Questions-EI_IE429159.0,7_IL.8,17_IM1091.htm) |
| Nutanix, other reports | A hiring-drive machine coding round on a thread-safe distributed job scheduler; an MTS round on navigating an unfamiliar database driver codebase | [CodingKaro](https://www.codingkaro.in/jobs-internships/leetcode-interview-experience/Nutanix), [LeetCode](https://leetcode.com/discuss/interview-experience/7429281/) |
| Intuit, Senior | Craft demo: present your strongest project, code tasks live, design and tests weighted, every line defended. Then DSA, LLD or HLD, hiring manager. One report adds a 30-min AI concepts round. Pass rate 31% across 42 reports | [LeetCode](https://leetcode.com/discuss/post/7171528/intuit-interview-expereince-senior-softw-bd8i/), [Taro](https://www.jointaro.com/interviews/companies/intuit/experiences/senior-software-engineer-bengaluru-august-12-2025-accepted-offer-positive-d72c7f65/) |
| Intuit, Sr Staff | Asked how to debug a blocked application in Kubernetes | [Glassdoor](https://www.glassdoor.ie/Interview/Intuit-Interview-E2293-RVW89865621.htm) |
| Flipkart SDE3, Jul 2025 | Screen, machine coding, DSA, HLD, hiring manager | [Glassdoor](https://www.glassdoor.com/Interview/Flipkart-SDE3-Interview-Questions-EI_IE300494.0,8_KO9,13.htm) |
| ServiceNow, Senior | DSA, HLD, LLD, hiring manager. A Dec 2025 candidate reports repeated AI questions | [TechPrep](https://www.techprep.app/blog/servicenow-interview-process), [Glassdoor](https://www.glassdoor.com/Interview/ServiceNow-Senior-Software-Engineer-Interview-Questions-EI_IE403326.0,10_KO11,35.htm) |

**What this means for preparation**

1. **Three constants:** a coding round (DSA, machine coding or both), design rounds, and a deep dive. Prepare all three every month.
2. **Go and Kubernetes are questioned inside technical and deep-dive rounds,** not in rounds of their own, and most of all through your own system. PRCP plus the Go agent on kind is your proof.
3. **Reading unfamiliar code is tested.** Section 6 has three code-reading drills.
4. **Machine coding decides at build-round companies:** working code, a clean model, and absorbing a mid-session change.
5. **AI shows up two ways:** an AI-assisted build round (Razorpay) and AI concept questions (ServiceNow, Intuit). The first is trained in rep 5. The second is a watch item for the JD harvest: concepts only, never features in PRCP.
6. **Phase 2 formats are not frozen here.** FAANG-tier AI-era rounds are re-researched when Phase 2 starts.

Limits: these reports are self-reported and skew to well-documented companies. Mid-size GCCs, your likeliest segment, are thinly covered. Confirm each loop with the recruiter before preparing.

---
## 4. Phase structure and gates

Phase 1 exits on gates, not dates. At 15 hrs/week the forecast is Gate A Feb 7 2027, Gate B Jun 20 2027, Gate C Jul 4 2027 (v3.3). Re-forecast monthly from actual hours; a slip moves the date, never the scope.

| Phase | Window | Hours | Scope |
| --- | --- | --- | --- |
| Bridge | Sep 26-30 2026 | ~8 | 25-min floors, machine coding rep 1, psycopg `Service` repository with a rollback test, office-Go test recorded |
| 1a Foundations | Oct 1 2026 - Feb 7 2027, W0-W18 | 250.5 | Go fundamentals. Python core. Kubernetes on kind: architecture, workloads, networking, config and RBAC, scenarios 1-5. PRCP persistence, SQL fluency, Postgres internals, SQLAlchemy and Alembic. LLD foundations, rep 2. HLD framework and building blocks. Insurance pack, stories |
| 1b Build and design | Feb 8 - Jun 20 2027, W19-W37 | 282.5 | Go agent. Docker, CI self-gating, metrics. Both apps on kind, scenarios 6-10. Distributed systems, practice designs, mocks 1-3. Reps 3-5. Python classes and data model, Python depth, a PRCP code walk. Load experiment, concurrency, networking and OS with real tools, gRPC, API security. PRCP v1.0 and a game day |
| 1c Convert | Jun 21 - Jul 4 2027, W38-W39 | 25 | Rep 6, mock 4, deep dive, DSA finish, checklist re-runs, Gate C. Light on purpose: interviews peak here |

**Gate A (Feb 7).** Every item, verified per section 7:

- Go practical: a package built from scratch with a struct, pointer receiver, interface, wrapped errors, slice and map, and table-driven tests. No AI; standard-library docs only after a first full attempt.
- Checklist B fundamentals half at 7/10 cold, zero correctness errors.
- Kubernetes audit at 10/15, with no zero on API server, etcd, scheduler, controller manager, kubelet, or Service and endpoints.
- PRCP integration tests green on a fresh clone; Alembic upgrade and downgrade round-trip.
- 3 timed SQL problems, 20 min each. Postgres internals set at 7/10. EXPLAIN ADR. Two-session isolation and deadlock demos.
- Checklist D baseline run. DSA 40 total / 24 cold. Machine coding reps 1 and 2 scored.
- Insurance pack live: resume v1, Naukri, LinkedIn, 60-second pitch. 2-3 stories told aloud.

**Gate B (Jun 20).**

- Craft-demo ready: a stranger runs PRCP from the README in 5 minutes, and you defend any line for 30.
- Agent: `go test -race ./...` clean, leak lab written up. Full Checklist B at 7/10.
- Kubernetes audit at 10/15 plus a live debugging challenge on your own cluster. Checklist C at 7/10.
- Checklists A and D at 7/10. Metrics, one symptom alert, self-gating CI green.
- 3 design mocks, at least 1 with a human, each at 11/16 or better with no zero.
- DSA 50 / 34, all 16 families touched, and the latest blind mixed set before the gate (W32) at 80% or better solved without hints, Mediums in 30-35 min.
- Machine coding reps 1-5 done, and the latest two pass the rubric (runs end to end, 8/12 or better).
- Story checkpoint: 4 defensible stories. Fewer is PARTIAL, not a blocker, except for top referrals (below).

**Gate C (Jul 4).**

- DSA 55 / 40-45 cold, plus the performance gate: 10 previously solved problems aged 14+ days, picked at random, 8 solved without hints, Mediums in 30-35 min, approach and complexity aloud.
- 6 machine coding reps. 4 mocks, at least 2 with humans, the last two at 12/16 or better.
- Every checklist at 7/10 on a cold re-run. 30-minute PRCP deep dive, timed.
- Resume v2 live. 5 stories: at least 3 recent and 2 leadership, never invented. Fewer is PARTIAL and never blocks applications.

**Applications**

- October: the insurance pack goes live whatever the phase, because a layoff can land any week.
- From W5 (Nov 2): a calibration lane of 2-3 low-stakes processes. No good referrals.
- After Gate A: normal calibration volume. After Gate B: good referrals. 1c: full push.
- **Top referrals** (the few you cannot afford to waste) also need 3 strong production stories that between them cover an architecture decision you owned, an incident or reliability story you owned, and cross-team leadership. One story may cover several. Calibration and normal applications never wait for this.
- No FAANG-tier loops in Phase 1, not even as calibration: a failed loop can lock you out of re-applying for months and spends referrals Phase 2 needs. Take one only if a real opportunity comes to you and you accept that cost on purpose. Interview hours come from the campaign reserve, never on top of the weekly 15.
- Notice period is 3 months, so an offer after Gate B means joining around October 2027 unless IBM agrees to an early release. Keep the plan running through the notice period.

---

## 5. Track priorities and hours

**Scheduled from Oct 1: 558 hours.** The 490-hour bottom-up estimate at beginner rates (rates table below) plus 13 hours the Oct 1 handoff proved necessary: SQL correction from the measured Sep 27 level (+7), the service repository restarting from zero with a psycopg prerequisite (+3), and a clean rep 1 because the parking-lot attempt used AI (+2.5, half an hour already inside P1). Then 55 hours the Oct 5 Python baseline proved necessary (v3.3): Python depth re-estimated from the measured level at realistic rates (+44), Python prerequisites before P1 (+1.5), a Checklist A baseline (+0.5), and DSA, weekly close and proofs in the three weeks this adds (+9). Om authorized up to 575: if measured actuals run slower than these rates, a track's remaining hours rise by the measured amount, up to that ceiling. A script checked every week, unit and track. Credited before Oct 1 and not counted: the schema (4 hrs), pgexercises Simple Queries, and the September cold re-solves.

| Track | Priority | Hours from Oct 1 | Notes |
| --- | --- | --- | --- |
| PRCP: Postgres 45, Python depth 71.5, Docker 8, CI 8, observability and load 11, finish and game day 11 | Very high | 154.5 | SQL correction from the measured Sep 27 level; Python from the Oct 5 baseline |
| Go: fundamentals 30, PRCP agent 35 | Very high | 65 | Starting from zero, pointers included |
| Kubernetes on kind | Very high | 36 | Ten scenarios at about 45 minutes each |
| HLD and distributed systems 51.5, mocks 12 | Very high | 63.5 | Starting from zero; the round that sets level at 12 years |
| LLD 18, machine coding reps 1-6 15 | Very high | 33 | Rep 1 is a clean Snake and Ladder rep in W0 |
| DSA | High, daily | 117.5 | Early beginner; breadth first, depth is Phase 2. Includes 7.5 for the three weeks v3.3 adds |
| Supporting: concurrency 5.5, networking 8, gRPC 3, OS 5, API security 6, cloud vocabulary 4 | Supporting | 31.5 | Tool-based practice; concurrency starts with a Checklist A baseline |
| Stories, resume, narratives | Insurance | 24 | Two deep dives, five stories |
| Verification and governance: unit proofs and weekly close 18, gates 14, Oct 1 procedure 1 | Required | 33 | Hidden hours made visible |
| **Total** | | **558** | 1a 250.5, 1b 282.5, 1c 25 |

**How the hours were estimated.** Assistants re-estimate from these rates and from actuals, never by feel.

| Activity | Rate | Why |
| --- | --- | --- |
| New video or text | 1.5x its run time | Pausing, notes, rewinding |
| Coding in a new tool (Go, SQL, asyncio, manifests) | About 1.5-2x a fluent engineer's time | First time in the tool |
| DSA NEW problem | 45 min Easy, 90 min Medium, plus a 50-minute lesson per new family | Early-beginner composition |
| DSA cold re-solve | About 13 min | Time-boxed 10 min Easy, 15 Medium |
| Kubernetes scenario | About 45 min, including the write-up | Reproduce, diagnose, fix, note |
| Design building block | About 1 hour | Learn, then explain cold |
| Practice design | 2.5 hours | Skeleton, spoken run, scored review |
| Design mock | 3 hours | Prep, the mock, review |
| Machine coding rep | 2.5 hours | 90 minutes plus a 60-minute review |
| Story | About 1.5 hours | Draft, reconcile numbers, tell aloud |
| SQL exercise at the measured level | About 10 minutes, after its concept lesson | Sep 27 baseline |
| Unit proof | About 15 minutes | Section 7 |
| New Python concept from zero (v3.3) | About 2.5-3 hours | 10 minutes to open and find the section, the video at 2x its run time, a short text pass, a guided example, a kata with tests, the unit interview with repair |
| Small follow-on Python topic (v3.3) | About 1.5 hours | Builds on a topic just learned |

**Capacity.** Target 2.5 hrs/day, 17.5/week. Normal weeks schedule 15; light weeks (W0, Diwali W5, W12, W13) schedule 8. No week exceeds 15. Floor on bad days: 25 minutes. The unscheduled gap across normal weeks is about 100 hours: about 50 for the job campaign (applications, JD harvest, interviews, monthly story rehearsal), never spent on study, and about 50 of contingency.

**Pace check.** Estimates count every overhead (opening the book or video, finding the section, rewatching, setup) and the prerequisite topics; hours are never compressed to keep a number small. Every weekly close records actual vs planned hours for each unit closed. From the W2 capacity check, a track whose measured pace is slower than its rate has its remaining hours raised by that ratio, up to the 575 ceiling; if that ceiling would break, Om decides with the data. Other tracks keep the rates above until their actuals say otherwise.

**Counted wherever it happens.** Required watching or reading counts in its unit's hours wherever you do it, bedside included, and goes into the weekly actual hours. Optional extra passes are bonus and are not counted.

**Capacity check at W2 (Oct 18).** Compute the average weekly hours since Oct 1. Under 10 means re-forecast the gate dates that Sunday instead of waiting for month-end. After that, re-forecast monthly from actual hours.

**Contingency is separate.** Every unit now has its full time built in, so contingency is only for life events and genuine surprises. If a unit still runs long, finish the proof, take the time from contingency, and log it in the weekly close. More than 10 hours of contingency used triggers a re-forecast. The weekly target stays at 15 until four straight weeks at or above plan justify raising it.

**Cut order** when interviews or life take hours, or contingency is spent. Cut, never stack on top:

1. PRCP polish
2. Observability depth
3. Docker and CI polish
4. Go work beyond agent v1
5. Narrative polish

**Never cut:** daily DSA, Python and Go fluency, LLD and machine coding, spoken design, stories, PRCP tests, Postgres, Kubernetes core.

**Extras queue.** Not scheduled. Each item is pulled only when its trigger is met, through these rules:

1. The trigger evidence (JD harvest count, repeated loop question, or mock feedback) is recorded in a weekly close.
2. One extra is active at a time, and never before its earliest pull point.
3. It is funded one-in, one-out from the section 5 cut order or from contingency, never from DSA, design, machine coding or stories.
4. It carries a beginner claim until its proof passes, and the script re-runs and the dates re-forecast.

| Extra | Hrs | Trigger | Earliest pull |
| --- | --- | --- | --- |
| One public cloud, practical translation (the provider the harvest names most) | 8 | That provider in 40% of accepted-role JDs | After Gate A |
| Terraform and IaC literacy | 4 | Terraform or IaC in 40% of accepted-role JDs | After Gate A |
| Kafka locally plus a rejection ADR | 8 | 40% of harvested JDs, or asked in 2 real loops | After Gate A |
| Redis locally (cache-aside for gate reads, a rate limiter) plus an ADR | 6 | 40% of harvested JDs, or asked in 2 real loops | After Gate A |
| OpenTelemetry tracing implementation (tracing concepts are already core in O1) | 7 | 40% of harvested JDs | After O1 |
| Controller mechanics lab: a tiny reconcile loop with client-go informers against a ConfigMap | 6 | Controllers or operators required in 40% of accepted control-plane JDs, or asked in 2 loops | After Gate B; otherwise Phase 2 |
| AI concepts for interviews (LLM vs classical ML, RAG and evaluation basics), concepts only | 4 | AI questions in 2 real loops, or 40% of JDs | Any time |
| System design extension | 4 | Mock feedback names a gap | Any time |

---

## 6. Curriculum by track

Each track lists its depth bar, ordered units with hours and proof, then resources: video first for the mental model, official docs as the authority. Units run in order inside a track; tracks run in parallel; section 14 places every unit in a week. Resource keys (NC, LGWT and so on) are defined in section 14.

**The week row picks the resource.** Never browse the resource key for more material, and no resource needs finishing: each one exists only to serve its named unit.

**Docs are for lookup, not learning.** Learn from the videos, texts and labs listed. When a claim is going into an ADR or an interview answer, confirm it in the official docs: a two-minute lookup, not a chapter. Videos and blogs carry their own assumptions and go stale, so the docs stay the final word on facts.

### 6.1 PRCP core: Python, Postgres, Docker, CI, metrics (154.5 hrs from Oct 1)

**Depth bar.** You can build, test and defend every layer of PRCP from memory: SQL written by hand, database behaviour under concurrency, the Python runtime under load, and a container that starts and stops cleanly.

| Unit | Hrs | Content | Proof |
| --- | --- | --- | --- |
| P1 Access layer | 9.5 | Python prerequisites first (1.5h, from the Oct 5 baseline): context managers and `with`, pytest fixtures with `yield`, dataclass equality. Then the psycopg prerequisite: install with `uv add "psycopg[binary]"`, read psycopg 3 Getting Started (basic usage, passing parameters, transactions management), and run a 15-line insert, select, rollback script against `prcp_test` (practice, not committed). Then raw-SQL repositories for Service, Environment, Probe, ProbeResult, GateDecision, with integration tests on `prcp_test`, one transaction rolled back per test. GateDecision links to the ProbeResults it used | Practice output pasted. Tests green on a fresh clone. Explain connection vs cursor vs transaction, parameter binding, what rollback undoes |
| P2 SQL correction and fluency | 14.5 | From the Sep 27 baseline, lesson before exercise: SQLBolt lessons on joins, outer joins, NULLs, aggregates and order of execution, plus its subqueries and set-operations topics (`IN`, `UNION`); a window-functions lesson. Then pgexercises in order: Joins and Subqueries, Aggregation, Working with Timestamps, Modifying Data; skip Recursive and String. Method: restate the asked output (columns, rows, limits, singular or plural) before writing; build a subquery by running the inner query alone first. Then 3 timed problems | Queries in `omieee/docs` `sql/pgexercises.sql` with a one-line note each. 3 unseen problems on a new schema, 20 min each |
| P3 Postgres internals | 12 | B-tree and composite index order, index-only scans, `EXPLAIN ANALYZE` and join types, isolation levels and anomalies including write skew, MVCC, row locks and deadlocks, WAL on commit, pooling, replication and failover, VACUUM. Code-read: how `psycopg_pool` hands out a connection | ADR with real `EXPLAIN` output. Two `psql` sessions showing a non-repeatable read and a deadlock, both explained. Internals set 7/10 |
| P4 SQLAlchemy 2.0 and Alembic | 9 | Port the repositories, keep the same tests. Main migration proof: expand, backfill, contract, with old and new app versions running together. A quick N+1 check if time remains | Old and new versions both work mid-migration; upgrade and downgrade round-trip. Explain the Session |
| Y1 Typing | 4 | PRCP has no mypy config yet. Type hints, `Optional`, generics, `Callable`; install and configure mypy; then `mypy --strict` clean on `src/prcp/` | Clean run on a fresh clone |
| Y2 Baseline | 1 | Checklist D cold. Only gaps that block current PRCP work move into 1a; the rest wait for Y3 and Y8. Done Oct 5: 0 solid, 6 shaky, 13 missing. The P1 blockers are taught at P1's start (P1 row) | Scored gap list |
| Y3 Python core | 22.5 | Sized from the Oct 5 baseline, done by Gate A: names and references, `is` vs `==`, mutability (2.5); shallow vs deep copy (1.5); hashing, `__eq__` and `__hash__`, container costs (3); iterables and iterators (2.5); generators (2.5); functions as objects, `*args` and `**kwargs`, scope, closures (3); decorators (3); exceptions, `raise from`, custom exceptions (2.5); context managers in depth, `contextlib` (2) | One tested kata per topic; unit interview per topic |
| Y4 asyncio | 14 | From zero first: coroutines vs functions, `await`, the event loop, tasks. Then `TaskGroup`, semaphores, cancellation, timeouts. Bounded async probe fan-out. Block the loop on purpose, observe it, fix it with `asyncio.to_thread` | Commit plus a one-page starvation write-up |
| Y5 GIL and profiling | 7 | Threads from zero (start, join, a shared-counter race). Threads vs processes vs asyncio; why the GIL does not make `x += 1` atomic; `cProfile` on the fan-out | A thread race and its lock fix, with a test. Before and after numbers |
| Y6 Test depth | 4.5 | pytest beyond the basics: fixture scopes, `conftest.py`, parametrize, `monkeypatch`, `tmp_path`; a Hypothesis property test on `decide()` | The property test catches a bug the assistant plants |
| Y7 PRCP code walk | 5 | Every pre-plan module of PRCP, read cold: Pydantic schemas, FastAPI `Depends` and `dependency_overrides`, Enums, exceptions, `conftest.py` fixtures, repositories, `decide()`. Explain each module's job and every line an interviewer could ask you to defend; fix what you cannot defend, or log it | Each module explained without notes; findings file committed |
| Y8 Classes and data model | 13.5 | Classes from the ground up, special methods, `classmethod` and `staticmethod`, `Enum` (3); dataclasses in depth (2.5); inheritance, MRO, `super()` (2.5); ABC vs Protocol (2.5); reference counting and GC (1.5); Checklist D cold re-run and repair (1.5) | One tested kata per topic; Checklist D 7/10 at Gate B |
| D1 Docker | 5 | Multi-stage Dockerfile, non-root user, `.dockerignore`, Compose with Postgres and healthchecks | `docker compose up` on a fresh clone reaches healthy |
| D2 Container internals | 3 | Namespaces, cgroups, layers and copy-on-write, PID 1 and SIGTERM | Graceful shutdown on `docker stop`; explain cgroups vs namespaces |
| C1 CI and self-gating | 8 | Lint, mypy, tests, coverage, image build. PRCP gates its own release | Green run. A planted failing probe blocks the release |
| O1 Metrics, load and SLO | 11 | `/metrics`, `/live`, `/ready`. Counter, gauge, histogram, label cardinality. A controlled load experiment: throughput, p50/p95/p99, the saturation point and one observed bottleneck, with before and after numbers. RED and USE. SLI and SLO for the gate. JSON logs with a correlation ID. One symptom-based alert rule. Tracing concepts: trace, span, context propagation, sampling, correlation with logs and metrics | Load report with numbers. PromQL against your own metrics. Alert rule file. Explain why it alerts on symptoms |
| F1 Finish v1.0 and game day | 11 | ADR index. README that leads with the verdict. A short ADR on why not Keptn, Argo Rollouts or Flagger (the deep dive needs it). Known limitations. Tag `v1.0.0`. Then a game day on kind: inject a database or probe-timeout failure, let the alert fire, diagnose, mitigate, and write a postmortem and runbook | Stranger test: the assistant runs it from the README alone in 5 min. Postmortem and runbook committed |

**Resources:** learn from SQLBOLT and PG-TUT (P2 concept lessons), INTERDB (the main text for P3), UTIL, CMU, HN, TS-ISO, PGEX, RP (first read for Y3 and Y8), FLUENT (second pass for Y3 and Y8, named chapters only), RP-ASYNC (the main text for Y4), BEAZ, MCODING, ARJAN, NANA-DOCKER, VEGETA (load generator for O1). Look up in PSY, SQLA, ALEMBIC, PG, PYDOCS, MYPY, PYTEST, HYP, DOCKER, GHA, PROM, USE, SRE (ch 6).

**Not in Phase 1:** Redis and Kafka hands-on, Grafana, OpenTelemetry implementation, other ORMs.

### 6.2 Go: fundamentals, then the PRCP probe agent (65 hrs)

**Depth bar.** You write Go fundamentals without lookups, and you can defend a concurrent service you built: why each goroutine exits, who cancels it, and how you would prove there is no leak. Office Go is a bonus and never counts toward a gate unless it meets the office proof path.

**The agent's contract.** The Go agent is PRCP's data plane. It loads a static JSON config, runs HTTP probes where the service lives, and pushes `ProbeResult`s to the Python control plane. It never decides: `decide()` stays in Python and stays pure. Non-goals: no cluster discovery, no controller, no Kubernetes API calls. Its only concurrency model is `errgroup` with `SetLimit`; hand-built channel worker pools stay in the sandbox. PRCP's Python async runner (Y4) is the local reference runner and a Python concurrency lab, frozen at Y4 scope. The Go agent is the only deployable external execution path, and every new probe feature goes there. Both emit the same `ProbeResult` contract.

| Unit | Hrs | Content | Proof |
| --- | --- | --- | --- |
| G1 Setup and basics | 3 | Toolchain, modules, `go test`, `go doc`. Learn Go with Tests: Hello World, Integers, Iteration | Tests green in `learning-go-sandbox` |
| G2 Slices | 3 | Arrays vs slices, length vs capacity, `append` growth and aliasing | A test proving two slices share a backing array, explained cold |
| G3 Types | 4.5 | Structs, methods, interfaces, implicit satisfaction, embedding, value vs pointer receivers | Kata with tests; explain which receiver and why |
| G4 Pointers and errors | 5 | `*` and `&`, nil, the nil-interface trap, `errors.New`, `%w`, `errors.Is` and `errors.As`, `defer`, panic and recover | A test showing the nil-interface trap; a wrapped-error test |
| G5 Maps and generics | 3 | Map semantics, why concurrent map writes crash, generics basics | Kata with tests |
| G6 Design for tests | 4.5 | Dependency injection, interfaces as seams, table-driven tests with `t.Run`, `httptest` | A table-driven test for an HTTP handler |
| G7 Concurrency basics | 7 | Goroutines, buffered vs unbuffered channels, `select`, closed-channel reads, `sync.Mutex` vs `RWMutex`, `WaitGroup`, `context`. The scheduler model (G, M, P) and GC basics, at interview level. Hand-built worker pool in the sandbox only | Feeds Gate A: Go practical plus Checklist B fundamentals half |
| A1 Sequential agent | 6 | Load config, run probes one by one with `net/http`, per-probe `context.WithTimeout`, results match PRCP's `ProbeResult`. Code-read the timeout fields of the `net/http` Client | Table-driven tests with `httptest`, including a slow server that must time out |
| A2 Bounded concurrency | 8 | `errgroup` with `SetLimit`, cancellation through every goroutine | `go test -race` clean under load. Explain who cancels what |
| A3 Push to control plane | 5 | POST results, bounded retries with backoff and jitter, an idempotency key per batch that the server de-duplicates, a service token | Test: a duplicate push creates no duplicate rows |
| A4 Operability | 5 | `log/slog` JSON logs, Prometheus `client_golang` metrics, graceful shutdown with `signal.NotifyContext`. Code-read how a `client_golang` histogram records a value | SIGTERM drains in-flight probes; metrics scraped |
| A5 Leak lab | 6 | Remove a timeout, watch goroutines climb, find it in the pprof goroutine profile, fix it, add a goroutine-count test | Write-up with before and after counts |
| A6 Ship it | 5 | Static binary in a small image; ADR on the control-plane and data-plane split | Image builds in CI; ADR merged |

**Resources:** FCC-Go (video, by chapter), LGWT (primary text), PIKE, GO100 (the classic Go traps with examples; it maps onto Checklist B), GOBYEX (for "how do I do X" instead of package docs), GO-SLICES, GO-ERRORS, GO-CONTEXT, GO-PIPELINES, GO-PPROF, GO-SLOG, ARDAN (scheduler and GC series; its Kubernetes CPU and memory limits articles also serve K7 scenario 6). Look up in EFFGO, ERRGROUP, CLIENTGO, or `go doc <pkg>` in the terminal.

**Not in Phase 1:** controller-runtime and CRDs, reflection, escape-analysis tuning, gRPC implementation in Go, CLI frameworks.

### 6.3 Kubernetes on kind (36 hrs)

**Depth bar.** You explain the control plane by component name, drive `kubectl` without notes, and diagnose the ten scenarios on your own system. The audit showed the mental model is real; this track adds names, commands and saying it out loud.

| Unit | Hrs | Content | Proof |
| --- | --- | --- | --- |
| K1 Cluster and kubectl | 4 | kind cluster, contexts, namespaces, `get`, `describe`, `logs`, `exec`, `port-forward`, `-o yaml`, `explain`, events sorted by time | Cold drill: 10 tasks, no notes, 8 correct |
| K2 Architecture | 5 | API server, etcd, scheduler, controller manager, kubelet, kube-proxy, CoreDNS; the full chain after `kubectl apply`. Controller anatomy at concept level: watch, informer cache, work queue, reconcile as an idempotent move toward desired state, requeue with backoff, finalizers, owner references, leader election | Narrative, no notes, 7/10 |
| K3 Workloads | 6 | Pod lifecycle, Deployment to ReplicaSet, rollout status, history and undo. StatefulSet vs DaemonSet vs Job and CronJob. Requests vs limits, QoS. Liveness, readiness and startup probes. HPA vs VPA vs cluster autoscaler, in concept | Each object applied, changed and rolled back on kind |
| K4 Networking | 4 | Service types, EndpointSlices, the Service dataplane: kube-proxy in iptables mode is one implementation and some network plugins replace it; skip IPVS internals, which the docs expect to deprecate. Cluster DNS path, Ingress basics, NetworkPolicy in concept. CNI vs CSI at architecture level | Trace a request from a pod to a Service name, step by step |
| K5 Config and access | 4 | ConfigMap as env vs volume and what happens on change, Secrets, ServiceAccounts, Role and RoleBinding, least privilege, as a standalone lab | A denied API call, fixed with the smallest Role |
| K6 Deploy PRCP | 5 | Postgres, the PRCP API and the Go agent on kind. Services, ConfigMap, Secret, probes, limits. The agent's ServiceAccount sets `automountServiceAccountToken: false` and gets no Role | Manifests in the repo; the assistant deploys them from a fresh clone |
| K7 Debugging drills | 8 | The ten scenarios below: 1-5 in KodeKloud's troubleshooting labs or on a sample app in 1a; 6-10 on PRCP in 1b. KodeKloud's control-plane and worker-node failure labs, which kind cannot easily simulate, are optional bonus only if K7 time remains; they are not Gate B requirements and never add Kubernetes hours. Each goes into `k8s-notes.md`: symptom, commands, cause, fix | Broken state reproduced, `kubectl` output pasted, fix committed, cold explanation |

**The ten scenarios:** (1) CrashLoopBackOff using `logs --previous`; (2) Pending: resources vs taint vs unbound PVC; (3) OOMKilled; (4) a Service with no endpoints; (5) an object stuck on a finalizer, and a namespace stuck Terminating (reading events by time is a K1 tooling skill); (6) CPU throttling vs a memory-limit kill; (7) an aggressive liveness probe killing pods under load; (8) a bad rollout: status, history, undo; (9) ConfigMap as env vs volume after an update; (10) DNS resolution failing inside a pod.

**Resources:** KK (owned; the main Kubernetes video and lab source: lectures plus in-browser lab clusters with auto-checked practice tests; use only the lessons each week names, never the whole course), K8SAF (one real postmortem a week for K7 and for incident talk), KIND, K8S (Concepts, Debug tasks, [RBAC good practices](https://kubernetes.io/docs/concepts/security/rbac-good-practices/), [Virtual IPs and Service Proxies](https://kubernetes.io/docs/reference/networking/virtual-ips/)), LEARNK8S. NANA-K8S only if a KodeKloud lesson does not click. `kubectl explain <resource>` in the terminal.

**Not in Phase 1:** operators and CRDs, Helm chart authoring, service mesh, CKA preparation, multi-cluster.

### 6.4 HLD and distributed systems (63.5 hrs)

**Depth bar.** In 45 minutes, out loud, you take an open problem to requirements, numbers, an API, a data model, a working design and a failure story. Every choice comes with the option you rejected and why.

| Unit | Hrs | Content | Proof |
| --- | --- | --- | --- |
| H1 Framework | 5 | Functional and non-functional requirements, back-of-envelope estimates, API, data model, high-level design, deep dive, bottlenecks | One design on paper, graded step by step |
| H2 Building blocks | 12 | L4 vs L7 load balancing, caching and invalidation, CDN, queue vs pub/sub, rate limiting, object storage with presigned uploads, WebSocket vs SSE vs polling, ID generation, storage selection: relational, key-value, document, wide-column, search, time-series | For each: when, what it costs, what breaks. 7/10 cold |
| H3 Distributed data | 9 | Leader and follower replication, sync vs async, lag. Hash vs range partitioning, consistent hashing, hot keys. Linearizable, eventual and read-your-writes consistency. Quorums | A quorum read and write explained with numbers |
| H4 Coordination and failure | 13 | Leader election, leases, split brain, what Raft solves. Partial failure and timeouts. Retries with backoff and jitter, idempotency. 2PC vs Saga vs outbox. Delivery semantics, consumer groups, DLQ, backpressure. Multi-region, active-passive vs active-active, RTO and RPO | A retry-storm scenario diagnosed and fixed in writing. 7/10 cold |
| H5 Practice designs | 12.5 | Multi-tenant PRCP at 10,000 services (tenant boundary, data isolation, quotas, noisy-neighbour protection, per-tenant rate limits, blast radius), a job scheduler, a payment or reservation system with idempotency and reconciliation, a distributed rate limiter, a notification service. Each: a one-page skeleton, then spoken against the clock | Scored spoken run per design |
| H6 Mocks | 12 | Mock 1 with the assistant; mocks 2-4, at least 2 with humans who interrupt | Section 7 rubric per mock |

**Resources:** HI (Core Concepts, Key Technologies) and HI-YT, KLEP (lectures 5.1-7.3 map to H3 and H4), BBG (5-10 minute visual refreshers, good for bedside time), SRE (ch 21, 22, 23), PRIMER.

**Human mocks:** if two peer interviewers are not lined up by Feb 1 2027, book paid expert mocks per section 6.9, 1-4 weeks before a real high-value loop.

**Not in Phase 1:** DDIA cover to cover (Phase 2), Raft implementation, Kafka or Cassandra internals, staff-level org strategy.

### 6.5 LLD and machine coding (33 hrs from Oct 1)

**Depth bar.** In 90 minutes you ship working Python with a clean domain model, absorb a new requirement mid-session without a rewrite, and defend every class. Priority when time runs short: working code, domain model, extensibility, readability, tests, concurrency. A pattern appears only because it solved a problem.

| Unit | Hrs | Content | Proof |
| --- | --- | --- | --- |
| L1 OOP foundations | 3 | Four pillars, interfaces vs abstract classes, association vs aggregation vs composition, coupling and cohesion, composition over inheritance | Each explained in two sentences cold, 7/10 |
| L2 SOLID | 5 | All five principles with Python examples; Liskov violations are the classic senior trap | A violation and its fix for each, in code |
| L3 Patterns and diagrams | 7 | Strategy, Factory, Observer, State, Decorator. Recognise Builder and Singleton. Minimal class and sequence diagrams | One kata per pattern; a diagram of rep 2 |
| L4 Thread-safe design | 3 | Locks, `queue.Queue`, where the lock goes, lock granularity | A thread-safe class with a test that fails without the lock |
| MC1-MC6 | 15 | Six reps, 90 min each plus a 60-minute review. A session under 90 minutes, or one with AI-written code outside rep 5, is practice, not a rep. Commit raw notes before any cleanup | Section 7 machine-coding rubric |

**The six reps:** (1) Snake and Ladder, diagnostic, W0 (the Sep 28 parking-lot attempt is logged as AI-assisted practice); (2) Splitwise; (3) in-memory relational datastore with keys, indexes and constraints, as reported at Razorpay; (4) thread-safe key-value store with TTL or a job scheduler, the concurrency rep; (5) reservation system, AI-assisted: architecture first, every generated line read, tests required, and a log of what AI proposed, what you accepted and rejected, and why; (6) cab or gym booking, as reported at Flipkart.

**Resources:** WAT, ALLD, RG, ARJAN.

**Not in Phase 1:** all 23 GoF patterns, UML beyond class and sequence diagrams, Java.

### 6.6 DSA (117.5 hrs, daily)

**Depth bar.** Clear the coding screen, not win contests. Every family touched before good referrals open at Gate B; Easy and Medium solid; unseen Mediums in 30-35 minutes with approach and complexity said aloud. Depth beyond this is Phase 2.

**Method, non-negotiable**

1. No problem before its NeetCode lesson or pattern explainer.
2. New technique: watch the worked example, reimplement it closed-book, explain the mechanism aloud. Cold-first applies only to re-solves.
3. Easy, then Medium, per family. Hards are optional and unscheduled, never required.
4. Tests come from the problem statement, never from your own code. Hand-trace every state when reading triggers recognition instead of construction.
5. Label every item: NEW counts toward the total; DRILL builds a structure and does not count; COLD is a spaced re-solve and counts toward the cold number.
6. Spaced re-solves on days 1, 3, 7, 14 and 28. No other intervals.
7. From W27, blind mixed sets with no pattern label run in the weeks marked in section 14.
8. DSA goes first in the daily block.
9. **Cold before new.** Due cold re-solves come before scheduled NEW problems. The 117.5 hours (110, plus 7.5 for the three weeks v3.3 adds) cover NEW problems at beginner pace (about 45 min Easy, 90 min Medium), a lesson per new family, about 200 colds at about 13 minutes each, and the blind sets. Time-box each cold (about 10 min Easy, 15 Medium). If cold debt still exceeds the week's DSA hours, NEW problems slip; reviews are never skipped.
10. **Tracker:** one row per problem: problem · first solved · D1 · D3 · D7 · D14 · D28 · result.

**Family order and totals (34 NEW, from 21 to 55)**

| # | Family | NEW | Lesson before it | When |
| --- | --- | --- | --- | --- |
| 1 | Stack, then monotonic stack | 3 | Stacks lesson, monotonic stack explainer | 1a |
| 2 | Binary search | 3 | Lessons 14 and 15 | 1a |
| 3 | Trees and BST | 4 | Recursion lessons 8 and 9, then 16 and 17 | 1a |
| 4 | Heap and priority queue | 3 | Lessons 23 to 25 | 1a |
| 5 | Intervals | 2 | Intervals explainer | 1a |
| 6 | Prefix sums | 2 | Advanced Algorithms: prefix sums | 1a |
| 7 | Backtracking | 2 | Lesson 22 | 1a |
| 8 | Graphs, BFS and DFS | 4 | Lessons 28 to 31 | 2 in 1b, 2 in 1c |
| 9 | Topological sort | 1 | Advanced Algorithms: topological sort | 1b |
| 10 | Union-find, built from scratch | 1 | Advanced Algorithms: union-find | 1b |
| 11 | Dijkstra and 0-1 BFS | 1 | Advanced Algorithms: Dijkstra | 1b |
| 12 | 1-D DP | 3 | Lesson 32 | 1 in 1b, 2 in 1c |
| 13 | 2-D DP | 2 | Lesson 33 | 1 in 1b, 1 in 1c |
| 14 | Greedy | 1 | Greedy explainer | 1b |
| 15 | Trie | 1 | Trie lesson | 1b |
| 16 | Bit manipulation | 1 | Bit manipulation explainer | 1b |

Sorting lessons 10 to 12 are DRILLs: implement merge sort and quicksort, not counted. Section 14 names a default problem for every NEW slot; swap any you have already solved.

**Targets:** Gate A 40 / 24 cold. Gate B 50 / 34. Gate C 55 / 40-45 plus the performance gate.

**Not in Phase 1:** segment and Fenwick trees, KMP, advanced DP, contest practice.

### 6.7 Supporting tracks (31.5 hrs)

**Depth bar.** Enough to debug Kubernetes and defend a design under follow-up questions.

| Unit | Hrs | Content | Proof |
| --- | --- | --- | --- |
| S1 Concurrency fundamentals | 5.5 | First a Checklist A baseline, cold and recorded (0.5h, before Gate A), so the rest of S1 is taught against measured gaps. Then race condition, critical section, mutex vs RW lock, atomics, semaphore, condition variable, the four deadlock conditions, livelock, starvation, lock granularity, optimistic vs pessimistic, producer-consumer, bounded queues and backpressure, mapped to Go and Python | Checklist A 7/10 cold (Gate B) |
| S2 Network path | 8 | DNS, TCP handshake, TLS cost, HTTP/1.1 keep-alive vs HTTP/2 multiplexing, pooling, timeouts vs deadlines. TCP retransmission, flow vs congestion control. L4 vs L7, reverse proxy, service discovery, retry amplification, pool exhaustion. Practised with `dig`, `curl -v`, `openssl s_client`, `ss` and one `tcpdump` capture | A planted timeout diagnosed with those tools, then explained end to end. 7/10 |
| S3 gRPC | 3 | Protobuf and schema evolution, unary vs streaming, deadlines, cancellation, status codes, retry implications, why service-to-service often picks gRPC | A breaking vs non-breaking proto change explained |
| S4 OS basics | 5 | Process vs thread, context switch, virtual memory, stack vs heap, syscalls, file descriptors, page cache, the OOM killer, signals. Practised on a misbehaving process with `ps`, `top`, `/proc`, `lsof`, `strace` and `ulimit` | The process diagnosed and explained from the tool output |
| S5 API and security | 6 | Resource modelling, verbs and idempotency, status codes, cursor vs offset pagination, versioning, error contract, idempotency keys. Authn vs authz, JWT validation, OAuth2 in concept, mTLS, secrets, RBAC, least privilege. One OWASP API Top 10 threat-model pass over PRCP | Findings file committed, BOLA covered |
| S6 Cloud vocabulary | 4 | IBM Cloud mapped to AWS and GCP: IAM, VPC, IKS to EKS or GKE, load balancing, object storage, managed Postgres, autoscaling, KMS. Terraform words only: resource, state, module | Mapping table from memory, 7/10. No certification, no console labs |

**Resources:** JVNS and MWDNS (DNS and networking you can break safely), OSTEP (targeted chapters only), HPBN (TCP, TLS and HTTP/2 chapters), HN, GRPC, OWASP ([plain-language review from ISACA](https://www.isaca.org/resources/news-and-trends/industry-news/2023/reviewing-the-2023-owasp-api-top-10)), official AWS and GCP product docs.

### 6.8 Stories, resume and narratives (24 hrs)

**Depth bar.** At 12 years the hiring-manager round sets your level. Every story shows a decision you owned, the option you rejected, a number that moved, and what you would change. No story from practice problems; no story inflated past its real scope.

| Unit | Hrs | Content | Proof |
| --- | --- | --- | --- |
| R1 Insurance pack | 5 | Resume v1 in combination format, headline built on the role identity. Naukri and LinkedIn complete. Keywords only for proven skills. Refresh after Gate A when Go becomes listable | Profiles live in October; every keyword traced to a closed unit |
| R2 Stories | 8 | The 2-3 honest stories now: registry cost reduction (reconcile the figures first), IKS upgrade programme, Circuit Breaker plus deployment gate. Context, decision, rejected option, outcome with a number, lesson | Each told aloud in 3 minutes; follow-ups answered |
| R3 Pitch and narratives | 8 | 60-second pitch and short recruiter answers. 5-minute PRCP narrative. Two 30-minute deep dives: PRCP (the problem, why existing tools do not fit, the design, determinism and `UNKNOWN`, the control-plane and data-plane split, what you would change), and one sanitized production system you owned (architecture, scale, failure modes, the decision you owned, the option you rejected, an operational consequence, the cross-team boundary, a measured result). Existing truthful work only | Timed, spoken, from memory |
| R4 Resume v2 | 3 | Rebuilt against the JD harvest frequency table | Every line traces to a proof or a story |

**Stories still to earn at work.** Seek tasks that produce these and log each the week it happens: (1) a Go production change, a feature, not a test; (2) a Kubernetes or platform debugging story; (3) an architecture decision you owned, with the option you rejected; (4) an incident: detection, mitigation, root cause, prevention; (5) cross-team ownership; (6) a measurable improvement with before and after numbers; (7) mentoring or code review.

**Counts:** Gate B checkpoint 4 stories; Gate C 5, at least 3 recent and 2 leadership. Fewer is PARTIAL and never blocks applications. Rehearse every story aloud once a month, 20 minutes, from the campaign reserve.

### 6.9 Paid resources, trigger-only

Nothing is bought without a proven gap. Already owned and used: NeetCode, Hello Interview, KodeKloud. Expected spend for all of Phase 1: two expert mocks and maybe one month of LeetCode Premium.

| Buy | Trigger | Note |
| --- | --- | --- |
| Expert mock interviews: [Hello Interview](https://www.hellointerview.com/) or Prepfully | No peer interviewers for mocks 2 and 4 by Feb 1 2027 | Book 1-4 weeks before a real high-value loop. Roughly $100-400 a session by one vendor's own figures, so treat that as the top of the range. At most two in Phase 1 |
| LeetCode Premium, one month | A real loop is booked at a company with tagged questions | Work that company's list, then cancel |
| *Fluent Python*, 2nd edition | The W0 Checklist D baseline shows 5 or more data-model items shaky or missing. **Met on Oct 5** | The one Python depth book worth buying. At the current level it is the second pass after Real Python, not the first read |
| [*Designing Data-Intensive Applications*, 2nd edition](https://martin.kleppmann.com/2026/03/24/designing-data-intensive-applications-2e.html) (Kleppmann and Riccomini, March 2026) | Phase 2 starts, about June 2027 | The one book worth owning. Buying it now means reading it now, which is scope creep |

**Do not buy:** more DSA courses (you own NeetCode), other Kubernetes or CKA courses (you own KodeKloud; if IBM wants the exam, IBM pays), Alex Xu's books or Grokking (overlap with Hello Interview), paid Go courses (Learn Go with Tests and the free course cover Phase 1), AWS or other certifications, GenAI courses, paid resume writers (the resume needs real numbers, not phrasing).

---
## 7. Verification protocol

Proof has two levels. Every unit gets light proof; milestones and gates get heavy proof. Running code is not proof of understanding.

**Mandatory learning loop: orient -> guided example -> independent practice -> prove -> repair -> retry -> retain.**

1. **Orient.** Confirm the prerequisite was studied. Make the core mental model explicit in plain language: what it is, why it exists, the mechanism or invariant, and the main failure mode or trade-off.
2. **Guided example.** When the concept is new or shaky, walk through one concrete case, trace, diagram or visual. Do not use the later cold-proof question as the guided example.
3. **Independent practice.** Om solves, implements, explains or debugs under the unit's AI rules. This is where authorship is established.
4. **Prove.** Check runtime evidence first, then the no-AI paragraph and three cold questions. Questions must test understanding, not file paths or trivia.
5. **Repair immediately.** After a wrong or partial answer is scored, explain the exact misconception with the smallest clear counterexample, trace, diagram or worked example.
6. **Retry fresh.** Ask one new question that tests the same mechanism without repeating the original wording. A correct retry shows the repair landed; an incorrect retry keeps only that local item open.
7. **Retain.** Re-test only at the unit's scheduled retention points. Use a changed example or scenario so the check measures transfer, not recall of the previous answer. DSA cold re-solves keep the same problem by design (section 6.6); the changed example applies to the questions asked about it.

Teacher and proctor are both mandatory. Teaching must not leak answers into a cold check, and proctoring must not replace teaching when a misconception is found.

**Prerequisites first.** Before any question, quiz or proof check, the assistant confirms the concept has been studied (plan progress, past submissions) or asks. A failed answer on something never taught is a teaching gap, not a FAIL: teach it on the spot, then ask.

**Authorship evidence.** Commit raw notes and self-reviews before any cleanup with a tool such as Cursor; the cleaned version is a second commit.

**Test records.** Every baseline, unit interview, audit, gate check and mock is recorded in `omieee/docs` by the coach who ran it, in its own `tests/<track>/` folder (section 0). A record holds the questions as asked, Om's answers verbatim, every prompt given, the marks and the correct answers, so the other coach can review the marks. A baseline only records where Om stands: no teaching right after it, and each gap is taught when the work that needs it comes up. Unit interviews are different: a miss is taught on the spot (section 0).

**Unit proof (every unit, about 15 minutes)**

1. A meaningful artifact in git: code, tests, a SQL file, lab output, a design scorecard or mock notes.
2. Tests or lab evidence, checked in the evidence order from section 0.
3. One paragraph from memory, no AI: what it does, why this way, what you rejected.
4. Three cold questions from the ladder below, scored, with on-the-spot teaching on any miss (section 0). NEW DSA problems get this too: the mechanism, a trace, and one transfer question.

**Milestone and gate proof (the five checks)**

| Check | How | Pass bar |
| --- | --- | --- |
| 1. Runs | A fresh CI run, else the assistant's own run, else pasted terminal output | All green. Any red is FAIL |
| 2. Honest tests | The assistant plants 1-2 bugs on a scratch branch; the tests must catch them. Tests must come from the spec, not the code | Every planted bug caught |
| 3. Cold explanation | Five questions, one per rung. No notes, no AI | 7/10 and zero correctness errors |
| 4. Change under pressure | One new requirement or one hidden bug, 20-30 minutes | A working change with a test |
| 5. Retention | Two questions again at day 7 and day 28 | 7/10 again; a miss reopens the item |

**Question ladder:** (1) Recall: define it in two sentences. (2) Mechanism: what happens, step by step, when X. (3) Failure: what breaks if Y, and how you would notice. (4) Trade-off: why A and not B, and what you gave up. (5) Transfer: a new scenario the unit never covered.

**Scoring.** Each answer earns 0 (wrong or missing), 1 (partly right, or needed a prompt) or 2 (right, specific, unprompted). During the cold answer, allow at most one neutral prompt per gap; do not teach until the answer has been scored. A wrong conclusion or an inverted invariant is FAIL whatever the score. After teaching, ask one fresh retry question on the same mechanism: a correct retry scores 1 for that item and clears the local FAIL; the original miss stays recorded as prompted. A wrong retry keeps the item open for the next session. Exact identifiers and file paths are trivia and never graded, except in the code-reading drills, where locating the code path is the skill.

**Failure stays local.** A failed unit blocks only the units that depend on it. A failed gate blocks the next phase. A failed item is repeated, never skipped.

**Track-specific checks**

- **DSA:** cold re-solves must pass asserts derived from the problem; the recall bar does not apply to them. Approach and complexity stated before coding.
- **Go:** `go vet` and `go test -race ./...` clean. For every goroutine: who starts it, who cancels it, who closes its channel.
- **Kubernetes:** the assistant describes a symptom or hands over a broken manifest. You reproduce it on kind and paste `kubectl` output before and after. Memory alone does not count.
- **Postgres:** two-session `psql` demonstrations pasted, real `EXPLAIN` plans, timed SQL on a schema you have not seen.
- **Machine coding:** six criteria, 0-2 each: runs end to end, domain model, extensibility after the mid-session change at minute 60, readability, tests, concurrency when asked. Pass: it runs, and 8/12 or better.
- **Design mocks:** eight criteria, 0-2 each: requirements, estimates, API and data model, high-level design, deep dive, failure modes, trade-offs stated, time and communication. Gate B: 11/16 with no zero. Gate C: the last two at 12/16 or better. Human mocks: bring their notes; the assistant scores against the same rubric.
- **Stories:** told aloud, then two hiring-manager follow-ups: what would you do differently, and who disagreed with you.

**Office proof path.** Office work counts only with: a ticket or PR id where safe to share, a sanitized description of the change, the CI or test outcome, a failure case, the decision and the rejected option, and a cold explanation. Never paste proprietary IBM code.

**Spoken proof.** A text chat cannot hear you. Spoken checks run in voice mode or with a live human. A timed written answer is the fallback, labelled as written.

**AI use.** No AI for first attempts, drills, DSA, machine coding reps 1-4 and 6, or any cold check. When a unit exists to teach a skill (Go syntax and concurrency in the G and A units, SQL in P1 and P2, manifests in the K units), you write that part yourself; AI may review it, explain an error or draft tests. Elsewhere in PRCP and agent work, AI is allowed once the design is decided, and generated code counts only after you verify the API, run the tests, inspect a failure case and can explain every line. Rep 5 tests AI-assisted work on purpose. The unit paragraph and cold answers are never AI-written; if one reads borrowed, the assistant asks a follow-up only your own context can answer.

**Cadence.** Per unit: unit proof. Every Sunday, 20 minutes: the weekly close below. Each skill is tested at four points only: baseline, milestone, gate, and the day 7 and day 28 retention checks after a gate. DSA alone keeps continuous spaced review. There are no extra monthly re-tests.

**Weekly close template**

```
WEEK N: PASS / PARTIAL / FAIL
Focused hours, planned / actual (bedside required items included):
Actual vs planned hours, each unit closed:
Largest overrun or underrun, and why:
Contingency used this week / total used / remaining (of about 50):
Planned:
Completed (with commit hashes):
Not completed:
DSA total / cold:
Machine coding reps:
Design mocks:
Git and production evidence:
Execution gaps (days with no artifact):
Carry-forward:
Next week's scope:
Change-control trigger: YES / NO
```

### Interview checklists

Gap-detection tools, not curricula. Run cold and aloud; mark each item solid, shaky or missing; study only shaky and missing; re-run a month later.

- **A. Concurrency (Gate B):** race condition, critical section, mutex vs RW lock, atomic operations, semaphore, condition variable, the four deadlock conditions, livelock, starvation, thread safety, lock granularity, optimistic vs pessimistic locking, producer-consumer, bounded queue and backpressure. Then in Go: when a mutex beats a channel, `WaitGroup`, `select`, context cancellation.
- **B. Go language.** Fundamentals half (Gate A): slice length vs capacity, `append` behaviour, array vs slice, map semantics and why concurrent map writes crash, struct embedding, implicit interfaces, the nil-interface trap, pointer vs value receivers, `defer` evaluation order, `%w` with `errors.Is` and `errors.As`, panic and recover and when not to, generics basics. Concurrency half (Gate B): buffered vs unbuffered channels, `select`, reading from a closed channel, `Mutex` vs `RWMutex`, `WaitGroup`, context, the race detector, goroutine leaks, the scheduler model, GC at a high level.
- **C. Kubernetes (Gate B):** start with what happens after `kubectl apply`. Then API server, etcd, scheduler, controller manager, kubelet, desired state and reconciliation, Pod lifecycle, Deployment to ReplicaSet to Pod, Service and endpoints, the Service dataplane, ClusterIP, DNS and service discovery, Ingress, CNI and CSI basics, requests vs limits, QoS classes, OOMKill vs CPU throttling, taints and tolerations, affinity, ConfigMap and Secret, ServiceAccount and RBAC, NetworkPolicy, the three probe types, rolling update and rollback, Deployment vs StatefulSet vs DaemonSet vs Job, HPA vs VPA vs cluster autoscaler.
- **D. Python (baseline in W0, pass at Gate B):** mutable vs immutable, hashability with `__eq__` and `__hash__`, shallow vs deep copy, list, dict and set complexity, iterator vs iterable, generators, decorators, context managers, the exception model, dataclass vs class, typing, the GIL and why it does not make compound operations atomic, thread vs process vs asyncio, async cancellation and timeouts, pytest fixtures, property-based testing, reference counting and cyclic GC, MRO and `super()`, ABC vs Protocol.

---

## 8. Positioning and conversion

Target Senior, list only what you can prove, and price against the role's market band, never against current CTC. Every keyword that gets you past the filter becomes an interview question.

**Profile and resume**

- **Headline formula:** role, years, 3-5 proven skills, one differentiator. After Gate A: "Senior Backend Infrastructure Engineer · 12 yrs · Python, Go, Kubernetes, PostgreSQL · distributed control planes".
- **Keyword rule:** a skill appears on the resume, Naukri or LinkedIn only with a closed unit or real production evidence. Kubernetes can be listed now as production IBM Cloud work; Go waits for Gate A.
- **Fill every Naukri filter field:** experience, location, current and expected CTC, notice period.
- **Combination format:** skills summary first, then chronological. Lead with platform engineering on IBM Cloud CDP, not just "IBM". Problem, then outcome, with numbers.
- **Career-speed questions:** never volunteer an explanation. If asked why 12 years and Band 7B, answer in two sentences and pivot to current scope and evidence.
- **Bullet formula:** action verb, the system you owned, the tech, a measured outcome. Name the product and its business result (GA shipped, cost cut by a stated percent). No "significantly", and no "targeting" in an achievement line: only results that happened.
- **Recognition section:** IBM awards and client-facing wins, each with its date. Third-party validation beats self-description.
- **Match the signal to the level.** DSA contest ratings and an entry-level cloud cert in a headline help a junior and read junior at 12 years. Your headline proof is scale, ownership and a shipped system.

**Search in three lanes** (Naukri, LinkedIn, Instahyre, Cutshort, Hirist, company career pages):

1. Go and control plane: `("control plane" OR "backend infrastructure" OR "distributed systems" OR "platform engineering") AND ("Go" OR "Golang") AND ("Senior" OR "Staff" OR "MTS") AND ("Bangalore" OR "Bengaluru" OR "Hyderabad" OR "Pune")`
2. Python and backend infrastructure: `("backend infrastructure" OR "platform backend" OR "distributed systems") AND "Python" AND ("Senior" OR "MTS") AND ("Bangalore" OR "Bengaluru" OR "Hyderabad" OR "Pune")`
3. Language-flexible systems: `("distributed systems" OR "control plane" OR "systems software") AND "Kubernetes" AND ("Go" OR "Python") AND ("Senior" OR "Staff" OR "MTS")`

SRE roles stay excluded unless the JD is development-heavy and matches the role identity.

**Channels:** referrals first when available (ex-IBM and CDP alumni), recruiter platforms, LinkedIn, direct applications. Never sit waiting for a referral while a strong role is live.

**Referral map (October, campaign reserve):** list ex-IBM and CDP colleagues now at target companies, with company, date moved and last contact. Warm each one with a no-ask message now. Ask for calibration referrals after Gate A and for good referrals after Gate B. People who left IBM recently, like the junior teammate who joined Amazon as L5 in Sept 2026, go on the list first; Amazon itself is a Phase 2 target.

**JD harvest in November (W6):** 20 or more live postings you would accept. Tabulate every named technology by frequency. This triggers or kills the conditional queue. Refresh it in W26 for resume v2.

**Lane-size check in the same harvest:** if fewer than 20 live roles both fit the role identity and can meet the ₹42L fixed gate, that is a change-control trigger. The response is to widen locations, add GCCs, or re-examine the cost of skipping Java, with the harvest as the evidence.

**During loops**

- Confirm each loop's shape with the recruiter before preparing.
- Ask at the start of any coding round whether AI is allowed.
- Feedback tracker after every round: round type, questions, where you struggled, and whether the failure was technical, communication, missing knowledge or timing. Three failures in one category trigger a targeted fix, not a new plan.

**Money and notice**

- Gate: at least ₹42-45L fixed cash. Not CTC, not RSUs.
- Never inflate current CTC; payslips get checked. Anchor expected pay on the role's band.
- Decompose every offer: fixed, variable, RSUs, joining bonus, notice buyout, and the level itself.
- Early-offer rule, decided now: an offer below the gate, or one that fails due diligence, gets a no, with the process kept warm.
- Notice period: 3 months at IBM India. Put 90 days in every notice field and state it up front. Ask early whether the team can wait. Find out whether IBM allows early release or buyout, and ask formally only after a signed offer. Never resign early to look immediate.

**Offer due diligence:** percentage of time coding, on-call load, tickets vs ownership, design responsibility, roadmap, team seniority, stack, manager, promotion path, and whether "Platform Engineer" really means cloud operations. A good title on an operations role damages the 2027 bridge.

---

## 9. Execution rules and safeguards

The failure mode is not the syllabus; it is going quiet. PRCP went 43 days without a commit and DSA went 23.

**Daily**

1. **The cue, written and fixed:** "If it is [TIME] and I am at my desk, I open the repo and start a 25-minute timer." The time is filled in on Oct 1.
2. **Floor: 25 minutes every day,** including travel, headaches, CDP crunch and no-nanny days. Pressure drops study to the floor, never to zero.
3. **Never two zero days in a row.** One miss is noise; two is a new habit.
4. **One meaningful artifact in git a day:** code, a test, a SQL file, lab output or a scorecard. Never a filler commit to keep a streak.
5. **DSA first** in the daily block.
6. **90-minute timed work** (machine coding reps, mocks) only on days with a clean block. Never in fragments.
7. **Calendar it.** The daily cue and the Sunday close go on the calendar as recurring events on Oct 1, so the safeguards do not depend on memory.

**Bedside time (phone only, dark room, while your son sleeps)**

This time is input only. It never counts as proof and never replaces the daily artifact; it takes the "watch" step off the desk so desk time goes to building. Required watch items done here count in their unit's hours and in the weekly actual hours.

1. **First: this week's watch items from section 14,** in order: the NeetCode lesson for the week's DSA family, the matching Go course chapter, the matching KodeKloud Kubernetes lesson.
2. **Then: Kleppmann's distributed systems lectures** (23 lectures of about 20 minutes). A first pass now is optional bonus time; the counted pass happens inside H3 and H4. After that, Hello Interview's full mock walkthroughs.
3. **Last 10 minutes, phone off:** recall in your head, eyes closed: today's DSA approach, what happens after `kubectl apply`, or one story start to finish.
4. **Setup:** each Sunday, build a Watch Later playlist from section 14 and play only from it. Autoplay off, dark mode, lowest brightness, one earbud. No earphones: read the week's Learn Go with Tests chapter or Kubernetes Concepts page instead. Falling asleep is allowed.

**Tripwires**

- **Every Sunday close checks the last 14 days.** Fewer than 10 days with an artifact, or any two-day gap, means stop forward work for one session and name the blocker: cue, time slot, work pressure, family load or avoidance. Fix that, then continue. No replanning.
- **Two-day gap found:** 25 minutes on the smallest open item, the same day. No catch-up sprint.
- **Rejection arrives:** log it in the tracker, then do that day's floor before anything else. One rejection triggers nothing more. Three in the same round type trigger a targeted correction.

**Branches**

- **CDP delivery pressure:** study drops to the floor. Keeping the job wins.
- **Layoff notice:** recalculate capacity from the actual situation, re-sequence the remaining units, and make applications the priority. The insurance pack is already live. Do not assume a fixed daily figure.
- **Early good offer:** take it seriously and bend the plan. Below the gate: section 8.

**Discipline**

- **Claim discipline:** beginner hours carry a beginner claim, said out loud. At 12 years a gap reads as focus; an overclaim caught in round three reads as dishonesty and burns the referral.
- **One-in, one-out:** any addition names what it removes. Everything else goes to the later-refactor log, logged once.
- **Ordering:** scope first, honest effort second, calendar last.
- **The urge to rewrite the plan is usually avoidance.** The plan was never the bottleneck.

**Change control**

- **Allowed triggers only:** a material execution failure, repeated interview failure, a major market shift, a newly found dependency defect, or a health or family constraint.
- **Every change states:** what changes, why, evidence, time cost, what is removed, and risk reduced.
- **Verification invariant, checked by script on every revision:** every week's item hours equal its label, the labels fit the weekly caps, and unit totals equal their track budgets.
- **Promise-execution invariant:** every unit in section 6 appears in a named week of section 14.
- **Review stop rule:** no adversarial re-review without new evidence. Every review finds something; that is a property of reviews, not of the plan.

---

## 10. Bridge week and the Oct 1 procedure

Nothing in the plan changes before Sept 30. The bridge week collects the evidence Oct 1 needs.

| Date | Task | Proof |
| --- | --- | --- |
| Sat Sep 26 | Floor: cold re-solves of 19 (day 3) and 206 (day 28) | Commit; asserts pass |
| Sun Sep 27 | Floor: pgexercises Simple SQL Queries | `.sql` file committed |
| Mon Sep 28 | Machine coding rep 1: parking lot, 90 min, no AI, no lookups, no preparation | Commit at minute 90, unedited |
| Tue Sep 29 | Rep 1 self-review, 60 min, into `lld-patterns`. Start the psycopg `Service` repository | Review notes committed |
| Wed Sep 30 | Finish the `Service` repository with one rollback integration test. Record the DSA count. Run the office-Go test | Commit, tests green, results written down |

**Office-Go test, for the record:** Go changes merged or in review at CDP; at least one test shipped; what you touched explained from memory; `go-notes.md` with 20 or more entries. Expected: FAIL. The Go track in section 6.2 is already scheduled.

**Oct 1 procedure (1 hour, with the assistant)**

1. **Record the evidence:** DSA total and cold, rep 1 rubric score, office-Go result, Postgres state, September artifact days.
2. **Write the gap diagnosis:** one paragraph on why Sep 1 to 21 had no commits (cue, slot, work pressure, family load or avoidance) and the one change that prevents a repeat.
3. **Fill in the cue time** in section 9, and put the daily cue and the Sunday close on the calendar as recurring events.
4. **Credit only what current evidence proves.** Any baseline-dependent change (unfinished bridge work, or a rep 1, Postgres or Go result that disproves an assumption) goes through change control now: amend, re-run the script.
5. **Upload this file** to the Claude project and to ChatGPT, and remove the old files per section 12.
6. **Freeze the file.** From here on, changes need a section 9 trigger.

**Oct 1 handoff, as recorded** (verified from the repos in a separate chat on Oct 1):

| # | Item | Status |
| --- | --- | --- |
| 1 | DSA | 21 total / 14 cold |
| 2 | Rep 1 | Not counted: the Sep 28 parking-lot attempt took 109 min with AI-written tests and one AI fix. A clean rep 1 (Snake and Ladder) is in W0 |
| 3 | Office-Go test | Om to run: 10 minutes, four criteria; an honest FAIL is fine |
| 4 | Postgres | Schema `68acbf6` merged to `main` via PR #8 (`7958798`); both databases match git on Postgres 18.6. Service repository not started, so P1 is October's first task |
| 5 | September artifact days | 10 of 30: Sep 12, Sep 14, Sep 22-29 |
| 6 | Gap diagnosis | Om to write. Sep 1-21 had 2 artifact days, not zero |
| 7 | Cue time | Om to set |
7. **Start W0.**

---

## 11. Phase 2: FAANG-equivalent and Staff

Phase 2 starts about early July 2027 and targets loops from November 2027 to February 2028. Most Phase 1 hours transfer: DSA, design, Python and Go depth, stories and the PRCP deep dive. Machine coding and Kubernetes drills do not appear in FAANG loops; they bought income safety.

**2a Convert and consolidate (about Jul to Aug 2027)**

- **Branch A, new job landed:** with a 3-month notice period, an offer around Gate B (late June) means joining around October. Keep the full plan running through the notice period. On joining, study drops to 1.5 hrs/day for 8-10 weeks of onboarding; that dip overlaps the start of 2b, and 2b's targets trail by the same weeks. Protect DSA cold re-solves, `go-notes.md`, and one spoken design rep every two weeks. Start a new story log on day one. DSA drifts to about 65 / 48, which is expected.
- **Branch B, no offer yet:** keep 2.5 hrs/day and keep interviewing. Diagnose which round fails using the tracker and fix that round. DSA to 90 / 60, design mocks to 8, machine coding reps to 10.
- **Both:** DDIA chapters 5-9, each producing a note tied to a PRCP decision. Answer any outside PRCP issue within a week.

**2b FAANG readiness (about Sep to Dec 2027)**

2b is shorter now. If its targets are not met by December, run the FAANG loops in January and February 2028, the back half of the window.

| Area | Target | Note |
| --- | --- | --- |
| DSA | About 150 total / 110 cold by Dec 31 | The real gate: an unseen Medium solved, spoken, in 25-40 min |
| Design | 16 mocks, at least 8 with humans | Staff-level framing and trade-offs |
| AI-era rounds | Re-research current formats when Phase 2 starts | Do not freeze today's formats |
| Stories | 8 at larger scope | Graded on what you owned, decided and influenced |
| Depth | DDIA chapters 1-12 | Project-linked notes |
| Optional, cut first | A controller-runtime `GateDecision` CRD whose reconciler calls PRCP; one merged Go OSS PR | Never a gate |

**Critical paths.** DSA is the longest chain: it compounds through spaced repetition and cannot be sprinted at the end. Spoken design reps are second: they need calendar time and other people.

**Failure branches**

- **No India offer by May 2027:** do not extend blindly. Diagnose the failing round from the tracker and fix it.
- **The new role is mis-sold support work:** leave. A bad role does not improve by enduring it.
- **FAANG matters more than the India job:** say so, and the plan is rebuilt: stay at IBM, DSA-dominant, weekly design, no machine coding, accept the layoff exposure.

**Out of scope here:** relocation and visas. If the March 2028 goal still means abroad, that track starts in parallel during 2027; raise it at the 2a review.

---

## 12. File hygiene

Keep one file. Conflicting numbers across files caused past confusion.

| File | Action | Why |
| --- | --- | --- |
| `Phase_1_Source_of_Truth (1).md` | Remove from the project on Oct 1; archive a copy outside it | Governance now lives in sections 0, 1 and 9 |
| `1_india_plan_sept_to_jan (1).md` | Remove and archive | Scope, capacity, checklists and conversion rules are carried into sections 5-9 with corrected numbers |
| `2_week_by_week (1).md` | Remove and archive | Replaced by section 14 |
| `3_bridge_to_m3_m4 (1).md` | Remove and archive | Carried into section 11 with corrected dates |
| `phase1_final_prcp_execution_plan.md`, `phase1_revised_6_month_senior_platform_plan.md` | Remove anywhere they still exist, including ChatGPT | Withdrawn on Aug 31 |
| The v3 Claude Doc draft | Keep as history only | Superseded by this file |
| `Phase1_Master_Plan_v3.1.md` | Remove from both projects once v3.2 is uploaded; archive a copy | Superseded by v3.2 |
| `Phase1_Master_Plan_v3.2.md` | Remove from both projects once v3.3 is uploaded; archive a copy | Superseded by v3.3 |
| Project instructions (Claude project settings) | Replace the line "Baseline plan: Phase 1 runs May 21 2026 to Nov 20 2026" with "Governing plan: Phase1_Master_Plan_v3.3.md" | The old baseline contradicts this file |
| This file | The only plan file in the Claude project and in ChatGPT | Single source of truth |

**After any approved change,** edit this file, re-run the script, and re-upload to both assistants the same day.

**Assistant memory.** Saved notes that still name the old files, the May 21 to Nov 20 plan, or the Jan 31 end date are stale; point them here. Current state (DSA count, audit scores, decisions) lives in the weekly close and the repos, never in memory alone.

---
## 13. Change log: v3 to v3.3

v3.1 folds in 70 corrections: 23 agreed after an outside review, 2 found by the week-map script, 16 more from the same review after cross-checking, the bedside rule, 2 positioning points from a former teammate's resume, 6 from the final pass, 13 from a second outside review, checked point by point, 1 for an owned KodeKloud subscription, 1 delta fix, 1 set of zero-hour substitutions from a third review, 1 overrun rule, the 420-hour authorization, a bottom-up re-estimate, and the Oct 1 handoff. All are already written into the sections above.

**Agreed after review (1-23):** draft status until Oct 1 · arithmetic rebuilt by script · two proof levels with verification hours budgeted · office proof path without proprietary code · agent ServiceAccount without token and without a Role · Service dataplane taught as replaceable · `errgroup` as the agent's only concurrency model · Hards optional · November calibration lane · three search lanes · story counts that never block applications · layoff capacity recalculated when it happens · Phase 2 formats re-researched later · one-page design skeletons · Go practical at Gate A · old files archived, not destroyed · Staff as opportunistic stretch only · direct Go and Kubernetes questions acknowledged · salary range not called a floor, band line softened · Kubernetes Gate A at 10/15, Gate B 10/15 plus a live challenge · mock bars rising to 12/16 by Gate C · monthly re-forecast from actual hours · all 16 DSA families by Gate B.

**Found by the script (24-25):** Docker, CI and concurrency fundamentals moved from 1a to 1b, giving Gate A Dec 13, Gate B Mar 28, Gate C Apr 11 · verification and governance budgeted at 29 hours, total 382.5 from Oct 1.

**Cross-checked additions (26-41):** Levels.fyi percentiles for the salary line · Nutanix Jul 2026 loop with three design rounds · Intuit's Kubernetes debugging question and 31% pass rate · three code-reading drills (W8, W11, W16) after a Nutanix code-navigation round · agent non-goals backed by Kubernetes RBAC good practices · IPVS internals skipped per the Kubernetes docs · Gate A no-zero rule on core Kubernetes components · Go practical with no AI and docs only after a first attempt · Gate B story checkpoint of 4 · weekly close template · meaningful artifacts, never filler commits · Oct 1 credit only on current evidence · failure blocks only dependent work · Phase 1 capability defined in one line · SRE excluded unless development-heavy · only blocking Python gaps pulled into 1a.

**Added on request (42):** the bedside-time rule in section 9.

**Added from a former teammate's resume and profile (43-44), Sept 25:** resume bullet formula, recognition section and a level-matched headline · a referral map of ex-IBM contacts, warmed with no ask, with asks timed to Gates A and B. Zero study hours; campaign reserve only. Not copied: his Java and Spring stack (Java stays out), his GenAI feature work (no AI features in PRCP), and a DSA-rating headline (junior signal).

**Final pass (45-50), Sept 25:** capacity check at W2 · lane-size check in the JD harvest · notice period recorded as 3 months, with joining-date and Branch A effects · daily cue and Sunday close on the calendar · docs demoted to lookup, with free non-doc resources added (INTERDB, GOBYEX, GO100, RP-ASYNC, IXIMIUZ, K8SAF, JVNS, MWDNS, BBG) · paid purchases listed with triggers in section 6.9. No hours added.

**Second review, checked independently (51-63):** Oct 1 evidence may change any baseline-dependent scope through change control, then the file freezes · required bedside watching counts in unit hours; the first Kleppmann pass is optional bonus · testing at baseline, milestone, gate and retention only, since monthly re-tests contradicted the W19 start of blind DSA sets and hid hours · weekly close records planned and actual focused hours · evidence order CI, then assistant run, then pasted output · rep 6 moved from W25 to W26, so Gate B needs reps 1-5 only · Python async runner frozen as the local reference, Go agent the only deployable execution path · AI rule widened for engineering work, with one counter: code that a unit exists to teach is still written by you · career-speed questions answered only when asked · no FAANG calibration in Phase 1 · cold-before-new rule and tracker, because about 200 cold reviews fit the DSA budget only at about 10 minutes each · stale "weekly file" text removed, salary data flagged for refresh · the week row picks the resource; no browsing, nothing to finish. Countered: the salary figure was already timestamped; the AI rule was kept narrower than proposed for learning-target code.

**Owned resource (64):** KodeKloud's CKA course becomes the Kubernetes track's main video and lab source (K1-K5, K7), replacing iximiuz Labs and its paid trigger; Nana drops to fallback. Its control-plane and worker-node failure labs cover scenarios kind cannot easily simulate. Use only the lessons each week names. No hours added.

**Delta fix (65):** exact KodeKloud mapping for W3 (Rolling Updates and Rollbacks), W4 (Scheduling covers only Resource Requirements and DaemonSets; StatefulSet, Job and CronJob, probes and QoS come from the Kubernetes docs) and W7 (Application Lifecycle: ConfigMaps, Secrets; Security: RBAC, ServiceAccounts) · control-plane and worker-node labs made optional bonus, since they had been added to W20 without hours · CKA wording clarified as study scope, not money · the child's name removed from section 9, since it could not be confirmed. Kubernetes stays at 25 hours.

**Third review, zero-hour substitutions (66):** O1 adds a controlled load experiment and tracing concepts · F1 shortens the Keptn/Argo/Flagger ADR and adds a game day with postmortem and runbook · S2 and S4 proofs become tool-based (`dig`, `curl -v`, `openssl s_client`, `ss`, `tcpdump`, `ps`, `/proc`, `lsof`, `strace`, `ulimit`) · K2 adds controller anatomy; K7 scenario 5 becomes a stuck finalizer, since events-by-time was already K1 · R3 adds a sanitized production deep dive, and top referrals need 3 strong production stories · Gate B checks quality, not counts: the latest two reps pass and the W24 blind set reaches 80% · H5 makes PRCP multi-tenant · P4's main proof becomes an expand, backfill, contract migration · items the checklists test but no unit taught (Go scheduler and GC, HPA/VPA/cluster autoscaler, CNI vs CSI) now sit in G7, K3 and K4 · the conditional queue becomes an extras queue with pull rules, cloud and Terraform split, and Redis and a controller mechanics lab added as trigger-only extras. Countered: the competitor ADR is shortened, not deleted, because the deep dive's 'why existing tools don't fit' depends on it; the hours for the production deep dive come from re-splitting R3, not from cutting a five-minute 'why no Java' answer. No hours added: the total stays 382.5.

**Overrun rule (67):** units overrun into contingency before any proof is cut, capped per unit at the smaller of 2 hours or 30%; campaign reserve is never used for study; contingency use is recorded weekly; two overruns in a month or more than 10 hours in total triggers a re-forecast; the weekly target stays at 15 until four straight weeks at or above plan.

**420 hours authorized by Om (68), Sept 25:** scheduled scope rises from 382.5 to 420 hours so every relevant topic has adequate time: Go fundamentals +4 and agent +2, DSA +10 (cold reviews at a realistic 15 minutes), HLD +5, PRCP +8 (Postgres internals, migration, asyncio, load and SLO, game day), Kubernetes +3, machine coding reviews +2.5, networking and OS +2, deep dives +1. Contingency (about 45 hours) stays separate. The per-unit overrun caps are replaced by one simple rule. Gates move to Dec 20, Apr 18 and May 2. Nothing was cut.

**Bottom-up estimate (69), Sept 26:** every unit re-estimated from explicit beginner rates (section 5) instead of adjusted from the old total: 490 hours, inside Om's 575 authorization. Biggest changes: DSA 110, Go 65, HLD 63.5, PRCP 99, Kubernetes 36. The 575 ceiling is released per track only by measured actuals. Gates: Jan 10, May 23, Jun 6 2027. Nothing cut, nothing padded.

**Oct 1 handoff and other project chats (70):** SQL correction track from the measured Sep 27 level (P2 7.5 to 14.5, SQLBolt and a window-functions lesson before each pgexercises section, skip Recursive and String) · P1 restarts from zero with the psycopg 3 prerequisite path (5 to 8) · the parking-lot attempt logged as AI-assisted practice, clean rep 1 (Snake and Ladder) added in W0 · prerequisite check before any question, from Om's standing rule · raw notes committed before any cleanup · baseline corrected: 21/14 DSA, 10 of 30 September artifact days, schema merged · project instructions' old baseline to be replaced. Total 503 hours; gates Jan 24, May 30, Jun 13 2027.

**Teach-first coaching (71), Oct 4, v3.2. GAP, approved by Om; wording consolidated Oct 5 across Claude and ChatGPT.** What: section 0 makes the assistant both teacher and proctor, with teaching before proof for new or shaky concepts, independent practice, scored cold checks, immediate misconception repair, a fresh retry and scheduled retention; it also requires the teaching format to fit the topic: plain words, flow diagram, image, video or worked example, with counterexamples preferred when they expose a wrong mental model. Section 7 makes that lifecycle operational and adds the unit interview for NEW DSA problems. Why: the protocol could verify artifacts without guaranteeing transferable understanding. Evidence: on Oct 4 Claude passed LC20 on 64/64 green tests and planted bugs, closing it on code alone; ChatGPT's transfer question then exposed a wrong two-pointer model that `"()[]{}"` breaks, and Om reported the counterexample explanation is what made it click. Trigger: a newly found defect in the verification protocol that every unit close depends on. Time cost: 0 scheduled hours; teaching on a miss uses the unit's own hours and replaces a blind re-study loop, and any overrun goes to contingency under the existing rule. Removed: nothing. Risk reduced: shallow completion, cargo-cult implementation and interview failure on why, changed examples, invariants and transfer questions.

**Realistic Python sizing, coach channel and test records (72), Oct 5, v3.3. BUG and GAP, drafted by Claude; approved by Om by uploading this file.** What: section 2's Python row corrected. Python depth re-estimated from the measured level at a realistic rate (section 5): 27.5 to 71.5 hours. Y3 becomes Python core, 22.5 hours by Gate A; new Y8 classes and data model, 13.5 hours; new Y7 PRCP code walk, 5 hours; Y1 2 to 4 (PRCP has no mypy config), Y4 10 to 14, Y5 5 to 7, Y6 2.5 to 4.5. P1 gains 1.5 hours of Python prerequisites. S1 starts with a Checklist A baseline. Resources: Real Python's free written tutorials as the first read, *Fluent Python* as the second pass, MYPY added; titles verified Oct 5. Section 0 gains the two-coach channel through `omieee/docs`; section 7 gains test records and a per-unit actual-hours line in the weekly close; section 5 gains the pace check. The week map was rebuilt from where Om actually is: W0's unfinished MC1, Y2, G1 and R1 moved into W1, and everything after slips forward in order, with reps and mocks kept whole. Why: Y3 was sized for "solid app level", and the P1 to P4 unit proofs and Gate B's craft demo depend on Python Om can explain. Om rejected a 10.5-hour version as too optimistic for his level. Evidence: Y2 baseline Oct 5 (`claude/tests/python/2026-10-05-Y2-checklist-D-baseline.md`, `0ddf130`): 0 solid, 6 shaky, 13 missing; PRCP's pre-plan code has 5 pytest fixtures, 16 `with` blocks, 11 route decorators, Protocols and frozen dataclasses, and each of those items came back missing or shaky; Q12 and Q13 showed the GIL and thread vs process missing, while Checklist A had no baseline. Trigger: a newly found dependency defect (a section 2 baseline that units depend on was wrong). Time cost: +55 hours, total 558, 17 under the 575 ceiling; three weeks added, gates Feb 7, Jun 20 and Jul 4 2027. Removed: nothing; the dates move instead. Risk reduced: P1 to P4 proofs and the craft demo failing on Python basics, a calibration loop after Gate A exposing them, S1 sized blind, and an estimate that forces another change later. Not changed: Go (already budgeted from zero), Kubernetes (raised after its audit), the Phase 1 Senior target.

**Checked and not added:** backend JDs asking to spot subtly wrong AI-generated Go (only AI-trainer gigs found; rep 5 already trains this) · a live Senior median of ₹56.8L (page would not load; the Dec 2025 snapshot is used) · Intuit Staff roles at 8+ years (not needed for a Senior target) · specific Nutanix Go, Kubernetes-deployment and query-planner questions (reports found show design and code-reading rounds instead).

**Rejected:** 8/10 pass bars on every checklist; Kubernetes 12/15 at Gate B; setting the date from September's demonstrated capacity of 3-4 hrs/week.

---

## 14. Week map from Oct 1

Forty weeks, Oct 1 2026 to Jul 4 2027, 558 scheduled hours. A script built and checked this map: every week fits its cap (15, or 8 in light weeks), every unit's hours match section 6, every sub-task is visible, DSA totals 117.5, verification plus gates total 33, and no unit starts before the units it depends on. The proof column names the units that close that week; each unit's proof is in section 6.

**How to use a row.** Work runs left to right within a week, DSA first each day. Watch the bracketed video first (bedside time is ideal), then read the docs as the authority, then build at the desk. A unit's proof is due in the week it ends. DSA problems are default picks from the NeetCode roadmap; swap any you have already solved. Campaign work comes from the reserve, never from these hours.

**Resource key (all checked 2026-09-25). Docs are lookup only; see section 6.**

| Key | Resource | Use |
| --- | --- | --- |
| NC | [NeetCode course and roadmap](https://neetcode.io/roadmap) | Lesson before every DSA family |
| FCC-Go | [freeCodeCamp and Boot.dev Go course](https://www.freecodecamp.org/news/go-programming-video-course/) (Lane Wagner, 2023; chapters with timestamps) | Go video, by chapter |
| LGWT | [Learn Go with Tests](https://quii.gitbook.io/learn-go-with-tests) | Primary Go text, chapters as named |
| PIKE | [Rob Pike, Go Concurrency Patterns](https://www.youtube.com/watch?v=f6kdp27TYZs) ([slides](https://go.dev/talks/2012/concurrency.slide)) | Concurrency video |
| GO-SLICES, GO-ERRORS | [Go Slices: usage and internals](https://go.dev/blog/slices-intro), [Working with Errors in Go 1.13](https://go.dev/blog/go1.13-errors) | Official deep reads |
| GO-CONTEXT, GO-PIPELINES | [Go blog: context](https://go.dev/blog/context), [pipelines](https://go.dev/blog/pipelines) | Cancellation and fan-out |
| GO-PPROF, GO-SLOG | [Profiling Go programs](https://go.dev/blog/pprof), [Structured logging with slog](https://go.dev/blog/slog) | Leak lab, logging |
| EFFGO, ERRGROUP, CLIENTGO | [Effective Go](https://go.dev/doc/effective_go), [errgroup](https://pkg.go.dev/golang.org/x/sync/errgroup), [client_golang](https://pkg.go.dev/github.com/prometheus/client_golang/prometheus) | Idiom and packages |
| KK | [KodeKloud](https://kodekloud.com/) (owned): CKA course by Mumshad Mannambeth, lectures plus in-browser lab clusters with auto-checked practice tests | Main Kubernetes video and labs; only the lessons each week names |
| NANA-K8S | [TechWorld with Nana, Kubernetes full course](https://www.youtube.com/watch?v=X48VuDVv0do) | Fallback if a KodeKloud lesson does not click |
| NANA-DOCKER | Docker Crash Course for Absolute Beginners and Docker Compose in 1h, on [TechWorld with Nana](https://www.youtube.com/c/techworldwithnana) | Docker video |
| KIND | [kind quick start](https://kind.sigs.k8s.io/docs/user/quick-start/) | Local cluster |
| K8S | [Kubernetes Concepts](https://kubernetes.io/docs/concepts/), [Debug tasks](https://kubernetes.io/docs/tasks/debug/) | Authority, pages as named |
| LEARNK8S | [Visual guide to troubleshooting Kubernetes deployments](https://learnk8s.io/troubleshooting-deployments) | Debugging map |
| PG | [PostgreSQL docs](https://www.postgresql.org/docs/current/) | Authority, chapters as named |
| CMU | CMU Database Group YouTube channel, 15-445 Fall 2024 lectures, by title | Database internals video |
| TS-ISO | [Tech School: isolation levels in Postgres](https://dev.to/techschoolguru/understand-isolation-levels-read-phenomena-in-mysql-postgres-c2e) | Hands-on isolation demo |
| SQLBOLT | [SQLBolt](https://sqlbolt.com/) lessons, plus its [subqueries and set-operations topics](https://sqlbolt.com/topics) | SQL concepts before each pgexercises section |
| PG-TUT | PostgreSQL tutorial, [Window Functions](https://www.postgresql.org/docs/current/tutorial-window.html) | Window-functions lesson |
| UTIL | [Use The Index, Luke](https://use-the-index-luke.com/sql) | Indexing |
| PGEX | [pgexercises](https://pgexercises.com/) | SQL practice, 81 exercises |
| PSY, SQLA, ALEMBIC | [psycopg 3](https://www.psycopg.org/psycopg3/docs/), [SQLAlchemy 2.0 tutorial](https://docs.sqlalchemy.org/en/20/tutorial/), [Alembic tutorial](https://alembic.sqlalchemy.org/en/latest/tutorial.html) | Driver, ORM, migrations |
| HN | Hussein Nasser's YouTube channel, searched by topic | Database and network intuition |
| BEAZ | [David Beazley, Python Concurrency From the Ground Up](https://pyvideo.org/pycon-us-2015/python-concurrency-from-the-ground-up-live.html) | Python concurrency video |
| PYDOCS | [Python docs](https://docs.python.org/3/): asyncio, data model, threading, queue, profile | Authority |
| MCODING, ARJAN | mCoding and ArjanCodes YouTube channels | Python internals, design |
| RP | [Real Python](https://realpython.com/) free written tutorials, by the title each week row names (titles checked 2026-10-05; skip the paid video courses) | First read for Y3 and Y8 topics |
| FLUENT | *Fluent Python*, 2nd edition, Luciano Ramalho (O'Reilly, 2022), chapters as each week row names them (section 6.9 trigger met Oct 5) | Second pass for Y3 and Y8, named chapters only |
| MYPY | [mypy docs](https://mypy.readthedocs.io/en/stable/): Getting started; Using mypy with an existing codebase (checked 2026-10-05) | Y1 |
| PYTEST, HYP | [pytest](https://docs.pytest.org/), [Hypothesis](https://hypothesis.readthedocs.io/) | Test depth |
| DOCKER, GHA | [Docker docs](https://docs.docker.com/), [GitHub Actions docs](https://docs.github.com/actions) | Authority |
| PROM, USE | [Prometheus instrumentation](https://prometheus.io/docs/practices/instrumentation/), [USE method](https://www.brendangregg.com/usemethod.html) | Metrics |
| SRE | [Google SRE book](https://sre.google/sre-book/table-of-contents/), chapters 6, 21, 22, 23 | Monitoring, overload, consensus |
| HI, HI-YT | [Hello Interview](https://www.hellointerview.com/) Core Concepts and Key Technologies; its YouTube mock walkthroughs | Design course |
| KLEP | [Martin Kleppmann, Distributed Systems lectures](https://www.youtube.com/playlist?list=PLeKd45zvjcDFUEv_ohr_HdUFe97RItdiB), [lecture notes](https://www.cl.cam.ac.uk/teaching/2122/ConcDisSys/dist-sys-notes.pdf) | Distributed systems video |
| PRIMER | [system-design-primer](https://github.com/donnemartin/system-design-primer) | Gap filler |
| WAT, ALLD, RG | [workat.tech machine coding](https://workat.tech/machine-coding), [awesome-low-level-design](https://github.com/ashishps1/awesome-low-level-design), [Refactoring.Guru](https://refactoring.guru/design-patterns) | LLD practice and patterns |
| OSTEP, HPBN | [OSTEP](https://pages.cs.wisc.edu/~remzi/OSTEP/), [High Performance Browser Networking](https://hpbn.co/) | OS, concurrency, networking |
| GRPC, OWASP | [gRPC core concepts](https://grpc.io/docs/what-is-grpc/core-concepts/), [OWASP API Security Top 10, 2023](https://owasp.org/API-Security/editions/2023/en/0x11-t10/) | RPC, API security |
| INTERDB | [The Internals of PostgreSQL](https://www.interdb.jp/pg), Hironobu Suzuki (covers v14 and earlier; the core ideas hold) | Main text for MVCC, VACUUM, WAL, replication |
| GOBYEX | [Go by Example](https://gobyexample.com/) (linked from go.dev) | "How do I do X" instead of package docs |
| GO100 | [100 Go Mistakes](https://100go.co/) (free site for the book) | The classic Go traps with examples |
| RP-ASYNC | [Real Python: asyncio walkthrough](https://realpython.com/async-python/) (about 40 minutes) | Main text for asyncio |
| K8SAF | [Kubernetes Failure Stories](https://k8s.af/) | Real postmortems |
| JVNS, MWDNS | [Julia Evans' blog](https://jvns.ca/), [Mess With DNS](https://messwithdns.net/) | Networking explained plainly; a real DNS server to break |
| BBG | ByteByteGo on YouTube | Short visual design refreshers |
| ARDAN | Ardan Labs blog: [Scheduling in Go, parts I-III](https://www.ardanlabs.com/blog/2018/08/scheduling-in-go-part2.html), Garbage Collection in Go parts I-III, and its Kubernetes CPU and memory limits articles for Go | Go scheduler and GC at interview level |
| VEGETA | `vegeta` HTTP load generator (the older `hey` is unmaintained) | O1 load experiment |
| Peers | A real engineer who interrupts | Human mocks |

### 1a Foundations: W0 to W18, Oct 1 2026 to Feb 7 2027

| Week | Work, hours and resources | Proof due |
| --- | --- | --- |
| W0 · Oct 1-4 · 3h | **Setup** 1h: Oct 1 procedure: evidence, gap diagnosis, change control, freeze · **DSA** 2h: Due colds first: 143 and 19 (day 7); then the stack lesson and NEW 20 Valid Parentheses [NC] | Oct 1 handoff recorded; amendments accepted and the file frozen |
| W1 · Oct 5-11 · 15h | **DSA** 3.5h: NEW 155 Min Stack, 739 Daily Temperatures (monotonic stack) [NC] · **MC1** 2.5h: Rep 1: Snake and Ladder, 90 min timed, no AI, raw notes committed before any cleanup, then a 60-minute review [WAT] · **Y2** 1h: Checklist D baseline, cold [section 7] · **G1** 0.5h: Install Go, Hello World, Integers, Iteration [FCC-Go ch 1-3, LGWT, GOBYEX for lookups] · **R1** 1h: Resume v1 draft · **R1** 2h: Naukri and LinkedIn live, every filter field filled, notice 90 days · **L1** 1h: OOP pillars, interface vs abstract class, composition [ARJAN, RG] · **P1** 1.5h: Python prerequisites, taught right before use: context managers and `with`, pytest fixtures with `yield`, dataclass equality [RP ("Python's with Statement: Manage External Resources Safely"), PYTEST (fixtures), MCODING] · **P1** 1.5h: psycopg 3 prerequisite first (Getting Started: basic usage, passing parameters, transactions; a 15-line insert, select, rollback practice script), then repositories for all 5 entities with rollback tests [PSY] · **Proofs and weekly close** 0.5h | Closes MC1, Y2 |
| W2 · Oct 12-18 · 15h | **DSA** 3.5h: Binary search lessons 14-15; NEW 704 Binary Search [NC] · **P1** 3h: psycopg 3 prerequisite first (Getting Started: basic usage, passing parameters, transactions; a 15-line insert, select, rollback practice script), then repositories for all 5 entities with rollback tests (continued) [PSY] · **G1** 2.5h: Install Go, Hello World, Integers, Iteration (continued) [FCC-Go ch 1-3, LGWT, GOBYEX for lookups] · **K1** 1.5h: kind cluster up, first pod [KK (Core Concepts intro), KIND] · **H1** 1h: Delivery framework; watch one full mock [HI, HI-YT] · **R3** 1.5h: 60-second pitch and recruiter answers · **L1** 1.5h: Association, aggregation, coupling and cohesion [ARJAN] · **Proofs and weekly close** 0.5h | Capacity check: under 10 hrs/week average since Oct 1 means re-forecast now; Closes G1 |
| W3 · Oct 19-25 · 15h | **DSA** 3.5h: NEW 74 Search a 2D Matrix, 875 Koko Eating Bananas [NC] · **P1** 1.5h: psycopg 3 prerequisite first (Getting Started: basic usage, passing parameters, transactions; a 15-line insert, select, rollback practice script), then repositories for all 5 entities with rollback tests (continued) [PSY] · **G2** 3h: Arrays and slices: `len` vs `cap`, `append`, aliasing [FCC-Go ch 8, LGWT, GO-SLICES] · **K1** 2h: `kubectl` drill: get, describe, logs, exec, events, `-o yaml` [KK (Imperative Commands with kubectl, and its practice test), K8S] · **R2** 3h: Write the 2-3 honest stories; fix the registry figures [section 6.8] · **L2** 1.5h: SOLID: SRP, OCP, LSP [ARJAN] · **Proofs and weekly close** 0.5h | Closes G2 |
| W4 · Oct 26-Nov 1 · 15h | **DSA** 3.5h: Recursion lessons 8-9, trees 16-17; NEW 226 Invert Binary Tree, 104 Maximum Depth [NC] · **L2** 1h: SOLID: SRP, OCP, LSP (continued) [ARJAN] · **P1** 2h: psycopg 3 prerequisite first (Getting Started: basic usage, passing parameters, transactions; a 15-line insert, select, rollback practice script), then repositories for all 5 entities with rollback tests (continued) [PSY] · **G3** 3h: Structs, methods and interfaces; receivers [FCC-Go ch 4-5, LGWT] · **K1** 0.5h: `kubectl` drill: get, describe, logs, exec, events, `-o yaml` (continued) [KK (Imperative Commands with kubectl, and its practice test), K8S] · **R2** 1h: Write the 2-3 honest stories; fix the registry figures (continued) [section 6.8] · **L1** 0.5h: Composition over inheritance, cold explanation [ARJAN] · **P2** 3h: SQL correction, lesson before exercise: SQLBolt lessons on joins, outer joins and NULLs, then its subqueries and set-operations topics (IN, UNION); then pgexercises Joins and Subqueries [SQLBOLT, PG-TUT (Window Functions), PGEX] · **Proofs and weekly close** 0.5h | Closes P1, K1, L1 |
| W5 · Nov 2-8 · 8h | **DSA** 2h: NEW 102 Level Order Traversal; colds [NC] · **G3** 1.5h: Structs, methods and interfaces; receivers (continued) [FCC-Go ch 4-5, LGWT] · **K2** 3h: Architecture: every component; the chain after `kubectl apply`; controller anatomy: watch, cache, work queue, reconcile, requeue with backoff, finalizers, owner references, leader election [KK (Core Concepts: etcd, API server, controller manager, scheduler, kubelet, kube-proxy), K8S] · **H1** 1h: Delivery framework; watch one full mock (continued) [HI, HI-YT] · **Proofs and weekly close** 0.5h | Diwali week. Calibration lane opens: 2-3 low-stakes processes; Closes G3 |
| W6 · Nov 9-15 · 15h | **DSA** 3.5h: NEW 98 Validate BST; heap lessons 23-25; NEW 703 Kth Largest in a Stream [NC] · **H1** 0.5h: Delivery framework; watch one full mock (continued) [HI, HI-YT] · **R2** 2h: Tell each story aloud; answer follow-ups [section 6.8] · **L2** 2.5h: SOLID: ISP, DIP; violation and fix for each [ARJAN] · **P2** 3h: SQL correction, lesson before exercise: SQLBolt lessons on joins, outer joins and NULLs, then its subqueries and set-operations topics (IN, UNION); then pgexercises Joins and Subqueries (continued) [SQLBOLT, PG-TUT (Window Functions), PGEX] · **L3** 3h: Strategy, Factory, Observer [RG, ARJAN] · **Proofs and weekly close** 0.5h | JD harvest with the lane-size check (campaign reserve); Closes L2 |
| W7 · Nov 16-22 · 15h | **DSA** 3.5h: NEW 1046 Last Stone Weight, 973 K Closest Points [NC] · **G4** 4h: Pointers and errors: `*` and `&`, the nil-interface trap, `%w`, `errors.Is` and `errors.As` [FCC-Go ch 6 and 11, LGWT (Pointers and errors, Error types), GO-ERRORS, GO100] · **K2** 2h: Architecture: every component; the chain after `kubectl apply`; controller anatomy: watch, cache, work queue, reconcile, requeue with backoff, finalizers, owner references, leader election (continued) [KK (Core Concepts: etcd, API server, controller manager, scheduler, kubelet, kube-proxy), K8S] · **H1** 1.5h: Framework dry run, then a first full design on paper, graded [HI] · **L3** 0.5h: Strategy, Factory, Observer (continued) [RG, ARJAN] · **P2** 3h: SQLBolt aggregates and order of execution, then pgexercises Aggregation (GROUP BY, HAVING); window functions lesson, then the window exercises [SQLBOLT, PG-TUT (Window Functions), PGEX] · **Proofs and weekly close** 0.5h | Closes K2 |
| W8 · Nov 23-29 · 15h | **DSA** 3.5h: Intervals explainer; NEW 56 Merge Intervals, 57 Insert Interval [NC] · **G4** 1h: Pointers and errors: `*` and `&`, the nil-interface trap, `%w`, `errors.Is` and `errors.As` (continued) [FCC-Go ch 6 and 11, LGWT (Pointers and errors, Error types), GO-ERRORS, GO100] · **K3** 3h: Pods, Deployment to ReplicaSet, rollout status, history, undo [KK (Pods, ReplicaSets, Deployments practice tests; Application Lifecycle: Rolling Updates and Rollbacks), K8S (Workloads)] · **H1** 1h: Framework dry run, then a first full design on paper, graded (continued) [HI] · **L3** 3.5h: State, Decorator; class and sequence diagrams [RG] · **P2** 2h: SQLBolt aggregates and order of execution, then pgexercises Aggregation (GROUP BY, HAVING); window functions lesson, then the window exercises (continued) [SQLBOLT, PG-TUT (Window Functions), PGEX] · **G5** 0.5h: Maps; Generics chapter [FCC-Go ch 9 and 15, LGWT (Maps, Generics)] · **Proofs and weekly close** 0.5h | Closes G4, H1, L3 |
| W9 · Nov 30-Dec 6 · 15h | **DSA** 3.5h: Prefix sums lesson; NEW 303 Range Sum Query, 560 Subarray Sum Equals K [NC] · **G5** 2.5h: Maps; Generics chapter (continued) [FCC-Go ch 9 and 15, LGWT (Maps, Generics)] · **K3** 3h: StatefulSet vs DaemonSet vs Job; requests, limits, QoS; the three probe types; HPA vs VPA vs cluster autoscaler [KK (Scheduling: Resource Requirements, DaemonSets), K8S (StatefulSet, Job and CronJob, probes, QoS)] · **H2** 1h: Load balancing, caching, CDN, queues, rate limiting [HI (Core Concepts), BBG] · **MC2** 2.5h: Rep 2: Splitwise, 90 min timed plus review [WAT] · **Y1** 2h: PRCP has no mypy config yet: type hints, `Optional`, generics, `Callable`; install and configure mypy; then `mypy --strict` clean on `src/prcp` [PYDOCS (typing), MYPY (Getting started, Using mypy with an existing codebase)] · **Proofs and weekly close** 0.5h | Closes G5, K3, MC2 |
| W10 · Dec 7-13 · 15h | **DSA** 3.5h: Backtracking lesson 22; NEW 78 Subsets, 39 Combination Sum (40 total) [NC] · **Y1** 2h: PRCP has no mypy config yet: type hints, `Optional`, generics, `Callable`; install and configure mypy; then `mypy --strict` clean on `src/prcp` (continued) [PYDOCS (typing), MYPY (Getting started, Using mypy with an existing codebase)] · **G6** 3h: Dependency injection, mocking, HTTP server, httptest [LGWT (Dependency Injection, Mocking, HTTP server)] · **K4** 3h: Services, EndpointSlices, the Service dataplane (iptables mode, not IPVS internals), cluster DNS; CNI vs CSI at architecture level [KK (Networking: Service Networking, DNS, CoreDNS, Ingress), K8S (Virtual IPs)] · **H2** 0.5h: Load balancing, caching, CDN, queues, rate limiting (continued) [HI (Core Concepts), BBG] · **P2** 2.5h: pgexercises Working with Timestamps and Modifying Data; 3 timed unseen problems set by the assistant [SQLBOLT, PG-TUT (Window Functions), PGEX] · **Proofs and weekly close** 0.5h | Closes Y1 |
| W11 · Dec 14-20 · 15h | **DSA** 3.5h: Colds only [NC] · **P2** 1h: pgexercises Working with Timestamps and Modifying Data; 3 timed unseen problems set by the assistant (continued) [SQLBOLT, PG-TUT (Window Functions), PGEX] · **G6** 1.5h: Dependency injection, mocking, HTTP server, httptest (continued) [LGWT (Dependency Injection, Mocking, HTTP server)] · **K4** 1h: Services, EndpointSlices, the Service dataplane (iptables mode, not IPVS internals), cluster DNS; CNI vs CSI at architecture level (continued) [KK (Networking: Service Networking, DNS, CoreDNS, Ingress), K8S (Virtual IPs)] · **H2** 3h: Load balancing, caching, CDN, queues, rate limiting (continued) [HI (Core Concepts), BBG] · **G7** 2h: Goroutines, channels, select, closed-channel reads [FCC-Go ch 13, LGWT (Concurrency, Select), PIKE] · **P3** 2.5h: Isolation intuition before the docs [TS-ISO, CMU (Multi-Version Concurrency Control)] · **Proofs and weekly close** 0.5h | Closes P2, G6, K4 |
| W12 · Dec 21-27 · 8h | **DSA** 2h: Colds only [NC] · **G7** 1.5h: Goroutines, channels, select, closed-channel reads (continued) [FCC-Go ch 13, LGWT (Concurrency, Select), PIKE] · **K5** 3h: ConfigMap env vs volume, Secret, ServiceAccount, RBAC least-privilege lab [KK (Application Lifecycle: ConfigMaps, Secrets; Security: RBAC, ServiceAccounts), K8S (RBAC good practices)] · **H2** 1h: Load balancing, caching, CDN, queues, rate limiting (continued) [HI (Core Concepts), BBG] · **Proofs and weekly close** 0.5h | Light week |
| W13 · Dec 28-Jan 3 · 8h | **DSA** 2h: Colds only [NC] · **H2** 1.5h: Load balancing, caching, CDN, queues, rate limiting (continued) [HI (Core Concepts), BBG] · **P3** 3.5h: B-tree, composite order, index-only scans; EXPLAIN ANALYZE; ADR [UTIL (Anatomy of an Index, The Where Clause), PG (Indexes, Using EXPLAIN), CMU (Join Algorithms)] · **G7** 0.5h: `sync.Mutex` vs `RWMutex`, `WaitGroup`, context; scheduler model (G, M, P) and GC basics [FCC-Go ch 14, LGWT (Sync, Context), GO-CONTEXT, GO-PIPELINES, ARDAN (Scheduling in Go, Garbage Collection in Go)] · **Proofs and weekly close** 0.5h | Light week |
| W14 · Jan 4-10 · 15h | **DSA** 3.5h: Colds only [NC] · **G7** 3h: `sync.Mutex` vs `RWMutex`, `WaitGroup`, context; scheduler model (G, M, P) and GC basics (continued) [FCC-Go ch 14, LGWT (Sync, Context), GO-CONTEXT, GO-PIPELINES, ARDAN (Scheduling in Go, Garbage Collection in Go)] · **K5** 1h: ConfigMap env vs volume, Secret, ServiceAccount, RBAC least-privilege lab (continued) [KK (Application Lifecycle: ConfigMaps, Secrets; Security: RBAC, ServiceAccounts), K8S (RBAC good practices)] · **P3** 3.5h: Isolation levels, MVCC, row locks, deadlocks; two-session demos [INTERDB (Concurrency Control), PG (Concurrency Control), CMU (Two-Phase Locking)] · **H2** 1.5h: Object storage, WebSocket vs SSE, IDs, storage selection [HI (Key Technologies), BBG] · **K7** 2h: Scenarios 1-3 on a sample app: CrashLoopBackOff, Pending, OOMKilled [KK (Troubleshooting: Application Failure labs), LEARNK8S, K8S (Debug)] · **Proofs and weekly close** 0.5h | Closes G7, K5 |
| W15 · Jan 11-17 · 15h | **DSA** 3.5h: Colds only [NC] · **K7** 0.5h: Scenarios 1-3 on a sample app: CrashLoopBackOff, Pending, OOMKilled (continued) [KK (Troubleshooting: Application Failure labs), LEARNK8S, K8S (Debug)] · **H2** 3.5h: Object storage, WebSocket vs SSE, IDs, storage selection (continued) [HI (Key Technologies), BBG] · **P3** 2.5h: WAL on commit, pooling, replication and failover, VACUUM; code-read how `psycopg_pool` hands out a connection [INTERDB (VACUUM, WAL, Replication), PG (Reliability and the Write-Ahead Log, Routine Vacuuming, High Availability), HN] · **K7** 1.5h: Scenarios 4-5: Service without endpoints; an object stuck on a finalizer [KK (Troubleshooting labs), LEARNK8S, K8S (Debug)] · **P4** 3h: SQLAlchemy 2.0: port repositories, same tests [SQLA] · **Proofs and weekly close** 0.5h | Closes H2, P3 |
| W16 · Jan 18-24 · 15h | **DSA** 2.5h: Colds only [NC] · **P4** 1.5h: SQLAlchemy 2.0: port repositories, same tests (continued) [SQLA] · **P4** 2h: Alembic: an expand, backfill, contract migration with old and new app versions running together; a quick N+1 check [SQLA, ALEMBIC] · **Y3** 2.5h: Names and references: everything is an object, `is` vs `==`, mutable vs immutable, how arguments are passed [RP ("Shallow vs Deep Copying of Python Objects": the mutable vs immutable part), FLUENT (ch 6), MCODING] · **Y3** 1.5h: Shallow vs deep copy: the `copy` module, copies of nested lists [RP ("Shallow vs Deep Copying of Python Objects"), FLUENT (ch 6)] · **Y3** 3h: Hashing: what a hash table does, the `__eq__` and `__hash__` contract, why a list cannot be a dict key, list, dict and set costs [FLUENT (ch 3), MCODING] · **Y3** 1.5h: Iterables vs iterators: the iterator protocol, what a `for` loop really does, why an iterator gets used up [RP ("Iterators and Iterables in Python: Run Efficient Iterations"), FLUENT (ch 17)] · **Proofs and weekly close** 0.5h | Work in progress |
| W17 · Jan 25-31 · 15h | **DSA** 2.5h: Colds only [NC] · **Y3** 1h: Iterables vs iterators: the iterator protocol, what a `for` loop really does, why an iterator gets used up (continued) [RP ("Iterators and Iterables in Python: Run Efficient Iterations"), FLUENT (ch 17)] · **Y3** 2.5h: Generators: `yield`, generator expressions, lazy evaluation [RP ("How to Use Generators and yield in Python"), FLUENT (ch 17), MCODING] · **Y3** 3h: Functions as objects: `*args` and `**kwargs`, scope and the LEGB rule, `nonlocal`, closures [RP ("Python args and kwargs: Demystified", "Python Scope and the LEGB Rule", "Python Closures: Common Use Cases and Examples"), FLUENT (ch 7, 9)] · **Y3** 3h: Decorators: what `@` does, wrappers, `functools.wraps`, decorators with arguments, PRCP's route decorators [RP ("Primer on Python Decorators"), FLUENT (ch 9), ARJAN] · **Y3** 2.5h: Exceptions: the hierarchy, `try`, `except`, `else`, `finally`, `raise from`, custom exceptions such as PRCP's `exceptions.py` [RP ("Python Exceptions: An Introduction"), FLUENT (ch 18)] · **Proofs and weekly close** 0.5h | Work in progress |
| W18 · Feb 1-7 · 13.5h | **DSA** 4.5h: Colds only [NC] · **Y3** 2h: Context managers in depth: what `__exit__` receives, suppressing an exception, `contextlib.contextmanager` [RP ("Python's with Statement: Manage External Resources Safely"), FLUENT (ch 18)] · **P4** 2.5h: Alembic: an expand, backfill, contract migration with old and new app versions running together; a quick N+1 check (continued) [SQLA, ALEMBIC] · **S1** 0.5h: Checklist A baseline, cold, recorded per section 7 [section 7] · **Gate** 4h: Gate A: Go practical, Checklist B fundamentals half, K8s audit 10/15, DSA 40/24 | Closes Y3, P4; GATE A |

### 1b Build and design: W19 to W37, Feb 8 to Jun 20 2027

| Week | Work, hours and resources | Proof due |
| --- | --- | --- |
| W19 · Feb 8-14 · 15h | **DSA** 2.5h: Graph lessons 28-31; NEW 200 Number of Islands [NC] · **D1** 3h: Multi-stage Dockerfile, non-root user, `.dockerignore` [NANA-DOCKER, DOCKER] · **A1** 3h: Sequential agent: config, `net/http`, per-probe timeout; code-read the timeout fields of the `net/http` Client [LGWT (HTTP server, JSON), EFFGO] · **L4** 1h: Where the lock goes; lock granularity [PYDOCS (threading)] · **H3** 3h: Replication and quorums, lectures 5.1-5.3 [KLEP] · **S1** 2h: Locks, condition variables, semaphores [OSTEP (Concurrency)] · **Proofs and weekly close** 0.5h | Work in progress |
| W20 · Feb 15-21 · 15h | **DSA** 2.5h: Colds only [NC] · **Y8** 3h: Classes from the ground up: `__init__` and `self`, instance vs class attributes, `@classmethod` and `@staticmethod`, special methods, `Enum` [RP ("Object-Oriented Programming (OOP) in Python", "Python's Magic Methods: Leverage Their Power in Your Classes"), FLUENT (ch 11), PYDOCS (enum)] · **A1** 3h: Sequential agent: config, `net/http`, per-probe timeout; code-read the timeout fields of the `net/http` Client (continued) [LGWT (HTTP server, JSON), EFFGO] · **L4** 2h: A thread-safe class with a test that fails without the lock [PYDOCS (threading, queue)] · **H3** 1.5h: Replication and quorums, lectures 5.1-5.3 (continued) [KLEP] · **S1** 0.5h: Locks, condition variables, semaphores (continued) [OSTEP (Concurrency)] · **R1** 2h: Resume refresh: Go is now listable · **Proofs and weekly close** 0.5h | Closes A1, L4, R1 |
| W21 · Feb 22-28 · 15h | **DSA** 2.5h: Colds only [NC] · **D1** 2h: Compose with Postgres and healthchecks [NANA-DOCKER (Compose), DOCKER] · **A2** 3h: `errgroup` with `SetLimit` (the only concurrency model in the agent), cancellation; `-race` clean [PIKE, GO-PIPELINES, ERRGROUP] · **MC3** 2.5h: Rep 3: in-memory relational datastore [WAT, ALLD] · **H3** 3h: Partitioning, consistent hashing, consistency models, lectures 7.2-7.3 [KLEP, HI] · **S1** 1.5h: Common concurrency bugs, mapped to Go and Python [OSTEP, BEAZ] · **Proofs and weekly close** 0.5h | Closes D1, MC3 |
| W22 · Mar 1-7 · 15h | **DSA** 2.5h: Topological sort lesson; NEW 994 Rotting Oranges, 210 Course Schedule II [NC] · **S1** 1h: Common concurrency bugs, mapped to Go and Python (continued) [OSTEP, BEAZ] · **Y8** 2.5h: Dataclasses in depth: generated methods, `field()`, the mutable-default trap, `frozen`, `slots` [RP (realpython.com/python-data-classes), FLUENT (ch 5)] · **A2** 3h: `errgroup` with `SetLimit` (the only concurrency model in the agent), cancellation; `-race` clean (continued) [PIKE, GO-PIPELINES, ERRGROUP] · **MC4** 2.5h: Rep 4: thread-safe key-value store with TTL, or a job scheduler [WAT] · **H3** 1.5h: Partitioning, consistent hashing, consistency models, lectures 7.2-7.3 (continued) [KLEP, HI] · **R2** 1.5h: New work stories; monthly rehearsal [section 6.8] · **Proofs and weekly close** 0.5h | Closes S1, MC4, H3 |
| W23 · Mar 8-14 · 15h | **DSA** 2.5h: Union-find built from scratch, NEW 684 Redundant Connection; Dijkstra, NEW 743 Network Delay Time [NC] · **D2** 3h: Namespaces, cgroups, layers, PID 1 and SIGTERM [DOCKER] · **A2** 2h: `errgroup` with `SetLimit` (the only concurrency model in the agent), cancellation; `-race` clean (continued) [PIKE, GO-PIPELINES, ERRGROUP] · **MC5** 2.5h: Rep 5: reservation system, AI-assisted [WAT] · **H4** 3h: Failure models, consensus, Raft, leases, split brain, lectures 2.1-2.4 and 6.1-6.2 [KLEP] · **S2** 1.5h: DNS, TCP handshake, TLS cost, with `dig`, `curl -v`, `openssl s_client` [JVNS, MWDNS, HPBN, HN] · **Proofs and weekly close** 0.5h | Closes D2, A2, MC5 |
| W24 · Mar 15-21 · 15h | **DSA** 2.5h: DP lessons 32-33; NEW 70 Climbing Stairs, 62 Unique Paths [NC] · **C1** 3.5h: CI: lint, mypy, tests, coverage, image build [GHA] · **A3** 3h: POST results, retries with backoff and jitter, idempotency key [SRE (ch 22)] · **H4** 2h: Failure models, consensus, Raft, leases, split brain, lectures 2.1-2.4 and 6.1-6.2 (continued) [KLEP] · **S2** 3h: HTTP/2, pooling, timeouts vs deadlines, L4 vs L7, retry amplification; `ss` for connection states; one `tcpdump` capture of a handshake [HPBN, HN] · **R2** 0.5h: New work stories; monthly rehearsal (continued) [section 6.8] · **Proofs and weekly close** 0.5h | Closes R2 |
| W25 · Mar 22-28 · 15h | **DSA** 2.5h: Greedy, NEW 53 Maximum Subarray; Trie, NEW 208 Implement Trie [NC] · **C1** 0.5h: CI: lint, mypy, tests, coverage, image build (continued) [GHA] · **A3** 2h: POST results, retries with backoff and jitter, idempotency key (continued) [SRE (ch 22)] · **H4** 3h: Overload, cascading failure, retries, idempotency [SRE (ch 21-22)] · **S2** 1.5h: HTTP/2, pooling, timeouts vs deadlines, L4 vs L7, retry amplification; `ss` for connection states; one `tcpdump` capture of a handshake (continued) [HPBN, HN] · **R3** 2.5h: 5-minute PRCP narrative, timed; outline one production system you owned for a deep dive [section 6.8] · **C1** 2.5h: Self-gating: PRCP gates its own release [GHA] · **Proofs and weekly close** 0.5h | Closes A3 |
| W26 · Mar 29-Apr 4 · 15h | **DSA** 2.5h: Bit manipulation, NEW 136 Single Number (50 total, all 16 families) [NC] · **C1** 1.5h: Self-gating: PRCP gates its own release (continued) [GHA] · **A4** 3h: `log/slog`, `client_golang` metrics, graceful SIGTERM; code-read how a `client_golang` histogram records a value [GO-SLOG, CLIENTGO] · **H4** 1h: Overload, cascading failure, retries, idempotency (continued) [SRE (ch 21-22)] · **S2** 2h: Diagnose a planted timeout with `dig`, `curl -v`, `ss`, `tcpdump`, then write it up [HPBN] · **R4** 3h: Resume v2 against the JD frequency table · **Y4** 1.5h: asyncio from zero: coroutines vs functions, `await`, the event loop, tasks [RP-ASYNC, MCODING] · **Proofs and weekly close** 0.5h | Closes C1, S2, R4 |
| W27 · Apr 5-11 · 15h | **DSA** 2.5h: Colds; first blind mixed set [NC] · **Y4** 1h: asyncio from zero: coroutines vs functions, `await`, the event loop, tasks (continued) [RP-ASYNC, MCODING] · **Y4** 4h: `TaskGroup`, semaphores, cancellation, timeouts [RP-ASYNC, BEAZ, PYDOCS (asyncio)] · **A4** 2h: `log/slog`, `client_golang` metrics, graceful SIGTERM; code-read how a `client_golang` histogram records a value (continued) [GO-SLOG, CLIENTGO] · **H4** 3h: 2PC vs Saga vs outbox, delivery semantics, DLQ, multi-region, lecture 7.1 [KLEP, SRE (ch 23)] · **S3** 2h: gRPC: protobuf evolution, streaming, deadlines, status codes [GRPC] · **Proofs and weekly close** 0.5h | Closes A4 |
| W28 · Apr 12-18 · 15h | **DSA** 2.5h: Colds [NC] · **S3** 1h: gRPC: protobuf evolution, streaming, deadlines, status codes (continued) [GRPC] · **Y4** 4.5h: Bounded async fan-out; starvation lab and write-up [RP-ASYNC, PYDOCS (asyncio)] · **A5** 3h: Leak lab: remove a timeout, find it in pprof, fix it, add a test [GO-PPROF, GO100] · **H4** 1h: 2PC vs Saga vs outbox, delivery semantics, DLQ, multi-region, lecture 7.1 (continued) [KLEP, SRE (ch 23)] · **S4** 2.5h: Process vs thread, virtual memory, file descriptors, page cache, OOM, signals, practised on a misbehaving process with `ps`, `top`, `/proc`, `lsof`, `strace`, `ulimit` [OSTEP (Virtualization)] · **Proofs and weekly close** 0.5h | Closes S3, H4 |
| W29 · Apr 19-25 · 15h | **DSA** 2.5h: Colds; blind mixed set [NC] · **S4** 2.5h: Process vs thread, virtual memory, file descriptors, page cache, OOM, signals, practised on a misbehaving process with `ps`, `top`, `/proc`, `lsof`, `strace`, `ulimit` (continued) [OSTEP (Virtualization)] · **Y4** 3h: Bounded async fan-out; starvation lab and write-up (continued) [RP-ASYNC, PYDOCS (asyncio)] · **A5** 3h: Leak lab: remove a timeout, find it in pprof, fix it, add a test (continued) [GO-PPROF, GO100] · **O1** 3.5h: `/metrics`, `/live`, `/ready`; counter, gauge, histogram; label cardinality; load experiment: throughput, p50/p95/p99, saturation point, one bottleneck [PROM, VEGETA, SRE (ch 6)] · **Proofs and weekly close** 0.5h | Closes S4, Y4, A5 |
| W30 · Apr 26-May 2 · 15h | **DSA** 2.5h: Colds [NC] · **Mock** 3h: Mock 1 with the assistant [HI] · **O1** 2h: `/metrics`, `/live`, `/ready`; counter, gauge, histogram; label cardinality; load experiment: throughput, p50/p95/p99, saturation point, one bottleneck (continued) [PROM, VEGETA, SRE (ch 6)] · **A6** 3h: Static binary image; ADR on control plane vs data plane [DOCKER] · **H5** 3h: Practice, one-page skeleton then spoken: multi-tenant PRCP at 10,000 services (isolation, quotas, noisy neighbours, per-tenant limits, blast radius); a job scheduler [HI, PRIMER] · **S5** 1h: API design; authn vs authz, JWT, mTLS; OWASP pass over PRCP [OWASP] · **Proofs and weekly close** 0.5h | Work in progress |
| W31 · May 3-9 · 15h | **DSA** 2.5h: Colds [NC] · **S5** 2h: API design; authn vs authz, JWT, mTLS; OWASP pass over PRCP (continued) [OWASP] · **O1** 5h: PromQL on your own metrics; one symptom alert; SLI and SLO; USE and RED; tracing concepts: trace, span, context propagation, sampling [PROM, USE] · **A6** 2h: Static binary image; ADR on control plane vs data plane (continued) [DOCKER] · **K6** 3h: Postgres, API and agent on kind; agent ServiceAccount with `automountServiceAccountToken: false`, no Role [K8S, KIND] · **Proofs and weekly close** 0.5h | Closes A6 |
| W32 · May 10-16 · 15h | **DSA** 2.5h: Colds; blind mixed set [NC] · **H5** 2.5h: Practice, one-page skeleton then spoken: multi-tenant PRCP at 10,000 services (isolation, quotas, noisy neighbours, per-tenant limits, blast radius); a job scheduler (continued) [HI, PRIMER] · **S5** 3h: API design; authn vs authz, JWT, mTLS; OWASP pass over PRCP (continued) [OWASP] · **O1** 0.5h: PromQL on your own metrics; one symptom alert; SLI and SLO; USE and RED; tracing concepts: trace, span, context propagation, sampling (continued) [PROM, USE] · **K6** 2h: Postgres, API and agent on kind; agent ServiceAccount with `automountServiceAccountToken: false`, no Role (continued) [K8S, KIND] · **H5** 3h: Practice: payment or reservation; rate limiter [HI, PRIMER] · **Y5** 1h: Threads from zero (start, join, a shared-counter race and its lock fix), processes, the GIL, threads vs processes vs asyncio, `cProfile` before and after [PYDOCS (threading, profile), BEAZ] · **Proofs and weekly close** 0.5h | Closes S5, O1, K6 |
| W33 · May 17-23 · 15h | **DSA** 2.5h: Colds [NC] · **Y5** 4h: Threads from zero (start, join, a shared-counter race and its lock fix), processes, the GIL, threads vs processes vs asyncio, `cProfile` before and after (continued) [PYDOCS (threading, profile), BEAZ] · **K7** 4h: Scenarios 6-10 on PRCP [LEARNK8S, K8SAF, K8S (Debug); optional bonus only if K7 time remains: KK (Troubleshooting: Control Plane, Worker Node, Network labs)] · **Y5** 2h: GIL, threads vs processes vs asyncio, `cProfile` before and after (continued) [PYDOCS (profile), BEAZ] · **H5** 1.5h: Practice: payment or reservation; rate limiter (continued) [HI, PRIMER] · **S6** 0.5h: IBM Cloud to AWS and GCP mapping, part 1 [official AWS and GCP product docs] · **Proofs and weekly close** 0.5h | Closes K7, Y5 |
| W34 · May 24-30 · 15h | **DSA** 2.5h: Colds only [NC] · **S6** 1h: IBM Cloud to AWS and GCP mapping, part 1 (continued) [official AWS and GCP product docs] · **Y6** 4.5h: pytest beyond the basics: fixture scopes, `conftest.py`, parametrize, `monkeypatch`, `tmp_path`; then Hypothesis on `decide()` [PYTEST, HYP] · **S6** 2.5h: Mapping table part 2; Terraform vocabulary [official AWS and GCP product docs] · **F1** 4h: ADR index; README leads with the verdict; a short ADR on Keptn, Argo Rollouts, Flagger; known limitations; tag `v1.0.0`; stranger test [GHA] · **Proofs and weekly close** 0.5h | Closes Y6, S6 |
| W35 · May 31-Jun 6 · 15h | **DSA** 2.5h: Colds only [NC] · **Mock** 3h: Mock 2 with a human [Peers, or a paid expert mock per section 6.9] · **F1** 2.5h: ADR index; README leads with the verdict; a short ADR on Keptn, Argo Rollouts, Flagger; known limitations; tag `v1.0.0`; stranger test (continued) [GHA] · **H5** 2.5h: Practice: notification service [HI] · **Mock** 3h: Mock 3 [HI] · **F1** 1h: Game day on kind: inject a database or probe-timeout failure, let the alert fire, diagnose, mitigate, write a postmortem and runbook [section 6.1] · **Proofs and weekly close** 0.5h | Closes H5 |
| W36 · Jun 7-13 · 15h | **DSA** 2.5h: Colds only [NC] · **F1** 3.5h: Game day on kind: inject a database or probe-timeout failure, let the alert fire, diagnose, mitigate, write a postmortem and runbook (continued) [section 6.1] · **Y8** 2.5h: Inheritance, MRO and `super()`, cooperative multiple inheritance [RP (realpython.com/python-super), FLUENT (ch 14)] · **Y8** 2.5h: ABC vs Protocol: nominal vs structural typing, `abstractmethod`, `runtime_checkable`, PRCP's repository Protocols [RP ("Implementing Interfaces in Python: ABCs and Protocols", "Python Protocols: Leveraging Structural Subtyping"), FLUENT (ch 13)] · **Y8** 1.5h: Reference counting, reference cycles, the `gc` module [RP ("Memory Management in Python"), FLUENT (ch 6)] · **Y7** 2h: PRCP code walk: every pre-plan module explained cold (Pydantic schemas, FastAPI `Depends` and `dependency_overrides`, Enums, exceptions, fixtures, `decide()`); fix or log what you cannot defend [section 6.1] · **Proofs and weekly close** 0.5h | Closes F1 |
| W37 · Jun 14-20 · 12.5h | **DSA** 4h: Colds only [NC] · **Y7** 3h: PRCP code walk: every pre-plan module explained cold (Pydantic schemas, FastAPI `Depends` and `dependency_overrides`, Enums, exceptions, fixtures, `decide()`); fix or log what you cannot defend (continued) [section 6.1] · **Y8** 1.5h: Checklist D cold re-run; repair what is still shaky [section 7] · **Gate** 4h: Gate B: checklists A, B, C, D; K8s audit plus live challenge; craft demo; 3 mocks; last 2 reps pass; latest blind set 80%; stories | Closes Y7, Y8; GATE B |

### 1c Convert: W38 to W39, Jun 21 to Jul 4 2027

| Week | Work, hours and resources | Proof due |
| --- | --- | --- |
| W38 · Jun 21-27 · 15h | **DSA** 5h: NEW 133 Clone Graph, 417 Pacific Atlantic Water Flow, 198 House Robber [NC] · **R3** 4h: Two 30-minute deep dives, timed: PRCP, and one sanitized production system you owned [section 6.8] · **MC6** 2.5h: Rep 6: cab or gym booking [WAT] · **Mock** 3h: Mock 4 with a human [Peers, or a paid expert mock per section 6.9] · **Proofs and weekly close** 0.5h | Closes R3, MC6, MOCK |
| W39 · Jun 28-Jul 4 · 10h | **DSA** 4h: NEW 322 Coin Change, 1143 Longest Common Subsequence (55 total); performance gate practice [NC] · **Gate** 2h: Re-run every checklist cold [section 7] · **Gate** 4h: Gate C: DSA 8 of 10 cold, 6 reps, 4 mocks, 5 stories, both deep dives | GATE C |

1c runs under 15 hours a week on purpose: interviews peak here and their hours come from the campaign reserve. If Gate B needs repairs, 1c has about 5 spare hours before Gate C moves.

**Running totals at each gate:** Gate A: DSA 40, reps 1-2, Go fundamentals, Kubernetes 10/15. Gate B: DSA 50 with all 16 families, reps 1-5 done, 3 mocks, agent shipped, PRCP v1.0 on kind. Gate C: DSA 55 with 40-45 cold, 6 reps, 4 mocks, 5 stories.

---

*Portable skills you can prove are the only insurance you control.*
