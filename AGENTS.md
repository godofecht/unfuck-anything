# Agent guidance

This repository packages the `unfuck-anything` agent skill. For architecture repair, load `.agents/skills/unfuck-anything/SKILL.md` and the relevant references. Do not treat this README or agent guidance as a substitute for the skill itself.

When editing this repository, enforce the independent verification gate in `.agents/skills/unfuck-anything/references/outside-verification.md` and the idea-correction protocol in `.agents/skills/unfuck-anything/references/claim-correction.md`. A claim is not independently verified because a maintainer, sponsor, reviewer or CI system approved it. If external reproduction cannot be obtained, report that limitation instead of manufacturing it.

When editing this repository, validate the evidence script with `python3 -m unittest discover -s tests -v`. Keep the skill portable and read-only by default. Do not invent tests, tooling, APIs, incident history, observed metrics, or motives. Any change to acceptance criteria must be justified by real evidence rather than a desire for a passing result.
