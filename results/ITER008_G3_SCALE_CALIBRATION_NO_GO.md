# QGR Iter008 G3 — scale calibration no-go across five immediate routes

Date: 2026-09-12
Status: `BLOCKED_SCOPED_IMMEDIATE_CLOCK_DISCRETENESS_TOPOLOGY_AND_MINIMAL_MATTER_ROUTES_DO_NOT_FIX_G`

GitHub Actions run `34661538161`: five lanes + aggregate `SUCCESS`.

## 1. Rank tick versus proper time

For the derived incidence form `C=J-I`, every elementary Boolean cover vector `e_i` is exactly null:

`e_i^T C e_i = 0`.

The symmetric rank direction `n=(1,1,1,1)` is timelike with

`n^T C n = 12`,

and the barycentric mean of the four possible covers, `n/4`, has dimensionless norm `3/4`. The dual rank covector has positive norm `4/3` under `E=C^-1`.

Thus the intrinsic rank clock has a derived timelike coarse direction, but **one actual unit-rank history step is null**. Assigning a nonzero proper duration to one tick therefore requires an additional coarse/readout prescription and still carries the unresolved physical cell scale `h`.

Classification:
`PARTIAL_SCOPED_RANK_CLOCK_HAS_DERIVED_TIMELIKE_SYMMETRIC_DIRECTION_BUT_ELEMENTARY_UNIT_TICKS_ARE_NULL__NO_UNIQUE_PROPER_TIME_PER_TICK`.

## 2. Configuration-space topology and topological prequantization

The Lorentzian symmetric-form space `Q_{1,3}` deformation-retracts to the choice of its unique positive Euclidean eigenspace line. The positive eigenvalue and the negative-definite operator on the orthogonal 3-space form a contractible fiber. Therefore

`Q_{1,3} ~ RP^3`.

The cellular chain complex of `RP^3` has one cell in each degree `0..3` and integer boundaries

`d1=0`, `d2=2`, `d3=0`.

Hence

- `H_2(RP^3;Z)=0`;
- `H^2(RP^3;Z)=Z2` torsion;
- `H^2_dR(RP^3)=0`.

There is therefore no nonzero continuous real two-form cohomology class whose integrality could quantize a positive real microscopic coupling `g`. The `Z2` torsion can at most support a discrete sign/flat-line-bundle sector.

Classification:
`FAIL_SCOPED_CONTINUOUS_TOPOLOGICAL_PREQUANTIZATION_ROUTE_FOR_FIXING_G__ONLY_Z2_TORSION_CLASS_REMAINS`.

## 3. Minimal intrinsic-clock dynamics

The minimal Hermitian nearest-neighbour rank-translation-invariant generator has, after removing a common phase/energy offset, one physical frequency scale `J_clock` multiplying the dimensionless dispersion

`lambda(theta)=2-2 cos(theta)=4 sin^2(theta/2)`.

Rescaling `J_clock` leaves all clock symmetries and dimensionless spectral ratios unchanged while changing every physical energy gap. The exact G2 branch/isometry normalization fixes moduli, not this phase scale.

Classification:
`BLOCKED_SCOPED_MINIMAL_RANK_TRANSLATION_INVARIANT_CLOCK_DYNAMICS_HAS_ONE_FREE_FREQUENCY_SCALE_AFTER_REMOVING_COMMON_PHASE`.

## 4. Intrinsic clock as matter

For a freely normalized scalar, the overall kinetic coefficient can be removed by a field rescaling and supplies no independent gravity calibration. If the scalar is instead identified with the intrinsic rank clock, unit rank increments fix its field normalization, so the kinetic coefficient `Z_tau` becomes a genuine physical coefficient and cannot be scaled away.

Nothing in the existing covariance/incidence construction fixes `Z_tau`. The clock-as-matter route therefore adds a new normalization instead of determining the gravitational `g`.

Classification:
`BLOCKED_SCOPED_METRIC_COVARIANT_RELATIONAL_MATTER_DOES_NOT_FIX_G__IDENTIFYING_THE_INTRINSIC_RANK_CLOCK_AS_A_PHYSICAL_SCALAR_MAKES_ITS_KINETIC_NORMALIZATION_A_NEW_FREE_PARAMETER`.

## 5. Natural B4 spectral discreteness

The B4 Hasse graph is the four-cube. Its exact graph-Laplacian spectrum is

`0,2,4,6,8`

with multiplicities

`1,4,6,4,1`.

These are dimensionless combinatorial eigenvalues. A physical Laplacian carries

`lambda_phys=lambda_B4/h^2`.

Therefore B4 discreteness fixes spectral ratios but not an absolute length or a nonzero refinement stop.

Classification:
`BLOCKED_SCOPED_B4_DISCRETE_SPECTRUM_FIXES_DIMENSIONLESS_RATIOS_BUT_NOT_AN_ABSOLUTE_LENGTH_OR_REFINEMENT_STOP`.

## Consolidated result

`BLOCKED_SCOPED_INTRINSIC_CLOCK_AND_B4_DISCRETENESS_DO_NOT_CALIBRATE_PHYSICAL_SCALE__CURRENT_Q13_TOPOLOGY_HAS_NO_CONTINUOUS_H2_PREQUANTIZATION_CLASS__MINIMAL_CLOCK_OR_CLOCK_MATTER_DYNAMICS_INTRODUCE_A_NEW_FREE_SCALE`.

The active blocker is now narrower:

`MISSING_NONTRIVIAL_SAME_REALIZATION_QUANTUM_GEOMETRIC_OR_MATTER_PRINCIPLE_THAT_RELATES_THE_CLOCK_ENERGY_SCALE_TO_G_WITHOUT_ADDING_A_NEW_FREE_NORMALIZATION`.

## Next gate

`QGR-ITER008-G4-INTERACTING-CLOCK-GRAVITY-CONSTRAINT-AND-DISCRETE-QUANTIZATION-AUDIT`

The next tests must move beyond free clock/matter additions:

1. derive/audit a common clock-gravity constraint and determine whether deparametrization fixes a relative normalization or merely moves the free parameter;
2. close the remaining fixed geometric conversion coefficient in the frozen QGR normalization if possible;
3. test whether the `Z2` topology yields a genuine second global quantization sector and whether the current scalar Hilbert choice selected one without derivation;
4. test whether loop/history phase consistency can quantize `g` or whether continuous curvature holonomy forbids that inference.

## Claim locks

No minimum length, Planck-time tick, `g=1`, or absolute beyond-GR rate is derived by G3.
