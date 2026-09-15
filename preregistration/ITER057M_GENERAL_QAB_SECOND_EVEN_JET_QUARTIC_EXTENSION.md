# Iter057M preregistration — general q_ab second-even-jet / quartic extension

Status: PROSPECTIVELY FROZEN
Date: 2026-09-15
Gate: `ITER057M-GENERAL-QAB-SECOND-EVEN-JET-QUARTIC-EXTENSION`
Parent authority: Iter057L terminal PASS `24de1e6d28cfd78327b79568ac2398337c309ac4`.

## Question

Does the unrestricted first-order correction that exists at quadratic local-jet order extend through the **next nontrivial even source jet** on the exact G3/H0 background?

Equivalently: can an exact quartic trace-reversed correction be chosen so that the first-order Einstein+Weyl3 equation and de Donder gauge hold through quadratic order in coordinates around the frozen origin?

## Frozen equation and expansion

Keep

`DG_ab[q]=S_ab`, `S_ab=-E_W3_ab[g0]/A_E`,

with finite nonzero `A_E` and symbolic/unfixed `c6`.

Use the exact source-owned G3/H0 metric and the Iter057L trace-reversed gauge formulation.

Because the source/background are static and inversion-even, freeze the local ansatz

`qbar_ab = (1/2) Q2_ab,cd x^c x^d + (1/24) Q4_ab,cdef x^c x^d x^e x^f + O(|x|^6)`,

where `Q2` is the already-authorized universal Iter057L quadratic jet specialized to the exact source value at the origin, and `Q4` is unrestricted apart from symmetry in `(ab)` and complete symmetry in `(cdef)`.

Odd correction jets are set to zero only because the frozen coefficients/source are exactly even and the Iter057L first-derivative conditions already vanish; this parity bookkeeping is not a new spatial symmetry reduction.

## Frozen obligations

A. **Exact source second jet.** Extract the exact coordinate/covariant quadratic coefficient of `S_ab(x)` needed at the origin from the same authorized G3/H0 + Iter056X Weyl3 source. Factor out the common `1/A_E`; no numerical finite differences may decide exact coefficients.

B. **Exact operator coefficient jet.** Expand the de Donder-reduced linearized Einstein operator through coordinate degree two, including all contributions from the quadratic background metric/inverse, connection, curvature, and the already-fixed `Q2` jet.

C. **Quartic generality.** Parameterize the full unrestricted `Q4_ab,cdef` space: symmetric in `ab`, fully symmetric in the four derivative indices. No conformal, diagonal, static-component, plane-wave, spherical, or additional ansatz may be imposed on `Q4`.

D. **Gauge through cubic order.** Impose `nabla^a qbar_ab=0` through coordinate degree three. Keep gauge-null/free directions explicit rather than eliminating them by an untracked restriction.

E. **Field equation through quadratic order.** Solve the exact linear system obtained from `DG_ab[q]-S_ab=0` through coordinate degree two.

F. **Independent control.** Substitute any solution back into the unreduced covariant linearized Einstein expression through the same order, or use another exact representation proven equivalent under the frozen conventions. Reduced-only self-consistency is insufficient.

G. **Source/Noether compatibility.** Verify the exact degree-one/degree-two consequences of `nabla^a S_ab=0` used by the coefficient system. No numerical tolerance may replace an exact identity.

## Decision rules

Maximum scoped PASS:

`PASS_SCOPED_ITER057M_GENERAL_QAB_QUARTIC_JET_EXTENDS_THROUGH_SECOND_EVEN_SOURCE_ORDER__OPEN_NEIGHBORHOOD_NOT_ESTABLISHED`

iff an exact unrestricted `Q4` solution exists and obligations A-G pass identically/symbolically.

Scientific FAIL:

`SCIENTIFIC_FAIL_SCOPED_ITER057M_GENERAL_QAB_SECOND_EVEN_JET_INCOMPATIBLE_WITH_FROZEN_SOURCE`

only if the exact coefficient system is inconsistent after gauge freedom and Noether identities are accounted for.

BLOCKED:

`BLOCKED_ITER057M_EXACT_QUARTIC_SYSTEM_NOT_TECHNICALLY_REALIZED`

if the exact source/operator second jet or exact solve cannot be completed in the bounded implementation without changing the frozen problem.

INVALID:

`INVALID_ITER057M_RESTRICTION_CONVENTION_OR_EXACTNESS_CONTROL`

if any post-hoc restricted ansatz is used to infer general solvability, a fitted/numerical exact-zero criterion is introduced, `c6` is fixed, or the reduced/unreduced convention control fails.

## Parallel execution lock

After a common exact source/operator coefficient representation is frozen, independent lanes may be used for: source-second-jet extraction, gauge-equation assembly, field-equation assembly, and independent substitution control. Do not launch a large matrix before the common exact conventions and monomial basis are fixed.

## Scope ceiling and claim locks

Even a PASS remains a finite local Taylor certificate, not an open-neighborhood existence theorem or convergent series. It does not establish physical characteristics, strong hyperbolicity, ghost freedom, stability, unitarity, regulator removal, UV completion, experiment, or QGR correctness.

`c6` remains symbolic/unfixed; `beta=1` remains unauthorized; theory established remains `0%`.