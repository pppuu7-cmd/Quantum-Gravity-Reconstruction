#!/usr/bin/env python3
import json, math

# dmu(G)=|det G|^-5/2 d^10G is invariant under congruence, including G->s^2 G.
# The positive scaling subgroup is R_+ with Haar measure ds/s = dt, t=ln s.
# Therefore any invariant disintegration along a noncompact scale orbit carries
# infinite Haar volume. Symmetric cutoffs s in [e^-L,e^L] have volume 2L.

Ls=[1,2,4,8,16]
volumes=[]
for L in Ls:
    v=2.0*L
    volumes.append(v)
assert all(volumes[i+1]>volumes[i] for i in range(len(volumes)-1))

result={
    "iteration":"009-G1",
    "lane":"scale-measure",
    "success":True,
    "classification":"BLOCKED_SCOPED_CONGRUENCE_INVARIANT_Q13_MEASURE_HAS_INFINITE_NONCOMPACT_SCALE_ORBIT_VOLUME_AND_IS_NOT_A_NORMALIZED_GLOBAL_VACUUM_PROBABILITY_MEASURE",
    "scale_subgroup":"G -> s^2 G, s>0",
    "orbit_Haar_measure":"ds/s = d(log s)",
    "symmetric_cutoff_log_volumes":[{"L":L,"integral":v} for L,v in zip(Ls,volumes)],
    "key_results":[
        "The existing kinematic measure is exactly invariant under positive global scaling of G.",
        "The scale subgroup is noncompact and its invariant Haar volume is infinite in both logarithmic directions.",
        "Therefore the invariant measure is suitable as a kinematic L2 reference measure but cannot itself be normalized into a global vacuum probability distribution without additional state/dynamical data.",
        "This does not invalidate square-integrable states or the finite normalized history instrument."
    ]
}
with open("iter009-g1-scale-measure.json","w",encoding="utf-8") as f: json.dump(result,f,indent=2)
print(json.dumps(result,sort_keys=True))
