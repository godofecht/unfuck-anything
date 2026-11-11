# Worked investigations

Each case is illustrative: the diagnosis follows from the *hypothetical observed evidence*, not from a label or an assumed villain.

## Case A — “microservices” that are a distributed monolith

**Claim:** Separating one service into twelve independently named packages improved reliability and team autonomy.

**Observed:** Every package writes the same database tables, deployment runs as one workflow, and changing a shared schema requires an atomic release. A user-facing request traverses seven synchronous calls with no retries or partial-failure contract.

**Competing explanations:** (H1) excessive service boundaries are adding failure surfaces; (H2) shared state is transitional while a genuine migration is underway; (H3) the split is required by isolation or ownership constraints.

**Discriminator:** Trace one request, record call graph and p95 latency in a controlled environment, examine independently deployed releases, and deliberately fail one service in staging. Check whether there's a documented cutover plan.

**Repair:** Characterize response and authorization behavior first; collapse purely forwarding hops behind a stable interface or establish real ownership and data boundaries. Use a reversible traffic switch. Verify responses, failure propagation, latency, and rollback under the same workload. **Do not** remove a process boundary that genuinely protects a security domain.

## Case B — all green CI while users encounter broken authentication

**Claim:** “CI passes; the incident cannot be in our code.”

**Observed:** The CI workflow runs lint and a mocked unit suite. A route test replaces the authorization middleware with a stub that always allows the request. An end-to-end unauthorized call returns 200 instead of 403 in staging.

**Competing explanations:** A configuration-only deployment bug or a bypass in the middleware stack.

**Discriminator:** Inspect the full route chain and deploy configuration; run unauthorized request tests in the real staging stack, then execute the same test on the last known-good revision.

**Repair:** Restore authorization at the trust boundary and keep a real negative integration assertion. Verify permitted users, denied users, audit logs, and failure response. Do not “fix” CI by suppressing the failing test or rewriting expected status to 200.

## Case C — a swarm of agents maximizes merged PR count

**Claim:** Fifteen agents collectively produced hundreds of changes and therefore accelerated progress.

**Observed:** A high fraction of patches revert one another, test failures get attributed to unrelated branches, and several agents edit the same fixtures to match their changed outputs. Review bandwidth falls while verified feature throughput stagnates.

**Competing explanations:** Genuine rapid experimentation; missing ownership and stable test contracts; a reward proxy favoring PRs over outcomes.

**Discriminator:** Analyze merge-to-revert/incident ratios, measure time to verified acceptance, run candidates against an immutable independent suite, and sample whether merged code is invoked in the product.

**Repair:** Make outputs *candidates*. Pin base revision and acceptance fixtures; evaluate isolated candidates independently; serialize conflicting writes; reject changes that rewrite the oracle. Reward independently verified behavior with low regressions. An orchestrator should choose interaction patterns and promotion gates, not assume the largest model is correct.

## Case D — institutional dashboard looks healthy while users lose access

**Claim:** A programme's compliance dashboard reports 100% completion.

**Observed:** The numerator counts forms closed, not users who regained access. “Successful” tickets include automatic closures after no reply; a sampled cohort still cannot perform the service. Decision rights to change the underlying workflow are split among offices.

**Competing explanations:** The dashboard measures a narrower legitimate process; the user experience is lagging; closure counts have been optimized independently of outcomes. **No individual intent is established.**

**Discriminator:** Obtain metric definitions, denominators and exclusions, anonymized case sampling, appeals and reopen counts, and the chain of authority for genuine resolution. Compare outcomes before and after policy or workflow changes.

**Repair:** Add independent user-success and reopened-case measures, document exclusions, enable escalation, and assign accountable authority. Audit the definition of “complete.” Do not accuse staff or remove required controls without proof and authorization.

## Case E — benchmark speedup without equivalent work

**Claim:** A new compiler pass delivers a 4x speedup.

**Observed:** The comparison changed input sizes, omits cold-start latency, and drops bounds checking in one variant. Neither numerical equivalence nor failure handling was tested.

**Competing explanations:** Legitimate optimization for a narrower workload or misleading comparison.

**Discriminator:** Pin compiler/toolchain, architecture, seeds, workload, warmups, correctness tolerance, and measured distributions. Test error cases and count excluded observations.

**Repair:** Report separate comparable measurements with output equivalence. Restore required checks or explicitly specify changed guarantees. Do not market a speedup as general when only one narrowed contract improved.

## Case F — an attractive full rewrite of a legacy system

**Claim:** Thousands of lines of older code can be replaced with an elegant hundred-line implementation.

**Observed:** The old implementation also handles malformed inputs, network interruptions, accessibility, versioned persistence, and a legacy consumer that is absent from the proposed rewrite.

**Competing explanations:** Genuine dead code or complexity required by a non-obvious contract.

**Discriminator:** Run a differential test corpus against old and new code including error paths, edge cases, and historical data. Identify callers through runtime traces and release documentation.

**Repair:** Replace one bounded seam after parity passes; retain legacy compatibility where demonstrated; remove obsolete code after migration evidence. A reduction in line count without preserved behavior is regression, not simplification.

## Case G — “we added observability” but errors now disappear

**Claim:** An added tracing layer eliminates noisy failures.

**Observed:** A broad catch returns empty output and emits a success metric; operators see lower error rates while upstream jobs silently lose data.

**Competing explanations:** Intended best-effort semantics with missing contract or accidental exception swallowing.

**Discriminator:** Inject a known failure in staging; correlate result, persisted records, trace, retry, and alert.

**Repair:** Make failure state explicit, preserve trace and downstream contract, and test partial results and retry idempotence. The outcome measure is recovered data correctness, not merely fewer alarms.

## Case H — an outsider's implementation is dismissed without a reproducible criterion

**Claim:** A proposed implementation is “not how serious developers do things.”

**Observed (hypothetical):** The submission has a reproducible correctness test and a measured latency improvement under a specified workload. Review notes invoke architectural style without a stated invariant; an accepted implementation with a familiar author uses a similar mechanism. No one has yet evaluated compatibility, operational burden, or the negative path for either proposal.

**Competing explanations:** (H1) an undocumented but real maintenance or security requirement; (H2) an incomplete comparison; (H3) familiarity and review access influence decisions independently of capability; (H4) a legitimate difference in scope or risk.

**Discriminator:** Compare the proposals against the same pinned contract and data, including negative cases; inspect their callers and release obligations; identify exact review criteria and exceptions; inspect accessible review chronology without guessing anyone's internal motive. Test counterexamples.

**Repair:** Make the contract and criteria explicit; add reproducible tests and equitable review instructions; accept or reject *each implementation* based on demonstrated outcomes and documented constraints. Neither outsider status nor insider reputation supplies a pass.

## Case I — the eligibility queue outlives the capability it claims to protect

**Claim:** A contributor must acquire a recognized badge or join a committee before their reproducible bug report can be triaged.

**Observed (hypothetical):** A user-facing defect remains open, two reproducible reports are redirected into an onboarding queue, and a maintainer cannot point to a security or governance reason why *triage* (rather than merge authority) requires the badge.

**Competing explanations:** Abuse prevention, scarce reviewer time, regulated approval for deployments, an opaque policy, or a gate that conflates evidence evaluation with permission to change production.

**Discriminator:** Separate rights to report, reproduce, review, merge, and deploy. Audit policy and moderation constraints, review turnaround, and the failure's consequences. Determine whether a trusted contributor can reproduce the report without granting any additional permissions to its author.

**Repair:** Enable evidence intake and reproducibility checks without granting unauthorized write access; keep code ownership and deployment approvals intact. Make criteria, appeal route, and response expectations transparent. If abuse risks justify gating, design a bounded alternative intake path.

## Transfer to other systems

For software, evidence is code, traces, CI, tests and runtime behavior. For organizations, evidence is process execution, defined metrics, anonymized case outcomes, authority and incentives. For agent ecosystems, evidence is immutable inputs, candidate diffs, independent tests, and acceptance/rejection history. The reasoning process stays the same; the evidence type and authorization boundaries change.

## Case J — “clean architecture” as an unfalsifiable mandate

**Claim:** Every module must implement five wrapper layers because this is “industry best practice.”

**Hypothetical observation:** Two layers only forward calls and carry no isolated dependency, lifecycle, invariant or real consumer; the mandate adds maintenance work. A legacy plugin ABI might still require the layer in one target.

**Outside-the-network test:** Pin public API and ABI contracts. Build a minimal implementation with and without the allegedly necessary wrappers using independently specified integration tests, plugin-loading checks and change-impact tasks. Include the ABI-constrained platform as a negative control.

**Correction:** “These wrappers are not necessary for the checked targets and acceptance contract; the ABI adapter remains required for target Y.” Do not extrapolate from one workload to every architecture.

## Case K — a reputable research claim exceeds its data

**Claim:** A published technique “always beats the baseline,” accompanied by a sponsor-selected benchmark.

**Hypothetical observation:** The reported improvement uses a subset with one data regime; the error bars and negative cases are missing. Independent reimplementation has not occurred.

**Outside-the-network test:** Freeze claim scope, retrieve lawful raw data where available, implement a baseline independently, preregister holdout selection and tolerance, and compare equal compute and failure cases. If underlying data are inaccessible, reproduce on independently generated data and report that this tests generalization, *not* the original figures.

**Correction:** “Under the published settings the approach is reported to improve the selected metric; it has not yet demonstrated a universal advantage.” Do not label the publication false until a relevant contradictory test has been run.

## Case L — an organizational policy presented as unavoidable engineering truth

**Claim:** Only officially affiliated developers can produce safe changes, because external contributors cannot understand the system.

**Hypothetical observation:** A policy restricts merge permissions for real security reasons, while a reproducible external bug report is rejected before technical triage. Policy authority is being used to defend a broader, testable claim about competence.

**Outside-the-network test:** Keep protected deployment and merge permissions. Invite independent reproducibility of the bug with sanitized inputs. Compare accepted and rejected patch correctness under a stable external contract, not contributor identity. Measure review effort and security outcomes separately.

**Correction:** “Production write access remains restricted, but reproducible external evidence can be evaluated safely. The premise that affiliation determines technical correctness is unestablished.” Institutional permission remains binding where applicable; technical truth is a separate question.

## Case M — a compelling contrarian claim is wrong

**Claim:** A longstanding institution-backed validation rule is “obvious nonsense” and should be removed.

**Hypothetical observation:** Local happy-path tests pass without the rule, but malformed or adversarial requests can cross a trust boundary.

**Outside-the-network test:** On an isolated test stack, generate malicious inputs and compare protected versus unprotected variants against a security property independently of the incumbent team's approval. Do not attack live services.

**Correction:** “The rule protects this threat model; removing it violates the stated security contract.” Explicitly retract the anti-institutional suspicion and keep the control.