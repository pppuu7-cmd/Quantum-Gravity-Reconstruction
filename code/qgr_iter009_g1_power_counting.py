#!/usr/bin/env python3
import json

# Generic continuum power counting for connected diagrams built from
# two-derivative gravity vertices and 1/p^2 propagators in D=4:
# omega = 4L + 2V - 2I.
# With L=I-V+1 this reduces exactly to omega=2L+2.
# This is only superficial power counting; it does not assert a nonzero
# divergence after gauge identities/on-shell cancellations.

samples=[(2,2),(2,3),(3,5),(4,7)] # (V,I)
rows=[]
for V,I in samples:
    L=I-V+1
    omega=4*L+2*V-2*I
    formula=2*L+2
    assert omega==formula
    rows.append({"V":V,"I":I,"L":L,"omega":omega})

result={
    "iteration":"009-G1",
    "lane":"power-counting",
    "success":True,
    "classification":"BLOCKED_SCOPED_CONTINUUM_TWO_DERIVATIVE_GRAVITY_POWER_COUNTING_ALLOWS_PROGRESSIVELY_HIGHER_DERIVATIVE_COUNTERTERM_ORDERS__MICROSCOPIC_QGR_MUST_CONTROL_THEIR_COEFFICIENTS_OR_SUPPRESSION",
    "formula":"omega=4L+2V-2I=2L+2",
    "sample_graphs":rows,
    "key_results":[
        "At loop order L, generic superficial momentum degree is 2L+2 for two-derivative gravity vertices in four dimensions.",
        "Thus symmetry plus the two-derivative action does not by itself restrict the quantum effective action to two derivatives.",
        "At one loop the allowed order is four derivatives; at two loops it is six derivatives, before any special cancellations are considered.",
        "This is a power-counting allowance only, not evidence that a particular counterterm coefficient is nonzero. QGR refinement dynamics must decide the actual coefficients."
    ]
}
with open("iter009-g1-power-counting.json","w",encoding="utf-8") as f: json.dump(result,f,indent=2)
print(json.dumps(result,sort_keys=True))
