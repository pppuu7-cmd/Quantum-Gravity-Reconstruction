#!/usr/bin/env python3
import json

# Petrov-D / purely electric algebraic Weyl representative.
# The electric Weyl block is symmetric traceless with eigenvalues (-2q,q,q).
# Its cubic trace is nonzero, so the parity-even Weyl^3 invariant is not an identity-zero
# on the Ricci-flat algebraic curvature sector.
q = 1
lam = [-2*q, q, q]
tr1 = sum(lam)
tr3 = sum(x**3 for x in lam)
assert tr1 == 0
assert tr3 == -6
parity_even_pair = 2*tr3  # equal real chiral blocks for a purely electric representative
assert parity_even_pair != 0

out = {
    "gate": "ITER009-G3-NONZERO-WEYL-CUBIC-WITNESS",
    "weyl_block_eigenvalues": lam,
    "trace": tr1,
    "trace_cube": tr3,
    "parity_even_chiral_sum": parity_even_pair,
    "classification": "PASS_SCOPED_WEYL_CUBED_PARITY_EVEN_CLASS_HAS_A_NONZERO_RICCI_FLAT_PETROV_D_ALGEBRAIC_WITNESS",
    "guard": "This establishes nontriviality of the operator class, not its QGR coefficient or a specific spacetime solution normalization."
}
print(json.dumps(out, sort_keys=True))
