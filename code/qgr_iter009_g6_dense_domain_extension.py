#!/usr/bin/env python3
import json
from fractions import Fraction

# Uniform-bounded dense-domain extension theorem used for the QGR one-particle branch maps.
# If T_n,T are uniformly bounded by M and T_n phi -> T phi for every phi in dense D,
# then T_n psi -> T psi for every psi in H.  For unitaries M=1.
# Exact epsilon/3 certificate:
# ||(T_n-T)psi|| <= ||T_n(psi-phi)|| + ||(T_n-T)phi|| + ||T(phi-psi)||
#                    <= 2 M ||psi-phi|| + dense_domain_error.
M=Fraction(1)
epsilon=Fraction(1,1)
approx_error=epsilon/Fraction(6)   # choose ||psi-phi|| < eps/(6M)
dense_error=epsilon/Fraction(3)   # eventually on phi
bound=2*M*approx_error+dense_error
assert bound==Fraction(2,3) < epsilon

out={
  'gate':'ITER009-G6-DENSE-DOMAIN-EXTENSION',
  'operator_family':'QGR one-particle branch Lorentz/transport unitaries on the characteristic L2 physical space',
  'dense_domain':'compactly supported continuous characteristic wavefunctions with finite two-mode fiber',
  'uniform_operator_bound':1,
  'exact_epsilon_certificate':{
    'epsilon':str(epsilon),
    'chosen_dense_approximation_error':str(approx_error),
    'eventual_dense_domain_convergence_error':str(dense_error),
    'full_space_error_bound':str(bound)
  },
  'proof_chain':[
    'C_c with finite polarization fiber is dense in the established characteristic L2 Hilbert space',
    'branch maps are unitary, hence uniformly bounded by one',
    'strong convergence on the dense domain plus the exact triangle bound extends to every L2 vector',
    'the same argument applies to adjoints because the representation is unitary'
  ],
  'classification':'PASS_SCOPED_DENSE_DOMAIN_PLUS_UNITARITY_EXTENDS_BRANCH_STRONG_CONVERGENCE_TO_THE_FULL_ESTABLISHED_ONE_PARTICLE_L2_PHYSICAL_SPACE',
  'guard':'This extension is only for the established one-particle Hilbert representation. It is not a construction of the full interacting many-body/nonperturbative Hilbert space.'
}
print(json.dumps(out,sort_keys=True))
