# Iter055K preregistration — raw one-particle L2 to finite-B3 boundary restriction

Date: 2026-09-14
Gate: `ITER055K-RAW-L2-TO-FINITE-B3-BOUNDARY-RESTRICTION`

## Frozen question
Can the already-defined regular one-particle characteristic Hilbert state of Iter007-G6F be mapped, without adding any new smearing, bandlimit, detector profile, Sobolev regularity, UV cutoff, vacuum/Fock completion or full-configuration dynamics, to the finite shared-B3 metric/connection boundary variables of G6C/G6E by the natural linearized field restriction/evaluation map, with a well-defined bounded/norm-controlled map on the actual Hilbert completion?

## Frozen source objects
- One-particle domain: `H_char(G)=direct_integral_{N_G^+} dmu_G(k) P_(G,k)` from G6F, with invariant future-null-cone measure.
- Boundary target: finite shared-B3 metric/connection restriction variables from G6C/G6E.
- Linearized candidate bridge under test only: reconstruct/evaluate the characteristic field (and, for connection data, its first derivative) at the finite B3 vertices/edges from its null-cone amplitudes.

No alternative bridge may be substituted after the result.

## Frozen analytic obligations
1. Check whether the raw point/reconstruction functional is defined on `L2` equivalence classes and bounded with respect to the G6F Hilbert norm.
2. For the momentum-to-field reconstruction functional `a -> integral a(k) e^{ik.x} dmu_G(k)`, test the Riesz/Cauchy-Schwarz criterion: the evaluation kernel must belong to the relevant `L2(dmu_G)` dual class.
3. Use the actual unbounded future-null-cone measure; do not insert compact momentum support or a cutoff unless already source-defined.
4. For connection/derivative boundary data, also test the extra momentum weight introduced by differentiation.
5. Distinguish failure of this raw map from impossibility of every overlap construction. A smeared/test-function or stronger-regularity bridge may still exist but would be additional structure requiring a new prospective gate.
6. Do not use finite numerical sampling as proof of boundedness on the Hilbert completion.

## Frozen classifications
- `PASS_SCOPED_ITER055K_RAW_L2_BOUNDARY_RESTRICTION_BOUNDED_AND_SOURCE_DEFINED` only if the source-defined reconstruction/restriction is a well-defined bounded map on the actual G6F Hilbert completion, including the boundary variables required by the B3 target.
- `FAIL_SCOPED_ITER055K_RAW_L2_BOUNDARY_POINT_RESTRICTION_NOT_BOUNDED__SMEARING_OR_REGULARITY_REQUIRED` if the natural point/reconstruction functional is not well-defined/bounded on the raw G6F `L2` completion, so an additional smearing/regularity/bandlimit object is mathematically required.
- `INVALID_PROVENANCE_ITER055K_SOURCE_MEASURE_OR_TARGET_NOT_FIXED` only if the frozen source formulas cannot be recovered consistently enough to apply the functional-analytic test.

## Interpretation ceiling
A FAIL would reject only the naive raw `L2 -> pointwise finite-boundary data` bridge. It would not prove no sector overlap exists. It would identify the minimal mathematical type of new structure needed before exact Iter009-G6 recovery can be used as a boundary-dynamics kill test. No boundary channel, beta, c6, Weyl3 treatment, regulator removal, full unitarity, UV completion, GR recovery, experiment or theory establishment follows.

No GitHub Actions run is preregistered because this is an exact functional-analytic gate.
