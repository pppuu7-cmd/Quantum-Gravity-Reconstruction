# CLEAN_SESSION_RECOVERY_VALIDATOR_FRONTIER_NAME_REPAIR

Date: 2026-09-18
Status: PROSPECTIVE / EXECUTION-ONLY REPAIR
Parent failing run: `35359480679`
Parent recovery head: `70bac5ff6c6c275dc453e0946dee81fad9d098a8`

## Observed defect

The clean-session recovery simulation correctly recovered:
- last terminal science `CORRECTED_DEGREE6_EINSTEIN_COMPLETED_QF_DEGREE_FLOW_ADJUDICATION`;
- next preregistered science `COVARIANT_WEYL3_DIRECTIONAL_VARIATION_FUNCTIONAL_DERIVATIVE_CERTIFICATE`;
- next status `IMPLEMENTATION_IN_PROGRESS`;
- the current active question and claim locks.

It nevertheless returned `valid=false` because the validator hard-coded that both terminal and active scientific gate names must begin with `ITER`. The current legitimate gate namespace no longer obeys that historical naming convention.

## Sole authorized repair

In `code/qgr_clean_recovery_test.py`:
1. remove the `startswith('ITER')` requirement from active preregistration consistency;
2. require instead a non-empty string, nonterminal status, exact equality with `recovery_sync.latest_active_gate`, and equality of active status;
3. remove the `startswith('ITER')` requirement from terminal-state consistency;
4. require instead a non-empty terminal-science name plus a non-empty `latest_terminal_result_commit`.

No scientific authority, gate status, readiness percentage, claim lock, active question, manifest question, workflow criterion, or science implementation may be changed by this repair.

## Allowed outcomes

- `PASS_EXECUTION_ONLY_CLEAN_SESSION_FRONTIER_NAME_REPAIR`
- `BLOCKED_CLEAN_SESSION_RECOVERY_REMAINS_INCONSISTENT`

This repair is maintenance only and cannot establish or weaken any QGR scientific claim.
