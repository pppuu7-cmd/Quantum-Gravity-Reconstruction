# Iter057AO phase-2 execution-only repair — covariant Iyer-Wald compression

Status: **PROSPECTIVELY FROZEN BEFORE PHASE-1 OR HELD-OUT OUTCOME CONSUMPTION**
Parent scientific preregistration: `e1ded07e5050763ecb707dad679b78286fe04744`
Prior phase-2 implementation freeze: `0daf8a632c060c0f758f15bd43b4837633a48efa`

## Reason for execution repair

A local implementation diagnostic of the already-frozen mechanical coordinate-density IBP algorithm attempted to extract the complete 150-component `(h, partial h, partial^2 h)` coefficient family by repeated exact rational two-jet propagation. The computation exceeded the diagnostic resource envelope before producing any scientific/held-out outcome. No coefficient, control result, phase-1 artifact, or held-out result was inspected.

This is an execution/expression-growth issue, not a scientific result. The frozen functional, seeds, tensor conventions, exact controls and terminal classifier are unchanged.

## Algebraically equivalent compressed route

For any scalar `f(g,Riemann)` with no derivatives of Riemann, define the exact algebraic curvature derivative `P^{abcd}` by the Frechet identity on the space of algebraic Riemann variations `K_{abcd}` at fixed metric:

`P^{abcd} K_{abcd} = d/ds f(g,R+s K)|_{s=0}`.

For AO, `f=I3=C_ab{}^{cd} C_cd{}^{ef} C_ef{}^{ab}` and the right hand side is constructed source-faithfully by varying the frozen Weyl definition and all index raising at fixed metric. This definition is canonical and does not import AF/AM/AN data.

Under the conventions frozen in `0daf8a...`, use the exact standard metric-variation identity

`delta [sqrt(-g) f] = sqrt(-g) [ E_cov^{ab} h_ab + nabla_mu Theta^mu ]`

for covariant metric variation `h_ab=delta g_ab`, with

`E_cov^{ab} = - P^{a c d e} R^b{}_{c d e} + 2 nabla_c nabla_d P^{a c d b} + (1/2) g^{ab} f`,

and

`Theta^mu = 2 P^{mu b c d} nabla_d h_bc - 2 (nabla_d P^{mu b c d}) h_bc`.

The sign convention is fixed by the Einstein-Hilbert control: for `f=R`, `P_EH^{abcd}=1/2(g^{ac}g^{bd}-g^{ad}g^{bc})`, the bulk coefficient multiplying covariant `h_ab` must reduce exactly to `-G^{ab}`, and `Theta^mu` must reduce to `nabla_nu h^{mu nu}-nabla^mu h`.

This compact covariant formula is the persisted Euler-Lagrange/boundary representation. It is not a symmetry reduction and does not drop the divergence.

## Required machine checks under this repair

1. Independently coded analytic raw directional variation on the generic seed, including inverse-metric, determinant, curvature, Weyl and raised-index variations.
2. Exact equality of the analytic generic directional density with the independent direct `g+eps h` phase-1 result after convention/canonicalization reconciliation.
3. Exact base and first-variation Weyl algebraic/trace controls.
4. Exact constant-curvature and nonconstant conformally-flat zero controls frozen in `0daf8a...`.
5. Exact Noether control using `h=L_xi g`: direct raw analytic variation must equal `partial_mu(xi^mu sqrt(-g) I3)` on the frozen formal rational jet. The structural identity is also recorded generally because `sqrt(-g) I3` is a scalar density.
6. Einstein-Hilbert sign/boundary control for the compact covariant variation identity.
7. Held-out analytic evaluation only after this repair and its implementation are frozen.
8. Independent adversarial Critic verifies that the compact formula and raw analytic constructor use the same frozen curvature/Weyl conventions and that no AF/AM/AN target enters acceptance.

## Noether consequence

For `h_ab=nabla_a xi_b+nabla_b xi_a`, scalar-density covariance gives exactly

`delta_xi[sqrt(-g)f]=partial_mu[xi^mu sqrt(-g)f]`.

Combining this with the compact bulk+boundary identity yields the off-shell Noether identity `nabla_a E_cov^{ab}=0` for the frozen covariant Euler representative. The machine direct-Lie-derivative control is required to detect implementation/index errors; the structural identity supplies the all-jet integration-by-parts certificate rather than a finite numerical fit.

## Classifier unchanged

The AO terminal PASS/FAIL/BLOCKED/INVALID criteria remain exactly those in `e1ded07e...`. This execution repair does not authorize a terminal PASS unless every original frozen obligation is met. `c6` stays symbolic/unfixed; `beta=1` remains unauthorized.