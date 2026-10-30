# Proposed changes from Phase 1 v3.8 to v3.9

**Author:** ChatGPT, Om's Phase 1 coach and Claude's equal partner.  
**Date:** 30 October 2026, IST.  
**Status:** PROPOSAL ONLY. No v3.9 master has been created. v3.8 and its approved checker remain unchanged. No new JD harvest was run.

## My recommendation

Make **Go, Kubernetes, AWS and Terraform a protected minimum**, demonstrated together in PRCP. Keep Python for the control plane and interviews. Keep the controller track for the control-plane role you want. Learning these four names is not the goal. You must build, debug and explain a system that uses them.

One correction matters: **3.8 already contains all four.** It has 68.5 hours of Go, 37 of Kubernetes, 46 of controller work and 33 of AWS/Terraform. Adding another foundation track would duplicate work. The useful 3.9 change is to protect the minimum, repair the sequence, and make the promised proofs executable.

I recommend five changes below. Helm and AI infrastructure remain separate choices with visible costs. The saved evidence supports the four-skill foundation; it does not justify turning every named technology into another compulsory course.

## What I read and verified

- Fresh `omieee/docs` at **495460458dedfa413739ba50ae4d4c275289098f**. The project attachments match `plan/` byte for byte: plan SHA-256 `25bb309e79a610f2b37651107d1b780cedd5e3897fd2c969fb0e2f3c4b0690a4`; checker `6c55bf071327801342463b4ac58efa721444a60c10d884a2dd9640178157f816`.
- Sections 0, 4-9 and the relevant section 14 rows, including current W4, 26 October to 1 November 2026. Both coach logs, both outboxes, the shared log and its later-refactor and continuity records. Fresh heads of the five learning/code repositories were also checked. This is a plan review, not a learner verdict or a rerun of Claude's proofs.
- Both saved harvest CSVs, their classification scripts, the 27 October CDP candidate proposal, both AI direction reviews, the office protocol, and the 28-29 October LinkedIn captures.
- The approved checker passes: **75 weeks, 834.5 hours, 146 DSA hours, 72.5 campaign hours**, with seven expected fragmentation warnings. All **25 existing negative mutations** are rejected as expected. Passing those checks does not prove that every teaching or scheduling promise is satisfied.

All repository links in the source list refer to the snapshot above. Existing postings were analysed from saved records, not re-opened or claimed to be live. Only the technical behaviour of errgroup, finalizers and envtest was checked against official documentation in this session.

## What the existing JD evidence actually says

The current CSVs contain **79 records**: 71 from Claude and eight from ChatGPT. One Claude record is an Om-supplied Oracle LinkedIn capture and is kept separate. The original search sample is therefore **78 records: 75 India and three international**. Only **20 India records have a populated day-level posted-date field**. That field includes source-recorded dates; it is not a claim that every date was independently verified on the employer's site.

| Signal in the saved India sample | All 75 | Dated-field subset, 20 |
| --- | ---: | ---: |
| Go required or accepted as one language choice | 54 | 13 |
| Go required with no alternative, under the saved hand coding | 21 | 6 |
| Python required or accepted as one choice | 37 | 12 |
| Kubernetes or a named managed Kubernetes platform in required/preferred skills | 54 | 13 |
| Public-cloud terms in required/preferred skills | 36 | 9 |
| Terraform field labelled required/preferred | 20 | 9 |
| Controller/operator field labelled required/preferred | 10 | 3 |
| Helm field labelled required/preferred | 8 | 2 |

Go and Python use the coaches' existing hand coding. Kubernetes/cloud counts use the saved classifier's vocabulary against required/preferred text. They are reproducible **mentions in this selected sample**, not a fresh audit of each employer's requirement. AWS is named in 40 of the 75 India records across skills, cloud fields or duties, including optional/context mentions. This supports retaining the existing AWS choice; it does not establish AWS's share of the whole market.

An example of why counts need care: Kong `CG-003` is tagged Terraform required, but its saved wording accepts Terraform **provider development OR Kubernetes operators OR stateful CI/CD**. It does not prove that every applicant needs Terraform, and provider development is Go software work, not the same skill as writing infrastructure configuration. Keep the wording, not just the tag.

The searches deliberately favoured Go, Python and Kubernetes. Many rows are undated, some source pages were unreadable, and the Gulf and Irish coverage gaps partly mean **not read**, not **no jobs**. Do not turn these counts into market-wide percentages, formal confidence claims, or an international lane decision. The newer Lease a Bike and SAP captures are useful qualitative signals and stay outside the original search denominator. Current skill gaps or location eligibility must not erase their technical demand signal.

## Five proposed changes

### F1. GAP: make the four-skill minimum explicit and protected

**What changes:** Sections 1, 4, 5 and 7 explicitly name Go, Kubernetes, AWS and Terraform as required for the full platform-readiness claim. Retain the existing units and role identity. Add AWS/Terraform fundamentals to the never-cut list. Remote state, locking and temporary CI credentials remain fundamentals; decorative PR comments and extra polish remain cuttable.

**Why and evidence:** All four already exist in sections 6.2, 6.3 and 6.11. Cloud is core in the narrative and Gate B, but absent from section 5's explicit never-cut line. The existing India records support this foundation. A stronger statement is useful; another duplicate syllabus is not.

| Skill | Minimum Om must independently demonstrate | Existing home |
| --- | --- | --- |
| Go | Write and test ordinary Go; explain slices, interfaces, pointers and errors; build a bounded concurrent probe agent; distinguish target failure from process failure; cancel and shut down without leaving work behind | G1-G7, A1-A6 |
| Kubernetes | Deploy API, database and agent locally; explain request routing, configuration, probes, resources and permissions; diagnose the ten specified failures; defend the controller separately | K1-K7b, OP1-OP7 |
| AWS | Explain identity permissions and the network path; run PRCP on EKS, AWS's managed Kubernetes, with managed Postgres; demonstrate access boundaries and cleanup | CL1, CL3 |
| Terraform | Write and change a small module; explain configuration versus recorded state; apply, inspect, import, identify drift and destroy; use shared state with locking and CI login through OIDC, which supplies temporary credentials | CL2, CL4, used in CL3 |

These are demonstration boundaries, not claims of production expertise. Python, SQL, design, machine coding, DSA and real ownership evidence still matter. No certification, second cloud or language switch is added.

**Proposed wording:**

```diff
 Section 1, after Role identity
+Required platform foundation: Go, Kubernetes, one public cloud (AWS), and
+Terraform. These are core skills for Om's chosen role. Each has a running
+artifact and an independent explanation. Python remains the control-plane
+and interview language. Completing these labs does not establish production
+experience in Go, AWS or controller development.

 Section 5, Never cut
+Add: AWS foundations, Terraform fundamentals, the CL3 deployment proof,
+and CL4's remote state, locking and temporary CI credentials.

 Section 4, Gate B
+Record the Go, Kubernetes, AWS and Terraform proofs separately. A missing
+one leaves full platform readiness incomplete even if the other three pass.
+Gate A remains the earlier foundation checkpoint; it does not certify the
+four-skill platform minimum. Earlier calibration applications may continue.
```

**Time cost:** 0 added learner hours. These requirements already have units and Gate B proofs. **Removed/date moved:** none for this change. **Risk reduced:** silently cutting one pillar or calling partial coverage complete.

### F2. BUG: make the deployment sequence and lab sessions executable

**What changes:** Repair the generator's dependency and session handling. Keep cloud after the Kubernetes basics. Bring the complete local agent deployment before the AWS deployment, and schedule CL3 as four whole 3-hour sessions.

**Evidence from the actual week map:**

| Item | v3.8 actually schedules | Proposed change |
| --- | --- | --- |
| Cloud foundations, CL1 | 8h spread across W36-W44, starting 7 June 2027 | Keep its funded scope; prefer longer connected sessions during the rebuild. Do not open AWS in W4 as another simultaneous beginner track |
| Terraform foundations, CL2 | 8h across W44-W51 | Keep before CL3; explain and run the small module before the EKS module |
| Complete agent deployment, K6b | W63, W66, W67, ending 16 January 2028 | Move its existing 2h to the first feasible slot after A6 closes in W45, before CL3 begins; give it an independent scheduling slot so it is not trapped behind the cloud queue |
| AWS deployment, CL3 | W51 1.5h; W52 3h; W54 3h; W55 3h; W57 1h; W58 0.5h | Four unsplit 3h lab entries. A lab includes setup Om does, apply, a smoke test, cleanup and the cost record. No half-hour cloud deployment lab |
| L3 prerequisite for MC2 | Last 0.25h of L3 lands in W36, although MC2 is in W18 | Put the remaining 0.25h before MC2. Preserve MC2's existing requirement instead of deleting it to get green output |

The last issue was exposed by the proposed checker: the approved checker combines every machine-coding label into `MC`, so its dependency on the individual label `MC2` is never evaluated. This is a plan/checker bug, not a reason to change any historical learner score.

**Proposed wording and generator rules:**

```diff
 Section 6.11, CL3
-Deploy the K6 manifests, smoke-test the gate, then terraform destroy.
+After K6b is proved on kind, deploy the API and agent to EKS with RDS as the
+database. Use an AWS overlay: do not deploy the local Postgres Pod as well.
+Show an agent result reaching the API and being stored, then remove the lab
+resources and record any deliberately retained state-storage resources.
+Four 3-hour sessions are indivisible in the week map. Each live session
+closes with cleanup; it cannot leave the deployment waiting for next week.

 Generator
+Schedule K6b independently after A6 and K6a, and before CL3.
+Represent CL3 as four atomic 3h lab parts. If a week has less than 3h,
+move the whole lab. Do not pour part of it into the week's remaining space.
+Validate prerequisites for fixed machine-coding entries as well as lanes.
+Check within-week execution order, not just the week numbers.
```

The AWS overlay is part of the already-funded CL3 deployment work. It must be explained, not copied blindly. Account/credit eligibility is checked when the lab is scheduled; a local Terraform plan is not accepted as proof of a live AWS deployment. Do not open an AWS credit period months early simply because the syllabus mentions an account.

**Time cost:** 0 new content hours: K6b 2h, CL3 12h and the L3 0.25h are already funded. Reordering can move other work and create retention work, so this is **not** a claim of zero calendar impact. **Removed/date moved:** no learning is removed. These existing hours replace later slots for the same units; the rebuilt generator must show the displaced units and fund any additional retrieval reps. **Risk reduced:** a deploy-before-integrate sequence, cloud sessions too short to complete, and a timed rep before its declared prerequisites.

### F3. BUG/GAP: correct the agent and controller proofs

This accepts the three concrete defects already discussed by both coaches on 27 October, with explicit implementation choices and more realistic time than a 15-minute edit allowance.

**A2, failed probes:** A down target, target timeout or invalid target response is recorded as that target's `ProbeResult`; it does not cancel unrelated probes. Cancellation of the parent run still stops the batch. Invalid global configuration is rejected before workers start; a fatal runner failure follows an explicitly defined batch-failure path. A cancelled or unmeasured target must never become a successful result. Also, do not reuse errgroup's derived context to push results after `Wait`; that context is cancelled when `Wait` returns. This is supported by the official [errgroup contract](https://pkg.go.dev/golang.org/x/sync/errgroup#WithContext).

**Finalizers, OP5:** A finalizer delays deletion until an explicit cleanup obligation is satisfied. The current gate adapter only reads PRCP; it registers nothing to deregister. Choose the smaller fix: **remove the invented deregistration from the shipped gate adapter**. Teach cleanup with a separate, labelled test fixture using the same resource type and an `httptest` service that stores a record keyed by the Kubernetes object's UID. Persist the finalizer before creating that record; failed cleanup retains it; already-absent cleanup succeeds; repeat reconciliation is safe. This fixture is not deployed in the PRCP release and adds no second CRD or PRCP production endpoint. The [Kubernetes finalizer contract](https://kubernetes.io/docs/concepts/overview/working-with-objects/finalizers/) supports this distinction.

**OP6, integration tests:** `envtest` starts an API server and etcd for controller tests. It is not a complete Kubernetes cluster. Require evidence that the named integration cases actually executed; missing binaries or skipped required cases fail that proof. Test a delayed PRCP response while the spec changes: an old answer must not be attributed to the new `observedGeneration`, the field identifying the spec version reflected by status. Refetch and requeue safely on conflict. Keep leader takeover and real cluster behaviour in OP7. The [Kubebuilder envtest guide](https://book.kubebuilder.io/reference/envtest) explains the missing built-in controllers and garbage-collection limitation.

| Exact unit change | v3.8 | Proposed | Added time and use |
| --- | ---: | ---: | --- |
| A2 | 8h | 9h | +1h: failure/cancellation trace, mixed-success test, explain-back |
| OP1 | 6h | 6.5h | +0.5h: envtest versus a real cluster, including its limits |
| OP5 | 7h | 9h | +2h: explicit fixture setup, cleanup failure and repeat-delete practice |
| OP6 | 8h | 9h | +1h: prove execution of integration cases and test a stale response |
| **Total** | | | **+4.5h** |

The added time includes Om's setup, reading, coding and explanation. Coach-side automated runs are separate. Existing generic finalizer work becomes the fixture work; the extra 2h funds its setup and failure cases. Apply the changed contract to section 6, the matching section 14 parts, Gate B and Checklist E together.

**Removed/date moved:** remove only the invalid deregistration requirement. Do not pay with DSA, design or core skills. Add 4.5h to Phase 1b and let Gate B/C move if the rebuild cannot place it safely. **Risk reduced:** incorrect probe results, a meaningless finalizer, and a green suite that did not exercise the controller.

### F4. BUG: write the latest teaching decisions into one consistent rule

**What changes:** Carry Om's 29 October instruction into section 0 safeguard 6, section 6.6 rule 11 and the session guidance. Repair the two current prerequisite/resource defects without adding another Python track.

```diff
 Section 0, safeguard 6
-At 1.5 times the box, stop, whatever the state; only Om extends.
+State the expected block size once and log active minutes quietly. During
+teaching, judge whether learning is progressing. If the work circles, stalls
+or causes frustration, pause, save the exact point and return in a later slot
+with a different explanation. Stop immediately when Om says stop.
+Keep the fixed timing of scored DSA checks, machine-coding reps and mocks.

 Section 6.6, rule 11
-DSA max 45 minutes a day.
+On a 2-hour planned day, DSA normally takes no more than about 1 hour.
+More requires Om's explicit agreement and productive flow. This is an upper
+guardrail, not a daily allocation. A missed scored attempt stays recorded;
+teaching and retry still happen in separate later slots.

 Section 5 and weekly guidance
+The week's scope is the minimum target. Extra progress is welcome when
+capacity is real and prerequisites are met. It does not silently increase
+future weekly capacity or convert activity minutes into passed scope.
```

This adopts Om's instruction; it is not permission for a coach to consume the whole day with DSA. In a 12h week, an hour of DSA on six days would be 6h, far above the scheduled W4 2.25h. Do not convert a daily maximum into a six-hour weekly entitlement. Required warm-ups also need funding beyond the existing trial; the 28-45h estimate in 3.8 remains unresolved until measured, not free.

For **Y7a**, replace “all `conftest.py` fixtures line by line” with “the storage fixtures and repository/schema code whose concepts have been taught.” Explicitly defer the FastAPI `TestClient`, `Depends` and `dependency_overrides` lines to Y7b. P1 proves the repository/database path and rollback; it does not claim HTTP dependency-injection mastery. If later work actually needs those HTTP concepts earlier, move that teaching before use through change control. Do not test them first. This selects the zero-added-hour option from Claude's 29 October note.

For **K1**, replace the 31-second “Core Concepts intro” learning step with the saved, previously checked KodeKloud sequence “Pods”, “Pods With YAML” and “Demo - Pods With YAML”, plus kind setup. The teaching coach checks availability and beginner fit again on the actual lesson day. Do not replay the part Om has already demonstrated.

**Time cost:** 0 fixed added hours. Y7a's untaught HTTP lines move to the already-existing Y7b scope; K1's actual lesson replaces its unsuitable orientation. Productive overruns remain measured. **Removed/date moved:** remove contradictory timing wording and premature proof obligations, not topic coverage. **Risk reduced:** teaching to a stopwatch, hidden DSA expansion and testing concepts before teaching them.

### F5. BUG: strengthen the Python checker without pretending it can grade understanding

**What changes:** Retain the approved checker and add the proposed structural checks in this folder. `check_plan_proposed.py` is a read-only executable prototype; `check_plan.py.diff` shows the equivalent proposed change to the single-file checker. Neither replaces `plan/check_plan.py`.

| Proposed automated rule | Failure it must catch |
| --- | --- |
| Mandatory unit inventory | Removing a whole pillar from both the curriculum and schedule, even if the totals are edited to agree |
| Ordered prerequisites using individual labels | A dependent item before its prerequisite in the same week; MC2 hidden by aggregation into MC; a missing prerequisite |
| Complete local deployment before AWS | CL3 before K6b has finished |
| Atomic CL3 sessions | Six fragments adding to 12h instead of four 3h labs |
| Gate inventory and order | Missing or duplicate gates; required platform units ending in or after the Gate B week |
| Structural parsing | Duplicate units/weeks, malformed rows, unparsed items and zero-hour entries |
| Protected cloud wording | AWS/public cloud and Terraform omitted from the never-cut line |

The checker can inspect dependencies and allocated sessions. It cannot prove that an AWS lab ran, an envtest case executed, a finalizer is correct, a resource is beginner-friendly or Om understands the code. Those require the unit's runtime evidence and interview. No regex searching for “understood” can replace that.

**Time cost:** 0 learner hours; implementation and regression tests are coach work. **Removed/date moved:** none. **Risk reduced:** false assurance from a mathematically balanced but unusable plan.

## Explicit decisions on the other coach discussions

| Topic | Recommendation for this proposal | Reason / cost |
| --- | --- | --- |
| Helm | Do not make it a fifth compulsory pillar in this amendment. Keep a concrete optional unit: one PRCP chart, values for two environments, lint/render/install/upgrade/rollback and one diagnosed mismatch | Eight tagged India rows are a useful signal, not evidence for a fabricated universal cutoff. Om can choose it for recurring owned work or target relevance. Cost remains **12-16h**, beginning after K6b for a full API/database/agent chart. It must displace named work or move dates |
| AI infrastructure | Keep the platform-facing direction open. Preserve the AI workflow checkpoint already in 3.8; do not add a second AI curriculum here | Existing captures show serving, evaluation, access and cost-control work. A future serving lab after the relevant Go/Kubernetes/controller prerequisites needs its own **13-15h provisional estimate**, not the old 4h interview-vocabulary allowance |
| Applied ML / fine-tuning | No compulsory Phase 1 addition | Course completion shows exposure; retained skill is unknown. The saved evidence does not justify declaring it impossible by 2028, but it also does not justify silently funding another career track |
| CDP office work | Keep the four-step office-AI protocol and the plan's office-proof path | Understand the changed lines before the PR; record portable proof after merge. No 46-68h parallel bridge, no invented topic percentages, and no public copy of internal repo material |
| New learning products | None | Use the existing resource map. Exact lesson links and prerequisites are checked when teaching starts |

## Hours and date consequences

| Item | Consequence |
| --- | --- |
| Approved v3.8 schedule | 834.5h |
| F1, F2, F4 and F5 | 0 new content hours; F2 still requires real resequencing |
| F3 | +4.5h, all in 1b; Go 68.5 to 69.5h, controllers 46 to 49.5h |
| Content subtotal before any added weeks or retention work | **839h** |
| Optional Helm / AI serving | Excluded from that subtotal |
| Warm-ups after the trial | Existing unresolved 28-45h estimate, not silently absorbed into the subtotal |

I would budget for **at least one additional week before Gate B**, rather than cut essential work or claim the four-skill floor for free. At the existing normal-week rates, an added 1b week also carries roughly **3.5h** of DSA, campaign and weekly proof/close work. A one-week illustration would therefore be **842.5h**, Gate B **13 February 2028** and Gate C **12 March 2028**, with Gate A unchanged. **These are conditional planning numbers, not generated or approved dates.** More time may be needed for measured warm-ups, new retention gaps or the protected lab blocks. Existing Gate B repair space is not a free fund for planned new scope.

The proposal does not assume 4h/day, silently raise the 12h normal week, or subtract learning because a course was watched. The final calendar must follow observed progress and the regenerated schedule.

## What is complete, and what approval would authorise later

Complete now: the source review, this proposed wording, the checker prototype and its patch, the regression results, and the identified schedule defects. The master, checker, coach verdicts and original harvest data remain unchanged.

If Om accepts these changes, the implementing coach copies `claude/plan-drafts/v3.8-build/` into its own folder, updates the generator's units, dependencies and atomic-session handling, rebuilds all affected sections, and publishes the **actual week-by-week delta**. That candidate must pass the old invariants and the new checks, with every negative mutation rejected. It must state any further retention/weekly overhead and exact displaced dates. Only after approval does the real v3.9 and its checker go into `plan/` and get uploaded to both projects. This proposal itself grants no learner PASS and approves no plan change.

## Sources

Snapshot root: [omieee/docs at 4954604](https://github.com/omieee/docs/tree/495460458dedfa413739ba50ae4d4c275289098f).

- [Master plan and checker](https://github.com/omieee/docs/tree/495460458dedfa413739ba50ae4d4c275289098f/plan), especially sections 0, 4-7, 9 and 14.
- [Claude outbox](https://github.com/omieee/docs/blob/495460458dedfa413739ba50ae4d4c275289098f/claude/outbox.md), 27 October 15:30/19:15/23:30/23:55, 28 October and 29 October 23:12/23:16; [ChatGPT outbox](https://github.com/omieee/docs/blob/495460458dedfa413739ba50ae4d4c275289098f/chatgpt/outbox.md), 27-30 October.
- [Shared log](https://github.com/omieee/docs/blob/495460458dedfa413739ba50ae4d4c275289098f/phase1-log.md), [Claude log](https://github.com/omieee/docs/blob/495460458dedfa413739ba50ae4d4c275289098f/claude-log-entries.md), [ChatGPT log](https://github.com/omieee/docs/blob/495460458dedfa413739ba50ae4d4c275289098f/chatgpt-log-entries.md). The Y7a prerequisite note is in Claude's 29 October 21:15 entry; the K1 resource correction is in both logs.
- [Claude harvest CSV](https://github.com/omieee/docs/blob/495460458dedfa413739ba50ae4d4c275289098f/claude/harvest/2026-10-27-claude.csv), [ChatGPT harvest CSV](https://github.com/omieee/docs/blob/495460458dedfa413739ba50ae4d4c275289098f/chatgpt/harvest/2026-10-27-chatgpt.csv), [classification and merge code](https://github.com/omieee/docs/tree/495460458dedfa413739ba50ae4d4c275289098f/claude/harvest/work).
- [Claude's CDP candidate proposal](https://github.com/omieee/docs/blob/495460458dedfa413739ba50ae4d4c275289098f/claude/plan-drafts/2026-10-27-v3.9-candidates-cdp-handoff.md); [Claude's AI review](https://github.com/omieee/docs/blob/495460458dedfa413739ba50ae4d4c275289098f/claude/plan-drafts/2026-10-27-ai-direction-review.md); [ChatGPT's AI review](https://github.com/omieee/docs/blob/495460458dedfa413739ba50ae4d4c275289098f/chatgpt/plan-drafts/2026-10-27-ai-career-dual-track-review.md).
- [Saved LinkedIn captures](https://github.com/omieee/docs/tree/495460458dedfa413739ba50ae4d4c275289098f/claude/harvest/linkedin); [office protocol](https://github.com/omieee/docs/blob/495460458dedfa413739ba50ae4d4c275289098f/claude/office-task-protocol.md).

Technical references were fetched on 30 October 2026. They verify the narrow behaviours cited in F3; they are not a fresh job-market sample or a recommendation to learn by reading reference documentation alone.
