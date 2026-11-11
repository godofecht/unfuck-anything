# Verification outside the claimant's authority

**Default: seek a decisive test whose execution, observations, and acceptance criterion are not controlled solely by the institution, vendor, expert, author, maintainer, team, or agent making the claim.** The purpose is *epistemic independence*, not a geographical ban on universities, standards bodies, libraries, labs, or institutions as useful sources and instruments.

An institutional approval can authorize deployment. It is **not a substitute** for empirical verification. A reproducible result can establish a technical property. It does **not automatically authorize** deploying software, accessing private information, or disregarding legal or safety requirements. Keep the two questions separate.

## Required outsider-verification gate

Before reporting a contested empirical or technical claim **independently verified**, obtain **at least one decisive check** that an appropriately equipped person who does not work for or belong to the claimant organization can evaluate without privileged membership, hidden fixtures, a personal relationship, a private dashboard, or a permission to disagree. If the claim can be tested locally, prefer an offline, externally inspectable method.

The verifier needs a stated property, accessible input or procedure, raw output or observable behavior, an independently justified expectation, and a disconfirmation threshold declared *before* inspecting the candidate result. The claimant can provide the artifact; the claimant must not be the sole source of the answer key, measurement selection, grading rubric, and outcome adjudication.

**If outside verification is impossible**, say **not independently verified** and specify which material, access, instrument, cost, or ethical constraint blocks it. Internal CI, social agreement, peer review, citation count, credentials, funding approval, or an AI's confident interpretation do not close this gap. Do not invent an external witness or copy an institution's assertions into a supposedly independent conclusion.

An outsider test can fail too. Independence addresses control and correlated bias; it does not guarantee a good instrument, representative sample, or accurate reasoning. Replicate with heterogeneous methods when feasible and disclose conflicts.

## Design a check that can escape the approval loop

| Claim category | Independent or externally observable check | What does NOT suffice |
| --- | --- | --- |
| Software correctness | Executable minimal reproduction with own input/expected behavior, negative tests, traceable code path and environment | Author-written green unit suite alone |
| Architecture quality | Same user workload and failure budget on old/new topology, actual dependency/deployment trace, rollback validation | Framework label or architecture diagram |
| Performance/scaling | Fixed hardware/toolchain, seed, data, equal semantics; raw timing and counterexamples; alternative profiler | Sponsor-selected chart or incomparable benchmark |
| Research hypothesis | Independent derivation, preregistered discriminating prediction, raw data or re-measurement, baseline and negative controls | Prestigious journal, citation count, or paraphrasing the abstract |
| Institutional outcome | Consentful independent sample of affected outcomes, accessible service completion, denominator and exclusion audit | The institution's own completion dashboard |
| “Standard practice” | Extract testable requirement and reproduce consequence with and without it | “Industry consensus,” title, committee vote |
| Safety or compliance | Independently inspect applicable authoritative text and practical control behavior; obtain qualified review where necessary | Invented legal permission or unsupported certification |
| Policy or value choice | Expose assumptions, decision rights, trade-offs and affected parties; test factual predictions separately | Pretending preferences can be proven by a benchmark |

A legal requirement has a legally authoritative source; independent analysis cannot repeal that authority. It **can** check whether a quoted requirement exists and whether a claimed technical consequence follows. Where specialist testing is needed, do not pretend a casual DIY check is equivalent.

## Five-part verifier packet

For each material claim, publish an appropriately redacted packet with:

1. **Claim and domain:** Exact proposition, scope, provenance and version; factual vs normative components; what would count as an exception.
2. **Predictions:** Competing explanations, falsifiable predictions, expected failure evidence, and tests selected before seeing outcomes.
3. **Protocol:** Reproducible inputs or lawful sampling design, independent oracle or invariant, controls, negative cases, environment, randomness/seeds, and measurement uncertainty.
4. **Evidence:** Raw outputs or hashes/locations for sensitive artifacts; command line, revisions, toolchain, log and honest account of who executed it. Hashes prove integrity, **not truth**.
5. **Judgment:** Supported within scope, contradicted within scope, mixed, or unresolved; distinction between externally replicated and only internally observed; precise corrected claim.

An outside reviewer must be able to reject the claim **without requesting that the claimant redefine the success criteria**. Where a clean-room copy cannot be shared because of confidentiality, security, personal data, paywalls, or cost, describe the minimum safe independent test, limitations, and access route; never expose secrets to make the packet public.

## Operational sequence

Freeze the claim and competing expectations. Obtain first-hand observations instead of institutional summaries where authorized. Reimplement a small oracle (e.g., conservation law, numerical identity, API contract, independent ground truth, direct user outcome) if possible. Select adversarial cases likely to separate rival hypotheses. Execute the check outside the originating success-reporting pipeline; pin inputs, revisions, dependencies, and record failed runs as well as passes. Compare to a same-condition baseline, then invite disconfirmation by a reviewer with no incentive to preserve the conclusion. Only then make the smallest scoped correction.

**Provenance independence:** A second LLM quoting the same institutional page is not an independent source. Several papers citing one original experiment are not independent replications. Multiple dashboards reading one database are not multiple measurements. A test administered by the claimant and a reviewer who cannot inspect its oracle is not independently graded.

**Where the network refuses to evaluate:** Keep a portable, reproducible artifact and a plainly falsifiable statement so others can test it without insider review. Do not circumvent access controls or misrepresent credentials.

## Public correction language

Prefer: “The claim that X always holds is contradicted for inputs Y by procedure Z; under conditions A the narrower claim B remains consistent with the evidence.” Or: “This is an institutional requirement, not an empirical consequence. Its technical benefits remain unverified by an outside-controlled test.”

Avoid: “Everyone knows X is bullshit,” “the institution is lying,” or “the outsider must be right.” Precision makes a correction harder to dismiss and easier to reproduce.

For full claim handling, read `claim-correction.md`. For reporting, use `../assets/CLAIM_CORRECTION_TEMPLATE.md`.
