#!/usr/bin/env python3
"""Iter057AW byte-safe Git provenance reader.

Technical repair only. This module does not perform dependency adjudication and
must not consume or replay descendant scientific results.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from pathlib import Path
from typing import Any, Dict

NON_UTF8_PROVENANCE = "NON_UTF8_PROVENANCE"
UTF8_TEXT = "UTF8_TEXT"
MISSING_PROVENANCE = "MISSING_PROVENANCE"


def read_at(repo: Path, ref: str, path: str) -> Dict[str, Any]:
    """Read one Git object as bytes, then decode candidate text strictly as UTF-8.

    Undecodable bytes are never interpreted semantically.  They are represented
    only by a deterministic fail-closed condition containing ref/path and the
    SHA256 of the raw bytes.
    """
    cp = subprocess.run(
        ["git", "-C", str(repo), "show", f"{ref}:{path}"],
        text=False,
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
        check=False,
    )
    if cp.returncode != 0:
        return {
            "status": MISSING_PROVENANCE,
            "ref": ref,
            "path": path,
        }

    raw = bytes(cp.stdout)
    digest = hashlib.sha256(raw).hexdigest()
    try:
        text = raw.decode("utf-8", errors="strict")
    except UnicodeDecodeError:
        return {
            "status": NON_UTF8_PROVENANCE,
            "ref": ref,
            "path": path,
            "raw_sha256": digest,
        }

    return {
        "status": UTF8_TEXT,
        "ref": ref,
        "path": path,
        "raw_sha256": digest,
        "text": text,
    }


def unresolved_if_required(result: Dict[str, Any]) -> bool:
    """Fail-closed predicate for any required provenance object."""
    return result.get("status") in {NON_UTF8_PROVENANCE, MISSING_PROVENANCE}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", type=Path, required=True)
    parser.add_argument("--ref", required=True)
    parser.add_argument("--path", required=True)
    args = parser.parse_args()
    result = read_at(args.repo, args.ref, args.path)
    print(json.dumps(result, sort_keys=True, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
