#!/usr/bin/env python3
import argparse,json,os
from fractions import Fraction as F

AUDITS=('current-authority-rank','minimal-phase-basis','beta-invariant-readout','insufficient-sample-witness')
BETAS=[F(1,3),F(1,2),F(2,3),F(3,4),F(4,5),F(5,6)]

# Local cubic count-coordinate jet retained from G13/G22:
# Phi(n)=K e2(n)+A p21(n)+B e3(n),
# where p21=sum_{i<j}(n_i^2 n_j+n_i n_j^2).
PATTERNS={
    'pair_unit':(1,1,0,0),
    'pair_asym':(2,1,0,0),
    'triple_unit':(1,1,1,0),
}

def rank_fraction(A):
    A=[list(map(F,row)) for row in A]
    if not A:return 0
    m,n=len(A),len(A[0]);r=0
    for c in range(n):
        p=next((i for i in range(r,m) if A[i][c]),None)
        if p is None:continue
        A[r],A[p]=A[p],A[r]
        z=A[r][c];A[r]=[x/z for x in A[r]]
        for i in range(m):
            if i!=r and A[i][c]:
                z=A[i][c];A[i]=[A[i][j]-z*A[r][j] for j in range(n)]
        r+=1
        if r==m:break
    return r

def features(n):
    e2=F(0);p21=F(0);e3=F(0)
    for i in range(4):
        for j in range(i+1,4):
            e2+=F(n[i]*n[j])
            p21+=F(n[i]*n[i]*n[j]+n[i]*n[j]*n[j])
    for i in range(4):
        for j in range(i+1,4):
            for k in range(j+1,4):e3+=F(n[i]*n[j]*n[k])
    return (e2,p21,e3)

def solve3(M,y):
    A=[list(map(F,row))+[F(v)] for row,v in zip(M,y)]
    n=3
    for c in range(n):
        p=next(i for i in range(c,n) if A[i][c])
        A[c],A[p]=A[p],A[c]
        z=A[c][c];A[c]=[x/z for x in A[c]]
        for i in range(n):
            if i!=c and A[i][c]:
                z=A[i][c];A[i]=[A[i][j]-z*A[c][j] for j in range(n+1)]
    return tuple(A[i][-1] for i in range(n))

def coeffs(lane):
    return (F(lane+2,lane+1),F(lane+1,lane+4),F(lane+3,lane+5))

def audit_current(lane):
    # Existing normalized history/order data and the unresolved beta coordinate orbit
    # supply no numerical phase sample. Hence their derivative wrt K,A,B is exactly zero.
    J=[[F(0),F(0),F(0)] for _ in range(6)]
    rk=rank_fraction(J)
    return {'gate':'ITER024-G24-CURRENT-PHASE-AUTHORITY-RANK','audit':'current-authority-rank','lane':lane,
      'rank_on_K_A_B':rk,'nullity':3-rk,'passed':rk==0,
      'classification':'BLOCKED_SCOPED_CURRENT_G19_G20_G21_G22_G23_INPUTS_SUPPLY_NO_NUMERICAL_FINITE_CURVED_ACTION_PHASE_SAMPLE_AND_HAVE_ZERO_AUTHORITY_RANK_ON_K_A_B',
      'guard':'This is an authority audit, not a claim that finite curved phases vanish.'}

def audit_basis(lane):
    names=('pair_unit','pair_asym','triple_unit');M=[features(PATTERNS[n]) for n in names]
    K,A,B=coeffs(lane);y=[sum(row[j]*x for j,x in enumerate((K,A,B))) for row in M]
    sol=solve3(M,y);rk=rank_fraction(M)
    return {'gate':'ITER024-G24-MINIMAL-FINITE-CURVED-PHASE-BASIS','audit':'minimal-phase-basis','lane':lane,
      'patterns':{n:list(PATTERNS[n]) for n in names},'feature_matrix':[[str(x) for x in r] for r in M],
      'rank':rk,'synthetic_control_coefficients':[str(K),str(A),str(B)],'synthetic_phase_samples':[str(v) for v in y],
      'recovered_coefficients':[str(v) for v in sol],'passed':rk==3 and sol==(K,A,B),
      'classification':'PASS_SCOPED_THREE_NONREDUNDANT_SAME_REALIZATION_FINITE_PHASE_SAMPLES_PAIR_UNIT_PAIR_ASYMMETRIC_AND_TRIPLE_UNIT_FORM_AN_EXACT_FULL_RANK_BASIS_FOR_K_A_B',
      'guard':'Synthetic coefficients are only an algebraic positive control. QGR still lacks the physical same-realization phase samples themselves.'}

def audit_beta(lane):
    beta=BETAS[lane];k,a,b=coeffs(lane)
    K=k*beta**2;A=a*beta**3;B=b*beta**3
    Ia=A*A/(K*K*K);Ib=B*B/(K*K*K);Rab=A/B
    target=(a*a/(k*k*k),b*b/(k*k*k),a/b)
    return {'gate':'ITER024-G24-BETA-INVARIANT-PHASE-READOUT','audit':'beta-invariant-readout','lane':lane,
      'beta':str(beta),'count_coefficients':[str(K),str(A),str(B)],
      'invariants':[str(Ia),str(Ib),str(Rab)],'beta_free_forms':[str(x) for x in target],
      'passed':(Ia,Ib,Rab)==target,
      'classification':'PASS_SCOPED_IF_THE_THREE_FINITE_PHASE_SAMPLES_ARE_OBTAINED_IN_COUNT_COORDINATES_THE_G22_EVENT_UNIT_BETA_DROPS_OUT_OF_THE_CUBIC_TO_QUADRATIC_INVARIANT_RATIOS',
      'guard':'Beta cancellation removes a calibration ambiguity; it does not manufacture the missing finite phase data.'}

def audit_insufficient(lane):
    M=[features(PATTERNS['pair_unit']),features(PATTERNS['triple_unit'])]
    rk=rank_fraction(M);K,A,B=coeffs(lane)
    # Exact null vector for rows [1,2,0] and [3,6,1] is (-2,1,0).
    v=(F(-2),F(1),F(0));ann=all(sum(r[j]*v[j] for j in range(3))==0 for r in M)
    alt=(K+v[0],A+v[1],B+v[2])
    y=lambda c:[sum(r[j]*c[j] for j in range(3)) for r in M]
    return {'gate':'ITER024-G24-INSUFFICIENT-PHASE-SAMPLE-WITNESS','audit':'insufficient-sample-witness','lane':lane,
      'two_sample_rank':rk,'nullity':3-rk,'exact_null_vector':[str(x) for x in v],'null_verified':ann,
      'family1':[str(K),str(A),str(B)],'family2':[str(x) for x in alt],
      'shared_two_phase_samples':[str(x) for x in y((K,A,B))],
      'passed':rk==2 and ann and y((K,A,B))==y(alt) and alt!=(K,A,B),
      'classification':'BLOCKED_SCOPED_A_UNIT_PAIR_PLUS_UNIT_TRIPLE_PHASE_ALONE_LEAVE_ONE_EXACT_K_A_DEGENERACY__A_NONUNIFORM_PAIR_OR_EQUIVALENT_THIRD_INDEPENDENT_FINITE_CURVED_SAMPLE_IS_REQUIRED',
      'guard':'Do not infer K and A separately from only the unit-pair and unit-triple amplitudes.'}

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--audit',choices=AUDITS,required=True);ap.add_argument('--lane',type=int,required=True);ap.add_argument('--out',required=True)
    a=ap.parse_args();assert 0<=a.lane<6
    fn={'current-authority-rank':audit_current,'minimal-phase-basis':audit_basis,'beta-invariant-readout':audit_beta,'insufficient-sample-witness':audit_insufficient}[a.audit]
    out=fn(a.lane);os.makedirs(os.path.dirname(a.out),exist_ok=True)
    with open(a.out,'w',encoding='utf-8') as f:json.dump(out,f,indent=2,sort_keys=True);f.write('\n')
    print(json.dumps(out,sort_keys=True))
    if not out['passed']:raise SystemExit(2)
if __name__=='__main__':main()
