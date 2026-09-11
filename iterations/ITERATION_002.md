# QGR Iteration 002 — Architecture Selection

Date: 2026-09-11
Status: `COMPLETE`
Current task completion: **100%**
Canonical candidate-program readiness: **24%**
Physical ansatz promoted: **NO**
Lead architecture: **A / CCRC**

## Objective

Generate several genuinely distinct pre-ansatz quantum-gravity architectures under Constitution v1.0, predeclare cheap falsification tests, execute them without post-hoc criterion changes, and identify at most one lead architecture.

## Initial matrix

| Branch | Core idea | Raw score | Initial dominant risk |
|---|---|---:|---|
| A / CCRC | constraint-closed relational complex | 30/40 | may reproduce known amplitude freedom |
| B / CQCG | compositional quantum-channel geometry | 30/40 | continuous channel freedom / weak GR route |
| C / PCMH | projectively consistent causal histories | 30/40 | refinement family may remain huge |
| D / LCSD | Lorentzian causal-spectral dynamics | 29/40 | spectral nonuniqueness / arbitrary functional freedom |
| E / RQEC | relational quantum error-correcting geometry | 31/40 | coding may not derive geometry/causality/dynamics |

Raw score was never allowed to override a fatal scientific weakness.

## Kill Round 1

Artifacts:
- `code/qgr_iter002_kill_round1.py`
- `results/ITER002_KILL_ROUND1.md`

### A / CCRC
With three relational labels and exact `S3` symmetry, the invariant gluing operator `K=aI+bJ` subject to `K^2=K` loses continuous coefficient freedom and collapses to four discrete projectors. The nontrivial standard-sector projector `P=I-J/3` preserves a nonzero projected traceless relational geometry operator.

Verdict: `PASS_SCOPED_TOY_COMPOSITION_GEOMETRY_RIGIDITY`.

### C / PCMH
Binary projective refinement leaves one free split parameter per internal history, giving `2^d-1` continuous parameters by depth `d`. Exact exchange symmetry kills the freedom only by forcing uniform refinement.

Verdict: `FAIL_SCOPED_RIGIDITY_MECHANISM_AS_STATED`.

Retained role: cross-scale consistency gate.

### E / RQEC
An exact three-qutrit one-erasure-correcting code has `Tr_rest |iL><jL|=delta_ij I_3/3`, yet for the maximally mixed logical state every two-qutrit reduced state is `I_9/9`, so all pair mutual informations vanish. Exact recoverability therefore need not generate adjacency, dimension, causal order or curvature dynamics.

Verdict: `FAIL_SCOPED_STANDALONE_GEOMETRY_CAUSALITY`.

Retained role: possible emergent robustness layer.

## Kill Round 2

Artifacts:
- `code/qgr_iter002_kill_round2.py`
- `results/ITER002_KILL_ROUND2.md`

### A / CCRC directed causal upgrade
The A toy was upgraded to forward-only causal layers. The same `P=I-J/3` kernel obeys exact associative gluing `(PP)P=P(PP)=P`, and the two-link coarse kernel is exactly `P^2=P`. The same nonzero projected geometry operator survives the fine-to-coarse map without coefficient retuning or realization switching.

Verdict: `PASS_SCOPED_DIRECTED_CAUSAL_TWO_SCALE_RIGIDITY`.

### B / CQCG control
The qubit depolarizing channel `D_p(rho)=p rho+(1-p)I/2` is CPTP for a continuous interval `-1/3<=p<=1` and closes under composition as `p_eff=pq`. Positivity, rotational covariance and composition therefore do not uniquely determine dynamics.

Verdict: `FAIL_SCOPED_RIGIDITY_AS_STATED`.

Retained role: possible operational-observable/coarse-map language.

### D / LCSD control
The non-isomorphic graphs `K_(1,4)` and `C4 + isolated vertex` have different degree sequences but the identical adjacency spectrum `{2,-2,0,0,0}`. Spectral eigenvalues alone therefore do not uniquely reconstruct even finite adjacency geometry.

Verdict: `PARTIAL / SPECTRUM_ONLY_GEOMETRY_NONUNIQUE / FULL_ALGEBRAIC_VERSION_NOT_KILLED`.

Retained role: possible diagnostic/geometric observable.

## Terminal Iter002 decision

A/CCRC is the **unique current lead architecture**, because it alone survived both predeclared cheap-kill rounds while maintaining exact low-freedom composition and same-realization two-scale survival.

This is not a truth claim. A has not yet derived:

- four macroscopic dimensions;
- Lorentzian signature from relational data;
- a continuum tensor/spin-2 mode;
- Einstein/GR dynamics;
- a full finite-definition theorem beyond finite toys;
- a normalized empirical observable.

Therefore A is **not yet promoted to a physical QGR ansatz** and the canonical candidate-program readiness remains **24%**.

## Controlled subordinate roles

The only permitted cross-architecture synthesis at the next stage is prospective and role-limited:

- A/CCRC: candidate microscopic rigidity/dynamics architecture;
- C/projective consistency: cross-scale gate;
- E/QEC: optional emergent robustness if derived;
- B/channels: operational/coarse-map language if required;
- D/spectral data: diagnostic/geometric constraints if required.

None may be added later solely to rescue a failed A gate.

## KMQGB synchronization

Latest inspected KMQGB head: `f503c39177012879a80bf767282a15d0c441e2f9`, containing Iter324-325 source spectral-epsilon audits. In the tested minimal-spin Toller objects, finite source spectral `i-epsilon` does not soften the short-distance pole; the explicit scope guard leaves a separate distributional/renormalized extension open and does not authorize D7.

QGR consequence: finite definition must be prospective and structural, not an after-the-fact regulator choice.

## Next iteration

`QGR Iter003 — 4D Lorentzian/GR Seed Gate`

Predeclared fatal rule: if a 4D Lorentzian/GR regime can only be obtained by inserting a background metric, Einstein-Hilbert action, arbitrary continuum/spectral function, or gate-specific free coefficients to hit the target, reject A/CCRC in its current reconstruction form.
