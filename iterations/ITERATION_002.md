# QGR Iteration 002 — Architecture Matrix and Kill Round 1

Date: 2026-09-11
Status: `ACTIVE / KILL_ROUND_1_COMPLETE / ROUND_2_QUEUED`
Current task completion: **78%**
Canonical candidate-program readiness: **24%** (held fixed pending full pre-ansatz promotion)
Physical ansatz promoted: **NO**

## Objective

Generate multiple genuinely distinct pre-ansatz architectures under Constitution v1.0, declare cheap falsification tests before computation, and select at most one lead architecture without forcing a winner.

## Initial architecture matrix

| Branch | Core idea | Raw score | Initial risk |
|---|---|---:|---|
| A / CCRC | constraint-closed relational complex | 30/40 | could reproduce known amplitude/counterterm freedom |
| B / CQCG | compositional quantum-channel geometry | 30/40 | weak intrinsic Lorentzian/GR route |
| C / PCMH | projectively consistent causal measure on histories | 30/40 | compatible measure family may remain huge |
| D / LCSD | Lorentzian causal-spectral dynamics | 29/40 | arbitrary spectral function / weak composition |
| E / RQEC | relational quantum error-correcting geometry | 31/40 | coding structure may not derive gravity dynamics |

Raw score was explicitly forbidden from selecting the winner. E had the highest initial score but was not promoted because its weakest dimension was a potentially fatal GR/causality obligation.

## Predeclared Kill Round 1

Priority branches were A, C and E because they represented three different proposed rigidity mechanisms:

- A: exact constraint/gluing closure;
- C: projective/refinement consistency;
- E: isometric/recoverability consistency.

Detailed derivation: `results/ITER002_KILL_ROUND1.md`.
Reproducibility: `code/qgr_iter002_kill_round1.py`.

## Result A / CCRC

Scoped toy: three relational labels with full `S3` symmetry. The most general invariant gluing operator is `K=aI+bJ`. Exact refinement/composition closure `K^2=K` forces the trivial and standard irreducible eigenvalues into `{0,1}`. Hence the continuous two-parameter family collapses to four discrete projectors: `0`, `I`, `J/3`, `I-J/3`.

For `G=diag(-1,0,1)`, the standard-sector projector `P=I-J/3` satisfies `PGP != 0`, while `P^2=P` exactly.

Predeclared verdicts:

- A1 composition/refinement: `PASS_SCOPED`;
- A2 nonzero relational geometry: `PASS_SCOPED`;
- A3 coefficient rigidity: `PASS_SCOPED`.

Classification: `PASS_SCOPED / LEAD_BRANCH / NOT_PROMOTABLE`.

Boundary: no causal direction, continuum theorem, 4D Lorentzian limit, GR dynamics, or normalized operational observable has yet been derived.

## Result C / PCMH

In the positive binary-refinement subcase,

`p(h)=p(h0)+p(h1)`

allows

`p(h0)=q_h p(h)`, `p(h1)=(1-q_h)p(h)`

with one free `q_h` per internal history. At refinement depth `d`, the number of free split parameters is `2^d-1`; depths 1..6 give `1,3,7,15,31,63`.

Exact child-exchange symmetry fixes `q_h=1/2`, but then the refinement is the unique uniform split and local dynamics has been trivialized rather than dynamically derived.

Classification: `FAIL_SCOPED_RIGIDITY_MECHANISM_AS_STATED`.

Retained value: projective consistency remains a strong cross-scale/same-realization gate, but not the standalone source of dynamics.

## Result E / RQEC

Exact witness: the three-qutrit code

`|0L>=(|000>+|111>+|222>)/sqrt(3)`,

`|1L>=(|012>+|120>+|201>)/sqrt(3)`,

`|2L>=(|021>+|102>+|210>)/sqrt(3)`.

For every single site,

`Tr_rest |iL><jL| = delta_ij I_3/3`,

so any one-qutrit erasure is exactly correctable. Yet for the maximally mixed logical state every two-qutrit reduced state equals `I_9/9`; all pair mutual informations vanish exactly.

Therefore exact recoverability/isometry need not generate adjacency, spatial dimension, causal direction or curvature dynamics.

Classification: `FAIL_SCOPED_STANDALONE_GEOMETRY_CAUSALITY`.

Retained value: QEC may still be an emergent robustness/encoding mechanism inside another architecture.

## Current scientific synthesis

The first evidence-backed role separation is:

`A-style constraint closure = candidate rigidity generator`

`C-style projective consistency = cross-scale gate`

`E-style QEC = possible emergent robustness layer`.

A later combination of these roles is only `CONJECTURED`. It is not yet a physical model and no terms may be added merely to rescue a failed gate.

## KMQGB delta incorporated

Fresh KMQGB Iter324-325 was checked. In its explicit minimal-spin Toller probes, finite source spectral `i-epsilon` does not remove the tested short-distance pole, including the full causal K5 witness. The KMQGB scope guard explicitly leaves separately specified distributional/renormalized extensions open and does not authorize D7.

QGR implication: the finite-definition mechanism must be generated prospectively by the construction; a regulator chosen only after divergence is detected will not count as closure.

## Exact next gate — Kill Round 2

`QGR-G0-KILL-ROUND-2-A-CAUSAL-REFINEMENT`

1. Replace the undirected A toy with a directed causal relational complex.
2. Demand exact associative gluing/refinement compatibility with orientation present.
3. Check whether coefficient freedom remains discrete/low-dimensional.
4. Construct an explicit two-scale coarse map and require a nonzero geometry mode to survive in the same realization.
5. Run cheap comparison-control tests on B/CQCG and D/LCSD before considering A for promotion.

## Readiness decision

- Iter002 completion: **78%**.
- Candidate-program readiness: **24%**, intentionally unchanged.
- Lead architecture: **A/CCRC**, but only at `PASS_SCOPED` level.
- Physical ansatz: **none**.

The readiness percentage will not be increased merely because one toy is encouraging. It moves only after the causal/two-scale gate establishes that the same rigidity mechanism survives beyond the smallest symmetric example.
