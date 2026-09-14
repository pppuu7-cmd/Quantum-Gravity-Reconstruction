# QGR Weyl^3 dynamical-treatment authority gap

Date: 2026-09-14

Status: **OBJECT-DEFINITION / DEPENDENCY AUDIT**, not a scientific PASS/FAIL gate.

## Question

If a future full corrected compact-support functional-variation gate establishes the metric Euler-Lagrange object associated with

`S6 = c6 * (six-derivative/EFT-order Weyl^3 correction)`,

what physical dynamical interpretation is authorized for stability and characteristic analysis?

Two inequivalent possibilities must not be conflated:

1. **Exact higher-derivative dynamics:** the corrected metric equation is solved as a fundamental fourth-order PDE, and additional roots/characteristic branches of its quartic principal polynomial are candidates for physical dynamical branches subject to gauge/constraint analysis.
2. **Perturbative EFT / order-reduced dynamics:** `c6` enters only as a controlled `O(h^4)` / `O(Gamma^2)` correction within a bounded expansion domain; high-frequency roots created by resumming the truncated higher-derivative equation are not automatically physical degrees of freedom, and stability must instead be posed on the order-reduced/perturbative evolution problem.

These define different physical objects and can yield different ghost/hyperbolicity interpretations.

## Existing authority

### Iter009-G2/G3: effective correction language and power counting

Iter009-G2 identifies six derivatives as the first potentially physical local vacuum correction after curvature-squared EOM redundancy, while explicitly keeping six-derivative microscopic matching open.

Iter009-G3 collapses the scoped parity-even Ricci-flat six-derivative operator shape to one Weyl-cubed direction and writes the correction as

`S6 = a_cont * c6 * h^4 * integral(I6)`,

with relative effect `c6 * Gamma^2 * (ell_Q^2 R_eff)^2`. It explicitly calls `c6` an unfixed coefficient competing at the same `O(h^4)` order as the history effect.

### Iter009-G4/G6: perturbative correction language but no order-reduction prescription

Iter009-G4 proves exact flat-Hessian decoupling and nonzero curved-background quadratic response. It describes the open object as a self-consistent curved `c6` correction.

Iter009-G6 states that a regular `c6 O(h^4)` per-cell correction accumulates as `O(c6 T h^3)` in the regular weak-curvature refinement regime and keeps `c6` as an unfixed UV-matching parameter.

These records strongly establish correction/Wilson/power-counting semantics, but they do not specify a physical order-reduction map for the corrected field equation.

### Iter010-G1/G4: Wilson direction and missing UV normalization

Iter010-G1 isolates a one-dimensional `c6` null direction left by lower-order microscopic authority. Iter010-G4 explicitly calls `c6` an independent six-derivative **Wilson direction** and forbids fixing it by lower-order normalization, phase composition, root-of-unity assumptions or homogeneous refinement.

This supports an effective-operator interpretation but still does not define whether the truncated corrected metric equation is to be evolved exactly or perturbatively/order-reduced.

### Iter051/052: variational object, not evolution prescription

Iter051C and Iter052 concern the exact variational identity/object for the Weyl-cubed density. Iter052 establishes a scoped 4D directional-variation certificate

`delta[sqrt(-g) W3] = H5^{ab} h_ab + partial_mu Theta^mu`

with symbolic `c6`.

This determines the candidate correction tensor in the tested scope, not the physical rule for treating the resulting higher-derivative equation beyond the truncation order.

## Finding

Current repository authority supports all of the following simultaneously:

- `Weyl^3` is the scoped unique parity-even six-derivative/Wilson operator direction in the stated Ricci-flat quotient;
- its coefficient is a genuine unfixed UV-matching parameter;
- its observable/local effect is power-counted as `O(h^4)` / `O(Gamma^2)` in the regular refinement regime;
- flat linearized propagation is blind to it, while nonzero-Weyl backgrounds activate its quadratic response;
- the repository is constructing its covariant variational tensor.

But the reviewed authority does **not** yet establish either:

- `EXACT_NONPERTURBATIVE_HIGHER_DERIVATIVE_EVOLUTION_AUTHORIZED`, or
- `PERTURBATIVE_ORDER_REDUCED_EVOLUTION_AUTHORIZED_WITH_EXPLICIT_REDUCTION_AND_VALIDITY_DOMAIN`.

Therefore a later observation of an additional quartic characteristic root cannot, by itself, be promoted to a physical ghost/new-DOF theorem; conversely, such roots cannot simply be discarded as EFT artifacts without a prospectively frozen order-reduction authority.

## Dependency classification

`MISSING_WEYL3_DYNAMICAL_TREATMENT_AUTHORITY`

This is an object-definition blocker for interpreting a future corrected principal-symbol calculation as a physical spectrum/stability verdict. It is not a refutation of the Weyl-cubed operator and does not block completing the current functional-variation gate.

## Highest-information resolution

After a valid full functional-variation authority exists, and before a physical ghost/hyperbolicity claim, prospectively freeze a **dynamical-treatment gate** that derives the treatment from the same QGR realization rather than choosing it post hoc.

A valid resolution must specify at least:

- exact vs perturbative status of the truncated `c6 Weyl^3` term;
- expansion/control parameter and validity domain if perturbative;
- whether and how order reduction is performed;
- which initial data are physical and how higher-time-derivative data are eliminated or retained;
- gauge/constraint compatibility;
- how `c6` remains symbolic/unfixed;
- what characteristic/stability observable is physically meaningful under that treatment;
- explicit PASS/FAIL/BLOCKED/INVALID and interpretation ceiling.

The gate must not select exact treatment because it gives a preferred spectrum, nor select order reduction merely to delete an unwanted branch.

## Consequence for the planned principal-symbol work

The analytic curvature-Hessian lemma remains useful: the raw unreduced linearized correction has a quartic high-frequency structure schematically `c6 Cbar k^4`, and a conformally-flat background is the clean Hessian null control. But until the dynamical-treatment authority is fixed, this raw symbol is a mathematical diagnostic rather than an automatically physical degree-of-freedom spectrum.

## Claim ceiling

No value or sign of `c6`, no ghost/no-ghost claim, no hyperbolicity theorem, no unitarity statement, no quantum-layer transition and no theory-establishment claim follows. `theory established=0%`; `beta=1` remains unauthorized.