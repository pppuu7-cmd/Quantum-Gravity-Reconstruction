# Iter057AP target-blind constructor defect — algebraic curvature derivative P projector

Date: 2026-09-17
Preregistration: `6de62a559381a7c86e01c58a62ea7d8c91606884`
Constructor run: `35176036834`
Artifact: `10478348850`, digest `sha256:6b85bbcbe2bd4ec640d9fad5e3222b8e20b47e71780e377a6e0e9ccd09a1dcb3`
Invalid constructor payload SHA256: `7c4fd5f62b80fa19275be83ade31ed98cd53aec8db768a8d83bdeebd3f777cc9`

No Iter057U/X target coefficient was opened or compared. After the previously documented correction of the cubic invariant, the target-blind controls now give `I3(0)/kappa^3=96` exactly, proving the AO cubic convention is restored. However the hand-written closed-form projection used to construct `P=dI3/dR` fails its own source-level controls: pair exchange, algebraic Bianchi, the nontrivial Frechet-direction equality and `P.R=3 I3`.

This identifies the projector implementation as invalid before any terminal source comparison. The failure is not scientific evidence against AO or Iter057X.

## Prospectively frozen repair

Replace only the hand-written `p_from_frechet_projection` helper by a direct exact reconstruction from the defining Frechet relation on the 20-dimensional vector space of algebraic Riemann tensors in four dimensions.

Use the fixed bivector order

`[(01),(02),(03),(12),(13),(23)]`.

Represent an algebraic Riemann tensor as a symmetric `6x6` bivector matrix `S`. Freeze the first-Bianchi relation in this convention as

`S[0,5] - S[1,4] + S[2,3] = 0`.

The basis is the lexicographically ordered set of the 21 upper-triangular symmetric matrix entries with `(2,3)` omitted; for each basis element enforce `S[2,3]=-S[0,5]+S[1,4]`. This gives exactly 20 fixed basis tensors `B_i`.

For each `B_i`, construct directly at fixed metric

- `delta Ricci`,
- `delta R`,
- `delta C_abcd`,
- `delta C_ab^{ cd}`,
- `dI3_i = 3 delta C_ab^{ cd} C_cd^{ ef} C_ef^{ ab}`

using the already corrected AO cubic convention.

Form the exact constant Gram matrix

`G_ij = sum_abcd B_i,abcd B_j,abcd`.

Its basis definition is fixed above; no target data enter. Solve exactly over rationals

`G c = dI3`

and set

`P^{abcd} = sum_i c_i B_i^{abcd}`.

This construction enforces the algebraic Riemann symmetries by construction and realizes the defining Frechet relation rather than assuming a closed-form projector. The same pre-existing target-blind controls (`P` antisymmetries, pair exchange, Bianchi, nonzero Frechet direction, exact Frechet equality, `P.R=3I3`) must all pass before a source payload can be frozen. No U/X comparator may be created before that happens.
