#!/usr/bin/env python3
import argparse,json,os
from fractions import Fraction as F

AUDITS=('reparam-invariance','authority-rank','beta-invariant-ratios','preparation-vs-calibration')
BETA=[F(1,3),F(1,2),F(2,3),F(3,4),F(4,5),F(5,6)]
LAM=[F(2),F(3,2),F(4,3),F(5,4),F(6,5),F(7,6)]

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

def data(beta,k,a,b):
    # Count-coordinate jet q_phys = beta*n.  The count-space coefficients are
    # K=k beta^2, A=a beta^3, B=b beta^3.
    return k*beta**2, a*beta**3, b*beta**3

def audit_reparam(lane):
    beta=BETA[lane]; lam=LAM[lane]
    k=F(lane+3,lane+2); a=F(lane+2,lane+5); b=F(lane+4,lane+7)
    K,A,B=data(beta,k,a,b)
    beta2=lam*beta; k2=k/lam**2; a2=a/lam**3; b2=b/lam**3
    K2,A2,B2=data(beta2,k2,a2,b2)
    passed=(K,A,B)==(K2,A2,B2) and beta2!=beta
    return {
      'gate':'ITER022-G22-BETA-REPARAM-INVARIANCE','audit':'reparam-invariance','lane':lane,
      'beta':str(beta),'lambda':str(lam),'k':str(k),'a':str(a),'b':str(b),
      'count_coefficients':[str(K),str(A),str(B)],'rescaled_beta':str(beta2),
      'rescaled_coefficients':[str(k2),str(a2),str(b2)],'count_coefficients_after_rescaling':[str(K2),str(A2),str(B2)],
      'passed':passed,
      'classification':'PASS_SCOPED_CONDITIONAL_ON_A_SINGLE_EVENT_RESPONSE_SCALE_BETA__THE_SIMULTANEOUS_REPARAMETRIZATION_BETA_TO_LAMBDA_BETA_K_TO_K_OVER_LAMBDA2_A_B_TO_A_B_OVER_LAMBDA3_LEAVES_ALL_QUADRATIC_AND_CUBIC_COUNT_SPACE_COEFFICIENTS_EXACTLY_INVARIANT',
      'guard':'This identifies a coordinate-normalization orbit of the local jet; it does not prove that physically distinct prepared boundary amplitudes are gauge-equivalent.'
    }

def audit_rank(lane):
    beta=BETA[lane]; k=F(lane+3,lane+2); a=F(lane+2,lane+5); b=F(lane+4,lane+7)
    # Jacobian d(K,A,B)/d(beta,k,a,b).
    J=[
      [2*k*beta, beta**2, 0, 0],
      [3*a*beta**2, 0, beta**3, 0],
      [3*b*beta**2, 0, 0, beta**3],
    ]
    rk=rank_fraction(J); nul=4-rk
    v=[beta,-2*k,-3*a,-3*b]
    annihilated=all(sum(J[i][j]*v[j] for j in range(4))==0 for i in range(3))
    passed=(rk==3 and nul==1 and annihilated)
    return {
      'gate':'ITER022-G22-BETA-AUTHORITY-RANK','audit':'authority-rank','lane':lane,
      'jacobian_rank':rk,'parameter_count':4,'nullity':nul,
      'exact_null_vector':[str(x) for x in v],'null_vector_verified':annihilated,'passed':passed,
      'classification':'BLOCKED_SCOPED_CONDITIONAL_ON_G21_SINGLE_BETA_MAP__EVEN_QUADRATIC_PLUS_FINITE_PAIR_PLUS_CONNECTED_TRIPLE_COUNT_SPACE_AUTHORITY_HAS_A_ONE_DIMENSIONAL_NORMALIZATION_NULL_DIRECTION_WHEN_BETA_IS_INCLUDED',
      'guard':'The null direction is field/event-unit reparametrization. It must not be removed by setting beta=1 unless that is explicitly declared a coordinate convention rather than a physical derivation.'
    }

def audit_ratios(lane):
    beta=BETA[lane]; k=F(lane+3,lane+2); a=F(lane+2,lane+5); b=F(lane+4,lane+7)
    K,A,B=data(beta,k,a,b)
    # Avoid irrational square roots: squared dimensionless invariants and A/B.
    Ia=A*A/(K*K*K)
    Ib=B*B/(K*K*K)
    Rab=A/B
    Ia0=a*a/(k*k*k); Ib0=b*b/(k*k*k); Rab0=a/b
    beta2=LAM[lane]*beta
    k2=k/LAM[lane]**2; a2=a/LAM[lane]**3; b2=b/LAM[lane]**3
    K2,A2,B2=data(beta2,k2,a2,b2)
    Ia2=A2*A2/(K2*K2*K2); Ib2=B2*B2/(K2*K2*K2); Rab2=A2/B2
    passed=(Ia,Ib,Rab)==(Ia0,Ib0,Rab0)==(Ia2,Ib2,Rab2)
    return {
      'gate':'ITER022-G22-BETA-INVARIANT-CUBIC-RATIOS','audit':'beta-invariant-ratios','lane':lane,
      'A2_over_K3':str(Ia),'B2_over_K3':str(Ib),'A_over_B':str(Rab),
      'same_physical_ratio_forms':[str(Ia0),str(Ib0),str(Rab0)],'passed':passed,
      'classification':'PASS_SCOPED_CUBIC_TO_QUADRATIC_DIMENSIONLESS_RATIO_DATA_CAN_BE_FORMED_THAT_ARE_EXACTLY_INVARIANT_UNDER_THE_SINGLE_BETA_EVENT_UNIT_REPARAMETRIZATION',
      'guard':'Beta cancellation does not derive the invariant ratios themselves; same-realization finite pair/triple microscopic authority is still needed to supply their values.'
    }

def audit_fork(lane):
    beta=BETA[lane]; beta_alt=beta+F(1,lane+7)
    k=F(lane+3,lane+2); a=F(lane+2,lane+5); b=F(lane+4,lane+7)
    d1=data(beta,k,a,b); d2=data(beta_alt,k,a,b)
    # A physically different prepared event at fixed theory coefficients changes data.
    preparation_changes=(d1!=d2)
    # A calibration/reparametrization change accompanied by coefficient change does not.
    lam=beta_alt/beta
    dcal=data(beta_alt,k/lam**2,a/lam**3,b/lam**3)
    calibration_same=(dcal==d1)
    passed=preparation_changes and calibration_same
    return {
      'gate':'ITER022-G22-PREPARATION-VS-CALIBRATION-FORK','audit':'preparation-vs-calibration','lane':lane,
      'beta':str(beta),'beta_alt':str(beta_alt),'fixed_theory_data':[str(x) for x in d1],
      'changed_preparation_data':[str(x) for x in d2],'co_rescaled_calibration_data':[str(x) for x in dcal],
      'passed':passed,
      'classification':'PARTIAL_SCOPED_BETA_HAS_TWO_LOGICALLY_DISTINCT_ROLES__CHANGING_BOUNDARY_EVENT_AMPLITUDE_AT_FIXED_THEORY_COEFFICIENTS_IS_PHYSICAL_PREPARATION_DATA_WHILE_A_UNIVERSAL_CHANGE_OF_EVENT_UNIT_WITH_COMPENSATING_COEFFICIENT_REPARAMETRIZATION_IS_PURE_CALIBRATION',
      'guard':'QGR must specify which role its Boolean-to-response map plays. Neither role supplies the nonhomogeneous curved microscopic phase target required to fix c6.'
    }

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--audit',choices=AUDITS,required=True); ap.add_argument('--lane',type=int,required=True); ap.add_argument('--out',required=True)
    args=ap.parse_args(); assert 0<=args.lane<6
    fn={'reparam-invariance':audit_reparam,'authority-rank':audit_rank,'beta-invariant-ratios':audit_ratios,'preparation-vs-calibration':audit_fork}[args.audit]
    out=fn(args.lane); os.makedirs(os.path.dirname(args.out),exist_ok=True)
    with open(args.out,'w',encoding='utf-8') as f: json.dump(out,f,indent=2,sort_keys=True); f.write('\n')
    print(json.dumps(out,sort_keys=True))
    if not out['passed']: raise SystemExit(2)
if __name__=='__main__': main()
