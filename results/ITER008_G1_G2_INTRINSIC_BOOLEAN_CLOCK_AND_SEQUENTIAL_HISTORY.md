# QGR Iter008 G1-G2 — intrinsic Boolean clock and sequential history closure

Date: 2026-09-12
Status: `PASS_SCOPED_CLOCK_AND_SEQUENTIAL_HISTORY / PHYSICAL_TICK_SCALE_OPEN`

## Scope

This record asks whether the existing B4 relational ontology already contains a non-arbitrary internal clock, and whether the normalized 24-history quantum instrument factorizes exactly with respect to that clock. It does **not** assume that one clock tick is a physical proper-time interval.

## G1 — intrinsic Boolean rank clock

GitHub Actions run `34660061343`: four lanes + aggregate `SUCCESS`.

Define the Boolean rank

`tau(S)=|S|`.

Within the tested class of S4-invariant scalar functions on B4 satisfying `tau(empty)=0` and disjoint-union additivity, the solution space is one-dimensional and is spanned by rank. Fixing unit elementary increment gives exactly `tau(S)=|S|`.

At the symmetric Lorentz seed, the rank gradient is the S4-symmetric direction `(1,1,1,1)`. The complementary sum-zero sector is three-dimensional and has the opposite sign, giving the exact `1+3` causal decomposition already present in the QGR incidence geometry. Fixed-rank level sets are antichains.

All 24 maximal B4 histories have the same clock profile

`0 -> 1 -> 2 -> 3 -> 4`.

Rank adds exactly across true serial B4 cells. The integer serial clock has compact dual `U(1)` quasi-frequency, but converting that dimensionless phase to physical energy still requires a physical tick duration.

Classification:

`PASS_SCOPED_INTRINSIC_BOOLEAN_RANK_CLOCK_DERIVED_UNIQUELY_IN_ADDITIVE_S4_CLASS_WITH_TIMELIKE_1_PLUS_3_CAUSAL_STRUCTURE_AND_EXACT_SERIAL_COMPOSITION__PHYSICAL_TICK_SCALE_REMAINS_OPEN`.

## G2 — clock-conditioned history law and sequential isometry

GitHub Actions run `34660219520`: four lanes + aggregate `SUCCESS`.

Condition the uniform 24-history law on rank. At rank `r`, exactly `4-r` unused elementary directions remain, so

`P(next direction | r)=1/(4-r)`.

The coherent one-tick moduli are therefore

`1/sqrt(4), 1/sqrt(3), 1/sqrt(2), 1`,

and factorize exactly to

`1/sqrt(4) * 1/sqrt(3) * 1/sqrt(2) * 1 = 1/sqrt(24)`.

Thus the previously derived global normalized history amplitude is exactly the product of intrinsic-clock one-step isometries. Clock-conditioned prefixes and suffixes are compatible with the established path-groupoid composition law.

A separate phase audit shows that an S4-invariant **clock-only** edge phase is removable by rank-slice vertex rephasings. Therefore the scalar rank clock does not supply an autonomous physical Hamiltonian phase. Nontrivial phases must still come from the geometry/QGR action-connection sector or from a new independently derived matter/symplectic sector.

Classification:

`PASS_SCOPED_INTRINSIC_RANK_CLOCK_GIVES_EXACT_SEQUENTIAL_BRANCH_MEASURE_AND_ISOMETRY_FACTORIZATION_COMPATIBLE_WITH_PATH_COMPOSITION__CLOCK_ALONE_HAS_NO_NONTRIVIAL_PHYSICAL_PHASE`.

## Consequence

The current CCRC/QGR realization now contains an intrinsic relational ordering clock and an exact clock-conditioned decomposition of its 24-history quantum instrument. This removes an arbitrary choice of clock variable, but it **does not** fix the physical duration of one rank tick, the microscopic action normalization `g=kappa/hbar`, or a nonzero refinement stop scale.

## Next gate

`QGR-ITER008-G3-CLOCK-GEOMETRY-TOPOLOGICAL-QUANTIZATION-AND-MATTER-CALIBRATION`

1. test whether an elementary rank increment can be calibrated from the derived Lorentzian geometry rather than from a convention;
2. test whether the topology/symplectic structure of the Lorentzian configuration space can quantize `g`;
3. test whether the most economical clock/matter dynamics introduces a new normalization instead of fixing the existing one;
4. preserve the scale blocker if all routes remain dimensionless or normalization-degenerate.

## Claim locks

- rank time is not yet physical proper time;
- one rank tick is not identified with Planck time;
- `g=1` is not derived;
- no new experimental prediction follows solely from the clock factorization;
- KMQGB `NEW_REQUIRED` remains unauthorized.
