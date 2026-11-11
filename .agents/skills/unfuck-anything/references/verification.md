# Verification, independence and anti-gaming

## Evidence hierarchy

An executed, reproducible test against a stated external contract is stronger than a passing mock-based unit test; a unit test is stronger than a code reading claim; a code reading claim is stronger than a design document assertion; an assertion is stronger than an agent's confidence. None is absolute. Any measurement needs its environment, revision, inputs, sample selection, and limitations.

Record the same information before and after a repair: pinned revision, exact command, exit code, relevant output or artifact, dependencies, environment, and failure cases. CI checks can be useful evidence only when their tested behavior matches the acceptance contract.

## Independent evaluation

The implementer must not be the only authority on correctness. When resources allow, use a separate agent or reviewer without access to the implementer's private rationale, provided the contract and evidence. The reviewer attempts to break the change and must be able to reject it. If independence is impossible, disclose that limit; do not imply a second opinion.

Promote a candidate only when it satisfies **all applicable** gates: reproducible defect or explicit justified improvement; stable contract; tests that would have failed before; positive and negative paths; preserved security and data behavior; no silenced errors; old/new comparison where needed; operational rollback; and clearly delimited change scope. For performance work, include output equivalence and repeatable baseline methodology.

Agent orchestration can use competition for *candidate generation* without rewarding PR count or mutually persuasive agents. Pin an immutable source revision and test fixture. Submit candidate patches to independent evaluation. Track false positives and regressions, not only approvals. A verifier must not alter the definition of success after seeing the candidate output.

## Deliberate adversarial questions

Would reverting the patch restore a broken behavior, or merely lose a fashionable abstraction? Could a test pass because the tested code is never called? Is coverage high because assertions are low-value? Did the change add compatibility shims that become permanent? Does the benchmark measure the same work? Are logs, retries, rates, auth, and failures visible? Are the model's “observations” really assumptions from a prompt? Are we changing a metric or the phenomenon it claims to represent?

## Stop / escalation conditions

Stop before changing real user data, removing controls, altering legal or regulatory representations, changing public API contracts without owner approval, force-pushing protected branches, increasing security risk, or running a non-reversible deployment. Record the blocker, cheapest safe next step, and required authorization. A blocked review with evidence is better than a fabricated success.

## Result labels

**Verified repair:** declared acceptance contract met by executed tests, independent checks where available, and no material known untested risk within the described scope.

**Partially verified:** some tests passed but important behavior, environment, or review remains untested.

**Blocked with evidence:** experiments indicate a cause but necessary access or approval is absent.

**No change justified:** alternatives explain the observation or proposed intervention provides no demonstrated improvement.

A single verification report is not a warranty for unexamined states, future changes, or every deployment environment.

## Mandatory check beyond the originating institution

For a contested empirical or technical claim, internal build logs, reviewers and GitHub CI are **supporting evidence, never the sole oracle**. Before reporting **independently verified**, require a decisive, externally inspectable procedure whose inputs, expectations and adjudication are not controlled solely by the claimant. The independent tester need not be excluded from every institution; they must be free to run or examine the test and reject the conclusion without the original authority's permission. Prefer controlled direct observation, independently derived invariants, independent implementations, new raw data, end-user outcomes, and comparable external reproductions. See `outside-verification.md`.

A published reproduction recipe is **externally reproducible**, not **externally replicated**. Passing a GitHub workflow or local test in a repository controlled by the author is *internal verification*, even if the workflow runs on externally hosted infrastructure. Hashing test artifacts establishes integrity, not correctness; a second source quoting the first is not independent corroboration.

The final report must separately state **claim support** (supported within scope / contradicted within scope / mixed / unresolved), **verification independence** (externally replicated / externally reproducible but not replicated / internal-only / unavailable), and **engineering release readiness** (verified repair / partially verified / blocked / no change). Do not combine them into a single ceremonial green status.

If sensitive or proprietary data prevent public reproduction, propose an ethical safe alternative or disclose the precise evidence gap. Do not bypass authorization, expose records, or make a claim of independent verification that has not occurred.