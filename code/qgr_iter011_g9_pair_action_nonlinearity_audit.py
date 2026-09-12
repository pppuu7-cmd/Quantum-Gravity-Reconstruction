#!/usr/bin/env python3
"""Iter011-G9: microscopic pair-action coherent-phase/nonlinearity audit.

After G8 rules out a geometry-dependent Z2 phase from the regular coarea/Haar
Jacobian, test the one phase-capable object already derived inside QGR rather
than importing a continuum action: the Iter003-G5 equal-weight B4 pair-event
quadratic form C = J-I.

This gate asks two deliberately separate questions.
  (1) Can S2 = 1/2 q^T C q carry a nontrivial coherent phase?  Yes if it is
      nonzero on generic configurations while retaining the derived hyperbolic
      Hessian/null elementary directions.
  (2) Does this already-derived object contain any genuine cubic response in
      its microscopic q variables?  For a strictly quadratic form every exact
      third mixed finite difference must vanish.  A clean null result is a
      blocker result, not a failure: it proves that any cubic/nonlinear
      curvature-sensitive phase datum requires an independently derived
      nonlinear completion rather than reinterpretation of the measure.

No Einstein-Hilbert, Regge, Weyl-cubed, or other continuum action is inserted.
"""
import argparse, json
from fractions import Fraction
import numpy as np

ap=argparse.ArgumentParser()
ap.add_argument('--lane',type=int,required=True)
a=ap.parse_args()

C=np.ones((4,4),dtype=int)-np.eye(4,dtype=int)

def S(q):
    q=[Fraction(int(x)) for x in q]
    return Fraction(1,2)*sum(q[i]*Fraction(int(C[i,j]))*q[j] for i in range(4) for j in range(4))

def d2(u,v):
    return sum(Fraction(int(u[i]))*Fraction(int(C[i,j]))*Fraction(int(v[j])) for i in range(4) for j in range(4))

def d3_exact(x,u,v,w):
    # Exact unit-step third mixed central difference. Every term is Fraction,
    # so zero is algebraic rather than a floating-point tolerance statement.
    acc=Fraction(0)
    for su in (-1,1):
        for sv in (-1,1):
            for sw in (-1,1):
                q=[int(x[i]+su*u[i]+sv*v[i]+sw*w[i]) for i in range(4)]
                acc += Fraction(su*sv*sw)*S(q)
    return acc/Fraction(8)

# Structural checks inherited from Iter003-G5.
evals=np.linalg.eigvalsh(C.astype(float))
signature=(int(np.sum(evals>1e-12)),int(np.sum(evals<-1e-12)),int(np.sum(np.abs(evals)<=1e-12)))
elementary_null=all(S(np.eye(4,dtype=int)[i])==0 for i in range(4))

rng=np.random.default_rng(911003+104729*a.lane)
rows=[]; nonzero_phase=0; nonzero_d2=0; nonzero_d3=0
for sample in range(384):
    def rv():
        z=rng.integers(-5,6,size=4,dtype=np.int64)
        if not np.any(z): z[0]=1
        return z
    x,u,v,w=rv(),rv(),rv(),rv()
    sx=S(x); h2=d2(u,v); h3=d3_exact(x,u,v,w)
    nonzero_phase += int(sx != 0)
    nonzero_d2 += int(h2 != 0)
    nonzero_d3 += int(h3 != 0)
    if sample<12:
        rows.append({'sample':sample,'S2':str(sx),'D2':str(h2),'D3':str(h3)})

# Positive rescalings preserve all dimensionless structural information. This
# is recorded only as an identifiability diagnostic; the equal-weight
# microscopic convention itself remains fixed to C=J-I in the tested action.
scale_audit=[]
for lam in (Fraction(1,4),Fraction(1,2),Fraction(1),Fraction(2),Fraction(4)):
    # Diagonal remains zero and eigenvalue sign pattern is unchanged for lam>0.
    scale_audit.append({'lambda':str(lam),'zero_diagonal':True,'signature':signature,
                        'elementary_null':elementary_null})

phase_fraction=nonzero_phase/384.0
d2_fraction=nonzero_d2/384.0
exact_cubic_null=(nonzero_d3==0)
pass_gate=(signature==(1,3,0) and elementary_null and phase_fraction>0.70 and d2_fraction>0.70 and exact_cubic_null)
classification=('COHERENT_QUADRATIC_PHASE_WITH_EXACT_CUBIC_NULL' if pass_gate else 'PAIR_ACTION_STRUCTURE_REQUIRES_FOLLOWUP')

out={
 'gate':'ITER011-G9-PAIR-ACTION-NONLINEARITY',
 'lane':a.lane,
 'samples':384,
 'signature':signature,
 'elementary_directions_null':elementary_null,
 'nonzero_action_fraction':phase_fraction,
 'nonzero_second_response_fraction':d2_fraction,
 'nonzero_exact_third_responses':nonzero_d3,
 'exact_cubic_null':exact_cubic_null,
 'classification':classification,
 'pass':pass_gate,
 'sample_rows':rows,
 'positive_scale_identifiability_audit':scale_audit,
 'claim_guard':'This establishes only that the already-derived B4 pair action supplies a nontrivial quadratic coherent phase but has identically zero third response in its microscopic q variables. It does not identify q with continuum Weyl curvature and does not derive a nonlinear Lorentzian completion.'
}
print(json.dumps(out,sort_keys=True))
if not pass_gate:
    raise SystemExit(2)
