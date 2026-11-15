# Research brief: evidence base for a learning and career plan (v3.9)

## 0. Read this first

You are doing the evidence research for version 3.9 of a personal learning and career plan. Two other AI reviewers (Claude, who drives the plan, and ChatGPT) will check your claims by opening your links. Any claim they cannot verify will be thrown away. So accuracy and traceable sources matter far more than polish or length.

- Do not ask me clarifying questions. Where something is unclear, write your assumption in one line and continue.
- Search the web extensively and read the actual pages, not only search snippets.
- Long output is fine. Completeness and accuracy beat brevity.
- Do not rewrite the plan. Your job is evidence and evidence-based recommendations.

## 1. The goal of this research

Build the evidence base so that every decision in v3.9 is backed by solid, current, verifiable data, in the right order, with nothing important missing. The learner's goals:

- **Near term (Phase 1):** hands-on Senior backend infrastructure, platform or distributed control-plane offers (Python and Go) at strong product companies or global capability centres in India, and in parallel in Europe (Germany, Netherlands, Ireland) and the Gulf (UAE, Saudi Arabia).
- **Long term:** a role at Google, Anthropic, OpenAI or a company of that tier, by 2028, else 2029, else 2030. No fixed title. He wants to be genuinely good at building systems, not only at passing interviews.
- **AI shift:** by 2027-2030 these roles will need knowledge that does not matter much today. Find out what that knowledge is, with evidence, and where it fits.

## 2. The learner (facts; use them)

- 12 years in software. At IBM Cloud since Dec 2020 (title Software Engineer). Leads a 3-person Release and Resiliency team for IBM Cloud Databases (classic offering: managed PostgreSQL, MySQL, Redis, RabbitMQ, MongoDB, Elasticsearch for clients such as banks and airlines).
- Production record: sole owner of Kubernetes version upgrades across 200-300 IBM Kubernetes Service clusters (about 19,000 worker nodes), five version cycles done, with his own automation (batch scheduling, a load-aware scheduler for dev clusters, speed control for prod). Cut container registry storage by 60% (about 250 TB, about USD 17K a month) with a 90-day retention policy. Built a cluster-level circuit breaker (a Kubernetes CRD plus a Jenkins gate) that other teams use to freeze a cluster.
- Earlier: built two products almost single-handedly about 12 years ago (PHP), then tech lead and architect roles that were mostly techno-managerial. Little hands-on coding at IBM for 2-3 years. He is now rebuilding hands-on depth.
- Current level: Python intermediate and growing; Go beginner; Kubernetes strong as a platform operator but weak on raw `kubectl` and internals (cold self-audit 4 of 15 in Sept 2026); SQL rusty; system design not yet studied formally; DSA early beginner: 26 problems solved, families done so far: arrays and hashing, two pointers, sliding window, linked lists, stack, binary search (in progress).
- **How he learns (observed over two months):** a concrete counterexample that breaks his wrong idea teaches him fastest. A real person live-coding in Python or Go, or interactive learn-and-code lessons (Boot.dev), work far better for him than docs or slides. He forgets quickly what he does not use (Go syntax faded after 11 idle days). He learns by trial and error ("as a lead, no one helps you"). When an idea is completely new to him (pytest was), he needs to start from what the thing is, one idea at a time.
- **His own DSA diagnosis:** "I can't tell the pattern." His example: Koko Eating Bananas can be retold a thousand ways and he should still see "this is binary search".
- **Time:** about 2-2.5 focused desk hours a day (about 12 a week); a reading-only slot of 1-2 hours most evenings (phone or Kindle, no audio, low light); some audio-only time on walks or commutes; about 30 minutes late at night. He will add hours if the evidence says more effort is needed. Money for courses, books and tools is not a constraint.
- Based in Bangalore, India.
- Already paid for: NeetCode (paid account), Boot.dev, KodeKloud (including the Mumshad Mannambeth CKA course), Udemy. Rate these first; recommend a new paid resource only when it is clearly better for a specific need, and say why.
- **Run mode (Nov 15, after two failed Fable runs):** Claude runs one part per chat (R4, then R2, R1, R5, R3), reads only sections 0-3, 5-7 and that part, opens every link it cites, and commits findings to `claude/research/v3.9/<part>.md` after each sub-question so a stopped run loses nothing.

## 3. The current plan (v3.8), in brief

- 75 weeks, Oct 2026 to Mar 2028, about 834 scheduled hours at 12 hours a week. Gates: A (foundations) May 2027, B (build and design) Feb 2028, C (offers) Mar 2028. These dates are being re-forecast because measured pace is lower: focused hours were about 18, 7.5 and 5.3 in three recent weeks; by Nov 11, 14 of 27 planned learning items were proved.
- **Tracks:** Python core; Postgres (psycopg 3, then SQLAlchemy 2.0 and Alembic) and SQL; Go (Learning Go 2nd edition order, with Boot.dev and Learn Go with Tests), used to build PRCP's probe agent; Kubernetes on a local kind cluster (KodeKloud CKA course order, exam-only parts skipped), later a Kubebuilder controller and reading two real operators end to end; Docker, CI that gates PRCP's own release, metrics, SLOs and a load test, AWS and Terraform, a game day with a postmortem; low-level design and machine-coding reps; high-level design (framework, building blocks, distributed systems, seven practice designs, mocks); DSA; resume, stories and job-description harvests.
- **DSA method today:** a NeetCode lesson before each new technique; Easy then Medium within a family; spaced re-solves on days 1, 3, 7, 14, 28 and 90; one problem per session, about 45-60 minutes a day; every new problem is followed by the question "which words in the problem point to this pattern, and why does the pattern fit"; two sets of never-seen problems (weeks 30 and 70) and blind mixed sets only in weeks 57-69.
- **PRCP, the flagship project** (public code: https://github.com/omieee/platform-reliability-control-plane; if you cannot open it, use this description): a release and environment reliability gate, not an uptime monitor. It runs configurable probes against a service in an environment, classifies failures, keeps an audit record, exposes Prometheus metrics, and returns a promotion decision of PASS, WARN, BLOCK or UNKNOWN. The decision function `decide(probe_results, config)` is pure and deterministic. It fails closed (no promotion without positive evidence). FastAPI, Python, Postgres; a Go probe agent; later a Kubernetes controller whose `ReleaseGate` custom resource asks PRCP's API for the decision. Phase 1 scope is one service in one environment. Parked for later: coordinated multi-service promotion; an LLM that adds an advisory note to the audit record without changing the decision.
- **Settled (do not reopen without new, strong evidence):** DSA stays in the plan (an earlier study of 104 Indian senior-level interview loops found a DSA round in 90 of the 98 with a clear answer); research the format and share of DSA at the target tier, not whether to keep it. PRCP's decision function stays pure and deterministic. Python leads the backend; Go builds the agent and the controller.

## 4. Research questions

Cover all five parts. If you run short, finish them in this priority order and mark what is left as INCOMPLETE: R4, R2, R1, R5, R3.

### R1. Target employers and the AI shift, 2027-2030

1. For Google, Anthropic and OpenAI, plus 4-6 companies of similar standing that hire infrastructure engineers in India or Europe (your choice, say why), what infrastructure, platform, reliability and AI-infrastructure roles exist now? Sample at least 30 current postings across them (give each URL and the date you saw it). Count how often each requirement appears: languages, distributed systems, Kubernetes, storage and databases, networking, accelerators and GPUs, inference serving, scheduling, observability, security. Note hard requirements (years, degree, location) and whether roles are open to candidates based in India, as stated in the posting.
2. What level would a 12-year engineer with this profile realistically be considered for at each company, and what evidence (scope, ownership, design depth, code) moves a candidate up a level? Use official level descriptions where published; self-reported sources only as support.
3. What do the interview loops for these roles look like now (rounds, coding style, system design, domain depth, behavioural)? Use official interview pages first, then dated candidate reports from 2025-2026. What is the DSA share and difficulty at this tier? Which companies now allow or test AI-assisted coding in interviews, and how?
4. Follow the money: what do 2025-2026 earnings calls, capital-expenditure figures, compute and data-centre deals (including India), and corporate backing of open-source projects say about where infrastructure hiring is going? Separate durable skills from hype.
5. Which AI-infrastructure knowledge will infrastructure engineers need by 2027-2030 (for example inference serving, GPU scheduling on Kubernetes, Dynamic Resource Allocation, the Gateway API inference extension, vLLM, llm-d, KServe, Kueue, Ray, evaluation pipelines, agent infrastructure)? Which of these have real backing and adoption, with evidence?
6. How do engineers from non-top-tier backgrounds with 10+ years actually get into these companies (referrals, open-source work, a specialist niche, an intermediate employer)? Evidence only, not anecdotes alone.

**Deliver:** (a) a capability map table: capability | why it matters (evidence IDs) | needed by (Phase 1 Senior offers / top tier 2028 / 2029-2030) | how to prove it; (b) a phase skeleton from 2027 to 2030 with gate criteria for each phase.

### R2. PRCP: a real problem of today

1. What share of production outages and incidents are caused by changes (deploys, config, upgrades) today? Use official postmortems (Google Cloud, AWS, Cloudflare, Microsoft, GitHub and others, including CrowdStrike's July 2024 root-cause report), DORA reports, the Google SRE books, and peer-reviewed studies of cloud incidents.
2. What do existing tools and published internal systems already solve: Argo Rollouts (analysis), Flagger, Spinnaker with Kayenta, Keptn (check its current status), Kargo, commercial platforms (Harness, LaunchDarkly and others), and published systems such as Google's Canary Analysis Service and Microsoft's Gandalf (NSDI 2020)? What stays unsolved, according to issue trackers, user surveys, talks and postmortems?
3. Evaluate these candidate directions, and add any better one you find: (a) fleet-wide rollout gating across many clusters (waves, automatic halt on bad signals), which matches his IBM work; (b) release gating for AI models and agents using evaluations; (c) coordinated promotion of interdependent services. For each: evidence the problem is real today, who has it, existing solutions and their gaps, fit with his background, whether one person at about 12 hours a week can reach a credible v1 in 12-18 months, and the value in interviews at the target tier.
4. What are real scale numbers at large organisations (number of services, deploys a day, clusters, nodes, published Kubernetes scalability limits)? Use them to propose a design envelope: what PRCP must handle at v1, at 10x and at 100x, and what usually breaks at each step.
5. Which architecture principles let a control plane like this grow 10x and 100x without a rewrite, from published designs (for example Borg, Omega, Kubernetes, Spinnaker)? Does PRCP's current core (pure decision function, PASS/WARN/BLOCK/UNKNOWN, fail closed) match industry practice, or does it need to change?

**Deliver:** a scorecard of the directions (0-5 per criterion, with evidence IDs), one recommended direction, a one-paragraph statement of the unsolved problem PRCP should own, and the design envelope numbers with sources.

### R3. Proving distributed-systems behaviour as one engineer

Evaluate, with evidence: Jepsen's Maelstrom and Fly.io's Gossip Glomers challenges; Jepsen-style testing; deterministic simulation testing (FoundationDB, TigerBeetle, Antithesis, and any usable Go or Python libraries); TLA+ and lighter options (PlusCal, Quint, the P language); property-based testing (Hypothesis for Python, rapid for Go); fault injection on Kubernetes (Chaos Mesh, LitmusChaos, Toxiproxy); load tests with many simulated endpoints (k6, vegeta). Also the best learning resources for distributed-systems theory (for example MIT 6.5840, Martin Kleppmann's lectures, Designing Data-Intensive Applications and whether its second edition is out).

**Deliver:** a table: method | what it proves | what it cannot prove | learning hours at his level | hardware needs (an old laptop and kind) | best beginner resource (live code preferred) | who uses it in industry (evidence) | fit with PRCP | recommended order. Then a recommended sequence tied to PRCP milestones.

### R4. Pattern recognition for DSA and system design (highest priority)

1. What does learning research say about recognising the deep structure of a problem instead of its surface story? Check, for example: Chi, Feltovich and Glaser (1981) on expert vs novice problem sorting; interleaved practice (Rohrer and Taylor 2007, later classroom trials, the Brunmair and Richter 2019 meta-analysis); comparing cases and analogical encoding (Gentner, Loewenstein and Thompson 2003; Alfieri, Nokes-Chiu and Schunn 2013); worked examples; retrieval practice and spacing (Cepeda et al. 2006; Dunlosky et al. 2013); computing-education work on programming plans, subgoal labels and Parsons problems. Give effect sizes, the population studied (school students vs adults), and the conditions where each method fails.
2. Turn that into DSA training: how to train recognition of disguised problems (classification-only drills, disguise sets, look-alike contrast pairs, mixed practice), how many repetitions, and how to measure recognition accuracy weekly. How should it fit a reading-only slot with no coding?
3. Interview evidence from 2025-2026: how often do target-tier interviews use known problems vs disguised variants, which follow-up questions are asked for each pattern, and what do interviewers score? Use official guidance, interviewing.io data and dated candidate reports.
4. Which resources train recognition explicitly, and how good are they: NeetCode, AlgoMonster, Grokking the Coding Interview Patterns, Beyond Cracking the Coding Interview (check its "triggers" idea), Tech Interview Handbook, LeetCode Explore and others you find?
5. The same for system design: recognising which building block a requirement points to, and handling follow-ups (10x traffic, a region failure, a hot key, a slow dependency). Which resources and rubrics show what senior and staff-level design interviews at the target tier score?

**Deliver:** (a) a recognition training design: drill types, weekly volume, measurement, slot fit; (b) a table for every DSA family (use NeetCode's roadmap categories as the base and add sub-patterns interviews treat separately, such as prefix sums, monotonic stack, binary search on the answer, union-find, topological sort): family | deep-structure signal in plain words | 3-5 disguised problems (LeetCode numbers and names, checked to exist) | one look-alike problem that needs a different pattern, and why | the 3 most common follow-ups; (c) the same kind of table for about 12 system design building blocks.

### R5. Learning method and time slots

1. Attempt-first (productive failure: Kapur; the Sinha and Kapur 2021 meta-analysis) vs worked-example-first (Sweller; the expertise reversal effect, Kalyuga; fading guidance, Renkl; the assistance dilemma, Koedinger and Aleven): when does each win for adult learners, and how should the choice depend on whether a topic is completely new or builds on a base?
2. Forgetting and spacing for procedural skills such as coding syntax across several parallel tracks (for example Arthur et al. 1998 on skill decay); the cost of switching between tracks; how many tracks a learner at about 12 hours a week can keep alive.
3. Which kinds of learning work in reading-only phone slots, audio-only slots and short slots, and which do not? What does research on sleep and memory consolidation say about evening study?
4. How to train independent problem solving and debugging, for someone who must work without help.

**Deliver:** a recommended learning loop for each topic type (new concept, new tool, recognition skill, design skill), and a slot map table: slot type | best activities (evidence IDs) | what to avoid | example.

## 5. Evidence rules

- **Bar for any recommendation:** at least 3 independent, dated sources, primary sources preferred. If fewer exist, mark it WEAK EVIDENCE and say so; do not drop the question.
- **Source ranking:** (1) primary: official career pages, official interview guidance, earnings releases and filings, official postmortems, official documentation and repositories, peer-reviewed papers and meta-analyses, talks by the engineers who built the system; (2) secondary: reputable press (Reuters, Bloomberg, FT, The Information, Economic Times, Moneycontrol), established practitioner blogs with a named author; (3) self-reported: LeetCode Discuss, Glassdoor, Blind, Reddit, levels.fyi, which count only as support and need at least 3 dated reports for one claim.
- **Recency:** job postings live or dated within the last 6 months; interview reports from 2025-2026; market data from 2025-2026. Older sources are fine for research papers and foundational system designs.
- **Never:** invent a URL; cite a homepage in place of the exact page; use SEO listicles, content farms or AI-generated summaries as evidence; state a statistic you did not see on the page.
- **Red team:** for every recommendation, search for the strongest counter-evidence and report it, even if it weakens your case.
- **Estimates:** give time costs at this learner's real level (beginner in DSA and Go, about 12 hours a week), counting setup, finding resources and rewatching. Never compress hours to look neat.
- **Out of scope:** salary, compensation, visa and immigration.

## 6. Method

1. Before searching, write your research plan: the sub-questions for each part.
2. Search broad, then go deep on the best primary sources.
3. For each claim, record the exact page and date.
4. Run the red-team search for each recommendation.
5. Write the report in the format below.

## 7. Output format (exactly this)

1. **Executive summary:** the 15 most important findings for v3.9, each with evidence IDs.
2. **Top 10 changes for v3.9,** ranked by impact on the long goal, each with evidence IDs and a confidence level.
3. **Research plan used** (short).
4. **R1 to R5,** each with: A. Findings (bullets, each tagged with evidence IDs like [E12]); B. Recommendations, each as: what | why | evidence IDs | time cost at his pace | what it replaces or which date it moves | risk reduced | confidence (high, medium, low); C. What would change these recommendations; D. Conflicts and gaps; then the part's required deliverable tables. Mark each part COMPLETE or INCOMPLETE.
5. **Evidence table,** numbered E1, E2, and so on: ID | claim (one line) | source title | exact URL | publication date | date accessed | type (primary, secondary, self-reported, peer-reviewed) | independent of other sources? | confidence | contradicting evidence IDs.
6. **Could not find or verify** (list).
7. **Assumptions I made** (list).
