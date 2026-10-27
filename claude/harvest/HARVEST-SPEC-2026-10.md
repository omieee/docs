# JD harvest, run 1: one spec for both coaches (v2)

**Written:** 2026-10-27 22:05 IST by Claude; **v2 at 22:20** after Om's 22:10 rules: 100 unique companies and up to 100 JDs per coach, no company shared, postings at most 3 months old, LinkedIn and Naukri kept as separate sheets, one Excel file per coach.
**Plan basis:** v3.8 section 8 (lanes a-d, international slice, lane-size check). This is the W6-W7 harvest's collection done early as coach work, off Om's clock. Nothing in the plan moves: Om marks his top 5 in W7 and the lane decision stays at the W7 close (Nov 22). Every posting is re-checked as live in W6 before any count is used.

## 1. Who does what (no company shared)

| Coach | Companies | JD target | Files |
| --- | --- | --- | --- |
| Claude | the 100 India-hiring companies in `claude/harvest/2026-10-27-companies-claude.csv` | up to 100 accepted India JDs | `claude/harvest/2026-10-27-claude.csv` and `.xlsx` |
| ChatGPT | its own 100 companies, **none in Claude's list**: about 50 hiring in India (Bengaluru, Hyderabad, Pune, remote-India) and about 50 hiring in the Netherlands, Ireland, Germany (English-working only), UAE and Saudi Arabia, about 10 per country | up to 100 accepted JDs | `chatgpt/harvest/2026-10-27-companies-chatgpt.csv`, `chatgpt/harvest/2026-10-27-chatgpt.csv` and `.xlsx` |

ChatGPT commits its company list first, before it searches, so both lists are visible. Om may change the split. A shortfall is a result, never padded.

## 2. Where postings come from, in this order

1. **The company's own career or ATS page** (Greenhouse, Lever, Ashby, SmartRecruiters, Workday, Eightfold, Phenom).
2. **Readable boards that mirror it** (for example Built In Bengaluru), with the employer page as `url` when it can be found.
3. **LinkedIn and Naukri, kept as separate sheets.** Claude's web tools are refused by both sites ("robots disallowed", tested Oct 27 22:12), so Claude does not read them and does not work around the block. Two routes instead: (a) a search result that shows a LinkedIn or Naukri posting is a *lead*: the coach finds the same job on the employer's page and records `source` as `LinkedIn lead` or `Naukri lead`; (b) Om collects LinkedIn-only and Naukri-only postings himself (section 6) and the coach classifies them, `source` = `Om LinkedIn` or `Om Naukri`. ChatGPT tests its own access first and reports what works.
4. **Wider internet** when a listed company has no matching live posting: other employers' pages and boards in the same lanes, still at most 3 months old, still no company from the other coach's list.

## 3. What counts as an accepted JD

- **Role identity (section 1):** Senior Backend Infrastructure, backend-heavy Platform, distributed control-plane or data-infrastructure platform software; building software is the main duty.
- **Level:** Senior, Staff, Lead, Principal or MTS, hands-on; experience asked fits 12 years.
- **Live and recent:** open on the day it is read, and posted on or after **2026-07-27** (3 months). An open posting with no posted date is kept with `posted` = unknown.
- **Search strings:** section 8's five lane strings; international adds section 8's title variants.
- **Not accepted** (to the Excluded sheet, one reason): DevOps, SRE or cloud operations duties; support-heavy; database administration; a language Om does not use is required (for example "Java required"); junior or manager-only; closed; older than 3 months; FAANG-tier (Google, Meta, Amazon, Apple, Netflix, Microsoft, and their units such as LinkedIn and GitHub; Om may change this list); IBM itself; a repost or mirror of a recorded job; unreadable.
- **No AI-infra search string for the counted sample;** it would inflate the share being measured. Optional: up to 5 such postings in a separate AI probe sheet, never counted.

## 4. Evidence rules

- Record only what the posting page shows. Never fill a field from a title, a search snippet or memory. `unknown` when the page does not say. Never invent a link, ID or date.
- One row per job; the same job seen on two sources is recorded once, with the other source in `notes`.
- Judgement fields (lane, build share, AI category) carry a short reason in `notes`.
- No AI-written interview banks, blogs or "top skills" articles as evidence.

## 5. Columns (CSV header exactly as below; the Excel file uses the same columns)

```
id,company_no,region,country,city,employer,title,req_id,url,source,retrieved,posted,status,work_summary,build_share,level,years_asked,langs_required,langs_alt_or_optional,skills_required,skills_preferred,lane,prod_history_screen,om_evidence,work_model,pay_stated,english_team,local_language,language_years_screen,interview_format,where_held,india_candidates,ai_infra,ai_terms,ai_req,helm,public_cloud,terraform,k8s_controllers,notes
```

| Column | Allowed values or format |
| --- | --- |
| `id` | `CL-001` to `CL-100` (Claude), `CG-001` to `CG-100` (ChatGPT) |
| `company_no` | the row in the coach's company list, or `web` for item 4 of section 2 |
| `region` | India, Europe, Gulf |
| `source` | career page, ATS, board, LinkedIn lead, Naukri lead, Om LinkedIn, Om Naukri |
| `retrieved`, `posted` | YYYY-MM-DD; `posted` may be unknown |
| `status` | open |
| `work_summary` | one line: the actual work |
| `build_share` | most, half, little |
| `langs_required` / `langs_alt_or_optional` | "Java required, Go helpful": Java in required, Go in optional |
| `skills_required` / `skills_preferred` | each tagged `(capability)` or `(product)`, separated by `;` |
| `lane` | a, b, c, d (section 8) |
| `prod_history_screen` | the years or ownership screened on, or none |
| `om_evidence` | from plan section 2 only, ending `(per plan s2, Om to confirm)`; none if no screen |
| `pay_stated` | as stated, else unknown |
| `english_team`, `local_language`, `language_years_screen`, `interview_format`, `where_held`, `india_candidates` | international only, as stated, else unknown; `india_candidates` is confirmed only when the page says so; India rows write n/a |
| `ai_infra` | none; app (LLM features, RAG or agents in the product); platform (GPU scheduling, model serving, inference routing or autoscaling on Kubernetes); engine (CUDA, C++ inference engine performance, kernels) |
| `ai_terms` | the AI terms the page names |
| `ai_req`, `helm`, `terraform`, `k8s_controllers` | required, preferred, none |
| `public_cloud` | for example `AWS required`, `any cloud preferred`, none |

Double-quote every CSV field; lists inside a field use `;`.

**Excel sheets (both coaches):** Companies (each listed company: searched date, postings read, accepted, result), JDs (accepted, all sources except LinkedIn and Naukri), LinkedIn (accepted, LinkedIn lead or Om LinkedIn), Naukri (accepted, Naukri lead or Om Naukri), Excluded (`id, employer, title, url, retrieved, reason`), AI probe (optional), Summary.

## 6. Om's part: LinkedIn and Naukri (optional, his call)

For jobs that exist only on LinkedIn or Naukri (often recruiter or Easy Apply posts): Om runs section 8's lane strings on each site with its date filter (LinkedIn "Past month", Naukri freshness 30 days), and for each matching job pastes the job link and the full description into one Google Doc per site (or into the chat in batches of 10). The coach classifies them into the LinkedIn and Naukri sheets. About 1.5-2 minutes a posting (estimate); this is the harvest time the plan already gives Om in W6 (2h) and W7 (2.5h).

## 7. When each coach is done

1. Validate: header matches, same field count in every row, no duplicate URL, no company from the other coach's list.
2. Commit CSV and Excel in batches (about every 25 companies), then one summary in your own outbox: accepted and excluded counts; per lane (India) and per country (international); how many name Go, Python, Kubernetes controllers, Helm, public cloud (AWS share), Terraform, a production-years screen; the `ai_infra` split with required vs preferred; the lane-size check (section 8: fewer than 20 India roles that fit and can plausibly meet the ₹42L fixed gate, or fewer than 10 international roles that fit, work in English and are open to a candidate in India, is a change-control trigger); countries under 3 qualifying postings flagged thin.
3. Claude only, plan content (section 3): refresh the Levels.fyi Bengaluru Senior pay snapshot, with its date.
4. Merge: Claude reads both CSVs with a script and posts one combined count table in `claude/outbox.md`, each share with its 95% range. Om reads it and marks his top 5 in W7.
5. No plan edit, no verdict, no lane decision by either coach. Om decides at the W7 close, Nov 22.
