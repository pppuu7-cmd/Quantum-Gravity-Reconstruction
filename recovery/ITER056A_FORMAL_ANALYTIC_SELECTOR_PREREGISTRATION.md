# Iter056A preregistration — formal/analytic perturbative-sector selector sufficiency

Date: 2026-09-14
Gate: `ITER056A-FORMAL-ANALYTIC-PERTURBATIVE-SECTOR-SUFFICIENCY`

## Frozen question
In the same exact scalar mixed-order control used by Iter055Z, does restricting the solution family to a regular formal power series in the higher-derivative parameter exclude the singular fast branch and leave only the lower-order/GR sector?

This tests mathematical sufficiency of a possible future treatment principle. It does not test whether QGR currently authorizes that principle; Iter054G-R already says it does not.

## Frozen control

`u''(t)+eps u''''(t)=0`, `eps>0`,

with lower-order equation `u''=0` and exact fast roots `+- i/sqrt(eps)`.

Assume a regular formal series

`u(eps,t)=sum_{n=0}^infinity eps^n u_n(t)`

with sufficiently smooth coefficient functions for termwise differentiation. A convergent analytic family is a special case.

## Frozen obligations
1. Substitute the formal series and derive the exact recurrence for `u_n`.
2. Determine whether the recurrence forces every coefficient `u_n` to lie in the lower-order solution space.
3. Compare against the Iter055Z beyond-all-orders witness `exp(-1/eps) sin(t/sqrt(eps))` and state whether it belongs to the regular formal/analytic sector.
4. Distinguish **formal power-series selection** from mere `C^infinity` dependence/extension at `eps=0`; a flat beyond-all-orders term can have zero Taylor series without being represented by that series.
5. If the formal sector excludes the fast branch, state exactly what remains free (analytic `a(eps),b(eps)` lower-order data) and what additional QGR source authority would still be needed.
6. Make no tensorial QGR mode/ghost/stability claim.

## Frozen classifications
- `PASS_SCOPED_ITER056A_FORMAL_POWER_SERIES_SECTOR_EXCLUDES_SINGULAR_FAST_BRANCH_IN_CONTROL__QGR_AUTHORITY_STILL_MISSING` if the recurrence contains only lower-order coefficient functions and the fast branch is beyond the regular formal sector.
- `FAIL_SCOPED_ITER056A_FORMAL_POWER_SERIES_SECTOR_STILL_CONTAINS_NONTRIVIAL_FAST_BRANCH` if a nonzero fast-branch family admits the frozen regular formal representation.
- `INVALID_ITER056A_FORMAL_RECURRENCE_NOT_WELL_DEFINED` only if termwise substitution cannot realize the frozen control.

## Interpretation ceiling
A PASS identifies a mathematically sufficient **candidate** perturbative-sector principle in this scalar control. It does not authorize it for QGR, derive order reduction of the full tensor equations, control remainders/nonperturbative sectors, define initial data, or establish hyperbolicity, unitarity, UV/GR/experiment/theory claims.

No GitHub Actions run is preregistered; this is exact formal-series analysis.
