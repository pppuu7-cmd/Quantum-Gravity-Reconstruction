# QGR Iteration 003 — 4D Lorentzian/GR Seed Gate

Date: 2026-09-11
Status: `COMPLETE / PROPOSED_LINEARIZED_ANSATZ / MASS_GAUGE_BLOCKED`
Current task completion: **100%**
Candidate-program readiness: **30%**
Readiness semantics: internal construction-roadmap progress only; not probability of correctness and not fraction of quantum gravity solved.
Physical ansatz promoted: **YES — LINEARIZED L0 ONLY**
Lead architecture: **A / CCRC**

## Objective and outcome

Iter003 tested whether the A/CCRC architecture could progress from a branching metric-free causal combinatorics to a rigid Lorentzian tensor-like linearized candidate without inserting a background metric or Einstein-Hilbert action.

Outcome:

- a derived four-direction Boolean causal seed exists;
- the exact rank-2 perturbation space contains a structurally selected two-dimensional physical quotient;
- microscopic rank-2 pair incidence carries a `(1,3)` Lorentzian signature for `d=4`;
- a minimal equal-pair quadratic action gives an explicit hyperbolic two-component linearized ansatz with no relative kinetic tuning;
- current microscopic redundancy does **not** protect masslessness;
- nonlinear GR, gauge/diffeomorphism closure, continuum recovery and observables remain open.

This is enough to close the seed-construction iteration, but not to call the object a graviton theory or a quantum-gravity model.

## G1 — Boolean causal cell

Events of `B_d` are subsets of `d` independent relational generators, ordered by inclusion.

`N_r=C(d,r)`, with rank polynomial `(1+x)^d`.

For `B_4`:

- `16` events;
- rank profile `(1,4,6,4,1)`;
- `24` maximal causal chains;
- derived combinatorial direction count `d=4`.

With the previously tested CCRC projector `P^2=P`, equal-chain symmetry plus exact coarse/refinement consistency fixes

`w_d=1/d!`, hence `w_4=1/24`.

Classification:

`PASS_SCOPED_DERIVED_COMBINATORIAL_DIMENSION_AND_UNIQUE_PATH_NORMALIZATION`.

Reproducibility: `code/qgr_iter003_boolean_causal_cell.py`.

## G2 — exact pair-sector decomposition

The six unordered direction pairs form the `S_4` pair representation

`6=1+3+2`.

Let `M` be the unsigned `4 x 6` vertex-edge incidence matrix of `K_4`. The balanced sector

`M x=0`

has dimension `2` and an exact basis

`TT1=(0,1,-1,-1,1,0)`,

`TT2=(1,0,-1,-1,0,1)`

in pair order `(01,02,03,12,13,23)`.

Embedded as symmetric zero-diagonal pair tensors, this sector is transverse to the fully symmetric direction and traceless relative to the Lorentzian seed.

The exact `S_4` commutant on this 2D sector is one-dimensional, so every equivariant internal transfer acts as `lambda I`.

Detailed result: `results/ITER003_G2_TETRAHEDRAL_LORENTZ_SECTOR.md`.
Reproducibility: `code/qgr_iter003_tetrahedral_lorentz_sector.py`.

## G3 — hyperbolic principal tensor

For four equivalent directions, the most general symmetric `S_4`-invariant principal tensor is

`G=A I+B J`.

Requiring its inverse propagation geometry to make the elementary causal directions null gives

`A+3B=0`, hence `B/A=-1/3`.

After removing overall normalization,

`G=I-J/3`,

with eigenvalues

`(-1/3,+1,+1,+1)`.

Thus the relative linearized kinetic structure is Lorentzian and fixed, not fitted coefficient by coefficient.

Detailed result: `results/ITER003_G3_HYPERBOLIC_KINETIC_SEED.md`.
Reproducibility: `code/qgr_iter003_g3_hyperbolic_operator.py`.

## G4 — microscopic incidence origin

The rank-2 events of `B_d` are exactly unordered pairs of **distinct** generators. Therefore the canonical equal-weight rank-2 incidence matrix is, up to scale/sign,

`C_d=J-I`.

Its spectrum is

`(d-1,-1,...,-1)`.

For `d=4`:

`spec(C_4)=(3,-1,-1,-1)`.

Hence the microscopic pair-incidence form itself already carries one sign opposite to the remaining three. Its inverse is

`C_4^{-1}=-I+J/3`,

matching the G3 tensor up to overall sign.

A separate exact intertwiner audit shows that the most general first-order direction-resolved `S_4`-equivariant update of the 2D sector has only one degree of freedom:

`T_0=T_1=T_2=T_3=lambda I`.

Therefore first directional order cannot produce nontrivial spatial Lorentzian TT propagation; second directional order is the minimal nontrivial level under the current symmetry structure.

Detailed result: `results/ITER003_G4_MICRO_INCIDENCE_BRIDGE.md`.
Reproducibility: `code/qgr_iter003_g4_micro_incidence.py`.

## G5 — proposed linearized QGR-L0 action

The existing six rank-2 Boolean events provide the minimal equal-weight quadratic cell functional

`S_cell^(2)=kappa sum_{i<j} D_i q · D_j q`

or equivalently

`S_cell^(2)=(kappa/2) Dq^T (J-I) Dq`.

This action uses only distinct rank-2 pair events. There is no diagonal self-pair coefficient to tune, because `{i,i}` is not a rank-2 Boolean event. `S_4` gives one common pair weight.

The principal polynomial is

`K(p)=(sum_i p_i)^2-sum_i p_i^2`

and, in the symmetric/spatial decomposition,

`K(p)=3 p_0^2-|p_perp|^2`.

The four elementary generator directions are exact null/characteristic directions.

The two TT-like components have identical kinetic structure because the internal commutant is one-dimensional.

Parameter audit at this level:

- relative directional kinetic coefficients: `0`;
- polarization splitting coefficients: `0`;
- overall normalization/coupling: `1` (`kappa`);
- protected mass parameter: not yet available;
- nonlinear interaction functions: not defined.

This is promoted as the first explicit linearized ansatz:

`QGR-L0 = two-component balanced relational quotient field with pair-incidence kinetic action`.

Detailed result: `results/ITER003_G5_PAIR_ACTION.md`.
Reproducibility: `code/qgr_iter003_g5_pair_action.py`.

## G6 — quotient origin and mass blocker

Rank-1 generator redefinitions act on pair data as

`x -> x+M^T u`, i.e. `x_ij -> x_ij+u_i+u_j`.

Because `rank(M)=4`, the physical pair quotient has dimension

`6-4=2`.

The exact projector is

`P_phys=I-M^T(MM^T)^(-1)M`,

with `P_phys^2=P_phys`, `M P_phys=0`, `rank(P_phys)=2`.

Thus the earlier 2D TT-like sector is not selected merely because it has dimension two: it is exactly the part of rank-2 data that cannot be changed by rank-1 redefinitions.

However `q=P_phys x` is itself gauge/redefinition invariant, so the onsite operator

`m^2 q·q`

is also invariant. The currently derived microscopic redundancy therefore does **not** forbid mass.

The G5 difference action has a global shift symmetry `q(n)->q(n)+c`, but Iter003 does not derive that shift as a fundamental microscopic gauge redundancy. Masslessness is therefore provisional and unprotected.

Classification:

`PASS_SCOPED_LOWER_RANK_REDEFINITION_QUOTIENT_EXACTLY_PRODUCES_TWO_DIMENSIONAL_TT_LIKE_PHYSICAL_PAIR_SECTOR__CURRENT_MICROSCOPIC_REDUNDANCY_DOES_NOT_FORBID_ONSITE_MASS_TERM__MASSLESSNESS_NOT_YET_PROTECTED`.

Detailed result: `results/ITER003_G6_GAUGE_MASS_AUDIT.md`.
Reproducibility: `code/qgr_iter003_g6_gauge_mass_audit.py`.

## What Iter003 established

Within the stated finite/linearized scope, QGR now has one coherent same-realization chain:

`Boolean causal order -> derived d=4 -> rank-2 pair incidence -> 2D physical quotient -> Lorentzian pair form -> hyperbolic pair-action`.

This is materially stronger than an isolated numerology match because each arrow has an explicit finite algebraic object and the same `B_4` realization is retained.

## What Iter003 did not establish

No claim is made for:

- protected masslessness;
- local Lorentz group in a continuum limit;
- diffeomorphism/first-class gauge algebra;
- Lorentz/Poincare spin-2 representation theorem;
- nonlinear self-coupling;
- Einstein equations;
- universal matter coupling/equivalence principle;
- continuum/refinement theorem;
- normalized operational observables;
- experimental validation;
- independent KMQGB PASS.

## Readiness decision

Candidate-program readiness moves from **24% to 30%** because QGR has crossed the pre-ansatz boundary and now possesses an explicit, low-freedom, reproducible linearized candidate action.

This percentage is only an internal roadmap metric. It is not probability that QGR is correct.

## Exact next stage — Iter004

`QGR-ITER004-MASSLESS-GAUGE-CLOSURE`

The next stage must search for a mechanism that protects masslessness and supplies a genuine constraint/gauge structure **for reasons independent of the desire to reproduce GR**.

At least four candidate mechanisms must be compared prospectively before one is adopted. Any mechanism that merely tunes `m=0`, declares a gauge symmetry after seeing the spectrum, or introduces arbitrary compensator functions fails the anti-overfitting constitution.
