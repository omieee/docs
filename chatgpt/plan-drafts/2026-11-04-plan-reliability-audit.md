# Phase 1 plan reliability audit, 2026-11-04

**Status:** Advisory review requested by Om. No learner verdict, no re-score, no change to approved v3.8. Owner of this review: ChatGPT. Timestamp checked live at 10:56 IST.

## Evidence checked

- Fresh metadata reads for all six repositories: `omieee/docs`, `dsa-python`, `learning-go-sandbox`, `learning-python-sandbox`, `lld-patterns`, `platform-reliability-control-plane`. This is **not** a fresh test run of all six repositories and makes no assertion about their runtime correctness.
- Fresh reads: `phase1-log.md`, both coach logs, both outboxes, `plan/README.md`, the W5 row and section 0 of approved `plan/Phase1_Master_Plan_v3.8.md`, the Nov 15 batch, the Nov 3 Go appendix, the taught-Go record, and Claude's `coach-errors-2026-10-19-to-11-04.md`.
- Verified supplied plan SHA-256 `25bb309e79a610f2...` and checker SHA-256 `6c55bf0713278013...` against `plan/README.md`. Checker result on original: PASS, 75 weeks, 834.5h, DSA 146h, campaign 72.5h, seven fragmentation warnings.
- **Negative reproduction:** copied the plan to a temporary local file and exchanged the entire `**MC2** 2.5h: Rep 2...` entry in W18 with the `**MC5** 2.5h: Rep 5...` entry in W40, leaving weekly hours and labels valid. The checker still returned **PASS**, despite MC5 occurring before L4 teaching and the declared dependency `(MC5,L4)`. No repository file or approved plan was modified.

## Accountable incident count, not an exhaustive independent audit

- Shared weekly closes W3 (Oct 19-25): Claude 11 coach errors; ChatGPT 3.
- W4 (Oct 26-Nov 1): Claude 9; ChatGPT 1.
- Claude's newly written incident ledger lists 25 numbered lines from Oct 19-Nov 4 and ~346 minutes lost, including a **240-minute aggregate Go-loss entry** that contains incidents #19-21. Do not treat all 25 lines as independent additive incidents, or double-charge those component errors. One other incident has unmeasured time. These are logged claims from the coaches and Om, not independently stopwatch-audited numbers.
- ChatGPT's own recorded errors include a resource presented as checked without same-day verification, MC1 over-teaching and time-box overrun, a wrong capacity calculation in an audit, and an unverified K1 resource recommendation. Transferring work to ChatGPT is not a zero-error guarantee.

## Five findings, with source and disposition

1. **BUG: course/prerequisite mismatch (existing Nov 15 batch B12).** Approved v3.8 teaches G3 pointer receivers before G4 pointers. Boot.dev Ch 9 lessons 11-13 included interfaces, functions as arguments and runes beyond the taught baseline. This was a realised failure, not a hypothetical one; Nov 2-3 Go incident is recorded by Claude and Om. **Remedy:** honor Om's approved Nov 3 Go strategy and ordered appendix, check every lesson against `claude/taught/go.md` before assignment, and move the G3 pointer teaching ahead of first receiver use when rebuilding. **Cost/trade:** the appendix revises measured Go cost to 6.25h, funded only as logged; reconcile in Nov 15 batch, not silently today. **Risk:** wasted study hours and false negative assessments.

2. **BUG: machine-coding prerequisite checks inert (existing Oct 30 v3.9 proposal/B8).** Checker line 84 collapses `MC0`-`MC8` to `MC`; dependency checks line 101-103 look for `MC2` or `MC5` in `first` and therefore skip them. Full-entry-swap reproduction passed validation. `L3` has a tail in W36 after MC2 W18, while its proof references rep 2, so simply requiring full L3 closure before MC2 would be circular. **Remedy:** retain both individual MC identities and MC aggregate budget; distinguish teaching-prerequisites from post-rep proof/closure. Add a negative fixture that swaps MC2 and MC5 and MUST FAIL. **Cost/trade:** checker and schedule repair is coach work; any shifted learner time requires a named displacement or revised gate date in Nov 15 batch. **Risk:** scripts falsely certify readiness/order.

3. **BUG: CL3 AWS execution contradicts atomic-lab rule (existing Oct 30 B8).** Section 6.11 requires four 3h apply/smoke/destroy labs; map splits 12h across W51/52/54/55/57/58 at 1.5/3/3/3/1/0.5h. `K6b`, the Go agent on local kind, is W63/66/67, after cloud lab W51-58. **Remedy:** schedule four indivisible three-hour labs and specify the exact smoke-test contract for the partial system deployed before K6b, or move K6b first. **Cost/trade:** plan must name displaced hours or dates; no unconditional earlier gate-date promise. **Risk:** impossible setup/teardown expectations or superficial cloud proof.

4. **GAP: validation tests words and hours, not external lesson prerequisites or observed runnable proof.** `TERMS` in `check_plan.py` covers a small static string list, not course lesson contents or `taught/go.md`. `Use in...` regex finds text but cannot verify the code or that a learner independently understood it; the plan itself acknowledges this. **Remedy:** a *human-visible preflight* before every lesson: fetch current canonical files, check Om's known setup, current W5+approved appendix, taught list, open the exact resource and inspect prerequisites, run the sample, ask what is known, then teach one concept. If evidence cannot be fetched, write UNVERIFIED and do not test the untaught concept. **Cost/trade:** coach-side preparation, not an unbudgeted learner unit. **Risk:** repeated 'looks checked' mistakes.

5. **BUG/process inconsistency: two versions of session governance (existing batch B1).** v3.8 s0 safeguard 6 and s6.6 #11 retain a hard 1.5x stop and daily 45m DSA. Om's Oct 29 request, recorded by both coaches, asks for flow-aware boxes and about one hour DSA on a two-hour day when productive. Claude says it applies the newer operating rule now; ChatGPT Oct 30 outbox notes the master still controls until an approved amendment is committed. **Remedy:** one explicit written approved override for the interim, or continue the master rule with Om-authorised extensions, then reconcile s0/s6.6 at Nov 15. No spontaneous track switch with spare minutes. **Cost/trade:** text/protocol change; no new learner hours. **Risk:** inconsistent coaching experience and another context switch like Nov 4.

## Reliability policy for ChatGPT, not a guarantee of error-free work

- Begin each unit with a short evidence preflight specifying checked plan/week/appendix/taught list/setup/resource; mark unchecked items rather than assert.
- Never give a proof before the concept is taught; never change tracks in the middle of a session without Om's direction.
- Run the code/CI on the exact commit where possible; otherwise label runtime evidence UNVERIFIED. Green CI alone never passes a unit without Om's explanation.
- Separate **plan validation**, **runtime verification**, and **learner understanding**; they are three different proofs.
- For plan changes, use five findings max, a negative checker test per claimed invariant, one-in/one-out hours or explicit date move, and Om's approval. The Nov 15 freeze and existing batch govern; this report does not reopen settled decisions.

**Conclusion:** Cannot guarantee zero errors. Can make checks visible, introduce regression tests for known errors, and be accountable for each repeat. No new curriculum work assigned by this audit.
