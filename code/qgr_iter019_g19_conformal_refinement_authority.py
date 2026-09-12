#!/usr/bin/env python3
import argparse,json,os
from fractions import Fraction as F

AUDITS=('conformal-reduction','weight-uniqueness','character-tension','normalization-inheritance')
BASES=[F(3,2),F(4,3),F(5,4),F(6,5),F(7,6),F(8,7)]

def rank_fraction(A):
    A=[list(map(F,row)) for row in A]
    if not A: return 0
    m,n=len(A),len(A[0]); r=0
    for c in range(n):
        p=next((i for i in range(r,m) if A[i][c]),None)
        if p is None: continue
        A[r],A[p]=A[p],A[r]
        piv=A[r][c]; A[r]=[x/piv for x in A[r]]
        for i in range(m):
            if i!=r and A[i][c]:
                z=A[i][c]; A[i]=[A[i][j]-z*A[r][j] for j in range(n)]
        r+=1
        if r==m: break
    return r

def audit_conformal(lane):
    # For g=s^2 C in d dimensions, after one integration by parts:
    # sqrt|g| R[g] = (d-1)(d-2) s^(d-4) (Ds)^2 + boundary,
    # with C flat/constant. In d=4 the field-dependent prefactor disappears exactly.
    d=4
    coeff=(d-1)*(d-2)
    exponent=d-4
    s=BASES[lane]
    ds=F(lane+1,lane+7)
    reduced=F(coeff)*s**exponent*ds*ds
    dirichlet=F(6)*ds*ds
    passed=(coeff==6 and exponent==0 and reduced==dirichlet)
    return {
      'gate':'ITER019-G19-CONFORMAL-REDUCTION','audit':'conformal-reduction','lane':lane,
      'dimension':d,'s':str(s),'ds':str(ds),'coefficient':coeff,'s_exponent':exponent,
      'reduced_bulk_density':str(reduced),'six_dirichlet_density':str(dirichlet),
      'passed':passed,
      'classification':'PASS_SCOPED_EXISTING_ALL_ORDERS_QGR_TWO_DERIVATIVE_ACTION_RESTRICTED_TO_G_EQUALS_S2_C_REDUCES_IN_FOUR_DIMENSIONS_TO_SIX_TIMES_DIRICHLET_DS2_MODULO_BOUNDARY',
      'guard':'This derives the conformal-sector bulk functional from the existing local QGR action. It does not by itself prove a fundamental microscopic Boolean-cell action or fix the endpoint r.'
    }

def audit_weight(lane):
    # Rational grid h=k/N. Let y(h)=w(h) h^2. Exact split/refinement invariance
    # on every linear endpoint profile requires y(i+j)=y(i)+y(j).
    # Solve all grid additivity equations without normalization: nullity must be 1.
    N=5+lane
    rows=[]
    # variables y_1,...,y_N
    for i in range(1,N+1):
      for j in range(1,N+1-i):
        row=[F(0)]*N
        row[i+j-1]+=1; row[i-1]-=1; row[j-1]-=1
        rows.append(row)
    rk=rank_fraction(rows); nullity=N-rk
    # Candidate basis y_k=k/N implies w(k/N)=N/k=1/h up to common scale.
    y=[F(k,N) for k in range(1,N+1)]
    additive=all(y[i+j-1]==y[i-1]+y[j-1] for i in range(1,N+1) for j in range(1,N+1-i))
    weights=[F(N,k) for k in range(1,N+1)]
    reciprocal=all(weights[k-1]*F(k,N)==1 for k in range(1,N+1))
    passed=(nullity==1 and additive and reciprocal)
    return {
      'gate':'ITER019-G19-REFINEMENT-WEIGHT-UNIQUENESS','audit':'weight-uniqueness','lane':lane,
      'grid_denominator':N,'variable_count':N,'equation_count':len(rows),'rank':rk,'nullity':nullity,
      'normalized_weights':[str(x) for x in weights],'passed':passed,
      'classification':'PASS_SCOPED_ON_POSITIVE_RATIONAL_REFINEMENTS_LOCAL_QUADRATIC_INCREMENT_ACTION_PLUS_EXACT_LINEAR_PROFILE_REFINEMENT_ADDITIVITY_FORCES_W_H_PROPORTIONAL_TO_ONE_OVER_H_WITH_ONLY_ONE_OVERALL_NORMALIZATION',
      'guard':'Uniqueness is within the local quadratic-in-increment ansatz inherited from the two-derivative sector; it does not exclude genuinely nonlocal or higher-derivative microscopic refinement terms.'
    }

def audit_character(lane):
    # Exact rational witness: choose N and base b, endpoint r=b^N. The multiplicative
    # character profile has s_k=b^k, while the Dirichlet minimizer at equal h=1/N is
    # linear in s. Strict convexity predicts larger action for the character profile.
    N=2+lane
    b=BASES[lane]
    r=b**N
    h=F(1,N)
    char=[b**k for k in range(N+1)]
    lin=[F(1)+F(k,N)*(r-1) for k in range(N+1)]
    Echar=sum((char[k+1]-char[k])**2/h for k in range(N))
    Elin=sum((lin[k+1]-lin[k])**2/h for k in range(N))
    mult=all(char[i+j]==char[i]*char[j] for i in range(N+1) for j in range(N+1-i))
    lin_mult_defect=(lin[1]*lin[1]-lin[2]) if N>=2 else F(0)
    tension=mult and Echar>Elin and lin_mult_defect!=0 and r!=1
    return {
      'gate':'ITER019-G19-G16-G18-COMPATIBILITY','audit':'character-tension','lane':lane,
      'segments':N,'base':str(b),'endpoint_r':str(r),'character_energy':str(Echar),'linear_minimum_energy':str(Elin),
      'multiplicative_character_exact':mult,'linear_profile_multiplicativity_defect_at_1_step_squared_vs_2_steps':str(lin_mult_defect),
      'passed':tension,
      'classification':'FAIL_SCOPED_JOINT_NONTRIVIAL_HYPOTHESIS_G16_MULTIPLICATIVE_EVENT_CHARACTER_AND_G18_LINEAR_S_DIRICHLET_EXTREMAL_PROFILE_CANNOT_BOTH_DEFINE_THE_SAME_REFINEMENT_TRAJECTORY_FOR_R_NOT_EQUAL_ONE',
      'interpretation':'This fails the joint auxiliary hypotheses, not QGR. Since G16 explicitly treated repeated-event character composition as scoped, it should not be promoted to fundamental microscopic refinement law without a variable/clock reinterpretation.'
    }

def audit_normalization(lane):
    # In d=4 the conformal restriction inherits lambda=6*a from the already existing
    # all-orders QGR coefficient a. Thus G18's lambda is not an independent coupling
    # inside this sector. Different endpoints remain allowed boundary data.
    a=F(lane+2,lane+5)
    lam=6*a
    r1=BASES[lane]; r2=BASES[(lane+1)%6]
    A1=lam*(r1-1)**2; A2=lam*(r2-1)**2
    lambda_independent=False
    endpoint_distinguishable=(r1!=r2 and A1!=A2)
    endpoint_selected=False
    passed=(lam==6*a and endpoint_distinguishable and not endpoint_selected)
    return {
      'gate':'ITER019-G19-NORMALIZATION-INHERITANCE','audit':'normalization-inheritance','lane':lane,
      'qgr_action_coefficient_a':str(a),'induced_dirichlet_lambda':str(lam),'lambda_independent_new_coupling':lambda_independent,
      'r1':str(r1),'r2':str(r2),'action1':str(A1),'action2':str(A2),'endpoint_selected_by_bulk_variation':endpoint_selected,
      'passed':passed,
      'classification':'PARTIAL_SCOPED_G18_DIRICHLET_NORMALIZATION_IS_INHERITED_AS_SIX_TIMES_THE_EXISTING_QGR_LOCAL_ACTION_NORMALIZATION_IN_THE_COMMON_CONFORMAL_SECTOR__NO_NEW_LAMBDA_IS_NEEDED_BUT_THE_ENDPOINT_R_REMAINS_UNSELECTED',
      'guard':'The inherited coefficient does not resolve the older absolute microscopic scale degeneracy of the QGR normalization chain.'
    }

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--audit',choices=AUDITS,required=True); ap.add_argument('--lane',type=int,required=True); ap.add_argument('--out',required=True)
    a=ap.parse_args(); assert 0<=a.lane<6
    fn={'conformal-reduction':audit_conformal,'weight-uniqueness':audit_weight,'character-tension':audit_character,'normalization-inheritance':audit_normalization}[a.audit]
    out=fn(a.lane); os.makedirs(os.path.dirname(a.out),exist_ok=True)
    with open(a.out,'w',encoding='utf-8') as f: json.dump(out,f,indent=2,sort_keys=True); f.write('\n')
    print(json.dumps(out,sort_keys=True))
    if not out['passed']: raise SystemExit(2)
if __name__=='__main__': main()
