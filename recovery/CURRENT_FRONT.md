# QGR Current Research Front

Updated: 2026-09-12
Active iteration: `Iter007`
Project phase: `MODEL_CONSTRUCTION_ACTIVE / MODEL_SIDE_BROADBAND_OBSERVABLE_CLOSED_SCOPED / ABSOLUTE_SCALE_BLOCKED`
Active roadmap stage: `R7 observable closure / R9 prediction-discrimination precursor`

## Canonical status

- Repository infrastructure readiness: **100%**
- Candidate-program readiness: **86%**
- Iter005 completion: **100%**
- Iter006 completion: **100%**
- Iter007 completion: **98%**
- Theory established: **0%**
- Lead architecture: `A / CCRC`
- Active candidate: `QGR-L1`
- Local metric-only two-derivative action: **all-orders PASS_SCOPED**
- Local action: `a integral sqrt(|det G|) R[G]`, zero-cosmological active branch
- Physical characteristic quotient: **2 modes**
- Regular state/measure/composition/refinement layer: **PASS_SCOPED**
- Strong-curvature path-groupoid transport: **PASS_SCOPED**
- Normalized 24-history instrument: **PASS_SCOPED**
- First history correction: **PASS_SCOPED, O(h^4)**
- Finite overlapping-region local net: **PASS_SCOPED**
- Positive curved two-mode quotient pairing: **PASS_SCOPED**
- Common target characteristic Hilbert: **PASS_SCOPED**
- Full cutoff-free broadband two-mode 24-history comparator for specified preparations: **PASS_SCOPED**
- Absolute physical microscopic scale `h`: **BLOCKED / not identified separately from kappa**
- Independent KMQGB pass: **NO**
- KMQGB `NEW_REQUIRED`: **NOT AUTHORIZED**

Readiness is an internal construction-roadmap metric, not probability of correctness.

## Established same-realization chain

`B4 relational seed`
`-> four derived directions + Lorentzian incidence form`
`-> Sym^2(W4) ten-component response`
`-> derivative gauge closure / no onsite mass`
`-> two physical characteristic modes`
`-> unique cubic + quartic self-coupling`
`-> all-orders metric-only two-derivative local action`
`-> Lorentzian configuration Hilbert / BRST operational algebra`
`-> refinement-connected finite torsion-free connection`
`-> path-groupoid transport`
`-> normalized 24-history instrument`
`-> O(h^4) finite-history correction`
`-> exact serial history branch law`
`-> finite B3 overlap fiber-product local net`
`-> canonical two-mode quotient descent`
`-> repaired C/E same-realization convention`
`-> positive covariant two-mode characteristic pairing`
`-> common characteristic direct-integral Hilbert`
`-> physical Wigner/polarization transport`
`-> cutoff-free full broadband two-mode comparator`
`-> microscopic-scale identifiability gate`.

No phenomenological noise coefficient, arbitrary 2x2 polarization projector, arbitrary cross-cell correlation, or Planck-scale identification has been inserted.

## G6E-G6H — curved physical/broadband observable closure

### G6E

Actions run `34657301235`: 5 lanes + aggregate SUCCESS.

The `C` versus `C^-1` convention boundary was repaired explicitly with `S=I-J/6`, `S^T C S=C^-1`. The finite G9 torsion/history construction was rerun using the covariant seed `E=C^-1`.

Repaired history-invariant refinement slopes remain approximately four:

- relative history trace: `4.0705480`;
- common-target null Gram: `4.0984388`;
- branch-pair barycentric rapidity scalar: `4.0685627`.

A trace-reversed covariant bilinear has the four derivative-gauge directions as its exact radical on the six-dimensional characteristic kernel and descends to a positive two-dimensional physical quotient. Regular positive boundary-measure disintegration over the shared B3 is also available without assuming conditional independence.

### G6F

Actions run `34657631926`: 3 lanes + aggregate SUCCESS.

A common positive target characteristic Hilbert is defined on the regular one-particle/readout domain. Two normalized packet families have exact overlaps

`2/(1+gamma)`

and

`4(2+gamma)/(3(1+gamma)^2)`.

Repaired-G9 history-mixture losses have slopes `4.0707806` and `4.0707012`, with fine-scale coefficient ratio approaching `4/3`. Thus the order is robust in this test but the coefficient is preparation dependent.

### G6G

Actions run `34657905251`: 3 lanes + aggregate SUCCESS.

Relative Lorentz generator RMS scales with exponent `2.0290`, while two independent quadratic Lorentz-algebra Casimirs and the finite trace defect scale near exponent `4.05`. In a specified relational detector section, Wigner-angle spread is `O(h^2)` and fixed linear spin-2 overlap loss is `O(h^4)`. The specified narrow-packet combined loss exponent is `4.0051`.

### G6H

Actions run `34658915788`: 4 lanes + aggregate SUCCESS.

The radial future-null-cone integral is analytic, so no arbitrary UV momentum cutoff is used. For every target null direction and every history, the branch-dependent source momentum and physical little-group/spin-2 transport are recomputed.

Full broadband two-mode history-mixture loss slopes:

- `m0`: `4.0342370`;
- `m1`: `4.0347357`.

For `m0`, polarization-preparation slopes are:

- envelope-only `4.0923625`;
- linear `4.0549234`;
- helicity `4.0591959`.

Therefore the current strongest model-side distinction from the GR continuum sector is a normalized finite-history correction whose tested refinement order is robustly `O(h^4)`, while the numerical coefficient is preparation/readout dependent.

Record: `results/ITER007_G6E_G6H_CURVED_BROADBAND_OBSERVABLE_CLOSURE.md`.

## G7A — microscopic-scale identifiability obstruction

First run `34659076333` failed closed because a lightweight script imported NumPy although the workflow omitted that dependency. The criterion was unchanged; after removing the unnecessary dependency, run `34659176245` completed 4 lanes + aggregate SUCCESS.

Four-dimensional refinement power counting gives

`a_cont = c_geom * kappa / h^2`.

In `(log kappa, log h)` coordinates the continuum normalization Jacobian is `[1,-2]`, rank one. The exact unresolved direction is

`h -> lambda h`,
`kappa -> lambda^2 kappa`.

The GR normalization is unchanged, while a leading `h^4` history observable changes as `lambda^4`.

The authoritative microscopic QGR action still retains one free overall normalization `kappa`; no existing later result derives an absolute physical `h`.

Classification:
`BLOCKED_SCOPED_ABSOLUTE_MICROSCOPIC_SCALE_NOT_IDENTIFIABLE_FROM_CURRENT_QGR_NORMALIZATION_CHAIN`.

Record: `results/ITER007_G7A_MICROSCOPIC_SCALE_IDENTIFIABILITY.md`.

## Active blocker / next gate

`MISSING_DERIVED_MICROSCOPIC_NORMALIZATION_OR_SECOND_INDEPENDENT_PHYSICAL_SCALE_OBSERVABLE`

Active gate:
`QGR-ITER007-G7B-MICROSCOPIC-NORMALIZATION-OR-MATTER-SECOND-SCALE`

Prospective routes:

1. derive `kappa` from the existing microscopic quantum/amplitude/measure realization; or
2. derive universal matter/detector coupling that supplies a second independent scale relation.

Fail closed if either route requires setting `h=l_P`, fixing `kappa` by convention, or fitting the scale to a desired effect.

## KMQGB synchronization

Latest observed KMQGB head: `d14e48f6790c49cca5b202dc227a179a9577819a`, Iter353-355. The GFT condensate child has a scoped dispersion-rigidity result, but its source/scope guard keeps the parent family nonterminal and explicitly forbids D7 promotion. `NEW_REQUIRED` remains unauthorized.

## Claim locks

- no experimental confirmation;
- no universal broadband/decoherence coefficient;
- no absolute numerical phenomenology until `h/kappa` separation is derived;
- no `h=l_P` identification by convention;
- no arbitrary 2x2 polarization projector;
- no face-neighbour cells treated as serial history channels;
- no independent KMQGB pass;
- no claim all known models fail;
- no `NEW_REQUIRED` authorization;
- no claim QGR is unique/correct as a full quantum-gravity theory.

## Recovery order

1. `recovery/state.json`
2. `recovery/CURRENT_FRONT.md`
3. `iterations/ITERATION_007.md`
4. `results/ITER007_G7A_MICROSCOPIC_SCALE_IDENTIFIABILITY.md`
5. `results/ITER007_G6E_G6H_CURVED_BROADBAND_OBSERVABLE_CLOSURE.md`
6. `results/ITER007_G6C_LOCAL_NET_AND_PHYSICAL_QUOTIENT_DESCENT.md`
7. `results/ITER007_G6B_OVERLAPPING_CELL_GLUING_AND_CURVED_HISTORY_SPREAD.md`
8. `iterations/ITERATION_006.md`
9. `docs/CONSTITUTION.md`
10. current KMQGB scoped deltas and authoritative front
