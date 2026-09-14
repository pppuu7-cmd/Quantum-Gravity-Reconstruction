# ITER056K — WEYL3 PHYSICAL TREATMENT SELECTOR AUTHORITY AUDIT

## GATE_ID
`ITER056K-WEYL3-PHYSICAL-TREATMENT-SELECTOR-AUTHORITY-AUDIT`

## QUESTION
Does the QGR repository authority existing before this gate contain a bona fide physical principle that distinguishes and selects one admissible dynamical treatment of the Weyl-cubic correction — in particular perturbative/order-reduced dynamics, exact higher-derivative dynamics, or another explicitly defined treatment — without introducing new model information in this gate?

## AUTHORITY_UNIVERSE_CUTOFF
All QGR authority on `main` through commit `65a9b52229014eb2b171e4b6c0c3fdc6e56aedb4` inclusive. This includes recovery/state, ledgers/roadmaps, iteration records, preregistrations, terminal results, source/action/measure/micro-to-continuum documents, treatment/branch records, and relevant code comments only where they document an already-authorized scientific statement. This gate itself and any later files have zero selector authority for this audit.

## QUALIFYING_SELECTOR_DEFINITION
An object receives physical-treatment-selector credit only if all of the following hold:
1. it belongs to pre-gate QGR authority;
2. it has an independently stated physical motivation within QGR;
3. it distinguishes at least two genuinely admissible dynamical treatments;
4. it selects one treatment for physical reasons rather than mathematical convenience;
5. it was specified before downstream treatment-dependent outcomes;
6. it is not circular ghost/instability avoidance;
7. it is stronger than continuity-to-GR alone unless a theorem shows unique selection;
8. it is not merely a computational approximation or formal expansion;
9. it does not require a newly fitted/free prescription to make the selection;
10. it can be stated as an explicit physical condition, map, limit, measure/contour rule, state/initial-data rule, or theorem with a defined domain.
If any mandatory item is absent, selector credit is zero. A principle that only removes some treatments is Type I admissibility; one correlating branches/data is Type II; only a principle leaving a unique treatment modulo an explicitly declared equivalence class is Type III selection.

## CANDIDATE_AUTHORITY_CLASSES
The audit must cover at least:
A. foundational action/candidate/source/covariance/constraint construction;
B. EFT/low-energy/c6 expansion/power-counting/validity-domain records;
C. micro→continuum histories/refinement/coarse-graining/matching records;
D. quantum amplitude/measure/contour/regulator/state-selection records;
E. causality/boundary/retarded/initial-data/regularity conditions;
F. explicit exact-vs-order-reduced treatment records including Iter054F/G/G-R and successors;
G. GR/weak-field/low-energy/classical/semiclassical recovery conditions;
H. field-redefinition/scheme/resummation material if present.
The terminal no-selector classification is forbidden if any material class remains unaudited.

## PASS
`PASS_EXISTING_QGR_PHYSICAL_TREATMENT_SELECTOR_FOUND_SCOPED` only if a pre-gate QGR-owned Type III selector is pinned to exact source authority, its domain and assumptions are explicit, and at least two competing treatments are shown not to survive the same physical condition.

## FAIL_OR_MISSING_AUTHORITY
`QGR_EXISTING_PRINCIPLES_DO_NOT_SELECT_WEYL3_DYNAMICAL_TREATMENT_SCOPED` if the authority universe is complete for the listed classes and every candidate principle is either absent, only Type I/II, generic EFT lore not owned by QGR, continuity-only, computational, post-hoc, dependent on missing micro/measure/state objects, or satisfied by at least two inequivalent treatments.

## BLOCKED
`AUDIT_INCOMPLETE_BLOCKED` if a material pre-gate authority class or necessary source object cannot be retrieved or interpreted reliably enough to evaluate selector power.

## INVALID
`INVALID_PROVENANCE` if chronology, source identity, or authority cutoff cannot be established; `INVALID_IMPLEMENTATION` if the audit credits material created after the cutoff or changes the selector definition after inspecting substantive evidence.

## EXCLUSION_RULES
No selector credit for: mathematical well-posedness alone; desire to avoid fast/ghost modes; lack of a theorem for the competing treatment; continuity to GR without unique-selection theorem; green CI; finite-sector certificates; generic external EFT practice; post-hoc initial-data restrictions; convenience of a lower-order PDE; fitted prescription; authority imported from another project.

## NO_POSTHOC_RESCUE
No new physical selector may be introduced, tuned, ranked by downstream success, or tested for model rescue in this gate. Any promising new principle is recorded only as `FUTURE_PRINCIPLE_CANDIDATE` and requires a distinct future preregistration/version.

## CLAIM_CEILING
This gate can establish only whether existing QGR authority already selects a Weyl3 dynamical treatment in the audited scope. It cannot establish that order reduction is physically correct, that exact dynamics is wrong, that ghosts exist, that the theory is unitary, UV complete, globally well posed, convergent to all orders, micro-to-continuum derived, or experimentally confirmed. `c6` remains symbolic/unfixed; `beta=1` remains unauthorized; `theory established = 0%`.

## NEXT_GATE_RULE
If a Type III selector is found, terminalize it first and open a separate prospective gate testing `SELECTOR -> PHYSICAL TREATMENT`. If no selector is found, the next admissible work may only investigate prospectively new candidate-owned selector classes (microscopic derivation, quantum-state/measure selection, EFT-domain principle, initial-data selection, causal/spectral selection, resummation/analyticity) without choosing among them by desired outcome.
