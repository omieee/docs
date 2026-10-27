# JD harvest, run 1: one spec for both coaches

**Written:** 2026-10-27 22:05 IST by Claude, at Om's request (22:03: "60 you and 60 ChatGPT, tonight").
**Plan basis:** v3.8 section 8 ("JD harvest in November", lanes a-d, international slice, lane-size check). This is the W6-W7 harvest's collection done early as coach work, off Om's clock. Nothing in the plan moves: Om reads the shortlist and marks his top 5 in W7, and the lane decision stays at the W7 close (Nov 22). Every posting is re-checked as live in W6 before any count is used.

## 1. Who does what (no overlap)

| Coach | Region | Target | Where it writes |
| --- | --- | --- | --- |
| Claude | India: Bengaluru, Hyderabad, Pune, remote-India | 60 accepted postings, aim for 15 per lane a-d where they exist | `claude/harvest/2026-10-27-india.csv` |
| ChatGPT | Netherlands, Ireland, Germany (English-working only), UAE, Saudi Arabia | 60 accepted postings, aim for 12 per country where they exist | `chatgpt/harvest/2026-10-27-international.csv` |

A shortfall is a result, never padded. Each coach writes only in its own folder (section 0).

## 2. What counts as an accepted posting

- **Role identity (section 1):** Senior Backend Infrastructure, backend-heavy Platform, distributed control-plane or data-infrastructure platform software. Building software is the main duty.
- **Level:** Senior, Staff, Lead, Principal or MTS, hands-on; experience asked fits 12 years (for example 5+, 8+, 8-12, 10-15).
- **Live:** open on the day you read it.
- **Not accepted** (goes to the excluded file with one reason): DevOps, SRE or cloud operations duties; support-heavy; database administration; a language Om does not use is required (for example "Java required"); junior or manager-only; closed; Phase 1 excludes FAANG-tier employers (Google, Meta, Amazon, Apple, Netflix, Microsoft; Om may change this list); a mirror or repost of a posting already recorded.

## 3. Where to look and how to search

- **Search strings:** the five lane strings in section 8, word for word. International: the same strings without the Indian city filter, plus the title variants in section 8 ("Senior Software Engineer, Backend and Infrastructure" in Europe, "Senior Backend Engineer" in the Gulf).
- **India sources:** employer career pages and their ATS pages (Greenhouse, Lever, Ashby, SmartRecruiters, Workday), LinkedIn Jobs public pages, Instahyre, Cutshort, Hirist, Naukri, Built In Bengaluru.
- **International sources:** LinkedIn Jobs, employer career pages, Built In and Built In Dublin, Bayt and GulfTalent for the Gulf.
- **Canonical link:** the employer's own career or ATS page when it exists; an aggregator link only when nothing else exists, written in `notes`.
- **No AI-infra search string in the counted sample.** The point is to measure what share of Om's own lanes asks for AI infrastructure; searching for it would inflate the share. Optional: up to 5 postings found with an AI-infra search go in a separate `-ai-probe.csv`, never counted in the shares.

## 4. Evidence rules (both coaches)

- Record only what the posting page shows. If the body does not load, try the employer's own page, then a LinkedIn public page. Still unreadable: put it in the excluded file as "unread" and do not count it. Never fill a field from the title, a search snippet or memory.
- `unknown` when the page does not say. Never invent a requisition ID, date or link.
- One line per posting; reposts and mirrors once.
- Judgement fields (lane, build share, AI category) carry a short reason in `notes`.
- No AI-written interview banks, blogs or "top skills" articles as evidence.

## 5. Columns (CSV, header line exactly as below)

Double-quote every field. Lists inside a field are separated by `;`. India rows write `n/a` in the international-only columns.

```
id,region,country,city,employer,title,req_id,url,retrieved,posted,status,work_summary,build_share,level,years_asked,langs_required,langs_alt_or_optional,skills_required,skills_preferred,lane,prod_history_screen,om_evidence,work_model,pay_stated,english_team,local_language,language_years_screen,interview_format,where_held,india_candidates,ai_infra,ai_terms,ai_req,helm,public_cloud,terraform,k8s_controllers,notes
```

| Column | Allowed values or format |
| --- | --- |
| `id` | `IN-01` to `IN-60` (Claude), `INT-01` to `INT-60` (ChatGPT) |
| `region` | India, Europe, Gulf |
| `retrieved`, `posted` | YYYY-MM-DD; `posted` may be unknown |
| `status` | open (only open rows are accepted) |
| `work_summary` | one line: the actual work |
| `build_share` | most, half, little |
| `langs_required` / `langs_alt_or_optional` | "Java required, Go helpful" puts Java in required and Go in optional |
| `skills_required` / `skills_preferred` | each tagged `(capability)` or `(product)`, for example `Kubernetes controllers (capability); Helm (product)` |
| `lane` | a, b, c, d (section 8 definitions) |
| `prod_history_screen` | the years or ownership the posting screens on, or none |
| `om_evidence` | Om's honest evidence for that screen, from plan section 2 only, ending `(per plan s2, Om to confirm)`; none if no screen |
| `pay_stated` | as stated, else unknown |
| `english_team`, `local_language`, `language_years_screen`, `interview_format` | as stated, else unknown (international only) |
| `where_held` | in-country only, remote in region, relocation offered, unknown (international only) |
| `india_candidates` | confirmed, unknown (international only; confirmed only when the page says so) |
| `ai_infra` | none; app (LLM features, RAG or agents in the product); platform (GPU scheduling, model serving platform, inference routing or autoscaling on Kubernetes); engine (CUDA, C++ inference engine performance, kernels) |
| `ai_terms` | the AI terms the page names, for example `GPU scheduling; vLLM; llm-d; KServe; Triton; Ray` |
| `ai_req`, `helm`, `terraform`, `k8s_controllers` | required, preferred, none |
| `public_cloud` | for example `AWS required` or `any cloud preferred` or none |

The excluded file (`-excluded.csv`) has only: `id,employer,title,url,retrieved,reason`.

## 6. When each coach is done

1. Validate the file: the header matches, every row has the same number of fields, no duplicate URL.
2. Commit the CSVs, then one summary in your own outbox: rows accepted and excluded; counts per lane (India) or per country (international); how many name Go, Python, Kubernetes controllers, Helm, public cloud (AWS share), Terraform, a production-years screen; `ai_infra` split (none, app, platform, engine) with required vs preferred; lane-size check (section 8: fewer than 20 India roles that fit and can plausibly meet the ₹42L fixed gate, or fewer than 10 international roles that fit, work in English and are open to a candidate in India, is a change-control trigger); countries under 3 qualifying postings flagged thin.
3. Claude only, plan content (section 3): refresh the Levels.fyi Bengaluru Senior pay snapshot, with the date.
4. Merge: Claude reads both files with a script, posts one combined count table in `claude/outbox.md`, and states each share with its 95% range, so a small count is never read as a market fact. Om reads it and marks his top 5 in W7.
5. No plan edit, no verdict, no lane decision by either coach. Om decides at the W7 close, Nov 22.
