# QGR Iteration 004 — Massless / Gauge Closure

Date: 2026-09-11
Status: `ACTIVE / MECHANISM_MATRIX_FROZEN`
Current task completion: **20%**
Candidate-program readiness: **30%**
Active candidate: `QGR-L0` proposed linearized pair-incidence ansatz

## Objective

Determine whether masslessness and the required gauge/constraint structure follow from an independently motivated relational/refinement principle rather than from setting a mass parameter to zero because GR requires it.

## Fixed anti-overfitting rule

A mechanism fails if it:

- simply declares `m=0`;
- introduces a gauge symmetry only after observing the desired two-mode spectrum;
- adds arbitrary compensator functions;
- requires a critical parameter to be tuned to an isolated value with no structural reason;
- changes the G5 kinetic cone solely to match GR.

At least four mechanisms are compared before selection.

---

## M1 — Local relational-frame / constraint redundancy

### Idea
Promote the existing rank-1 redefinitions to a genuinely local relational-frame principle and determine whether exact composition generates a first-class/constraint-like algebra strong enough to constrain the full six pair variables and interactions.

The already derived algebraic redundancy is

`x(n) -> x(n)+M^T u(n)`.

It is local because `P_phys M^T=0` cell by cell, even for spacetime-dependent `u(n)`. It removes the `1+3` lower-rank sectors exactly.

### Required new result
A Ward/constraint identity must forbid an onsite potential for the physical quotient `q=P_phys x`, rather than merely remove unphysical components.

### Cheap kill test
Construct the most general local quadratic action invariant under `x -> x+M^T u(n)`. If `q·q` remains allowed, M1 alone does not protect masslessness.

### Preliminary status
`PARTIAL`: G6 already shows `q·q` is invariant, so the currently known algebraic frame redundancy is insufficient by itself. A stronger derivative/first-class closure would have to be derived, not declared.

---

## M2 — Exact refinement fixed-background protection

### Idea
Use the earlier exact nonzero refinement branch `T=I`: a uniform physical quotient deformation that survives refinement may have to remain a zero-cost/stationary background under the same microscopic dynamics.

If every constant refinement-fixed `q=c` is required to be a physical stationary background, then any local potential with nonzero quadratic curvature at `q=0` is forbidden, including `m^2 q^2`.

### Cheap kill test
Separate kinematic refinement from dynamical stationarity. Determine whether the CCRC axioms actually imply

`refinement-fixed constant configuration => stationary physical configuration`.

If not, M2 is only an extra assumption and cannot protect masslessness.

### Preliminary status
`PROMISING / UNPROVED`.

---

## M3 — Continuous Goldstone/shift protection

### Idea
Interpret the G5 global shift `q(n)->q(n)+c` as the remnant of a continuous microscopic symmetry, making the two modes Goldstone-like and forbidding mass.

### Cheap kill test
Identify the continuous microscopic symmetry and its generator before invoking spontaneous breaking.

### Preliminary status
`FAIL_SCOPED_AS_CURRENT_MICROSCOPIC_MECHANISM`: the exact finite local automorphism supplied so far is discrete `S_4` plus lower-rank redefinitions; no continuous symmetry acting as `q->q+c` has been derived. Goldstone protection remains possible only as a later emergent mechanism, not as current microscopic evidence.

---

## M4 — Cohomological / curvature-only protection

### Idea
Treat the 2D quotient as a cohomological or curvature-like variable, hoping that gauge origin forbids a mass term.

### Cheap kill test
Check whether `q·q` is invariant under the proposed lower-rank gauge structure.

### Preliminary status
`FAIL_SCOPED_AS_STANDALONE_MASS_PROTECTION`: G6 already establishes that `q` is gauge invariant, so `q·q` is gauge invariant too. Curvature/cohomology origin alone does not forbid an onsite mass.

---

## M5 — Symmetry enhancement under refinement

### Idea
The microscopic cell has finite `S_4` symmetry, but repeated null tetrahedral frames might acquire a continuous local Lorentz/frame redundancy in a controlled refinement limit. If the full constant `q` family is then related by emergent local frame transformations, an onsite potential selecting one `q` would violate the enhanced symmetry.

### Cheap kill tests
1. Determine the exact continuous stabilizer of the Lorentzian pair form `C=J-I`.
2. Determine whether any non-discrete part of that stabilizer is realized by allowed microscopic/refinement transformations rather than by an external embedding.
3. Reject if continuous enhancement is merely assumed in the continuum.

### Preliminary status
`OPEN / HIGH_VALUE_BUT_HIGH_RISK`.

---

## Initial decision

No protection mechanism is adopted yet.

Two mechanisms are already insufficient as standalone explanations:

- M3 current microscopic Goldstone protection;
- M4 cohomological origin alone.

The active comparison is therefore primarily **M1 vs M2 vs M5**, with the strongest near-term test assigned to M2 because it can be decided using existing CCRC refinement objects before introducing any new fields.

## Exact next gate — Iter004-G1

`QGR-ITER004-G1-REFINEMENT-STATIONARITY-AUDIT`

Determine whether exact CCRC refinement plus the existing path/coarse-kernel rules imply that every uniform nonzero TT-like refinement-fixed configuration is dynamically stationary.

Pass condition:

- stationarity follows from the same composition/amplitude rule already used in QGR-L0;
- then an onsite quadratic mass curvature is structurally forbidden.

Fail/block condition:

- refinement is only kinematic and does not constrain the onsite potential;
- then M2 cannot be used as mass protection and attention shifts to M1/M5.
