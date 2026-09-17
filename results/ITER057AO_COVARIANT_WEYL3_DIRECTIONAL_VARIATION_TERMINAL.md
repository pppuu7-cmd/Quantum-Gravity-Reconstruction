# Iter057AO terminal result — covariant Weyl^3 directional variation certificate

Date: 2026-09-17
Gate: `ITER057AO_COVARIANT_WEYL3_DIRECTIONAL_VARIATION_CERTIFICATE`
Preregistration: `e1ded07e5050763ecb707dad679b78286fe04744`
Durable authority: `3274acefe845c9843d6a742c42370e73bb3a2892`

## Terminal classification

**`PASS_SCOPED_ITER057AO_COVARIANT_WEYL3_DIRECTIONAL_VARIATION_CERTIFIED`**

## New scientific authority

For the frozen classical functional

`S6[g] = c6 integral sqrt(-g) C_ab^{ cd} C_cd^{ ef} C_ef^{ ab}`

with `c6` symbolic/unfixed, a source-faithful covariant metric-variation certificate has now been independently established without importing AF/AM/AN obstruction matrices or AG/AH witness data.

The terminal authority contains two independent exact first-variation constructions:

1. an analytic tensor variation route with explicit variation of inverse metric, curvature, Weyl tensor, all index raising and determinant density; and
2. an independent direct first-order dual-number propagation of the full `g + epsilon h` tensor constructor through inverse metric, Riemann, Ricci, scalar curvature, Weyl and the cubic invariant.

They agree exactly on both frozen seeds:

- generic directional-density SHA256: `588c590a2d7a3bc3a87eddfe2aead38af19c9d7b23676f4f688d713ec2847aed`;
- held-out directional-density SHA256: `b3701b7beef637a741fb6ef2dad18a5b81b086f0bc5cf3255f7a70242f5441db`.

Both directional variations are nonzero.

## Exact controls

All frozen terminal controls pass exactly:

- first-order linearity in `h`;
- structural symmetry `h_ab=h_ba`;
- base and linearized Weyl antisymmetries, pair exchange, algebraic Bianchi and trace-free identities;
- exact constant-curvature Weyl-zero control, with `C=0`, `C^3=0` and first variation zero by the cubic structure;
- exact nonconstant conformally-flat control for the frozen `Omega=2+t+x^2+2y^2+3z^2`, with the same exact zeros;
- exact direct diffeomorphism/Noether density identity for `h_ab=nabla_a xi_b+nabla_b xi_a`:
  `delta_xi[sqrt(-g) I3] = partial_mu[xi^mu sqrt(-g) I3]`;
- fake-gauge negative control detected;
- Einstein-Hilbert sign control reduces the compact bulk formula to `-G^{ab}` for covariant `h_ab`;
- Einstein-Hilbert boundary control reduces to `nabla_nu h^{mu nu}-nabla^mu h`;
- wrong sign in `delta g^{-1}`, omitted determinant variation, and omitted raised-index variation are all detected by prospectively frozen negative controls;
- no floating scientific tolerance is used.

## Compact bulk + boundary / IBP authority

The exact source-level variation is represented by the frozen general `f(g,Riemann)` identity

`delta[sqrt(-g) f] = sqrt(-g)[E_cov^{ab} h_ab + nabla_mu Theta^mu]`,

with algebraic curvature derivative `P^{abcd}` defined by

`P^{abcd} K_abcd = d/ds f(g,R+sK)|_{s=0}`

on algebraic Riemann variations, and

`E_cov^{ab} = -P^{a c d e} R^b_{ c d e} + 2 nabla_c nabla_d P^{a c d b} + (1/2)g^{ab}f`,

`Theta^mu = 2 P^{mu b c d} nabla_d h_bc - 2(nabla_d P^{mu b c d})h_bc`.

Canonical formula SHA256: `ed33830a964d90b9b9e09b75f8ebc0e0820677ae8b57bb09fb5ba073ce5030dc`.

The divergence term is explicitly retained. Combining the exact Lie-density identity with this bulk+boundary representation gives the off-shell Noether identity `nabla_a E_cov^{ab}=0` for the frozen covariant Euler representative.

## Production and independent replay

Analytic phase-2 implementation:

- phase-2 implementation freeze: `0daf8a632c060c0f758f15bd43b4837633a48efa`;
- execution-only compact repair: `7a7c764f3d2a4e592f738af906040d4f8cca93e5`;
- implementation commit: `c1616a7ba5d540e14c667ad49c53f873ae21a0cc`;
- assembled source SHA256: `7cc63a46cba36fe903095494876028d9e7ebbe163a60ae35978372756a0ddf4a`;
- authoritative production run: `35174624482`.

Independent direct-dual replay:

- implementation commit: `1426fee93f2ea830b3c84e23999bf22b650c7a1e`;
- production run: `35174764423`;
- generic artifact `10477483765`, digest `sha256:8cc1150774e158696d7a293f50e7a31c1cce6be953d5e1263600e04d267098d8`;
- held-out artifact `10478421220`, digest `sha256:dbf4c239103afe5f2ddb8c8c42f2c25527107889cffc67ec929bb04a971833ba`.

Terminal adversarial Critic:

- Critic-v3 implementation `1fd630bc42b9b407e2380b2d2c0158d7800e2be3`;
- workflow head `7ded678585202ede8e2a2a57c02c64dd553e2bfd`;
- run/job `35174996304 / 105054622895`;
- artifact `10477623774`, digest `sha256:b2aecfe717e2f4ab8159b23dea3b7e7a33a0a12eeef0e1e9ffd8d54a030399ed`;
- terminal scientific payload SHA256 `73af6936acccf1cd69a95a2d153b5fc572bea0cdd59e21b0612fcdd55b835dd0`;
- all 21 Critic predicates are exact `true`.

The Critic artifact was independently downloaded and its scientific payload SHA256 was recomputed byte-for-semantic-payload exactly.

## Technical history that is not scientific evidence

- phase-2 run `35174458061` failed before any scientific lane or held-out evaluation because one transported source chunk was binary-corrupted; packaging-only repair `49564d70a7adb4cb43f9a118f0c83a8a9e7d983a` restored the already-frozen source without changing its SHA or scientific logic;
- Critic-v2 run `35174885633` failed because the Critic parser used `control.defect_detected` instead of the already-frozen artifact schema `controls.defect_detected`; review/repair record `aef0903c50cefd61a454a21a16af05c6989e912d` changed only that field lookup and did not change any acceptance criterion.

The original phase-1 giant-SymPy run `35168268602` remains in progress at terminalization and is explicitly nonterminal supplemental evidence; it was not used for the terminal classification.

## Scientific meaning

This is the first independently reproduced **source-level covariant classical Weyl^3 metric-variation authority** in the current programme, including a retained boundary/divergence representation, exact Noether/diffeomorphism identity, exact Weyl-zero controls, held-out no-refit certificate and an independent constructor-level replay.

It is therefore materially stronger than the earlier finite-local AF/AM/AN obstruction panels, but it does not yet prove that the newly derived covariant Euler object restricts to the same AF/AM/AN one-dimensional R14 obstruction class. That comparison remains a separate no-refit gate.

## Claim ceiling

This result does **not** establish an arbitrary-background theorem, an all-orders/global no-go theorem, hyperbolicity, mode health, ghost freedom, stability, quantum unitarity, regulator removal, UV completion, experiment or new physics. `c6` remains symbolic/unfixed; `beta=1` remains unauthorized; theory established remains `0%`.

## Highest-information next gate

Prospectively freeze a no-refit `COVARIANT-TO-R14 RESTRICTION / OBSTRUCTION MATCH` gate. The restriction map, basis conventions, background identities, normalization, equivalence quotient and comparison invariant must be fixed before looking at AF/AM/AN match outcomes. The central question is whether the independently derived covariant `E6_ab`, restricted through that frozen map, reproduces the previously observed one-dimensional compatibility obstruction class without fitting.