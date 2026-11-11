# Repair plan: [bounded fault or improvement]

## Evidence-backed problem
Observed defect and affected contract, with evidence IDs and any alternate causes.

## Scope
Concrete files / interfaces / workflows changed, untouched boundaries, compatibility constraints, permission and data constraints.

## Repair alternatives
| Approach | Expected capability gain | Risk / uncertainty | Reversibility | Why selected or rejected |
| --- | --- | --- | --- | --- |
| No change / gather more evidence | | | | |
| Minimal bounded change | | | | |
| Larger replacement | | | | |

## Baseline and regression contract
Exactly reproducible behavior to characterize before implementation, including negative paths and relevant performance constraints.

## Implementation stages and stop conditions
Each stage has an independent pass/fail check. Define escalation for data migration, auth, rollout, or changed public behavior.

## Rollback
Revert steps, state/data compatibility and monitoring. Do not claim a rollback is safe unless verified or explicitly marked untested.
