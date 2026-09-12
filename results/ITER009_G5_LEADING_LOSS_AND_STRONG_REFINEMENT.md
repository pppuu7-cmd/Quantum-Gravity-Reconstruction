# Iter009 G5 — Leading history-loss c6 order and strong refinement control

Run: `34664051772` — 6 lanes + aggregate SUCCESS.

## Result

Under a regular self-consistent curved correction

`Delta X_alpha = h^2 A_alpha + c6 h^4 B_alpha + ...`,

a quadratic branch-mixture purity/loss functional has expansion

`Loss = h^4 Q(A,A) + 2 c6 h^6 Q(A,B) + c6^2 h^8 Q(B,B) + ...`.

Therefore the already established leading `O(h^4)` G6H history-mixture loss is independent of `c6` provided the self-consistent `c6` geometry response is regular `O(h^4)` and carries no singular inverse-h enhancement. The first branch-dependent `c6` contribution enters at `O(h^6)`.

A common unitary geometry shift leaves mixture purity exactly invariant. This protection is observable-specific: absolute coherent propagation observables can still respond linearly to a common `O(h^4)c6` correction.

The repaired-G9 branch-relative Lorentz generator remains numerically `O(h^2)` down to `h=1/64` on the tested sequence. Exact G6F packet-overlap formulas then give an `O(h^2)` state distance for the specified normalized `m0/m1` packet profiles, yielding a summable dyadic strong-state bound.

## Classification

`PASS_SCOPED_LEADING_OH4_HISTORY_MIXTURE_PURITY_IS_C6_INDEPENDENT_UNDER_REGULAR_SELF_CONSISTENT_OH4_C6_GEOMETRY_CORRECTIONS__SPECIFIED_G6F_PACKET_DOMAIN_HAS_SUMMABLE_STRONG_REFINEMENT_CONTROL__ABSOLUTE_COHERENT_C6_RESPONSE_AND_FULL_DOMAIN_LIMIT_REMAIN_OPEN`

## Guard

This result does not fix `c6`, does not make all observables `c6` independent, and does not by itself establish a full-Hilbert strong limit beyond the tested packet domain. G6 addresses the full established one-particle `L2` domain separately.
