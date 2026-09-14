# Iter054T Preregistration — G3 Weyl-Active History-to-Source/Action Map

Date: 2026-09-14

Gate: `ITER054T-G3-WEYL-ACTIVE-HISTORY-TO-SOURCE-ACTION-MAP`

Status at freeze: **PREREGISTERED BEFORE TARGETED SOURCE/ACTION SEARCH**

This gate is orthogonal to active Iter054S transport blocking. It tests the second missing arrow from Iter054R and does not use Iter054S partial outputs.

## Frozen history object

Use only the already-authorized Iter010-G3 weak-tidal same-field family:

- `kappa=0.08`;
- 24 permutation paths produced by `code/qgr_iter010_g3_common.py` from the solved six-generator Lorentz connection;
- weak static harmonic tidal tetrad / second-moment metric;
- no new background deformation or source profile.

For source/action authority search, `h=0.05` is the frozen representative finite scale because it lies in the already-used G40/G41 refinement panel. Other h values may be cited as historical controls but cannot be selected post hoc to obtain PASS.

## Scientific question

Can current QGR source/action authority map these identifiable G3 Weyl-active history/path objects into concrete branch actions `S_alpha` — or at least a concrete normalized relative action `S_alpha-S_beta` for an explicitly identified pair — without introducing a new physical source normalization, source profile, branch weight, phase datum, coupling, or matching parameter?

## Frozen obligations

### A — history identity

The candidate action datum must refer to explicit G3 history/path identities (e.g. exact permutation labels/endpoints), not merely to a generic tidal metric or symbolic history index.

### B — source assignment

Repository authority must provide an actual rule mapping the G3 history/background data to the source/boundary datum entering the action. `J(n)=beta*n` by itself is insufficient unless the relevant `n` and any remaining scale cancel or are independently fixed for the chosen relative observable.

### C — action evaluation

A tracked QGR action/phase functional must be evaluable on the same G3 history/source object. Nonzero derivative/sensitivity `dS/dc6` is not an action target. A symbolic placeholder `S_alpha` is not a computed action.

### D — normalized relative observable / transport treatment

For at least one explicit pair `(alpha,beta)`, either:

1. `S_alpha-S_beta` is source-derived and all common unresolved scales demonstrably cancel; and the treatment/comparison of `U_alpha,U_beta` is explicit; or
2. an operator-valued normalized observable retaining `U_alpha,U_beta` is explicitly defined from existing authority.

The pair may not be chosen after inspecting candidate phase values.

## Frozen search scope

Audit tracked repository authority for G8A/G19/G20/G25/G27/G28/G29/G30/G31/G32 and later source/action files, together with the G3/G40/G41 tidal realization. Search action/source/boundary/history formulas and recovery/results for an exact map into the frozen G3 histories.

## Positive controls

- Recognize G3/G40/G41 as a genuine Weyl-active same-field geometric/history-path family.
- Recognize G8A `K_alpha=24^(-1/2) exp(iS_alpha/hbar) U_alpha` as the symbolic branch-operator authority.
- Recognize G25 as showing the action can evaluate a specified source if one is supplied.
- Recognize G27 `J(n)=beta*n` as an additive source-law shape, not automatically as absolute normalization.

## Negative controls

Reject as sufficient action data:

- G4 nonzero `dPhi/dc6` sensitivity;
- symbolic `S_alpha` with no source/history evaluation;
- a manually assigned source profile on the G3 tidal metric;
- setting `beta=1`;
- G28 Weyl-inactive conformal ratios used as a Weyl-active G3 phase;
- synthetic Iter054O/P rational phase/coefficient values;
- a scalar phase observable that silently discards uncompared transport factors.

## Classification

PASS only as

`PASS_SCOPED_ITER054T_G3_HISTORY_SOURCE_ACTION_RELATIVE_PHASE_MAP_FOUND__C6_STILL_UNFIXED`

if A+B+C+D all close for at least one prospectively fixed G3 pair from existing authority.

BLOCKED as

`BLOCKED_MISSING_REQUIRED_OBJECT_ITER054T_G3_HISTORY_TO_SOURCE_ACTION_MAP`

if the G3 history is identifiable but current authority does not supply the required source/action map.

INVALID only for incomplete audit/procedure/provenance failure.

## Interpretation ceiling

PASS would close only the history-to-action object map for one scoped G3 realization. It would not fix `c6`, authorize `beta=1`, establish regulator removal/global measure, unitarity, UV completion, strong hyperbolicity, full GR recovery, experiment, new physics or theory correctness. Theory established remains 0%.