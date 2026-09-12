#!/usr/bin/env python3
import json, math

# The minimal Hermitian translation-invariant nearest-neighbour clock generator
# on an extended serial rank lattice is H = eps I + J(2I-T-T^-1).
# eps is an unobservable common energy offset. J is the only nontrivial scale.
# The dimensionless dispersion is lambda(theta)=2-2cos(theta).

thetas = [0.0, math.pi/6, math.pi/4, math.pi/3, math.pi/2, math.pi]
lambdas = [2.0 - 2.0*math.cos(t) for t in thetas]

# Rescaling J changes every physical energy gap but preserves symmetry,
# eigenvectors and all dimensionless spectral ratios.
J1, J2 = 1.0, 7.0
E1 = [J1*x for x in lambdas]
E2 = [J2*x for x in lambdas]
for a, b in zip(E1[1:], E2[1:]):
    assert abs(b/a - 7.0) < 1e-12

result = {
    "iteration": "008-G3",
    "lane": "clock-dynamics",
    "success": True,
    "classification": "BLOCKED_SCOPED_MINIMAL_RANK_TRANSLATION_INVARIANT_CLOCK_DYNAMICS_HAS_ONE_FREE_FREQUENCY_SCALE_AFTER_REMOVING_COMMON_PHASE",
    "dimensionless_dispersion": "lambda(theta)=2-2 cos(theta)=4 sin^2(theta/2)",
    "nontrivial_scale_parameters": 1,
    "free_scale_name": "J_clock",
    "sample_dimensionless_eigenvalues": lambdas,
    "key_results": [
        "Hermiticity and rank-translation symmetry fix the nearest-neighbour clock generator only up to one nontrivial hopping/frequency scale J_clock plus a removable common phase offset.",
        "Rescaling J_clock preserves every dimensionless spectral ratio and the intrinsic rank ordering while changing all physical energy gaps.",
        "The exact one-tick branch/isometry normalization from G2 does not constrain J_clock because it fixes probability modulus rather than clock Hamiltonian phase scale.",
        "Therefore a dynamical clock extension does not calibrate g unless an additional same-realization principle relates J_clock to the gravitational action normalization."
    ]
}

with open("iter008-g3-clock-dynamics.json", "w", encoding="utf-8") as f:
    json.dump(result, f, indent=2)
print(json.dumps(result, sort_keys=True))
