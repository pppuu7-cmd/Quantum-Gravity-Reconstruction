# Iter057AO Critic v2 execution-only schema defect

Date: 2026-09-17
Parent preregistration: `e1ded07e5050763ecb707dad679b78286fe04744`
Frozen Critic v2 commit: `6e142899f582f281bfe7507948bc5d0bfaf1fc66`
Critic workflow head: `7ec4083ffb0ef94f068c7a9c8ee6030134562988`
Critic run: `35174885633`

## Defect

The phase-2 constructor was frozen before held-out evaluation and writes every negative-control result with both:

- top-level `detected: true/false`, and
- `controls.defect_detected: true/false`.

The frozen Critic v2 mistakenly queried `control.defect_detected` (singular `control`). Therefore the predicate evaluated false for all negative-control artifacts even though each artifact itself records `detected=true` and `controls.defect_detected=true`.

This is a parser/schema implementation defect in the Critic. It does not alter the preregistered scientific requirement: each frozen defect must be detected for the intended reason. No generic or held-out numerical/scientific value is used to choose this repair.

## Allowed repair

Critic v3 may replace only the malformed field lookup with the exact pre-existing artifact schema predicate

`artifact['detected'] is True and artifact['controls']['defect_detected'] is True`.

All other Critic predicates, source hashes, seeds, formulas, replay rules and terminal classifier remain byte-for-byte semantically unchanged. Critic v2 remains preserved as a historical technical failure and is not reclassified as scientific evidence.