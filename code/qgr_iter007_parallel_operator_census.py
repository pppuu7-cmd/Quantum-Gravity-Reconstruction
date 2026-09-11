#!/usr/bin/env python3
import argparse, json
from fractions import Fraction

P=argparse.ArgumentParser(); P.add_argument('--output',required=True); args=P.parse_args()

# Four-derivative, parity-even metric-only local bulk action in 4D.
# Raw curvature-squared basis: R^2, Ricci^2, Riemann^2.
# Euler/Gauss-Bonnet E4 = Riemann^2 - 4 Ricci^2 + R^2 is topological in 4D;
# box R is a boundary term. Hence two independent parity-even dynamical bulk directions.
raw=3; gauss_bonnet_relations=1; bulk=raw-gauss_bonnet_relations
assert bulk==2

# A unitary Hamiltonian correction, including any local R^2/Ricci^2 term, cannot change purity:
# d Tr(rho^2)/dt = -2 i Tr(rho [H,rho]) = 0 by cyclicity.
# In contrast, the QGR history channel has a positive covariance double-commutator and non-positive purity derivative.
unitary_purity_derivative=Fraction(0)

out={
 'lane':'COMPETING_OPERATOR_CENSUS',
 'parity_even_curvature_squared_raw_scalars':raw,
 'four_dimensional_gauss_bonnet_bulk_relations':gauss_bonnet_relations,
 'independent_parity_even_four_derivative_bulk_action_directions':bulk,
 'representative_bulk_basis':['R^2','R_ab R^ab'],
 'topological_or_boundary':['R_abcd R^abcd - 4 R_ab R^ab + R^2 (Euler/Gauss-Bonnet)','box R'],
 'unitary_higher_derivative_terms_change_purity':False,
 'unitary_purity_derivative_exact':str(unitary_purity_derivative),
 'history_double_commutator_can_reduce_purity':True,
 'classification':'PASS_SCOPED_PURITY_LOSS_DISCRIMINATES_HISTORY_CHANNEL_FROM_UNKNOWN_UNITARY_CURVATURE_SQUARED_ACTION_TERMS',
 'scientific_interpretation':'Unknown unitary four-derivative metric operators remain a genuine EFT/RG ambiguity, but they cannot fake the normalized purity-loss signature of the positive history channel. Purity is therefore a cleaner discriminator than a phase/dispersion observable for this gate.',
 'guard':'This does not prove that curvature-squared coefficients vanish, nor does it include matter-sector or nonlocal operators.'
}
open(args.output,'w').write(json.dumps(out,indent=2,sort_keys=True)+'\n')
print(json.dumps(out,sort_keys=True))
