# D5 canonical-lattice cache equivalence — frozen infrastructure contract

Date: 2026-09-14

Status: **NON-SCIENTIFIC IMPLEMENTATION-EQUIVALENCE CONTROL**. This gate cannot classify Iter053T/Iter053U or change any QGR scientific result. Active authoritative runs are not modified.

## Purpose

Test whether the historical nested five-point `direct_D5` / `assemble_minus5` implementation can be replaced in a later, separately frozen scientific production by an exact canonical-lattice cache that evaluates each unique P/Weyl stencil point once.

The historical implementation requests about 290 P/Weyl evaluations per H5 evaluation; the exact nested stencil contains 129 unique canonical integer lattice points. The intended optimization changes evaluation reuse only, not the finite-difference formula.

## Frozen implementation identity

Historical reference:
`code/qgr_iter051c_d2n_near_null.py::assemble_minus5`

Candidate cached implementation must:

1. represent every stencil point as integer offset `n in Z^4` and coordinate `x+h*n`;
2. build the complete nested five-point offset set before any H/D reduction;
3. compute geometry and projected Weyl-P object once per unique offset;
4. reconstruct every inner first derivative with exactly the coefficients `(-1,8,-8,1)/(12h)` at offsets `(+2,+1,-1,-2)`;
5. reconstruct every outer derivative with the same coefficients;
6. use the same `b0.first_cov`, connection terms, algebraic A/I terms and final sign `A+I-2 sqrt(-g) D` as the historical implementation;
7. use no interpolation, fitted coefficient, altered step or changed tensor convention.

## Frozen panel

Use H5 derivative step exactly `h=5e-4`.

Use every Iter053R scientific metric lane once at each of two fixed coordinate points:

- point P0 = `(0,0,0,0)`;
- point P1 = `(0.04,-0.03,0.025,-0.02)`.

Matrix:

- A0,A1,A2,A3 × P0/P1 = 8 lanes;
- B0,B1 × P0/P1 = 4 lanes;
- C0,C1 × P0/P1 = 4 lanes.

Total: **16 independent lanes**, `fail-fast:false`.

Metric seeds/constructors are inherited exactly from Iter053R lane identities. Perturbations are irrelevant to this D5 object and are not used to select points.

## Frozen validity controls per lane

A lane is INVALID if:

- historical or cached output contains non-finite values;
- the historical `extended_controls(metric,x)` signature/inverse control fails;
- maximum inverse residual from that control exceeds `3e-11`;
- cached unique P/Weyl evaluation count is not exactly `129`;
- the cache offset set is not complete/unique;
- center cached metric/P object is missing.

## Frozen equivalence predicates

For each valid lane:

- relative Frobenius residual `||D_cached-D_historical|| / max(||D_cached||,||D_historical||,1e-30) <= 1e-9`;
- relative Frobenius residual `||H_cached-H_historical|| / max(||H_cached||,||H_historical||,1e-30) <= 1e-9`;
- center algebraic A residual `<=1e-13` relative;
- center lowering-insertion I residual `<=1e-13` relative;
- center P residual `<=1e-13` relative.

The tolerances are frozen before any matrix execution and account only for floating-coordinate construction/order differences; they are far below the existing finite-difference scientific tolerances.

## Frozen negative control

Using the already built cached lattice, multiply exactly one noncentral cached P tensor at canonical offset `(2,0,0,0)` by `1.01` and recompute the cached D/H reduction without changing any other entry.

Require at least one of:

- corrupted-D relative difference from the uncorrupted cached D `>=1e-6`;
- corrupted-H relative difference from the uncorrupted cached H `>=1e-6`.

This prevents a vacuous cache-equivalence pass in which stencil P samples do not influence the scored object.

## Aggregate

All 16 lanes must be present, unique, valid and pass. Only:

- `D5_CANONICAL_CACHE_EQUIVALENCE_PASS`
- `D5_CANONICAL_CACHE_EQUIVALENCE_INVALID`

are allowed.

## Interpretation ceiling

PASS would authorize only a future **prospective implementation choice** to use the validated cache at `h=5e-4` on the tested Iter053R metric family, subject to the future scientific gate separately freezing that implementation. It does not retroactively modify any active run and is not a QGR scientific result. FAIL/INVALID means the cache is not authorized for Iter053U without a separately preregistered repair/equivalence gate.