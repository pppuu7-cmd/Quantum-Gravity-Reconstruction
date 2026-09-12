#!/usr/bin/env python3
import json, math

# Explicit generator of pi1(Q_13)~=pi1(RP3)=Z2.
# Let v(s)=(cos(pi s), sin(pi s),0,0), s in [0,1].
# Define G(s)=2 v v^T-I. It has eigenvalue +1 along v and -1 orthogonal.
# v(1)=-v(0), so the positive line closes while its S3 lift changes sign:
# this is the nontrivial RP3 loop. G(1)=G(0).

def G_of(s):
    v=[math.cos(math.pi*s),math.sin(math.pi*s),0.0,0.0]
    return [[2*v[i]*v[j]-(1.0 if i==j else 0.0) for j in range(4)] for i in range(4)]

G0=G_of(0.0); G1=G_of(1.0)
max_close=max(abs(G0[i][j]-G1[i][j]) for i in range(4) for j in range(4))
assert max_close<1e-12

# Check G^2=I on sample points -> eigenvalues are +/-1; trace=-2 gives one + and three -.
for s in [0,0.125,0.25,0.5,0.75,1.0]:
    G=G_of(s)
    G2=[[sum(G[i][k]*G[k][j] for k in range(4)) for j in range(4)] for i in range(4)]
    assert max(abs(G2[i][j]-(1.0 if i==j else 0.0)) for i in range(4) for j in range(4))<1e-10
    assert abs(sum(G[i][i] for i in range(4))+2.0)<1e-10

result={
    "iteration":"008-G5",
    "lane":"global-z2-loop",
    "success":True,
    "classification":"PASS_SCOPED_EXPLICIT_NONCONTRACTIBLE_Q13_LOOP_DISTINGUISHES_THE_TWO_FLAT_QUANTUM_SECTORS_BY_A_GLOBAL_SIGN_HOLONOMY",
    "loop":"v(s)=(cos(pi s),sin(pi s),0,0); G(s)=2 vv^T-I",
    "endpoint_metric_closure_error":max_close,
    "positive_line_lift":"v(0)=e0 -> v(1)=-e0",
    "flat_sector_holonomies":{"trivial":"+1","twisted":"-1"},
    "key_results":[
        "The loop stays in signature (1,3), closes exactly in metric configuration space, and lifts to an open path from e0 to -e0 on the S3 double cover.",
        "It therefore represents the nontrivial generator of pi1(Q_13)=Z2.",
        "A globally coherent configuration-space interference process winding this loop acquires relative flat holonomy +1 in the trivial sector and -1 in the twisted sector.",
        "This supplies a sharp global discriminator between sectors, but the current local/refinement broadband observable does not wind this loop and cannot select the sector."
    ]
}
with open("iter008-g5-global-z2-loop.json","w",encoding="utf-8") as f: json.dump(result,f,indent=2)
print(json.dumps(result,sort_keys=True))
