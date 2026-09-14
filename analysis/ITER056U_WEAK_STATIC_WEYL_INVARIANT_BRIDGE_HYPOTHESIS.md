# Iter056U hypothesis-generation note — weak-static tidal Hessian to Weyl invariants

Date: 2026-09-14
Status: `HYPOTHESIS_GENERATION_ONLY / NOT_A_TERMINAL_GATE`
Parent terminal: Iter056T `48d74f1ecc88464196ed51523eefe7134ea8bd9f`

This note records the analytic relation noticed after Iter056T. It is written before a separate prospective derivation/validation gate and is not itself counted as a scientific PASS.

## Frozen continuum metric family already used by G3 / Iter040

In the Minkowski frame with signature `(+---)`, the weak-static family has

`g_00 = 1 + 2 Phi`,

`g_0i = 0`,

`g_ij = -(1 - 2 Phi) delta_ij`,

with

`Phi(x) = (kappa/2) x^i H_ij x^j`,

where `H` is a constant real symmetric trace-free 3x3 tidal Hessian.

## Candidate linearized curvature relation

Using the standard linearized Riemann convention

`R_{rho sigma mu nu}^{(1)} = 1/2 (d_mu d_sigma h_{rho nu} + d_nu d_rho h_{sigma mu} - d_nu d_sigma h_{rho mu} - d_mu d_rho h_{sigma nu})`,

the candidate identities are

`R_{0i0j}^{(1)} = -kappa H_ij`,

`R_{0ijk}^{(1)} = 0`,

and, because `Tr(H)=0`, the linearized Ricci tensor and scalar vanish. Hence `C^{(1)}=R^{(1)}`.

Therefore the electric/magnetic Weyl parts for the static observer are expected to satisfy

`E_ij = C_{0i0j}^{(1)} = -kappa H_ij`,

`B_ij = 0`.

## Candidate invariant coefficients

Let

`I2 = Tr(H^2)`, `I3 = Tr(H^3)`.

For the Lorentz-contracted quadratic Weyl invariant

`J2 = C_abcd C^abcd`

and the cubic contraction used by the repository helper

`J3 = C_ab^{ cd} C_cd^{ ef} C_ef^{ ab}`,

the candidate leading weak-field relations are

`J2 = 8 kappa^2 I2 + O(kappa^3)`,

`J3 = 16 kappa^3 I3 + O(kappa^4)`

under the convention above.

Consequently, for nonzero `H` and positive `kappa`,

`J3 / J2^(3/2) -> (1/sqrt(2)) * I3/I2^(3/2)`

as `kappa -> 0`, and the convention-insensitive squared shape invariant obeys

`J3^2 / J2^3 -> (1/2) * I3^2/I2^3`.

## Important firewall

Iter040's diagnostic `np.linalg.norm(W)` is the Euclidean component norm of the finite-cell Weyl array. It is **not** the Lorentz-contracted invariant `J2` above. The prospective gate must not silently equate them.

Iter040's `weyl_cubic(W)` does implement the cubic contraction `J3` by raising the last index pair with the repository Minkowski metric. Its finite-h sign/orientation convention is not to be used to change the analytic coefficient after preregistration.

## Required prospective validation

A separate gate must derive these relations for a generic symmetric trace-free `H`, not only diagonal H0, and must explicitly check:

1. linearized Ricci-flatness from `Tr(H)=0`;
2. `E=-kappa H` and `B=0`;
3. the exact leading coefficients 8 and 16 under the frozen Riemann/contraction convention;
4. off-diagonal held-out Hessians as algebraic domain controls;
5. a traceful negative control showing why Ricci subtraction / trace-free tidal restriction matters;
6. an explicit statement that this is a linearized weak-static continuum result, not an exact finite-kappa theorem.

No finite-h result has been used to tune these coefficients.