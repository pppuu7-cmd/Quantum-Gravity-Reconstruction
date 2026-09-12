#!/usr/bin/env python3
import json
from fractions import Fraction

# Diagnostic ordinary scalar clock on flat +--- background with normalized
# timelike gradient u_mu=(1,0,0,0):
# T_mn = Z (u_m u_n - 1/2 eta_mn u^2), u^2=1.
eta=[1,-1,-1,-1]
u=[1,0,0,0]
Z=Fraction(1,1)
T=[]
for mu in range(4):
    row=[]
    for nu in range(4):
        eta_mn=eta[mu] if mu==nu else 0
        row.append(Z*(u[mu]*u[nu]-Fraction(1,2)*eta_mn))
    T.append(row)
expected=[[Fraction(1,2),0,0,0],[0,Fraction(1,2),0,0],[0,0,Fraction(1,2),0],[0,0,0,Fraction(1,2)]]
assert T==expected

# No nonzero Z makes this stress tensor vanish for fixed nonzero u.
for z in [Fraction(1,7),Fraction(1),Fraction(13,3)]:
    assert z*Fraction(1,2)!=0

result={
    "iteration":"008-G4",
    "lane":"clock-backreaction",
    "success":True,
    "classification":"FAIL_SCOPED_ORDINARY_DYNAMICAL_RANK_CLOCK_SCALAR_CANNOT_PRESERVE_THE_ESTABLISHED_ZERO_LAMBDA_FLAT_VACUUM_BRANCH_WITH_NONZERO_KINETIC_NORMALIZATION_WITHOUT_NEW_BACKREACTION_OR_COMPENSATION_DATA",
    "flat_signature":"+---",
    "unit_timelike_gradient":"u=(1,0,0,0)",
    "stress_tensor_for_Z_equal_1":[[str(x) for x in row] for row in T],
    "key_results":[
        "An ordinary scalar interpretation of the intrinsic clock with nonzero timelike gradient carries nonzero stress energy for every nonzero kinetic normalization Z_tau.",
        "The established active QGR branch used a flat zero-cosmological vacuum seed; adding this clock as ordinary matter changes that background rather than merely calibrating it.",
        "Taking Z_tau to zero makes the clock a probe/label but removes its ability to supply a physical energy scale.",
        "Cancelling the clock stress with a potential, cosmological term or second matter sector would introduce additional tuned data not derived by the current CCRC realization."
    ]
}
with open("iter008-g4-clock-backreaction.json","w",encoding="utf-8") as f: json.dump(result,f,indent=2)
print(json.dumps(result,sort_keys=True))
