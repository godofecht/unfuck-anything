#!/usr/bin/env python3
"""Read-only architecture evidence inventory. Never executes project code."""

from __future__ import annotations

import argparse
from collections import Counter
import json
import os
from pathlib import Path
import subprocess
import sys

EXCLUDED_DIRS = {
    ".git", ".hg", ".svn", ".venv", "venv", "node_modules", "__pycache__",
    "dist", "build", ".next", ".turbo", "target", ".gradle", ".tox",
    ".mypy_cache", ".pytest_cache", "coverage", ".coverage", "vendor",
}
MANIFESTS = {
    "pyproject.toml", "requirements.txt", "setup.py", "package.json",
    "package-lock.json", "pnpm-lock.yaml", "yarn.lock", "cargo.toml",
    "cargo.lock", "go.mod", "go.sum", "cmakelists.txt", "makefile",
    "pom.xml", "build.gradle", "build.gradle.kts", "composer.json",
    "gemfile", "mix.exs", "dockerfile", "justfile",
}
SOURCE_EXTENSIONS = {
    ".py", ".js", ".jsx", ".ts", ".tsx", ".go", ".rs", ".c", ".h",
    ".cc", ".cpp", ".hpp", ".java", ".kt", ".swift", ".rb", ".php",
    ".cs", ".ex", ".exs", ".sh", ".sql", ".flow",
}
SAMPLE_BYTES = 262144


def git_info(root: Path) -> dict[str, str | None]:
    def get(*args: str) -> str | None:
        try:
            result = subprocess.run(
                ["git", "-C", str(root), *args],
                capture_output=True, text=True, timeout=8, check=False,
            )
        except (OSError, subprocess.TimeoutExpired):
            return None
        return result.stdout.strip() if result.returncode == 0 else None

    return {
        "revision": get("rev-parse", "HEAD"),
        "branch": get("branch", "--show-current"),
        "status_porcelain": get("status", "--porcelain=v1"),
    }


def looks_like_test(relative: str) -> bool:
    p = Path(relative)
    name = p.name.lower()
    parts = {part.lower() for part in p.parts}
    return (
        bool(parts.intersection({"test", "tests", "__tests__", "spec", "specs"}))
        or name.startswith("test_")
        or name.endswith(("_test.py", "_test.go", "_test.rs", "_test.cpp"))
        or ".test." in name
        or ".spec." in name
    )


def inventory(root: Path, max_files: int) -> dict:
    paths: list[Path] = []
    truncated = False
    for directory, dirnames, filenames in os.walk(root, followlinks=False):
        dirnames[:] = sorted(
            d for d in dirnames
            if d not in EXCLUDED_DIRS and not (Path(directory) / d).is_symlink()
        )
        for name in sorted(filenames):
            candidate = Path(directory) / name
            if candidate.is_symlink() or not candidate.is_file():
                continue
            if len(paths) >= max_files:
                truncated = True
                break
            paths.append(candidate)
        if truncated:
            break

    extensions: Counter[str] = Counter()
    top_directories: Counter[str] = Counter()
    tests: list[str] = []
    manifests: list[str] = []
    workflows: list[str] = []
    large_sources: list[dict[str, int | str]] = []
    scanned_bytes = 0
    for path in paths:
        relative = path.relative_to(root).as_posix()
        extension = path.suffix.lower() or "[none]"
        extensions[extension] += 1
        top_directories[relative.split("/")[0] if "/" in relative else "[root]"] += 1
        if looks_like_test(relative):
            tests.append(relative)
        if path.name.lower() in MANIFESTS:
            manifests.append(relative)
        if relative.startswith(".github/workflows/") and relative.endswith((".yml", ".yaml")):
            workflows.append(relative)
        if extension not in SOURCE_EXTENSIONS:
            continue
        try:
            with path.open("rb") as stream:
                data = stream.read(SAMPLE_BYTES + 1)
        except OSError:
            continue
        if b"\x00" in data[:4096]:
            continue
        scanned_bytes += min(len(data), SAMPLE_BYTES)
        if len(data) > SAMPLE_BYTES:
            continue  # line count would be inaccurate
        lines = data.count(b"\n") + (1 if data and not data.endswith(b"\n") else 0)
        if lines >= 600:
            large_sources.append({"path": relative, "lines": lines})

    findings: list[str] = []
    if not tests:
        findings.append("No conventional test paths found in sampled files; unconventional tests may exist.")
    if not workflows:
        findings.append("No GitHub Actions YAML found; another CI system may be used.")
    if not manifests:
        findings.append("No recognized dependency/build manifest found; the list is non-exhaustive.")
    if large_sources:
        findings.append("Large source files warrant boundary inspection; file length is not itself a defect.")

    return {
        "schema_version": "1",
        "root": str(root),
        "git": git_info(root),
        "sample": {
            "files": len(paths),
            "max_files": max_files,
            "truncated": truncated,
            "source_bytes_sampled": scanned_bytes,
            "excluded_dirnames": sorted(EXCLUDED_DIRS),
            "extensions": dict(sorted(extensions.items())),
            "top_level_counts": dict(sorted(top_directories.items())),
        },
        "evidence": {
            "test_paths": tests[:40],
            "test_path_count": len(tests),
            "manifests": manifests[:50],
            "github_workflows": workflows[:30],
            "large_source_files": sorted(
                large_sources, key=lambda row: (-int(row["lines"]), str(row["path"]))
            )[:20],
        },
        "leads_not_diagnoses": findings,
        "limitations": [
            "Read-only file sampling; no code, tests, builds, services or network requests executed.",
            "Excluded directories, file cap, binary files and 256 KiB/source sampling limit visibility.",
            "Filenames and line counts cannot prove causation, correctness, quality or motives.",
            "Sensitive filenames and git status may appear in output; review before sharing.",
        ],
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=Path("."))
    parser.add_argument("--output", type=Path, help="Write JSON to this file; otherwise print to stdout.")
    parser.add_argument("--max-files", type=int, default=20000)
    args = parser.parse_args(argv)
    if args.max_files < 1:
        parser.error("--max-files must be positive")
    root = args.repo.resolve()
    if not root.is_dir():
        parser.error(f"Not a directory: {root}")
    payload = inventory(root, args.max_files)
    output = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.output:
        destination = args.output.resolve()
        if destination == root or destination.is_dir():
            parser.error("--output must name a file, not a directory")
        try:
            destination.write_text(output, encoding="utf-8")
        except OSError as exc:
            parser.error(f"Unable to write output: {exc}")
    else:
        sys.stdout.write(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
