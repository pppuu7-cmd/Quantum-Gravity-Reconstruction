# Iter057AT — Corrected homogeneous degree-six Weyl^3 source authority

Status: PROSPECTIVELY PREREGISTERED; NO TARGET EVIDENCE CONSUMED FOR THIS GATE.
Date: 2026-09-17

## Scientific object
Construct, from the unchanged Iter057W source geometry and the exact Frechet derivative P_F = d I3 / d R used by Iter057AQ, the corrected homogeneous total-degree-six coefficient slice of the covariant Weyl^3 Euler/source response. The coefficient c6 remains symbolic and factored out.

The frozen serialization domain is exactly:
- four coordinate variables;
- ten symmetric tensor component pairs;
- homogeneous multi-indices alpha with sum(alpha)=6;
- 84 monomials per tensor component;
- exactly 840 ordered rational source slots.

This is a NEW gate. It is not an Iter057AR reproduction and does not retroactively modify Iter057AR, whose frozen 2100-slot object remains terminal BLOCKED.

## Frozen construction
1. Use the unchanged Iter057W seed/geometry and conventions.
2. Use exact rational arithmetic only; no floating tolerance.
3. Use exact Frechet P_F=dI3/dR; do not restore the legacy P_L construction diagnosed by Iter057AQ.
4. Preserve the inherited PAIRS order and homogeneous alphas(6) order.
5. c6 is SYMBOLIC_UNFIXED and factored out.
6. No historical Iter057X/AR target coefficient vector may be loaded before the primary 840-vector is serialized and SHA256-frozen.
7. No sign, scale, basis, normalization, threshold, or embedding fit is permitted after seeing comparison evidence.

## Primary controls
The primary constructor must report and freeze, before any historical comparison:
- slot_count == 840;
- monomial_count_per_pair == 84;
- all alpha satisfy sum(alpha)==6;
- exact-rational serialization only;
- unchanged source seed/conventions fingerprint;
- P_F intrinsic controls inherited from Iter057AQ;
- source tensor symmetry and the applicable exact covariant/Noether controls already validated for the corrected constructor path;
- SHA256 of the ordered 840-vector and complete scientific payload.

A green workflow is not scientific PASS.

## Independent reproduction firewall
A second implementation/reproduction must construct the same 840-slot object without reading the primary coefficient payload. It may read this preregistration and frozen source definitions. Terminal PASS requires bit-for-bit equality of the independently serialized ordered rational vector and agreement of the frozen controls. If independent reproduction is technically unavailable, classify BLOCKED rather than weakening the gate.

## Terminal classifications
PASS_SCOPED_ITER057AT_CORRECTED_HOMOGENEOUS_DEGREE6_SOURCE_INDEPENDENTLY_REPRODUCED — all frozen primary controls pass and independent no-read reproduction is bit-for-bit identical.

FAIL_ITER057AT_CORRECTED_HOMOGENEOUS_DEGREE6_SOURCE — a frozen scientific/control criterion fails after valid construction.

BLOCKED_ITER057AT_CORRECTED_HOMOGENEOUS_DEGREE6_SOURCE — the exact 840-slot object or required independent reproduction cannot be realized as frozen.

## Scope / claim locks
Even PASS establishes only an exact finite homogeneous degree-six source certificate on the frozen source construction. It is not a global/all-orders theorem, not quantum unitarity, not regulator removal, not UV completion, and not experimental confirmation. Theory established remains 0%. beta=1 is unauthorized. c6 remains unfixed. KMQGB NEW_REQUIRED remains unauthorized.

## Post-PASS rule
Only after durable terminal PASS may descendants that depended on the legacy degree-six source be replayed, each under a separate prospective adjudication/replay gate. Historical results are not silently rewritten.