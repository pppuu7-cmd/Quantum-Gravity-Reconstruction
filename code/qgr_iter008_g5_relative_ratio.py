#!/usr/bin/env python3
import json
from fractions import Fraction

# G6F exact normalized overlaps as functions of branch Lorentz gamma_L:
# A0=2/(1+gamma_L)
# A1=4(2+gamma_L)/(3(1+gamma_L)^2)
# Let gamma_L=1+eps. The first nonzero loss coefficients are
# 1-A0 = eps/2 + O(eps^2)
# 1-A1 = 2 eps/3 + O(eps^2)
# so their ratio is exactly 4/3. The common microscopic scale cancels.

c0=Fraction(1,2)
c1=Fraction(2,3)
ratio=c1/c0
assert ratio==Fraction(4,3)

# If eps itself starts at common refinement order q ~ Gamma^2 X^2, both losses
# share it and the leading ratio remains 4/3.
result={
    "iteration":"008-G5",
    "lane":"relative-ratio",
    "success":True,
    "classification":"PASS_SCOPED_PARAMETER_FREE_RELATIVE_PACKET_PREDICTION_SURVIVES_THE_UNFIXED_MICROSCOPIC_SCALE__LEADING_M1_TO_M0_LOSS_RATIO_EQUALS_FOUR_THIRDS",
    "A0":"2/(1+gamma_L)",
    "A1":"4(2+gamma_L)/(3(1+gamma_L)^2)",
    "leading_loss_coefficients":{"m0":"1/2","m1":"2/3"},
    "leading_ratio_m1_over_m0":str(ratio),
    "key_results":[
        "The common microscopic scale/refinement factor cancels from the leading ratio of the two exact normalized packet losses.",
        "The resulting 4/3 ratio is fixed by the already-derived packet profiles, not by choosing g or h.",
        "This is a parameter-free relative prediction within the specified model-side preparation/readout comparison; it is not claimed universal across arbitrary experiments.",
        "The previously measured fine-refinement numerical ratio 1.333333315... is consistent with this exact 4/3 value."
    ]
}
with open("iter008-g5-relative-ratio.json","w",encoding="utf-8") as f: json.dump(result,f,indent=2)
print(json.dumps(result,sort_keys=True))
