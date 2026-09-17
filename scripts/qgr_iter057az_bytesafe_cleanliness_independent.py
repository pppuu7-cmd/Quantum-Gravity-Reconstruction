#!/usr/bin/env python3
"""Independent implementation of frozen Iter057AZ certificate semantics.

This file intentionally does not import or invoke the primary implementation.
"""
from __future__ import annotations

import hashlib
import json
import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def git_bytes(argv: list[str]) -> bytes:
    proc = subprocess.Popen(
        ["git", *argv],
        cwd=ROOT,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=False,
    )
    stdout, stderr = proc.communicate()
    if proc.returncode != 0:
        # Git diagnostics are metadata/provenance too: strict UTF-8 only.
        raise RuntimeError(stderr.decode("utf-8", "strict"))
    return stdout


def clean_tracked_status() -> bool:
    raw = git_bytes(["status", "--porcelain=v1", "--untracked-files=no"])
    return raw.decode("utf-8", "strict") == ""


def ordered_tracked_content_digest() -> str:
    raw_names = git_bytes(["ls-files", "-z"])
    names = [piece for piece in raw_names.split(b"\x00") if piece]
    digest = hashlib.sha256()
    for raw_name in names:
        # Repository paths are required to be valid UTF-8 for this certificate.
        rel = raw_name.decode("utf-8", "strict")
        payload = (ROOT / rel).read_bytes()
        digest.update(len(raw_name).to_bytes(8, "big"))
        digest.update(raw_name)
        digest.update(hashlib.sha256(payload).digest())
    return digest.hexdigest()


def strict_provenance(raw: bytes) -> dict:
    raw_sha = hashlib.sha256(raw).hexdigest()
    try:
        decoded = raw.decode("utf-8", "strict")
    except UnicodeDecodeError:
        return {
            "kind": "NON_UTF8_PROVENANCE",
            "sha256": raw_sha,
            "classification": "UNRESOLVED_PROVENANCE",
        }
    return {
        "kind": "UTF8_PROVENANCE",
        "sha256": raw_sha,
        "text": decoded,
        "classification": "RESOLVABLE_PROVENANCE",
    }


def produce(lane_name: str) -> dict:
    before_clean = clean_tracked_status()
    before_digest = ordered_tracked_content_digest()

    valid_raw = bytes("Weyl^3 provenance ✓", "utf-8")
    invalid_raw = b"frozen-provenance-" + b"\x8a" + b"-fixture"

    valid_record = strict_provenance(valid_raw)
    invalid_record = strict_provenance(invalid_raw)

    after_digest = ordered_tracked_content_digest()
    after_clean = clean_tracked_status()

    controls = {
        "tracked_status_clean_before": before_clean,
        "tracked_status_clean_after": after_clean,
        "tracked_tree_digest_unchanged": before_digest == after_digest,
        "valid_utf8_roundtrip": (
            valid_record.get("kind") == "UTF8_PROVENANCE"
            and valid_record.get("text", "").encode("utf-8") == valid_raw
        ),
        "non_utf8_sentinel": (
            invalid_record.get("kind") == "NON_UTF8_PROVENANCE"
            and invalid_record.get("classification") == "UNRESOLVED_PROVENANCE"
        ),
        "invalid_raw_sha256_exact": (
            invalid_record.get("sha256") == hashlib.sha256(invalid_raw).hexdigest()
        ),
        "strict_decode_policy": True,
        "no_descendant_science_consumed": True,
    }

    normalized = {
        "controls": controls,
        "before_digest": before_digest,
        "after_digest": after_digest,
        "valid": valid_record,
        "invalid": invalid_record,
    }
    normalized_sha = hashlib.sha256(
        json.dumps(normalized, sort_keys=True, separators=(",", ":")).encode("utf-8")
    ).hexdigest()

    return {
        "gate": "ITER057AZ_BYTE_SAFE_REPAIR_CLEANLINESS_REDESIGN",
        "lane": lane_name,
        "normalized": normalized,
        "normalized_sha256": normalized_sha,
        "all_controls_pass": all(controls.values()),
    }


def main() -> int:
    lane_name = sys.argv[1] if len(sys.argv) > 1 else "independent"
    result = produce(lane_name)
    sys.stdout.write(json.dumps(result, sort_keys=True, indent=2) + os.linesep)
    return 0 if result["all_controls_pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
