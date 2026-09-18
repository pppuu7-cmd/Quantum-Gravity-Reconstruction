# QGR Critic A/B semantic alignment repair — prospective execution-only preregistration

Date: 2026-09-18

Scope: programme-infrastructure validation only. This record authorizes exactly two repairs in `code/qgr_programme_readiness_critic.py` after run 35382792073 exposed disagreement between the primary validator and independent Critic.

Frozen observations before repair:
- primary readiness validator: 16/16 PASS;
- independent Critic: 14/16, failures A and B only;
- clean-session recovery: valid;
- all 18 negative controls: valid.

Authorized repair A: replace the Critic's obsolete requirement that every claim-lock value be false with the same semantic invariant class used by the primary validator: forbidden positive scientific claims must remain false, while protective locks `c6_symbolic_unfixed` and `corrected_q10_locked` must remain true. Also require the declared readiness semantics and experimental-confirmation false state.

Authorized repair B: remove the obsolete syntactic requirement that terminal/next gate identifiers start with `ITER`. Require instead nonempty string identifiers, presence in `CURRENT_FRONT.md`, no stale README/ROADMAP marker, and valid independent clean-session recovery.

Forbidden changes: no scientific witness, target, threshold, sign, normalization, parent discrepancy, classification, Iter049/Iter048 authority, c6 status, beta status, Q10 lock, KMQGB NEW_REQUIRED status, or active scientific question may change. No change to the A7 lower-order preregistration or its frozen contribution classes is authorized by this repair.

Success criterion: a fresh Actions run must show both primary and independent Critic 16/16 and independent agreement. Green CI remains infrastructure evidence only and is not a scientific PASS.
