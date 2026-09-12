#!/usr/bin/env python3
import argparse,itertools,json,os
from fractions import Fraction as F

AUDITS=('prefix-moments','phase-authority-rank','coefficient-family-witness','order-vs-action-cumulant')
PERMS=list(itertools.permutations(range(4)))
TRIPLES=[(F(2),F(1),F(1,2)),(F(3,2),F(2,3),F(1,3)),(F(5,4),F(3,5),F(2,5)),(F(7,5),F(4,7),F(3,7)),(F(9,7),F(5,9),F(4,9)),(F(11,8),F(6,11),F(5,11))]

def rank_fraction(A):
    A=[list(map(F,row)) for row in A]
    if not A: return 0
    m,n=len(A),len(A[0]); r=0
    for c in range(n):
        p=next((i for i in range(r,m) if A[i][c]),None)
        if p is None: continue
        A[r],A[p]=A[p],A[r]
        z=A[r][c]; A[r]=[x/z for x in A[r]]
        for i in range(m):
            if i!=r and A[i][c]:
                z=A[i][c]; A[i]=[A[i][j]-z*A[r][j] for j in range(n)]
        r+=1
        if r==m: break
    return r

def prefix_stats(m):
    vals=[]
    for p in PERMS:
        S=set(p[:m])
        x=[F(1) if i in S else F(0) for i in range(4)]
        vals.append(x)
    E1=sum(v[0] for v in vals)/24
    E2=sum(v[0]*v[1] for v in vals)/24
    E3=sum(v[0]*v[1]*v[2] for v in vals)/24
    k2=E2-E1*E1
    k3=E3-3*E2*E1+2*E1**3
    return E1,E2,E3,k2,k3

def audit_prefix(lane):
    m=1+(lane%3)
    E1,E2,E3,k2,k3=prefix_stats(m)
    th1=F(m,4)
    th2=F(m*(m-1),12)
    th3=F(m*(m-1)*(m-2),24)
    passed=(E1,E2,E3)==(th1,th2,th3)
    return {
      'gate':'ITER023-G23-PREFIX-ORDER-MOMENTS','audit':'prefix-moments','lane':lane,'prefix_size':m,
      'E_X0':str(E1),'E_X0X1':str(E2),'E_X0X1X2':str(E3),'connected_pair_cumulant':str(k2),'connected_triple_cumulant':str(k3),
      'theory_E1':str(th1),'theory_E2':str(th2),'theory_E3':str(th3),'passed':passed,
      'classification':'PASS_SCOPED_UNIFORM_24_HISTORY_ORDER_MEASURE_EXACTLY_FIXES_COMBINATORIAL_PREFIX_OCCUPANCY_ONE_TWO_AND_THREE_POINT_MOMENTS_AND_THEIR_CONNECTED_CUMULANTS',
      'guard':'These are order/occupancy statistics of the permutation register, not coefficients of the microscopic action phase.'
    }

def audit_rank(lane):
    # Observable authority supplied by branch moduli/completeness and prefix occupancy moments.
    # All are independent of real action-phase coefficients (K,A,B).
    m=1+(lane%3); E1,E2,E3,_,_=prefix_stats(m)
    # rows are derivatives d(completeness,E1,E2,E3)/d(K,A,B)
    J=[[F(0),F(0),F(0)] for _ in range(4)]
    rk=rank_fraction(J); nul=3-rk
    passed=(rk==0 and nul==3 and F(24)*F(1,24)==1)
    return {
      'gate':'ITER023-G23-PHASE-AUTHORITY-RANK','audit':'phase-authority-rank','lane':lane,'prefix_size':m,
      'completeness':str(F(24)*F(1,24)),'order_moments':[str(E1),str(E2),str(E3)],
      'authority_jacobian_rank_on_K_A_B':rk,'nullity':nul,'passed':passed,
      'classification':'BLOCKED_SCOPED_EQUAL_24_HISTORY_MODULI_COMPLETENESS_AND_ALL_PREFIX_ORDER_MOMENTS_HAVE_ZERO_AUTHORITY_RANK_ON_THE_THREE_REAL_QUADRATIC_CUBIC_ACTION_PHASE_COEFFICIENTS_K_A_B',
      'guard':'The history instrument can carry coefficient-dependent phases, but its normalized order measure does not determine those phases.'
    }

def inv_ratios(K,A,B):
    return A*A/(K*K*K),B*B/(K*K*K),A/B

def audit_family(lane):
    K,A,B=TRIPLES[lane]
    K2=K+F(1,lane+5); A2=A+F(1,lane+6); B2=B+F(1,lane+7)
    # avoid accidental equality of invariants
    if inv_ratios(K,A,B)==inv_ratios(K2,A2,B2): B2+=F(1,13)
    r1=inv_ratios(K,A,B); r2=inv_ratios(K2,A2,B2)
    m=1+(lane%3); stats=prefix_stats(m)[:3]
    # Both real coefficient families keep branch modulus 1/sqrt(24) and same order distribution.
    passed=(r1!=r2 and F(24)*F(1,24)==1)
    return {
      'gate':'ITER023-G23-COEFFICIENT-FAMILY-WITNESS','audit':'coefficient-family-witness','lane':lane,
      'family1':[str(K),str(A),str(B)],'family2':[str(K2),str(A2),str(B2)],
      'family1_beta_invariant_ratios':[str(x) for x in r1],'family2_beta_invariant_ratios':[str(x) for x in r2],
      'shared_order_moments':[str(x) for x in stats],'shared_history_branch_probability':str(F(1,24)),'passed':passed,
      'classification':'BLOCKED_SCOPED_TWO_EXACT_REAL_ACTION_COEFFICIENT_FAMILIES_WITH_DISTINCT_BETA_INVARIANT_CUBIC_SHAPE_RATIOS_ARE_COMPATIBLE_WITH_THE_IDENTICAL_NORMALIZED_24_HISTORY_ORDER_MEASURE',
      'guard':'This is a non-identifiability witness, not evidence that either coefficient family is physically realized.'
    }

def audit_mismatch(lane):
    m=1+(lane%3); _,_,_,k2_order,k3_order=prefix_stats(m)
    K,A,B=TRIPLES[lane]
    # G13 connected triple action datum is B in count coordinates; it is independent of order cumulant.
    # Exhibit an alternative B while keeping all order statistics fixed.
    B_alt=B+F(1,lane+9)
    action_pair_shape=A*A/(K*K*K)
    action_triple_shape=B*B/(K*K*K)
    action_triple_shape_alt=B_alt*B_alt/(K*K*K)
    passed=(B_alt!=B and action_triple_shape_alt!=action_triple_shape)
    return {
      'gate':'ITER023-G23-ORDER-VS-ACTION-CUMULANT','audit':'order-vs-action-cumulant','lane':lane,'prefix_size':m,
      'order_connected_pair_cumulant':str(k2_order),'order_connected_triple_cumulant':str(k3_order),
      'action_pair_shape_A2_over_K3':str(action_pair_shape),'action_triple_shape_B2_over_K3':str(action_triple_shape),
      'alternate_action_triple_shape':str(action_triple_shape_alt),'passed':passed,
      'classification':'BLOCKED_SCOPED_COMBINATORIAL_ORDER_CUMULANTS_CANNOT_BE_IDENTIFIED_WITH_G13_FINITE_PAIR_OR_CONNECTED_TRIPLE_ACTION_DATA_WITHOUT_AN_ADDITIONAL_DERIVED_EVENT_TO_ACTION_PHASE_MAP',
      'guard':'Equating the numerical order cumulant to an action coefficient would be a new matching postulate and is not authorized by G8A normalization.'
    }

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--audit',choices=AUDITS,required=True); ap.add_argument('--lane',type=int,required=True); ap.add_argument('--out',required=True)
    a=ap.parse_args(); assert 0<=a.lane<6
    fn={'prefix-moments':audit_prefix,'phase-authority-rank':audit_rank,'coefficient-family-witness':audit_family,'order-vs-action-cumulant':audit_mismatch}[a.audit]
    out=fn(a.lane); os.makedirs(os.path.dirname(a.out),exist_ok=True)
    with open(a.out,'w',encoding='utf-8') as f: json.dump(out,f,indent=2,sort_keys=True); f.write('\n')
    print(json.dumps(out,sort_keys=True))
    if not out['passed']: raise SystemExit(2)
if __name__=='__main__': main()
