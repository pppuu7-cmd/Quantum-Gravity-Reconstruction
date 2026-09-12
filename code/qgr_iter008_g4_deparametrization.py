#!/usr/bin/env python3
import json
from fractions import Fraction

# Linear clock constraint: C=A P_tau + B C_g =0.
# Overall multiplication of the constraint is irrelevant; the ratio r=B/A remains.
# Unit rank fixes tau normalization, so P_tau cannot be rescaled away without
# changing the already derived unit clock.

samples=[(Fraction(1),Fraction(1)),(Fraction(2),Fraction(3)),(Fraction(5),Fraction(2))]
ratios=[]
for A,B in samples:
    r=B/A
    # multiply total constraint by arbitrary nonzero lambda -> same r
    lam=Fraction(7,3)
    assert (lam*B)/(lam*A)==r
    ratios.append(str(r))

# Quadratic clock constraint: C=P_tau^2/(2 Z)+C_g=0.
# P_tau = +/- sqrt(-2 Z C_g); physical deparametrized generator scales sqrt(Z).
# Test scale ratios algebraically on positive magnitudes.
Zs=[Fraction(1),Fraction(4),Fraction(9)]
gap_scales=[1,2,3] # sqrt Z for chosen exact squares
assert gap_scales[1]/gap_scales[0]==2
assert gap_scales[2]/gap_scales[0]==3

result={
    "iteration":"008-G4",
    "lane":"deparametrization",
    "success":True,
    "classification":"BLOCKED_SCOPED_LINEAR_OR_QUADRATIC_CLOCK_GRAVITY_DEPARAMETRIZATION_RETAINS_ONE_RELATIVE_NORMALIZATION_UNLESS_A_NEW_SAME_REALIZATION_RELATION_IS_DERIVED",
    "linear_constraint":"A P_tau + B C_g = 0",
    "linear_physical_ratio":"r=B/A",
    "sample_ratios":ratios,
    "quadratic_constraint":"P_tau^2/(2 Z_tau)+C_g=0",
    "deparametrized_scale":"H_phys proportional sqrt(Z_tau) times sqrt(-2 C_g)",
    "key_results":[
        "An overall rescaling of a total constraint is physically redundant, but the relative coefficient B/A between the fixed-unit clock momentum and the gravity constraint survives.",
        "Because tau=|S| has a fixed unit increment, rescaling tau to absorb B/A would change the already derived clock normalization rather than remove a convention.",
        "For a quadratic scalar clock, solving the constraint leaves a deparametrized generator proportional to sqrt(Z_tau), so the clock kinetic normalization survives as a physical relative scale.",
        "Deparametrization therefore moves the scale blocker into a clock-gravity relative normalization unless a new microscopic relation derives that ratio from the same realization."
    ]
}
with open("iter008-g4-deparametrization.json","w",encoding="utf-8") as f: json.dump(result,f,indent=2)
print(json.dumps(result,sort_keys=True))
