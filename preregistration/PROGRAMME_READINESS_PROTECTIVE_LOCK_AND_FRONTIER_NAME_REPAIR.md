# PROGRAMME_READINESS_PROTECTIVE_LOCK_AND_FRONTIER_NAME_REPAIR

Date: 2026-09-18
Status: PROSPECTIVE / EXECUTION-ONLY VALIDATOR REPAIR
Parent failing run: `35364342296`
Parent head: `b56bd1aebecbe1916e00fd1ed4547fbe3ac4c463`

## Raw observed defect

The clean-session recovery simulation itself is now valid, but the primary programme-readiness validator still reports obligations A=false and B=false.

A is false because it requires `all(v is False for v in state['claim_locks'].values())`. The current schema intentionally contains affirmative protective locks such as `c6_symbolic_unfixed=true` and `corrected_q10_locked=true`; these are conservative restrictions, not unauthorized scientific claims.

B is false because the primary validator independently retains the obsolete `startswith('ITER')` naming assumption for terminal and preregistered gates, although the legitimate current gate names are descriptive non-ITER identifiers.

## Sole authorized repair

In `code/qgr_programme_readiness_validator.py` only:

1. Replace obligation A's blanket all-false test by an explicit denylist of claim flags that must remain false. Require `c6_symbolic_unfixed is True` and `corrected_q10_locked is True` as protective locks.
2. Replace obligation B's `startswith('ITER')` tests by non-empty-string tests plus presence of the exact terminal and next gate names in `CURRENT_FRONT.md`; retain the independent `recovery_run()['valid'] is True` requirement.
3. Do not change any scientific authority, gate, threshold, witness, target, claim-lock value, readiness declaration, active question, or scientific implementation.

## Frozen allowed outcomes

- `PASS_EXECUTION_ONLY_PROGRAMME_READINESS_VALIDATOR_REPAIR`
- `BLOCKED_PROGRAMME_READINESS_VALIDATOR_REMAINS_INCONSISTENT`

This maintenance repair cannot establish scientific PASS, theory correctness, experimental confirmation, beta=1, fixed c6, quantum unitarity, global measure closure, UV completion, new physics, or KMQGB NEW_REQUIRED.