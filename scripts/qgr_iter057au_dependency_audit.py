#!/usr/bin/env python3
"""Iter057AU target-blind dependency adjudication.

This script never replays descendant science.  It reconstructs provenance from the
frozen preregistration tree and classifies load-bearing dependence on the legacy
Iter057X degree-six source.  Primary and independent modes use separate
classification implementations and never read one another's payloads.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
from pathlib import Path
from typing import Dict, Iterable, List, Sequence, Set, Tuple

PREREG = "616859890df95057556d265612c53da839a5848a"
ITER_X_RANK = 24
TEXT_EXT = {".md", ".json", ".yml", ".yaml", ".py", ".txt", ".toml", ".ini", ".cfg", ".sh"}
DEP_WORDS = (
    "input", "inputs", "source", "sources", "consume", "consumes", "consumed",
    "load", "loaded", "loads", "depend", "depends", "dependency", "derived",
    "parent", "lineage", "provenance", "replay", "uses", "using", "from",
    "canonical", "artifact", "manifest", "hash", "sha256",
)
DENY_WORDS = (
    "independent of", "does not depend", "not dependent", "without reading",
    "historical only", "historical record", "remains immutable", "preserved only",
    "not rewritten", "do not rewrite", "no retroactive", "not load-bearing",
)
PATH_RE = re.compile(r"(?:(?:results|preregistration|scripts|recovery|data|artifacts)/[^\s`'\"<>]+|\.github/workflows/[^\s`'\"<>]+)")
SHA_RE = re.compile(r"\b[0-9a-f]{40}\b", re.I)
LONG_HASH_RE = re.compile(r"\b[0-9a-f]{64}\b", re.I)
ITER_TOKEN_RE = re.compile(r"\b(?:ITER|Iter|iter)057([A-Z]{1,3})\b")
RESULT_RE = re.compile(r"^results/.*?ITER057([A-Z]{1,3})[^/]*\.(?:md|json|ya?ml|txt)$", re.I)


def run(repo: Path, *args: str, check: bool = True) -> str:
    cp = subprocess.run(["git", "-C", str(repo), *args], text=True, stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE)
    if check and cp.returncode != 0:
        raise RuntimeError(f"git {' '.join(args)} failed: {cp.stderr.strip()}")
    return cp.stdout


def iter_rank(tag: str) -> int:
    n = 0
    for ch in tag.upper():
        n = n * 26 + (ord(ch) - 64)
    return n


def read_at(repo: Path, ref: str, path: str) -> str | None:
    cp = subprocess.run(["git", "-C", str(repo), "show", f"{ref}:{path}"], text=True,
                        stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
    if cp.returncode != 0:
        return None
    return cp.stdout


def list_records(repo: Path) -> List[Tuple[str, str]]:
    names = run(repo, "ls-tree", "-r", "--name-only", PREREG, "--", "results").splitlines()
    out: List[Tuple[str, str]] = []
    for p in names:
        m = RESULT_RE.match(p)
        if not m:
            continue
        tag = m.group(1).upper()
        if iter_rank(tag) > ITER_X_RANK:
            out.append((p, tag))
    out.sort(key=lambda x: (iter_rank(x[1]), x[0]))
    return out


def list_x_records(repo: Path) -> List[str]:
    names = run(repo, "ls-tree", "-r", "--name-only", PREREG, "--", "results").splitlines()
    ans = []
    for p in names:
        m = RESULT_RE.match(p)
        if m and m.group(1).upper() == "X":
            ans.append(p)
    return sorted(ans)


def changed_text_files(repo: Path, sha: str) -> List[str]:
    cp = subprocess.run(["git", "-C", str(repo), "show", "--format=", "--name-only", sha],
                        text=True, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
    if cp.returncode != 0:
        return []
    out = []
    for p in cp.stdout.splitlines():
        p = p.strip()
        if p and Path(p).suffix.lower() in TEXT_EXT:
            out.append(p)
    return sorted(set(out))


def collect_context(repo: Path, record_path: str) -> List[Tuple[str, str]]:
    """Collect bounded textual provenance reachable from one result record."""
    base = read_at(repo, PREREG, record_path) or ""
    entries: List[Tuple[str, str]] = [(record_path, base)]
    seen_sources = {record_path}

    # Explicit paths in the result are authoritative provenance candidates.
    for raw in PATH_RE.findall(base):
        p = raw.rstrip(".,;:)]}")
        if p in seen_sources:
            continue
        txt = read_at(repo, PREREG, p)
        if txt is not None and len(txt.encode("utf-8")) <= 1_000_000:
            entries.append((p, txt))
            seen_sources.add(p)

    # Referenced commits expose the implementation/workflow/result files that
    # were durably recorded by the result.  This is provenance reconstruction,
    # not scientific replay.
    shas = sorted(set(SHA_RE.findall(base)))
    for sha in shas:
        for p in changed_text_files(repo, sha):
            key = f"{sha}:{p}"
            if key in seen_sources:
                continue
            txt = read_at(repo, sha, p)
            if txt is not None and len(txt.encode("utf-8")) <= 1_000_000:
                entries.append((key, txt))
                seen_sources.add(key)
    return entries


def legacy_tokens(repo: Path) -> Tuple[Set[str], List[str]]:
    tokens: Set[str] = {"ITER057X", "Iter057X", "iter057x"}
    sources: List[str] = []
    for p in list_x_records(repo):
        sources.append(p)
        txt = read_at(repo, PREREG, p) or ""
        # Hashes and source-like paths recorded by Iter057X are stable provenance
        # anchors.  Context tests below prevent a bare historical mention from
        # being treated as load-bearing consumption.
        tokens.update(SHA_RE.findall(txt))
        tokens.update(LONG_HASH_RE.findall(txt))
        for raw in PATH_RE.findall(txt):
            low = raw.lower()
            if any(k in low for k in ("degree6", "degree_6", "weyl", "source", "iter057x")):
                tokens.add(raw.rstrip(".,;:)]}"))
    return tokens, sources


def context_has_dependency(text: str, start: int, end: int, radius: int = 260) -> bool:
    lo = max(0, start - radius)
    hi = min(len(text), end + radius)
    window = text[lo:hi].lower()
    if any(d in window for d in DENY_WORDS):
        return False
    return any(w in window for w in DEP_WORDS)


def primary_edges(entries: Sequence[Tuple[str, str]], known_tags: Set[str], legacy: Set[str]) -> Tuple[Set[str], bool, List[str]]:
    deps: Set[str] = set()
    direct_legacy = False
    evidence: List[str] = []
    for src, text in entries:
        for m in ITER_TOKEN_RE.finditer(text):
            tag = m.group(1).upper()
            if tag in known_tags or tag == "X":
                if context_has_dependency(text, m.start(), m.end()):
                    deps.add(tag)
                    evidence.append(f"{src}:context->ITER057{tag}")
                    if tag == "X":
                        direct_legacy = True
        for tok in sorted(legacy, key=len, reverse=True):
            if len(tok) < 8 or tok.lower() in {"iter057x"}:
                continue
            pos = text.find(tok)
            if pos >= 0 and context_has_dependency(text, pos, pos + len(tok)):
                direct_legacy = True
                evidence.append(f"{src}:legacy-anchor:{tok[:24]}")
                break
    return deps, direct_legacy, sorted(set(evidence))


def independent_edges(entries: Sequence[Tuple[str, str]], known_tags: Set[str], legacy: Set[str]) -> Tuple[Set[str], bool, List[str]]:
    """Independent line-oriented classifier; it does not call primary_edges."""
    deps: Set[str] = set()
    direct_legacy = False
    evidence: List[str] = []
    legacy_lower = [(t.lower(), t) for t in legacy if len(t) >= 8 and t.lower() != "iter057x"]
    for src, text in entries:
        lines = text.splitlines()
        for i, line in enumerate(lines):
            neighborhood = "\n".join(lines[max(0, i - 1): min(len(lines), i + 2)])
            low = neighborhood.lower()
            if any(d in low for d in DENY_WORDS):
                continue
            dep_signal = any(w in low for w in DEP_WORDS)
            if not dep_signal:
                continue
            for m in ITER_TOKEN_RE.finditer(neighborhood):
                tag = m.group(1).upper()
                if tag in known_tags or tag == "X":
                    deps.add(tag)
                    evidence.append(f"{src}:line{max(1,i)}->ITER057{tag}")
                    if tag == "X":
                        direct_legacy = True
            for lowtok, rawtok in legacy_lower:
                if lowtok in low:
                    direct_legacy = True
                    evidence.append(f"{src}:line{max(1,i)}:legacy-anchor:{rawtok[:24]}")
                    break
    return deps, direct_legacy, sorted(set(evidence))


def provenance_sufficient(entries: Sequence[Tuple[str, str]]) -> bool:
    merged = "\n".join(t for _, t in entries).lower()
    # Fail closed unless the record exposes at least one durable provenance
    # mechanism and at least one concrete identifier/path.
    mechanism = any(k in merged for k in (
        "preregistration", "implementation", "production head", "actions run",
        "artifact", "source", "input", "manifest", "durable result", "commit",
    ))
    concrete = bool(SHA_RE.search(merged) or LONG_HASH_RE.search(merged) or PATH_RE.search(merged))
    return mechanism and concrete


def acyclic(edges: Dict[str, Set[str]], tag_by_record: Dict[str, str]) -> bool:
    # Iteration dependency edges must point strictly to an earlier iteration.
    for rec, deps in edges.items():
        rr = iter_rank(tag_by_record[rec])
        for tag in deps:
            if tag == "X":
                tr = ITER_X_RANK
            else:
                tr = iter_rank(tag)
            if tr >= rr:
                return False
    return True


def classify(repo: Path, mode: str) -> dict:
    records = list_records(repo)
    if not records:
        raise RuntimeError("no post-Iter057X scientific result records found on frozen preregistration head")
    tag_by_record = {p: t for p, t in records}
    known_tags = {t for _, t in records}
    legacy, x_sources = legacy_tokens(repo)
    contexts = {p: collect_context(repo, p) for p, _ in records}

    edge_fn = primary_edges if mode == "primary" else independent_edges
    edges: Dict[str, Set[str]] = {}
    direct_flags: Dict[str, bool] = {}
    evidence_map: Dict[str, List[str]] = {}
    sufficient: Dict[str, bool] = {}
    for p, _tag in records:
        deps, direct, evidence = edge_fn(contexts[p], known_tags, legacy)
        edges[p] = deps
        direct_flags[p] = direct
        evidence_map[p] = evidence
        sufficient[p] = provenance_sufficient(contexts[p])

    classes: Dict[str, str] = {}
    for p, _ in records:
        if direct_flags[p]:
            classes[p] = "DIRECT_LOAD_BEARING_DEPENDENT"

    # Propagate only through explicit earlier-iteration dependencies.
    changed = True
    while changed:
        changed = False
        dependent_tags = {tag_by_record[p] for p, c in classes.items()
                          if c in {"DIRECT_LOAD_BEARING_DEPENDENT", "TRANSITIVE_LOAD_BEARING_DEPENDENT"}}
        for p, _tag in records:
            if p in classes:
                continue
            if edges[p] & dependent_tags:
                classes[p] = "TRANSITIVE_LOAD_BEARING_DEPENDENT"
                changed = True

    for p, _ in records:
        if p not in classes:
            classes[p] = ("INDEPENDENT_OF_LEGACY_DEGREE6_SOURCE" if sufficient[p]
                          else "UNRESOLVED_PROVENANCE")

    ordered = [
        {"record": p, "iteration": f"ITER057{tag}", "class": classes[p]}
        for p, tag in records
    ]
    replay = [x["record"] for x in ordered if x["class"] in {
        "DIRECT_LOAD_BEARING_DEPENDENT", "TRANSITIVE_LOAD_BEARING_DEPENDENT"
    }]
    unresolved = [x["record"] for x in ordered if x["class"] == "UNRESOLVED_PROVENANCE"]
    detail = []
    for p, tag in records:
        ev = evidence_map[p] or [f"{p}:record-and-referenced-provenance-reviewed"]
        detail.append({
            "record": p,
            "iteration": f"ITER057{tag}",
            "class": classes[p],
            "evidence_path": ev,
            "explicit_iteration_dependencies": [f"ITER057{x}" for x in sorted(edges[p], key=iter_rank)],
            "provenance_sufficient": sufficient[p],
        })

    clean = run(repo, "status", "--porcelain").strip() == ""
    payload = {
        "gate": "ITER057AU_CORRECTED_DEGREE6_DESCENDANT_DEPENDENCY_ADJUDICATION",
        "mode": mode,
        "preregistration_commit": PREREG,
        "census_head": PREREG,
        "iter057x_seed_records": x_sources,
        "record_count": len(records),
        "ordered_classifications": ordered,
        "classification_detail": detail,
        "replay_queue": replay,
        "unresolved_records": unresolved,
        "dag_acyclic": acyclic(edges, tag_by_record),
        "historical_result_tree_clean": clean,
        "claim_lock_promoted": False,
        "descendant_science_recomputed": False,
        "primary_payload_read": False,
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    payload["payload_sha256"] = hashlib.sha256(canonical).hexdigest()
    return payload


def aggregate(root: Path) -> dict:
    payloads = []
    for p in sorted(root.rglob("*.json")):
        try:
            obj = json.loads(p.read_text())
        except Exception:
            continue
        if obj.get("gate") == "ITER057AU_CORRECTED_DEGREE6_DESCENDANT_DEPENDENCY_ADJUDICATION" and obj.get("mode") in {"primary", "independent"}:
            payloads.append(obj)
    by_mode = {p["mode"]: p for p in payloads}
    missing = [m for m in ("primary", "independent") if m not in by_mode]
    if missing:
        return {
            "gate": "ITER057AU_CORRECTED_DEGREE6_DESCENDANT_DEPENDENCY_ADJUDICATION",
            "preregistration_commit": PREREG,
            "classification": "BLOCKED_ITER057AU_UNRESOLVED_PROVENANCE",
            "reason": f"missing independent lane payload(s): {missing}",
        }

    a, b = by_mode["primary"], by_mode["independent"]
    same_census = [x["record"] for x in a["ordered_classifications"]] == [x["record"] for x in b["ordered_classifications"]]
    same_classes = a["ordered_classifications"] == b["ordered_classifications"]
    same_queue = a["replay_queue"] == b["replay_queue"]
    unresolved = sorted(set(a.get("unresolved_records", [])) | set(b.get("unresolved_records", [])))
    controls = {
        "complete_census_agrees": same_census,
        "ordered_classifications_bit_identical": same_classes,
        "replay_queue_bit_identical": same_queue,
        "primary_dag_acyclic": bool(a.get("dag_acyclic")),
        "independent_dag_acyclic": bool(b.get("dag_acyclic")),
        "primary_historical_tree_clean": bool(a.get("historical_result_tree_clean")),
        "independent_historical_tree_clean": bool(b.get("historical_result_tree_clean")),
        "no_claim_lock_promoted": not a.get("claim_lock_promoted") and not b.get("claim_lock_promoted"),
        "no_descendant_science_recomputed": not a.get("descendant_science_recomputed") and not b.get("descendant_science_recomputed"),
        "independent_did_not_read_primary_payload": not b.get("primary_payload_read"),
    }
    all_controls = all(controls.values())
    if unresolved or not all_controls:
        classification = "BLOCKED_ITER057AU_UNRESOLVED_PROVENANCE"
        reason = "unresolved provenance or independent reconstruction/control disagreement"
    else:
        classification = "PASS_SCOPED_ITER057AU_CORRECTED_DEGREE6_DESCENDANT_DEPENDENCY_ADJUDICATION_INDEPENDENTLY_REPRODUCED"
        reason = "complete frozen-head census classified with acyclic deterministic replay queue and independent agreement"

    out = {
        "gate": "ITER057AU_CORRECTED_DEGREE6_DESCENDANT_DEPENDENCY_ADJUDICATION",
        "preregistration_commit": PREREG,
        "classification": classification,
        "reason": reason,
        "controls": controls,
        "record_count": a.get("record_count"),
        "unresolved_records": unresolved,
        "ordered_classifications": a.get("ordered_classifications") if same_classes else None,
        "replay_queue": a.get("replay_queue") if same_queue else None,
        "primary_payload_sha256": a.get("payload_sha256"),
        "independent_payload_sha256": b.get("payload_sha256"),
        "interpretation_ceiling": "dependency adjudication/replay planning only; no descendant scientific outcome recomputed",
        "claim_locks": {
            "theory_established_pct": 0,
            "beta_1_authorized": False,
            "c6_status": "SYMBOLIC_UNFIXED",
            "finite_certificate_is_theorem": False,
            "classical_implies_quantum": False,
        },
    }
    canonical = json.dumps(out, sort_keys=True, separators=(",", ":")).encode()
    out["terminal_payload_sha256"] = hashlib.sha256(canonical).hexdigest()
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", type=Path)
    ap.add_argument("--mode", choices=("primary", "independent"))
    ap.add_argument("--output", type=Path, required=True)
    ap.add_argument("--aggregate-root", type=Path)
    ns = ap.parse_args()
    if ns.aggregate_root is not None:
        obj = aggregate(ns.aggregate_root)
    else:
        if ns.repo is None or ns.mode is None:
            ap.error("--repo and --mode are required outside aggregate mode")
        obj = classify(ns.repo, ns.mode)
    ns.output.parent.mkdir(parents=True, exist_ok=True)
    ns.output.write_text(json.dumps(obj, indent=2, sort_keys=True) + "\n")
    print(json.dumps(obj, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
