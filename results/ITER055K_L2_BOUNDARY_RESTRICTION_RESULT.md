# Iter055K terminal result — raw one-particle L2 to finite-B3 boundary restriction

Date: 2026-09-14
Preregistration: `f49fc045fa0387634638d7eedd67b75c150a9d64`

## Terminal classification

`FAIL_SCOPED_ITER055K_RAW_L2_BOUNDARY_POINT_RESTRICTION_NOT_BOUNDED__SMEARING_OR_REGULARITY_REQUIRED`

## Source identity

G6F fixes the regular one-particle Hilbert object

`H_char(G)=direct_integral_{N_G^+} dmu_G(k) P_(G,k)`

with

`dmu_G = sqrt(|det G^-1|) d4k delta(k G^-1 k) theta_future`

and positive two-dimensional physical polarization quotient fibers. G6C/G6E fix finite shared-B3 metric/connection restriction variables as the boundary target.

The only bridge tested here is the prospectively frozen raw linearized reconstruction/restriction: reconstruct the characteristic field from its null-cone amplitudes and evaluate the field and first-derivative/connection data at the finite B3 boundary points/edges.

## 1. Null-cone measure has infinite total volume

In a local Lorentz frame the future-null-cone measure has the standard radial form

`dmu ~ d3p/(2|p|) = (1/2) r dr dOmega`

up to the fixed nonsingular metric density factor. Therefore the regular future cone has infinite total measure at large momentum:

`integral dmu = infinity`.

A fixed finite angular patch and shell `A_R={R<r<2R}` already has measure proportional to `R^2`.

## 2. Point reconstruction is not a bounded functional on the G6F L2 completion

For a fixed spacetime/boundary point `x`, one component of the linearized field reconstruction has the form

`L_x[a] = integral a(k) e^{i k.x} dmu(k)`

on a regular physical polarization patch. The kernel has modulus one, so its `L2(dmu)` norm would be

`||e^{ik.x}||_2^2 = integral dmu = infinity`.

By the Riesz representation criterion there is therefore no bounded extension of this raw evaluation functional to the full G6F `L2` Hilbert completion.

An explicit witness makes the failure quantitative. Choose a measurable unit physical polarization on a fixed regular angular patch and define

`a_R(k)=1_{A_R}(k) e^{-ik.x}/sqrt(mu(A_R))`.

Then

`||a_R||_2=1`

but

`|L_x[a_R]|=sqrt(mu(A_R)) ~ R -> infinity`.

Thus no constant `C` can satisfy `|L_x[a]| <= C ||a||_2` on the frozen Hilbert domain.

This argument uses physical quotient polarizations rather than gauge directions, so quotienting does not remove the obstruction.

## 3. Finite many B3 evaluation points do not help

The boundary target contains only finitely many vertex/edge values, but each individual raw point-evaluation functional is already unbounded. A finite product of unbounded evaluation maps is not a bounded Hilbert-space restriction map.

Also, an `L2` state is an equivalence class modulo measure-zero changes. No source-defined pointwise representative is supplied by the Hilbert completion itself.

## 4. Connection / derivative boundary data are more singular

A first derivative inserts a momentum factor:

`partial h(x) ~ integral (i k) a(k) e^{ik.x} dmu(k)`.

The corresponding kernel has squared norm containing an additional `|k|^2`, giving radial growth proportional to

`integral r^3 dr`,

so the derivative/connection evaluation is also unbounded, more strongly than the metric value itself.

## 5. What would repair the map

The failure is specific to the raw `L2 -> pointwise finite-boundary data` map. A well-defined bridge could be obtained only after adding extra mathematical structure, for example one of:

- smearing against boundary/test functions whose momentum kernels are square-integrable;
- a source-defined compact momentum support or bandlimit;
- a weighted/Sobolev domain strong enough for the required traces/derivatives;
- an explicit detector/profile map;
- another prospectively defined bounded sector-identification transform.

None of these is presently fixed by the audited QGR authority, and none may be chosen post hoc as part of this gate.

## Scientific consequence

Iter055J's missing overlap is not merely an omitted notation map. The most naive canonical-looking bridge is mathematically unavailable on the actual one-particle `L2` completion:

`H_char(L2) -/-> raw finite B3 point values`.

Therefore exact recovery of Iter009-G6 cannot yet be used as an interacting-boundary dynamics kill test. Before dynamics selection, QGR needs an explicit **bounded sector bridge**, which necessarily carries additional smearing/regularity information beyond the raw G6F Hilbert definition.

This is a scoped failure of one natural bridge, not a no-go theorem for every possible overlap construction.

## Next highest-information gate

Prospectively compare minimal bridge axiom classes before choosing one: at minimum (A) covariant smearing/test-function bridge and (B) stronger weighted/Sobolev trace domain. Freeze which structure is independently motivated by existing QGR observables/locality and demand exact covariance, positivity/pairing control, refinement compatibility, and recovery of G6F/Iter009-G6 on their common regular domain. Do not tune a cutoff/profile after results.

## Claim ceiling

- no interacting boundary dynamics selected;
- no theorem that every overlap is impossible;
- Iter009-G6 one-particle result remains valid in its scope;
- theory established = 0%;
- `beta=1` unauthorized;
- `c6` unfixed;
- no global regulator removal, full quantum unitarity, UV completion, GR recovery, experiment or new physics.

No GitHub Actions run was needed: the obstruction is exact functional analysis.
