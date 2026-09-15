# Iter057L preregistration — general nonconformal first-order Einstein+Weyl3 background jet

Status: PROSPECTIVELY FROZEN
Date: 2026-09-15
Gate: `ITER057L-GENERAL-NONCONFORMAL-FIRST-ORDER-BACKGROUND-JET`

## Motivation and parent authority

Iter057J prospectively required that if the conformal continuation fails, the successor must test the general symmetric-tensor equation `DG[q]=S` with gauge/constraint control rather than interpreting the conformal failure as failure of all first-order corrections.

The later exact analytic Iter057J evaluation (`02b842b784023307fd64616f3594afae9824ed35`) supplies an exact nonzero first-prolongation component for the conformal ansatz, and terminal result `3b70ce21c9406f13c07631b763ad908f65f4499c` rejects only that conformal continuation. Historical Iter057K remains a terminal BLOCKED technical production attempt and is not reclassified by this gate.

The next bounded scientific question is therefore whether a **general symmetric first-order metric correction** has a source-compatible local jet on the same frozen G3/H0 background.

## Frozen equation

Use only

`A_E G_ab[g] + c6 E_W3_ab[g] = 0`,

with finite nonzero `A_E`, symbolic/unfixed `c6`, and

`g_ab = g0_ab + c6 q_ab + O(c6^2)`.

At first order,

`DG_ab[q] = S_ab`,

`S_ab := -E_W3_ab[g0]/A_E`.

`q_ab` is now an arbitrary symmetric tensor. No conformal, scalar, diagonal, static, plane-wave, spherical, or third symmetry reduction may be imposed as a derivation.

The source geometry remains the exact analytic G3/H0 metric already authorized by Iter057D. No fitted source, fitted `c6`, cosmological term, matter source, or additional curvature operator may be introduced.

## Gauge formulation to be audited, not assumed

A convenient candidate formulation is trace reversal

`qbar_ab := q_ab - (1/2) g0_ab q`

with covariant de Donder condition

`nabla^a qbar_ab = 0`.

On a Ricci-flat background the expected reduced linearized Einstein operator is a Lichnerowicz-type wave operator of the form

`DG_ab[q] = -(1/2) [Box qbar_ab + 2 R_acbd qbar^cd]`

up to the repository's frozen curvature/sign conventions.

This exact sign/index formula is an **obligation of the gate**, not pre-authorized input. It must be derived or mapped to existing repository authority before use.

## Frozen obligations

A. **Linearized-Einstein identity.** Derive the general covariant `DG_ab[q]` on the Ricci-flat G3/H0 background and independently verify the trace-reversed/de Donder reduction with repository curvature conventions.

B. **Source conservation.** Verify exactly that the frozen source satisfies

`nabla^a S_ab = 0`

to the jet order used. Existing Iter056X Noether authority may be invoked analytically, but any coordinate implementation used downstream must reproduce the required local divergence identity exactly rather than by a numerical tolerance.

C. **Gauge/constraint compatibility.** Show that the reduced equation and de Donder constraint are mutually compatible at the origin and through the first nontrivial source-owned derivative order. Pure gauge freedom must be kept explicit; rank counting may not mistake gauge directions for physical correction data.

D. **General local jet construction.** Construct the smallest exact Taylor jet of general symmetric `q_ab` sufficient to solve the ten first-order equations at the origin and the first source-owned derivative compatibility conditions. Prefer exact symbolic/rational coefficients with the common `1/A_E` factored out.

E. **No hidden conformal reuse.** Demonstrate that the constructed solution space is genuinely the unrestricted symmetric-tensor problem. The rejected Iter057J conformal Hessian may be used only as a negative control, not as the ansatz for this gate.

F. **Independent control.** At minimum use one independently derived identity or alternative exact representation to check the solved jet (for example direct unreduced `DG[q]` versus trace-reversed reduced form).

G. **Scope ceiling.** A local jet PASS does not establish an open-neighborhood analytic solution, global boundary conditions, exact all-orders background, physical characteristics, hyperbolicity, modes/ghosts, stability, unitarity, regulator removal, UV completion, experimental confirmation, or QGR correctness.

## Decision rules

Maximum scoped PASS:

`PASS_SCOPED_ITER057L_GENERAL_QAB_FIRST_ORDER_LOCAL_JET_SOURCE_COMPATIBLE__OPEN_NEIGHBORHOOD_SOLUTION_NOT_ESTABLISHED`

iff obligations A-F are satisfied exactly and a nonempty general symmetric-tensor local solution jet survives gauge/constraint controls through the prospectively frozen derivative order.

Scientific FAIL:

`SCIENTIFIC_FAIL_SCOPED_ITER057L_GENERAL_QAB_FIRST_ORDER_LOCAL_JET_INCOMPATIBLE_WITH_FROZEN_SOURCE`

only if an exact gauge-invariant/source-compatibility obstruction rules out the general symmetric-tensor first-order local jet, not merely a gauge choice or restricted ansatz.

BLOCKED:

`BLOCKED_ITER057L_GENERAL_QAB_EXACT_JET_NOT_TECHNICALLY_REALIZED`

if the exact source/operator representation needed by the frozen obligations cannot be completed in a bounded attempt without changing the scientific problem.

INVALID:

`INVALID_ITER057L_GAUGE_CONVENTION_OR_EXACTNESS_CONTROL`

if a post-hoc symmetry reduction, fitted `c6`, fitted source, numerical tolerance used as exact-zero evidence, or unverified sign/convention mapping enters the decision.

## Execution lock

Do not launch a large CI matrix before a minimal exact local constructor and the unreduced-vs-reduced identity control exist in source form. Parallel lanes are allowed only for logically independent exact controls or disjoint jet sectors after the common conventions are frozen.

## Claim locks

Theory established remains `0%`; no experimental confirmation; `beta=1` unauthorized; `c6` symbolic/unfixed; no physical Weyl3 treatment selector; no strong-hyperbolicity, ghost, stability, unitarity, regulator-removal, UV-completion or KMQGB `NEW_REQUIRED` claim.