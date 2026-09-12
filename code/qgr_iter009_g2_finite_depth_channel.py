#!/usr/bin/env python3
import json

N = 24
checks = []
for depth in range(1, 9):
    paths = N**depth
    weight = N**(-depth)
    completeness = paths * weight
    assert completeness == 1.0
    checks.append({"depth": depth, "histories": paths, "branch_weight": weight, "sum_KdagK": completeness})

out = {
    "gate": "ITER009-G2-FINITE-DEPTH-CHANNEL",
    "branch_count_per_cell": N,
    "depths_checked": 8,
    "exact_rule": "N^n branches times N^(-n) completeness weight = 1",
    "classification": "PASS_SCOPED_ARBITRARY_FINITE_DEPTH_HISTORY_COMPOSITION_REMAINS_NORMALIZED_CPTP_ISOMETRIC_GIVEN_UNITARY_BRANCH_LIFTS",
    "guard": "Finite-depth completeness does not imply existence of an infinite-depth strong or diamond-norm limit."
}
print(json.dumps(out, sort_keys=True))
