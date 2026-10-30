# Proposal validation

Run on 30 October 2026 against `omieee/docs` commit `495460458dedfa413739ba50ae4d4c275289098f`.

| Check | Observed result |
| --- | --- |
| Uploaded plan/checker versus fresh repository master | Both byte-identical |
| Approved v3.8 checker on its unchanged plan | PASS: 75 weeks, 834.5h, DSA 146h, campaign 72.5h |
| Existing negative mutation suite | 25/25 mutations rejected; clean original passes |
| New rule behaviour tests | 23 tests pass, including positive fixtures and negative cases |
| Draft checker on unchanged v3.8 | Expected FAIL on the four findings below |
| Proposed single-file patch | `git apply --check` passes; temporary patched checker returns the same four findings |
| Master plan and approved checker after validation | Hashes unchanged |
| A rebuilt v3.9 calendar | Not generated or validated; excluded by the proposal-only request |
| Om's runtime artifacts or understanding | No learner proof or verdict performed |

Expected stricter-checker findings:

1. CL3 starts in W51 before K6b finishes in W67. This is the new complete-local-system-before-cloud requirement in F2.
2. MC2 starts in W18 before the final 0.25h of L3 in W36. The existing checker has this dependency but loses the individual MC2 label when aggregating machine-coding hours.
3. CL3 is six entries of 1.5, 3, 3, 3, 1 and 0.5 hours. The content contract calls for four 3-hour sessions.
4. The never-cut line omits AWS/public cloud and Terraform. They already appear elsewhere as core; F1 makes that protection explicit.

The tests exercise removing an entire pillar from both tables, missing funding or schedule, zero funding, missing prerequisites, correct and reversed same-week order, prerequisites with a later unfinished part, cloud before local integration, fragmented/missing cloud sessions, missing/duplicate/reversed gates, core completion too late, malformed/duplicate rows, zero-hour and unparsed entries, and cloud protection wording.

These are plan-structure tests. They do not execute Go, Terraform, Kubernetes or PRCP. The patch does not mechanically verify the meaning of the agent/finalizer contracts, whether a lesson is suitable, or whether required integration tests actually ran. Those remain human review and runtime proof obligations.

The sample schedule used for new rule tests is a small synthetic dependency fixture, not a proposed week map. It is not passed off as a complete v3.9 plan.

Reproduce with:

```bash
python3 chatgpt/plan-drafts/v3.9-proposal/validate_proposal.py
```
