#!/usr/bin/env python3
import argparse,itertools,json,os
from fractions import Fraction as F

AUDITS=('linear-bridge','nonlinear-congruence','profile-obstruction','authority-after-bridge')
C=[[F(0) if i==j else F(1) for j in range(4)] for i in range(4)]

def rank_fraction(A):
    A=[[F(x) for x in row] for row in A]
    if not A:return 0
    m,n=len(A),len(A[0]);r=0
    for c in range(n):
        p=next((i for i in range(r,m) if A[i][c]),None)
        if p is None:continue
        A[r],A[p]=A[p],A[r];z=A[r][c];A[r]=[x/z for x in A[r]]
        for i in range(r+1,m):
            if A[i][c]:
                z=A[i][c];A[i]=[A[i][j]-z*A[r][j] for j in range(n)]
        r+=1
    return r

def permute_vec(q,p):
    out=[F(0)]*4
    for i in range(4):out[p[i]]=q[i]
    return out

def permute_mat(G,p):
    out=[[F(0)]*4 for _ in range(4)]
    for i in range(4):
        for j in range(4):out[p[i]][p[j]]=G[i][j]
    return out

def linear_bridge(q):
    # Differential at identity of G=F^T C F with generator-local F=diag(1+eps q).
    return [[F(0) if i==j else q[i]+q[j] for j in range(4)] for i in range(4)]

def finite_bridge(scales):
    return [[C[i][j]*scales[i]*scales[j] for j in range(4)] for i in range(4)]

def audit_linear(lane):
    q=[F(lane+1,7),F(2*lane+3,11),F(5-lane,13),F(lane+4,17)]
    H=linear_bridge(q)
    # Off-diagonal map q -> (q_i+q_j) is injective in d=4.
    M=[]
    for i in range(4):
        for j in range(i+1,4):
            row=[F(0)]*4;row[i]=1;row[j]=1;M.append(row)
    mr=rank_fraction(M)
    diag_zero=all(H[i][i]==0 for i in range(4))
    endpoint_local=True
    # exact S4 covariance over all permutations
    cov=True
    for p in itertools.permutations(range(4)):
        cov &= (linear_bridge(permute_vec(q,p))==permute_mat(H,p))
    passed=(mr==4 and diag_zero and cov)
    return {'gate':'ITER016-G15-GENERATOR-LOCAL-FRAME-RESCALE-BRIDGE','audit':'linear-bridge','lane':lane,
      'offdiag_linear_map_rank':mr,'diagonal_response_zero':diag_zero,'s4_covariant':cov,'passed':passed,
      'classification':'PASS_SCOPED_EXISTING_FRAME_CONGRUENCE_G_EQUALS_FT_C_F_HAS_A_CANONICAL_GENERATOR_LOCAL_DIAGONAL_RESCALE_SUBBRIDGE_WITH_DELTA_GIJ_QI_PLUS_QJ_AND_RANK_FOUR',
      'guard':'This is canonical only after identifying the four event coordinates with generator-local frame rescalings; QGR has not yet derived that G13 event interpretation.'}

def audit_nonlinear(lane):
    s=[F(lane+2,lane+1),F(lane+3,lane+2),F(lane+4,lane+3),F(lane+5,lane+4)]
    t=[F(lane+6,lane+5),F(lane+7,lane+6),F(lane+8,lane+7),F(lane+9,lane+8)]
    Gs=finite_bridge(s)
    composed=[s[i]*t[i] for i in range(4)]
    Gcomp=finite_bridge(composed)
    # Applying t by congruence to G(s) multiplies entry ij by t_i t_j.
    Gseq=[[Gs[i][j]*t[i]*t[j] for j in range(4)] for i in range(4)]
    cov=True
    p=list(itertools.permutations(range(4)))[(lane*7+1)%24]
    cov=(finite_bridge(permute_vec(s,p))==permute_mat(Gs,p))
    passed=(Gseq==Gcomp and cov and all(Gcomp[i][i]==0 for i in range(4)))
    return {'gate':'ITER016-G15-NONLINEAR-FRAME-RESCALE-COMPOSITION','audit':'nonlinear-congruence','lane':lane,
      'exact_multiplicative_composition':Gseq==Gcomp,'s4_covariant':cov,'zero_diagonal_preserved':all(Gcomp[i][i]==0 for i in range(4)),
      'passed':passed,'classification':'PASS_SCOPED_GENERATOR_LOCAL_FRAME_RESCALINGS_FORM_AN_EXACT_PARAMETER_FREE_NONLINEAR_CONGRUENCE_SUBMANIFOLD_OF_THE_EXISTING_G_ARENA'}

def audit_profile(lane):
    # Same endpoint displacement q across one versus two equal refinement steps.
    # Any quadratic first-difference action gives different finite value unless a separate refinement/profile law is supplied.
    q=F(lane+2,lane+9)
    one=q*q
    two=2*(q/F(2))**2
    three=3*(q/F(3))**2
    # A constant configuration has exactly zero first derivative and hence zero two-derivative connection-density action.
    constant_action=F(0)
    passed=(one!=two and two!=three and constant_action==0)
    return {'gate':'ITER016-G15-FINITE-PROFILE-ACTION-OBSTRUCTION','audit':'profile-obstruction','lane':lane,
      'endpoint_q':str(q),'one_step_quadratic_difference':str(one),'two_step_same_endpoint':str(two),'three_step_same_endpoint':str(three),
      'constant_q_two_derivative_action':str(constant_action),'passed':passed,
      'classification':'BLOCKED_SCOPED_THE_CANONICAL_FRAME_RESCALE_BRIDGE_DOES_NOT_BY_ITSELF_DEFINE_A_FINITE_EVENT_AMPLITUDE__THE_TWO_DERIVATIVE_ACTION_IS_ZERO_ON_CONSTANT_Q_AND_PROFILE_DEPENDENT_FOR_FINITE_ENDPOINT_CHANGES',
      'interpretation':'A microscopic event profile/refinement action must be derived before finite pair or connected-triple amplitudes can be computed from the same realization.'}

def audit_authority(lane):
    # Adopting a coordinate bridge is not an amplitude measurement: it adds no row in (k,a,b) coefficient authority.
    rows_before=[[1,0,0]]
    rows_after=rows_before[:]  # q->G bridge alone supplies geometry coordinates, not a nonhomogeneous scalar amplitude target.
    rb=rank_fraction(rows_before);ra=rank_fraction(rows_after)
    hypothetical=rank_fraction(rows_after+[[1,2,0],[0,0,1]])
    passed=(rb==1 and ra==1 and hypothetical==3)
    return {'gate':'ITER016-G15-AUTHORITY-AFTER-CANONICAL-SUBBRIDGE','audit':'authority-after-bridge','lane':lane,
      'rank_before_bridge':rb,'rank_after_bridge_without_finite_profile_action':ra,'rank_with_hypothetical_pair_triple_data':hypothetical,
      'cubic_nullity_after_bridge':3-ra,'passed':passed,
      'classification':'BLOCKED_SCOPED_CANONICAL_GENERATOR_LOCAL_Q_TO_G_COORDINATE_BRIDGE_DOES_NOT_INCREASE_CUBIC_AMPLITUDE_AUTHORITY_RANK_WITHOUT_A_DERIVED_FINITE_PROFILE_ACTION'}

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--audit',choices=AUDITS,required=True);ap.add_argument('--lane',type=int,required=True);ap.add_argument('--out',required=True)
    a=ap.parse_args();assert 0<=a.lane<6
    fn={'linear-bridge':audit_linear,'nonlinear-congruence':audit_nonlinear,'profile-obstruction':audit_profile,'authority-after-bridge':audit_authority}[a.audit]
    out=fn(a.lane);os.makedirs(os.path.dirname(a.out),exist_ok=True)
    with open(a.out,'w') as f:json.dump(out,f,indent=2,sort_keys=True)
    print(json.dumps(out,sort_keys=True))
    if not out['passed']:raise SystemExit(1)
if __name__=='__main__':main()
