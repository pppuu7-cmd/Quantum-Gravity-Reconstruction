# QGR Iteration 004 — Massless / Gauge Closure

Date: 2026-09-11
Status: `COMPLETE / LINEARIZED_GAUGE_CLOSURE_PASSED / NONLINEAR_CLOSURE_OPEN`
Current task completion: **100%**
Candidate-program readiness: **36%**
Active candidate: **QGR-L1**
Candidate state: `PROPOSED_LINEARIZED_GAUGE_CLOSED_CAUSAL_TWO_MODE`

## Objective

Determine whether masslessness and the required derivative gauge/constraint structure can follow from independently motivated relational structure rather than from setting `m=0` or inserting continuum GR by hand.

## Anti-overfitting lock

The iteration was not allowed to:

- declare `m=0`;
- choose a gauge law merely because it matches linearized GR;
- add arbitrary compensators;
- choose the GR-like member of an underdetermined family by resemblance;
- alter the previously derived causal cone solely to obtain a desired answer.

## G1-G3 — mechanisms and tensor arena

Earlier protection candidates were narrowed:

- current local lower-rank redundancy: insufficient by itself because `q^2` is invariant;
- refinement-fixed `T=I`: does not imply dynamical stationarity;
- microscopic Goldstone shift: not derived;
- cohomological origin alone: does not forbid `q^2`;
- continuous `O(1,3)` stabilizer of the incidence form: not yet an exact Boolean automorphism.

The six Boolean pair variables obey exactly

`pair6 ~= Sym^2(V3_standard_S4) = 1+3+2`,

while the rank-1 redefinition image is

`4=1+3`,

leaving the exact old two-dimensional quotient.

Detailed records:

- `results/ITER004_G1_G2_PROTECTION_AUDIT.md`
- `results/ITER004_G3_TENSOR_REPRESENTATION_AUDIT.md`

## G4 — scoped obstruction for the original six-component arena

The complete local `S4`-invariant quadratic two-derivative Hessian space on the six Boolean off-diagonal pair fields has **15** orbit coefficients.

For the natural derivative pair-boundary law

`delta x_ij = k_i u_j + k_j u_i`,

the Noether constraints have rank **15**, so the only compatible Hessian is zero.

A relative law

`delta x_ij=(k_i-k_j)(u_j-u_i)`

leaves one Hessian direction by itself, but imposing the already frozen exact local redundancy

`x_ij -> x_ij + u_i + u_j`

again leaves only the zero Hessian.

Classification:

`FAIL_SCOPED_DERIVATIVE_GAUGE_CLOSURE_FOR_CURRENT_BOOLEAN_PAIR6_TWO_DERIVATIVE_ARENA`.

This localizes the failure: QGR-L0 is too strongly pre-reduced to carry the desired derivative gauge closure.

Detailed record:

`results/ITER004_G4_DERIVATIVE_CONSTRAINT_AUDIT.md`

Reproducibility:

`code/qgr_iter004_g4_derivative_constraint_audit.py`

## G5 — natural unreduced second-moment arena

The repair was not allowed to add four diagonal fields merely because ten components are convenient.

The existing four rank-1 relational directions already define the four-dimensional permutation representation `W4`. Its symmetric second moment

`Sym^2(W4)`

has dimension **10** and a canonical split

`diag4 + offdiag6`.

The four diagonal entries can be interpreted as self-response/second-moment components of the existing rank-1 frame, not repeated Boolean events `{i,i}`.

Exact representation decomposition:

`Sym^2(W4)=2*1 + 2*3 + 2`.

On this ten-component arena, the complete `S4`-invariant quadratic two-derivative Hessian space has 38 orbit coefficients. Imposing

`delta h_ij = k_i xi_j + k_j xi_i`

leaves a **two-dimensional** nonzero Hessian family.

However no nonzero member embeds the old QGR-L0 kinetic operator unchanged on the old 2D quotient. The augmented exact matching system has full rank 39/39.

Therefore the repair cannot be cosmetic: a new pre-reduction linear candidate is required.

Classification:

`PASS_SCOPED_NATURAL_10D_SECOND_MOMENT_ARENA__FAIL_SCOPED_EXACT_QGR_L0_KINETIC_EMBEDDING`.

Detailed record:

`results/ITER004_G5_SECOND_MOMENT_ARENA.md`

Reproducibility:

`code/qgr_iter004_g5_second_moment_arena.py`

## G6 — unique causal two-mode gauge-closed branch

Let `(H0,H1)` be a deterministic exact basis of the two-dimensional gauge-compatible Hessian family and write

`H(t)=H0+t H1`.

### Selection criterion 1 — preserve the previously derived incidence cone

At a fundamental cover covector, the determinant of the six-dimensional gauge-complement block factorizes exactly as

`-(t+1)^4 (2t-1)^2 / 4`.

Thus only two projective branches make the fundamental covers characteristic:

- `t=-1`;
- `t=1/2`.

### Selection criterion 2 — reproduce the independently derived two-mode quotient

At an incidence-null covector:

- `t=-1` gives Hessian rank 3, i.e. three additional non-gauge null modes;
- `t=1/2` gives Hessian rank 4, i.e. exactly two additional non-gauge null modes beyond the four gauge directions.

Therefore the already derived two-dimensional physical quotient uniquely selects

`QGR-L1 := H0 + (1/2) H1`

up to overall normalization.

This selection uses only prior QGR data: the incidence cone and the independently derived two-mode quotient.

### Nontrivial cone checks

The selected branch has rank 4 on tested nontrivial rational covectors satisfying

`K_C(k)=k^T(J-I)k=0`,

including `(1,1,1,-1)`, `(1,2,3,-11/6)`, and `(2,-1,3,-1/4)`.

Representative non-null covectors retain rank 6.

### Mass protection

The complete onsite `S4`-invariant quadratic mass-matrix space has seven orbit coefficients. The derivative Noether identity has rank **7**, leaving

`dim allowed nonzero onsite mass deformations = 0`.

Thus linearized masslessness is now structurally protected rather than imposed.

Classification:

`PASS_SCOPED_UNIQUE_CAUSAL_TWO_MODE_DERIVATIVE_GAUGE_CLOSED_LINEARIZED_BRANCH_QGR_L1`.

Detailed record:

`results/ITER004_G6_SELECT_L1.md`

Reproducibility:

`code/qgr_iter004_g6_select_l1.py`

## A posteriori sanity check — not a selection criterion

Only after the internal QGR selection was completed, QGR-L1 was compared with the standard massless Fierz-Pauli quadratic kinetic operator written in the tetrahedral null frame whose contravariant form is

`C=J-I`.

They coincide up to overall normalization.

This is a consistency check, not the reason QGR-L1 was selected. It does **not** prove nonlinear GR, diffeomorphism invariance beyond the linearized response, or quantum gravity.

## Iter004 final decision

The Iter004 mass/gauge blocker is **closed at linearized level**.

Promoted candidate:

`QGR-L1 = PROPOSED_LINEARIZED_GAUGE_CLOSED_CAUSAL_TWO_MODE_CANDIDATE`.

QGR-L0 is retained as the six-component Lorentzian seed but is superseded as the active candidate.

### Established in scope

- natural unreduced ten-component second-moment arena from existing rank-1 relational data;
- nontrivial local derivative Noether closure;
- unique branch after prior-QGR causal-cone and two-mode criteria;
- incidence characteristic cone preserved on tested nontrivial rational null covectors;
- exactly two physical null modes on that cone;
- all `S4`-invariant onsite quadratic mass terms forbidden;
- a posteriori agreement with the known consistent massless spin-2 linear kinetic structure.

### Still open

- nonlinear gauge/constraint algebra;
- nonlinear self-coupling;
- exact microscopic derivation of the finite transformation law beyond linear response;
- Einstein equations and equivalence principle;
- same-realization refinement/continuum theorem;
- finite interacting quantum amplitude/measure;
- normalized observables;
- independent KMQGB evaluation.

## Readiness

- Iter004 completion: **100%**.
- Candidate-program readiness: **36%**.
- Readiness is a construction-roadmap metric, not probability of correctness.

## Exact next gate

`QGR-ITER005-NONLINEAR-CONSTRAINT-AND-SELF-COUPLING-CLOSURE`

Do not improve the quadratic action further. Test whether the same relational construction can generate a nonlinear completion without importing Einstein-Hilbert by hand.
