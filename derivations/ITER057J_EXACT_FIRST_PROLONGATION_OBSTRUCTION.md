# Iter057J exact first-prolongation obstruction

Date: 2026-09-15
Gate: `ITER057J-OPEN-NEIGHBORHOOD-FIRST-ORDER-BACKGROUND-CONTINUATION`
Prospective preregistration: `0f4d3cf9e1482029382dd158aa8feef89a8d736a`
Reduction authority: `5e1775dd83da8b952ea0463bfef946eb7692f632`

## Scope

Evaluate the preregistered first nontrivial Hessian-prolongation tensor

`K_ecab = [nabla_e nabla_c H_ab - nabla_e nabla_a H_cb]_0 - R_ca b{}^d(0) H_ed(0)`

on the source-owned G3/H0 metric. A single exact nonzero component is sufficient for the preregistered scientific FAIL of the conformal open-neighborhood continuation candidate. No value or sign of `c6` is chosen.

Factor out the finite nonzero Einstein normalization and define

`Hbar_ab := A_E H_ab`.

Using `S_ab=-E_W3_ab/A_E` and `H_ab=g_ab S/6-S_ab/2`,

`Hbar_ab = (1/2) E_W3_ab - (1/6) g_ab E_W3`,

where `E_W3=g^{ab}E_W3_ab`. Therefore exact zero/nonzero of `K` is equivalent to exact zero/nonzero of `Kbar=A_E K`.

## 1. Source and conventions

Use the exact G3/H0 source metric from Iter057D,

`Phi=(kappa/2)(x^2+y^2-2 z^2)`,

`g_00=1+2 Phi`, `g_ij=-(1-2 Phi) delta_ij`, `g_0i=0`.

The equivalent global-sign convention used by the Iter057F production code, `(-,+,+,+)`, was evaluated independently as a basis/convention cross-check below. The obstruction component obtained below is unchanged.

At the origin,

`Gamma^a_bc=0`, `nabla R=0`, and in the repository curvature convention

`R_0i0j=-kappa diag(1,1,-2)_ij`.

In particular

`R_0110=+kappa`, hence `R_011{}^0=+kappa` in the `(+---)` convention.

## 2. Exact Weyl3 Euler tensor at the origin

Use the Iter056X covariant response

`E_W3^{ab} = (1/2) g^{ab} I3 - P^{(a|cde|} R^{b)}_cde - 2 nabla_mu nabla_nu P^{mu(ab)nu}`,

with

`P = 3 Pi_W Pi_R[C^2]`.

An exact symbolic source-jet evaluation gives

`I3(0) = -96 kappa^3`

in the `(+---)` convention and

`E_W3^{ab}(0) = kappa^3 diag(0,160,160,-416)`.

Because the origin metric is diagonal with entries of unit magnitude, the lower-index tensor has the same diagonal components there. Its trace is

`E_W3(0)=+96 kappa^3=-I3(0)`,

exactly reproducing the Iter056X trace Ward identity.

For auditability, the diagonal Euler decomposition at the origin is

| a | `(1/2) g^{aa} I3` | `P^{(a|cde|}R^{a)}_cde` | `D^{aa}=nabla_mu nabla_nu P^{mu(aa)nu}` | `E_W3^{aa}` |
|---|---:|---:|---:|---:|
| 0 | `-48 kappa^3` | `-72 kappa^3` | `12 kappa^3` | `0` |
| 1 | `48 kappa^3` | `72 kappa^3` | `-92 kappa^3` | `160 kappa^3` |
| 2 | `48 kappa^3` | `72 kappa^3` | `-92 kappa^3` | `160 kappa^3` |
| 3 | `48 kappa^3` | `72 kappa^3` | `196 kappa^3` | `-416 kappa^3` |

The same symbolic evaluator independently satisfies

`P^{abcd} R_abcd = 3 I3`

and the full trace identity through the quadratic source jet used for the prolongation calculation.

Therefore

`Hbar_ab(0)=kappa^3 diag(-16,96,96,-192)`.

In particular

**`Hbar_00(0)=-16 kappa^3`.**

## 3. Counterexample-first component

Choose the preregistered component `(e,c,a,b)=(0,0,1,1)`:

`Kbar_0011 = [nabla_0 nabla_0 Hbar_11 - nabla_0 nabla_1 Hbar_01]_0 - R_011{}^d Hbar_0d`.

The source and every covariantly constructed response tensor are static. At the origin `Gamma=0`, while the source is diagonal and inversion-even. Consequently both differentiated terms in this component vanish exactly:

`[nabla_0 nabla_0 Hbar_11]_0=0`,

`[nabla_0 nabla_1 Hbar_01]_0=0`.

Only the curvature-prolongation term remains. Since `Hbar_0d` is nonzero only for `d=0`,

`Kbar_0011 = - R_011{}^0 Hbar_00`

`             = -(kappa)(-16 kappa^3)`

`             = 16 kappa^4`.

Thus for every nonzero source amplitude,

**`Kbar_0011 = 16 kappa^4 != 0`.**

For the exact production value `kappa=2/25`,

**`Kbar_0011 = 256/390625 != 0`.**

Because `A_E` is frozen finite and nonzero, `Kbar=A_E K` and therefore `K_0011` is also exactly nonzero.

## 4. Full-tensor and convention cross-checks

A separate exact symbolic enumeration of all 256 ordered components found 24 nonzero ordered components of `Kbar`; every nonzero entry is proportional to `kappa^4`. The simplest family includes

- `Kbar_0011=Kbar_0022=16 kappa^4`,
- `Kbar_0033=-32 kappa^4`,
- the corresponding `c <-> a` exchanges with the required minus sign.

The same calculation was repeated after the global metric-sign conversion to the frozen `(-,+,+,+)` convention used by `qgr_iter057f_g3_origin_weyl3_k2.py`. `I3` changes its expected global-sign weight, while `Hbar_ab(0)` and the complete `Kbar` component set above are unchanged. This rules out the known source/production signature presentation difference as an explanation of the nonzero obstruction.

Additional exact controls passed:

- `P.R = 3 I3`;
- `g_ab E_W3^{ab} = -I3` through the required quadratic jet;
- the fully antisymmetric four-form part of the source `C^2` insertion vanishes at the origin;
- repeated exact rational probes at `kappa=1/10`, `1/20`, and `2/25` reproduce the symbolic `16 kappa^4` scaling.

A numerical finite-difference reimplementation was attempted only as a post-target diagnostic but exceeded the local execution limit; it is not used for the scientific decision.

## 5. Preregistered decision

The Iter057J preregistration requires exact zero of the full independent `K_ecab` set for the conformal candidate to survive this prolongation. It explicitly authorizes a single exact nonzero component to terminalize the candidate as scientific FAIL.

Since

`Kbar_0011=16 kappa^4 != 0` for `kappa != 0`,

the frozen first-order **conformal open-neighborhood continuation candidate fails its first nontrivial prolongation condition**.

This does not show that no nonconformal first-order correction exists, no Weyl-active on-shell background exists, or that Einstein+Weyl3 dynamics is inconsistent. It only rejects the specific Iter057I conformal Hessian continuation as an open-neighborhood solution on the frozen G3/H0 source.

## Claim locks

`c6` remains symbolic/unfixed; `beta=1` remains unauthorized; no physical Weyl3 treatment selector is established; no strong-hyperbolicity, ghost, stability, unitarity, regulator-removal, UV-completion, experimental-confirmation, or KMQGB `NEW_REQUIRED` claim is authorized. Theory established remains `0%`.