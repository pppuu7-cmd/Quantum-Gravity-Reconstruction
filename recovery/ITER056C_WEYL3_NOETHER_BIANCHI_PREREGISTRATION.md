# Iter056C preregistration — Weyl3 Noether/Bianchi compatibility in the formal perturbative sector

Date: 2026-09-14
Gate: `ITER056C-WEYL3-NOETHER-BIANCHI-FIRST-ORDER-COMPATIBILITY`

## Frozen question
For the prospective formal perturbative architecture of Iter056B, is the first Weyl3 correction source automatically compatible with the lower-order linearized diffeomorphism/Bianchi constraint at the covariant action level, without requiring a component-expanded Weyl3 Euler-Lagrange tensor?

This is a necessary consistency test for a future versioned perturbative candidate, not historical QGR treatment authority.

## Frozen source object
Take the covariant local correction action

`S1[g] = integral d^4x sqrt(|g|) I3[g]`,

where `I3[g]` is the already-established scalar Weyl-cubic invariant used by QGR. Define its metric Euler-Lagrange tensor `E1^{mu nu}` by the variational identity, assuming compactly supported variations / boundary conditions sufficient to drop the boundary term.

Take a lower-order background `g0` satisfying the metric-only lower-order equation `E0[g0]=0`. Let `L0=D E0[g0]` be the linearized lower-order operator.

## Frozen obligations
1. Use infinitesimal diffeomorphism invariance of `S1` to derive the off-shell Noether identity `nabla_mu E1^{mu nu}=0` up to the fixed index/sign convention.
2. Differentiate the lower-order Noether/Bianchi identity and use `E0[g0]=0` to derive the corresponding background divergence identity for `L0 h`.
3. Show that the first formal correction equation from Iter056B,
   `L0 g1 = -E1[g0]`,
   satisfies the necessary divergence/constraint compatibility condition identically.
4. Do not infer existence/uniqueness of `g1`, gauge fixing, hyperbolicity, positivity, or global boundary solvability from source conservation alone.
5. If the identity needs matter or boundary terms outside the frozen metric-only compact-support scope, state the limitation rather than importing extra physics.
6. No component expression for `E1` may be invented post hoc; the gate is action/Noether level only.

## Frozen classifications
- `PASS_SCOPED_ITER056C_WEYL3_FIRST_ORDER_SOURCE_IS_NOETHER_CONSERVED_AND_LINEARIZED_BIANCHI_COMPATIBLE__SOLVABILITY_NOT_ESTABLISHED` if the two identities imply the compatibility condition.
- `FAIL_SCOPED_ITER056C_WEYL3_FIRST_ORDER_SOURCE_VIOLATES_LOWER_ORDER_BIANCHI_COMPATIBILITY` if the covariant action source is not divergence-compatible on a lower-order background.
- `INVALID_ITER056C_COVARIANT_ACTION_VARIATION_OBJECT_NOT_DEFINED_ENOUGH_FOR_NOETHER_IDENTITY` only if the existing Weyl3 scalar-action object cannot support the variational/Noether statement even formally.

## Interpretation ceiling
A PASS closes one necessary formal constraint-consistency obligation only. It does not authorize perturbative treatment physically for QGR, provide the full component Weyl3 EOM, fix gauge/constraints, establish a solution, convergence/remainder control, hyperbolicity, unitarity, UV completion, regulator removal, GR recovery, experiment or theory establishment.

No GitHub Actions run is preregistered; this is exact covariant variational analysis.
