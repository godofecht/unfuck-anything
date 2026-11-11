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

## Transfer to other systems

For software, evidence is code, traces, CI, tests and runtime behavior. For organizations, evidence is process execution, defined metrics, anonymized case outcomes, authority and incentives. For agent ecosystems, evidence is immutable inputs, candidate diffs, independent tests, and acceptance/rejection history. The reasoning process stays the same; the evidence type and authorization boundaries change.
