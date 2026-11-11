"""Integration and unit checks for the read-only evidence inventory."""

import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

REPO = Path(__file__).resolve().parents[1]
SKILL = REPO / ".agents" / "skills" / "unfuck-anything"
sys.path.insert(0, str(SKILL / "scripts"))

import evidence  # noqa: E402


class InventoryTests(unittest.TestCase):
    def test_finds_source_tests_and_github_workflows(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "tests").mkdir()
            (root / "tests" / "test_engine.py").write_text("assert True\n", encoding="utf-8")
            (root / ".github" / "workflows").mkdir(parents=True)
            (root / ".github" / "workflows" / "ci.yml").write_text("name: CI\n", encoding="utf-8")
            (root / "pyproject.toml").write_text("[project]\n", encoding="utf-8")
            (root / "src.py").write_text("x = 3\n", encoding="utf-8")
            data = evidence.inventory(root, 20)
            self.assertEqual(data["evidence"]["test_path_count"], 1)
            self.assertEqual(data["evidence"]["github_workflows"], [".github/workflows/ci.yml"])
            self.assertEqual(data["evidence"]["manifests"], ["pyproject.toml"])
            self.assertEqual(data["sample"]["files"], 4)
            self.assertFalse(data["leads_not_diagnoses"])

    def test_skips_build_directories_and_symlinks(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "node_modules").mkdir()
            (root / "node_modules" / "x.js").write_text("test\n", encoding="utf-8")
            (root / "app.py").write_text("print('safe')\n", encoding="utf-8")
            try:
                (root / "external.py").symlink_to(root / "app.py")
            except (OSError, NotImplementedError):
                pass
            data = evidence.inventory(root, 20)
            self.assertEqual(data["sample"]["files"], 1)

    def test_reports_sampling_limits_and_large_source(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "big.py").write_text("pass\n" * 601, encoding="utf-8")
            (root / "small.py").write_text("pass\n", encoding="utf-8")
            data = evidence.inventory(root, 1)
            self.assertTrue(data["sample"]["truncated"])
            self.assertEqual(data["evidence"]["large_source_files"][0]["lines"], 601)

    def test_cli_is_read_only_without_output(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "app.py").write_text("print(1)\n", encoding="utf-8")
            before = sorted(str(p.relative_to(root)) for p in root.rglob("*"))
            process = subprocess.run(
                [sys.executable, str(SKILL / "scripts" / "evidence.py"), "--repo", str(root)],
                capture_output=True, text=True, check=True,
            )
            data = json.loads(process.stdout)
            after = sorted(str(p.relative_to(root)) for p in root.rglob("*"))
            self.assertEqual(before, after)
            self.assertEqual(data["sample"]["files"], 1)

    def test_invalid_cli_max_files_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            process = subprocess.run(
                [sys.executable, str(SKILL / "scripts" / "evidence.py"),
                 "--repo", directory, "--max-files", "0"],
                capture_output=True, text=True,
            )
            self.assertNotEqual(process.returncode, 0)
            self.assertIn("--max-files must be positive", process.stderr)


class SkillStructureTests(unittest.TestCase):
    def test_skill_metadata_and_references(self):
        text = (SKILL / "SKILL.md").read_text(encoding="utf-8")
        self.assertTrue(text.startswith("---\n"))
        self.assertIn("\nname: unfuck-anything\n", text)
        self.assertIn("\ndescription:", text)
        for reference in (
            "references/patterns.md", "references/cases.md", "references/verification.md",
            "assets/AUDIT_TEMPLATE.md", "assets/REPAIR_PLAN_TEMPLATE.md",
            "assets/VERIFICATION_TEMPLATE.md", "scripts/evidence.py"
        ):
            self.assertTrue((SKILL / reference).is_file(), reference)


if __name__ == "__main__":
    unittest.main()
