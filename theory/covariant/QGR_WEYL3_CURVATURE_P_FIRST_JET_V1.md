# QGR Weyl3 curvature P and first jet v1

Preregistration: `d081640ffed1122d314c835ac54fca3277ef1de9`.

This note defines an abstract covariant object only. It does not inspect or fit any historical residual.

Let `A_g` be the vector space of algebraic Riemann tensors at a point with the metric-induced contraction pairing `<.,.>`. Let `W_g` be its Weyl subspace and `Pi_g:A_g->W_g` the standard trace-removing Weyl projection. Write `Pi_g^*` for the adjoint under the same pairing. Let

`C = Pi_g[R]`,
`I3 = C_ab{}^cd C_cd{}^ef C_ef{}^ab`,
`L6 = c6 I3`, with `c6=SYMBOLIC_UNFIXED`.

Treating a Weyl tensor as an endomorphism of antisymmetric index pairs, define `C o C` by the same middle-pair contraction appearing in `I3`. For every algebraic-Riemann variation `delta R`, linearity gives `delta C=Pi_g[delta R]` at fixed metric in the curvature derivative. Cyclicity of the complete cubic contraction gives

`delta I3 = 3 <C o C, delta C> = 3 <Pi_g^*[C o C], delta R>`.

Therefore the curvature derivative is defined convention-independently by

`P_R := d L6 / d R = 3 c6 Pi_g^*[C o C]`,

where the equality means `delta L6=<P_R,delta R>` for every algebraic-Riemann variation. This Frechet definition fixes any component factor associated with antisymmetric-pair coordinates.

For the Levi-Civita connection, `nabla g=0`. Since `Pi_g` and its adjoint are built algebraically only from `g`, `g^{-1}` and dimension-dependent numerical coefficients, `nabla Pi_g=0` and `nabla Pi_g^*=0`. Hence

`nabla_e P_R = 3 c6 Pi_g^*[(nabla_e C) o C + C o (nabla_e C)]`.

No commutativity of `o` is used.

## Intrinsic controls

1. Algebraic symmetries: PASS by the codomain of `Pi_g^*` on the Weyl subspace; P_R has pair antisymmetry and pair exchange symmetry.
2. Trace-free projected slots: PASS because `Pi_g^*` maps through the Weyl projection under the contraction pairing.
3. Euler homogeneity: PASS. Since `Pi_g[R]=C`, `<P_R,R>=3 c6 <C o C,C>=3 c6 I3=3 L6`.
4. Jet degree/product rule: PASS. `nabla P_R` is linear in `nabla C` and linear in the second C factor, hence curvature-times-curvature-jet, as required for the derivative of a curvature-quadratic P.
5. Symbolic coefficient: PASS; c6 is never fixed or run.
6. Target blindness: PASS by construction of this source from the preregistered abstract invariant only; no historical residual is referenced.

## Scope

Classification: `PASS_SCOPED_CURVATURE_WEYL3_P_AND_FIRST_JET_DEFINED`.

This closes only the missing object-definition blocker at the abstract covariant tensor-map level. It does not establish that the historical generic-P residual is repaired, does not supply the complete metric Euler-Lagrange tensor, and does not establish a global theorem, physical quantum measure, unitarity, UV completion, or experimental confirmation. Any residual comparison requires a new prospective preregistration.