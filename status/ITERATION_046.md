# QGR Iter046 — exact nonlinear radiative pp-wave gate

Date: 2026-09-12
Status: `PREREGISTERED_BEFORE_IMPLEMENTATION`
Gate: `ITER046-QGR-L1-EXACT-NONLINEAR-PPWAVE-RADIATIVE-SECTOR`

## Scientific question
Does the already reconstructed **all-orders local two-derivative QGR-L1 action**, without linearizing about the flat incidence seed and without inserting a TT curvature solution as a dynamical input, admit a nontrivial exact finite-amplitude curved radiative vacuum sector and reject nearby non-vacuum controls?

This gate is deliberately stronger and different from Iter005-G3. G3 established only local weak-background **principal-symbol** cone/mode stability. Iter046 tests the full nonlinear Euler-Lagrange tensor of the already fixed all-orders local action on exact curved radiative configurations.

## Frozen authority
Existing authority fixed before this gate:
- Iter004: QGR-L1 quadratic branch and two physical massless modes;
- Iter005 G1/G2: unique cubic and quartic two-derivative Noether continuation;
- Iter005 G3: weak-background principal-symbol stability only;
- Iter007 G1: unique all-orders local metric-only at-most-two-derivative action
  `S_local = a ∫ sqrt(|det G|) R[G]`, zero cosmological branch;
- Iter043–045: independent radiative observable geometry, linear end-to-end QGR-L1 TT dynamics, and relative two-polarization residue degeneracy.

The production code must construct the metric, inverse metric, Levi-Civita connection, Riemann/Ricci/scalar curvature and Euler-Lagrange tensor directly from this action geometry. It may not hard-code the vacuum field equation for the chosen profiles as the solver.

## Frozen metric family
Use Brinkmann coordinates `(u,v,x,y)` and the Lorentzian response metric

`ds^2 = 2 du dv + H(u,x,y) du^2 + dx^2 + dy^2`.

The gate freezes several transverse profile families before implementation.

Harmonic transverse bases:
- `P2 = x^2-y^2`;
- `X2 = 2xy`;
- `P3 = x^3-3xy^2`;
- `P4 = x^4-6x^2 y^2+y^4`.

Frozen longitudinal polynomials are drawn from:
- `f0(u)=1`;
- `f1(u)=1+u`;
- `f2(u)=1+u+u^2/3`;
- `f3(u)=1-u/2+u^3/5`.

Frozen rational finite amplitudes are drawn from `{1/20, 1/10, 1/5, 1/2, 3/4}`. No small-amplitude limit is used to define PASS.

## Frozen streams
### A — exact finite-amplitude nonlinear vacuum lanes: 12
Twelve predetermined combinations of harmonic transverse basis, longitudinal polynomial and finite rational amplitude.

PASS per lane requires, by direct symbolic geometry:
1. metric determinant is nonzero and Lorentzian at the frozen representative point;
2. the complete Euler-Lagrange/Einstein tensor of the all-orders two-derivative action simplifies identically to zero;
3. at least one Riemann component is symbolically nonzero, excluding the flat solution;
4. no perturbative truncation in amplitude is used.

### B — non-harmonic falsification controls: 6
Use profiles containing `N2=x^2+y^2`, optionally plus a frozen harmonic component.

PASS per lane requires:
1. the direct Euler-Lagrange tensor is **not** identically zero;
2. all components except the expected null-null component vanish after symbolic simplification;
3. the nonzero component agrees identically with `-1/2*(∂_x^2 H + ∂_y^2 H)` as an independently evaluated diagnostic;
4. the transverse Laplacian is symbolically nonzero.

If these controls accidentally vanish, the whole gate is `CONTROL_INVALID_NONLINEAR_PPWAVE_GATE`.

### C — held-out polarization/superposition closure: 6
Use frozen rational mixtures `P2 + λ X2` with `λ in {0,1/2,-2/3,1,3/2,-1/3}`, paired with frozen longitudinal profiles/amplitudes not reused lane-for-lane from A.

PASS requires exact zero Euler-Lagrange tensor and nonzero curvature in every lane. No fitted rotation or amplitude parameter is allowed.

### D — exact finite-amplitude curvature scaling: 6
For a frozen harmonic mixed profile containing quadratic and higher harmonic pieces, compare two finite nonzero rational amplitudes `a,b`.

PASS requires:
1. both configurations solve the exact Euler-Lagrange tensor identically;
2. the complete coordinate Riemann tensor satisfies `R[b] = (b/a) R[a]` identically component-by-component for the frozen pp-wave family;
3. curvature is nonzero.

This is an exact finite-amplitude statement for this family, not a perturbative slope fit.

### E — coordinate-covariance anti-artifact lanes: 4
Apply four frozen invertible rational **constant linear coordinate transformations** to selected harmonic pp-wave configurations, transform the metric as a covariant tensor, and recompute the full connection/curvature/Euler-Lagrange tensor from scratch in the transformed chart.

PASS requires exact zero transformed Euler-Lagrange tensor, nonzero transformed curvature, and nonzero Jacobian determinant. This guards against a special-coordinate implementation artifact.

Total: **34 scientific lanes + aggregate**. `fail-fast: false`.

## Frozen terminal classification
Full PASS only if all 34 lanes are present, all controls are valid and all lane criteria pass:

`PASS_SCOPED_QGR_L1_EXACT_FINITE_AMPLITUDE_NONLINEAR_PPWAVE_RADIATIVE_SECTOR`

If B controls are invalid:

`CONTROL_INVALID_NONLINEAR_PPWAVE_GATE`

Otherwise any scientific lane failure:

`PARTIAL_OR_FAIL_QGR_L1_NONLINEAR_PPWAVE_RADIATIVE_SECTOR`

No threshold or profile may be changed after the production trigger to rescue a result.

## Interpretation locks
Even a full PASS establishes only an exact nonlinear **special radiative family** inside the already fixed local two-derivative QGR-L1 sector. It does not establish generic strong-field stability, binary-merger dynamics, global hyperbolicity, nonlinear stability of pp-waves, quantum amplitudes, quantum unitarity, an absolute action sign, experimental confirmation, `beta`, or `c6`.

The unfixed `c6 Weyl^3` operator is deliberately excluded from the dynamical equation in this gate; a later independent gate may test how that higher-derivative correction acts on a curved radiative background without assigning it an unauthorized numerical coefficient.

`theory_established_pct` must remain `0%` regardless of Iter046 outcome.