#!/usr/bin/env python3
import json
from math import comb

# B4 Hasse graph is the 4-cube Q4. Its graph Laplacian spectrum is
# 2k with multiplicity C(4,k). Verify exactly using Walsh characters.

n = 4
vertices = list(range(1 << n))

def parity(x):
    return bin(x).count("1") & 1

def laplacian_apply(vec):
    out = [0 for _ in vertices]
    for x in vertices:
        total = n * vec[x]
        for i in range(n):
            total -= vec[x ^ (1 << i)]
        out[x] = total
    return out

observed = {}
for mask in vertices:
    chi = [(-1 if parity(mask & x) else 1) for x in vertices]
    Lchi = laplacian_apply(chi)
    k = bin(mask).count("1")
    lam = 2 * k
    assert all(Lchi[x] == lam * chi[x] for x in vertices)
    observed[lam] = observed.get(lam, 0) + 1

expected = {2*k: comb(n, k) for k in range(n+1)}
assert observed == expected

result = {
    "iteration": "008-G3",
    "lane": "b4-spectrum",
    "success": True,
    "classification": "BLOCKED_SCOPED_B4_DISCRETE_SPECTRUM_FIXES_DIMENSIONLESS_RATIOS_BUT_NOT_AN_ABSOLUTE_LENGTH_OR_REFINEMENT_STOP",
    "dimensionless_laplacian_spectrum": observed,
    "physical_scaling": "lambda_phys=lambda_dimensionless/h^2",
    "key_results": [
        "The natural B4 Hasse-graph Laplacian has exact spectrum 0,2,4,6,8 with multiplicities 1,4,6,4,1.",
        "This spectrum is purely combinatorial and dimensionless; under a physical cell rescaling h it becomes lambda_phys=lambda/h^2.",
        "All spectral ratios are fixed but the overall physical scale remains arbitrary until h or an equivalent clock/matter calibration is derived.",
        "Therefore discreteness of B4 alone is not a minimum-length theorem and cannot set the finite-history correction amplitude."
    ]
}

with open("iter008-g3-b4-spectrum.json", "w", encoding="utf-8") as f:
    json.dump(result, f, indent=2)
print(json.dumps(result, sort_keys=True))
