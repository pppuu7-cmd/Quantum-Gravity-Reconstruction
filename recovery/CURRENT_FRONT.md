# QGR Current Research Front

Updated: 2026-09-11
Completed iteration: `Iter002`
Project phase: `MODEL_CONSTRUCTION_ACTIVE / PRE_ANSATZ`
Active roadmap stage: `R2 -> R3 boundary / 4D Lorentzian-GR seed gate`

## Canonical status

- Repository infrastructure readiness: **100%**
- Candidate-program readiness: **24%** (KMQGB R3 bookkeeping baseline; intentionally unchanged because no physical ansatz is yet promotable)
- Iter002 completion: **100%**
- Next task completion: **0%**
- Physical ansatz promoted: **NO**
- Active physical model branch: `NONE`
- Lead architecture: `A / CCRC — Constraint-Closed Relational Complex`
- Theory established: **NO**
- Independent benchmark passed: **NO**
- KMQGB `NEW_REQUIRED` authorization: **NO**

## Iter002 terminal result

Five architecture classes were prospectively compared under Constitution v1.0. Two kill rounds were executed without changing the tests after seeing outcomes.

### A / CCRC — `PASS_SCOPED_LEAD_ARCHITECTURE_NOT_YET_PHYSICAL_ANSATZ`

Kill Round 1 showed that an `S3`-invariant three-label gluing operator `K=aI+bJ`, when required to satisfy exact composition/refinement closure `K^2=K`, loses its continuous coefficient freedom and collapses to four discrete projectors. The nontrivial standard-sector projector `P=I-J/3` preserves a nonzero projected traceless relational geometry operator.

Kill Round 2 upgraded the toy to directed causal morphisms. Forward-only layer composition is associative, `P^2=P` gives an exact two-link-to-one-link coarse map, and the same nonzero geometry mode survives coarse graining without retuning or switching realization.

This is the strongest current evidence for A: **rigidity + causal composition + two-scale same-realization survival** coexist in the smallest exact toy.

Boundary: no 4D Lorentzian dimension, continuum field content, massless spin-2 sector, Einstein dynamics, physical normalization theorem, or empirical observable has been derived.

### B / CQCG — `FAIL_SCOPED_RIGIDITY_AS_STATED`

The `SU(2)`-covariant qubit depolarizing family is CPTP on a continuous interval and closes under composition `p_eff=pq`. Thus positivity + symmetry + channel composition do not determine dynamics uniquely. B is retained only as a possible operational/coarse-graining language.

### C / PCMH — `FAIL_SCOPED_RIGIDITY_MECHANISM_AS_STATED`

Binary projective refinement leaves `2^d-1` continuous split parameters by depth `d`; exact exchange symmetry removes them only by forcing uniform trivial refinement. C is retained as a cross-scale consistency requirement rather than standalone dynamics.

### D / LCSD — `PARTIAL / SPECTRUM_ONLY_NONUNIQUE`

`K_(1,4)` and `C4 + isolated vertex` are non-isomorphic but have identical adjacency spectrum `{2,-2,0,0,0}`. Spectrum alone therefore cannot uniquely reconstruct finite adjacency geometry. A full algebra/state/operator version is not refuted, but D remains underspecified and non-leading.

### E / RQEC — `FAIL_SCOPED_STANDALONE_GEOMETRY_CAUSALITY`

An exact three-qutrit one-erasure-correcting code can have maximally mixed two-qutrit reduced states `I_9/9` for every pair, so perfect recoverability need not generate adjacency, dimension, causal order or curvature dynamics. E is retained only as possible emergent robustness.

## Controlled role decomposition

The only currently permitted synthesis hypothesis is:

- `A/CCRC` = candidate microscopic rigidity/dynamics architecture;
- `C/projective consistency` = mandatory cross-scale consistency gate;
- `E/QEC` = optional emergent robustness if derived, never inserted as gravity;
- `B/channels` = possible operational-observable/coarse-map language;
- `D/spectral data` = possible diagnostic/geometric observable, not substitute for dynamics.

This is a construction policy, not yet a theory.

## Reproducibility

- `code/qgr_iter002_kill_round1.py`
- `results/ITER002_KILL_ROUND1.md`
- `code/qgr_iter002_kill_round2.py`
- `results/ITER002_KILL_ROUND2.md`
- `iterations/ITERATION_002.md`

## KMQGB synchronization

Latest inspected KMQGB head: `f503c39177012879a80bf767282a15d0c441e2f9` (Iter324-325 merge).

Relevant delta: finite source spectral `i-epsilon` does not soften the tested minimal-spin Toller short-distance pole, including the explicit causal K5 witness. The KMQGB scope guard leaves separate distributional/renormalized extensions open, does not terminally fail LQG/spinfoam, and does not authorize D7.

QGR consequence: finite definition must be prospective and structural, not a regulator choice added after divergence is observed.

## Active scientific gate — QGR Iter003

`QGR-ITER003-4D-LORENTZIAN-GR-SEED`

The lead A/CCRC architecture now faces its first genuinely gravity-specific test:

1. replace the directed chain by the smallest branching/recombining causal cell complex capable of carrying a derived local dimension notion;
2. define volume/area/distance-like relational observables without a background metric;
3. test exact gluing/refinement rigidity on that nontrivial complex;
4. construct a prospective coarse/continuum mode and ask whether a Lorentzian tensor/spin-2 sector can emerge from the same realization;
5. identify what would make Einstein/GR dynamics unavoidable or approximately universal rather than inserted by hand.

### Predeclared fatal criterion

If obtaining a 4D Lorentzian/GR regime requires inserting a continuum metric action, Einstein-Hilbert term, arbitrary spectral/action function, or gate-specific free coefficients solely to hit GR, the A branch fails the QGR reconstruction objective in its current form.

## Claim locks

Unchanged:

- existing models are not collectively declared wrong;
- a new model is not formally required by KMQGB;
- `BLOCKED` is not `FAIL`;
- QGR is not unique or correct merely because A leads the internal architecture search;
- scoped LQG results are not universal QG no-go theorems.

## Exact next action

Begin `Iter003`: construct the smallest nontrivial A/CCRC causal cell complex with branching/recombination and derive, rather than assume, a dimension/geometry candidate. Do not write an Einstein-Hilbert action as an input.
