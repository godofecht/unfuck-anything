# Outside the network: a required audit lens, not an automatic verdict

The project's philosophical position is explained in [the root philosophy statement](../../../../PHILOSOPHY.md). This reference translates that position into explicit **tests** for architecture reviews and socio-technical system repair.

## The separation that matters

Do not conflate **empirical validity** (does it work), **institutional authorization** (who is permitted to act), **social recognition** (who is considered credible), **access** (who receives resources and a hearing), and **mutual obligation** (who actually helps whom and under what terms).

Each may be justified or unjustified independently. A working patch may still be unauthorized to deploy; an authorized design may still be broken; a rejected outsider proposal may be wrong; an accepted insider proposal may be wrong. Do not conclude any of these from social status alone.

## Trace two architectures

**Technical architecture:** Call/data graph, dependency graph, state, trust boundaries, failure modes, runtime behavior, deployment, observability, actual user outcomes.

**Recognition and access architecture:** Who defines acceptance criteria? Who can propose, review, test, merge, deploy, appeal, receive resources, and change policy? What evidence does each actor see? What behaviors receive credit, budget, status, access, promotions, or automated approval? What is required of an unrecognized contributor versus an established contributor?

Compare the two. A technical capability claim should be evaluated on a consistent contract regardless of the claimant's membership. A governance claim should be evaluated on its actual permissions and effects. Test whether improvements to measured output are improvements to user capability, rather than improvements to the institution's representation of itself.

## Questions to ask when gatekeeping may be the failure mechanism

1. What was the proposal's exact observable contract and what independent evidence was provided?
2. Were acceptance criteria stated before the identity or affiliation of the proposer became salient?
3. Do similar proposals receive similar review standards, response times, instrumentation, and opportunity to correct errors? Control for quality, risk, workload and project relevance.
4. Are standards requirements for security, maintenance, and compatibility genuinely enforced for *incumbent* code too?
5. Does a credential or introduction grant valid delegated trust, or replace technical examination where examination is feasible?
6. Can a newcomer reproduce the project's benchmarks, run tests, locate the decision-maker, and appeal an ambiguous rejection?
7. Who bears the unpaid evidence-production burden, and is it necessary for safety or simply a consequence of inaccessible infrastructure?
8. Which distinctions disappear when participants are classified as insider/outsider, expert/novice, legitimate/illegitimate? Would retaining a distinction improve predictions or decisions?
9. What evidence would show the suspected gate is fair or the outsider's proposed change is mistaken?
10. Is the actual bottleneck access, operational capacity, unclear ownership, tool availability, code quality, scope, or some combination?

Only describe **institutional gatekeeping** as a measured mechanism when there is evidence of exclusion conditions, asymmetric standards, or consistent barriers. Do not infer discriminatory motive, collusion, or intent without independent evidence.

## Differentiating experiments

**Blinded review:** Where feasible and permitted, compare equivalent patches without identity information, then inspect whether identity is associated with outcome after controlling for quality. Do not misrepresent author identity or violate community rules to create a blind test.

**Standards symmetry:** Take the criteria used to reject the outsider proposal and apply them to relevant accepted incumbent code under comparable constraints. Document exceptions and justification. A difference in outcome is not automatically unfair if risk or requirements differ.

**Reproduction under identical constraints:** Execute a proposal and its incumbent alternative with the same tests, hardware, data, failure cases, and security contract. If external conditions cannot be matched, explain why the comparison is limited.

**Decision trace:** Reconstruct decisions from accessible, authorized artifacts (review threads, issues, policy, CI, service level commitments). Distinguish missing review capacity from viewpoint disagreement and withheld access.

**Consequences over labels:** Inspect downstream user results, incident rates, support burdens, maintainability costs, and time to usable contribution rather than counting approvals, meetings, merges, or prestige signals.

**Disconfirmation:** Actively seek counterexamples: low-status contributors accepted on merit, well-connected proposals rejected on technical grounds, legitimate security requirements, and outsider proposals that do not survive independent tests.

## Applying Recognition Dynamics without pretending it proves itself

Represent a recognizer (review process, team, model, policy) as a rule that maps available evidence and history into a decision. Ask what it can observe, what distinctions it collapses, how its judgments change after contradiction, and whether a discarded distinction has predictive value. This is an analysis device—not a license to assign fabricated mental states to reviewers.

Do not equate a model's prediction of alignment with demonstrated downstream alignment. Do not label dissent misrecognition merely because it is dissent. Preserve unresolved alternatives and report what would settle them.

## An example: a working contribution the network ignores

Hypothetical evidence: an outsider provides a memory-safe fix with a replicable failing test. A maintainer refuses it with “not aligned with architecture,” but the architecture policy is undocumented. A nearly identical fix from a long-standing contributor is merged after receiving help with compatibility tests.

Possible causes: uneven familiarity with workflows, reviewer capacity, a real compatibility difference, social deference, or inconsistent standards. The agent reads both diffs and tests; checks compatibility and safety; reconstructs each review timeline; measures the differences; and requests an explicit policy where one is missing. If the outsider fix fails the contract, report that regardless of process asymmetry. If equivalent fixes meet identical criteria but are treated differently, report the observable difference and propose transparent criteria, reproducible tooling, and appealable review decisions.

**Never repair social exclusion by bypassing code ownership, exposing private records, fabricating credentials, or weakening a safety gate.** Repair the testability and accountability of the gate.

## Required report additions

For reviews where recognition/access materially affects outcomes, include an **access and recognition ledger** with actor role, authority, accessible evidence, criterion, decision, affected person or user, cost, and unknowns. Explain whether the failure is technical, procedural, reputational, resource-related, or not established. Report remedies that can be implemented without assuming access or authority the investigator does not possess.

## Escaping a gate's self-confirming measurement loop

When the same institution owns the gate, samples the evidence, defines success, and reports that it has succeeded, distinguish **authorization** from **independent correctness**. Write an outsider-verifiable claim whose test does not require network membership, private reviewer approval, or affiliation-based credibility. Use publicly runnable contract tests, independently derived invariants, anonymized affected-user outcomes, or a portable, consentful reproduction. A test must be ethical and lawful; a withheld sensitive dataset is not a license to expose it.

If only the gatekeeper can observe the relevant outcome, say **not independently verified**. Do not automatically infer a bad motive. Assess whether a properly anonymized test, published acceptance criterion, or genuinely independent auditor could open the process. The test should be equally able to contradict the outsider's proposed alternative.

Read `outside-verification.md` and `claim-correction.md`.