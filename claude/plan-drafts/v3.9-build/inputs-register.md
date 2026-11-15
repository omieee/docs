# v3.9 inputs register

**Started:** Sun 2026-11-15 10:45 IST, Claude. **Status:** record only. No plan edit, no verdict. v3.8 governs until Om approves v3.9.
**Read from:** `omieee/docs` fresh clone at `d1c92aa` (Nov 14 17:06 UTC): `claude/plan-drafts/2026-11-15-batch.md`, `phase1-log.md` later-refactor log, `claude/state.md`, `chatgpt/state.md`, `chatgpt/outbox.md`, `chatgpt/plan-drafts/` (v3.9 proposal, Nov 4 audit, Oct 27 AI review), `chatgpt/research/2026-11-06-...coachops-proposal.md`, `claude/plan-drafts/2026-10-27-ai-direction-review.md`, and Om's chat of Nov 15 (10:15 and 10:33 IST).

**How v3.9 gets built (agreed in chat, Om to confirm):** S0 this register · S1 W6 close and re-forecast (fresh chat) · S2 think-through: every item gets DECIDE, RESEARCH or DROP · S3 research briefs R1-R5 · S4 research runs (Fable) · S5 verification of every decision-driving claim (Claude and ChatGPT, separately) · S6 section 9 entries, Om approves line by line · S7 build with the generator, `check_plan.py` PASS, negative tests FAIL as expected · S8 blind audit of the built file (Fable and ChatGPT, separately) · S9 approval, `plan/` commit, upload to both projects the same day. Daily work continues on v3.8 plus decisions already approved (Go appendix, Kubernetes course order, Oct 29 operating rule) while this runs.

**Next step key:** DECIDE = Om decides in chat, no research needed · R1-R5 = goes into that research brief · DATA = waits for a measured number · FOLD = already decided, only the plan text or week rows change.

## A. Booked by v3.8 for Nov 15

| ID | Item | Type | Source | Next |
| --- | --- | --- | --- | --- |
| A1 | Re-forecast Gates A, B, C from logged minutes and from topics proved, W3-W6 | DATA | v3.8 s4, s5; batch A1 | S1 (W6 close) |
| A2 | Full cost of the 5-minute warm-ups (28-45h): gates move or a named source pays | DECIDE | v3.8 s5, s6.12; batch A2 | after A1 |
| A3 | W6-W7 JD harvest results as inputs; Helm IDEA waits for the W7 close (Nov 22) | DATA | Oct 27 candidates file; batch A3 | W7 close |

## B. Pending plan changes (Nov 15 batch, section B)

| ID | Item | Type | Source | Next |
| --- | --- | --- | --- | --- |
| B1 | Oct 29 operating rule into s0 safeguard 6 and s6.6 #11 (boxes are a guide, judge the flow, DSA about 1h on a 2h day) | text of a decided rule | batch B1 | FOLD |
| B2 | Y7a `client` fixture lines move to Y7b | BUG | batch B2 | FOLD (text only) |
| B3 | K1 resource: replace the 31-second intro | BUG | batch B3 | FOLD, likely absorbed by B13 |
| B4 | Finalizer with nothing to clean up (OP4, OP5): Claude option (a), real registration by UID, about 2.5-3h, vs ChatGPT test-only fixture, 2h | BUG | batch B4, section C point 3 | DECIDE |
| B5 | A2: a down target becomes a `ProbeResult`, never cancels other probes (+1h) | GAP | batch B5, C point 6 | DECIDE |
| B6 | OP6 envtest proof, stale PRCP answer test, OP1 envtest limits (+1.5h) | GAP | batch B6, C point 6 | DECIDE |
| B7 | CDP on-ramp: OP1 earlier only if controller work at IBM is confirmed and regular | IDEA | batch B7 | DATA (office) |
| B8 | ChatGPT v3.9 proposal F1, F2, F5: never-cut line adds cloud and Terraform; CL3 as four atomic 3h labs and its order against K6b; stronger checker (MC2/MC5 false PASS, same-week order) | GAP, BUG, BUG | batch B8, C points 4-5, 7 | DECIDE line by line |
| B9 | `check_plan.py` docstring wording | cosmetic | batch B9 | FOLD |
| B10 | Task-specific scoring bands (PASS 85+, PARTIAL 70-84, DEVELOPING 50-69, FAIL <50) | GAP | batch B10 | DECIDE |
| B11 | DSA's protected daily share vs loop evidence | GAP | batch B11 | R1 (share at the target tier; DSA's presence stays settled) |
| B12 | Go order follows the course (approved Nov 3); fold the Nov 4-15 appendix into weeks | FOLD | batch B12 | FOLD |
| B13 | Kubernetes follows Mumshad's KodeKloud CKA order (decided Nov 13), skip list kept; rebuild rows | FOLD | batch B13 | FOLD |

## C. Om's Nov 11 instruction: tailor v3.9 to the topic-level record (batch section D)

| ID | Item | Type | Next |
| --- | --- | --- | --- |
| C1 | Progress is reported per topic as taught, proved, used in real code; hours second | IDEA | DECIDE |
| C2 | No topic stays "taught, not proved" for more than 7 days | GAP | DECIDE |
| C3 | Multi-week units (G2, K1, L1, P1) get a small proof at the end of each slice | GAP | DECIDE |
| C4 | Size each week to the measured record, not the 12-hour assumption alone | GAP | after A1 |
| C5 | Items taught but not proved are proved before new topics start in the same track | GAP | DECIDE |

## D. ChatGPT inputs still open

| ID | Item | Type | Source | Next |
| --- | --- | --- | --- | --- |
| D1 | CoachOps: a small deterministic gate before each session, with an incident casebook; Claude's independent critique is owed | IDEA | `chatgpt/research/2026-11-06-...coachops-proposal.md`; outbox Nov 6 | Claude critique, then DECIDE |
| D2 | Nov 4 reliability audit, findings 1-5 (overlap B12, B8, B1; finding 4: human-visible preflight before every lesson) | BUG, GAP | `chatgpt/plan-drafts/2026-11-04-plan-reliability-audit.md` | merge into B and G, DECIDE |
| D3 | AI career dual track (AI-infra vs applied AI) and Claude's review F1-F5 | IDEA | both Oct 27 AI files | R1 |

## E. Om's inputs, Nov 15

| ID | Item | Type | Next |
| --- | --- | --- | --- |
| E1 | Token rules in s0: one chat per block or day, warn once when long with a 3-5 line handoff (permanent); small start-of-session read with a one-page week card; lean project docs; hash or PR number instead of pasted code; batched questions; research outside the driving chat | IDEA | DECIDE |
| E2 | PRCP solves a real problem of today, not a portfolio project; design envelope taken from real large-organisation numbers; very strong base; path to much larger scale | IDEA | R2 |
| E3 | Accurate proof of distributed-systems principles (candidates: Maelstrom and Gossip Glomers, fault injection on kind, deterministic simulation testing, TLA+, Raft labs) | IDEA | R3 |
| E4 | DSA overhaul for recognition: Om "can't tell the pattern" (Nov 15). Recognise a disguised problem (Koko eating bananas told a thousand ways is still binary search on the answer) and handle follow-ups | GAP | R4 |
| E5 | System design gets the same recognition and follow-up training | GAP | R4 |
| E6 | Long goal: Google, Anthropic, OpenAI tier by 2028, else 2029, else 2030, no title fixed; v3.9 bridges Phase 1 into Phases 2-5, with what AI knowledge will be required by 2027 found by research | IDEA | R1 |
| E7 | Learning method: Om learns by trial and error ("no one helps a lead"); check against v3.8's worked-example-first rule and the Oct 18 zero-knowledge rule | GAP | R5 |
| E8 | Slot map: the most useful activity for each kind of slot (desk block, bedside reading only, walk or commute audio, office days, the short night slot) | IDEA | R5, then DECIDE |
| E9 | More hours if needed (night); no cost cutting on time or money for resources; the 15-working-day leave after W6 | DATA | Om to confirm leave dates |
| E10 | Model roles: Claude drives; Fable runs research and a blind audit; ChatGPT verifies and audits separately; Om decides | IDEA | DECIDE (Nov 15) |

## F. Coach reliability

| ID | Item | Type | Next |
| --- | --- | --- | --- |
| F1 | Coach-error lessons: 24-25 logged errors, about 346 minutes, Oct 19-Nov 4 (`claude/coach-errors-2026-10-19-to-11-04.md`), plus the repeated plain-words errors with counts (owed for the Nov 15 close) turned into safeguards that prevent repeats | GAP | DECIDE with D1 |

## Research briefs (drafted only after S2)

- **R1 Target employers and the AI shift, 2027-2030:** what Google, Anthropic, OpenAI and that tier hire for in infrastructure, platform and AI-infrastructure roles at 12-15 years; their loops now and how AI is changing them; the DSA share at that tier (B11); the AI knowledge needed (D3); follow-the-money evidence. Feeds E6 and the Phase 2-5 skeleton.
- **R2 PRCP real problem:** release and rollout failures today (incident and postmortem data); what existing tools (Argo Rollouts, Flagger, Kayenta, Spinnaker, Keptn and others) solve and what stays unsolved; real scale numbers at large organisations to set the design envelope; candidate directions (fleet rollout gating across many clusters, release gating for AI models and agents with evaluations). Feeds E2.
- **R3 Proving distributed-systems behaviour as a solo engineer:** methods in E3 with time cost at Om's level, hardware needs, order, and what interviewers at the target tier value. Feeds E3.
- **R4 Pattern recognition for DSA and system design:** learning research on deep vs surface structure, mixed practice, comparing problems, and interview evidence on how problems are disguised and which follow-ups are asked. Feeds E4, E5.
- **R5 Learning method and slots:** attempt-first vs worked-example-first for an adult with Om's profile; forgetting and spacing across all tracks; which work fits reading-only, audio-only and desk slots. Feeds E7, E8.

**Every brief returns one table:** claim, link, date, primary or secondary source, confidence, conflicting evidence. **Bar for a plan decision:** at least 3 independent, dated sources, primary preferred, follow-the-money sources for market calls; a claim with no link is dropped.
