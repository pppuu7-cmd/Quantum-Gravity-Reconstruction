#!/usr/bin/env python3
"""Iter057C: exact reduced null-cone two-block pencil maximal-minor GCD certificate."""
import argparse
import itertools
import json
from pathlib import Path
import sympy as sp

import qgr_iter057a_null_cone_kernel_intersection as a57

core = a57.core
GATE = "ITER057C-NULL-CONE-REDUCED-TWO-BLOCK-PENCIL-MAXIMAL-MINOR-GCD-CERTIFICATE"
PREREG = "c2e0c2b867cb4fbd286dfff315eb9798d136a0f3"
PASS_CLASS = "PASS_SCOPED_ITER057C_TWO_BLOCK_NULL_CONE_PENCIL_RANK5_FOR_ALL_NONZERO_SYMBOLIC_MULTIPLIERS_ON_FROZEN_PANEL"
FAIL_CLASS = "SCIENTIFIC_FAIL_ITER057C_TWO_BLOCK_PENCIL_HAS_NONZERO_SYMBOLIC_RANK_DROP_ON_FROZEN_PANEL"
INVALID_CLASS = "INVALID_ITER057C_REDUCED_PENCIL_OR_GCD_CERTIFICATE"
LAM = sp.symbols("lambda")
INTERP_NODES = tuple(range(6))
VERIFY_NODE = 6
ROW_SUBSETS = tuple(itertools.combinations(range(10),5))


def deterministic_complement(common_kernel):
    cur = common_kernel.copy()
    cols = []
    r = cur.rank()
    for j in range(10):
        e = sp.zeros(10,1); e[j,0] = 1
        test = cur.row_join(e)
        rt = test.rank()
        if rt > r:
            cols.append(e)
            cur = test
            r = rt
        if len(cols) == 5:
            break
    B = sp.Matrix.hstack(*cols) if cols else sp.zeros(10,0)
    return B, cur


def det_at(U0,U1,rows,n):
    return sp.cancel((U0.extract(rows,range(5)) + sp.Integer(n)*U1.extract(rows,range(5))).det(method="domain-ge"))


def interpolated_minor(U0,U1,rows):
    values = [det_at(U0,U1,rows,n) for n in INTERP_NODES]
    expr = sp.expand(sp.interpolate([(sp.Integer(n),values[n]) for n in INTERP_NODES], LAM))
    poly = sp.Poly(expr,LAM,domain=sp.QQ)
    verify = det_at(U0,U1,rows,VERIFY_NODE)
    ok = sp.simplify(poly.eval(VERIFY_NODE)-verify) == 0
    return poly, ok


def pure_lambda_power(poly):
    p = poly.monic()
    if p.is_zero:
        return False, None
    d = p.degree()
    if d < 1:
        return False, d
    return bool(p.as_expr() == LAM**d), d


def run_case(null_index,seed):
    k = a57.NULL_K[null_index]
    M2 = a57.einstein_symbol_matrix(k)
    K = a57.pure_gauge_columns(k)
    M4,_ = core.q_matrix(core.background_operator(seed),k)
    stacked = M2.col_join(M4)
    common = stacked.nullspace()
    N = sp.Matrix.hstack(*common) if common else sp.zeros(10,0)
    common_dim = N.cols
    B,NB = deterministic_complement(N)

    controls = bool(
        a57.k2(k)==0 and K.rank()==4 and M2.rank()==4 and M4.rank()==4 and
        M2*K==sp.zeros(10,4) and M4*K==sp.zeros(10,4) and
        common_dim==5 and stacked.rank()==5 and (M2+M4).rank()==5 and
        B.cols==5 and NB.rank()==10 and M2*N==sp.zeros(10,5) and M4*N==sp.zeros(10,5)
    )
    if not controls:
        return {
            "null_k_index":null_index,"seed":seed,"controls_valid":False,
            "common_kernel_dim":common_dim,"complement_cols":B.cols,"NB_rank":int(NB.rank()),
        }

    U0 = M2*B
    U1 = M4*B
    nonzero = 0
    zero = 0
    interp_invalid = []
    gcd_poly = None
    first_nonzero = None
    last_gcd = None

    for idx,rows in enumerate(ROW_SUBSETS):
        poly,ok = interpolated_minor(U0,U1,rows)
        if not ok:
            interp_invalid.append(idx)
            continue
        if poly.is_zero:
            zero += 1
            continue
        nonzero += 1
        if first_nonzero is None:
            first_nonzero = {"row_subset":list(rows),"poly":str(sp.factor(poly.as_expr()))}
        gcd_poly = poly.monic() if gcd_poly is None else sp.gcd(gcd_poly,poly).monic()
        last_gcd = gcd_poly

    interpolation_valid = not interp_invalid and (nonzero+zero == len(ROW_SUBSETS))
    gcd_exists = gcd_poly is not None
    pure_power,power = pure_lambda_power(gcd_poly) if gcd_exists else (False,None)
    rank_zero = int(M2.rank())
    rank_one = int((M2+M4).rank())

    extra_factor = None
    rational_root_checks = []
    if gcd_exists:
        gexpr = sp.factor(gcd_poly.as_expr())
        if not pure_power:
            # Remove the maximal explicit lambda power and retain the exact residual factor.
            terms = sp.Poly(gcd_poly,LAM).terms()
            min_exp = min(t[0][0] for t in terms)
            extra_factor = sp.factor(gexpr / (LAM**min_exp))
            # Only exact rational roots are direct-rank checked, as frozen in the preregistration.
            for rr in sp.roots(sp.Poly(extra_factor,LAM)):
                if rr.is_Rational and rr != 0:
                    rational_root_checks.append({"root":str(rr),"full_rank":int((M2+rr*M4).rank())})

    valid = bool(interpolation_valid and gcd_exists and rank_zero==4 and rank_one==5)
    return {
        "null_k_index":null_index,
        "seed":seed,
        "controls_valid":controls,
        "quotient_construction_valid":bool(B.cols==5 and NB.rank()==10),
        "common_kernel_dim":common_dim,
        "maximal_minor_count":len(ROW_SUBSETS),
        "nonzero_minor_polynomial_count":nonzero,
        "zero_minor_polynomial_count":zero,
        "interpolation_verification_valid":interpolation_valid,
        "interpolation_invalid_indices":interp_invalid,
        "gcd_exists":gcd_exists,
        "gcd_monic_factor":str(sp.factor(gcd_poly.as_expr())) if gcd_exists else None,
        "gcd_is_pure_lambda_power":pure_power,
        "gcd_lambda_power":power,
        "extra_gcd_factor":str(extra_factor) if extra_factor is not None else None,
        "rational_extra_root_full_rank_checks":rational_root_checks,
        "rank_at_lambda_0":rank_zero,
        "rank_at_lambda_1":rank_one,
        "first_nonzero_minor":first_nonzero,
        "case_valid":valid,
    }


def run():
    cases=[]
    invalid=[]
    nonzero_rankdrop=[]
    for ni in range(2):
        for seed in range(12):
            row=run_case(ni,seed)
            cases.append(row)
            if not row.get("controls_valid") or not row.get("case_valid"):
                invalid.append([ni,seed])
            elif not row.get("gcd_is_pure_lambda_power"):
                nonzero_rankdrop.append([ni,seed])
    if invalid:
        cls=INVALID_CLASS
    elif nonzero_rankdrop:
        cls=FAIL_CLASS
    else:
        cls=PASS_CLASS
    return {
        "gate":GATE,
        "preregistration_commit":PREREG,
        "classification":cls,
        "implementation_valid":not bool(invalid),
        "case_count":len(cases),
        "invalid_cases":invalid,
        "nonzero_rankdrop_factor_cases":nonzero_rankdrop,
        "pure_lambda_gcd_case_count":sum(bool(r.get("gcd_is_pure_lambda_power")) for r in cases),
        "all_252_minors_interpolation_verified_case_count":sum(bool(r.get("interpolation_verification_valid")) for r in cases),
        "cases":cases,
        "claim_ceiling":"EXACT TWO-BLOCK REDUCED-PENCIL MAXIMAL-MINOR GCD CERTIFICATE ONLY; LOWER-DEGREE WEYL3/FULL CHARACTERISTICS/HYPERBOLICITY/GHOST/TREATMENT NOT ESTABLISHED; C6 SYMBOLIC UNFIXED; THEORY_ESTABLISHED_0",
    }


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--out',required=True); args=ap.parse_args()
    out=run(); Path(args.out).parent.mkdir(parents=True,exist_ok=True)
    Path(args.out).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k!='cases'},sort_keys=True))
    if not out['implementation_valid']:
        raise SystemExit(2)

if __name__=='__main__':
    main()
