# Iter054U Preregistration — G3 Branch-Resolved Weyl3 Differential Operator Observable

Date: 2026-09-14

Gate: `ITER054U-G3-BRANCH-RESOLVED-WEYL3-DIFFERENTIAL-OPERATOR`

Status at freeze: **PREREGISTERED BEFORE TARGETED AUTHORITY AUDIT**

## Motivation

Iter054T localized the remaining G3 history-to-action obstruction at the nonhomogeneous physical source/boundary insertion that would produce a concrete `S_alpha`. The current front permits a distinct route only if a nontrivial Weyl-active normalized observable cancels the unresolved source scale while retaining `c6` sensitivity and treats `U_alpha` explicitly.

The most conservative such candidate is a logarithmic/differential response with respect to the symbolic IR coefficient `c6`. A source contribution proportional to the unresolved additive scale `beta` may cancel from `d/dc6` if it is genuinely independent of `c6`; this must not be assumed to create a branch action that does not otherwise exist.

## Frozen objects

Use only the established Iter010-G3 weak-tidal same-field family and its 24 explicit permutation histories from `code/qgr_iter010_g3_common.py`, with the established G8A symbolic branch structure

`K_alpha = 24^(-1/2) exp(i S_alpha / hbar) U_alpha`.

Use G4 only for its already established background-level statement that the G3 Weyl-active geometry has nonzero `d Phi / d c6 = h^4 Weyl^3` sensitivity. Do not reinterpret that scalar background sensitivity as a history-resolved action datum unless repository authority explicitly supplies the map.

## Scientific question

Does existing QGR authority define, for at least two explicit G3 permutation histories `alpha` and `beta`, a branch-resolved Weyl3 action response `d S_alpha/dc6` and `d S_beta/dc6` on the same source-faithful realization, so that a normalized operator response can be formed without fixing the unresolved source scale?

A qualifying object may have the schematic form

`R_ab = (d/dc6)(K_alpha K_beta^{-1}) (K_alpha K_beta^{-1})^{-1}`,

or an exactly equivalent operator-valued response, but only if every term is source/geometry-derived under existing authority.

## Frozen obligations

### A — explicit histories and transport

At least two prospectively fixed explicit G3 permutation histories must be identified. Their transport operators `U_alpha`, `U_beta` must be computed/identified from the existing G3 connection; transport may not be silently set to identity.

### B — branch-resolved Weyl3 action response

Repository authority must provide a rule assigning `dS_alpha/dc6` to each explicit history from the same G3 geometry/source realization. A single background scalar `h^4 Weyl^3`, a local sensitivity with no history integration rule, or a symbolic placeholder does not satisfy B.

### C — source-scale cancellation

Any unresolved additive source-calibration direction (including `J(n)=beta*n`) must cancel algebraically from the differential/relative observable without setting `beta=1` and without importing a new physical normalization.

### D — nontrivial c6 sensitivity

The final normalized/operator observable must have a nonzero, branch-resolved `c6` response. A common scalar response identical for every history is insufficient because it does not supply the missing history-to-action information.

### E — no synthetic discretization convention

No new path quadrature, vertex weighting, cell assignment, source profile, branch weight, phase value, or measure prescription may be invented after seeing outputs. If current authority does not specify how the Weyl3 density is accumulated along a G3 history, classify BLOCKED rather than choose a convenient rule.

## Frozen positive controls

- G3 has 24 explicit permutation transport histories and a Weyl-active tidal background.
- Iter054S establishes source-ordered fine-to-coarse transport blocking in finite-panel scope on that Weyl-active realization.
- G4 establishes nonzero background-level Weyl3 action-phase sensitivity.
- G8A provides the symbolic branch-operator structure with explicit `U_alpha`.

## Frozen negative controls

Reject as sufficient:

- the common G4 scalar sensitivity copied onto all 24 histories;
- synthetic Iter054O/P phase coefficients;
- setting `U_alpha=1` or dropping transport;
- defining a new path integral/quadrature rule not already authorized;
- setting `beta=1`;
- using G35–G37 distant-root weights as physical branch weights;
- treating a finite-panel result as a global measure, unitarity or full-QG theorem.

## Classification

PASS only as

`PASS_SCOPED_ITER054U_G3_BRANCH_RESOLVED_WEYL3_DIFFERENTIAL_OPERATOR_DEFINED__C6_STILL_UNFIXED`

if A–E all close from pre-existing authority.

BLOCKED as

`BLOCKED_MISSING_REQUIRED_OBJECT_ITER054U_NO_BRANCH_RESOLVED_WEYL3_ACTION_RESPONSE`

if explicit histories/transports exist but no authorized branch-resolved Weyl3 action-response map exists.

INVALID only for incomplete audit/provenance/procedure failure.

## Interpretation ceiling

Even PASS would define only a scoped differential/operator observable. It would not fix `c6`, authorize `beta=1`, establish regulator removal/global measure, exact-vs-order-reduced Weyl3 dynamics, strong hyperbolicity, unitarity, UV completion, full GR recovery, experimental confirmation, new physics or QGR correctness. Theory established remains 0%.
