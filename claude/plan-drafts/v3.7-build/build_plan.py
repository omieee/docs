import re, sys, os
D = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(D, "base", "Phase1_Master_Plan_v3.5.md"), encoding="utf-8").read()  # v3.5 Oct 21 copy, sha256 5e9a9bf242f47fc1


def rep(text, old, new, count=1):
    n = text.count(old)
    if n != count:
        raise SystemExit(f"expected {count} of: {old[:90]!r}, found {n}")
    return text.replace(old, new)


# split into header+section 0, sections 1..14
parts = re.split(r"(?m)^(?=## \d+\. )", src)
head = parts[0]
secs = {int(re.match(r"## (\d+)\.", p).group(1)): p for p in parts[1:]}

# ---------- title and section 0 ----------
s0 = head + secs[0] if 0 in secs else head
s0 = rep(s0, "# Phase 1 Master Plan v3.5: Portable Skills You Can Prove", "# Phase 1 Master Plan v3.6: Portable Skills You Can Prove")
s0 = rep(s0, "updated 2026-10-21 (machine coding practice trial, machine coding scoring when concurrency is not asked, two standing coach rules) · **Replaces:** v3.4, v3.3, v3.2, v3.1,",
         "updated 2026-10-21 (machine coding practice trial, machine coding scoring when concurrency is not asked, two standing coach rules) · **v3.6 amendment drafted:** 2026-10-23 (hardening from both coaches' Oct 23 audits and Om's Oct 23 instructions: no hour ceiling, the continuity rule, prerequisites at first use, earlier integration, honest hours with the campaign inside the map, Kubernetes controllers in Go, AWS and Terraform, eight reps and weekly machine coding practice, one coaching owner), effective when Om uploads it · **Replaces:** v3.5, v3.4, v3.3, v3.2, v3.1,")
s0 = rep(s0, "3. **Make the model click.** Use one guided example, trace or visual when the idea is new or shaky. This is teaching, not proof.",
         "3. **Make the model click.** Use one guided example, trace or visual when the idea is new or shaky. This is teaching, not proof. Fade this step for material Om has already shown in a recent check; never skip the ask-first question or the teaching of a new prerequisite (v3.6).")
s0 = rep(s0, "8. Never change this file silently. Changes go through section 9 change control.",
         "8. Never change this file silently. Changes go through section 9 change control.\n9. Check the continuity record in `phase1-log.md` (section 6.12) before choosing a block: a watched track at its gap limit gets its retrieval rep first (v3.6).")
s0 = rep(s0, "**Two coaches, one repository.** Claude and ChatGPT are equal peers; Om decides. Their only channel is `omieee/docs` on GitHub:",
         "**Two coaches, one repository.** Claude and ChatGPT are equal peers; Om decides. **Coaching owner (Om, Oct 23 2026):** ChatGPT owns teaching, proofs, verdicts and the Sunday close. Claude works only on request: plan audits, repo proofs Om asks for, and second opinions. Om can move ownership at any time; every rule in this section binds whichever coach runs a unit, and settled verdicts stand. The coaches' only channel is `omieee/docs` on GitHub:")
s0 = rep(s0, "The Sunday close is split: Claude supplies git, CI and tracker facts, ChatGPT runs a short spoken check, and they make one combined close.",
         "The Sunday close is run by the coaching owner (ChatGPT from Oct 23), who reads git, CI and the tracker; the other coach adds facts only when Om asks.")

s0 = rep(s0, "Every resource here was checked on 2026-09-25.", "Every resource here was checked on 2026-09-25 (v3.6 additions on 2026-10-23).")
s0 = rep(s0, "- Language (protects understanding)", "- Language (protects understanding)") if "- Language (protects understanding)" in s0 else s0

# ---------- section 1 ----------
s1 = secs[1]
s1 = rep(s1, "- **Beyond this file:** a senior or staff backend-heavy platform role abroad by March 2028, later AI infrastructure. Relocation is out of scope until the Phase 2 review.",
         "- **Beyond this file:** a senior or staff backend-heavy platform role abroad, later AI infrastructure; the target date is re-decided at Gate C, which v3.6 forecasts for Feb 20 2028. Relocation is out of scope until the Phase 2 review.")
s1 = rep(s1, "| 4 | Fixed end date Jan 31 2027 | Gates set the end. Forecast (v3.4): Gate A Mar 21 2027, Gate B Sep 5 2027, Gate C Sep 26 2027, at 12 hrs/week from the W2 capacity check, re-forecast monthly from actual hours |",
         "| 4 | Fixed end date Jan 31 2027 | Gates set the end. Forecast (v3.6): Gate A May 2 2027, Gate B Jan 23 2028, Gate C Feb 20 2028, at 12 hrs/week from the W2 capacity check, re-forecast monthly from actual hours |")
s1 = rep(s1, "572 with two unseen DSA sets (v3.5). Om authorized up to 575 |",
         "572 with two unseen DSA sets (v3.5). 814.25 in v3.6, with no ceiling (Om, Oct 23; section 5 ledger) |")
s1 = rep(s1, "**Unchanged and still frozen**",
         """**Decisions adopted in v3.6 (Om's Oct 23 instructions and both coaches' Oct 23 audits)**

| # | Was (v3.5) | Now (v3.6) | Evidence |
| --- | --- | --- | --- |
| 9 | 575-hour ceiling, 3 hours left | No ceiling: scope sets the hours, the dates follow; 814.25 hours, including 69.5 of campaign inside the map | Om, Oct 23: "don't under-time anything"; both audits found the campaign unfunded |
| 10 | Tracks finish their units, then go idle for up to 20 weeks | The continuity rule: a watched track is idle at most 1 week while learning and 3 weeks after; retrieval reps fill any hole; the checker enforces it | Om, Oct 23 (Go untouched for two weeks); counted gaps of 2-20 weeks in v3.5's map; skill-decay and spacing research (section 6.12) |
| 11 | Controllers and CRDs out of Phase 1; a 6h lab after Gate B at most | Kubernetes controllers in Go: two operators read end to end and a gate controller built in PRCP (46h, section 6.10) | Om's Oct 23 addition; controllers required in the most control-plane-like JDs |
| 12 | Cloud and Terraform trigger-only | AWS and Terraform core (33h, section 6.11), one provider, one named output | About 45% of sampled Kubernetes-platform JDs name public cloud, mostly AWS, and about 35% Terraform; Om left the call to Claude |
| 13 | Six reps; machine coding practice only from spare hours | Eight reps and a core practice session most weeks | MC1 2/10; Om's Oct 20 idea; machine coding is on the never-cut list |
| 14 | Topics placed after the work that first used them | Prerequisites at first use: `yield` before `yield` fixtures, classes and dataclasses before MC2, a code walk before each module changes | ChatGPT F1 and Claude F2, Oct 23 |
| 15 | A1 in W25, PRCP on kind in W41, first mock in W39 | A1 right after G7, PRCP on kind at 1b's start, Mock 1 before Gate A | Both audits, Oct 23 |
| 16 | Two coaches with a split Sunday close | ChatGPT owns coaching; Claude on request | Om, Oct 23 (`chatgpt/state.md`) |

**Unchanged and still frozen**""")
s1 = rep(s1, "- Terraform and public-cloud depth stay conditional on the November JD harvest. Redis and Kafka hands-on stay out.",
         "- AWS with Terraform is core from v3.6 (section 6.11), one provider only; GCP stays vocabulary and Azure is out. Redis and Kafka hands-on stay out.\n- Kubernetes controllers: one built in PRCP and two open-source operators read end to end (section 6.10). This is personal-project and code-reading evidence, never claimed as production operator experience.")

# ---------- section 2 ----------
s2 = secs[2]
s2 = rep(s2, "## 2. Verified baseline (2026-09-25)\n\nEngineering judgement is at level; tool fluency in Go, Kubernetes and SQL is not. Plan the tracks separately and never slow PRCP, Go or design because DSA is behind.",
         "## 2. Verified baseline (2026-09-25, updated 2026-10-23)\n\nEarlier product building and client and delivery leadership are strengths. Current fluency in each language and tool, independent implementation and timed problem solving are measured from recent evidence, topic by topic. Credit what is shown; teach only the missing piece. Plan the tracks separately and never slow PRCP, Go or design because DSA is behind (v3.6 wording, from both coaches' Oct 23 audits).")
s2 = rep(s2, "| Execution | Restarted after long gaps |",
         "| History (Om, Oct 23) | Built before, then years with little coding | Coded Duplive in college and built GetMyUni single-handed (acquired by CollegeDekho, Feb 2022). Technical Lead and Architect roles from 2016 to 2020 were techno-managerial (client work, making sure others delivered), followed by more years with little personal coding. Om's reading, which the record supports: rust, not a lack of ability |\n| Recent checks (Oct 2026) | Passes when taught at his level | G1 5/6; P1 context managers 4/6 after one retry; pytest basics 6/6; L1 part check 5/6 after one retry; NEW 155 and 739 PASS 4/6 after repairs; NEW 704 interview PARTIAL 5/8; MC1 FAIL 2/10. The misses are explaining why and building from a blank page against a clock |\n| Execution | Restarted after long gaps |")
s2 = rep(s2, "| System design, machine coding | Not started | Machine coding: one parking-lot attempt on Sep 28 (109 min, AI-written tests and one AI fix), logged as practice, not a rep. System design: no study, no mocks |",
         "| System design, machine coding | Started in October | Machine coding: one parking-lot attempt on Sep 28 (109 min, AI-written tests and one AI fix), logged as practice, not a rep; MC0 method taught Oct 19; MC1 Snake and Ladder FAIL 2/10 on Oct 20 (does not run end to end, no tests, the minute-60 change not started). System design: no study, no mocks |")
s2 = rep(s2, "| Stories | 2-3 honest | IBM registry cost reduction (reconcile the savings figures first), IKS upgrade programme, Circuit Breaker plus deployment gate. The rest must be earned at work |",
         "| Stories | 2-3 honest | IBM registry cost reduction (reconcile the savings figures first), IKS upgrade programme, Circuit Breaker (Om, Oct 21: there was no deployment-gate or ArgoCD RBAC work). Two older dated stories can be written now (GetMyUni, one tech-lead decision). The rest must be earned at work |")

# ---------- section 3 ----------
s3 = secs[3]
s3 = rep(s3, "**What this means for preparation**",
         """**Evidence added Oct 23 2026 (v3.6)**

- **Round mix in 104 India senior loops** (Claude, Oct 14, one link per row): DSA in 90 of 98 loops with a clear answer, HLD in 81% of complete loops, hiring manager 65%, project deep dive 55%, LLD 41%, machine coding 23%, AI concepts 8%, AI-assisted coding 3%. The sample leans on LeetCode Discuss.
- **AI in interviews:** Razorpay runs AI-assisted and agentic coding rounds (Glassdoor, 2026); Canva requires AI tools in its interviews ([Canva Engineering, Jun 2025](https://www.canva.dev/blog/engineering/yes-you-can-use-ai-in-our-interviews/)); Meta has an AI-enabled round. Still, 62% of 400 engineering leaders in the US, India and China say their organisations ban AI in technical interviews ([Karat, Jan 2026](https://karat.com/engineering-interview-trends-2026)).
- **Controllers:** required in the platform JDs closest to "control plane" (Red Hat OpenShift, Intuit's Kubernetes runtime platform, ThoughtSpot Cloud Platforms) and a plus elsewhere ([Nutanix NKP](https://careers.nutanix.com/en/jobs/32362/staff-engineer-nutanix-kubernetes-platform-nkp/)). Not every senior backend role needs them (ChatGPT's 13 employer-page JDs).
- **Cloud and Terraform:** public cloud in about 45% and Terraform in about 35% of 20 Bengaluru Kubernetes-platform JDs (Claude's Oct 23 sample, searched on Kubernetes, so a direction only).
- **Titles:** at 10-15 years, many Bengaluru platform roles are titled Staff, and GCCs use "Lead Software Engineer" for hands-on roles that reward tech-lead years. Being offered a level below the loop's title is common.
- **AI skills at GCCs:** about two-thirds of new GCC roles in 2026 ask for AI, data science or automation skills (64%, Business Today figures, [Outsource Accelerator, Jul 2026](https://news.outsourceaccelerator.com/india-gcc-hiring-peak/)). The definition is broad; it does not mean AI infrastructure.
- **Keyword traps:** a JD that lists Python, Go and Kubernetes can still be Java-first, an authentication specialist role, data-pipeline heavy or partly frontend (ChatGPT's J6-J12). The harvest classifies duties before counting words (section 8).

**What this means for preparation**""")
s3 = rep(s3, "5. **AI shows up two ways:** an AI-assisted build round (Razorpay) and AI concept questions (ServiceNow, Intuit). The first is trained in rep 5. The second is a watch item for the JD harvest: concepts only, never features in PRCP.",
         "5. **AI shows up two ways:** an AI-assisted build round (Razorpay) and AI concept questions (ServiceNow, Intuit). The first is trained in AI1 and rep 6, plus one AI-assisted practice in the week a recruiter confirms such a round. The second is a trigger-only extra: concepts only, never features in PRCP.")
s3 = rep(s3, "6. **Phase 2 formats are not frozen here.** FAANG-tier AI-era rounds are re-researched when Phase 2 starts.",
         "6. **Phase 2 formats are not frozen here.** FAANG-tier AI-era rounds are re-researched when Phase 2 starts.\n7. **The Kubernetes-platform lane needs controllers and one cloud** (v3.6). Om's strongest production record is Kubernetes platform work, so sections 6.10 and 6.11 make that lane reachable without dropping the Python-led backend lane.")

# ---------- section 7 ----------
s7 = secs[7]
s7 = rep(s7, "NEW DSA problems get this too: the mechanism, a trace, one transfer question, and the pattern-signal question: which words in the problem point to this pattern (v3.5).",
         "NEW DSA problems get this too: the mechanism, a trace, one transfer question, and the pattern-signal question: which words in the problem point to this pattern (v3.5), followed by the structural reason the pattern fits (v3.6).")
s7 = rep(s7, "- **Machine coding:** six criteria, 0-2 each:",
         "- **Operators (v3.6):** envtest green on a fresh clone; explain why the reconcile is idempotent, when it requeues and what the finalizer protects; UNKNOWN never promotes.\n- **Cloud (v3.6):** `plan` read before every `apply`; destroy confirmed in the AWS console and the cost log; no long-lived keys in the repo or CI.\n- **Machine coding:** six criteria, 0-2 each:")
s7 = rep(s7, "No AI for first attempts, drills, DSA, machine coding reps 1-4 and 6, or any cold check.",
         "No AI for first attempts, drills, DSA, machine coding reps 1-5, 7 and 8, practice sessions, retrieval reps, or any cold check.")
s7 = rep(s7, "Rep 5 tests AI-assisted work on purpose.", "Rep 6 and AI1 test AI-assisted work on purpose.")
s7 = rep(s7, "Each skill is tested at four points only: baseline, milestone, gate, and the day 7 and day 28 retention checks after a gate. DSA alone keeps continuous spaced review. There are no extra monthly re-tests.",
         "Each skill is tested at four points only: baseline, milestone, gate, and the day 7 and day 28 retention checks after a gate; checks due after Gate C carry into Phase 2. DSA alone keeps continuous spaced review. Retrieval reps (section 6.12) are practice, not tests: held or slipped, no score. There are no extra monthly re-tests.")
s7 = rep(s7, "Coach errors this week (both coaches): count, minutes lost, rules broken (section 0 safeguards)",
         "Coach errors this week (both coaches): count, minutes lost, rules broken (section 0 safeguards)\nHours by clock: Om's active / coach work / elapsed waits (section 5)\nContinuity record: last real use of Go, Kubernetes, LLD, HLD, operators, cloud; any track at its limit")
s7 = rep(s7, "- **D. Python (baseline in W0, pass at Gate B):**",
         "- **E. Kubernetes controllers (Gate B, v3.6):** CRD anatomy (group, version, kind, schema, status subresource), desired vs observed state, level-triggered vs edge-triggered, informer, lister and cache, work queue and rate-limited requeue, idempotent reconcile, `observedGeneration` and conditions, owner references and garbage collection, finalizers and stuck deletion, leader election, controller RBAC, admission webhooks in concept, controller-runtime vs client-go, envtest vs a real cluster, how Argo Rollouts' AnalysisRun maps to PRCP's PASS, WARN, BLOCK and UNKNOWN.\n- **F. Cloud and Terraform (Gate B, v3.6):** IAM user vs role vs policy, least privilege, public vs private subnets, route tables, NAT and its cost, security groups vs NACLs, EKS control plane vs node groups, how a pod gets AWS permissions, RDS vs Postgres in a pod, plan, apply and state, remote state and locking, drift, modules and inputs, `for_each` vs `count`, import, why OIDC instead of static keys in CI, cost control and teardown.\n- **D. Python (baseline in W0, pass at Gate B):**")

# ---------- section 8 ----------
s8 = secs[8]
s8 = rep(s8, '- **Headline formula:** role, years, 3-5 proven skills, one differentiator. After Gate A: "Senior Backend Infrastructure Engineer · 12 yrs · Python, Go, Kubernetes, PostgreSQL · distributed control planes".',
         '- **Headline formula:** role, years, 3-5 proven skills, one differentiator. After Gate A: "Senior Backend Infrastructure Engineer · 12 yrs · Python, Go, Kubernetes, PostgreSQL · release-gate control plane". After OP7: add "Kubernetes controllers in Go". "Control plane" describes PRCP exactly; explain its real parts and failure behaviour, and never let the phrase suggest operator work you have not done.')
s8 = rep(s8, "- **Keyword rule:** a skill appears on the resume, Naukri or LinkedIn only with a closed unit or real production evidence. Kubernetes can be listed now as production IBM Cloud work; Go waits for Gate A.",
         "- **Keyword rule:** a skill appears on the resume, Naukri or LinkedIn only with a closed unit or real production evidence. Kubernetes can be listed now as production IBM Cloud work; Go waits for Gate A; controllers wait for OP7 and AWS and Terraform for CL3, both as personal-project work.")
s8 = rep(s8, '1. Go and control plane: `("control plane" OR "backend infrastructure" OR "distributed systems" OR "platform engineering") AND ("Go" OR "Golang") AND ("Senior" OR "Staff" OR "MTS") AND ("Bangalore" OR "Bengaluru" OR "Hyderabad" OR "Pune")`',
         '1. Go and control plane: `("control plane" OR "backend infrastructure" OR "distributed systems" OR "platform engineering") AND ("Go" OR "Golang") AND ("Senior" OR "Staff" OR "Lead" OR "MTS") AND ("Bangalore" OR "Bengaluru" OR "Hyderabad" OR "Pune")`')
s8 = rep(s8, '2. Python and backend infrastructure: `("backend infrastructure" OR "platform backend" OR "distributed systems") AND "Python" AND ("Senior" OR "MTS") AND ("Bangalore" OR "Bengaluru" OR "Hyderabad" OR "Pune")`',
         '2. Python and backend infrastructure: `("backend infrastructure" OR "platform backend" OR "distributed systems") AND "Python" AND ("Senior" OR "Lead" OR "MTS") AND ("Bangalore" OR "Bengaluru" OR "Hyderabad" OR "Pune")`')
s8 = rep(s8, '3. Language-flexible systems: `("distributed systems" OR "control plane" OR "systems software") AND "Kubernetes" AND ("Go" OR "Python") AND ("Senior" OR "Staff" OR "MTS")`',
         '3. Language-flexible systems: `("distributed systems" OR "control plane" OR "systems software") AND "Kubernetes" AND ("Go" OR "Python") AND ("Senior" OR "Staff" OR "Lead" OR "MTS")`\n4. Controllers (v3.6): `("operator" OR "controller" OR "CRD" OR "controller-runtime" OR "client-go") AND "Kubernetes" AND "Go" AND ("Senior" OR "Staff" OR "Lead")`\n\nTitles are search terms, not filters: a "Platform Engineer" or "Lead Engineer" role whose duties are building and owning software fits the role identity; a Staff-titled role whose duties read Senior is fair to apply to. Filter by the duties.')
s8 = rep(s8, "**JD harvest in November (W6):** 20 or more live postings you would accept. Tabulate every named technology by frequency. This triggers or kills the conditional queue. Refresh it in W34 for resume v2.",
         """**JD harvest in November (W6-W7, v3.6 method):** 20 or more live postings Om would accept, with Om's 5 most wanted marked. The coach records, for each posting: employer, requisition and canonical link, location and retrieval date; the actual work and how much of it is building software; seniority and the relevant experience asked for; languages as required, alternative or optional ("Java required, Go helpful" is not a Go role); each named skill as required or preferred, and as a capability or a named product; the lane, (a) Python-led backend infrastructure, (b) Go and Kubernetes platform, (c) controllers and operators, or excluded with the reason; any production-history requirement and Om's honest evidence for it; pay and work model if stated, unknown otherwise. Reposts and mirrors are counted once. Counts are per lane, and the extras triggers in section 5 read "2 of Om's top 5, or 40% of that lane's accepted roles". Om then picks the primary lane. Refresh in W58 for resume v2.""")
s8 = rep(s8, "- Ask at the start of any coding round whether AI is allowed.",
         "- Ask at the start of any coding round whether AI is allowed. When a recruiter confirms an AI-assisted round, do one 60-minute AI-assisted practice that week from the campaign line, using rep 6's log method (v3.6).")

s8 = rep(s8, "**Referral map (October, campaign reserve):**", "**Referral map (October, campaign line):**")

# ---------- section 9 ----------
s9 = secs[9]
s9 = rep(s9, "4. **Setup:** each Sunday, build a Watch Later playlist from section 14 and play only from it.",
         "4. **Optional cards (v3.6):** short questions from closed units' interviews, read on the phone. Never required, never counted (section 6.12).\n5. **Setup:** each Sunday, build a Watch Later playlist from section 14 and play only from it.")
s9 = rep(s9, "- **Two-day gap found:** 25 minutes on the smallest open item, the same day. No catch-up sprint.",
         "- **Two-day gap found:** 25 minutes on the smallest open item, the same day. No catch-up sprint.\n- **Continuity (v3.6):** a watched track at its gap limit gets its retrieval rep in the next normal block (section 6.12).")
s9 = rep(s9, "- **Verification invariant, checked by script on every revision:** every week's item hours equal its label, the labels fit the weekly caps, and unit totals equal their track budgets.",
         "- **Verification invariant, checked by script on every revision:** every week's item hours equal its label, the labels fit the weekly caps, unit totals equal their track budgets, and no watched track breaks the continuity rule (v3.6).")

s9 = rep(s9, "- **One-in, one-out:** any addition names what it removes.", "- **One-in, one-out:** any addition names what it removes, or the date it moves (v3.6: there is no hour ceiling, so the trade is scope or date, said out loud).")

# ---------- section 11 ----------
s11 = secs[11]
s11 = rep(s11, "Phase 2 starts after Gate C, now forecast Sep 26 2027 (v3.4).", "Phase 2 starts after Gate C, now forecast Feb 20 2028 (v3.6).")
s11 = rep(s11, "and the FAANG loop window (planned as November 2027 to February 2028) are re-decided at Gate C on the actual dates.",
         "and the FAANG loop window (planned in v3.5 as November 2027 to February 2028, which v3.6 makes impossible) are re-decided at Gate C on the actual dates.")
s11 = rep(s11, "- **Branch A, new job landed:** with a 3-month notice period, an offer around Gate B (now about September 2027) means joining around December 2027.",
         "- **Branch A, new job landed:** with a 3-month notice period, an offer around Gate B (now about January 2028) means joining around May 2028. An offer after Gate A can come earlier.")
s11 = rep(s11, "| Optional, cut first | A controller-runtime `GateDecision` CRD whose reconciler calls PRCP; one merged Go OSS PR | Never a gate |",
         "| Optional, cut first | One merged Go OSS PR, ideally to one of the two operators read in OP2 and OP3 (the PRCP gate controller itself moved into Phase 1 in v3.6) | Never a gate |")
s11 = rep(s11, "- **No India offer by about three months after Gate A (now late June 2027):** do not extend blindly.",
         "- **No India offer by about three months after Gate A (now early August 2027):** do not extend blindly.")
s11 = rep(s11, "**Out of scope here:** relocation and visas. If the March 2028 goal still means abroad, that track starts in parallel during 2027; raise it at the 2a review.",
         "**Out of scope here:** relocation and visas. With Gate C in Feb 2028, a March 2028 move abroad is no longer realistic; Om re-decides that goal at Gate C.")

# ---------- section 12 ----------
s12 = secs[12]
s12 = rep(s12, "| `Phase1_Master_Plan_v3.5.md`, Oct 20 copy (sha256 `3aa6efedf5d2ae9e`) | Replace in both projects with the Oct 21 copy; check its sha256 against `plan/README.md` | The Oct 21 copy adds Om's Oct 20-21 decisions (change 75) |",
         "| `Phase1_Master_Plan_v3.5.md` (Oct 21 copy, sha256 `5e9a9bf242f47fc1`) | Remove from both projects once v3.6 is uploaded; it stays in `omieee/docs` git history. The Claude project still held v3.4 on Oct 23 | Superseded by v3.6 |\n| `check_plan.py` | Replace with the v3.6 checker (it reads split and two-letter units, sections 6.10-6.12, the campaign line and the continuity rule) | The v3.5 checker cannot read v3.6 |")
s12 = rep(s12, '| Project instructions (Claude project settings) | The line "Source of truth: Phase1_Master_Plan_v3.3.md" must name the current file: "Source of truth: Phase1_Master_Plan_v3.5.md". Om edits it; coaches cannot | The old name points at a retired file |',
         '| Project instructions (both projects) | The line "Source of truth: Phase1_Master_Plan_v3.3.md" must name the current file: "Source of truth: Phase1_Master_Plan_v3.6.md". The "two coaches, equal voice" lines should match section 0\'s coaching owner. Om edits them; coaches cannot | The old names point at retired files |')

# ---------- section 13 ----------
s13 = secs[13]
s13 = rep(s13, "## 13. Change log: v3 to v3.5", "## 13. Change log: v3 to v3.6")
s13 = rep(s13, "**Checked and not added:**", open(os.path.join(D, "change76.md")).read().rstrip() + "\n\n**Checked and not added:**")

# ---------- v3.7 layer ----------
exec(open(os.path.join(D, "v37_edits.py"), encoding="utf-8").read())

# ---------- assemble ----------
sec46 = open(os.path.join(D, "sec04_05.md")).read().rstrip() + "\n\n---\n\n"
sec6 = open(os.path.join(D, "sec06.md")).read().rstrip() + "\n\n---\n"
sec14 = open(os.path.join(D, "sec14_head.md")).read().rstrip() + "\n\n" + open(os.path.join(D, "sec14.md")).read().rstrip() + "\n\n" + open(os.path.join(D, "sec14_tail.md")).read().rstrip() + "\n"
out = s0 + s1 + s2 + s3 + sec46 + sec6 + s7 + s8 + s9 + secs[10] + s11 + s12 + s13 + sec14
open(sys.argv[1], "w", encoding="utf-8").write(out)
print("written", len(out.splitlines()), "lines")
