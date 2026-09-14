# Iter056X — covariant Weyl3 directional-variation certificate

Date: 2026-09-15
Gate: `ITER056X-COVARIANT-WEYL3-DIRECTIONAL-VARIATION-CERTIFICATE`
Prospective preregistration: `ed37dea540cb8afdc395486c93a8a92fefb02a0c`

## Scope and convention

Work in four spacetime dimensions with Levi-Civita connection and Lorentzian metric `g_ab`. Antisymmetrization brackets have weight one half. The varied field is the **covariant** metric,

`delta g_ab = h_ab`,

with symmetric compactly supported `h_ab`. Indices on `h` are raised only after the variation, e.g. `h^a_b = g^{ac} h_cb`.

The frozen scalar is

`I3 = C_ab{}^{cd} C_cd{}^{ef} C_ef{}^{ab}`,

and

`S_W3[g] = c6 integral sqrt(-g) I3 d^4x`,

with `c6` a global symbolic multiplier throughout.

This derivation uses the same all-lowered curvature/P-tensor convention already certified in Iter051B1 and the same directional-variation/boundary-current convention used by the terminal Iter052 4D certificate. In particular the derivative-sector sign is the authoritative Iter052 sign `-2 D`, not the historical pre-correction `+2 D` sign.

## A. Determinant and inverse-metric variation

For `delta g_ab=h_ab`,

`delta g^{ab} = - h^{ab}`,

and

`delta sqrt(-g) = (1/2) sqrt(-g) g^{ab} h_ab`.

Thus the determinant contribution is exact and is not omitted from the Weyl-cubic variation.

## B. Curvature and Weyl variation

The Levi-Civita connection varies as

`delta Gamma^a_bc = (1/2) g^{ad} (nabla_b h_cd + nabla_c h_bd - nabla_d h_bc)`.

The mixed Riemann tensor varies by the Palatini identity

`delta R^a_bcd = 2 nabla_[c delta Gamma^a_{d]b}`.

For the all-lowered curvature object used by the repository,

`delta R_abcd = h_ae R^e_bcd + g_ae delta R^e_bcd`.

The Ricci and scalar variations are derived from this same object:

`delta R_bd = delta R^a_bad`,

`delta R = - h^{bd} R_bd + g^{bd} delta R_bd`.

In four dimensions, with the stated bracket convention,

`C_abcd = R_abcd - (g_{a[c} R_{d]b} - g_{b[c} R_{d]a}) + (1/3) R g_{a[c} g_{d]b}`.

Therefore

`delta C_abcd = delta R_abcd`

` - [ h_{a[c} R_{d]b} + g_{a[c} delta R_{d]b} - h_{b[c} R_{d]a} - g_{b[c} delta R_{d]a} ]`

` + (1/3) delta R g_{a[c} g_{d]b}`

` + (1/3) R [ h_{a[c} g_{d]b} + g_{a[c} h_{d]b} ]`.

The mixed Weyl tensor appearing in `I3` also contains inverse-metric variation:

`delta C_ab{}^{cd} = g^{ce} g^{df} delta C_abef - h^c_e C_ab{}^{ed} - h^d_e C_ab{}^{ce}`.

Hence the complete cubic variation is

`delta I3 = 3 (C^2)_cd{}^{ab} delta C_ab{}^{cd}`,

where `(C^2)_cd{}^{ab}=C_cd{}^{ef} C_ef{}^{ab}`. This explicitly includes the metric/Ricci/scalar/Weyl-projector and index-raising dependence required by the preregistration.

### Curvature insertion P

At fixed metric define the algebraic-Riemann curvature derivative

`P^{abcd} := partial I3 / partial R_abcd |_g`.

Equivalently, let

`Q^{abcd} = C^{ab}{}_{ef} C^{efcd}`,

project `Q` onto the algebraic-Riemann subspace and then onto its Weyl-trace-free part. If `Pi_R` is the algebraic-Riemann projection and `Pi_W` the four-dimensional Weyl projector, then

`P = 3 Pi_W Pi_R[Q]`.

For any algebraic-Riemann tensor `X_abcd`,

`(Pi_W X)_abcd = X_abcd - (g_{a[c} X_{d]b} - g_{b[c} X_{d]a}) + (1/3) X g_{a[c} g_{d]b}`,

with `X_bd = g^{ac} X_abcd` and `X=g^{bd}X_bd`. In 4D, for a pair-antisymmetric/pair-symmetric tensor, `Pi_R` removes its fully antisymmetric four-form component. This representation is the analytic form of the projected `P=dI3/dR` object already numerically certified by Iter051B1.

Consequences used below:

- `P` has the algebraic Riemann symmetries;
- all Ricci traces of `P` vanish because `P` lies in the Weyl subspace;
- cubic homogeneity gives the exact Euler identity

  `P^{abcd} R_abcd = 3 I3`,

  because the trace parts of `R` are annihilated by the Weyl-trace-free `P`.

## C. Covariant integration by parts and boundary current

Split the all-lowered curvature variation into the lowering insertion and the connection response:

`P^{abcd} delta R_abcd = P^{abcd} h_ae R^e_bcd + P^{abcd} g_ae delta R^e_bcd`.

The first term is algebraic. Its symmetric coefficient is

`P^{(a|cde|} R^{b)}_cde h_ab`.

Using the Palatini identity in the second term and integrating covariantly twice gives the exact repository-convention identity

`sqrt(-g) P^{abcd} g_ae delta R^e_bcd`

`= -2 sqrt(-g) [nabla_mu nabla_nu P^{mu(ab)nu}] h_ab + partial_mu Theta^mu`,

where the boundary-current density is

`Theta^mu = 2 sqrt(-g) [ P^{mu(ab)nu} nabla_nu h_ab - h_ab nabla_nu P^{mu(ab)nu} ]`.

This is the same current and the same `-2` derivative-sector sign used in the terminal Iter052 identity.

For compactly supported `h_ab`, the integrated boundary term vanishes independently:

`integral partial_mu Theta^mu d^4x = 0`.

No coordinate ansatz or symmetry reduction is used.

## D. Explicit covariant bulk response

Combining determinant, explicit metric/index-raising dependence, the curvature-lowering insertion, and the integrated connection response gives

`delta S_W3 = c6 integral sqrt(-g) E_W3^{ab} h_ab d^4x + c6 integral partial_mu Theta^mu d^4x`,

with

`E_W3^{ab} = (1/2) g^{ab} I3`

`              - P^{(a|cde|} R^{b)}_cde`

`              - 2 nabla_mu nabla_nu P^{mu(ab)nu}`.

This is the coefficient for the frozen **covariant** variation `delta g_ab=h_ab`. If one instead varies `g^{ab}`, the Euler tensor has the opposite raised/lowered sign, because `delta g^{ab}=-h^{ab}`.

### Exact equivalence to the Iter052 decomposition

Iter052 wrote the density coefficient as

`H5 = A + I - 2 sqrt(-g) D5`.

The analytic decomposition above identifies

`D5^{ab} = nabla_mu nabla_nu P^{mu(ab)nu}`,

`I^{ab} = sqrt(-g) P^{(a|cde|} R^{b)}_cde`,

and

`A^{ab} = sqrt(-g) [ (1/2) g^{ab} I3 - 2 P^{(a|cde|} R^{b)}_cde ]`.

Hence

`A + I = sqrt(-g) [ (1/2) g^{-1} I3 - P.R ]`,

and the present analytic bulk tensor reproduces the already-authorized Iter052 `A+I-2 sqrt(-g) D5` identity exactly in the same convention.

## E. Highest metric-derivative order

`P` is algebraic and quadratic in Weyl:

`P = O(C^2)`.

The Weyl tensor contains at most second derivatives of the metric. Therefore

`nabla nabla P = O(C nabla nabla C) + O((nabla C)^2)`.

Generically off shell, `nabla nabla C` contains fourth derivatives of the metric. The algebraic `P.R` and `I3` terms contain at most second metric derivatives. Therefore the generic covariant Weyl3 Euler response is **fourth order in the metric**, not sixth order.

The phrase “six-derivative operator” is EFT/operator counting (`Riemann^3`), not the differential order of the metric field equation.

This is consistent with the earlier principal-part authority. Iter056G further proves a separate scoped refinement: on smooth four-dimensional Einstein backgrounds, `nabla^a C_abcd=0` lets the `C nabla nabla C` pieces be commuted/reduced to `(nabla C)^2 + R C^2`, removing the generic fourth-metric-derivative channel on that shell. That Einstein-shell reduction is not promoted off shell here.

## F. Diffeomorphism / Noether identity

The density `sqrt(-g) I3` is a scalar density constructed covariantly from the metric and its Levi-Civita curvature. Under an infinitesimal compactly supported diffeomorphism generated by `xi^a`,

`h_ab = L_xi g_ab = 2 nabla_(a xi_b)`.

Diffeomorphism invariance gives `delta_xi S_W3=0`. Using the bulk formula and integrating once,

`0 = 2 c6 integral sqrt(-g) E_W3^{ab} nabla_a xi_b`

`  = -2 c6 integral sqrt(-g) (nabla_a E_W3^{ab}) xi_b`,

with boundary terms zero by compact support. Since `xi_b` is arbitrary,

`nabla_a E_W3^{ab} = 0`

identically off shell.

This is the formal covariant Noether identity required by the gate. It is a consequence of the explicit tensor expression plus diffeomorphism covariance, not a dynamical on-shell assumption.

## G1. Conformally-flat null control

If `C_abcd=0`, then

`I3=0`, `Q=0`, `P=0`.

Therefore every term in `E_W3^{ab}` vanishes and `Theta^mu` also vanishes. Thus the Weyl-cubic first variation is identically zero on the conformally-flat sector, as required. This agrees with the independent conformally-flat null lanes of Iter051B1/Iter052.

## G2. Constant overall rescaling control

Take a constant positive rescaling

`g_ab -> lambda g_ab`.

The Levi-Civita connection and `R^a_bcd` are unchanged. In four dimensions,

`sqrt(-g) -> lambda^2 sqrt(-g)`,

`C_abcd -> lambda C_abcd`,

`C_ab{}^{cd} -> lambda^{-1} C_ab{}^{cd}`,

so

`I3 -> lambda^{-3} I3`

and

`sqrt(-g) I3 -> lambda^{-1} sqrt(-g) I3`.

For the infinitesimal direction `h_ab=g_ab`, the exact density variation must therefore be

`delta [sqrt(-g) I3] = - sqrt(-g) I3`.

The bulk tensor reproduces this directly. Weyl-trace-freeness gives

`g_ab nabla_mu nabla_nu P^{mu(ab)nu}=0`,

and cubic homogeneity gives `P.R=3 I3`, hence

`g_ab E_W3^{ab} = 2 I3 - 3 I3 = - I3`.

This exact trace identity is a sensitive control on the determinant term, all index-raising contributions, the algebraic curvature insertion, and the sign convention.

## G3. Downstream weak-field control

Only after the covariant derivation, specialize to the already-authorized weak static trace-free tidal family used by Iter040/041. There

`C = kappa C_(1) + O(kappa^2)`,

so

`I3 = kappa^3 I3_(3) + O(kappa^4)`

and

`P = O(kappa^2)`.

For the amplitude direction `h_ab = partial g_ab / partial kappa`, the covariant directional variation therefore has leading scaling

`d I3 / d kappa = 3 kappa^2 I3_(3) + O(kappa^3)`.

This is exactly the derivative law implied by the independent Iter040/041 result `Weyl3 ~ kappa^3` (measured slopes approximately 3 on both training and held-out tidal shapes). This is a downstream specialization only and is not used to derive the covariant tensor.

## H. Claim locks

This certificate does **not**:

- fix `c6` or derive its running;
- authorize `beta=1`;
- select exact versus order-reduced physical dynamics;
- establish strong hyperbolicity of the full higher-derivative theory;
- establish a regulator-removed interacting quantum measure;
- establish quantum unitarity or UV completion;
- turn finite/refinement controls into global theorems;
- establish full GR recovery, experiment, new physics, or QGR correctness.

`theory established = 0%` remains unchanged.

## Frozen-requirement disposition

- A determinant variation: **SATISFIED**.
- B Weyl variation from metric/Riemann/Ricci/scalar variations: **SATISFIED**.
- C covariant integration by parts and boundary separation: **SATISFIED**.
- D explicit covariant bulk response: **SATISFIED**.
- E highest derivative accounting: **SATISFIED**; generic off-shell order four, with Iter056G Einstein-shell reduction kept separate.
- F diffeomorphism/Noether divergence identity: **SATISFIED** formally and covariantly.
- G conformal-null, constant-rescaling, and downstream weak-field controls: **SATISFIED**.
- H no coefficient/treatment/quantum promotion: **SATISFIED**.

The analytic certificate is source-compatible with the already-consumed Iter051B1 and Iter052 computational authority and does not overwrite any historical FAIL/INVALID record.