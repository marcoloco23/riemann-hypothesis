#!/usr/bin/env python3
"""Repository verification entry point.

The quick suite checks Python syntax, local Markdown links, and the fast
Davenport-Heilbronn/resolvent calibration. The explicit-formula suite additionally
runs the slower numerical regressions. Neither suite upgrades numerical evidence to
a proof or certifies an omitted infinite tail.
"""

from __future__ import annotations

import argparse
import os
from pathlib import Path
import py_compile
import re
import subprocess
import sys
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
SKIP_PARTS = {".git", ".venv", "venv", "__pycache__", ".lake", "build"}
MARKDOWN_LINK = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")


def repository_files(suffix: str):
    for path in ROOT.rglob(f"*{suffix}"):
        if not any(part in SKIP_PARTS for part in path.parts):
            yield path


def check_python_syntax() -> None:
    files = sorted(repository_files(".py"))
    for path in files:
        py_compile.compile(str(path), doraise=True)
    print(f"PASS Python syntax: {len(files)} files")


def check_local_markdown_links() -> None:
    failures: list[str] = []
    checked = 0
    for document in sorted(repository_files(".md")):
        text = document.read_text(encoding="utf-8")
        for match in MARKDOWN_LINK.finditer(text):
            target = match.group(1).strip()
            if target.startswith("<") and target.endswith(">"):
                target = target[1:-1]
            if not target or target.startswith("#"):
                continue
            if re.match(r"^[A-Za-z][A-Za-z0-9+.-]*:", target):
                continue
            target = unquote(target.split("#", 1)[0].split("?", 1)[0])
            if not target:
                continue
            # Mathematical prose often uses Markdown-like function notation such as
            # ``L_n[f](x)``. Check only targets that look like repository paths.
            if any(character in target for character in " =+*{}\\"):
                continue
            if not (
                target.startswith(("./", "../"))
                or "/" in target
                or Path(target).suffix
                or target in {"LICENSE", "NOTICE"}
            ):
                continue
            checked += 1
            resolved = (document.parent / target).resolve()
            if not resolved.exists():
                rel = document.relative_to(ROOT)
                failures.append(f"{rel}: missing {target}")
    if failures:
        raise RuntimeError("Broken local Markdown links:\n" + "\n".join(failures))
    print(f"PASS local Markdown links: {checked} targets")


def run(command: list[str]) -> None:
    print("RUN", " ".join(command), flush=True)
    subprocess.run(command, cwd=ROOT, check=True)


def quick_suite() -> None:
    check_python_syntax()
    check_local_markdown_links()
    run(
        [
            sys.executable,
            "workspace/scratch/explicit-formula-check/check_smooth_and_dh.py",
            "--calibration-only",
        ]
    )


def explicit_formula_suite() -> None:
    quick_suite()
    run([sys.executable, "workspace/scratch/explicit-formula-check/check_ef.py"])
    run([sys.executable, "workspace/scratch/explicit-formula-check/hostile_review_check.py"])
    run([sys.executable, "workspace/scratch/explicit-formula-check/check_smooth_and_dh.py"])


def main() -> int:
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--quick", action="store_true")
    group.add_argument("--explicit-formula", action="store_true")
    args = parser.parse_args()

    os.environ.setdefault("PYTHONDONTWRITEBYTECODE", "1")
    if args.quick:
        quick_suite()
    else:
        explicit_formula_suite()
    print("PASS repository verification")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
