# Correct claims, not merely their implementations

An agent that can refactor code but cannot challenge bad premises may perfectly implement nonsense. When a user asks to challenge a widely endorsed idea, institutional push, expert claim, architecture mandate, or plausible AI-generated explanation, switch to **claim correction mode**. Do not require the user to present institutional credentials before investigating.

The target is a **proposition and its consequences**, not a person or category of people. Never treat official recognition as proof, but never treat rejection of authority as proof either. Be ready to find that the allegedly nonsensical idea is correct, or that the user's own alternative fails.

## The correction protocol

### 1. Capture the exact claim

Quote or faithfully transcribe the claim with its original scope and conditions. Identify its actual proponent, source, version/date, affected users, and whether it is a requirement, prediction, causal explanation, value judgment, or an ambiguous mixture. Do not attack a stronger statement than the source made; avoid straw men.

### 2. Decompose the argument

Make a claim ledger:

| Item | Question |
| --- | --- |
| Premise | What observations or axioms does the argument assume? |
| Mechanism | By what causal pathway should it work? |
| Prediction | What changes should be observable, for whom and when? |
| Scope | Which conditions must hold? What are counterexamples? |
| Incentive | Which outcome is rewarded or counted? Who defines it? |
| Decision authority | Who can impose the rule? Who can dispute the evidence? |
| Alternative | What other mechanism fits the available facts? |

A phrase such as “best practice,” “enterprise grade,” “AI-native,” “industry standard,” “safe by design,” or “everyone agrees” is **not** an independent premise. Demand the mechanism and the claimed consequence.

### 3. Separate four issues

**Logical:** Does the conclusion follow from the premises? Expose circular reasoning, undefined terms, category errors and conflations.

**Empirical:** Are the premises true in the relevant domain, and does the mechanism predict real observations? Seek disconfirming examples, negative controls, replication, and uncertainty.

**Normative:** Who bears costs and receives benefits? Is a preference being presented as a law of nature? A value choice may deserve debate, not a faux-scientific verdict.

**Governance:** Who is authorized to make the decision, and is that authorization being confused with factual correctness? You can challenge a technical rationale without denying legitimate legal or organizational power.

### 4. Form competing explanations

State at least one serious rival, including legitimate reasons the institutional practice may exist (legacy compatibility, compliance, system safety, operational continuity, scarce reviewer time). For each, write the **cheapest lawful external test that would discriminate it from the primary claim** and what result would change your mind. Consider negative evidence, selection bias, confounders, data provenance and reproducibility.

### 5. Get the acceptance criterion outside the claimant

Use `outside-verification.md`. A **decisive** result must not rely solely on the institution's own grades, prestige, metrics, guidelines, internal CI, citations, or controlled example set. Prefer affected user outcomes, independent invariants, direct runtime measurements, freely executable reproductions and controlled comparisons. If a claim is inherently value-laden, separate the checkable factual predictions from the value choice.

An external source is not automatically independent; a source that copies the original institution is a derivative assertion. Identify whether the observation, expected result, method, and adjudicator have distinct control. If independence is not obtainable, explicitly state **not independently verified**.

### 6. Correct the proposition

For a disproven universal claim, state the counterexample and narrow the surviving domain. For a partially supported claim, quantify the conditional evidence and limits. For an untestable slogan, replace it with a measurable question; do not declare it logically false just because it is vague. For a justified claim, acknowledge that and explicitly retract the initial suspicion.

Correct the documentation, requirement, PR justification, benchmark, acceptance criteria, or implementation **only where authorized**. A rhetorical correction is not evidence of a repaired system. Preserve approvals, public API and data obligations unless separately authorized.

### 7. Audit the correction itself

Ask a skeptical outsider to reconstruct and try to refute it. Check that proposed evidence is independent rather than reproduced from the same institutional pipeline. Report all failed experiments, unknowns, changed hypotheses, and who controlled the test. Do not pretend a narrative is an experiment.

## Response standard

Write **original claim → status (supported/contradicted/mixed/unresolved) → evidence → rival explanation → independent replication instructions → corrected claim → consequences and residual unknowns**. Cite original sources as evidence *of what was claimed*, not as proof that the claim was true.

Use `../assets/CLAIM_CORRECTION_TEMPLATE.md`. When the contention involves access, eligibility, review criteria, or developer networks, also read `outside-the-network.md`. For examples, see `cases.md`; for evaluation traps, see the repository's `evals/scenarios.md`.

## Anti-patterns to reject

“Published, therefore true.” “Senior engineer approved it, therefore correct.” “The test passes because the fixture was rewritten.” “That outsider is unfamiliar, therefore the method is invalid.” “The outsider is excluded, therefore the institution must be wrong.” “The legal rule is inconvenient, therefore doesn't apply.” “Everyone I know agrees, therefore consensus is independent replication.” “If the tool produced it, the result has been verified.” All are arguments to investigate, not verdicts.
