# Iter055P preregistration — cell-relative covariant smearing class and boundary causal type

Date: 2026-09-14
Gate: `ITER055P-CELL-RELATIVE-COVARIANT-SMEARING-CLASS`

## Frozen question
Can the already-existing microscopic refinement parameter `h` and the Iter055O boundary normal anchor `n` define a nonempty normalized Lorentz-covariant Hilbert-dual smearing **class** before the absolute physical calibration of `h`, and for which regular non-null B3 causal types?

No concrete radial profile is selected in this gate.

## Frozen objects
- G6F future-null-cone one-particle measure and physical quotient Hilbert space.
- Iter055O regular non-null boundary normal/conormal line.
- Existing microscopic/refinement scale parameter `h` from G7A, with its absolute calibration explicitly still unidentified.

## Frozen class ansatz under test
For a spacelike B3 with future-timelike unit normal `n`, test radial envelopes of the form

`phi_(h,n)(k) = h * f(h * E_n(k))`, with `E_n(k)=n.k>0`,

up to physical polarization/tensor factors whose separate source selection is not claimed here.

For a timelike B3 with unit spacelike normal `n`, test whether any nonzero envelope depending only on `h*(n.k)` can be square-integrable over the full future null cone.

## Frozen obligations
1. Show exact norm scaling under `k` dilation and determine the function space required of `f` for the timelike-normal case.
2. Derive the induced refinement/dilation law under `h -> h/r` without choosing a profile shape.
3. Verify Lorentz covariance at class level when `(n,k)` transform together.
4. Determine whether a spacelike normal alone controls all ultraviolet null directions; use the full cone measure rather than finite angular sampling.
5. Keep absolute calibration distinct from internal refinement covariance: a class may exist for symbolic/unfixed `h` without establishing a physical value of `h`.
6. Do not claim a complete bridge if polarization/tensor kernel, profile shape, B3 attachment or refinement coefficients remain unfixed.

## Frozen classifications
- `PASS_SCOPED_ITER055P_CELL_RELATIVE_SMEARING_CLASS_EXISTS_FOR_ALL_REGULAR_NON_NULL_B3_TYPES` only if `(h,n)` alone defines a nonempty square-integrable class for both timelike and spacelike normals.
- `PASS_SCOPED_PARTIAL_ITER055P_CELL_RELATIVE_CLASS_EXISTS_FOR_SPACELIKE_B3_TIMELIKE_NORMAL__TIMELIKE_B3_NEEDS_EXTRA_ANCHOR` if the class exists with timelike normal but a spacelike normal alone cannot control the full cone.
- `FAIL_SCOPED_ITER055P_CELL_RELATIVE_H_AND_NORMAL_INSUFFICIENT_EVEN_FOR_SPACELIKE_B3` if no nonempty normalized class exists even for future-timelike `n`.
- `INVALID_PROVENANCE_ITER055P_H_OR_NORMAL_SOURCE_NOT_FIXED` only if the frozen source objects are not sufficient to pose the class-level test.

## Interpretation ceiling
A partial or full PASS proves only existence of a scale-covariant smearing class with symbolic `h`; it does not select `f`, fix absolute `h`, supply polarization/tensor kernels, define the B3 bridge, select interacting dynamics, or establish beta/c6/Weyl3 treatment/regulator removal/unitarity/UV/GR/experiment/theory claims.

No GitHub Actions run is preregistered; this is an exact measure/scaling analysis.
