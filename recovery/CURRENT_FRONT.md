# QGR Current Research Front

Updated: 2026-09-11
Iteration: `Iter002`
Project phase: `MODEL_CONSTRUCTION_ACTIVE / PRE_ANSATZ`
Active roadmap stage: `R2 — ontology search / rigidity selection`

## Canonical status

- Repository infrastructure readiness: **100%**
- Candidate-program readiness: **24%** (external KMQGB R3 bookkeeping baseline; unchanged until a branch satisfies the full pre-ansatz promotion rule)
- Current iteration completion: **78%**
- Physical ansatz promoted: **NO**
- Active physical model branch: `NONE`
- Lead architecture for next kill gate: `A / CCRC`
- Theory established: **NO**
- Independent benchmark passed: **NO**
- KMQGB `NEW_REQUIRED` authorization: **NO**

## Iter002 result so far

The QGR-G0 architecture matrix was generated prospectively under Constitution v1.0 and Kill Round 1 has now been executed on the three predeclared priority branches.

### A / CCRC — `PASS_SCOPED / LEAD_BRANCH / NOT_PROMOTABLE`

In the exact `S3` three-label toy, an invariant gluing operator has form `K=aI+bJ`. Exact composition/refinement closure `K^2=K` collapses the continuous coefficient family to four discrete projectors. The nontrivial standard-sector projector `P=I-J/3` preserves a nonzero projected traceless relational geometry operator. Thus composition, nonzero geometry and rigidity all pass at toy scope.

This does **not** yet establish causal orientation, continuum closure, 4D Lorentzian geometry, GR dynamics or an operational observable.

### C / PCMH — `FAIL_SCOPED_RIGIDITY_MECHANISM_AS_STATED`

Binary projective refinement `p(h)=p(h0)+p(h1)` leaves one continuous split parameter per internal history. At depth `d`, the positive classical subcase already contains `2^d-1` free split parameters. Exact child-exchange symmetry removes them only by forcing uniform `q_h=1/2` refinement. Therefore projective consistency is retained as a valuable cross-scale gate, but rejected as sufficient standalone dynamics.

### E / RQEC — `FAIL_SCOPED_STANDALONE_GEOMETRY_CAUSALITY`

An exact three-qutrit one-erasure-correcting code was used as a counterexample. Recovery/isometry is exact, yet for the maximally mixed logical state every two-qutrit reduced density matrix is `I_9/9`, hence every pair mutual information vanishes. Strong recoverability therefore need not generate adjacency, dimension, causal orientation or curvature dynamics. QEC remains admissible as an emergent robustness layer, not as standalone gravity dynamics.

Reproducibility: `code/qgr_iter002_kill_round1.py`.
Detailed record: `results/ITER002_KILL_ROUND1.md`.

## Strongest current model-design result

The first useful decomposition of roles is now evidence-backed at toy scope:

- **A-style constraint closure** is the current best rigidity generator.
- **C-style projective consistency** is better treated as a same-realization/refinement constraint than as the source of dynamics.
- **E-style QEC/recoverability** is better treated as a possible emergent robustness/encoding property than as the source of geometry and causality.

A possible future synthesis `A dynamics + C consistency gate + optional E robustness` is only `CONJECTURED`. It is not yet a QGR model.

## KMQGB synchronization

Fresh KMQGB Iter324-325 was inspected. In its explicit minimal-spin Toller tests, finite source spectral `i-epsilon` does not soften the tested short-distance pole, including the full causal K5 witness. KMQGB explicitly states that this does not exclude a separately specified distributional/renormalized extension, does not terminally fail LQG/spinfoam, and does not authorize D7.

QGR consequence: keep the frozen finite-definition obligation. A candidate should derive its finite/extension mechanism from construction rather than select a regulator after encountering a divergence.

## Active scientific gate — QGR-G0-KILL-ROUND-2-A-CAUSAL-REFINEMENT

1. Upgrade A/CCRC from the undirected `S3` toy to a directed causal relational complex.
2. Demand exact gluing associativity/refinement compatibility with causal orientation present.
3. Test whether the low-dimensional/discrete coefficient closure survives causal directionality.
4. Add a two-scale coarse-graining map and require the same nonzero geometry mode to survive in one realization.
5. Run cheap control tests on B/CQCG and D/LCSD before any branch promotion.

## Promotion rule

No architecture becomes “the QGR model” unless it:

- triggers no fatal gate;
- passes at least three prospective cheap kill tests;
- has explicit/bounded residual functional freedom;
- has a concrete finite-definition mechanism;
- has a plausible same-realization UV-to-IR path;
- has an explicit route toward causal 4D Lorentzian/GR recovery rather than only a kinematic toy.

A/CCRC has now passed the first three toy tests but **has not yet passed the remaining promotion obligations**.

## Claim locks

Unchanged:

- existing models are not collectively declared wrong;
- a new model is not formally required by KMQGB;
- `BLOCKED` is never silently converted to `FAIL`;
- QGR is not called unique or correct;
- theory-specific LQG extension results are not universalized into quantum-gravity no-go claims.

## Exact next action

Execute `QGR-G0-KILL-ROUND-2-A-CAUSAL-REFINEMENT`, with B and D as comparison controls. Do not write a preferred physical action/amplitude until directed causal closure and two-scale same-realization survival have been tested.
