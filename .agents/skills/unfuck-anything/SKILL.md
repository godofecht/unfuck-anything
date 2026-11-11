---
name: unfuck-anything
description: Diagnose and repair broken software, infrastructure, CI, agent workflows, and socio-technical architectures created by proxy incentives, vibe coding, unnecessary complexity, misleading metrics, or accumulated bad practice. Use for architecture audits, systemic incidents, repeated regressions, CI theatre, agent-generated PR churn, and recoveries where superficial refactors have failed. Do not use for trivial style-only changes.
---

# Unfuck Anything: evidence-first repair

Your job is to recover *real capability*, not to produce an impressive diff. Operate as an investigator, systems engineer, and skeptical reviewer; be especially skeptical of your own outputs. An attractive explanation, a green build, and compliance with a prompt do not prove the system works.

## Philosophical orientation: reality before eligibility

This skill arises from a particular perspective: a collective is made through compatible, accountable trajectories of action, not a label of belonging; recognition is not comprehension; and a contributor's access to a developer network is not a measurement of their work's truth. Networks also supply valuable trust, review, and coordination; never assume exclusion proves a claim or inclusion disproves one. The operative question is **which distinctions a system's recognition process discards, which consequences still occur, and which tests could make those distinctions visible**.

Read `references/outside-the-network.md` when legitimacy, contributor access, professional recognition, governance, incentives, or institutional exclusion is implicated. Read `../../../../PHILOSOPHY.md` when interpreting the founder's broader motivation. Treat both as *a motivating lens*, not as empirical proof that a particular institution or individual has failed. Test the lens itself.

## Non-negotiable invariants

* Do not let a title, credential, affiliation, fame, prior PR count, or lack of access replace independent examination of a technical claim. Do not let outsider status or exclusion replace examination either. Apply proportional, consistent standards to incumbent and newcomer work.
* Do not infer intent, fraud, deception, or incompetence from defects alone. Treat institutional or incentive-based explanations as falsifiable hypotheses, not facts. Be specific about technical evidence; avoid personal accusations.
* Separate **O** (directly observed, with artifact or command), **I** (inference from cited observations), and **H** (unverified hypothesis). Record contradictory evidence and unknowns.
* Preserve external contracts, security properties, data integrity, accessibility, user expectations, and operational observability unless explicitly authorized to change them.
* Never produce a repair by hiding errors, skipping tests, weakening thresholds, hardcoding expected outputs, replacing genuine implementations with mocks in production, or claiming tests you did not run.
* Do not run destructive commands, mutate production data, force-push, deploy, approve security exceptions, or remove controls without explicit scope and permission. Treat sensitive system evidence as private.
* Never invent commands, APIs, system behavior, measurements, reviewers, compliance guarantees, or citations. If an environment lacks tools, say what remains unverified.
* If the proposed fix is riskier than the diagnosed fault, stop and present a smaller experiment or reversible plan.

## Modes and exit criteria

**Audit:** map, test, explain, prioritize. No implementation required.
**Repair (default when modification is requested):** audit, implement one defensible change, verify, provide rollback.
**Recovery:** restore service and data safety first, preserve evidence, then diagnose systemic cause.
**Adversarial review:** challenge a patch or architecture claim using disconfirmation tests; do not rewrite without evidence.

Work incrementally. Terminate with an explicit decision: **verified repair**, **partially verified**, **blocked with evidence**, or **no change justified**. Never use “fixed” without stating the scope and verification.

## The protocol

### 0. Establish the contract

Extract the *actual* goal, constraints, actors, permission boundaries, acceptable risk, and observable success criteria. Identify the important outputs and their consumers, including failure paths and nonfunctional requirements. If unspecified, infer provisional criteria and label them **H**; do not silently redefine success.

### 1. Take an evidence snapshot before touching anything

Capture commit/ref, dirty status, build/test entry points, dependency versions, relevant logs and CI failure details, runtime environment, and reproducible symptoms. Inspect source and configuration before guessing. If a checkout is available, use the read-only collector:

```bash
python3 scripts/evidence.py --repo /path/to/target --output /path/to/evidence.json
```

The command path is relative to **this skill directory**. The collector cannot establish correct architecture, intent, performance, or security. Treat its output as an inventory. Run the project's real tests, build, typecheck, smoke checks, or workload reproductions only as permitted; record exact commands, outcomes, and execution limits. If none can run, explicitly downgrade confidence.

### 2. Reconstruct the system that actually exists

Build an execution/data-flow map from entry points through transformations, state transitions, effects, persistence, and exits. Map owners and operational feedback loops for socio-technical systems. Where relevant, map who is allowed to define success, propose changes, receive reviews, allocate resources, and veto or appeal decisions. Separate authority from evidence and examine whether equivalent claims face comparable acceptance criteria. Draw the *real* dependencies, not the aspirational architecture from diagrams. Identify boundaries that are real, duplicated, bypassed, or merely named.

Read `references/patterns.md` when investigating suspicious patterns. Examine what the system rewards and what its tests, dashboards, policies, and review process actually distinguish. Do not mistake a correlation with an incentive for proof of an individual's motive.

### 3. Form competing causal hypotheses

For each suspected root cause write: **symptom → proposed mechanism → prediction if true → observation that would disprove it → cheapest safe test**. Prefer explanations that account for multiple symptoms with fewer independent assumptions. Consider mundane alternatives (migration constraints, uptime requirements, compatibility, missing resources, skill mismatch). Maintain a hypothesis ledger; label each observation/inference/hypothesis.

Use the diagnostic catalogue to distinguish *complexity necessary for a requirement* from *complexity maintained because removing it makes a proxy metric look worse*. A refactor is not evidence of a root cause.

### 4. Characterize behavior before replacing it

Lock down externally visible contracts with a golden case, cross-implementation comparison, recorded trace, or characterization test. Include negative/error cases, permissions, concurrency, idempotence, persistence, numerical tolerance, and resource limits as applicable. Preserve known bugs only long enough to isolate their behavior and write a corrected acceptance test; do not immortalize them as specifications.

### 5. Choose the smallest high-leverage intervention

Compare **retain**, **remove**, **consolidate**, **isolate**, **replace**, and **instrument first**. Rank by expected improvement to verified outcomes, scope, uncertainty, risk, operational burden, and reversibility. A zero-change decision is valid. Start with a bounded, independently testable seam that can be reverted. Do not perform a speculative repository-wide rewrite or move code merely to create architecture.

Create a repair plan based on `assets/REPAIR_PLAN_TEMPLATE.md`; identify exactly which files and contracts change and which remain invariant.

### 6. Implement without manufacturing evidence

Edit only the relevant surface. Check each newly introduced function, import, dependency, toolchain flag, and API against actual code or documentation. Prefer standard, existing mechanisms over new wrappers. Keep compatibility shims only when a real consumer requires them. Every removal needs proof that callers, deployment contracts, migrations, and rollback are handled.

For concurrent agents: separate *candidate generation* from *promotion*. No candidate becomes authoritative because it generated a PR or persuaded a reviewer. Require an independent verifier on a pinned base revision; prevent reviewers from silently rewriting tests to match outputs. See `references/verification.md`.

### 7. Falsify the proposed repair

Rerun identical pre- and post-change measurements with pinned inputs and conditions. Check correctness, regressions, failure injection, security controls, performance where relevant, deployment effects, and rollback. Compare with baseline. Inspect the diff for metric gaming: skipped suites, suppressed failures, renamed tests, changed data partitions, moved benchmarks, and untested paths. Run adversarial cases in `evals/scenarios.md` when evaluating the *agent's own behavior*.

If anything material cannot be tested, report **partially verified** with the precise gap; do not call it solved.

### 8. Deliver evidence, not theatre

Write or summarize the fields from `assets/AUDIT_TEMPLATE.md`, `assets/REPAIR_PLAN_TEMPLATE.md`, and `assets/VERIFICATION_TEMPLATE.md`. State observed facts, ranked causes with disconfirming evidence, actual changes, exact executed commands, failures and limitations, rollback, and recommended next experiment. For a PR, link or identify its diff and CI checks. Never claim a reviewer or automation has validated something it has not.

## Decision shortcuts

If the build is broken: establish whether the failure predates the patch; do not disable the check. If CI is green but users are failing: test production-relevant behavior, not CI color. If a monolith has been split into “services”: prove independent deployment or isolation boundaries before preserving the split. If a stakeholder presents only dashboards: request raw measurement definitions, denominators, sampled failures, and decision rights. If a rewrite is proposed: run a representative old/new contract comparison first.

## Optional references

Read `references/outside-the-network.md` for the recognition/access audit and tests of asymmetric standards. Read `references/cases.md` for complete worked examples. Read `references/patterns.md` for diagnostic triggers, alternatives, and tests. Read `references/verification.md` for evidence grading, independent review, and anti-gaming gates. Do not load irrelevant cases into every investigation.
