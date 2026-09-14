# Post-Iter053 audit — exact remaining Weyl^3 principal-symbol / stability object

Date: 2026-09-14

Status: outcome-independent dependency audit. **Not a preregistration and not an active scientific gate.** It is valid regardless of the terminal outcome of the active Iter053T productions.

## Question

Assuming a later gate establishes an admissible full covariant metric functional derivative for the QGR `sqrt(-g) Weyl^3` correction, what stability/spectrum object is still missing before any quantum-amplitude/measure transition can be scientifically justified?

## Existing authority and what it already closes

### Iter005 — two-derivative weak-background principal symbol

Iter005 established, for the already reconstructed local at-most-two-derivative QGR-L1 action, a scoped local weak-background characteristic structure: one continuously deformed Lorentzian cone and two physical modes on tested weak regular backgrounds. It explicitly did not establish global hyperbolicity or strong-background stability.

Therefore a new gate must not repeat the two-derivative weak-background rank calculation.

### Iter010 — Weyl-active same-field background exists

Iter010 constructed a same-field-content weak tidal background with nonzero continuum Weyl and Weyl-cubed invariant. Its role was a `c6` sensitivity witness. It did not compute the linearized corrected equations or their characteristic polynomial.

### Iter043–045 — flat/linearized TT and relative residues

Iter043 validated a held-out TT radiative curvature observable but explicitly did not show the QGR dynamics generates it. Iter044 then established an end-to-end flat-background QGR-L1 linearized TT sector with two massless modes, gauge robustness and flat-background decoupling of `c6 Weyl^3`. Iter045 established only relative degeneracy/sign of the two TT pole coefficients and explicitly did not establish overall energy positivity, quantum unitarity or nonlinear stability.

A new gate must therefore avoid treating the already-closed flat TT sector as the missing `c6` stability question.

### Iter046 — exact nonlinear pp-wave sector is Weyl^3-blind

Iter046 established an exact finite-amplitude nonlinear pp-wave family for the at-most-two-derivative action, but explicitly excluded the dynamics of the six-derivative correction. Iter047 subsequently proved why: the tested type-N pp-wave has nonzero Weyl tensor but `W2=W3=0`.

Thus pp-wave stability cannot expose the generic principal part of a Weyl-cubic correction.

### Iter047 — curvature classes where Weyl^3 is active

Iter047 established exact nonzero `W3` on Schwarzschild/Petrov-D and Kasner witnesses, while type-N pp-wave and conformally flat controls are blind. This supplies suitable curved-background classes for a future `c6` principal-symbol test.

### Iter048–050 — variational prerequisites, not corrected characteristics

Iter048 and Iter049 established nonzero symmetry-reduced variational response in Bianchi-I/Kasner and static spherical/Schwarzschild sectors. Iter050 established a non-symmetry-reduced fixed-metric curvature-direction/P-tensor prerequisite. None derived the gauge-reduced principal symbol of the full corrected metric equations.

### Iter051–Iter053 chain

The current chain is attempting to close the full covariant metric-functional-variation object, including the derivative/double-divergence sector. Until that chain has a valid terminal authority, the full corrected principal symbol is not an admissible scientific object.

## Exact missing object

The next fatal-consistency object after a valid full functional-variation closure is:

**the gauge-reduced highest-derivative principal symbol of the linearization of the full corrected metric equations**

`E_2[g] + c6 E_6[g] = 0`

about at least one frozen, Weyl-active curved background, with `c6` kept symbolic/unfixed.

The calculation must distinguish:

1. the already-known two-derivative QGR-L1 principal symbol;
2. the genuine highest-derivative contribution from linearized `E_6`;
3. pure diffeomorphism/gauge null directions;
4. physical characteristic branches after gauge reduction;
5. degeneracies special to the chosen background or propagation direction.

## Why this is the fatal gate

A six-derivative metric correction can modify the high-frequency characteristic polynomial on backgrounds where Weyl is nonzero even though it decouples on flat background. Before introducing a quantum measure or amplitude, the candidate must determine whether the corrected classical equations possess extra physical high-frequency branches, non-hyperbolic directions, unavoidable multiple characteristics, or other principal-symbol obstructions in the Weyl-active sector.

This is a structural consistency question, not a precision refinement.

## Recommended frozen background hierarchy

If and only if the functional-variation dependency is later authorized, the most informative prospective matrix is:

- **A / Schwarzschild-Petrov-D local tetrad witnesses:** Weyl-active, geometrically independent of Bianchi-I;
- **B / Kasner anisotropic witnesses:** Weyl-active and analytically simple enough for independent symbolic checks;
- **C / conformally-flat control:** `Weyl=0`, where the six-derivative contribution should satisfy the separately derived null expectation appropriate to the exact linearized object;
- **D / type-N pp-wave control:** scalar `W3=0`; included only if the full linearized `E_6` null/degeneracy expectation is derived prospectively, not assumed from scalar blindness.

Backgrounds must be frozen before observing the principal-symbol spectrum. No background may be selected because it gives a preferred result.

## Required prospective controls

A future gate should include, before substantive calculation:

- exact object identity to the terminal full functional derivative;
- frozen local frame/tetrad and covector panel;
- gauge-map rank and explicit gauge annihilation checks;
- independent symbolic vs finite-difference or automatic-differentiation construction of the principal symbol where feasible;
- coordinate/frame covariance of characteristic rank/invariants;
- `c6=0` control reproducing the already-authorized two-derivative result;
- Weyl-blind/conformally-flat control derived at the equation level;
- sign/normalization reparameterization checks keeping `c6` symbolic;
- exceptional covectors and rank-deficient strata searched counterexample-first;
- no interpretation of finite panel as a global hyperbolicity theorem.

## Possible future terminal logic

Exact PASS/FAIL thresholds and classifications must be prospectively preregistered only after the full `E_6` object is authorized. Qualitatively:

- **PASS_SCOPED** may establish absence of additional physical principal branches / preservation of a controlled hyperbolic reduced symbol only on a frozen finite background/covector panel;
- **SCIENTIFIC_FAIL** may be justified by a reproducible physical extra branch, non-hyperbolic reduced symbol, unavoidable rank pathology, or covariance inconsistency of the correctly derived object;
- **BLOCKED_OBJECT_DEFINITION** is required if the full functional derivative or gauge-reduced symbol cannot be defined unambiguously;
- **INVALID** is required for failed controls/provenance/implementation.

## Dependency lock

Do **not** preregister or run this as authoritative science while the current functional-variation chain is unresolved. A terminal Iter053T diagnostic PASS alone is insufficient; a distinct full corrected A4+B2+C2 replacement/full functional-variation authority must first establish the required `E_6` object.

## Claim ceiling

This audit authorizes no new physics claim. `theory established=0%`; `c6` remains symbolic/unfixed; `beta=1` remains unauthorized; no quantum amplitude/measure, unitarity, UV completion, GR recovery or experimental claim follows.