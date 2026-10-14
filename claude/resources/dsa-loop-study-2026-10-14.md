# DSA in senior India interview loops, Oct 2024 to Oct 2026

Built 2026-10-14 by Claude at Om's request: "100+ reports, weighted toward 8+ years, every row with its link, round types and a yes/no for DSA."
Full data, one row per loop with its link: `dsa-loop-study-2026-10-14.xlsx` (same folder). Replaces the 14-loop quick study (`dsa-loop-evidence-2026-10-14.md`) as the evidence base.

## Filters

- India location or India-only employer; senior title (Senior, SDE3, Lead, Staff, Principal, SMTS, LMTS, IC3+) or 6+ yrs; software engineering roles only.
- Interview or post date Oct 2024 to Oct 2026.
- Sources: LeetCode Discuss (72), Taro (24), Glassdoor (8). Each row links to its page.
- Partial loops (candidate stopped early) kept only if DSA was seen, so the honest number is complete loops.
- Same author and same company counted once; 107 rows, 104 counted. 134 links excluded, each with a reason (sheet "Excluded").
- Spot-check: 8 random rows re-read against the source with a neutral prompt; DSA yes/no matched 8 of 8.

## Results (share = yes / (yes + no); unclear left out)

| Slice | Loops | DSA yes | DSA no | Unclear | Share |
| --- | --- | --- | --- | --- | --- |
| All counted | 104 | 90 | 8 | 6 | 92% |
| Complete loops only | 84 | 70 | 8 | 6 | 90% |
| YoE 8+ | 13 | 11 | 2 | 0 | 85% |
| YoE 6-7 | 28 | 26 | 2 | 0 | 93% |
| Year 2026 | 25 | 22 | 2 | 1 | 92% |
| Year 2026, complete | 22 | 19 | 2 | 1 | 90% |
| LeetCode only | 72 | 65 | 7 | 0 | 90% |
| Taro + Glassdoor only | 32 | 25 | 1 | 6 | 96% |

Round mix in the 78 complete loops with a clear answer (387 rounds):

| Round | Share of rounds | Loops with it |
| --- | --- | --- |
| DSA (incl. online test) | 32% | 90% |
| HLD | 19% | 81% |
| HM / behavioral | 15% | 65% |
| Project deep-dive | 11% | 55% |
| LLD | 9% | 41% |
| Lang / CS fundamentals | 6% | 29% |
| Machine coding | 5% | 23% |
| AI concepts | 2% | 8% |
| Code review / debug | 1% | 6% |
| AI-assisted coding | 1% | 3% |

DSA difficulty where stated: medium 41, mixed 18, easy 7, hard 7.

No-DSA loops (8): Meesho SDE3, Razorpay Lead SE (2025), Target L5, Groww SDE3, Postman Senior, Oracle Health IC4, JioHotstar Senior SDE, Intuit Senior SE (craft round). Meesho and Razorpay also have loops in the set that did include DSA.

## What it says

1. DSA is in about 9 of 10 senior loops in India, at 8+ years too, and 2026 is no lower than 2024-25. "No DSA for 6 months" is not supported.
2. DSA is about a third of the rounds, design (HLD + LLD + machine coding) another third, people and project rounds the rest. "DSA only for 6 months" would skip HLD, which shows up in 81% of loops.
3. The plan gives DSA 21% of hours (117.5 of 558) against 32% of rounds, so the plan is not overweighting DSA. The Oct 14 problem was daily time per session (about 4 hours on one problem), which is an execution fix.
4. The bar is LeetCode medium. Hard is rare.
5. AI rounds are new but small: 2 AI-assisted coding rounds (Intuit Senior SE 2025, Razorpay Lead SE Jun 2026 agentic coding) and 7 loops with an AI-concept round or block (Intuit, Oracle SMTS agentic orchestrator design, Oracle Health MCP tools, Walmart Staff AI tool usage, Deliveroo, Rakuten). Both of the AI coding loops also had DSA or a coding screen. So far AI rounds are added on top of DSA, not replacing it.

## Limits

- Self-reported posts; LeetCode writers may lean DSA, but the Taro + Glassdoor slice is higher, not lower.
- Only 13 rows state 8+ yrs; YoE is missing in 47. The 8+ figure has a wide error range.
- Undated LeetCode posts were dated from the post number, only to check the window.
