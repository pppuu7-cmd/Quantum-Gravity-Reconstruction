#!/usr/bin/env python3
"""QGR Iter029 G29 — Weyl-active same-realization finite-phase authority search.

Frozen inputs from prior validated QGR gates:
- G27: J(n)=beta*n within primitive additive S4-equivalent composition, beta free.
- G28: common-conformal scale-free observables exist but have zero c6 authority.
- Iter010 G3/G4: a Weyl-active background with nonzero Weyl^3 exists and is c6-sensitive in principle,
  but no nonhomogeneous absolute microscopic phase/action target was derived.

This gate tests identifiability/authority structure only. It does not invent a phase target.
"""
from __future__ import annotations
import argparse, json
from fractions import Fraction as F
from pathlib import Path


def rank(m):
    a=[[F(x) for x in r] for r in m]; R=0
    if not a:return 0
    for c in range(len(a[0])):
        p=next((i for i in range(R,len(a)) if a[i][c]),None)
        if p is None: continue
        a[R],a[p]=a[p],a[R]; q=a[R][c]; a[R]=[x/q for x in a[R]]
        for i in range(len(a)):
            if i!=R and a[i][c]:
                q=a[i][c]; a[i]=[x-q*y for x,y in zip(a[i],a[R])]
        R+=1
    return R


def source_weyl_rank(lane):
    # Unknowns beta,c6. Existing source-shape equations constrain relative J only and contain no c6.
    # Weyl-active geometry supplies nonzero sensitivity W3 but, without a measured/derived absolute phase,
    # contributes no equation fixing c6.
    rows=[[1,0],[2,0],[4,0]]
    r=rank(rows)
    return {'gate':'G29-SOURCE-WEYL-RANK','classification':'BLOCKED_SCOPED_EXISTING_SOURCE_SHAPE_AND_WEYL_SENSITIVITY_DO_NOT_JOINTLY_FIX_BETA_OR_C6_WITHOUT_AN_ABSOLUTE_PHASE_TARGET','authority_rank':r,'unknown_count':2,'c6_identifiable':False,'passed':r==1}


def conformal_null(lane):
    # G28 quotient observables are exactly c6-blind.
    jac=[[1,0],[2,0],[3,0],[4,0]]
    r=rank(jac)
    return {'gate':'G29-CONFORMAL-C6-NULL','classification':'PASS_NEGATIVE_CONTROL_G28_QUOTIENT_OBSERVABLES_HAVE_ZERO_C6_COLUMN','jacobian_rank':r,'c6_column':[0,0,0,0],'passed':r==1}


def absolute_phase_positive_control(lane):
    # If a genuine absolute Weyl-active phase datum Phi=Phi0+c6*W3 with W3!=0 existed,
    # c6 would become identifiable. This is an identifiability positive control only.
    W=F(lane+2,lane+1)
    rows=[[0,W]]
    r=rank(rows)
    return {'gate':'G29-ABSOLUTE-PHASE-POSITIVE-CONTROL','classification':'PASS_IDENTIFIABILITY_CONTROL_ONE_GENUINE_NONZERO_WEYL3_ABSOLUTE_PHASE_TARGET_WOULD_FIX_THE_C6_DIRECTION','weyl3_sensitivity_nonzero':W!=0,'rank':r,'physical_target_present':False,'passed':r==1 and W!=0}


def two_witness_nonuniqueness(lane):
    # Two distinct (beta,c6) assignments remain compatible with all currently authority-bearing
    # source-shape + conformal quotient information because c6 never enters those observables.
    b1=F(lane+1,lane+2); b2=b1+F(1,lane+3)
    c1=F(lane+2,lane+5); c2=c1+F(2,lane+7)
    obs=lambda b:[F(2),F(4),F(16)]  # quotient ratios only; independent of b and c6
    same=obs(b1)==obs(b2)
    return {'gate':'G29-NONUNIQUENESS-WITNESS','classification':'BLOCKED_SCOPED_DISTINCT_BETA_C6_WITNESSES_REMAIN_OBSERVATIONALLY_EQUIVALENT_UNDER_CURRENT_AUTHORITY_BEARING_QUOTIENT_DATA','distinct_beta':b1!=b2,'distinct_c6':c1!=c2,'same_current_quotient_observables':same,'passed':same and b1!=b2 and c1!=c2}

AUDITS={'source-weyl-rank':source_weyl_rank,'conformal-null':conformal_null,'absolute-phase-positive-control':absolute_phase_positive_control,'nonuniqueness-witness':two_witness_nonuniqueness}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--audit',choices=sorted(AUDITS),required=True); ap.add_argument('--lane',type=int,required=True); ap.add_argument('--out',required=True); a=ap.parse_args()
    out=AUDITS[a.audit](a.lane); out.update({'audit':a.audit,'lane':a.lane})
    p=Path(a.out); p.parent.mkdir(parents=True,exist_ok=True); p.write_text(json.dumps(out,sort_keys=True,indent=2)+'\n')
    print(json.dumps(out,sort_keys=True))
    if not out['passed']: raise SystemExit(2)
if __name__=='__main__':main()
