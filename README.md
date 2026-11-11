# unfuck-anything

**Repair systems, not appearances.** A portable Agent Skill for evidence-first architectural diagnosis and bounded repair. It works with codebases, CI pipelines, agent swarms, data systems, and socio-technical processes.

The premise: if teams or agents are rewarded for commits, PRs, green dashboards, complexity, conformity, or speed rather than demonstrated outcomes, the architecture can optimize those proxies while losing the capability it was supposed to provide. That is a hypothesis to test, not an accusation to assume.

## What it does

Invoking **unfuck-anything** gives an agent a protocol to reconstruct what a system actually does, identify its failure mechanisms, establish a baseline, compare repair options, make the smallest justified changes, and independently verify the result. It explicitly forbids passing off formatting, renamed abstractions, suppressed tests, and presentation metrics as repairs.

The skill is compatible with the [Agent Skills specification](https://agentskills.io/specification). The canonical skill is at [`.agents/skills/unfuck-anything/SKILL.md`](.agents/skills/unfuck-anything/SKILL.md). It contains a read-only, Python-standard-library evidence collection script, diagnostic reference material, worked cases, and report templates.

## Installation

For Codex or another agent that reads project skills in `.agents/skills`, copy the entire `.agents/skills/unfuck-anything` directory into the target repository's `.agents/skills/` directory. For Claude Code, copy it into `.claude/skills/unfuck-anything/`. For GitHub Copilot, copy it into `.github/skills/unfuck-anything/`. Client support and discovery rules differ; installing the directory is not proof that the agent activated the skill.

To audit the **current** repository from the checked-out skill source:

```bash
python3 .agents/skills/unfuck-anything/scripts/evidence.py --repo . --output audit-evidence.json
python3 -m unittest discover -s tests -v
```

For skill activation, explicitly instruct the agent: **"Use the unfuck-anything skill. Audit this repository, collect evidence, and fix the highest-leverage verified architectural failure without changing observable behavior beyond the approved contract."**

To audit another checkout with the evidence script:

```bash
python3 .agents/skills/unfuck-anything/scripts/evidence.py --repo /path/to/project
```

This collector does **not** run builds, tests, package installations, telemetry, or network calls. Its signals are leads for investigation, not a diagnosis.

## Operating contract

**Default mode: audit + bounded repair**, only where the environment grants the necessary permissions. For uncertain, high-impact, or irreversible operations, stop at a repair proposal until explicitly authorized. Never delete production data, weaken authorization, tamper with audit trails, falsify benchmarks, change legal/compliance claims, or bypass safety controls as a shortcut.

The agent produces an evidence ledger, an architecture map, falsifiable hypotheses, an acceptance contract, a ranked repair plan, and verification results. Each claim is marked observed, inferred, or hypothesized. Independently review behavior, failure handling, operations, and rollback before accepting a repair.

**A successful repair must improve measured capability, risk, or maintainability under the same declared constraints.** Green CI alone is not enough; neither is fewer lines of code.

## Examples

See [worked cases](.agents/skills/unfuck-anything/references/cases.md) covering a vibe-coded distributed monolith, CI theatre, agent-swarm PR factories, dashboard-driven institutional failure, performance benchmark theatre, and risky legacy rewrites.

Read the [diagnostic patterns](.agents/skills/unfuck-anything/references/patterns.md), [verification protocol](.agents/skills/unfuck-anything/references/verification.md), and [output templates](.agents/skills/unfuck-anything/assets/AUDIT_TEMPLATE.md) before running substantial changes.

## Status

The built-in collector and skill structure are exercised by a Python standard-library unit suite in `tests/`. That suite tests the **tool**, not whether an arbitrary agent successfully repairs a real system. The example evaluations in `evals/scenarios.md` describe the additional behavioral checks a deployed agent must pass.

No proprietary dependency, model provider, or orchestration service is required. No license is granted merely by the repository being public; add an explicit license if redistribution is desired.
