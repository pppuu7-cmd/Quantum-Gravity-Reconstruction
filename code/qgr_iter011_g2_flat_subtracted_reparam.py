#!/usr/bin/env python3
import json,numpy as np
rng=np.random.default_rng(1102)
# Use nonsingular square constraint Jacobians as an algebraic coarea test.
Q,_=np.linalg.qr(rng.normal(size=(8,8)))
J0=Q@np.diag(np.linspace(0.7,2.1,8))
J1=J0+0.03*rng.normal(size=(8,8))
A=np.eye(8)+0.07*rng.normal(size=(8,8))
B=np.eye(8)+0.06*rng.normal(size=(8,8))
for X in (J0,J1,A,B): assert abs(np.linalg.det(X))>1e-4

def ld(X): return float(np.linalg.slogdet(X)[1])
delta=ld(J1)-ld(J0)
# T'=A T, omega'=B omega => J'=A J B^{-1}.
Bi=np.linalg.inv(B)
J0p=A@J0@Bi;J1p=A@J1@Bi
deltap=ld(J1p)-ld(J0p)
err=abs(delta-deltap)
assert err<2e-12,(delta,deltap,err)
out={
 'gate':'ITER011-G2-FLAT-SUBTRACTED-JACOBIAN-REPARAMETRIZATION',
 'delta_logdet_original':delta,
 'delta_logdet_after_constant_constraint_and_connection_coordinate_change':deltap,
 'absolute_error':err,
 'classification':'PASS_SCOPED_FLAT_SUBTRACTED_LOG_TORSION_JACOBIAN_IS_INVARIANT_UNDER_CURVATURE_INDEPENDENT_LINEAR_REPARAMETRIZATIONS_OF_CONSTRAINT_AND_CONNECTION_COORDINATES',
 'interpretation':'Constant determinant factors cancel between curved and flat reference Jacobians. Therefore a scoped curvature coefficient extracted from Delta log|det J| is not an artifact of a constant basis normalization.',
 'guard':'Curvature-dependent coordinate changes require the associated Haar/configuration measure Jacobians and are not covered by this cancellation identity.'
}
print(json.dumps(out,sort_keys=True))
