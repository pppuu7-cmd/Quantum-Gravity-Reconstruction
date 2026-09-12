#!/usr/bin/env python3
import json

# In 4D, parity-even local scalar densities quadratic in curvature may be based on
# Riemann^2, Ricci^2, R^2. The Euler (Gauss-Bonnet) density gives one topological
# linear combination E4=Riemann^2-4 Ricci^2+R^2. Box R is a total derivative.
# Therefore the local bulk quotient has dimension 3-1=2.

basis=["Riemann^2","Ricci^2","R^2"]
euler=[1,-4,1]
rank_relations=1 if any(euler) else 0
bulk_dim=len(basis)-rank_relations
assert bulk_dim==2

# Two convenient quotient bases are {R^2,Ricci^2} or {R^2,Weyl^2}; selection is
# not made here.
result={
    "iteration":"009-G1",
    "lane":"four-derivative-census",
    "success":True,
    "classification":"BLOCKED_SCOPED_TWO_INDEPENDENT_PARITY_EVEN_FOUR_DERIVATIVE_LOCAL_METRIC_BULK_DIRECTIONS_REMAIN_SYMMETRY_ALLOWED_IN_4D",
    "raw_curvature_squared_basis":basis,
    "euler_relation_coefficients":euler,
    "total_derivative":"Box R",
    "independent_bulk_dimension":bulk_dim,
    "key_results":[
        "The unique two-derivative Einstein-Hilbert action does not imply uniqueness once four-derivative local metric operators are admitted.",
        "Modulo the 4D Euler density and total derivatives, two independent parity-even curvature-squared bulk directions remain.",
        "Diffeomorphism/BRST symmetry allows these operators; their absence or coefficients must therefore come from microscopic refinement dynamics, not symmetry alone.",
        "No arbitrary R^2/Ricci^2 coefficient is introduced here and no claim is made that either coefficient is actually generated."
    ]
}
with open("iter009-g1-four-derivative-census.json","w",encoding="utf-8") as f: json.dump(result,f,indent=2)
print(json.dumps(result,sort_keys=True))
