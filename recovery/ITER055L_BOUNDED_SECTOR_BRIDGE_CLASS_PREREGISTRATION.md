# Iter055L preregistration — minimal bounded one-particle / boundary sector-bridge class

Date: 2026-09-14
Gate: `ITER055L-MINIMAL-BOUNDED-SECTOR-BRIDGE-CLASS`

## Frozen question
Given Iter055K's exact failure of raw point restriction on the G6F `L2` completion, which of the two minimal repair classes can preserve the already-authoritative one-particle Hilbert/channel domain and finite-frame covariance without importing an undeclared preferred frame, UV scale or dynamics?

Compare only these prospectively frozen classes:

A. `SMEAR`: keep the existing G6F Hilbert space unchanged and replace raw point values by a finite family of bounded covariant linear boundary observables `B_j(a)=<phi_j,a>` with square-integrable physical kernels/test functions. Metric and connection observables may use distinct kernels, but no profile is selected in this gate.

B. `TRACE`: replace/shrink the state domain by a stronger weighted/Sobolev/trace-regularity space on which raw field and derivative point traces are continuous.

No third repair class may be introduced after the result.

## Frozen obligations
1. **Existing-domain preservation:** determine whether each class leaves the full established G6F one-particle `L2` Hilbert/channel domain intact or replaces it by a stricter domain.
2. **Boundedness:** prove whether the class can make the finite boundary observables continuous.
3. **Finite-frame covariance:** require a transformation law that does not secretly choose an observer, preferred timelike vector or non-source-defined momentum scale.
4. **Physical quotient descent:** bridge observables must be defined on the positive physical polarization quotient, not gauge representatives.
5. **Refinement compatibility:** state the exact algebraic condition required for coarse boundary observables to be obtained from fine ones; do not invent a profile to satisfy it.
6. **One-particle channel compatibility:** the existing Iter009-G6 channel must remain a well-defined channel on the retained domain. If a class shrinks the domain, source authority must already establish invariance of that stronger domain under every required branch unitary; otherwise classify that obligation as unclosed.
7. **Residual freedom:** identify whether the surviving class is itself unique or leaves new kernel/regularity data to be supplied as explicit candidate input.

## Frozen analytic controls
- For `SMEAR`, use Hilbert-space duality/Cauchy-Schwarz: every physical `phi_j in H_char` defines a bounded functional, with norm `||phi_j||`.
- For `TRACE`, test whether a nonconstant ultraviolet-suppressing weight can be defined from the null momentum alone while preserving full finite-frame/Lorentz covariance. In particular, use the fact that the Lorentz group acts transitively on the nonzero future null cone, including rescalings of a null vector by boosts along its direction.
- Do not count an observer-dependent frequency weight `w(n.k)`, Euclidean `|k|`, compact support, bandlimit or cutoff as source-free covariance; each would be new structure.

## Frozen classifications
- `PASS_SCOPED_ITER055L_SMEARING_CLASS_MINIMAL_DOMAIN_PRESERVING_BRIDGE__PROFILE_SELECTION_STILL_NEW_INPUT` if bounded covariant smearing survives all class-level obligations while `TRACE` cannot preserve the current full `L2` domain/covariance without extra structure.
- `PASS_SCOPED_ITER055L_TRACE_CLASS_SOURCE_COMPATIBLE_WITHOUT_NEW_FRAME_OR_SCALE` only if current authority supplies a stronger trace domain and its invariance/covariance without new structure.
- `BLOCKED_ITER055L_BOTH_MINIMAL_BRIDGE_CLASSES_REQUIRE_UNRESOLVED_NEW_STRUCTURE` if neither class survives the frozen class-level obligations.
- `INVALID_ITER055L_CLASS_COMPARISON_NOT_WELL_POSED` only if the G6F source domain or covariance action is too ambiguous to perform the frozen comparison.

## Interpretation ceiling
A class-level PASS does not select a concrete kernel/profile and does not define interacting dynamics. It only narrows the mathematically admissible form of the new sector bridge. Any remaining profile, scale, smearing shape, detector observable or refinement rule is explicit new candidate input requiring a successor preregistered selection/falsification gate. No beta/c6/Weyl3 treatment/regulator-removal/unitarity/UV/GR/experiment/theory-establishment claim follows.

No GitHub Actions run is preregistered; this is an exact Hilbert/covariance comparison.
