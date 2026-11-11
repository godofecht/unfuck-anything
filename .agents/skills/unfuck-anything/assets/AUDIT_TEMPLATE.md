# Architecture audit: [system / revision]

## Scope and authorization
System, owner, environment, permitted actions, prohibited actions, non-negotiable contracts:

## Actual capability contract
User-visible input/output; operational, security, accessibility and persistence constraints; acceptance criteria. Separate documented facts from provisional assumptions.

## Evidence ledger
| ID | Grade (O/I/H) | Claim | Source (file/line, command, run, incident record) | Alternative / limitation |
| --- | --- | --- | --- | --- |
| E1 | O | | | |

## Actual topology
Entry points, call/data/effect flows, storage, trust boundaries, deployment boundaries, ownership and feedback loops. Explicitly state unknowns.

## Recognition and access architecture (when relevant)
Who defines acceptance criteria? Who can propose, review, reproduce, merge, deploy, appeal, and allocate resources? What evidence is accessible to each actor? Are equivalent claims evaluated by comparable standards? Distinguish technical validity, permission, social reputation, and exclusion without inferring motive.

## Causal hypotheses
| Hypothesis | Supporting evidence | Disconfirming evidence | Discriminator / experiment | Status |
| --- | --- | --- | --- | --- |
| H1 | | | | untested |

## Baseline
Revision, environment, exact commands, exit codes, measured outcomes, sample/fixture definitions, known failures, confidence limits.

## Ranked opportunities
Candidate changes including **no change** and **instrument first**; expected outcome, risks, dependencies, reversibility. Do not assign made-up precision.

## Decision
Audit-only, intervention selected, blocked, or no change justified, with rationale.
