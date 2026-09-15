# Iter057S preregistration — on-shell first-order Q2/Q4 correction on the completed seed

Status: PROSPECTIVELY FROZEN
Date: 2026-09-15
Gate: `ITER057S-ONSHELL-FIRST-ORDER-Q2-Q4-CORRECTION`
Parent authority: Iter057R terminal corrected source `e395d2fb4be3e6f556f893ce63ae68f3b4b51ea2`; Iter057Q canonical Einstein seed `c4f1c5c01205a6991e7215e3824111e1f36d1436`.

## Question

Does the first-order Einstein+Weyl3 equation

`A_E DG_ab[q] + E_W3,ab[g_seed] = 0`

admit an unrestricted exact quadratic+quartic local correction on the canonical quartic+sextic Einstein-completed seed through coordinate degree two?

Define

`qhat_ab := A_E q_ab`, `Shat_ab := -E_W3,ab[g_seed]`.

The frozen equation is therefore

`DG_ab[qhat] = Shat_ab`.

No value or sign of `c6` or `A_E` is chosen; `A_E` is only factored as a finite nonzero normalization.

## Frozen data

Use exactly:

- the canonical Iter057O quartic seed correction;
- the canonical Iter057Q sextic seed correction;
- the Iter057R exact corrected source `Shat^(0), Shat^(2)`.

No old Iter057M off-shell G3 source coefficient, no post-hoc seed homogeneous freedom and no restricted correction ansatz may be substituted.

## Frozen correction space

Use trace-reversed local correction

`qhatbar_ab = (1/2) Q2_ab,cd x^c x^d + (1/24) Q4_ab,cdef x^c x^d x^e x^f`.

`Q2` is an arbitrary symmetric rank-two-by-rank-two normalized Hessian jet subject only to the exact field/gauge equations. `Q4` spans all 350 coefficients: 10 symmetric tensor components times 35 fully symmetric derivative multi-indices.

## Frozen obligations

A. **Consume the corrected source.** Replay the full Iter057R source: point tensor plus all 22 nonzero normalized degree-two coefficients, including all 7 time-containing terms. Verify its degree-one Noether identity rather than assuming it.

B. **Quadratic correction.** Construct an exact `Q2` solving the pointwise field equation and de Donder condition at the first nontrivial order. Independently substitute it into the unreduced covariant linearized Einstein tensor at the origin.

C. **Corrected background coefficient jet.** Assemble the degree-two/cubic gauge contributions of the fixed `Q2` directly on the full canonical Einstein seed. It is permitted to prove that quartic/sextic seed terms drop out at the frozen order, but this must follow from exact degree counting or direct substitution, not from reuse of the historical Iter057M affine RHS.

D. **Full quartic generality.** Parameterize all 350 Q4 coefficients and impose all 80 cubic de Donder rows plus all 100 quadratic field rows. No static, diagonal, conformal, spherical, plane-wave or component restriction is allowed.

E. **Exact compatibility.** Use the complete 16-dimensional Bianchi left-nullspace of the universal 180x350 principal matrix and evaluate every affine compatibility contraction against the corrected Iter057R source/background RHS. Numerical rank or tolerance may not decide consistency.

F. **Exact solve.** If consistent, construct at least one unrestricted exact particular Q4 and preserve the full homogeneous solution space. Record exact rank, augmented rank and nullity.

G. **Independent full-seed unreduced control.** Convert the chosen trace-reversed Q2+Q4 correction back to the metric perturbation and recompute the unreduced covariant linearized Ricci/Einstein response on the full quartic+sextic seed. Require

`DG_ab[qhat]-Shat_ab=0`

through coordinate degree two for all ten independent symmetric components and de Donder through cubic order.

H. **Scope/accounting.** Record that a PASS is only the `O(c6)` local coefficient solution through the second even coordinate order on a zeroth-order seed known vacuum-consistent through degree four. Higher seed/correction orders and convergence remain open.

## Decision rules

Maximum scoped PASS:

`PASS_SCOPED_ITER057S_ONSHELL_FIRST_ORDER_Q2_Q4_CORRECTION_MATCHES_CORRECTED_WEYL3_SOURCE_THROUGH_SECOND_EVEN_ORDER__HIGHER_ORDERS_REMAIN_OPEN`

iff obligations A-H pass exactly.

Scientific FAIL:

`SCIENTIFIC_FAIL_SCOPED_ITER057S_CORRECTED_SEED_FIRST_ORDER_Q2_Q4_SYSTEM_INCOMPATIBLE`

only if the full unrestricted exact affine system is inconsistent after the complete Bianchi/Noether compatibility space is accounted for.

BLOCKED:

`BLOCKED_ITER057S_EXACT_ONSHELL_Q2_Q4_SYSTEM_NOT_REALIZED`

if the corrected source/background system or unreduced control cannot be realized without changing the frozen problem.

INVALID:

`INVALID_ITER057S_OLD_SOURCE_REUSE_RESTRICTION_CONVENTION_OR_EXACTNESS_CONTROL`

if historical G3 source coefficients are reused, a restricted correction ansatz is generalized, numerical zero/rank is used, seed homogeneous freedom is altered post hoc, `c6` is fixed/fitted, or the unreduced control fails.

## Scope ceiling

A PASS does not establish higher coordinate orders, a convergent/open-neighborhood Einstein+Weyl3 background, global/asymptotic boundary data, physical characteristics, hyperbolicity, ghosts, stability, unitarity, regulator removal, UV completion, experiment, or QGR correctness.

`c6` remains symbolic/unfixed; `beta=1` remains unauthorized; theory established remains `0%`.