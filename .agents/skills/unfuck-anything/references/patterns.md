# Diagnostic patterns: observations, alternative explanations, falsifiers

These are *investigation prompts*, not labels to apply to people. A defect is not proof of incentives or intent.

| Pattern | Observable lead | Alternative explanation | Discriminating test | Candidate repair |
| --- | --- | --- | --- | --- |
| Vibe-coded architecture | Abstractions exist with no distinct contract, lifecycle or consumer | Framework constraint, plugin ABI, future migration | Trace callers, deployments and changes over several releases | Collapse redundant layers only after contract characterization |
| PR-count optimization | High PR volume; recurring regressions and overlapping changes | Deliberately small patches or broad team work | Correlate reverted changes, incident rate, useful behavior delivered | Reward verified outcomes and independent review, not merged PR totals |
| CI theatre | Green checks coexist with failing user journeys | Environment-specific failure | Reproduce journey; inspect assertions, exit codes, skipped suites | Restore failing assertion and representative integration test |
| Test laundering | New snapshot/golden data generated from changed code without independent oracle | Intended behavior change | Compare against stable external contract or prior known-good behavior | Freeze independent oracle; separately approve changes |
| Green-by-suppression | Broad exception catch, ignored errors, disabled alerts | Legitimate graceful degradation | Inject controlled failures and inspect end-to-end signal | Surface failure with bounded retry and explicit degraded state |
| Microservice costume | Multiple processes but shared database, release train, and state | Intermediate decomposition | Independently deploy or failure-isolate a component | Recombine or establish genuine contracts, ownership, and isolation |
| Wrapper accumulation | Every function forwards to another layer without new invariant | ABI or cross-platform isolation | Enumerate unique invariants and boundary consumers | Delete only wrappers that contribute no measurable property |
| Dashboard substitution | Targets green while user-facing outcomes degrade | Lagging metric, cohort shift | Trace numerator, denominator, provenance, exclusions, raw cases | Align metrics to independently observed capability |
| Governance smokescreen | Review signatures but no accountable acceptance or enforcement | Legitimate division of authority | Test who can veto unsafe release and what evidence they receive | Bind approval to objective gates and clear decision rights |
| Architecture astronautics | New orchestration layer introduced before a failing workload is characterized | Scale or regulatory need | Benchmark actual workload and failure mode with/without layer | Prefer existing mechanisms when sufficient |
| Performance theatre | Reported speedup depends on cache, dataset, hardware, or correctness change | Legitimate workload specialization | Pin input, hardware, output equivalence, warmup and statistics | Publish reproducible methodology and truthful boundaries |
| Rewrite compulsion | Everything renamed/replaced simultaneously | Unavoidable platform migration | Characterize a bounded interface and compare old/new | Strangler seam, feature flags, rollback, incremental retirement |
| Ownership diffusion | Every incident crosses teams but no one can resolve it | Truly shared infrastructure | Map escalation paths and actual authority to change | Assign end-to-end responsibility with escalation |
| Agent self-certification | Implementer authored all tests and declared success | No separate review capacity | Run independent adversarial tests against pinned contract | Split generator/verifier and enforce rejection criteria |
| Dependency mirage | A tool or dependency is present but its feature is never executed | Pre-adoption scaffolding | Trace runtime path and compare observable outcomes | Remove or actually exercise feature, as warranted |
| Recognition substituted for evidence | Credentials or network familiarity decide whether a test is even examined | Limited maintainer time, trust and risk requirements | Compare same-contract work, review criteria and counterexamples | Transparent reproducible acceptance and bounded evidence intake |
| Eligibility loop | Contributor must gain membership before their defect evidence can be evaluated | Anti-abuse, security or regulated access needs | Separate rights to report, validate, merge and deploy | Permit safe evidence triage without bypassing ownership controls |
| Asymmetric acceptance standards | Incumbent and newcomer proposals face different undocumented requirements | Real differences in scope, risk, or support burden | Apply written criteria to both with comparable inputs | Publish criteria, reproduce outcomes, allow appeal |
| Security-by-documentation | Policy described but not enforced | Control may exist upstream | Negative authorization tests and audit-trail inspection | Enforce at trust boundary, preserve logs |

## Hypothesis ledger

For each major issue write an evidence identifier and confidence. A useful entry is:

```text
H2: Releases are green because integration tests never exercise authorization failure.
Observed: CI job runs unit tests only (file:path and run URL).
Prediction: A token without permission reaches the protected route in the test environment.
Disconfirmation: Explicit end-to-end 403 assertion in a separately executed integration suite.
Experiment: Issue unauthorized request against isolated test environment.
Outcome: NOT YET RUN. Intent: UNKNOWN.
```

**Do not use subjective scores to replace a missing test.** Counted layers, line counts, tickets, meeting hours, and confidence percentages are not outcomes by themselves. Read the source, trace real execution, and seek evidence that could overturn your favorite diagnosis.

## Challenging unsupported ideas and institutional prescriptions

| Pattern | Claim worth testing | Outside-controlled discriminator | Honest correction |
| --- | --- | --- | --- |
| Authority laundering | “Committee X endorsed the architecture, so it's technically correct” | Extract the actual claim; run independently specified workload and failure tests | Approval is governance evidence, not a performance or correctness result |
| Consensus as oracle | “Everyone competent agrees with this best practice” | Compare alternatives against a common, third-party inspectable contract | State domain where practice actually outperforms, if any |
| Institutional evidence enclosure | “Only approved members can see whether this method works” | Create anonymized or synthetic independent oracle, bounded external test, or disclose irreducible access limits | Not independently verified if no external check is available |
| Policy marketed as physical necessity | “Our preferred workflow is the only safe architecture” | Construct lawful, comparable alternative and measure safety invariants | Separate mandatory policy from claims of unique technical necessity |
| Premise laundering | “AI-native architecture makes this automatically scalable” | Define throughput/latency/failure targets and independently measure a real workload | Replace slogan with conditional quantified claims |
| Citation echo chamber | “Dozens of papers verify it” but they repeat one dataset or theoretical assumption | Trace evidence lineage; seek independent data, derivation, or falsifying experiment | Count independent observations, not repetitions |
| Correcting by contrarianism | “An institution supports it, therefore it must be bad” | Test incumbent and alternative under the same external contract | Preserve the supported result even when institution-backed |
| Certification confusion | “Certified” is used to assert outcomes beyond the certification scope | Inspect actual certificate scope and externally reproduce relevant observable claim | Report certified scope and untested claims separately |

Refer to `claim-correction.md` for exact corrections and `outside-verification.md` for evidence independence. These are diagnostic prompts, **not** accusations of misconduct.