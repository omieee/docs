# v3.9 proposal, 30 October 2026

Start with [PROPOSAL.md](PROPOSAL.md). It contains five proposed changes, the four-skill minimum, evidence limits, exact wording, time costs and conditional date effects.

This directory is a proposal package. No v3.9 master is included, and nothing under `plan/` was changed.

| File | Purpose |
| --- | --- |
| [PROPOSAL.md](PROPOSAL.md) | Proposed v3.8 to v3.9 changes for Om's decision |
| [check_plan.py.diff](check_plan.py.diff) | Proposed single-file checker patch; not applied |
| [check_plan_proposed.py](check_plan_proposed.py) | Run the approved checker and proposed additional rules |
| [proposed_rules.py](proposed_rules.py) | The additional structural checks |
| [test_proposed_rules.py](test_proposed_rules.py) | 23 behaviour tests, including deliberate schedule defects |
| [validate_proposal.py](validate_proposal.py) | Reproduce baseline, negative tests, prototype and patch checks |
| [VALIDATION.md](VALIDATION.md) | Results and the limits of what was verified |

From the `omieee/docs` root:

```bash
python3 chatgpt/plan-drafts/v3.9-proposal/validate_proposal.py
```

The validation command should exit 0. It expects the proposal's stricter checker to reject the unchanged v3.8 schedule on four identified findings.

To inspect those failures directly:

```bash
python3 chatgpt/plan-drafts/v3.9-proposal/check_plan_proposed.py plan/Phase1_Master_Plan_v3.8.md
```

That command should exit 1. Do not weaken the proposed rules or alter the master simply to turn this into a PASS. A future approved rebuild must repair the schedule first. The prototype's default base checker is the repository's `plan/check_plan.py`; `--base-checker` can supply its path when running elsewhere.

To inspect the proposed patch without applying it:

```bash
git apply --check chatgpt/plan-drafts/v3.9-proposal/check_plan.py.diff
```

The patch embeds the same additional rules inside the existing single-file checker. `validate_proposal.py` verifies that equivalence and runs the patched checker in a temporary location. A source-hash mismatch means the base changed and the proposal needs rebasing.
