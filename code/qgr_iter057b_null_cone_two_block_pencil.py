#!/usr/bin/env python3
"""Iter057B: symbolic null-cone two-block Einstein/Weyl3 pencil rank audit."""
import argparse
import json
from pathlib import Path
import sympy as sp

import qgr_iter057a_null_cone_kernel_intersection as a57

core = a57.core
GATE = "ITER057B-NULL-CONE-TWO-BLOCK-EINSTEIN-WEYL3-SYMBOLIC-PENCIL-RANK"
PREREG = "9045d51c4b542122c171756488333e20655012a4"
PASS_CLASS = "PASS_SCOPED_ITER057B_NULL_CONE_TWO_BLOCK_PENCIL_RANK5_FOR_ALL_NONZERO_SYMBOLIC_MULTIPLIER_ON_FROZEN_PANEL"
PARTIAL_CLASS = "PARTIAL_SCOPED_ITER057B_GENERIC_NONZERO_MULTIPLIER_RANK5_ALL_NONZERO_NOT_CERTIFIED"
FAIL_CLASS = "SCIENTIFIC_FAIL_ITER057B_TWO_BLOCK_RANK5_HYPOTHESIS_ON_FROZEN_PANEL"
INVALID_CLASS = "INVALID_ITER057B_ITER057A_OBJECT_OR_PROVENANCE_CONTROL"


def run():
    lam = sp.symbols("lambda")
    rows=[]
    invalid=[]
    generic_fail=[]
    all_nonzero_unproved=[]

    for ni,k in enumerate(a57.NULL_K):
        M2=a57.einstein_symbol_matrix(k)
        K=a57.pure_gauge_columns(k)
        for seed in range(12):
            M4,_=core.q_matrix(core.background_operator(seed),k)
            common_dim=10-M2.col_join(M4).rank()
            controls=bool(
                a57.k2(k)==0 and K.rank()==4 and M2.rank()==4 and M4.rank()==4 and
                M2*K==sp.zeros(10,4) and M4*K==sp.zeros(10,4) and common_dim==5
            )
            M1=M2+M4
            rank_at_one=int(M1.rank())
            generic_rank5=False
            det_factor=None
            minor_rows=[]; minor_cols=[]; monomial=False

            if controls and rank_at_one==5:
                # A nonzero exact 5x5 minor polynomial certifies rank 5 over Q(lambda).
                minor_cols=list(M1.rref()[1])
                if len(minor_cols)==5:
                    minor_rows=list(M1[:,minor_cols].T.rref()[1])
                if len(minor_rows)==5:
                    det_factor=sp.factor((M2+lam*M4).extract(minor_rows,minor_cols).det())
                    generic_rank5=bool(det_factor!=0)
                    if generic_rank5:
                        poly=sp.Poly(sp.expand(det_factor),lam)
                        terms=poly.terms()
                        monomial=bool(len(terms)==1 and terms[0][0][0]>=1 and terms[0][1]!=0)

            if not controls:
                invalid.append([ni,seed])
            elif not generic_rank5:
                generic_fail.append([ni,seed])
            elif not monomial:
                all_nonzero_unproved.append([ni,seed])

            rows.append({
                "null_k_index":ni,
                "seed":seed,
                "controls_valid":controls,
                "rank_M2":int(M2.rank()),
                "rank_M4":int(M4.rank()),
                "common_kernel_dim":int(common_dim),
                "rank_at_lambda_1":rank_at_one,
                "generic_rank5_certified_by_nonzero_minor_polynomial":generic_rank5,
                "frozen_candidate_minor_rows":minor_rows,
                "frozen_candidate_minor_cols":minor_cols,
                "candidate_minor_factor":str(det_factor) if det_factor is not None else None,
                "candidate_minor_is_nonzero_monomial":monomial,
            })

    if invalid:
        cls=INVALID_CLASS
    elif generic_fail:
        cls=FAIL_CLASS
    elif not all_nonzero_unproved:
        cls=PASS_CLASS
    else:
        cls=PARTIAL_CLASS

    return {
        "gate":GATE,
        "preregistration_commit":PREREG,
        "classification":cls,
        "implementation_valid":not bool(invalid),
        "case_count":len(rows),
        "invalid_cases":invalid,
        "generic_rank5_fail_cases":generic_fail,
        "all_nonzero_monomial_certificate_unproved_cases":all_nonzero_unproved,
        "generic_rank5_case_count":sum(r["generic_rank5_certified_by_nonzero_minor_polynomial"] for r in rows),
        "monomial_minor_case_count":sum(r["candidate_minor_is_nonzero_monomial"] for r in rows),
        "cases":rows,
        "claim_ceiling":"TWO-BLOCK SYMBOLIC MATRIX-PENCIL AUDIT ONLY; LOWER-DEGREE WEYL3 TERMS/FULL CHARACTERISTICS/HYPERBOLICITY/GHOST/TREATMENT NOT ESTABLISHED; C6 SYMBOLIC UNFIXED; THEORY_ESTABLISHED_0",
    }


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--out',required=True); a=ap.parse_args()
    out=run(); Path(a.out).parent.mkdir(parents=True,exist_ok=True)
    Path(a.out).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k!='cases'},sort_keys=True))
    if not out['implementation_valid']:
        raise SystemExit(2)

if __name__=='__main__': main()
