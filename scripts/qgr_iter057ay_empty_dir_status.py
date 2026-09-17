#!/usr/bin/env python3
import argparse
import hashlib
import json
import os
from pathlib import Path
import subprocess

AW_COMMIT = "1c4963a4bcc84a5bf331f0173c76b05d7a6a1864"
OUTPUT_DIR = "iter057aw-output"
SENTINEL = ".iter057ay-sentinel"


def run(repo: Path, *args: str) -> bytes:
    cp = subprocess.run(["git", "-C", str(repo), *args], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
    return cp.stdout


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def status(repo: Path) -> bytes:
    return run(repo, "status", "--porcelain=v1", "-z", "--untracked-files=normal")


def tracked_index(repo: Path) -> bytes:
    return run(repo, "ls-files", "-s", "-z")


def encode(raw: bytes) -> dict:
    return {"hex": raw.hex(), "sha256": sha256(raw), "length": len(raw)}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", required=True)
    ap.add_argument("--lane", required=True, choices=("primary", "independent"))
    ap.add_argument("--output", required=True)
    ns = ap.parse_args()

    repo = Path(ns.repo).resolve()
    out = Path(ns.output).resolve()
    head = run(repo, "rev-parse", "HEAD").decode("ascii").strip()

    target = repo / OUTPUT_DIR
    sentinel = target / SENTINEL
    if target.exists():
        raise SystemExit(f"precondition failure: {target} already exists")

    pre_status = status(repo)
    pre_index = tracked_index(repo)

    target.mkdir()
    empty_dir_status = status(repo)
    empty_index = tracked_index(repo)

    sentinel.write_bytes(b"iter057ay\n")
    sentinel_status = status(repo)
    sentinel_index = tracked_index(repo)

    sentinel.unlink()
    target.rmdir()
    restored_status = status(repo)
    restored_index = tracked_index(repo)

    expected_sentinel = (f"?? {OUTPUT_DIR}/".encode("utf-8") + b"\x00")
    normalized = {
        "frozen_aw_commit": AW_COMMIT,
        "observed_head": head,
        "output_dir": OUTPUT_DIR,
        "sentinel_name": SENTINEL,
        "porcelain_command": "git status --porcelain=v1 -z --untracked-files=normal",
        "pre_status": encode(pre_status),
        "empty_directory_status": encode(empty_dir_status),
        "sentinel_status": encode(sentinel_status),
        "expected_sentinel_status": encode(expected_sentinel),
        "restored_status": encode(restored_status),
        "tracked_index_before": encode(pre_index),
        "tracked_index_after_empty_directory": encode(empty_index),
        "tracked_index_after_sentinel": encode(sentinel_index),
        "tracked_index_after_restore": encode(restored_index),
        "controls": {
            "frozen_aw_head_exact": head == AW_COMMIT,
            "pre_harness_porcelain_empty": pre_status == b"",
            "empty_untracked_directory_invisible": empty_dir_status == b"",
            "tracked_tree_sha256_unchanged": sha256(pre_index) == sha256(empty_index) == sha256(sentinel_index) == sha256(restored_index),
            "sentinel_makes_output_directory_visible_exactly": sentinel_status == expected_sentinel,
            "sentinel_removal_restores_empty_porcelain": restored_status == b"",
            "descendant_science_read_or_produced": False,
            "historical_classification_changed": False
        }
    }
    normalized["all_controls_pass"] = all(
        value is True for key, value in normalized["controls"].items()
        if key not in ("descendant_science_read_or_produced", "historical_classification_changed")
    ) and normalized["controls"]["descendant_science_read_or_produced"] is False \
      and normalized["controls"]["historical_classification_changed"] is False

    payload = {
        "gate": "ITER057AY_EMPTY_DIRECTORY_GIT_STATUS_SEMANTICS_DIAGNOSTIC",
        "lane": ns.lane,
        "target_blind_technical_diagnostic": True,
        "normalized": normalized
    }
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
