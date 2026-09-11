# QGR Iteration 005 — Nonlinear Constraint and Self-Coupling Closure

Date: 2026-09-11
Status: `ACTIVE / G1A_ZERO_DERIVATIVE_CUBIC_SECTOR_CLOSED`
Current task completion: **15%**
Candidate-program readiness: **36%**
Active candidate: **QGR-L1**

## Starting authority

Iter004 closed the linearized mass/gauge blocker. QGR-L1 is a ten-component second-moment response field on

`Sym^2(W4)`

with a uniquely selected local derivative-gauge-compatible quadratic Hessian, incidence characteristic cone, exactly two physical null modes on that cone, and no allowed `S4`-invariant onsite quadratic mass deformation.

This iteration does **not** assume a nonlinear GR completion.

## Objective

Determine whether the same relational/incidence/composition structure can generate a nonlinear completion of QGR-L1 with a closed constraint algebra and low-dimensional self-coupling freedom.

## Fixed anti-overfitting rules

Forbidden shortcuts:

- insert Einstein-Hilbert because it is known to self-couple consistently;
- import the full nonlinear diffeomorphism transformation law as an axiom;
- add arbitrary functions/counterterms after a failed closure equation;
- change the QGR-L1 quadratic kinetic cone solely to make cubic closure work;
- use a different microscopic realization for the nonlinear and linear sectors.

Any later match to GR is allowed only as an a posteriori comparison after QGR-internal selection.

## G1A — zero-derivative cubic potential census

The active field representation has character

`chi_H=[10,4,2,1,0]`.

The exact character of `Sym^3(H)` is

`[220,32,12,4,0]`,

whose trivial `S4` multiplicity is exactly **20**.

Therefore finite `S4` symmetry alone permits 20 independent algebraic cubic invariants.

### Gauge elimination

For constant `h` and affine gauge parameter `xi`, the already derived linear gauge law

`delta_0 h_ij = D_i xi_j + D_j xi_i`

spans arbitrary constant symmetric shifts in all ten components. A derivative quadratic action carries no constant-field term capable of cancelling an arbitrary variation of a nonconstant algebraic cubic potential.

Hence gauge invariance requires

`V_3(h)=0`.

All **20/20** zero-derivative cubic directions are excluded.

Classification:

`PASS_SCOPED_20_S4_CUBIC_POTENTIALS_CENSUSED_AND_ALL_EXCLUDED_BY_DERIVED_AFFINE_GAUGE_SHIFT`.

Authoritative record:

`results/ITER005_G1A_CUBIC_POTENTIAL_CENSUS.md`

Reproducibility:

`code/qgr_iter005_g1a_cubic_potential_census.py`

## G1B — active gate

`QGR-ITER005-G1B-TWO_DERIVATIVE_CUBIC_CENSUS_AND_NOETHER_SYSTEM`

1. Enumerate local `S4`-invariant cubic terms with exactly two first-neighbor derivatives.
2. Quotient obvious integration-by-parts and field-permutation redundancies.
3. Derive the most general first nonlinear gauge correction allowed by relational frame composition.
4. Solve

   `delta_0 S_3 + delta_1 S_2 = 0`

   as an exact linear system in cubic couplings and gauge-correction coefficients.
5. Count surviving coupling directions before any comparison with Einstein-Hilbert.

## G2 — nonlinear algebra closure

If G1B produces a nontrivial candidate, compute the commutator of two deformed gauge transformations and determine whether it closes on the existing parameter space without new arbitrary generators.

## G3 — causal cone stability

Check weak nonlinear backgrounds for preservation/deformation of the incidence cone. A deformation is not automatically a failure, but it must be derived, causal, and controlled rather than fitted.

## G4 — same-realization refinement handoff

Only after local nonlinear closure survives, begin refinement/coarse-graining on the same QGR-L1 realization. Do not splice a separate continuum theory into the IR.

## Claim locks

Until Iter005 closes positively:

- QGR is not a nonlinear gravity theory;
- Einstein equations are not derived;
- equivalence principle is not derived;
- nonlinear diffeomorphism invariance is not established;
- a posteriori Fierz-Pauli agreement does not authorize Einstein-Hilbert completion;
- KMQGB `NEW_REQUIRED` remains unauthorized.

## Recovery

Read in order:

1. `recovery/state.json`
2. `recovery/CURRENT_FRONT.md`
3. this file
4. `iterations/ITERATION_004.md`
5. `results/ITER004_G6_SELECT_L1.md`
6. `results/ITER005_G1A_CUBIC_POTENTIAL_CENSUS.md`
7. `docs/CONSTITUTION.md`
