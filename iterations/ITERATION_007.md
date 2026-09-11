# QGR Iteration 007 — All-Orders Local Gravity and Distinguishability

Date: 2026-09-12
Status: `COMPLETE / MODEL_SIDE_BROADBAND_OBSERVABLE_CLOSED_SCOPED / ABSOLUTE_SCALE_BOUNDARY_EXPLICIT`
Current task completion: **100%**
Candidate-program readiness: **87%**
Active candidate: **QGR-L1**
Theory established: **0%**

Readiness is an internal construction-roadmap metric, not a probability of correctness or fraction of quantum gravity solved.

## Objective

1. close the local nonlinear gravitational action in the metric-only two-derivative class;
2. derive the first QGR-specific finite-refinement correction without adding a novelty coefficient;
3. derive network composition, overlapping-region gluing and physical two-mode transport/readout from the same realization;
4. produce a normalized curved broadband comparator;
5. determine whether its absolute physical magnitude is fixed by the current microscopic normalization chain.

All five questions are now answered in scope. The fifth is closed **negatively**: the current realization leaves one dimensionless microscopic action normalization unfixed.

## G1 — all-orders local two-derivative action

Within the metric-only local class with at most two derivatives, the unique nontrivial action density is

`a sqrt(|det G|) R[G]`

modulo a boundary term and the zero-cosmological active branch. This is the all-orders continuation of the independently derived QGR quadratic/cubic/quartic terms.

Classification:
`PASS_SCOPED_UNIQUE_ALL_ORDERS_LOCAL_METRIC_ONLY_TWO_DERIVATIVE_ACTION_WITH_ZERO_COSMOLOGICAL_BRANCH`.

Record: `results/ITER007_G1_ALL_ORDERS_TWO_DERIVATIVE_LOCAL_ACTION.md`.

## G2-G5 — first finite-history correction and network scaling boundary

For the 24 B4 orderings the exact ordering covariance has spectrum

`1/3 x3 ; 5/3 x3`,

and after tracing the normalized history register

`Delta E(rho)=(h^4/8) C_ab [K_a,[K_b,rho]] + O(h^5)`.

The finite-cell covariance is microscopic `S4`, not exact continuous Lorentz. On a fixed causal path the accumulated correction is `O(L h^3)` and the normalized purity-loss form is positive.

A naive same-carrier four-volume accumulation is only a stress bound. Later path-groupoid analysis proves that face-neighbour B4 cells are overlapping supports rather than serial history-channel steps.

## G6A-G6C — history composition, finite local net and physical quotient

Runs `34653478008`, `34654604762`, and `34655130571` establish in scope:

- true serial B4 diagonals have the exact product-uniform `24^-n` branch law;
- face-neighbour B4 cells share a complete B3 face but their opposite-vertex 24-history morphisms are not serially composable;
- the minimal regular two-cell configuration glues as the exact fiber product `352+352-152=552` over common B3 data;
- cylindrical multiplication algebras intersect on the shared B3 subalgebra;
- quantum boundary matching is relative/direct-integral gluing rather than an independent tensor product duplicating the boundary;
- finite frame pullback maps `ker H / im R` canonically between two-dimensional physical characteristic fibers;
- no arbitrary phenomenological `2x2` polarization projector is required or permitted.

## G6E-G6H — curved physical pairing and full broadband comparator

Runs:

- G6E `34657301235`: 5 lanes + aggregate SUCCESS;
- G6F `34657631926`: 3 lanes + aggregate SUCCESS;
- G6G `34657905251`: 3 lanes + aggregate SUCCESS;
- G6H `34658915788`: 4 lanes + aggregate SUCCESS.

The earlier `C` versus `C^-1` same-realization convention boundary was repaired explicitly and the finite torsion/history construction rerun on the covariant seed `E=C^-1`.

A trace-reversed covariant bilinear has the four derivative-gauge directions as its exact radical on the six-dimensional characteristic kernel and leaves a positive two-dimensional quotient. This supports a common positive characteristic direct-integral Hilbert space on the regular one-particle/readout domain.

Normalized packet, polarization/Wigner and full momentum-dependent broadband calculations all retain a leading `O(h^4)` history-mixture loss on repaired G9.

Full broadband exponents:

- radial profile `m0`: `4.034237010354219`;
- radial profile `m1`: `4.034735702727535`;
- envelope-only control: `4.092362452141089`;
- fixed linear spin-2: `4.05492344294805`;
- definite helicity: `4.059195890628427`.

The radial null-energy integral is analytic, so no arbitrary UV momentum cutoff enters this normalized comparator. Coefficients are explicitly preparation/readout dependent; no universal decoherence constant is claimed.

Record: `results/ITER007_G6E_G6H_CURVED_BROADBAND_OBSERVABLE_CLOSURE.md`.

## G7A — microscopic scale identifiability

Corrected run `34659176245`: 4 lanes + aggregate SUCCESS.

Four-dimensional refinement matching gives

`a_cont = c_geom kappa/h^2`.

The logarithmic normalization Jacobian in `(log kappa,log h)` is `[1,-2]`, rank one, leaving

`h -> lambda h`, `kappa -> lambda^2 kappa`

unresolved. The continuum GR normalization is unchanged while the leading history correction changes as `lambda^4`.

Classification:
`BLOCKED_SCOPED_ABSOLUTE_MICROSCOPIC_SCALE_NOT_IDENTIFIABLE_FROM_CURRENT_QGR_NORMALIZATION_CHAIN`.

Record: `results/ITER007_G7A_MICROSCOPIC_SCALE_IDENTIFIABILITY.md`.

## G7B — immediate scale-fixing routes fail closed

Run `34659478647`: 4 lanes + aggregate SUCCESS.

Results:

- the existing history isometry/CPTP normalization is independent of the overall real action coefficient `kappa`; it fixes branch modulus `1/sqrt(24)` but not the phase scale;
- the current Lorentzian configuration measure `|det G|^-5/2 d^10G` is exactly scale neutral;
- metric-only scalar covariance fixes the principal causal cone but leaves independent matter mass/nonminimal data;
- shared metric cones do not by themselves derive multi-species universality or a second physical scale relation.

Classification:
`BLOCKED_SCOPED_EXISTING_QGR_QUANTUM_NORMALIZATION_DOES_NOT_FIX_KAPPA_AND_METRIC_ONLY_MATTER_COVARIANCE_DOES_NOT_SUPPLY_A_DERIVED_SECOND_SCALE`.

## G7C — no derived nonzero refinement stop scale

Run `34659644866`: 4 lanes + aggregate SUCCESS.

Results:

- if `h` is a removed regulator, keeping continuum gravity normalization fixed requires `kappa~h^2`, while the leading history correction vanishes as `h^4`;
- current `Q_13` geometry is continuous and its invariant measure contains no minimum nonzero scale;
- naive canonical `T*Q_13` prequantization does not quantize `kappa` because the canonical symplectic form is exact;
- B4 incidence/history/S4 counts are dimensionless and unchanged by global physical rescaling.

Classification:
`BLOCKED_SCOPED_CURRENT_CCRC_QGR_HAS_NO_DERIVED_NONZERO_STOP_SCALE__H_IS_EITHER_REMOVED_REGULATOR_WITH_VANISHING_H4_EFFECT_OR_REQUIRES_A_NEW_PHYSICAL_DISCRETENESS_PRINCIPLE`.

## G7D — one dimensionless microscopic coupling remains

Run `34659779779`: 4 lanes + aggregate SUCCESS.

Restore physical units and define

`g = kappa/hbar`,

`ell_Q^2 = hbar/a_cont`.

Then

`h^2 = c_geom g ell_Q^2`.

Thus, once the continuum normalization and `hbar` are specified, the unresolved freedom is equivalent to **one dimensionless microscopic coupling `g`**, not an independently arbitrary new dimensionful length.

A generic leading broadband effect can be written schematically as

`loss = C_prep c_geom^2 g^2 (ell_Q^2 R_eff)^2 + ...`.

Pure classical vacuum gravity does not operationally calibrate the overall Einstein-Hilbert coefficient by itself, and no authoritative current QGR rule fixes `g=1` or any other value. Choosing units `hbar=1` does not fix a dimensionless coupling.

Classification:
`PARTIAL_SCOPED_ABSOLUTE_SCALE_AMBIGUITY_REDUCED_TO_ONE_DIMENSIONLESS_MICROSCOPIC_COUPLING_G_KAPPA_OVER_HBAR__G_REMAINS_UNFIXED_AND_MATTER_CLOCK_CALIBRATION_OPEN`.

Record: `results/ITER007_G7B_G7D_SCALE_BOUNDARY.md`.

## Iter007 conclusion

The distinguishability problem is closed in its intended scope:

- **positive:** QGR-L1 has a normalized, cutoff-free, curved broadband two-mode 24-history comparator for specified preparations, with robust tested leading order `O(h^4)`;
- **negative:** the current CCRC/QGR realization does not derive a nonzero physical refinement stop scale or the remaining dimensionless microscopic action normalization `g`.

If `h` is only a regulator and is removed, the leading finite-history correction disappears and the scoped local continuum remains the Einstein-Hilbert/GR sector. A finite beyond-GR effect therefore requires a new prospectively derived physical-discreteness, relational-clock/matter, or nontrivial microscopic amplitude/symplectic principle.

This negative boundary is a completion result, not a reason to set `g=1` or `h=l_P` by convention.

## KMQGB synchronization

Latest observed KMQGB head: `d14e48f6790c49cca5b202dc227a179a9577819a`, Iter353-355. The GFT condensate child has a scoped dispersion-rigidity result, but its source/scope guard keeps the parent family nonterminal and explicitly forbids D7 promotion. `NEW_REQUIRED` remains unauthorized.

## Claim locks

- theory established remains `0%`;
- no experimental confirmation;
- no universal QGR decoherence coefficient;
- no absolute physical prediction until `g`/matter-clock calibration is derived or independently bounded;
- no identification `h=l_P` or `g=1` by convention;
- no arbitrary `2x2` polarization projector;
- no face-neighbour cells treated as serial history channels;
- no independent KMQGB pass;
- no claim all known models fail;
- no KMQGB `NEW_REQUIRED` authorization;
- no claim QGR is unique/correct as a full quantum-gravity theory.

## Progress accounting

- Iter007 completion: **100%**.
- Candidate-program readiness: **87%**.
- Theory established: **0%**.

Next stage: `Iter008 — Physical Scale and Relational Matter Reconstruction`.
