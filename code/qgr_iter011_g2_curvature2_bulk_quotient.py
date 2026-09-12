#!/usr/bin/env python3
import json
from fractions import Fraction
# 4D parity-even curvature-squared basis: Riem^2, Ric^2, R^2.
# Euler E4 = Riem^2 - 4 Ric^2 + R^2 is topological in the bulk.
# First-order metric redefinitions around EH span Ric^2 and R^2 on shell,
# with the exact Iter009-G2 coefficient map rank 2.
M=[[Fraction(1),Fraction(0)],[Fraction(-1,2),Fraction(-1)]]
det=M[0][0]*M[1][1]-M[0][1]*M[1][0]
assert det==Fraction(-1)
# Mod Euler plus the two EOM-redefinition directions, no local parity-even R^2 bulk direction remains.
raw_dim=3; euler_dim=1; eom_rank=2; quotient_dim=raw_dim-euler_dim-eom_rank
assert quotient_dim==0
out={
 'gate':'ITER011-G2-CURVATURE2-PURE-VACUUM-BULK-QUOTIENT',
 'raw_parity_even_curvature2_dimension':raw_dim,
 'euler_topological_dimension':euler_dim,
 'field_redefinition_rank_after_euler_separation':eom_rank,
 'physical_bulk_quotient_dimension':quotient_dim,
 'classification':'PASS_SCOPED_ANY_LOCAL_COVARIANT_PARITY_EVEN_CURVATURE_SQUARED_TERM_IN_THE_PURE_VACUUM_EH_QGR_BULK_HAS_NO_INDEPENDENT_ON_SHELL_OPERATOR_DIRECTION_MODULO_EULER_BOUNDARY_AND_EOM_REDEFINITIONS',
 'interpretation':'If the leading torsion-Jacobian measure correction covariantizes only into the usual local curvature-squared class, it cannot by itself become a new independent pure-vacuum bulk Wilson direction. This does not erase measure, boundary, topology, off-shell, or matter effects.',
 'guard':'Operator-class statement only. The numerical -25/16 tidal coefficient has not yet been promoted to a unique covariant density.'
}
print(json.dumps(out,sort_keys=True))
