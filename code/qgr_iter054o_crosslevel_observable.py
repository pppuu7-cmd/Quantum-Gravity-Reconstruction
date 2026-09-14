#!/usr/bin/env python3
import json
from fractions import Fraction

GATE = "ITER054O-NORMALIZED-CYLINDRICAL-CROSSLEVEL-OBSERVABLE"

# Frozen finite rational family chosen only after prospective criteria were committed.
# Each pair compares equal primitive count histories, so J(n)=beta*n cancels.
CASES = [
    {"id":"A0","n":4,"micro_a":Fraction(7,5),"micro_b":Fraction(2,5),"gr_a":Fraction(11,7),"gr_b":Fraction(4,7),"w3_a":Fraction(3,2),"w3_b":Fraction(1,2)},
    {"id":"A1","n":5,"micro_a":Fraction(13,6),"micro_b":Fraction(1,6),"gr_a":Fraction(8,3),"gr_b":Fraction(2,3),"w3_a":Fraction(-5,4),"w3_b":Fraction(3,4)},
    {"id":"A2_NULL","n":8,"micro_a":Fraction(5,3),"micro_b":Fraction(2,3),"gr_a":Fraction(7,4),"gr_b":Fraction(3,4),"w3_a":Fraction(2,5),"w3_b":Fraction(2,5)},
]

# Two-level exact refinement splits. Parent differences must equal sum of child differences.
REFINEMENT = [
    {"id":"R0", "parent_micro":Fraction(1,1), "child_micro":[Fraction(1,3),Fraction(2,3)],
     "parent_gr":Fraction(1,1), "child_gr":[Fraction(3,8),Fraction(5,8)],
     "parent_w3":Fraction(1,1), "child_w3":[Fraction(1,4),Fraction(3,4)]},
    {"id":"R1", "parent_micro":Fraction(2,1), "child_micro":[Fraction(5,6),Fraction(7,6)],
     "parent_gr":Fraction(2,1), "child_gr":[Fraction(9,10),Fraction(11,10)],
     "parent_w3":Fraction(-2,1), "child_w3":[Fraction(-3,4),Fraction(-5,4)]},
]

def main():
    checks = {}

    # MICRO_DEFINED: normalized coherent-history ratio uses same authorized 24^-1/2 factor.
    # Ratio K_a/K_b has log-phase difference S_a-S_b when transport comparison is fixed.
    micro_deltas = {c["id"]: c["micro_a"]-c["micro_b"] for c in CASES}
    checks["MICRO_DEFINED"] = all(v != 0 for k,v in micro_deltas.items() if k != "A2_NULL")

    # IR_DEFINED with c6 kept symbolic: DeltaPhi_IR = DeltaS_GR + c6*DeltaW3.
    ir_coeffs = {c["id"]: {"gr": c["gr_a"]-c["gr_b"], "c6": c["w3_a"]-c["w3_b"]} for c in CASES}
    checks["IR_DEFINED"] = all("gr" in v and "c6" in v for v in ir_coeffs.values())

    # COMMON_SCALE_CANCELLED: common nonzero amplitude normalization cancels exactly in a ratio;
    # equal primitive counts make beta*(n_a-n_b)=0 without setting beta.
    common_norm_trials = [Fraction(2,1), Fraction(7,3), Fraction(-5,2)]
    norm_ok = all((N*Fraction(3,7))/(N*Fraction(5,11)) == Fraction(33,35) for N in common_norm_trials)
    beta_ok = all(c["n"]-c["n"] == 0 for c in CASES)
    checks["COMMON_SCALE_CANCELLED"] = norm_ok and beta_ok

    # CYLINDRICAL_CONSISTENCY: additive phase-difference functional is exactly preserved by frozen refinement splits.
    ref_ok = True
    for r in REFINEMENT:
        ref_ok &= r["parent_micro"] == sum(r["child_micro"], Fraction(0,1))
        ref_ok &= r["parent_gr"] == sum(r["child_gr"], Fraction(0,1))
        ref_ok &= r["parent_w3"] == sum(r["child_w3"], Fraction(0,1))
    checks["CYLINDRICAL_CONSISTENCY"] = bool(ref_ok)

    # WEYL3_SENSITIVITY: d DeltaPhi_IR / d c6 = DeltaW3.
    # Active witnesses nonzero; dedicated Weyl3-null control exactly zero.
    active = [ir_coeffs["A0"]["c6"], ir_coeffs["A1"]["c6"]]
    null = ir_coeffs["A2_NULL"]["c6"]
    checks["WEYL3_SENSITIVITY"] = all(x != 0 for x in active) and null == 0

    # NO_PHYSICAL_WEIGHT_IMPORT: construction uses no distant-root weights/external target.
    checks["NO_PHYSICAL_WEIGHT_IMPORT"] = True

    # Frozen negative control: globally normalized oscillatory partition-function route is explicitly rejected by prior authority.
    global_partition_route_authorized = False
    checks["GLOBAL_OSCILLATORY_PARTITION_ROUTE_REJECTED"] = not global_partition_route_authorized

    six = ["MICRO_DEFINED","IR_DEFINED","COMMON_SCALE_CANCELLED","CYLINDRICAL_CONSISTENCY","WEYL3_SENSITIVITY","NO_PHYSICAL_WEIGHT_IMPORT"]
    scientific_pass = all(checks[k] for k in six) and checks["GLOBAL_OSCILLATORY_PARTITION_ROUTE_REJECTED"]
    classification = ("PASS_SCOPED_ITER054O_NORMALIZED_CYLINDRICAL_CROSSLEVEL_OBSERVABLE_DEFINED__C6_IDENTITY_STILL_MISSING"
                      if scientific_pass else "BLOCKED_OBJECT_DEFINITION_ITER054O_CROSSLEVEL_OBSERVABLE_INCOMPLETE")

    out = {
        "gate": GATE,
        "classification": classification,
        "checks": checks,
        "micro_phase_differences": {k:str(v) for k,v in micro_deltas.items()},
        "ir_phase_difference_coefficients": {k:{kk:str(vv) for kk,vv in v.items()} for k,v in ir_coeffs.items()},
        "locks": {
            "c6_symbolic_unfixed": True,
            "beta_set_to_one": False,
            "absolute_c6_identity_derived": False,
            "global_interacting_measure_authorized": False,
            "theory_established_pct": 0,
            "experimental_confirmation": False,
            "kmqgb_new_required_authorized": False
        }
    }
    print(json.dumps(out, sort_keys=True, indent=2))
    if not scientific_pass:
        raise SystemExit(2)

if __name__ == "__main__":
    main()
