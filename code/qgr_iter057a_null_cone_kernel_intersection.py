#!/usr/bin/env python3
"""Iter057A: exact null-cone Einstein/Weyl3 quotient-kernel intersection audit."""
import argparse
import json
from pathlib import Path
import sympy as sp

import qgr_iter054c_local_metric_principal_symbol_retry as retry

core = retry.core
ETA = core.ETA
GATE = "ITER057A-NULL-CONE-EINSTEIN-WEYL3-QUOTIENT-KERNEL-INTERSECTION"
PREREG = "100849c18508b89cc36dade42ed18053916097c7"
PASS_CLASS = "PASS_SCOPED_ITER057A_GR_AND_WEYL3_SHARE_TWO_NONGAUGE_NULL_CONE_KERNEL_CLASSES_ON_FROZEN_PANEL"
FAIL_CLASS = "SCIENTIFIC_FAIL_ITER057A_COMMON_NULL_CONE_KERNEL_HYPOTHESIS_ON_FROZEN_PANEL"
INVALID_CLASS = "INVALID_ITER057A_NULL_CONE_SYMBOL_OR_PROVENANCE_CONTROL"
NULL_K = [
    [sp.Integer(1), sp.Integer(1), sp.Integer(0), sp.Integer(0)],
    [sp.Integer(5), sp.Integer(3), sp.Integer(4), sp.Integer(0)],
]


def k2(k):
    return sp.simplify(sum(ETA[a,b]*k[a]*k[b] for a in range(4) for b in range(4)))


def vec_h(h):
    return sp.Matrix([h[a,b] for a,b in core.SYM_BASIS])


def pure_gauge_columns(k):
    K = sp.zeros(10,4)
    for r in range(4):
        xi = [sp.Integer(1) if i == r else sp.Integer(0) for i in range(4)]
        h = sp.zeros(4)
        for a in range(4):
            for b in range(4):
                h[a,b] = sp.expand(k[a]*xi[b] + k[b]*xi[a])
        K[:,r] = vec_h(h)
    return K


def einstein_symbol_matrix(k):
    """Coordinate-output matrix for the principal linearized Einstein tensor."""
    M = sp.zeros(10)
    for j in range(10):
        h = core.symmetric_h(j)
        R = core.riemann_principal(k,h)
        Ric = sp.zeros(4)
        for b in range(4):
            for d in range(4):
                Ric[b,d] = sp.simplify(sum(ETA[a,c]*R[a,b,c,d] for a in range(4) for c in range(4)))
        scal = sp.simplify(sum(ETA[b,d]*Ric[b,d] for b in range(4) for d in range(4)))
        G = sp.zeros(4)
        for b in range(4):
            for d in range(4):
                G[b,d] = sp.simplify(Ric[b,d] - sp.Rational(1,2)*ETA[b,d]*scal)
        M[:,j] = vec_h(G)
    return M


def physical_kernel_complement(M2,K):
    """Choose two exact columns extending gauge K to a basis of ker(M2)."""
    ns = M2.nullspace()
    B = K.copy()
    rank = B.rank()
    phys = []
    for col in ns:
        T = B.row_join(col)
        if T.rank() > rank:
            phys.append(col)
            B = T
            rank += 1
        if len(phys) == 2:
            break
    P = sp.Matrix.hstack(*phys) if phys else sp.zeros(10,0)
    return ns,P,B


def run():
    cases = []
    invalid = []
    scientific_fail = []
    second_checks = []

    for ni,k in enumerate(NULL_K):
        M2 = einstein_symbol_matrix(k)
        K = pure_gauge_columns(k)
        n2,P,B = physical_kernel_complement(M2,K)
        null_control = (k2(k) == 0)
        gauge_rank = int(K.rank())
        rank_m2 = int(M2.rank())
        m2_gauge_zero = (M2*K == sp.zeros(10,4))
        phys_basis_valid = (len(n2) == 6 and P.cols == 2 and B.rank() == 6)

        for seed in range(12):
            W = core.background_operator(seed)
            M4,_ = core.q_matrix(W,k)
            rank_m4 = int(M4.rank())
            m4_gauge_zero = (M4*K == sp.zeros(10,4))
            intersection_dim = int(10 - M2.col_join(M4).rank())
            q_intersection_dim = int(intersection_dim - gauge_rank)
            map_rank_on_gr_phys = int((M4*P).rank()) if phys_basis_valid else None
            bilinear_rank_on_gr_phys = int((P.T*M4*P).rank()) if phys_basis_valid else None

            controls_valid = bool(
                null_control and gauge_rank == 4 and rank_m2 == 4 and
                m2_gauge_zero and rank_m4 == 4 and m4_gauge_zero and phys_basis_valid
            )
            hypothesis_pass = bool(controls_valid and q_intersection_dim == 2)

            row = {
                "null_k_index": ni,
                "k": [str(x) for x in k],
                "seed": seed,
                "k2_exact_zero": bool(null_control),
                "gauge_rank": gauge_rank,
                "rank_M2": rank_m2,
                "nullity_M2": 10-rank_m2,
                "rank_M4": rank_m4,
                "nullity_M4": 10-rank_m4,
                "M2_gauge_zero": bool(m2_gauge_zero),
                "M4_gauge_zero": bool(m4_gauge_zero),
                "full_kernel_intersection_dim": intersection_dim,
                "quotient_kernel_intersection_dim": q_intersection_dim,
                "M4_map_rank_on_two_GR_nongauge_kernel_classes": map_rank_on_gr_phys,
                "M4_bilinear_rank_on_two_GR_nongauge_kernel_classes": bilinear_rank_on_gr_phys,
                "controls_valid": controls_valid,
                "hypothesis_pass": hypothesis_pass,
            }
            cases.append(row)
            if not controls_valid:
                invalid.append([ni,seed])
            elif not hypothesis_pass:
                scientific_fail.append([ni,seed])

        second_checks.append({
            "null_k_index": ni,
            "Einstein_kernel_dim": len(n2),
            "gauge_rank": gauge_rank,
            "nongauge_Einstein_kernel_complement_dim": P.cols,
            "kernel_basis_total_rank": int(B.rank()),
        })

    if invalid:
        classification = INVALID_CLASS
    elif scientific_fail:
        classification = FAIL_CLASS
    else:
        classification = PASS_CLASS

    return {
        "gate": GATE,
        "preregistration_commit": PREREG,
        "classification": classification,
        "implementation_valid": not bool(invalid),
        "scientific_hypothesis_pass": classification == PASS_CLASS,
        "case_count": len(cases),
        "invalid_cases": invalid,
        "scientific_fail_cases": scientific_fail,
        "unique_quotient_intersection_dims": sorted(set(r["quotient_kernel_intersection_dim"] for r in cases)),
        "unique_M4_map_ranks_on_GR_physical_kernel": sorted(set(r["M4_map_rank_on_two_GR_nongauge_kernel_classes"] for r in cases)),
        "unique_M4_bilinear_ranks_on_GR_physical_kernel": sorted(set(r["M4_bilinear_rank_on_two_GR_nongauge_kernel_classes"] for r in cases)),
        "second_checks": second_checks,
        "cases": cases,
        "claim_ceiling": "FROZEN EXACT 24-CASE NULL-CONE KERNEL-INTERSECTION AUDIT ONLY; NO GLOBAL CHARACTERISTIC/HYPERBOLICITY/GHOST/TREATMENT/UNITARITY CLAIM; C6 SYMBOLIC UNFIXED; THEORY_ESTABLISHED_0",
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    args = ap.parse_args()
    out = run()
    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    Path(args.out).write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
    print(json.dumps({k:v for k,v in out.items() if k != "cases"}, sort_keys=True))
    if not out["implementation_valid"]:
        raise SystemExit(2)


if __name__ == "__main__":
    main()
