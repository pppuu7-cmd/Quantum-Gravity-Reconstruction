# Iter054H preregistration — refinement-domain conditional order-reduction derivation

Date: 2026-09-14

Gate: `ITER054H-WEYL3-REFINEMENT-DOMAIN-CONDITIONAL-ORDER-REDUCTION`

Status at freeze: **PREREGISTERED BEFORE SUBSTANTIVE OUTPUTS**

Frozen QGR source snapshot: `0772597480b06d2d69b5ced2842c2203378635d5`

## Scientific question

After Iter054G-R established that no **pre-existing** QGR authority selects exact finite-`c6` versus perturbative/order-reduced Weyl3 dynamics, can the already-derived QGR refinement/operator hierarchy prospectively supply a controlled **conditional** low-resolution domain in which the exact singular higher-derivative branch lies above an explicitly defined resolved band?

If the conditional separation is exact, does existing QGR authority also supply enough physical band/cutoff, coefficient/background bound and omitted-operator/remainder control to promote that conditional statement to an actual order-reduced dynamical-treatment selector?

The gate must distinguish these two claims. It is not allowed to declare order-reduced dynamics physical merely because a toy singular root can be placed outside an arbitrarily chosen band.

## Frozen QGR inputs

Read only source material available at the frozen snapshot, especially:

- `iterations/ITERATION_007.md`;
- `iterations/ITERATION_008.md`;
- `iterations/ITERATION_009.md`;
- `results/ITER009_G3_SIX_DERIVATIVE_PHYSICAL_OPERATOR_CENSUS.md`;
- `results/ITER009_G6_STRONG_LIMIT_AND_C6_DECISION.md`;
- `preregistration/ITER054A_WEYL3_DERIVATIVE_ORDER_AND_REGIME_SEPARATION.md`;
- `results/ITER054A_TERMINAL_RESULT.md`;
- `results/ITER054G_R_TERMINAL_RESULT.md`;
- `recovery/CURRENT_FRONT.md`;
- `recovery/state.json`.

Later files cannot retroactively satisfy this gate.

The frozen source facts to be checked rather than assumed are:

1. the first nonredundant Ricci-flat parity-even local six-derivative correction is represented as
   `S6 = a_cont * c6 * h^4 * integral(Weyl^3)`;
2. current QGR lacks an exact higher-derivative finite-cell UV action/matching rule fixing `c6`;
3. the regular weak-curvature branch admits a refinement expansion in which regular `c6 O(h^4)` per-cell corrections vanish in the `h -> 0` serial limit;
4. the established broadband one-particle comparator uses an analytic momentum integral with **no arbitrary UV momentum cutoff**;
5. the physical microscopic scale/coupling remains unfixed rather than supplying a universal nonzero stop scale;
6. exact-vs-perturbative characteristic regimes are distinct and the singular exact root is non-analytic in the small higher-derivative coefficient.

## Frozen principal proxy and dimensionless variables

For the sole purpose of deriving a necessary/sufficient scale-separation inequality in one frozen Weyl-active eigenchannel, use

`P(z) = z + alpha z^2 = z(1+alpha z)`

with

`alpha = c6 * h^4 * Cbar_eig`,

where `Cbar_eig != 0` is the signed background Weyl/eigenchannel factor carried by the fourth-order principal correction. This proxy inherits the Iter054A/E factor structure; it is not a full tensor characteristic determinant.

Define magnitudes

`chi = |c6 * Cbar_eig| * h^2 > 0`,

`q^2 = |z| * h^2`,

and an assumed resolved dimensionless band

`0 <= q <= q_max`.

Then the preregistered target relations are

`rho(q) = |alpha z| = chi q^2`,

and for the exact singular root `z_HD=-1/alpha`,

`q_HD^2 = |z_HD| h^2 = 1/chi`,

`q_HD = chi^(-1/2)`.

These identities alone do not make `q_max` physical.

## Frozen streams

### A0 — exact symbolic scale-separation identities

Using exact SymPy algebra with positive symbols for magnitudes, require:

1. `|alpha z|` reduces to `chi q^2` under the magnitude definitions;
2. the exact singular root is `z_HD=-1/alpha`;
3. `q_HD^2=1/chi` and `q_HD=1/sqrt(chi)`;
4. if `chi*q_max^2 < 1`, then the higher-derivative/Einstein principal ratio is <1 throughout the assumed band;
5. if `chi < 1/q_max^2`, then `q_HD > q_max`;
6. the two inequalities are algebraically the same separation condition for positive variables.

A0 is exact algebra only.

### A1 — frozen rational positive/negative panel

Use a preregistered deterministic panel:

Positive conditional-separation cases:

- `(chi,q_max)=(1/100,1/2)`;
- `(1/25,1/2)`;
- `(1/16,1)`;
- `(1/9,1/2)`;
- `(1/4,1/2)`;
- `(1/100,1)`.

Require in every positive case:

- `rho_max=chi*q_max^2 < 1`;
- `q_HD=1/sqrt(chi) > q_max`.

Negative controls:

- `(chi,q_max)=(4,1)`;
- `(1,1)`;
- `(9,1/2)`;
- `(16,1/2)`.

Require each negative control to violate strict branch-above-band separation (`q_HD <= q_max`) and/or strict perturbative ratio (`rho_max >=1`) exactly as implied by the same formulas. No case may be dropped.

### B0 — frozen QGR authority audit for physical promotion

Audit the frozen sources for five independent obligations:

1. **h4 hierarchy authority** — `Weyl^3` enters as the first local correction with explicit `h^4` refinement power;
2. **physical resolved-band authority** — QGR supplies a derived momentum/frequency band or cutoff in terms of `h` that physically restricts the histories/modes to `q<=q_max`, rather than the analyst choosing a band;
3. **chi-bound authority** — QGR supplies a derived physical bound ensuring `|c6 Cbar_eig| h^2 q_max^2 < 1` on the claimed background/domain;
4. **remainder/operator-tower control** — QGR supplies sufficient omitted-operator/all-orders/remainder control to justify truncating at the Weyl3 correction in that domain;
5. **microscopic/state mapping** — the proposed reduced domain is mapped to the QGR microscopic state/measure/composition structure and GR-connected branch rather than merely imposed on a scalar proxy.

Each obligation is separately true/false with exact source paths/excerpts. Keyword presence is not enough.

### B1 — anti-overclaim / counterexample lane

Freeze the following controls:

1. the cutoff-free broadband one-particle comparator is evidence that `q<=1` is **not automatically** an already-authorized physical momentum cutoff;
2. `c6` is unfixed, so weak curvature `h^2|Cbar|<<1` alone does not imply `chi<<1` uniformly for arbitrary allowed `c6`;
3. if `chi>=1/q_max^2`, the exact singular branch is at or below the assumed band edge and cannot be excluded by the scale argument;
4. a conditional branch-above-band theorem does not establish strong hyperbolicity, because eigenvector/symmetrizer/constraint obligations from Iter054F remain separate;
5. no physical ghost/no-ghost, mode count, residue sign, unitarity or quantum claim follows.

## Frozen aggregate classifier

All A0/A1/B0/B1 must be present and controls-valid.

If A0/A1 exact scale-separation controls pass:

- if **all five** B0 physical-promotion obligations are true and B1 passes, classify
  `ITER054H_ORDER_REDUCED_TREATMENT_SELECTED_IN_DERIVED_REFINEMENT_DOMAIN_READY_FOR_REDUCED_EVOLUTION_CONSTRUCTION`;
- if the exact conditional separation is established but one or more B0 promotion obligations are false and B1 passes, classify
  `PASS_SCOPED_ITER054H_CONDITIONAL_REFINEMENT_BAND_SEPARATION__PHYSICAL_ORDER_REDUCED_TREATMENT_NOT_AUTHORIZED`;
- if source provenance contradicts the frozen `h^4` hierarchy or required inputs, classify
  `INVALID_SOURCE_OR_OBJECT_ITER054H`;
- if exact algebra/controls do not realize the frozen formulas, classify
  `INVALID_IMPLEMENTATION_ITER054H`.

No threshold may be tuned after output. `q_max` in A0/A1 is an explicit assumed analysis band, not a discovered physical cutoff.

## Interpretation ceiling

A conditional scoped classification establishes at most this mathematical bridge:

**if** a QGR physical domain later satisfies `chi q_max^2 < 1`, **then** the singular proxy branch lies above that domain and the higher-derivative principal correction is perturbative there.

It does not itself select order-reduced QGR dynamics, construct the reduced tensor equations, define the full evolution object, establish strong hyperbolicity/well-posedness, count physical modes, prove a ghost or positivity, fix `c6`, authorize `beta=1`, establish quantum unitarity/amplitude/measure, UV completion, full GR recovery, experiment or new physics.

Theory established remains 0%.
