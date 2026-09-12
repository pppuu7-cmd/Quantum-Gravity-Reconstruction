#!/usr/bin/env python3
import json, math

# Leading specified-preparation loss:
# Delta = C * Gamma^2 * X^2,  X=ell_Q^2 R_eff.
# Any future upper bound Delta <= delta_max with C>0 and X!=0 gives
# Gamma <= sqrt(delta_max/C)/|X|.
# In frozen |c_geom|=1/2 convention, |g| = 2 Gamma.

def gamma_bound(delta_max,C,X):
    return math.sqrt(delta_max/C)/abs(X)

tests=[
    (1e-6,1.0,0.1),
    (1e-8,4.0/3.0,0.01),
    (1e-4,0.5,2.0),
]
rows=[]
for d,C,X in tests:
    b=gamma_bound(d,C,X)
    assert b>0
    rows.append({"delta_max":d,"C":C,"X":X,"Gamma_bound":b,"abs_g_bound_frozen":2*b})

result={
    "iteration":"008-G5",
    "lane":"conditional-bound",
    "success":True,
    "classification":"PASS_SCOPED_UNFIXED_MICROSCOPIC_NORMALIZATION_IS_DIRECTLY_BOUNDABLE_BY_ANY_FUTURE_ABSOLUTE_BROADBAND_LIMIT_WITHOUT_SETTING_G_BY_CONVENTION",
    "bound_formula":"Gamma <= sqrt(delta_max/C_prep)/abs(ell_Q^2 R_eff)",
    "frozen_convention_map":"abs(g) <= 2 Gamma when abs(c_geom)=1/2",
    "synthetic_algebra_checks":rows,
    "key_results":[
        "Leaving Gamma free does not make the leading QGR correction unfalsifiable: one absolute experimental upper limit maps directly to an upper bound on Gamma.",
        "A detection would analogously estimate Gamma, after which other specified preparations/readouts predict correlated amplitudes and parameter-free ratios.",
        "No numerical experimental bound is inserted here; the map is an algebraic prediction/identifiability relation only.",
        "The result does not identify Gamma with a Planck-scale value and does not fix g internally."
    ]
}
with open("iter008-g5-conditional-bound.json","w",encoding="utf-8") as f: json.dump(result,f,indent=2)
print(json.dumps(result,sort_keys=True))
