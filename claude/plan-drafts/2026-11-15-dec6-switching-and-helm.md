# Dec 6 re-forecast drafts: switching cost and Helm (Claude, Nov 15 2026, 21:55 IST)

Status: new recommendations, not approved. v3.9 is frozen until Dec 6 and neither item is a section 9 trigger. Om decides at Dec 6; the other coach verifies the rebuild (section 0, plan versions). Source: Om's message of Nov 15, 21:45 IST, at the W6 close.

## 1. GAP: switching cost and warm-ups are not measured

- **What.** (a) From W7, every lane session's log line carries three things, written by the coach from message times, with no extra work for Om: the warm-up as held or slipped and what slipped (the s6.12 rule, unchanged, still no score); restart minutes, from the session's start to Om's first new step after the warm-up; and the days since that lane's last session. (b) From W7, the coach orders each week as one lane per day after that day's DSA slot. Two lanes on one day only when they share a codebase (P1 and L1 both work in PRCP). The row, its hours and the dated reviews do not change. (c) At Dec 6, Om decides with the W7-W9 records, about 15 to 20 lane sessions. If restart minutes are often above 10 (twice the warm-up box), or if slips gather in lanes that sat idle for 7 days or more, the coach drafts a structural change: fewer lanes a week, or two-week lane blocks kept inside the continuity limits. Otherwise the mix stays.
- **Why.** Om, Nov 15, 21:45: too many tracks compete for attention, and a correctly ordered 969-hour plan can still waste time if every session restarts a different mental model; the funded warm-ups may help, but nobody has measured whether they work. The W7 row has 9 items across 8 subjects in 12 hours. The warm-up rule records only held or slipped. Since Oct 29 there are 3 warm-up records in all, so the 34.25-hour warm-up cost decided on Nov 15 had no evidence on its effect.
- **Evidence.** The W7 row (section 14). The W6 close: 1 of 5 lane sessions opened with a warm-up. The section 6.12 warm-up rule.
- **Counterpoint, kept honest.** Spacing a lane across days is deliberate: the continuity rule and row 38's interleaving research say it helps memory. The suspected cost is switching inside one day, not spacing across days. So the test groups lanes by day; it does not drop lanes.
- **Time cost.** 0 learner hours. Coach logging only.
- **Removed or date moved.** Nothing. No date moves.
- **Risk reduced.** Paying 34.25 hours for warm-ups, plus an unknown switching cost, with no evidence either way.

## 2. IDEA: Helm in Phase 1, in two parts, both on KodeKloud (Mumshad)

- **What.** Change section 6.3's "Not in Phase 1: Helm chart authoring."
  - **H-a, using Helm.** The CKA course's own "Helm Basics (2025 Updates)" section, taken where the course order puts it, after the troubleshooting section (Om's Nov 13 course-order rule). Its 11 lectures, about 50 minutes of video, cover what Helm is, installing it, the Helm 2 vs 3 note, components, charts, the basics, customising chart parameters, and lifecycle management. Use on kind (code): install one public chart, change its values, upgrade it, roll it back, and read the release history.
  - **H-b, writing a chart.** KodeKloud "Helm for Beginners" (Mumshad, about 2.25 hours of video with labs), the chart-anatomy part: writing a chart, pipelines, conditionals, `with`, `range`, named templates and hooks. Then package PRCP (API, Postgres, agent) as one chart after K6a, which writes PRCP's own manifests. The work covers `helm lint` and `helm template`; install, upgrade and rollback on kind; values for two environments; and one diagnosed values or RBAC mismatch. The chart templates PRCP's own Postgres manifest, with no Bitnami chart (F4, Oct 27).
  - **On top of the videos.** The course videos may predate Helm 4 (Nov 2025), so these three F4 facts are taught on top. A new Helm 4 install defaults to server-side apply. A release made by Helm 3 keeps client-side three-way merge. helm-diff compares release manifests by default, so a hand edit made with `kubectl` shows only with `--three-way-merge`.
- **Why.** Om, Nov 15, 21:45: Helm should be in, after a good Kubernetes base, and only on Mumshad's course; he has the whole KodeKloud package for a year. F4 (Oct 27) also says Helm is the delivery path at CDP, which is not verified here.
- **Evidence.**
  - **Market.** 8 of the 73 accepted postings in Claude's Oct 27 sheet name Helm (about 11%). In lane (b), Go and Kubernetes platform, it is 7 of 31 (about 23%): 6 list it as required, 2 as preferred. ChatGPT's 8 rows name it 0 times.
  - **Caveat.** None of these rows has been re-checked live yet; that happens in the W7 harvest part 1. All the counts are below the 35-45% bars used for Terraform and AWS (section 6.11). The market alone does not carry H-b. Om's reasons are the course he has already paid for and his CDP work.
  - **Resources checked Nov 15.** The KodeKloud CKA course page lists Helm Basics as added on Jan 27 2025. The Helm for Beginners page shows Mumshad, 2.25 hours of video, 4 modules and labs.
- **Time cost (provisional, section 5 new-tool rates of 1.5-2x).**
  - **H-a:** about 2 to 2.5 hours (the video at 1.5x is about 1.25 hours; the lab and use step about 1 hour).
  - **H-b:** about 9 to 13 hours (the videos at 1.5x 2 to 3 hours, the PRCP chart 3 to 6, the upgrade and rollback lab 1 to 1.5, the diagnosed mismatch 0.5 to 1, proof and interview 1, setup and rewatching 1).
  - **Total:** about 11 to 15.5 hours, close to ChatGPT's 12 to 16 for F4.
- **Removed or date moved.** Nothing is removed (Om, Nov 15: no shrink). H-a sits in the K track at the course's place. H-b comes after K6a (from W37, Jun 2027), which is after Gate A and before Gate B. At 12 hours a week Gate B moves about 1 to 1.5 weeks, from Apr 30 2028 to about May 7-14 2028, unless open hours absorb it. The checker sets the exact date at rebuild.
- **Risk reduced.** A platform interview, or a CDP task, that needs a chart Om has never written.
- **Open, for Om.** The end date of the KodeKloud package. K6a starts in W37 (Jun 2027), K6b in W57 (Nov 2027) and OP1 in W60 (Nov 2027). If the package ends before Om's last KodeKloud lesson, the renewal is a cost the plan must name, or those lessons need another source.
