# Market-demand evidence: Lease a Bike, Germany (Capture 1)

- Date classified: 2026-10-28
- Raw evidence: [Claude's verbatim capture](https://github.com/omieee/docs/blob/main/claude/harvest/linkedin/2026-10-28-raw.md), capture 1, received 10:33 IST
- Classification owner: ChatGPT, per HARVEST-SPEC-2026-10.md v2.1, §8.3 (all jobs outside India)
- Source: Om LinkedIn
- Exact LinkedIn URL recovered from public indexed result (not invented): https://de.linkedin.com/jobs/view/lead-ai-platform-engineer-m-f-d-at-lease-a-bike-deutschland-4483542694
- Source limitation: direct LinkedIn page not independently fetched due access restriction; employer, title, pay and description match indexed result. The raw user capture supports the detailed fields.
- Employer: Lease a Bike | Deutschland; legal organization in posting: Bike Mobility Services GmbH, a Pon.Bike subsidiary
- Role: Lead AI Platform Engineer (m/f/d); Cloppenburg, Lower Saxony, Germany
- Date: 2026-10-27 (capture dated Oct 28 says "1 day ago"; v2.1 §8.5 allows this day-level conversion)
- Pay: €95,000–€110,000 per year (the posting's stated range)
- Work model: full-time, 100% remote *within EU only*, regular team meetups
- English: fluency explicitly required; conversational German or Dutch is a nice-to-have
- Experience screen: at least 6 years platform, DevOps, cloud or MLOps, with production platform design and operation; production ML/LLM workload operation required
- Role duties: own AI platform architecture and roadmap, provisioning via Terraform/AWS, operate Bedrock gateway and SageMaker/GPU workloads, Snowflake-connected orchestration/CI, model tracing/evaluation/cost governance, security/access controls and mentorship
- Core counted sample: EXCLUDED under the narrow v2.1 §3 backend-heavy software/control-plane construction definition, because the JD describes building and operating an AI platform primarily using managed AWS/Snowflake services and Terraform, without specifying backend-language software development. **This is only a sampling classification, not a claim that the job lacks engineering or that its skills are irrelevant.** Keep as market-demand evidence; do not count toward lane a/b/c/d unless the sampling rules are explicitly amended.
- AI probe interpretation (not counted in main sample): **platform**. Model-serving/GPU workload scaling and managed inference access are core duties; this does *not* prove a Kubernetes controller or self-hosted model runtime requirement. This is a candidate for the separate AI-probe analysis, not evidence of broad market prevalence by itself.
- Other fields: Terraform or AWS CDK required (alternatives); AWS required; Helm not named; Kubernetes and self-hosted serving preferred; no Kubernetes-controller requirement; interview format two steps (introduction and technical conversation)
- Candidate geography: role held anywhere in EU. From the page, ability to apply while based in India and relocation support are **unknown**; worldwide remote is NOT offered. Do not infer EU work authorization/visa conditions not stated.
- Purpose and gap: **This harvest measures what industry asks, NOT jobs to apply for now.** The explicit production ML/LLM experience screen is an important market learning-gap signal, regardless of Om's current competence. Do not drop it because he may lack that experience today; any eventual skill-plan change requires separate change control.
- Duplicate check: employer was on neither coach's 100-company list and was not in either accepted JD CSV when checked.
- Recording: this classification note preserves all demand evidence. The core sampling decision is Excluded; LinkedIn sheet records accepted core rows only under §5. A workbook addition must be verified rather than claimed. No immediate application recommendation, accepted core count change, or plan decision.

## Skill-demand extraction (independent of Om's present eligibility)

- **Required hands-on production history:** 6+ years in platform/cloud/DevOps/MLOps; platform design plus operations; experience running ML and LLM workloads in production.
- **Required products/tooling:** AWS (including managed AI access such as Bedrock), Terraform or AWS CDK, Docker, CI/CD (GitLab CI example), workflow orchestration (Airflow example), Snowflake or comparable cloud data platform, tracing/evaluation and model cost controls, security and governance.
- **Expected ownership:** architecture, roadmap, build-vs-buy, self-service components, quotas, per-team cost, technical leadership, mentoring and communication with non-technical teams.
- **Preferred only:** MCP infrastructure for agents; Kubernetes plus self-hosted vLLM or similar; EU AI Act/GDPR familiarity; conversational German/Dutch.
- **Interpretation:** one observed posting establishes that this employer requires these things. It does not establish market-wide frequency, and does not trigger a change to v3.8 by itself.
