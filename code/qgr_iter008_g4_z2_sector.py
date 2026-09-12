#!/usr/bin/env python3
import json

# Q_{1,3} ~ RP^3 and pi_1(RP^3)=Z2.
# Flat U(1) line bundles are classified by Hom(Z2,U(1)).
# If z is the nontrivial generator, z^2=e requires rho(z)^2=1,
# so rho(z)=+1 or -1: exactly two characters.

characters=[1,-1]
assert all(x*x==1 for x in characters)
assert len(set(characters))==2

# Aut(Z2) is trivial, so any homeomorphism-induced automorphism preserves
# the nontrivial element and hence preserves both character labels.
aut_z2_count=1

result={
    "iteration":"008-G4",
    "lane":"z2-sector",
    "success":True,
    "classification":"PARTIAL_SCOPED_Q13_ADMITS_TWO_FLAT_U1_LINE_BUNDLE_QUANTIZATION_SECTORS__CURRENT_SCALAR_L2_CONSTRUCTION_IS_THE_TRIVIAL_SECTOR_AND_NO_EXISTING_QGR_RULE_SELECTS_IT_UNIQUELY",
    "configuration_space":"Q_{1,3} ~ RP^3",
    "fundamental_group":"Z2",
    "flat_U1_characters":{"trivial":"+1","twisted":"-1"},
    "number_of_flat_sectors":2,
    "Aut_Z2_size":aut_z2_count,
    "key_results":[
        "The residual Z2 topology found in G3 is not empty: it gives exactly two flat U(1) line-bundle sectors, with holonomy +1 or -1 around the noncontractible loop.",
        "The existing H_kin=L^2(Q_13,dmu) construction uses ordinary scalar functions and therefore realizes the trivial + sector.",
        "The twisted sector is locally indistinguishable from the trivial one on contractible patches, so all local QGR-L1 dynamics can coexist with it.",
        "Because Aut(Z2) is trivial, covariance of configuration-space maps does not exchange or eliminate the two sectors; no current same-realization rule uniquely selects the trivial sector.",
        "This is a discrete global quantization ambiguity, not a quantization of the positive real coupling g."
    ]
}
with open("iter008-g4-z2-sector.json","w",encoding="utf-8") as f: json.dump(result,f,indent=2)
print(json.dumps(result,sort_keys=True))
