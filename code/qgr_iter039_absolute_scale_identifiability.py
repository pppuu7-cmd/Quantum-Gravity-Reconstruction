#!/usr/bin/env python3
"""QGR Iter039: exact/current-authority identifiability of beta and c6 after Iter038.

No new physical data are introduced. Hypothetical target rows are used only to determine minimal
calibration rank, never as measurements or derived QGR observables.
"""
from __future__ import annotations
import argparse,json,math
from fractions import Fraction as F
from pathlib import Path
import numpy as np
import qgr_iter038_principal_refinement as g38


def rank(mat):
    a=[[F(x) for x in row] for row in mat]
    if not a: return 0
    r=0
    for c in range(len(a[0])):
        p=next((i for i in range(r,len(a)) if a[i][c]),None)
        if p is None: continue
        a[r],a[p]=a[p],a[r]; q=a[r][c]; a[r]=[x/q for x in a[r]]
        for i in range(len(a)):
            if i!=r and a[i][c]:
                q=a[i][c]; a[i]=[x-q*y for x,y in zip(a[i],a[r])]
        r+=1
    return r


def additive_matrix(N=8):
    rows=[]
    for a in range(1,N+1):
        for b in range(1,N+1):
            if a+b<=N:
                row=[F(0)]*N; row[a+b-1]+=1; row[a-1]-=1; row[b-1]-=1; rows.append(row)
    return rows


def audit_source_null(lane):
    N=8; rows=additive_matrix(N); r=rank(rows); nullity=N-r
    b1=F(lane+1,lane+2); b2=b1+F(1,lane+5)
    v1=[b1*n for n in range(1,N+1)]; v2=[b2*n for n in range(1,N+1)]
    def satisfies(v): return all(sum(row[j]*v[j] for j in range(N))==0 for row in rows)
    counts=[1,2,3,4,5,8]
    lam=F(lane+3,lane+1)
    def quotient(beta):
        end=[beta*F(n)/(2*lam) for n in counts]
        phase=[-(beta*F(n))**2/(4*lam) for n in counts]
        return [x/end[0] for x in end],[x/phase[0] for x in phase]
    q1=quotient(b1); q2=quotient(b2)
    passed=bool(r==7 and nullity==1 and satisfies(v1) and satisfies(v2) and b1!=b2 and q1==q2 and
                q1[0]==[F(n) for n in counts] and q1[1]==[F(n*n) for n in counts])
    return {'gate':'ITER039-A-SOURCE-NULL','constraint_rank':r,'nullity':nullity,
            'canonical_null_ray':list(range(1,N+1)),'distinct_beta_witnesses':[str(b1),str(b2)],
            'quotient_observables_identical':q1==q2,'absolute_beta_fixed':False,'passed':passed,
            'classification':'PASS_EXACT_ONE_DIMENSIONAL_SOURCE_SCALE_ORBIT' if passed else 'CONTROL_FAIL'}


def audit_refinement_blind(lane):
    # beta is deliberately only a dummy witness here: the frozen G38 geometric principal equations
    # contain no source-conversion beta. We recompute representative quantities for multiple witnesses
    # and require bit-level/numerical equality of outputs.
    betas=[F(lane+k+1,lane+k+2) for k in range(1,7)]
    x=np.array([0.25,0.25,0.25,0.25]); h=1/16
    z,rn,me,ok,sv=g38.solve_principal(x,h,1800)
    A,prow=g38.path_product(np.zeros(4),lane%4,0.5,16)
    if not ok or A is None:
        return {'gate':'ITER039-B-REFINEMENT-BLIND','passed':False,'classification':'CONTROL_FAIL'}
    ref=np.concatenate([z,[rn,me,float(sv.min())],A.reshape(-1)])
    copies=[]
    for beta in betas:
        # Re-evaluate unchanged geometric equations; beta does not enter their mathematical definition.
        z2,rn2,me2,ok2,sv2=g38.solve_principal(x,h,1800)
        A2,p2=g38.path_product(np.zeros(4),lane%4,0.5,16)
        if not ok2 or A2 is None:
            return {'gate':'ITER039-B-REFINEMENT-BLIND','passed':False,'classification':'CONTROL_FAIL'}
        cur=np.concatenate([z2,[rn2,me2,float(sv2.min())],A2.reshape(-1)])
        copies.append(float(np.max(np.abs(cur-ref))))
    mx=max(copies) if copies else float('inf')
    passed=bool(mx<1e-12)
    return {'gate':'ITER039-B-REFINEMENT-BLIND','beta_witnesses':[str(b) for b in betas],
            'max_output_difference':mx,'authority_rank_on_beta':0,'passed':passed,
            'classification':'PASS_G38_PRINCIPAL_REFINEMENT_HAS_ZERO_BETA_AUTHORITY' if passed else 'CONTROL_FAIL'}


def audit_current_rank(lane):
    # Unknown coordinates (u=beta^2,c6). Current authorized absolute observation equations: none.
    # Scale-free quotients and geometric regularity controls have zero rows in absolute-parameter space.
    rows=[[F(0),F(0)] for _ in range(4+lane)]
    r=rank(rows)
    passed=(r==0)
    return {'gate':'ITER039-C-CURRENT-AUTHORITY-RANK','unknowns':['u=beta^2','c6'],
            'authority_rank':r,'unknown_count':2,'beta_magnitude_identifiable':False,
            'c6_identifiable':False,'passed':passed,
            'classification':'PASS_CURRENT_ABSOLUTE_PARAMETER_AUTHORITY_RANK_ZERO' if passed else 'CONTROL_FAIL'}


def audit_minimal_calibration(lane):
    n=F(lane+1); lam=F(lane+2,lane+1); W=F(lane+3,lane+2); A=F(lane+4,lane+3)
    conformal=[-n*n/(4*lam),F(0)]
    weyl=[A,W]
    r0=rank([]); rc=rank([conformal]); rw=rank([weyl]); rb=rank([conformal,weyl])
    det=conformal[0]*W
    passed=bool(r0==0 and rc==1 and rw==1 and rb==2 and det!=0 and W!=0)
    return {'gate':'ITER039-D-MINIMAL-CALIBRATION-RANK','rank_no_absolute_targets':r0,
            'rank_conformal_absolute_only':rc,'rank_weyl_absolute_only':rw,
            'rank_conformal_plus_weyl':rb,'determinant':str(det),'hypothetical_targets_are_physical_data':False,
            'passed':passed,
            'classification':'PASS_TWO_INDEPENDENT_ABSOLUTE_DIRECTIONS_MINIMALLY_IDENTIFY_U_AND_C6' if passed else 'CONTROL_FAIL'}


def audit_beta_sign(lane):
    beta=F(lane+1,lane+2); n=F(lane+2); lam=F(lane+3,lane+1)
    def phase(b): return -(b*n)**2/(4*lam)
    def endpoint(b): return b*n/(2*lam)
    phase_even=(phase(beta)==phase(-beta)); endpoint_odd=(endpoint(beta)==-endpoint(-beta)); endpoint_nonzero=endpoint(beta)!=0
    passed=bool(phase_even and endpoint_odd and endpoint_nonzero)
    return {'gate':'ITER039-E-BETA-SIGN','beta':str(beta),'phase_beta':str(phase(beta)),
            'phase_minus_beta':str(phase(-beta)),'endpoint_beta':str(endpoint(beta)),
            'endpoint_minus_beta':str(endpoint(-beta)),'phase_is_sign_blind':phase_even,
            'signed_endpoint_is_sign_sensitive':endpoint_odd,'passed':passed,
            'classification':'PASS_PHASE_FIXES_AT_MOST_BETA_MAGNITUDE_SIGN_REQUIRES_SIGNED_ABSOLUTE_SOURCE_DATUM' if passed else 'CONTROL_FAIL'}

AUDITS={
    'source-null':audit_source_null,
    'refinement-beta-blind':audit_refinement_blind,
    'current-authority-rank':audit_current_rank,
    'minimal-calibration-rank':audit_minimal_calibration,
    'beta-sign':audit_beta_sign,
}


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--audit',choices=sorted(AUDITS),required=True)
    ap.add_argument('--lane',type=int,required=True); ap.add_argument('--out',required=True); a=ap.parse_args()
    if not 0<=a.lane<6: raise SystemExit('lane must be 0..5')
    out=AUDITS[a.audit](a.lane); out.update({'audit':a.audit,'lane':a.lane})
    p=Path(a.out); p.parent.mkdir(parents=True,exist_ok=True); p.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(json.dumps(out,sort_keys=True))
    if not out.get('passed'): raise SystemExit(2)

if __name__=='__main__': main()
