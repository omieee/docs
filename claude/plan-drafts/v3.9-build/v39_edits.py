# v3.9 edits, layered on the v3.8 layer (Claude, Nov 15 2026). Every target string below is v3.8 output text.
# rep() fails loudly if a target is missing. Sections 4-6 and 14 are edited in their own files.

# ---------- title, header, section 0 ----------
s0 = rep(s0, "# Phase 1 Master Plan v3.8: Portable Skills You Can Prove", "# Phase 1 Master Plan v3.9: Portable Skills You Can Prove")
s0 = rep(s0, "the first spoken stories in W10), effective when Om uploads it · **Replaces:** v3.7,",
         "the first spoken stories in W10), approved by Om on 2026-10-24 · **v3.9 re-forecast:** built by Claude and verified by ChatGPT on 2026-11-15 (Om, Nov 15: one coach builds, the other verifies), final revision approved by Om on 2026-11-15 (19:10 IST: \"lets create final plan now and will freeze that\"): dates at 12 hours a week with slower-pace illustrations, no scope shrink (Om), warm-ups funded, Go on the Learning Go 2e order, Kubernetes on the KodeKloud course order, the finalizer fix, a distributed-systems proof, PRCP's real problem and scale envelope, recognition-first DSA and design, token rules, topic-level progress; revision 2 the same day after ChatGPT's verification: its five bugs fixed, P1 re-sized against PRCP PR #11, release evidence (E1), dated DSA reviews, short-week rules and a W7-W12 run sheet; final revision after ChatGPT's second review: hiring dates tied to the gates, fixed-work illustrations, decisions that move with their evidence, a four-line Gate A record, the ownership checkpoint and the transfer check; effective when Om uploads it · **Replaces:** v3.8, v3.7,")
s0 = rep(s0, "Fade this step for material Om has already shown in a recent check; never skip the ask-first question or the teaching of a new prerequisite (v3.6).",
         "Fade this step for material Om has already shown in a recent check; never skip the ask-first question or the teaching of a new prerequisite (v3.6). **New vs known (v3.9):** for a topic new to Om (Go pointers, a new DSA family, controllers, Terraform) the worked example comes first; where he has real prior use (Kubernetes he runs at IBM with `describe`, `logs` and events, Postgres concepts, designs of systems he ran) he attempts first with the worked example kept for reference, and the coach then teaches the gap. Evidence: worked examples help novices most and lose their benefit as knowledge grows, the expertise reversal effect (Kalyuga, Ayres, Chandler and Sweller, 2003); Om says he learns by trial and error (Nov 15).")
s0 = rep(s0, "6. **Box every block.** Before starting, state the block's plan time from the rates table (section 5). At the box, say so and give a save line. At 1.5 times the box, stop, whatever the state; only Om extends, and only after being told the overrun in minutes. \"Stop\" from Om ends the block at once: the next reply is only the save line. DSA follows section 6.6 #11.",
         "6. **Box every block, then judge the flow (Om, Oct 29; written in by v3.9).** Before starting, state the block's plan time from the rates table (section 5). The box is a guide, not a wall: knowing the thing matters more than the minutes. If the flow is good and there are no signs of strain, let it run and say the minutes at the end; if a block is not turning fruitful, pause, say so, and re-plan it for a later slot with a different approach. DSA stays at about 1 hour at most on a 2-hour day unless Om says otherwise. \"Stop\" from Om ends the block at once: the next reply is only the save line. The week's row is the floor; anything more is a bonus. DSA follows section 6.6 #11.")
s0 = rep(s0, "\n\n**Two coaches, one repository.**",
         """

*Repeats written in by rule 12 (v3.9: from the Oct 19 to Nov 15 coach-error logs)*
14. **Check a note's style before sending it** (Nov 12, Nov 13): a teaching note for bedside reading is one connected read, in short steps, on Om's own numbers, with no log text at the top and no compressed sentences; never five ideas packed in one block, and never one point a day cut off from the rest.
15. **Ask the setup before any setup command** (Nov 12, the zsh vs bash slip; Nov 4, Postgres only in Docker): shell, operating system and how the tool is installed, before a command that edits a profile or installs anything.
16. **Plain names, not log labels** (Oct 19 "planted bugs", Nov 14 "MP1's find_shelf"): name a skill or a past task in plain words, never by a log label or an old function name, and give a task once, without its answer in the same message.
17. **Count the fixed days before planning a day** (Nov 12): office days, the Thursday commitment and on-call days come first; a day plan that ignores them is a coach error.
18. **Size any delegated run to what Om can spend** (Nov 15, the Fable run): before advising a long research run or an agent, ask what credit or time Om has, and split the run into small parts that save as they go.

**Two coaches, one repository.**""")
s0 = rep(s0, "- GitHub token (Om, Oct 18): a coach uses Om's GitHub token only with his explicit OK each time. When repo access is stuck, the coach asks Om first.",
         """- GitHub token (Om, Oct 18): a coach uses Om's GitHub token only with his explicit OK each time. When repo access is stuck, the coach asks Om first.
- Plan versions (Om, Nov 15 2026, 13:14; v3.9): one coach builds a plan version and the other verifies it, or the other way round, with no research pipeline in between. v3.9 was built by Claude and is verified by ChatGPT. Outside evidence is looked up only for the decisions that change direction, and each is cited where it is used. Fable is not used for plan work.
- **Session preflight (v3.9; ChatGPT's Nov 4 audit, finding 4).** Before a lesson, the coach shows Om five lines: the IST date and the week; the plan line being taught; every term the lesson uses, checked against the taught list; the exact resource part, checked today; the box. If a line fails, the lesson does not start. ChatGPT's fuller Nov 6 CoachOps proposal (a scripted gate and an incident casebook) stays open for Om's decision.

**Token rules (v3.9, Om's Nov 15 input; permanent).** Fewer tokens, same quality:

1. One chat per block or per day. When a chat is getting long, or earlier parts are being trimmed, the coach says so once and gives a 3-5 line handoff (Om, Oct 15; permanent from Nov 15).
2. A session start reads only section 0, the current week's row in section 14 and the due items, by line range, plus the newest lines of the logs and outboxes; the coach never prints the whole plan into the chat. The rest of the file is read for a plan change, a gate or the Sunday close.
3. Om points to work by commit hash, PR number or file path; he never pastes code the coach can fetch.
4. Questions for a block go in one message, not one per reply.
5. Research and plan builds run in their own chat, never in a teaching chat; the result comes back as a file link and a 5-line summary.
6. Project docs stay lean: each project holds only this plan and its checker; drafts and records live in `omieee/docs`.
7. Each coach's `state.md` (20 lines at most) is the session cache; canonical logs still win before any verdict.""")

# ---------- section 1 ----------
s1 = rep(s1, "Forecast (v3.8): Gate A May 2 2027, Gate B Feb 6 2028, Gate C Mar 5 2028,", "Forecast (v3.9): Gate A Jun 6 2027, Gate B Apr 30 2028, Gate C May 28 2028,")
s1 = rep(s1, "820.75 in v3.7, 834.5 in v3.8 |", "820.75 in v3.7, 834.5 in v3.8, 969 in v3.9 (the Nov 15 re-forecast, 934 in its first draft; section 4 gives available-time scenarios) |")
s1 = rep(s1, "**Role identity, stated exactly:**",
         """- **The long goal (Om, Nov 15 2026; v3.9):** a hands-on role at Google, Anthropic, OpenAI or a company of that tier, by 2028, else 2029, else 2030, no title fixed; set high on purpose. What the numbers say (section 4): at 12 hours a week Gate C lands May 28 2028 and the top-tier preparation (Phase 2) starts after it, so a top-tier offer in 2028 needs almost every week at about 12 hours of plan work from now. The target year stays Om's goal; Phase 2 sets its loop window at Gate C (section 11), so the plan does not derive an offer year from the slower illustrations in section 4 (v3.9 final, ChatGPT's finding 2). The plan keeps the goal and shows the hours it costs.

**The real problem PRCP solves (v3.9, Om's Nov 15 input).** Most outages start with a change. Google's SRE book says roughly 70% of its outages come from changes to a live system, and its SRE Workbook (Appendix C) finds binary pushes (37%) and configuration pushes (31%) the top two triggers in thousands of postmortems from 2010 to 2017. Uptime Institute's 2025 outage analysis puts configuration and change-management failure at half of major network outages. In July 2024 one faulty CrowdStrike content update reached more than 8 million Windows machines at once; its root cause analysis commits to staged deployment through rings, each promoted only after the last shows no problem. PRCP is built to be that promotion decision, made from probe evidence and fail-closed: a change moves to the next environment only on positive evidence. Until E1's proof passes (v3.9 r2), its honest claim is narrower: it summarises the probe results it has received. On Nov 15 Claude ran `decide()` from PRCP PR #11 and it returned PASS when probe A passed and required probe B never reported, and the same for one passing result sent twice (section 6.1, release evidence). Its design envelope starts from Om's own IKS fleet (200-300 clusters, about 19,000 workers) and is written for a million probed endpoints in the H3 scale ADR. The base stays a pure `decide()`, so the scale work never touches the decision logic, and DS1 proves the coordination pieces on Maelstrom. It is a real tool for a real failure mode, not a portfolio toy; what it can honestly claim is still a personal project's claim (section 9, claim discipline).

**Role identity, stated exactly:**""")
s1 = rep(s1, "\n\n**Unchanged and still frozen**",
         """

**Decisions adopted in v3.9 (Nov 15 2026 re-forecast; built by Claude, verified by ChatGPT, approved by Om)**

| # | Was (v3.8) | Now (v3.9) | Evidence |
| --- | --- | --- | --- |
| 32 | Dates at 12 hours a week only | The same 12-hour rows; 9 and 6 hours shown as available-time scenarios, not a forecast (r2); the next re-forecast, Sun Dec 6 2026, uses active minutes, closed plan hours and restart minutes from the W7-W9 closes | W3 to W5 logged about 18.3, 7.5 and 5.3 focused hours, which is activity, not closed scope (ChatGPT's finding 1); W6 not closed |
| 33 | Warm-ups unpriced (28 to 45 hours) | Funded: 34.25 hours inside "Proofs and weekly close"; the gates move | Om, Nov 15: no shrink; trial minutes 2, 3 and 9 |
| 34 | Go units on Learn Go with Tests order; G2 3.5 hours | Learning Go 2e order with Boot.dev first and Learn Go with Tests for the tests; G2 8.75 hours, pointers before methods | Go strategy approved by Om, Nov 3; step A took twice its box |
| 35 | Kubernetes lessons picked by the plan | The KodeKloud CKA course's own order; exam-only parts skipped | Om, Nov 13; the plan's K1 lab used commands not yet taught |
| 36 | No accurate proof of distributed-systems behaviour | DS1: Gossip Glomers 1-4 in Go on Maelstrom, every run checked by Jepsen's checker | Om, Nov 15; Fly.io and Jepsen's author built the series |
| 37 | PRCP described as a release gate | Its problem statement and scale envelope from outage data; the scale ADR in H3 | Google SRE book and Workbook Appendix C; Uptime 2025; CrowdStrike's Aug 2024 RCA |
| 38 | DSA trained on solutions | Recognition first: a pattern card per NEW, a weekly name-the-pattern drill at bedside, one follow-up on each COLD from D7 | Chi, Feltovich and Glaser 1981; Rohrer and others 2014 and 2020; Om's 875 record |
| 39 | Design blocks taught, recognition not trained | A signal card per building block; the three hardest requirements named first; two follow-ups in every mock | The same evidence; Om's Nov 15 input |
| 40 | A hard stop at 1.5 times the box | The box is a guide; judge the flow; DSA about 1 hour on a 2-hour day | Om, Oct 29 |
| 41 | A finalizer with nothing to remove; a down target could cancel the others; no stale-answer test | A real registration by UID; a down target is a failed result; a stale answer is ignored | Both coaches, Oct 27-30 |
| 42 | AWS labs before the full local system, CL3 in six pieces | K6b before CL3; four atomic 3-hour CL3 sessions | ChatGPT's v3.9 proposal F2, checked by Claude Oct 30 |
| 43 | Token use not managed | Section 0 token rules | Om, Nov 15 |
| 44 | Progress read in hours | Topics first: taught, proved, used in real code; no topic taught but not proved for more than 7 days (section 9) | Om, Nov 11: "I don't care about hours" |
| 45 | Plan versions built through a long review and research process | One coach builds, the other verifies (section 0) | Om, Nov 15 13:14 |
| 46 | P1 sized at 3 more hours for four repositories and the decision's evidence | 9 more hours, part by part, against PRCP PR #11; Gate A moves two weeks | ChatGPT's proposal 2, modified; the measured Service slice (Nov 4-12) |
| 47 | `decide()` trusted to make the release decision | E1: one result per required probe, for this release, missing as UNKNOWN, through a gate endpoint; `decide()` unchanged; the Y6 property fixed | ChatGPT's proposal 3, modified; Claude's run on PR #11 (section 6.1) |
| 48 | Due DSA reviews hidden in the cold pool | Dated reviews first in the week of their date; NEW work slides | ChatGPT's finding 2; the tracker's dates |
| 49 | A short week left to the coach in the moment | One fixed order for short weeks, a W7-W12 run sheet at 9 and 6 hours, and three lines for next week in every close | ChatGPT's proposal 1, modified |
| 50 | Scale design and load test with no shared numbers | The H3 ADR states its inputs and what would prove it wrong; O1 measures against them, 0 added hours | ChatGPT's proposal 4 |
| 51 | Hiring dates written by hand; slower-pace dates read as a forecast; a decision due even when its evidence moved | Application and joining dates tied to the gates by the checker; 9 and 6 hours as fixed-work illustrations with the weekly close costed; a decision moves with its evidence | ChatGPT's 16:22 review, findings 1 to 3 |
| 52 | Gate A checked only the technical bar; ownership asked for with no next step | A four-line Gate A record like Gate C's; the W8 ownership checkpoint names the code path, the person and the next conversation; a transfer check on every full rep and Om's yes or no on F2 | ChatGPT's 16:22 review, ideas 4 and 5; 7 of 8 October postings screen on production ownership |

**Unchanged and still frozen**""")

# ---------- section 7 ----------
s7 = rep(s7, "Focused hours, planned / actual (bedside required items included):\nActual vs planned hours, each unit closed:",
         "Topics first (v3.9, Om Nov 11): taught / proved / used in real code this week; any topic taught but not proved for more than 7 days\nPattern drill (v3.9): this week's name-the-pattern score, out of 6\nFocused hours, planned / actual (bedside required items included):\nActual vs planned hours, each unit closed:")
s7 = rep(s7, "Next week's scope:", "Next week's scope (v3.9 r2): the first dated obligation; the first runnable step; what moves first at 9 hours and at 6 (section 14, short weeks):")
s7 = rep(s7, "Coach errors this week (both coaches): count, minutes lost, rules broken (section 0 safeguards)",
         "Coach errors this week (both coaches): count, minutes lost, rules broken (section 0 safeguards); target under 30 minutes a week (Nov 4)")

# ---------- section 8 ----------
import spec as _spec
s8 = s8.replace("W58", f"W{58 + _spec.K1_INS}")
s8 = rep(s8, "**JD harvest in November (W6-W7, v3.6 method):**", "**JD harvest in November (W7-W8 in v3.9 r2, v3.6 method):**")
s8 = rep(s8, "in the same weeks (W6-W7 and", "in the same weeks (W7-W8 and")
s8 = rep(s8, "(0.5h in W7 and", "(0.5h in W8 and")
s3 = rep(s3, "Om decides that change (F2) at the W7 close, Nov 22 2026.", "Om decides that change (F2) at the W8 close, Nov 29 2026 (v3.9 r2: the harvest's second part moved to W8).")

# ---------- section 9 ----------
s9 = rep(s9, "the matching Go course chapter,", "the matching Learning Go or Boot.dev chapter (v3.9),")
s9 = rep(s9, "- **Freeze (v3.8, ChatGPT's Oct 24 audit, B5):** once Om approves v3.8, its structure is frozen until the Nov 15 re-forecast.",
         "- **Prove what was taught (v3.9, Om's Nov 11 instruction).** No topic stays taught but not proved for more than 7 days: its check is booked in the same or the next session. A unit that runs over several weeks (G2, K2, L1, P1 and the like) gets a short proof at the end of each slice, so a stalled unit shows within a week. Inside a track, a topic taught but not proved is proved before the next new topic starts.\n- **Freeze (v3.9).** Once Om approves v3.9, its structure is frozen until the Dec 6 2026 re-forecast and then between monthly re-forecasts; only the three triggers below open change control. Coach research and plan rebuilds run outside Om's study block and never take his hours (v3.9 final; one planning exchange cost him 70 minutes in W5). The v3.8 wording follows for the record.\n- **Freeze (v3.8, ChatGPT's Oct 24 audit, B5):** once Om approves v3.8, its structure is frozen until the Nov 15 re-forecast.")

# ---------- section 11 ----------
s11 = rep(s11, "Phase 2 starts after Gate C, now forecast Mar 5 2028 (v3.8).", "Phase 2 starts after Gate C, now forecast May 28 2028 (v3.9).")
s11 = rep(s11, "an offer around Gate B (now early February 2028) means joining around May 2028", "an offer around Gate B (now the end of April 2028) means joining around August 2028")
s11 = rep(s11, "- **No India offer by about three months after Gate A (now early August 2027):**", "- **No India offer by about three months after Gate A (now early September 2027):**")
s11 = rep(s11, "**Critical paths.**", "**Top-tier target (v3.9).** Google, Anthropic, OpenAI or that tier (section 1). What those roles and loops need in 2028 to 2030, the AI knowledge included, is researched at Gate B from dated job posts and follow-the-money evidence, because requirements read today will be two years old by then. v3.9 invents no such list now; ChatGPT's and Claude's Oct 27 AI-direction reviews are the inputs to that research.\n\n**Critical paths.**")

# ---------- section 13 ----------
s13 = rep(s13, "**Rejected:** 8/10 pass bars on every checklist;",
          """**v3.9 (Nov 15 2026 re-forecast; built by Claude, verified by ChatGPT; Om's instruction of 13:14: one coach builds, the other verifies).** Inputs: the Nov 15 batch (`claude/plan-drafts/2026-11-15-batch.md`), the v3.9 inputs register, Om's Nov 11 and Nov 15 instructions, ChatGPT's v3.9 proposal and Nov 4 audit. Labels: BUG, GAP, IDEA.

- **(1) DATA · Re-forecast.** W4-W6 recorded as done at plan hours; the work not done moves forward unchanged; the measured-pace dates are in section 4. First-draft gates: A May 23 2027 (W33), B Apr 9 2028 (W79), C May 7 2028 (W83); revision 2 below moves them.
- **(2) GAP · Warm-ups funded** (34.25 hours). Om: no shrink, so the dates move.
- **(3) BUG, folded · Go order** (batch B12): the Learning Go 2e spine approved Nov 3; the Nov 4-15 appendix is now G2's rows; G2 sized at the measured pace (+6.25 hours across G2, G3, G4, G6).
- **(4) BUG, folded · Kubernetes order** (batch B3 and B13): the KodeKloud CKA course order; K1's 31-second intro replaced; the kubectl drill moved into K2 after the course's Imperative Commands lesson; ConfigMaps, Secrets and security in K4, storage and networking in K5; hours unchanged.
- **(5) BUG and GAP · Controllers and agent** (batch B4, B5, B6): finalizer option (a), A2's down target, OP1's test-environment limits, OP6's stale answer and run proof (+5.5 hours).
- **(6) BUG · ChatGPT's proposal F1, F2, F5** (batch B8): the never-cut line names AWS, Terraform, CL3's proof and CL4's state, locking and CI credentials; K6b before CL3, with four atomic 3-hour CL3 sessions; the checker keeps MC labels apart, checks order inside a week, checks that no unit disappears and that CL3 sessions are whole. L3's teaching ends before MC2 (Claude's Oct 30 point 4).
- **(7) IDEA, Om's · PRCP's real problem and scale envelope** (section 1; the H3 scale ADR, +2 hours) and **DS1**, the distributed-systems proof (+13 hours).
- **(8) GAP, Om's · Recognition first** in DSA (section 6.6 #14) and design (section 6.4), inside the existing hours and bedside time.
- **(9) IDEA, Om's · Token rules, the slot map, new vs known teaching, topic-level progress, the session preflight, safeguards 14 to 18.** Text only.
- **(10) Text only:** Y7a's `client` fixture lines moved to Y7b (batch B2); Om's Oct 29 operating rule written into safeguard 6 (batch B1); Naukri placed by date in W31; the first two stories told aloud move to W15 (R3 and R2 slipped in W4-W6, and Om is not applying, so no calibration call waits on them).
- Totals in the first draft: 834.5 to 934 hours, 84 weeks, DSA 163.25.

**v3.9 revision 2 (Nov 15 2026, after ChatGPT's verification; ChatGPT's five findings and five proposals, `chatgpt/outbox.md` and `chatgpt/plan-drafts/2026-11-15-v3.9-execution-proposal.md` at `05b3735`).** Build note: `claude/plan-drafts/2026-11-15-v3.9-r2-build-note.md`.

- **(11) BUG, fixed · The forecast counted activity as closed scope** (finding 1): 9 and 6 hours become available-time scenarios (section 4); W6 is UNVERIFIED until its close; the Dec 6 re-forecast reads the three numbers of section 5's pace check.
- **(12) BUG, fixed · Due DSA reviews were hidden** (finding 2): dated reviews first in their week (W7, W8, W12-W15, W17); the NEW work slides; the checker fails a dated review placed outside its week.
- **(13) BUG, fixed · Go sequence** (finding 3): the standalone `strings.Builder` drill dropped (Om, Nov 6); G2 gets the loops and control part the Go strategy names (Boot.dev chapter 8, Learning Go chapter 4), +2.75 hours; the checker compares each Go row's chapter numbers in its text and its resource key against the declared Learning Go map.
- **(14) BUG, fixed · kubelet** (finding 4): K1's use step names the kube-system Pods and says where kubelet runs; same hours.
- **(15) BUG, fixed · Live week references** (finding 5, and more Claude found: the blind sets, the Gate A unseen set, the W58 refresh, Naukri's week, mock 2's week, the 1c note): each points to its row now, and the checker compares them with the map.
- **(16) GAP, Claude's own · The W6 harvest part** had left the map with the unused application hours; it moves forward (+1.25 hours) and the lane decision moves to the W8 close, Nov 29.
- **(17) Proposals:** 1 modified (the short-week order, the W7-W12 run sheet and the close's three lines), 2 modified (P1 +6 hours), 3 modified (E1 +7.5 hours and C1 +0.5), 4 accepted (0 hours), 5 accepted (15 minutes inside W8's harvest).

**v3.9 final (Nov 15 2026, after ChatGPT's 16:22 review of revision 2; approved by Om 19:10).** All text, 0 learner hours, dates unchanged. Note: `claude/plan-drafts/2026-11-15-v3.9-final-note.md`.

- **(18) BUG, fixed · Hiring dates** (finding 1): normal applications after Gate A (Jun 6 2027) and joining around August 2028 for an offer after Gate B (Apr 30 2028); the checker ties both to the gate dates.
- **(19) GAP, fixed · Slower-pace dates** (finding 2): labelled fixed-work illustrations, with the weekly close of each extra calendar week costed; the offer year is no longer derived from them; the Dec 6 re-forecast rule written out; coach research and plan rebuilds run outside Om's study block.
- **(20) BUG, fixed · A decision moves with its evidence** (finding 3): the lane decision targets Nov 29 and moves to the first close with both harvest parts done; the run sheet's proof column is the full-row case.
- **(21) IDEA, accepted · Ownership and early signals** (idea 4): the W8 ownership checkpoint's three lines; the four-line Gate A record.
- **(22) IDEA, accepted · Transfer check and F2** (idea 5): three facts on every full rep from MC2; Om's yes or no on F2 at the W8 close, its only addition the 1-hour debugger lesson.
- Boot.dev chapter 8 has six lessons (ChatGPT, checked again by Claude on Nov 15); its 1.25 hours stay provisional until the first sitting.
- Totals: 834.5 to 969 hours, 87 weeks, DSA 169.5. Gates Jun 6 2027 (W35), Apr 30 2028 (W82), May 28 2028 (W86).

**Checked and not added in v3.9:** moving the controller build to Phase 2 (Om, Nov 15: "no shrink allowed") · task-specific scoring bands (batch B10: the PASS, PARTIAL and FAIL rubrics already work per task, and a second scale invites disputes) · the CDP on-ramp (batch B7: stays a trigger, waiting for regular controller work at IBM) · the Helm IDEA (waits for the W7 close, Nov 22) · a research pipeline before the build (Om, Nov 15 13:14) · a list of AI skills for 2028 (researched at Gate B, section 11) · ChatGPT's CoachOps scripted gate (open, Om decides; v3.9 takes its visible preflight only).

**Rejected:** 8/10 pass bars on every checklist;""")
s13 = s13.replace("## 13. Change log: v3 to v3.8", "## 13. Change log: v3 to v3.9")
