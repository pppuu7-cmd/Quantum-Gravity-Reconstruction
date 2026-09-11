# QGR Iter002 — Kill Round 1 Results

Date: 2026-09-11
Scope: pre-ansatz toy mathematics only
Constitution: `docs/CONSTITUTION.md` v1.0
Reproducibility script: `code/qgr_iter002_kill_round1.py`

## Executive result

Three predeclared branches were tested without changing the tests after seeing outcomes.

- **A / CCRC**: `PASS_SCOPED_TOY_COMPOSITION_GEOMETRY_RIGIDITY`
- **C / PCMH**: `FAIL_SCOPED_RIGIDITY_MECHANISM_AS_STATED`
- **E / RQEC**: `FAIL_SCOPED_STANDALONE_GEOMETRY_CAUSALITY`

No physical QGR ansatz is promoted. A/CCRC becomes the **lead architecture for the next kill gate**, not the theory.

---

## A / CCRC — Constraint-Closed Relational Complex

### Toy definition
Take three relational labels transformed transitively by `S3`. Any `S3`-invariant linear gluing operator has the form

`K = a I + b J`,

where `J` is the all-ones matrix. Exact refinement/composition consistency is represented by

`K^2 = K`.

The two irreducible eigenvalues are

- `lambda_std = a` on the two-dimensional standard representation;
- `lambda_triv = a + 3b` on the one-dimensional trivial representation.

Idempotence therefore forces each eigenvalue to lie in `{0,1}`. The continuous `(a,b)` freedom collapses to four discrete projectors:

- `0`;
- `I`;
- `J/3`;
- `I - J/3`.

Thus the toy has **zero continuous coefficient freedom** after exact symmetry + composition closure.

### Geometry witness
Use the traceless relational observable

`G = diag(-1,0,1)`.

For the trivial projector `P0=J/3`, `P0 G P0 = 0`.

For the standard-sector projector `Pstd=I-J/3`,

`Pstd G Pstd != 0`.

Its nonzero eigenvalues are `+-1/sqrt(3)`, so a nontrivial relational geometric observable survives exact gluing/refinement projection without a continuum metric being inserted.

### Test verdicts

- A1 composition/refinement: **PASS_SCOPED** (`Pstd^2=Pstd` exactly).
- A2 nonzero geometry: **PASS_SCOPED** (`Pstd G Pstd != 0`).
- A3 rigidity: **PASS_SCOPED** (continuous two-parameter invariant operator family collapses to four discrete projectors; two nontrivial).

### Boundary
This does **not** establish causal propagation, a continuum limit, 4D Lorentzian geometry, Einstein dynamics, or a physical observable. It only shows that the proposed closure mechanism can be genuinely rigid and nontrivial in the smallest symmetric toy.

**Status:** `PASS_SCOPED / LEAD_BRANCH / NOT_PROMOTABLE`.

---

## C / PCMH — Projectively Consistent Causal Measure on Histories

### Toy definition
Consider positive binary refinement, already a subcase of any richer quantum-measure construction. Every parent history `h` splits into `h0,h1`, with projective consistency

`p(h)=p(h0)+p(h1)`.

The general positive refinement is

`p(h0)=q_h p(h)`,
`p(h1)=(1-q_h)p(h)`,

with one independent `q_h in [0,1]` per internal history.

At binary depth `d`, the number of independent split parameters is

`N_free(d)=2^d-1`.

For depths 1..6 this gives `1,3,7,15,31,63`.

### Consequence
Projective consistency by itself therefore does not generate rigidity; freedom grows exponentially with refinement depth.

Imposing exact exchange symmetry at every split forces `q_h=1/2`, which removes the freedom but also gives the unique uniform refinement. In this toy, rigidity is obtained by trivializing all local split dynamics rather than deriving nontrivial dynamics.

### Test verdicts

- C1 projective consistency: **PASS_SCOPED_EXISTENCE** — compatible refinements exist abundantly.
- C2 freedom-count/rigidity: **FAIL_SCOPED** — one new continuous split parameter per internal history; exponential growth.
- C3 normalized causal measure: **PASS_SCOPED only for chosen refinements**, but normalization does not fix the `q_h` family.

### Boundary
This does not prove that every projective-limit quantum-gravity construction fails. It refutes the **specific proposed rigidity mechanism** `projective consistency + normalization (+ naive local symmetry)` as sufficient by itself. Any rescue requires an additional dynamical principle and therefore constitutes a redesigned branch, not a post-hoc pass of the original C branch.

**Status:** `FAIL_SCOPED_RIGIDITY_MECHANISM_AS_STATED`; retain projective consistency as a useful supporting principle, not as standalone dynamics.

---

## E / RQEC — Relational Quantum Error-Correcting Geometry

### Exact code witness
Use the three-qutrit code

`|0L>=(|000>+|111>+|222>)/sqrt(3)`

`|1L>=(|012>+|120>+|201>)/sqrt(3)`

`|2L>=(|021>+|102>+|210>)/sqrt(3)`.

For every physical site and logical indices `i,j`, exact partial tracing gives

`Tr_rest |iL><jL| = delta_ij I_3/3`.

Hence erasure of any one qutrit is exactly correctable.

However, for the maximally mixed logical state

`rho=(1/3) sum_i |iL><iL|`,

every two-qutrit reduced state is exactly

`rho_ab = I_9/9`.

Therefore every pair mutual information is exactly zero.

### Consequence
Strong isometry/recoverability can exist while pairwise relational information supplies **no adjacency signal at all**. The code condition also contains no intrinsic time orientation, so causal order is not derived from recoverability alone. No curvature evolution equation follows from the coding property.

### Test verdicts

- E1 background-independent adjacency/dimension: **FAIL_SCOPED_STANDALONE** — exact recoverability need not yield any pairwise geometry signal.
- E2 intrinsic causality: **FAIL_SCOPED_STANDALONE** — isometric code conditions carry no directed causal order.
- E3 gravity dynamics: **FAIL_SCOPED_STANDALONE** — no curvature dynamics follows from the code property.

### Boundary
This does not refute quantum error correction as a mechanism inside quantum gravity. It only rejects QEC/recoverability as the **standalone source of geometry + causality + dynamics** in the present branch. QEC remains admissible as an emergent robustness/encoding layer in another architecture.

**Status:** `FAIL_SCOPED_STANDALONE_GEOMETRY_CAUSALITY`; retain as possible submechanism.

---

## Cross-branch conclusion

The first kill round distinguishes three roles:

1. **A/CCRC** currently supplies the strongest candidate **rigidity generator**.
2. **C/PCMH** supplies a valuable **same-realization/refinement consistency condition**, but not dynamics by itself.
3. **E/RQEC** supplies a potentially valuable **robustness/encoding mechanism**, but not geometry/causality/dynamics by itself.

This suggests a disciplined synthesis hypothesis for later testing, not yet a model:

`A-style constraint-closed relational dynamics`
`+ C-style projective/refinement consistency as a gate`
`+ optional E-style error-correcting robustness as an emergent property`.

The synthesis is **CONJECTURED** and must not be treated as a pass until prospective tests are written and executed.

## KMQGB synchronization note

Fresh KMQGB Iter324-325 strengthens the importance of QGR's finite-definition obligation: keeping the published spectral `i-epsilon` finite did not soften the tested minimal-spin Toller short-distance pole, including the explicit causal K5 witness. KMQGB itself explicitly scopes this as not excluding a separate distributional/renormalized extension and not authorizing D7. QGR therefore should prefer a finite/extension mechanism generated by its construction rather than an externally chosen regulator.

## Exact next gate

`QGR-G0-KILL-ROUND-2-A-CAUSAL-REFINEMENT`:

1. Upgrade A/CCRC from undirected `S3` toy labels to a directed causal relational complex.
2. Require exact gluing associativity and refinement compatibility in the directed case.
3. Test whether rigidity survives once causal orientation is present.
4. Construct a two-scale coarse-graining map and test whether a nonzero geometry mode survives in the same realization.
5. In parallel, run cheap control tests on B/CQCG and D/LCSD to ensure A is not selected merely because the other branches were tested less deeply.

No preferred action or amplitude is to be written before this gate closes.
