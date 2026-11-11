# Verification: [change / revision]

**Decision:** verified repair | partially verified | blocked with evidence | no change justified

## Contract and oracle
Where the acceptance criteria come from, who or what independently checks them, and which behaviors are intentionally changed.

## Executed checks
| Check | Base revision / result | Candidate revision / result | Command / environment | Limitations |
| --- | --- | --- | --- | --- |
| | | | | |

## Adversarial probes
Negative cases, authorization failures, data loss, race cases, correctness equivalence, metric gaming and visibility of errors.

## Evidence integrity
Changed tests, skipped checks, fixture rewrites, altered thresholds, and whether review was independent of implementation.

## Operational risk and rollback
Unverified conditions, owner approvals, migration risks, monitoring, exact rollback action when known.

## Final statement
What is actually better, how it was observed, what remains unknown, and whether the change is ready for promotion.

## Outsider verification gate

**Claim support:** supported within scope | contradicted within scope | mixed | unresolved

**Independence:** externally replicated | externally reproducible (not replicated) | internal-only | unavailable

Which decisive test can be reproduced by someone outside the claimant institution's test-and-approval pipeline? Who controlled inputs, expected outputs, instrumentation, test execution and adjudication? Record outside-run evidence separately from the internal CI result. If none is possible, report **not independently verified** and name the blocker. A hash or a GitHub badge does not validate the truth of its contents.