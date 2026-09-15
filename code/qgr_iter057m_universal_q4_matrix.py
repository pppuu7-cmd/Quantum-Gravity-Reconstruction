#!/usr/bin/env python3
"""Iter057M source-independent exact Q4 matrix in the frozen normalized Taylor basis."""
import argparse
import json
from itertools import product
from pathlib import Path

import sympy as sp

GATE = "ITER057M-GENERAL-QAB-SECOND-EVEN-JET-QUARTIC-EXTENSION"
ARCH = "19e76eb481d1cfd6c77b168ebe6320822510624b"
RANK_DERIVATION = "5a00b06241c3bc034c02bb8d8abe9a1bd63c599a"
PAIRS = [(0,0),(0,1),(0,2),(0,3),(1,1),(1,2),(1,3),(2,2),(2,3),(3,3)]
ETA = (-1,1,1,1)


def alphas(n):
    return sorted(a for a in product(range(n+1), repeat=4) if sum(a) == n)


def pair_index(a,b):
    if a > b:
        a,b = b,a
    return PAIRS.index((a,b))


def assemble():
    a2, a3, a4 = alphas(2), alphas(3), alphas(4)
    col = {(p,al): p*len(a4)+j for p in range(10) for j,al in enumerate(a4)}
    rows = []
    meta = []

    for b in range(4):
        for al in a3:
            d = {}
            for a in range(4):
                beta = list(al); beta[a] += 1; beta = tuple(beta)
                j = col[(pair_index(a,b), beta)]
                d[j] = d.get(j, 0) + ETA[a]
            rows.append(d)
            meta.append(("G", b, al))

    for p,pair in enumerate(PAIRS):
        for al in a2:
            d = {}
            for m in range(4):
                beta = list(al); beta[m] += 2; beta = tuple(beta)
                j = col[(p, beta)]
                d[j] = d.get(j, 0) - sp.Rational(ETA[m], 2)
            rows.append(d)
            meta.append(("F", pair, al))

    entries = {(i,j):v for i,d in enumerate(rows) for j,v in d.items() if v != 0}
    M = sp.MutableSparseMatrix(180, 350, entries)
    return M, meta, a4


def encode_meta(x):
    kind, idx, al = x
    if kind == "G":
        return {"kind":"G", "b":int(idx), "alpha":list(al)}
    return {"kind":"F", "pair":list(idx), "alpha":list(al)}


def summary():
    M, meta, a4 = assemble()
    rank = M.rank()
    left = M.T.nullspace()
    relations = []
    for v in left:
        support = []
        for i in range(M.rows):
            if v[i] != 0:
                support.append({"row":i, "meta":encode_meta(meta[i]), "coefficient":str(v[i])})
        relations.append(support)
    return {
        "gate":GATE,
        "architecture_commit":ARCH,
        "rank_derivation_commit":RANK_DERIVATION,
        "shape":[M.rows,M.cols],
        "nnz":len(M.todok()),
        "rank":rank,
        "nullity":M.cols-rank,
        "left_nullity":len(left),
        "left_null_relations":relations,
        "all_left_relations_have_eight_rows":all(len(s)==8 for s in relations),
        "exact_rank_uses_tolerance":False,
    }


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--out")
    args=ap.parse_args()
    out=summary()
    text=json.dumps(out,indent=2,sort_keys=True)+"\n"
    if args.out:
        Path(args.out).parent.mkdir(parents=True,exist_ok=True)
        Path(args.out).write_text(text)
    print(text,end="")
    if out["shape"] != [180,350] or out["rank"] != 164 or out["left_nullity"] != 16:
        raise SystemExit(2)


if __name__ == "__main__":
    main()
