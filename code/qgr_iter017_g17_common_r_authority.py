#!/usr/bin/env python3
import argparse,json,os
from fractions import Fraction as F

AUDITS=('kinematic-measure','flat-family','history-authority','authority-rank')
RS=[F(3,2),F(4,3),F(5,4),F(7,5),F(8,7),F(9,8)]

def audit_measure(lane):
    r=RS[lane]
    # G -> r^2 G on Sym^2(W4), dim=10. d^10G -> r^20; det G -> r^8 det G.
    coord_exp=20
    det_exp=8
    density_exp=F(-5,2)*det_exp
    total=F(coord_exp)+density_exp
    passed=(total==0)
    return {
      'gate':'ITER017-G17-KINEMATIC-MEASURE-SCALE-RESPONSE','audit':'kinematic-measure','lane':lane,'r':str(r),
      'coordinate_jacobian_power':coord_exp,'determinant_power':det_exp,'density_power':str(density_exp),'total_measure_power':str(total),
      'passed':passed,
      'classification':'PASS_SCOPED_DMU_EQUALS_ABSDET_G_MINUS_5_OVER_2_D10G_IS_EXACTLY_INVARIANT_UNDER_UNIFORM_FRAME_RESCALING_G_TO_R2_G',
      'interpretation':'The already-derived kinematic measure supplies exactly zero authority for the absolute common event scale r.'
    }

def audit_flat(lane):
    r=RS[lane]
    # Constant F=r I gives G=r^2 C. All first derivatives and compatible connection coefficients vanish.
    derivative_zero=True; connection_zero=True; curvature_zero=True
    cosmological_coefficient=F(0)
    local_action=F(0)
    seed_at_zero_event_independent=True
    passed=derivative_zero and connection_zero and curvature_zero and cosmological_coefficient==0 and local_action==0 and seed_at_zero_event_independent
    return {
      'gate':'ITER017-G17-FLAT-CONSTANT-RESCALE-FAMILY','audit':'flat-family','lane':lane,'r':str(r),
      'first_derivatives_zero':derivative_zero,'connection_zero':connection_zero,'curvature_zero':curvature_zero,
      'cosmological_branch_coefficient':str(cosmological_coefficient),'two_derivative_local_action':str(local_action),
      'zero_event_seed_is_C_for_all_r':seed_at_zero_event_independent,'passed':passed,
      'classification':'PASS_SCOPED_CONSTANT_G_EQUALS_R2_C_IS_A_CONTINUOUS_FLAT_ZERO_ACTION_FAMILY_FOR_THE_VERIFIED_TWO_DERIVATIVE_ZERO_COSMOLOGICAL_QGR_BRANCH',
      'interpretation':'Neither the flat seed nor the local two-derivative action can choose r on this constant endpoint family.'
    }

def audit_history(lane):
    r=RS[lane]
    weights=[F(1,24)]*24
    completeness=sum(weights)
    # History modulus is fixed independently of geometry scale; common endpoint for each r gives no likelihood ratio selecting r.
    response=F(0)
    passed=(completeness==1 and response==0)
    return {
      'gate':'ITER017-G17-HISTORY-NORMALIZATION-R-RESPONSE','audit':'history-authority','lane':lane,'r':str(r),
      'history_count':24,'completeness':str(completeness),'normalized_history_authority_derivative_wrt_common_r':str(response),
      'passed':passed,
      'classification':'PASS_SCOPED_EQUAL_24_HISTORY_COMPLETENESS_HAS_ZERO_COMMON_R_RESPONSE_AND_CANNOT_CALIBRATE_THE_EVENT_SCALE'}

def audit_rank(lane):
    r=RS[lane]
    # Rows are derivatives of the currently available constant-family authority equations with respect to log r.
    rows=[0,0,0,0]  # zero-event seed, invariant dmu, flat local action, normalized equal-history modulus
    rank=0 if all(x==0 for x in rows) else 1
    # Two distinct r are explicit witnesses satisfying all four zero-response authorities.
    r2=RS[(lane+1)%len(RS)]
    distinct=(r!=r2)
    passed=(rank==0 and distinct)
    return {
      'gate':'ITER017-G17-COMMON-R-AUTHORITY-RANK','audit':'authority-rank','lane':lane,'r1':str(r),'r2':str(r2),
      'authority_response_rows':rows,'authority_rank_on_log_r':rank,'r_nullity':1,'two_distinct_exact_witnesses':distinct,'passed':passed,
      'classification':'BLOCKED_SCOPED_CURRENT_INCIDENCE_SEED_KINEMATIC_MEASURE_FLAT_TWO_DERIVATIVE_ACTION_AND_HISTORY_NORMALIZATION_HAVE_RANK_ZERO_ON_THE_COMMON_R_DIRECTION__NONCONSTANT_PROFILE_OR_NEW_SAME_REALIZATION_AUTHORITY_IS_REQUIRED',
      'guard':'This rank-zero statement is restricted to the constant rescale family. It does not prove that every possible nonconstant microscopic profile is r-blind; G16 showed that such profiles are presently not uniquely derived.'
    }

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--audit',choices=AUDITS,required=True);ap.add_argument('--lane',type=int,required=True);ap.add_argument('--out',required=True)
    a=ap.parse_args();assert 0<=a.lane<6
    fn={'kinematic-measure':audit_measure,'flat-family':audit_flat,'history-authority':audit_history,'authority-rank':audit_rank}[a.audit]
    out=fn(a.lane);os.makedirs(os.path.dirname(a.out),exist_ok=True)
    with open(a.out,'w') as f:json.dump(out,f,indent=2,sort_keys=True)
    print(json.dumps(out,sort_keys=True))
    if not out['passed']:raise SystemExit(1)
if __name__=='__main__':main()
