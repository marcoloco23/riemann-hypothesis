#!/usr/bin/env python3
"""Scan publishable files and Git history for common secret formats.

Only the location and detector name are printed. Suspected secret values are never
echoed. This is a focused pre-publication check, not a guarantee that no sensitive
information exists.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path
import re
import subprocess


ROOT = Path(__file__).resolve().parents[1]
MAX_BLOB_BYTES = 2_000_000


@dataclass(frozen=True)
class Detector:
    name: str
    pattern: re.Pattern[bytes]


DETECTORS = (
    Detector("private-key", re.compile(rb"-----BEGIN (?:RSA |EC |OPENSSH |DSA )?PRIVATE KEY-----")),
    Detector("aws-access-key", re.compile(rb"\b(?:AKIA|ASIA)[0-9A-Z]{16}\b")),
    Detector("github-token", re.compile(rb"\b(?:gh[pousr]_[A-Za-z0-9]{36,255}|github_pat_[A-Za-z0-9_]{50,255})\b")),
    Detector("google-api-key", re.compile(rb"\bAIza[0-9A-Za-z_-]{35}\b")),
    Detector("slack-token", re.compile(rb"\bxox[baprs]-[0-9A-Za-z-]{20,}\b")),
    Detector("credential-in-url", re.compile(rb"[A-Za-z][A-Za-z0-9+.-]*://[^\s/:]+:[^\s/@]+@")),
    Detector(
        "assigned-secret",
        re.compile(
            rb"(?i)\b(?:password|passwd|client_secret|api[_-]?key|access[_-]?token)\b"
            rb"\s*[:=]\s*['\"]?[A-Za-z0-9+/=_-]{16,}"
        ),
    ),
)

SENSITIVE_NAMES = re.compile(
    r"(?i)(^|/)(?:\.env(?:\..*)?|id_(?:rsa|ed25519)|credentials?|secrets?|[^/]+\.(?:pem|key|p12|pfx))$"
)


def git(*args: str) -> bytes:
    return subprocess.check_output(["git", *args], cwd=ROOT, stderr=subprocess.DEVNULL)


def scan_bytes(label: str, data: bytes, findings: set[tuple[str, str]]) -> None:
    if b"\x00" in data[:8192]:
        return
    for detector in DETECTORS:
        if detector.pattern.search(data):
            findings.add((label, detector.name))


def current_paths() -> list[str]:
    tracked = git("ls-files", "-z").split(b"\0")
    untracked = git("ls-files", "--others", "--exclude-standard", "-z").split(b"\0")
    return sorted({item.decode("utf-8", "surrogateescape") for item in tracked + untracked if item})


def scan_current(findings: set[tuple[str, str]]) -> int:
    scanned = 0
    for relative in current_paths():
        if SENSITIVE_NAMES.search(relative):
            findings.add((relative, "sensitive-filename"))
        path = ROOT / relative
        if not path.is_file() or path.stat().st_size > MAX_BLOB_BYTES:
            continue
        scan_bytes(relative, path.read_bytes(), findings)
        scanned += 1
    return scanned


def scan_history(findings: set[tuple[str, str]]) -> int:
    scanned = 0
    seen: set[str] = set()
    for line in git("rev-list", "--objects", "--all").decode("utf-8", "replace").splitlines():
        oid, _, path = line.partition(" ")
        if not path or oid in seen:
            continue
        seen.add(oid)
        if SENSITIVE_NAMES.search(path):
            findings.add((f"history:{path}", "sensitive-filename"))
        if git("cat-file", "-t", oid).strip() != b"blob":
            continue
        if int(git("cat-file", "-s", oid)) > MAX_BLOB_BYTES:
            continue
        scan_bytes(f"history:{path}", git("cat-file", "-p", oid), findings)
        scanned += 1
    return scanned


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--current-only", action="store_true")
    args = parser.parse_args()
    findings: set[tuple[str, str]] = set()
    count = scan_current(findings)
    if not args.current_only:
        count += scan_history(findings)
    if findings:
        print("Potential sensitive material found (values suppressed):")
        for location, detector in sorted(findings):
            print(f"- {location}: {detector}")
        return 1
    scope = "current files" if args.current_only else "current files and Git history"
    print(f"PASS secret-format scan: {count} blobs across {scope}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
