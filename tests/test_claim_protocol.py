"""Structural tests: documentation references and the outsider-verification contract.

These tests exercise documentation integrity, NOT agent reasoning or claim truth.
"""

import re
from pathlib import Path
from urllib.parse import unquote, urlsplit
import unittest

REPO = Path(__file__).resolve().parents[1]
SKILL = REPO / ".agents" / "skills" / "unfuck-anything"
MARKDOWN_LINK = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


class ReferenceIntegrityTests(unittest.TestCase):
    def test_local_markdown_links_resolve(self):
        missing = []
        paths = [
            REPO / "README.md",
            REPO / "PHILOSOPHY.md",
            SKILL / "references" / "outside-the-network.md",
            SKILL / "references" / "outside-verification.md",
            SKILL / "references" / "claim-correction.md",
        ]
        for source in paths:
            for link in MARKDOWN_LINK.findall(source.read_text(encoding="utf-8")):
                if link.startswith(("https://", "http://", "mailto:", "#")):
                    continue
                clean = unquote(urlsplit(link).path)
                if clean and not (source.parent / clean).exists():
                    missing.append(f"{source.relative_to(REPO)}: {link}")
        self.assertEqual(missing, [])

    def test_skill_cross_references_exist(self):
        text = (SKILL / "SKILL.md").read_text(encoding="utf-8")
        for relative in (
            "references/outside-verification.md",
            "references/claim-correction.md",
            "assets/CLAIM_CORRECTION_TEMPLATE.md",
        ):
            self.assertIn(relative, text)
            self.assertTrue((SKILL / relative).is_file(), relative)

    def test_verification_distinguishes_reproduction_from_replication(self):
        verification = (SKILL / "references" / "outside-verification.md").read_text(
            encoding="utf-8"
        )
        self.assertIn("not independently verified", verification)
        self.assertIn("Hash", verification)
        self.assertIn("claimant", verification)
        self.assertIn("legal", verification.lower())
        self.assertIn("normative", verification.lower())


if __name__ == "__main__":
    unittest.main()
