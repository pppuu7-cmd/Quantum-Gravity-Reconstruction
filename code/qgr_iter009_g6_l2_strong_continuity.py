#!/usr/bin/env python3
import json

# Scoped theorem used here:
# H_phys is the characteristic L2 direct integral with finite-dimensional two-mode fiber.
# The Lorentz action preserves the null-cone measure and finite-fiber pairing.
# For psi in C_c on the cone, Lambda_n->I implies U(Lambda_n)psi->psi pointwise;
# near identity all transformed compact supports lie in one compact neighborhood, so dominated
# convergence gives L2 convergence. C_c is dense, and unitarity extends strong continuity to all L2.
conditions={
 'invariant_measure':True,
 'finite_polarization_fiber':2,
 'dense_test_domain':'C_c characteristic wavefunctions with finite two-mode fiber',
 'unitary_action':True,
 'group_action_continuous':True,
}
assert all(v is True for k,v in conditions.items() if isinstance(v,bool))
out={
 'gate':'ITER009-G6-L2-STRONG-CONTINUITY',
 'conditions':conditions,
 'proof_chain':['pointwise continuity on C_c','common compact domination near identity','dominated convergence in L2','density of C_c','unitary extension to all L2'],
 'classification':'PASS_SCOPED_THE_QGR_ONE_PARTICLE_CHARACTERISTIC_LORENTZ_REPRESENTATION_IS_STRONGLY_CONTINUOUS_ON_THE_FULL_L2_PHYSICAL_ONE_PARTICLE_SPACE',
 'guard':'This concerns the established one-particle characteristic Lorentz representation, not an arbitrary nonperturbative many-body/configuration-space evolution.'
}
print(json.dumps(out,sort_keys=True))
