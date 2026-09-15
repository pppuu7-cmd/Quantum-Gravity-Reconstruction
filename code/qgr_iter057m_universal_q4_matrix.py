#!/usr/bin/env python3
"""Iter057M source-independent exact Q4 matrix in the frozen normalized Taylor basis."""
import argparse
import json
from itertools import product
from pathlib import Path

import sympy as sp

GATE = "ITER057M-GENERAL-QAB-SECOND-EVEN-JET-QUARTIC-EXTENSION"
ARCH = "19e76eb481d1cfd6c77b168ebe6320822510624b"
RANK_DERIVATION = "8a6a5a56f646b4c96fec4ac50ab392203d26475a"
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


def canonical_bianchi_basis(meta):
    lookup = {m:i for i,m in enumerate(meta)}
    vecs = []
    labels = []
    for b in range(4):
        for j in range(4):
            v = sp.zeros(180,1)
            for m in range(4):
                al = [0,0,0,0]; al[m] += 2; al[j] += 1
                v[lookup[("G",b,tuple(al))]] += sp.Rational(ETA[m],2)
            for a in range(4):
                al = [0,0,0,0]; al[a] += 1; al[j] += 1
                pair = (a,b) if a <= b else (b,a)
                v[lookup[("F",pair,tuple(al))]] += ETA[a]
            vecs.append(v)
            labels.append((b,j))
    return vecs, labels


def support(v,meta):
    return [
        {"row":i,"meta":encode_meta(meta[i]),"coefficient":str(v[i])}
        for i in range(len(meta)) if v[i] != 0
    ]


def summary():
    M, meta, a4 = assemble()
    rank = M.rank()
    raw_left = M.T.nullspace()
    canonical, labels = canonical_bianchi_basis(meta)
    Y = sp.Matrix.hstack(*canonical).T
    canonical_zero = all(v.T*M == sp.zeros(1,M.cols) for v in canonical)
    canonical_support = []
    for label,v in zip(labels,canonical):
        canonical_support.append({"b":label[0],"j":label[1],"support":support(v,meta)})
    return {
        "gate":GATE,
        "architecture_commit":ARCH,
        "rank_derivation_commit":RANK_DERIVATION,
        "shape":[M.rows,M.cols],
        "nnz":len(M.todok()),
        "rank":rank,
        "nullity":M.cols-rank,
        "left_nullity":len(raw_left),
        "raw_cas_left_null_support_sizes":[len(support(v,meta)) for v in raw_left],
        "canonical_bianchi_count":len(canonical),
        "canonical_bianchi_rank":Y.rank(),
        "canonical_bianchi_all_annihilate_M":canonical_zero,
        "canonical_bianchi_all_have_eight_rows":all(len(x["support"])==8 for x in canonical_support),
        "canonical_bianchi_relations":canonical_support,
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
    required=(out["shape"]==[180,350] and out["rank"]==164 and out["left_nullity"]==16
              and out["canonical_bianchi_count"]==16 and out["canonical_bianchi_rank"]==16
              and out["canonical_bianchi_all_annihilate_M"] and out["canonical_bianchi_all_have_eight_rows"])
    if not required:
        raise SystemExit(2)


if __name__ == "__main__":
    main()
