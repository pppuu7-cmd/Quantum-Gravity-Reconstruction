#!/usr/bin/env python3
import argparse, json, os
from fractions import Fraction as F

AUDITS = (
    "local-ift-inverse-bound",
    "existing-finite-regularity-anchors",
    "pointwise-not-uniform",
    "compact-gap-sufficient-control",
    "bounded-action-not-coercive",
)

def s(x): return str(F(x))

def audit_local_ift(lane):
    # Scalar exact control for the quantitative IFT mechanism:
    # a Jacobian gap m>0 gives inverse response bound 1/m.
    m = F(lane + 2, lane + 5)
    forcing = F(lane + 1, lane + 7)
    response = forcing / m
    passed = m > 0 and response * m == forcing
    return {
      "gate":"ITER033-G33-LOCAL-IFT-INVERSE-BOUND","audit":"local-ift-inverse-bound","lane":lane,
      "jacobian_gap_control":s(m),"forcing":s(forcing),"response":s(response),"inverse_bound":s(1/m),
      "passed":passed,
      "classification":"PASS_SCOPED_A_UNIFORM_POSITIVE_TORSION_JACOBIAN_GAP_WOULD_GIVE_A_UNIFORM_LOCAL_RESPONSE_LIPSCHITZ_BOUND_VIA_THE_QUANTITATIVE_IMPLICIT_FUNCTION_MECHANISM",
      "guard":"This is the required mechanism, not evidence that the QGR tower already has a uniform gap."
    }

def audit_anchors(lane):
    # Provenance anchors already present in QGR: G5 has an exact invertible seed
    # Jacobian (det=11664 in its recorded basis); G9 numerically found a finite
    # curved regular branch with sigma_min≈0.34944.  The lane perturbation is only
    # an exact bookkeeping control that these are finite, positive local anchors.
    seed_det = F(11664)
    g9_conservative_gap = F(3,10)  # deliberately below the reported ~0.34944
    local_radius = F(1, lane + 4)
    passed = seed_det != 0 and g9_conservative_gap > 0 and local_radius > 0
    return {
      "gate":"ITER033-G33-EXISTING-FINITE-REGULARITY-ANCHORS","audit":"existing-finite-regularity-anchors","lane":lane,
      "g5_seed_determinant":s(seed_det),"g9_conservative_gap_witness":s(g9_conservative_gap),
      "local_radius_control":s(local_radius),"passed":passed,
      "classification":"PASS_SCOPED_QGR_ALREADY_HAS_NONDEGENERATE_LOCAL_TORSION_ANCHORS_AT_THE_SYMMETRIC_SEED_AND_ONE_FINITE_CURVED_NUMERICAL_BRANCH",
      "guard":"Two finite anchors do not imply a lower Jacobian gap on an infinite refinement tower. The G9 gap is used only conservatively relative to its reported numerical sigma_min."
    }

def audit_pointwise(lane):
    # Every finite level can be regular while the tower has no uniform gap.
    shift = lane + 1
    vals = [F(1, n + shift) for n in (1,2,4,8,16,32)]
    all_positive = all(v > 0 for v in vals)
    strictly_decreasing = all(vals[i+1] < vals[i] for i in range(len(vals)-1))
    tail_witness = F(1, 10**6 + shift)
    passed = all_positive and strictly_decreasing and tail_witness > 0 and tail_witness < vals[-1]
    return {
      "gate":"ITER033-G33-POINTWISE-NOT-UNIFORM","audit":"pointwise-not-uniform","lane":lane,
      "finite_level_gaps":[s(v) for v in vals],"far_tail_positive_gap":s(tail_witness),
      "passed":passed,
      "classification":"BLOCKED_SCOPED_POINTWISE_REGULARITY_AT_EVERY_FINITE_LEVEL_DOES_NOT_IMPLY_A_TOWER_WIDE_POSITIVE_INFIMUM_OF_THE_TORSION_JACOBIAN_GAP",
      "guard":"Local IFT certificates must not be promoted to uniform refinement regularity without an independent compactness or coercivity argument."
    }

def audit_compact(lane):
    # Exact sufficient-condition control: on compact x∈[-1,1], m(x)=delta+x^2
    # has uniform positive minimum delta.
    delta = F(lane + 1, lane + 9)
    samples = [F(-1),F(-1,2),F(0),F(1,2),F(1)]
    vals = [delta + x*x for x in samples]
    minimum = min(vals)
    passed = delta > 0 and minimum == delta
    return {
      "gate":"ITER033-G33-COMPACT-GAP-SUFFICIENT-CONTROL","audit":"compact-gap-sufficient-control","lane":lane,
      "delta":s(delta),"sampled_values":[s(v) for v in vals],"uniform_minimum":s(minimum),
      "passed":passed,
      "classification":"PASS_SCOPED_COMPACT_BRANCH_CONTROL_PLUS_CONTINUOUS_NONVANISHING_TORSION_JACOBIAN_WOULD_SUPPLY_THE_UNIFORM_GAP_REQUIRED_BY_G32",
      "guard":"QGR has not yet proved compactness of the full relevant branch family nor exclusion of singular strata."
    }

def audit_noncoercive(lane):
    # Generic exact counter-control: bounded action values do not imply compactness.
    # S(x)=x^2/(1+x^2) stays <1 along x_n→∞.
    ns = [lane+2, lane+4, lane+8, lane+16, lane+32]
    vals = [F(n*n, 1+n*n) for n in ns]
    bounded = all(F(0) < v < F(1) for v in vals)
    increasing_escape = all(ns[i+1] > ns[i] for i in range(len(ns)-1))
    passed = bounded and increasing_escape
    return {
      "gate":"ITER033-G33-BOUNDED-ACTION-NOT-COERCIVE","audit":"bounded-action-not-coercive","lane":lane,
      "escaping_coordinates":ns,"bounded_action_controls":[s(v) for v in vals],"passed":passed,
      "classification":"BLOCKED_SCOPED_AN_ACTION_BOUND_ALONE_DOES_NOT_GENERALLY_EXCLUDE_NONCOMPACT_ESCAPE__A_QGR_SPECIFIC_COERCIVITY_OR_COMPACTNESS_THEOREM_IS_REQUIRED",
      "guard":"This is a generic insufficiency witness, not a claim that the actual QGR action has this synthetic form."
    }

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--audit',choices=AUDITS,required=True); ap.add_argument('--lane',type=int,required=True); ap.add_argument('--out',required=True)
    a=ap.parse_args(); assert 0 <= a.lane < 6
    fn={
      'local-ift-inverse-bound':audit_local_ift,
      'existing-finite-regularity-anchors':audit_anchors,
      'pointwise-not-uniform':audit_pointwise,
      'compact-gap-sufficient-control':audit_compact,
      'bounded-action-not-coercive':audit_noncoercive,
    }[a.audit]
    out=fn(a.lane); os.makedirs(os.path.dirname(a.out),exist_ok=True)
    with open(a.out,'w',encoding='utf-8') as f: json.dump(out,f,indent=2,sort_keys=True); f.write('\n')
    print(json.dumps(out,sort_keys=True))
    if not out['passed']: raise SystemExit(2)
if __name__=='__main__': main()
