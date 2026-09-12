#!/usr/bin/env python3
import json
from fractions import Fraction

n = 4
C = [[(0 if i == j else 1) for j in range(n)] for i in range(n)]  # J-I
E = [[(-1 if i == j else 0) + Fraction(1, 3) for j in range(n)] for i in range(n)]  # C^-1

def quad(M, v):
    return sum(v[i] * M[i][j] * v[j] for i in range(n) for j in range(n))

covers = []
for i in range(n):
    e = [Fraction(0) for _ in range(n)]
    e[i] = Fraction(1)
    covers.append(quad(C, e))

rank_grad = [Fraction(1) for _ in range(n)]
mean_step = [Fraction(1, 4) for _ in range(n)]

rank_tangent_norm = quad(C, rank_grad)
rank_covector_norm = quad(E, rank_grad)
mean_step_norm = quad(C, mean_step)

assert all(x == 0 for x in covers)
assert rank_tangent_norm == 12
assert rank_covector_norm == Fraction(4, 3)
assert mean_step_norm == Fraction(3, 4)

result = {
    "iteration": "008-G3",
    "lane": "clock-geometry",
    "success": True,
    "classification": "PARTIAL_SCOPED_RANK_CLOCK_HAS_DERIVED_TIMELIKE_SYMMETRIC_DIRECTION_BUT_ELEMENTARY_UNIT_TICKS_ARE_NULL__NO_UNIQUE_PROPER_TIME_PER_TICK",
    "cover_edge_C_norms": [str(x) for x in covers],
    "rank_symmetric_tangent_C_norm": str(rank_tangent_norm),
    "rank_covector_E_norm": str(rank_covector_norm),
    "barycentric_mean_step_C_norm": str(mean_step_norm),
    "key_results": [
        "Every elementary B4 cover raises rank by one but is exactly null in the derived C=J-I geometry.",
        "The S4-symmetric rank direction is timelike, while the average of the four possible unit covers is timelike with dimensionless norm 3/4.",
        "The barycentric average is not an actual history edge; using it as a proper-time tick requires an additional coarse/readout prescription.",
        "Therefore rank gives causal ordering and a timelike coarse direction but does not calibrate one unit tick as nonzero physical proper time or fix h."
    ]
}

with open("iter008-g3-clock-geometry.json", "w", encoding="utf-8") as f:
    json.dump(result, f, indent=2)
print(json.dumps(result, sort_keys=True))
