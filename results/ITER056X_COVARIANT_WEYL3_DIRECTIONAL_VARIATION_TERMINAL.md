# Iter056X terminal result — covariant Weyl3 directional variation

Date: 2026-09-15
Gate: `ITER056X-COVARIANT-WEYL3-DIRECTIONAL-VARIATION-CERTIFICATE`
Prospective preregistration: `ed37dea540cb8afdc395486c93a8a92fefb02a0c`
Analytic derivation certificate: `5b2acf5a47f4ba66fb126bdeab28505dd0dfb852`

## Terminal classification

**`PASS_SCOPED_ITER056X_COVARIANT_WEYL3_DIRECTIONAL_VARIATION_CERTIFIED__C6_SYMBOLIC_UNFIXED`**

## Certified covariant identity

For the frozen covariant metric variation

`delta g_ab = h_ab`,

with symmetric compactly supported `h_ab`, and

`I3 = C_ab{}^{cd} C_cd{}^{ef} C_ef{}^{ab}`,

let

`P^{abcd} = partial I3 / partial R_abcd |_g`

in the all-lowered algebraic-Riemann convention already certified by Iter051B1. Then

`delta S_W3 = c6 integral sqrt(-g) E_W3^{ab} h_ab d^4x + c6 integral partial_mu Theta^mu d^4x`,

with

`E_W3^{ab} = (1/2) g^{ab} I3`

`              - P^{(a|cde|} R^{b)}_cde`

`              - 2 nabla_mu nabla_nu P^{mu(ab)nu}`,

and

`Theta^mu = 2 sqrt(-g) [ P^{mu(ab)nu} nabla_nu h_ab - h_ab nabla_nu P^{mu(ab)nu} ]`.

For compact support the integrated boundary term vanishes independently.

`c6` remains an overall symbolic multiplier and is not fixed or fitted.

## Frozen requirement audit

### A — determinant variation: PASS

The derivation explicitly uses

`delta sqrt(-g) = (1/2) sqrt(-g) g^{ab} h_ab`

and `delta g^{ab}=-h^{ab}`.

### B — Weyl variation: PASS

The Weyl variation is derived from the Levi-Civita connection, Palatini Riemann variation, Ricci variation, scalar variation, explicit metric factors in the 4D Weyl projector, and inverse-metric variation in the mixed Weyl indices. No symmetry-reduced Weyl response is imported into the derivation.

### C — covariant integration by parts: PASS

The curvature-response term is integrated twice covariantly. The exact boundary current is displayed, with the authoritative Iter052 derivative-sector sign `-2` preserved.

### D — explicit bulk response: PASS

The tensor `E_W3^{ab}` above is a manifestly covariant off-shell bulk response in the frozen covariant-metric convention.

### E — highest derivative accounting: PASS

Because `P=O(C^2)` and `C` contains second metric derivatives,

`nabla nabla P = O(C nabla nabla C) + O((nabla C)^2)`.

Thus the **generic off-shell metric equation is fourth differential order**, not sixth order. “Six derivative” is EFT/operator counting for `Riemann^3`, not the field-equation differential order.

The separate Iter056G Einstein-shell result remains a scoped reduction: on smooth 4D Einstein backgrounds the highest fourth-metric-derivative channel can be commuted/reduced using `nabla^a C_abcd=0`. That shell result is not promoted off shell.

### F — diffeomorphism / Noether identity: PASS

Using `h_ab=L_xi g_ab=2 nabla_(a xi_b)` and compact support, diffeomorphism invariance implies the exact formal identity

`nabla_a E_W3^{ab}=0`.

No equation of motion is assumed in deriving this identity.

### G1 — conformally-flat null: PASS

`C=0 => I3=0, P=0, E_W3=0, Theta=0`.

This agrees with the independent conformally-flat null authority in Iter051B1/Iter052.

### G2 — constant rescaling: PASS

In 4D under constant `g_ab -> lambda g_ab`,

`sqrt(-g) I3 -> lambda^(-1) sqrt(-g) I3`.

Therefore the direction `h_ab=g_ab` requires

`g_ab E_W3^{ab} = -I3`.

The explicit bulk tensor satisfies this exactly because `P.R=3 I3`, `P` is Weyl-trace-free, and the double-divergence trace vanishes.

This control independently catches omitted determinant or index-raising contributions and wrong algebraic signs.

### G3 — downstream weak-field control: PASS / consistency only

After the covariant derivation, the authorized Iter040/041 weak static tidal family gives `C~kappa` and `I3~kappa^3`. The covariant directional variation therefore gives `dI3/dkappa~3 kappa^2`, consistent with the independent measured cubic amplitude slopes approximately equal to 3. This control is downstream only and was not used to derive `E_W3`.

### H — no promotion: PASS

No value or running of `c6` is inferred; `beta=1` is not used; no exact-vs-order-reduced treatment is selected; no quantum unitarity, UV completion, or theory-establishment claim is made.

## Relationship to earlier authority

This result does not rewrite earlier history.

- Iter051B1 remains the independent finite generic certificate for the algebraic `P=dI3/dR` insertion.
- Historical Iter051C / D2 sign/control failures remain immutable.
- Iter052 remains the independent 12-lane genuinely 4D computational certificate of
  `direct directional derivative = H5.h + div Theta`, with the corrected `H5=A+I-2 sqrt(-g) D5` sign.
- Iter056G remains the scoped Einstein-shell derivative-reduction result.

The new information is that these previously separated computational/operator facts are now assembled into one explicit manifestly covariant analytic bulk-and-boundary formula satisfying the frozen Iter056X A–H obligations.

## Why no new GitHub Actions production was launched

No new numerical CI was required to establish this terminal result. The new step is an exact analytic assembly using already-authorized source objects and sign conventions, while the nontrivial generic numerical directional-variation, covariance and conformal-null tests were already consumed by Iter051B1 and Iter052. Launching a new job that merely replays those panels would be duplicate/fake load; green CI would add no scientific authority to the analytic identity.

## Interpretation ceiling

This PASS is a scoped classical covariant variational certificate for the Weyl-cubic local operator. It is not a proof of a complete quantum-gravity theory or of a physically preferred higher-derivative treatment.

It does not establish strong hyperbolicity of exact Weyl3 dynamics, convergence of an EFT/order-reduced expansion, a regulator-removed interacting measure, quantum unitarity, UV completion, full GR recovery, experiment, or new physics.

`c6` remains symbolic/unfixed; `beta=1` remains unauthorized; `theory established = 0%`.