# Iter057J integrability reduction — first nontrivial open-neighborhood obstruction

Date: 2026-09-15
Gate: `ITER057J-OPEN-NEIGHBORHOOD-FIRST-ORDER-BACKGROUND-CONTINUATION`
Prospective preregistration: `0f4d3cf9e1482029382dd158aa8feef89a8d736a`

## Scope

This note does not terminalize Iter057J. It reduces the frozen Hessian-integrability test to the first nontrivial source-owned covariant jet that must be evaluated next. No value/sign of `c6` is chosen and no new geometry is introduced.

## 1. Frozen equation

Let

`S_ab = -E_W3_ab[g0]/A_E`, `S=g0^{ab}S_ab`,

and

`H_ab = g0_ab S/6 - S_ab/2`.

The conformal continuation candidate requires a scalar `psi` satisfying

`nabla_a nabla_b psi = H_ab`

on an open neighborhood.

The exact commutator condition is

`C_cab := nabla_c H_ab - nabla_a H_cb = R_ca b{}^d v_d`,

where `v_d := nabla_d psi` must simultaneously obey

`nabla_a v_b = H_ab`.

Thus the continuation problem is a closed first-order prolongation system for `(psi,v_a)` with source-owned coefficients `(H,R)`.

## 2. Noether compatibility is necessary but not sufficient

Iter056X gives the off-shell identity `nabla^a E_W3_ab=0`; hence `nabla^a S_ab=0` on the Ricci-flat G3 source. The linearized Einstein operator also obeys the corresponding linearized Bianchi identity. Therefore there is no independent divergence/constraint obstruction at this order.

This does not prove existence of a conformal scalar: the Hessian system is overdetermined and its curl/prolongation conditions remain stronger than source conservation.

## 3. Frozen-origin first curl vanishes automatically

The source-owned G3/H0 metric is exactly even under spatial inversion `y -> -y`. Consequently all covariantly constructed tensors `R`, `C`, `P`, `E_W3`, `S`, and `H` are even, while their first spatial covariant derivatives vanish at the origin. The background is static, so time derivatives vanish as well. Therefore

`nabla_c H_ab(0)=0`

and hence

`C_cab(0)=0`.

The Iter057I representative fixes `v_d(0)=nabla_d psi(0)=0`, so the right-hand side `R_ca b{}^d v_d` also vanishes. Thus the zeroth prolongation/curl condition is exactly satisfied at the frozen origin. A pointwise curl test cannot decide Iter057J.

## 4. First nontrivial prolongation condition

Differentiate the exact curl identity and evaluate at the origin. Because `v(0)=0` and `nabla R(0)=0`, while `nabla_e v_d(0)=H_ed(0)`, the first nontrivial necessary condition is

`K_ecab := [nabla_e nabla_c H_ab - nabla_e nabla_a H_cb]_0 - R_ca b{}^d(0) H_ed(0) = 0`.

This is the smallest source-owned open-neighborhood obstruction not already killed by inversion symmetry.

Every object in `K_ecab` is fixed by existing authority:

- the exact analytic G3/H0 metric `g00=1+2 Phi`, `gij=-(1-2 Phi)delta_ij` with quadratic `Phi`;
- the covariant Iter056X Euler tensor `E_W3`;
- `H` algebraically from `E_W3` and finite symbolic `A_E`;
- covariant derivatives generated from the same metric.

No third symmetry reduction or new background primitive is required.

## 5. Next computation lock

The next executable task is to evaluate the full independent component set of `K_ecab` exactly (prefer rational/symbolic `kappa`, with the common overall `1/A_E` factored out), and independently verify tensor symmetries and coordinate/basis consistency. A single exact nonzero component is sufficient for the preregistered scientific FAIL of the conformal candidate. A zero result is not yet a PASS: higher prolongations or an explicit local scalar construction would still be required by the preregistration.

No empirical tolerance may replace an exact-zero decision unless a prospectively frozen numerical cross-check is added only after the symbolic target is fixed.

## Claim locks

Theory established remains 0%; no experimental confirmation; `beta=1` unauthorized; `c6` symbolic/unfixed; no physical Weyl3 treatment selector; no strong-hyperbolicity, ghost, stability, unitarity, regulator-removal, UV-completion, or KMQGB `NEW_REQUIRED` claim.
