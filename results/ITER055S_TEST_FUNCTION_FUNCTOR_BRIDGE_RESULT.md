# Iter055S terminal result — test-function/readout functor versus candidate-owned smearing profile

Date: 2026-09-14
Preregistration: `fefed520adcff06181b359036340390c753531b5`

## Terminal classification

`PASS_SCOPED_ITER055S_TEST_FUNCTION_FUNCTOR_MAKES_PROFILE_CHOICE_OBSERVABLE_DATA__FINITE_B3_SECTOR_ATTACHMENT_STILL_BLOCKED`

## 1. G6F already supplies the correct Hilbert-dual readout structure

G6F establishes the positive regular characteristic Hilbert space

`H_char(G)=direct_integral_(N_G^+) dmu_G(k) P_(G,k)`

with invariant future-null-cone measure and positive two-dimensional physical quotient fibers. Because this is a Hilbert space, every physical section `phi in H_char` defines a bounded linear readout

`B_phi[a]=<phi,a>_Hchar`

with

`|B_phi[a]| <= ||phi|| ||a||`.

Thus the theory does not need to single out one Hilbert-dual vector in order for the one-particle observable sector to be mathematically well defined.

## 2. Smooth test/readout probes form a broad bounded covariant class

Let `F_ab(x)` be a smooth compactly supported spacetime test tensor whose on-shell Fourier data define a gauge-compatible functional on the physical characteristic quotient. Its Fourier transform is Schwartz. Restricted to the future null cone, it is bounded near the cone tip and decays faster than any power at large null momentum.

With `dmu ~ r dr dOmega`, this decay is sufficient for square-integrability. Therefore its descended physical on-shell section `phi_F` belongs to `H_char`, and

`B_F[a]=<phi_F,a>`

is bounded.

The phrase “gauge-compatible” is essential: a generic raw tensor test function need not define a functional on the quotient unless it annihilates gauge directions / descends to the physical dual. G6F/G6C fix the physical quotient and its covariant pairing; Iter055S does not invent a preferred projector onto a gauge representative.

Under finite frame changes, the characteristic cone, measure, physical quotient pairing, state and admissible test section transform together. The G6F isometry therefore gives the standard covariance relation for the pairing rather than selecting one fixed profile.

## 3. G6F/G6G/G6H source scope confirms that packet profiles are observable/preparation data

The historical source is explicit:

- G6F calls the exponential and polynomial-times-exponential families **benchmark preparations**, not fitted theory parameters;
- G6G calls its narrow packet a specified preparation/readout comparator, not a universal QGR number;
- G6H shows preparation dependence and requires a phenomenological prediction to state the prepared polarization state and detector readout;
- multiple radial profiles are validated rather than source-selected.

Therefore Iter055R's radial-profile nonuniqueness should not be promoted to a new fundamental coupling of QGR. It is naturally the freedom to choose an observable/preparation test function in the established one-particle sector.

Iter055M/R remain historically correct: no universal candidate-owned kernel was selected, and many admissible profiles exist. Iter055S changes the **interpretation of that freedom**, not those results.

## 4. The exact finite-B3 attachment is still missing

The test-function/readout functor acts on the continuum/characteristic one-particle sector. G6C/G6E instead use a finite shared-B3 configuration label consisting of metric/response variables at boundary vertices and compatible-isometry/connection data on boundary edges, with its own configuration-measure disintegration.

No audited authority supplies an exact source-defined map

`F_ab(x) or phi_F(k) -> finite B3 cylindrical/configuration observable`

or an intertwiner identifying the resulting one-particle readout with a boundary-relative quantum observable/channel.

A smooth probe localized in a collar of the boundary is not automatically the same object as the exact finite B3 restriction map. Conversely, using raw vertex/edge point values would reintroduce the Iter055K unboundedness problem.

Hence the missing candidate-owned object is now more precise: **a continuum/test-function to finite-cell B3 observable attachment/coarse-observable map**, not one universal packet profile.

## 5. Consequences for the timelike-B3 result

Iter055Q remains relevant only for attempts to build a scalar envelope directly from intrinsic timelike-boundary geometry. An externally conditioned detector/source four-velocity is legitimate observable data in the Iter055S functorial interpretation; it is simply not a universal candidate-owned boundary observer.

Thus generic observables may be conditioned on external preparation/readout data without converting those data into QGR dynamics.

## Scientific consequence

The bridge chain is revised to

`G6F one-particle physical Hilbert/channel`

`-> broad covariant test/readout functor (scoped established)`

`-> [MISSING continuum/test-function -> finite B3 cylindrical observable attachment]`

`-> boundary-sector intertwining/recovery test`

`-> interacting boundary dynamics selection`.

This removes an unnecessary demand that QGR select one universal radial profile while preserving the real finite-B3 sector-identification blocker.

## Next highest-information gate

Audit all existing discrete-to-continuum / continuum-to-cell reconstruction authority (especially G7A continuum matching, local-response definitions, cell averaging/interpolation rules, and any finite-element/coarse observable maps) for a source-defined **linearized continuum/test-function -> finite B3 cylindrical observable attachment**. Fail closed if the repo has only power counting or point-sampling conventions without a bounded coarse map.

## Claim ceiling

No finite-B3 sector map, interacting boundary channel, absolute h, beta/c6 fixing, Weyl3 treatment, regulator removal, full quantum unitarity, UV completion, GR recovery, experiment or theory establishment follows. Theory established remains 0%.

No GitHub Actions run was required; this is a Hilbert/source-functional result.
