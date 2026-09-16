#!/usr/bin/env python3
"""Iter057AE aggregation-only exact obstruction-map decision.

Consumes only the eight terminal Iter057AD artifacts copied by the workflow from
Actions run 35070896151.  It never recomputes an Iter057AD lane.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from fractions import Fraction
from pathlib import Path
from typing import Any, Iterable

NROWS = 1456
NCOLS = 1114
NLANES = 8
EXPECTED_O0_NONZERO = 223

PASS = "PASS_SCOPED_ITER057AE_FULL_R12_HOMOGENEOUS_OBSTRUCTION_MAP_ADMITS_EXACT_BRANCH__R14_RESPONSE_STILL_REQUIRED"
FAIL = "SCIENTIFIC_FAIL_ITER057AE_FULL_R12_HOMOGENEOUS_FREEDOM_CANNOT_REMOVE_R14_BIANCHI_NOETHER_OBSTRUCTION"
BLOCKED = "BLOCKED_ITER057AE_EIGHT_LANE_TERMINAL_ARTIFACTS_DO_NOT_REALIZE_COMPLETE_EXACT_OBSTRUCTION_MAP"
INVALID = "INVALID_ITER057AE_PROVENANCE_COVERAGE_REPLAY_BASIS_NORMALIZATION_OR_EXACTNESS_CONTROL"


def rat(x: Any) -> Fraction:
    if isinstance(x, bool):
        raise ValueError("boolean is not an exact rational payload")
    if isinstance(x, int):
        return Fraction(x, 1)
    if isinstance(x, str):
        s = x.strip()
        if re.fullmatch(r"[-+]?\d+", s):
            return Fraction(int(s), 1)
        if re.fullmatch(r"[-+]?\d+\s*/\s*[-+]?\d+", s):
            a, b = s.replace(" ", "").split("/", 1)
            return Fraction(int(a), int(b))
        raise ValueError(f"non-rational string {x!r}")
    if isinstance(x, dict):
        for pkey, qkey in (("p", "q"), ("num", "den"), ("numerator", "denominator")):
            if pkey in x and qkey in x:
                return Fraction(int(x[pkey]), int(x[qkey]))
    # Floats are forbidden, even if integral-looking.
    raise ValueError(f"unsupported exact-rational value type {type(x).__name__}")


def walk(obj: Any, path: str = "$") -> Iterable[tuple[str, Any]]:
    yield path, obj
    if isinstance(obj, dict):
        for k, v in obj.items():
            yield from walk(v, f"{path}.{k}")
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            yield from walk(v, f"{path}[{i}]")


def lower_key_path(path: str) -> str:
    return path.lower().replace("-", "_")


def parse_vector(obj: Any, n: int) -> list[Fraction] | None:
    if not isinstance(obj, list) or len(obj) != n:
        return None
    out: list[Fraction] = []
    try:
        for x in obj:
            out.append(rat(x))
    except Exception:
        return None
    return out


def matrix_shape(obj: Any) -> tuple[int, int] | None:
    if not isinstance(obj, list) or not obj or not all(isinstance(r, list) for r in obj):
        return None
    widths = {len(r) for r in obj}
    if len(widths) != 1:
        return None
    return len(obj), next(iter(widths))


def parse_matrix(obj: Any) -> list[list[Fraction]] | None:
    shp = matrix_shape(obj)
    if shp is None:
        return None
    try:
        return [[rat(x) for x in row] for row in obj]
    except Exception:
        return None


def find_lane_number(doc: Any, fallback_name: str) -> int | None:
    aliases = {"lane", "lane_id", "lane_index", "shard", "shard_id", "partition"}
    for path, obj in walk(doc):
        if isinstance(obj, dict):
            for k, v in obj.items():
                if k.lower().replace("-", "_") in aliases and isinstance(v, int) and 0 <= v < NLANES:
                    return v
    m = re.search(r"(?:lane|shard|part)[-_]?(\d+)", fallback_name, flags=re.I)
    if m and 0 <= int(m.group(1)) < NLANES:
        return int(m.group(1))
    return None


def find_o0(doc: Any) -> list[Fraction] | None:
    strong = ("o0", "obstruction0", "obstruction_0", "base_obstruction", "canonical_obstruction", "canonical_o0")
    candidates: list[tuple[int, str, list[Fraction]]] = []
    for path, obj in walk(doc):
        v = parse_vector(obj, NROWS)
        if v is None:
            continue
        p = lower_key_path(path)
        score = 0
        if any(tok in p for tok in strong):
            score += 100
        if "obstruction" in p:
            score += 30
        if "base" in p or "canonical" in p:
            score += 20
        candidates.append((score, path, v))
    if not candidates:
        return None
    candidates.sort(key=lambda t: (-t[0], t[1]))
    if candidates[0][0] < 30:
        return None
    return candidates[0][2]


def find_index_list(doc: Any) -> list[int] | None:
    aliases = ("column_indices", "columns_indices", "homogeneous_indices", "parameter_indices", "basis_indices", "column_ids")
    for path, obj in walk(doc):
        p = lower_key_path(path)
        if not any(tok in p for tok in aliases):
            continue
        if isinstance(obj, list) and obj and all(isinstance(x, int) and not isinstance(x, bool) for x in obj):
            if all(0 <= x < NCOLS for x in obj) and len(set(obj)) == len(obj):
                return list(obj)
    # Explicit start/end or start/count metadata.
    for _, obj in walk(doc):
        if not isinstance(obj, dict):
            continue
        norm = {str(k).lower().replace("-", "_"): v for k, v in obj.items()}
        start = next((norm[k] for k in ("column_start", "start_column", "col_start") if k in norm), None)
        end = next((norm[k] for k in ("column_end", "end_column", "col_end") if k in norm), None)
        count = next((norm[k] for k in ("column_count", "ncolumns", "ncols") if k in norm), None)
        if isinstance(start, int) and isinstance(end, int) and 0 <= start <= end < NCOLS:
            return list(range(start, end + 1))
        if isinstance(start, int) and isinstance(count, int) and count > 0 and 0 <= start < NCOLS and start + count <= NCOLS:
            return list(range(start, start + count))
    return None


def find_column_records(doc: Any) -> tuple[list[int], list[list[Fraction]]] | None:
    for path, obj in walk(doc):
        p = lower_key_path(path)
        if not isinstance(obj, list) or not obj or not all(isinstance(x, dict) for x in obj):
            continue
        if not any(tok in p for tok in ("column", "obstruction", "linear_map", ".b")):
            continue
        idxs: list[int] = []
        cols: list[list[Fraction]] = []
        ok = True
        for rec in obj:
            norm = {str(k).lower().replace("-", "_"): v for k, v in rec.items()}
            idx = next((norm[k] for k in ("index", "column", "column_index", "basis_index", "parameter_index") if k in norm), None)
            vec_obj = next((norm[k] for k in ("vector", "values", "obstruction", "delta", "column_values") if k in norm), None)
            vec = parse_vector(vec_obj, NROWS)
            if not isinstance(idx, int) or not (0 <= idx < NCOLS) or vec is None:
                ok = False
                break
            idxs.append(idx)
            cols.append(vec)
        if ok and len(set(idxs)) == len(idxs):
            return idxs, cols
    return None


def find_matrix_block(doc: Any, idxs: list[int] | None) -> tuple[list[int], list[list[Fraction]]] | None:
    records = find_column_records(doc)
    if records is not None:
        return records

    candidates: list[tuple[int, str, list[list[Fraction]], bool]] = []
    for path, obj in walk(doc):
        shp = matrix_shape(obj)
        if shp is None:
            continue
        r, c = shp
        if r != NROWS and c != NROWS:
            continue
        p = lower_key_path(path)
        score = 0
        if any(tok in p for tok in ("obstruction_matrix", "linear_map", "b_block", ".b", "columns")):
            score += 50
        if "obstruction" in p:
            score += 25
        if idxs is not None and ((r == NROWS and c == len(idxs)) or (c == NROWS and r == len(idxs))):
            score += 100
        mat = parse_matrix(obj)
        if mat is not None:
            candidates.append((score, path, mat, r != NROWS))
    if not candidates:
        return None
    candidates.sort(key=lambda t: (-t[0], t[1]))
    score, _, mat, transposed = candidates[0]
    if score < 50:
        return None
    if transposed:
        # rows are columns: k x 1456 -> list of k column vectors already
        cols = mat
    else:
        # 1456 x k -> transpose to list of k column vectors
        cols = [list(col) for col in zip(*mat)]
    if idxs is None:
        return None
    if len(cols) != len(idxs):
        return None
    return idxs, cols


def load_docs(root: Path) -> list[tuple[Path, Any]]:
    docs: list[tuple[Path, Any]] = []
    for p in sorted(root.rglob("*.json")):
        try:
            docs.append((p, json.loads(p.read_text(encoding="utf-8"))))
        except Exception:
            continue
    return docs


def extract_lane(root: Path) -> dict[str, Any] | None:
    docs = load_docs(root)
    if not docs:
        return None
    # Prefer a single document that contains both O0 and a matrix block.
    best: dict[str, Any] | None = None
    for p, doc in docs:
        lane = find_lane_number(doc, p.name)
        o0 = find_o0(doc)
        idxs = find_index_list(doc)
        block = find_matrix_block(doc, idxs)
        if o0 is not None and block is not None:
            bidxs, cols = block
            cand = {"lane": lane, "o0": o0, "indices": bidxs, "columns": cols, "source": str(p)}
            if best is None or len(cols) > len(best["columns"]):
                best = cand
    if best is not None:
        return best

    # Allow O0 and the block to live in separate JSON files in the same artifact.
    o0 = None
    lane = None
    for p, doc in docs:
        if lane is None:
            lane = find_lane_number(doc, p.name)
        if o0 is None:
            o0 = find_o0(doc)
    for p, doc in docs:
        idxs = find_index_list(doc)
        block = find_matrix_block(doc, idxs)
        if block is not None and o0 is not None:
            bidxs, cols = block
            return {"lane": lane, "o0": o0, "indices": bidxs, "columns": cols, "source": str(p)}
    return None


def frac_text(x: Fraction) -> str:
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def write_result(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def exact_ranks(Bcols: list[list[Fraction]], o0: list[Fraction]) -> tuple[int, int]:
    # python-flint is the primary exact backend for the dense global ranks.
    try:
        from flint import fmpq, fmpq_mat  # type: ignore

        flat_B = [fmpq(v.numerator, v.denominator) for i in range(NROWS) for v in (Bcols[j][i] for j in range(NCOLS))]
        flat_A = []
        for i in range(NROWS):
            flat_A.extend(fmpq(Bcols[j][i].numerator, Bcols[j][i].denominator) for j in range(NCOLS))
            rhs = -o0[i]
            flat_A.append(fmpq(rhs.numerator, rhs.denominator))
        Bm = fmpq_mat(NROWS, NCOLS, flat_B)
        Am = fmpq_mat(NROWS, NCOLS + 1, flat_A)
        return int(Bm.rank()), int(Am.rank())
    except Exception as exc:
        print(f"python-flint rank backend unavailable/failed: {exc}; falling back to SymPy", file=sys.stderr)

    from sympy import Matrix, Rational  # type: ignore

    rows_B = [[Rational(Bcols[j][i].numerator, Bcols[j][i].denominator) for j in range(NCOLS)] for i in range(NROWS)]
    rows_A = [row + [Rational(-o0[i].numerator, o0[i].denominator)] for i, row in enumerate(rows_B)]
    return int(Matrix(rows_B).rank()), int(Matrix(rows_A).rank())


def exact_witness(Bcols: list[list[Fraction]], o0: list[Fraction]) -> list[Fraction]:
    # Only reached if exact ranks prove consistency.  Use SymPy's exact solver,
    # set all free parameters to zero, then verify directly with Fraction.
    from sympy import Matrix, Rational  # type: ignore

    rows_B = [[Rational(Bcols[j][i].numerator, Bcols[j][i].denominator) for j in range(NCOLS)] for i in range(NROWS)]
    rhs = Matrix([Rational(-x.numerator, x.denominator) for x in o0])
    sol, params = Matrix(rows_B).gauss_jordan_solve(rhs)
    substitutions = {s: 0 for s in params.free_symbols}
    sol = sol.subs(substitutions)
    out = [Fraction(int(v.p), int(v.q)) for v in sol]
    if len(out) != NCOLS:
        raise RuntimeError("exact witness has wrong dimension")
    for i in range(NROWS):
        total = o0[i]
        for j, h in enumerate(out):
            if h:
                total += Bcols[j][i] * h
        if total != 0:
            raise RuntimeError(f"exact witness replay failed at compatibility row {i}")
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--source", required=True, type=Path)
    ap.add_argument("--manifest", required=True, type=Path)
    ap.add_argument("--output", required=True, type=Path)
    args = ap.parse_args()

    manifest = json.loads(args.manifest.read_text(encoding="utf-8"))
    artifacts = manifest.get("artifacts", [])
    base = {
        "gate": "ITER057AE-FULL-R12-BRANCH-OBSTRUCTION-AGGREGATE",
        "preregistration_commit": "60f50bcf9002631e44e16e758a75b9bdb14b0ed3",
        "source_run": 35070896151,
        "source_head": "041fb0046d92e5a9800dd99b0ce4e8b841242df5",
        "source_artifacts": artifacts,
        "exact_arithmetic": True,
        "nrows": NROWS,
        "ncols": NCOLS,
    }

    if manifest.get("run_id") != 35070896151 or manifest.get("head_sha") != "041fb0046d92e5a9800dd99b0ce4e8b841242df5":
        write_result(args.output, {**base, "classification": INVALID, "reason": "source run/head provenance mismatch"})
        return 0
    if len(artifacts) != NLANES:
        write_result(args.output, {**base, "classification": BLOCKED, "reason": f"expected exactly 8 source artifacts, found {len(artifacts)}"})
        return 0
    if len({a.get("id") for a in artifacts}) != NLANES or len({a.get("name") for a in artifacts}) != NLANES:
        write_result(args.output, {**base, "classification": INVALID, "reason": "duplicate artifact id or name"})
        return 0

    extracted: list[dict[str, Any]] = []
    for art in artifacts:
        root = args.source / f"artifact-{art['id']}"
        lane = extract_lane(root)
        if lane is None:
            write_result(args.output, {**base, "classification": BLOCKED, "reason": f"artifact {art['id']} does not expose an exact O0 plus obstruction-column block"})
            return 0
        lane["artifact_id"] = art["id"]
        lane["artifact_name"] = art["name"]
        extracted.append(lane)

    lane_numbers = [x.get("lane") for x in extracted]
    known_lanes = [x for x in lane_numbers if x is not None]
    if known_lanes and (len(known_lanes) != NLANES or set(known_lanes) != set(range(NLANES))):
        write_result(args.output, {**base, "classification": INVALID, "reason": f"lane provenance is not exactly 0..7: {lane_numbers}"})
        return 0

    o0 = extracted[0]["o0"]
    if any(x["o0"] != o0 for x in extracted[1:]):
        write_result(args.output, {**base, "classification": INVALID, "reason": "lane artifacts disagree on canonical O0"})
        return 0
    o0_nnz = sum(x != 0 for x in o0)
    if o0_nnz != EXPECTED_O0_NONZERO:
        write_result(args.output, {**base, "classification": INVALID, "reason": f"canonical h=0 replay mismatch: expected {EXPECTED_O0_NONZERO} nonzero compatibility contractions, found {o0_nnz}"})
        return 0

    columns: dict[int, list[Fraction]] = {}
    source_for_column: dict[int, int] = {}
    for lane in extracted:
        for idx, col in zip(lane["indices"], lane["columns"]):
            if idx in columns:
                write_result(args.output, {**base, "classification": INVALID, "reason": f"duplicate homogeneous column {idx}"})
                return 0
            if len(col) != NROWS:
                write_result(args.output, {**base, "classification": INVALID, "reason": f"column {idx} has wrong row count"})
                return 0
            columns[idx] = col
            source_for_column[idx] = lane["artifact_id"]

    expected = set(range(NCOLS))
    got = set(columns)
    if got != expected:
        missing = sorted(expected - got)
        extra = sorted(got - expected)
        write_result(args.output, {**base, "classification": BLOCKED, "reason": "eight artifacts do not cover the complete frozen 1114-column basis", "missing_columns": missing[:100], "extra_columns": extra[:100], "covered_count": len(got)})
        return 0

    Bcols = [columns[j] for j in range(NCOLS)]
    rank_B, rank_aug = exact_ranks(Bcols, o0)
    payload: dict[str, Any] = {
        **base,
        "canonical_o0_nonzero_count": o0_nnz,
        "coverage_count": len(columns),
        "rank_B": rank_B,
        "rank_augmented": rank_aug,
        "column_artifact_ids": [source_for_column[j] for j in range(NCOLS)],
    }

    if rank_aug > rank_B:
        payload.update({"classification": FAIL, "decision": "exact affine obstruction system inconsistent"})
        write_result(args.output, payload)
        return 0
    if rank_aug < rank_B:
        payload.update({"classification": INVALID, "reason": "impossible exact rank ordering rank([B|-O0]) < rank(B)"})
        write_result(args.output, payload)
        return 0

    try:
        h = exact_witness(Bcols, o0)
    except Exception as exc:
        payload.update({"classification": BLOCKED, "reason": f"consistent exact ranks but exact branch witness was not technically realized: {exc}"})
        write_result(args.output, payload)
        return 0

    payload.update({
        "classification": PASS,
        "decision": "complete exact obstruction map admits a rational homogeneous branch; unrestricted R14 response remains untested",
        "branch_nonzero_count": sum(x != 0 for x in h),
        "branch_witness": [frac_text(x) for x in h],
        "witness_replay_all_1456_zero": True,
    })
    write_result(args.output, payload)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
