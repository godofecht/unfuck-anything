# Agent guidance

This repository packages the `unfuck-anything` agent skill. For architecture repair, load `.agents/skills/unfuck-anything/SKILL.md` and the relevant references. Do not treat this README or agent guidance as a substitute for the skill itself.

When editing this repository, validate the evidence script with `python3 -m unittest discover -s tests -v`. Keep the skill portable and read-only by default. Do not invent tests, tooling, APIs, incident history, observed metrics, or motives. Any change to acceptance criteria must be justified by real evidence rather than a desire for a passing result.
