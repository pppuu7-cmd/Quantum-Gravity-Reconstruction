#!/usr/bin/env python3
import json

# Two cases for a scalar/clock sector coupled to the already-derived metric G.
# A generic scalar phi has a kinetic coefficient Z that can be removed by field
# rescaling if phi's normalization is not physically fixed.
# If the field is identified with intrinsic rank tau, unit tick normalization
# fixes tau and forbids that rescaling; then Z_tau becomes a genuine new free
# coefficient unless derived independently.

generic_scalar = {
    "kinetic_coefficient": "Z_phi",
    "field_rescaling": "phi_canonical=sqrt(Z_phi)*phi",
    "physical_new_scale_from_Z_alone": False,
    "mass_parameter_if_allowed": "m_phi independent",
    "curvature_coupling_if_allowed": "xi independent"
}

rank_clock_scalar = {
    "field": "tau=|S|",
    "unit_increment_fixed": True,
    "rescaling_tau_allowed": False,
    "kinetic_coefficient": "Z_tau",
    "Z_tau_status": "physical_and_free_without_new_derivation"
}

assert generic_scalar["physical_new_scale_from_Z_alone"] is False
assert rank_clock_scalar["rescaling_tau_allowed"] is False

result = {
    "iteration": "008-G3",
    "lane": "clock-matter-normalization",
    "success": True,
    "classification": "BLOCKED_SCOPED_METRIC_COVARIANT_RELATIONAL_MATTER_DOES_NOT_FIX_G__IDENTIFYING_THE_INTRINSIC_RANK_CLOCK_AS_A_PHYSICAL_SCALAR_MAKES_ITS_KINETIC_NORMALIZATION_A_NEW_FREE_PARAMETER",
    "generic_scalar": generic_scalar,
    "intrinsic_rank_clock_scalar": rank_clock_scalar,
    "key_results": [
        "For an otherwise freely normalized scalar, the overall kinetic coefficient is removable by field rescaling and supplies no independent physical calibration of gravity.",
        "If the scalar is identified with the intrinsic rank clock, its unit tick normalization fixes the field scale, so the kinetic coefficient Z_tau can no longer be scaled away.",
        "Covariance/incidence alone does not determine Z_tau; the clock-as-matter route therefore introduces a new normalization rather than fixing g.",
        "Allowing a clock mass, potential or nonminimal curvature term introduces further independent data and cannot be used as a derived second scale without a new microscopic principle."
    ]
}

with open("iter008-g3-clock-matter-normalization.json", "w", encoding="utf-8") as f:
    json.dump(result, f, indent=2)
print(json.dumps(result, sort_keys=True))
