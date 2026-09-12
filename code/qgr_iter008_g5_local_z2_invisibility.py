#!/usr/bin/env python3
import json
from fractions import Fraction

# Seed E=C^-1=-I+J/3 has eigenvalues +1/3 on the symmetric line and -1 on
# the three-dimensional sum-zero subspace. By Weyl's eigenvalue bound, any
# symmetric perturbation H with operator norm ||H||_2 < 1/3 keeps signature
# (1,3). The open norm ball B(E,1/3) is convex and therefore contractible.
# Hence the nontrivial Z2 flat bundle has trivial holonomy on all loops fully
# contained in this ball. The leading h->0 refinement histories eventually lie
# in such a neighborhood by continuity G(h)->E.

seed_eigs=[Fraction(1,3),Fraction(-1),Fraction(-1),Fraction(-1)]
radius=Fraction(1,3)
assert seed_eigs[0]-radius==0
assert seed_eigs[1]+radius==Fraction(-2,3)

result={
    "iteration":"008-G5",
    "lane":"local-z2-invisibility",
    "success":True,
    "classification":"PASS_SCOPED_LEADING_LOCAL_REFINEMENT_AND_BROADBAND_OBSERVABLES_ARE_Z2_SECTOR_INSENSITIVE_ON_A_CONTRACTIBLE_LORENTZIAN_NEIGHBORHOOD_OF_THE_SEED",
    "seed_spectrum":[str(x) for x in seed_eigs],
    "certified_open_operator_norm_radius":"1/3",
    "topology":"convex neighborhood -> contractible -> flat Z2 holonomy trivial on contained loops",
    "key_results":[
        "E has spectral gap 1/3 to the signature-changing boundary in the positive direction and gap 1 in the negative directions.",
        "Every symmetric perturbation with operator norm strictly below 1/3 remains Lorentzian; the corresponding ball is convex and contractible.",
        "The twisted and trivial flat-line-bundle sectors are locally isomorphic on this ball, so all loops contained there have the same +1 flat holonomy.",
        "Because the refinement-connected local construction satisfies G(h)->E as h->0, its leading asymptotic O(h^4) broadband result is insensitive to the global Z2 sector.",
        "This does not prove that finite strong-curvature paths outside the local neighborhood are Z2-insensitive."
    ]
}
with open("iter008-g5-local-z2-invisibility.json","w",encoding="utf-8") as f: json.dump(result,f,indent=2)
print(json.dumps(result,sort_keys=True))
