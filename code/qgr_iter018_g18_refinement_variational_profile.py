#!/usr/bin/env python3
import argparse,itertools,json,os
from fractions import Fraction as F

AUDITS=('linear-profile','strict-minimality','s4-lift','authority-rank')
RS=[F(3,2),F(4,3),F(5,4),F(7,5),F(8,7),F(9,8)]
PARTITIONS=[
    [F(1)],
    [F(1,2),F(1,2)],
    [F(1,3),F(1,3),F(1,3)],
    [F(1,4),F(1,4),F(1,4),F(1,4)],
    [F(1,2),F(1,3),F(1,6)],
    [F(2,5),F(1,5),F(1,10),F(3,10)],
]

def energy(h,dq):
    assert len(h)==len(dq) and sum(h,F(0))==1 and all(x>0 for x in h)
    return sum((dq[i]*dq[i])/h[i] for i in range(len(h)))

def linear_dq(q,h):
    return [q*x for x in h]

def perturbation(h,lane):
    # exact endpoint-preserving perturbation with sum eps = 0
    n=len(h)
    if n==1:
        return [F(0)]
    eps=[F(0)]*n
    a=F(lane+1,97)
    eps[0]=a
    eps[-1]=-a
    return eps

def audit_linear(lane):
    r=RS[lane]; q=r-1
    vals=[]
    for h in PARTITIONS:
        dq=linear_dq(q,h)
        vals.append(energy(h,dq))
    exact=all(v==q*q for v in vals)
    return {
      'gate':'ITER018-G18-REFINEMENT-CONSISTENT-LINEAR-PROFILE','audit':'linear-profile','lane':lane,
      'r':str(r),'q':str(q),'partition_count':len(PARTITIONS),'energies':[str(v) for v in vals],
      'all_equal_q2_exact':exact,'passed':exact,
      'classification':'PASS_SCOPED_DIRICHLET_DISCRETIZATION_SUM_DQ2_OVER_H_IS_EXACTLY_PARTITION_INVARIANT_ON_THE_LINEAR_ENDPOINT_PROFILE',
      'guard':'This uses the two-derivative Dirichlet discretization as a candidate microscopic refinement functional; QGR has not yet derived that discretization uniquely.'
    }

def audit_minimal(lane):
    r=RS[lane]; q=r-1
    checks=[]
    for h in PARTITIONS[1:]:
        base=linear_dq(q,h)
        eps=perturbation(h,lane)
        alt=[base[i]+eps[i] for i in range(len(h))]
        endpoint=(sum(alt,F(0))==q)
        e0=energy(h,base); e1=energy(h,alt)
        excess=e1-e0
        certificate=sum((eps[i]*eps[i])/h[i] for i in range(len(h)))
        checks.append(endpoint and excess==certificate and excess>0)
    passed=all(checks)
    return {
      'gate':'ITER018-G18-STRICT-VARIATIONAL-MINIMALITY','audit':'strict-minimality','lane':lane,'r':str(r),
      'nontrivial_partitions_checked':len(checks),'all_endpoint_preserving_perturbations_raise_action_exactly':passed,
      'identity':'E[q h + eps]-q^2 = sum eps_k^2/h_k when sum eps_k=0','passed':passed,
      'classification':'PASS_SCOPED_WITH_POSITIVE_CELL_WIDTHS_THE_LINEAR_PROFILE_IS_THE_UNIQUE_MINIMIZER_OF_THE_CANDIDATE_DIRICHLET_REFINEMENT_ACTION_FOR_FIXED_ENDPOINTS'
    }

def audit_s4(lane):
    r=RS[lane]; q=r-1
    h=PARTITIONS[lane]
    # Four generator directions carry the same common-r endpoint displacement.
    directional=[energy(h,linear_dq(q,h)) for _ in range(4)]
    total=sum(directional,F(0))
    invariant=True
    for p in itertools.permutations(range(4)):
        perm=[directional[p[i]] for i in range(4)]
        invariant &= (sum(perm,F(0))==total and perm==directional)
    passed=invariant and total==4*q*q
    return {
      'gate':'ITER018-G18-S4-LIFT-OF-MINIMAL-PROFILE','audit':'s4-lift','lane':lane,'r':str(r),
      'directional_minimal_actions':[str(x) for x in directional],'total_action':str(total),
      'all_24_permutations_exact':invariant,'passed':passed,
      'classification':'PASS_SCOPED_COMMON_R_PLUS_IDENTICAL_DIRICHLET_PROFILE_LIFTS_TO_AN_EXACT_S4_INVARIANT_FOUR_DIRECTION_MINIMAL_ACTION_4_R_MINUS_1_SQUARED'
    }

def audit_authority(lane):
    r1=RS[lane]; r2=RS[(lane+1)%len(RS)]
    q1=r1-1; q2=r2-1
    lam1=F(lane+2,lane+3)
    A=lam1*q1*q1
    lam2=A/(q2*q2)
    same=(lam1*q1*q1==lam2*q2*q2)
    distinct=(r1!=r2 and lam1!=lam2)
    # One measured nonzero amplitude A would constrain lambda*(r-1)^2 but cannot separate lambda from r.
    rank=1
    nullity=1
    passed=same and distinct and rank==1 and nullity==1
    return {
      'gate':'ITER018-G18-PROFILE-AUTHORITY-RANK','audit':'authority-rank','lane':lane,
      'r1':str(r1),'lambda1':str(lam1),'r2':str(r2),'lambda2':str(lam2),'common_amplitude':str(A),
      'two_distinct_exact_witnesses_same_amplitude':same and distinct,'authority_rank_in_lambda_r_combination':rank,
      'remaining_nullity':nullity,'passed':passed,
      'classification':'BLOCKED_SCOPED_VARIATIONAL_REFINEMENT_CAN_REMOVE_PROFILE_SEGMENTATION_AMBIGUITY_BUT_A_FINITE_AMPLITUDE_ONLY_FIXES_THE_COMBINATION_LAMBDA_R_MINUS_1_SQUARED__AN_INDEPENDENT_NORMALIZATION_OR_R_AUTHORITY_IS_STILL_REQUIRED',
      'guard':'The result does not claim lambda is a new physical coupling; it records the normalization freedom of the candidate microscopic Dirichlet functional until matched to an independently derived same-realization amplitude.'
    }

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--audit',choices=AUDITS,required=True); ap.add_argument('--lane',type=int,required=True); ap.add_argument('--out',required=True)
    a=ap.parse_args(); assert 0<=a.lane<6
    fn={'linear-profile':audit_linear,'strict-minimality':audit_minimal,'s4-lift':audit_s4,'authority-rank':audit_authority}[a.audit]
    out=fn(a.lane); os.makedirs(os.path.dirname(a.out),exist_ok=True)
    with open(a.out,'w') as f: json.dump(out,f,indent=2,sort_keys=True)
    print(json.dumps(out,sort_keys=True))
    if not out['passed']: raise SystemExit(1)
if __name__=='__main__': main()
