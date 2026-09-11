# QGR Iter004-G5 — minimal unreduced second-moment arena

Date: 2026-09-11
Status: `PASS_SCOPED_NATURAL_10D_ARENA / FAIL_SCOPED_EXACT_L0_EMBEDDING`

## Motivation

Iter004-G4 showed that the current six Boolean pair variables cannot support a nonzero local `S4`-invariant quadratic two-derivative Hessian with the natural derivative rank-1 gauge law, while a diagnostic ten-component symmetric arena can.

The repair is **not** allowed to add four fields merely because ten components are convenient. G5 therefore asks whether a ten-component object already follows from the existing rank-1 relational data.

## Natural object already latent in QGR

The four rank-1 relational directions form the four-dimensional permutation representation `W4` of `S4`.

The symmetric second moment

`Sym^2(W4)`

is therefore an independently defined object built from the existing rank-1 frame, with dimension

`4*5/2 = 10`.

It decomposes canonically into

- four diagonal/self-response components `(ii)`;
- six off-diagonal pair responses `(ij), i<j`.

The latter are exactly the index set already used by the Boolean rank-2 pair sector. The four diagonal entries need not be interpreted as repeated Boolean events `{i,i}`; they can instead be interpreted as self-correlation / second-response components of the same four rank-1 directions.

Thus the event ontology can remain Boolean while the **field/response arena** becomes unreduced.

## Exact S4 representation structure

The character of `Sym^2(W4)` is

`[10,4,2,1,0]`.

Its exact irrep decomposition is

`Sym^2(W4) = 2*1 + 2*3 + 2`.

The canonical diagonal/off-diagonal split is

`diag4 = 1+3`,

`offdiag6 = 1+3+2`.

Therefore adding the four self-response components adds exactly one additional lower-rank `1+3` sector while preserving the old six-component pair sector as a canonical subspace.

This is a structural reason for ten components that does **not** use GR degree-of-freedom counting.

## Derivative-gauge diagnostic

On this ten-component second-moment arena, the complete space of local `S4`-invariant quadratic Hessians homogeneous of degree two in first-neighbor momentum has 38 orbit coefficients.

For the derivative frame-change law

`delta h_ij = k_i xi_j + k_j xi_i`,

including

`delta h_ii = 2 k_i xi_i`,

the exact Noether constraints have rank 36.

Hence there is a two-dimensional nonzero gauge-compatible Hessian space.

Classification:

`PASS_SCOPED_EXISTENCE_OF_LOCAL_DERIVATIVE_GAUGE_CLOSURE_IN_NATURAL_SECOND_MOMENT_ARENA`.

This is still only an existence result. No preferred member of the two-dimensional Hessian family is selected here.

## Can QGR-L0 be embedded unchanged?

The old physical 2D quotient basis is retained in the old off-diagonal six-dimensional subspace. Its unique `S4`-invariant inner product is represented by `B^T B`, and QGR-L0 uses the directional kinetic polynomial

`K_L0(k)=k^T(J-I)k = 2 sum_{i<j} k_i k_j`.

G5 imposes simultaneously:

1. the exact ten-component derivative Noether identity;
2. exact restriction to the old 2D quotient;
3. exact equality of the restricted kinetic operator to `lambda K_L0(k)` times the invariant 2D metric, for one overall normalization `lambda`.

This augmented exact linear system has 39 unknowns (38 orbit coefficients plus `lambda`) and rank **39**.

Therefore the only exact solution is the zero Hessian with `lambda=0`.

So no nonzero derivative-gauge-compatible ten-component Hessian contains the old QGR-L0 kinetic operator as an unchanged physical sub-block/projection.

Classification:

`FAIL_SCOPED_EXACT_QGR_L0_KINETIC_EMBEDDING_IN_DERIVATIVE_GAUGE_10D_ARENA`.

## Scientific consequence

The G4 obstruction cannot be repaired cosmetically.

The current status is:

- **QGR-L0 remains a valid scoped Lorentzian/hyperbolic seed** derived from the six Boolean pair sector;
- **QGR-L0 is not gauge-complete**;
- the natural unreduced response object is `Sym^2(W4)` with ten components;
- derivative gauge closure exists on that arena;
- but obtaining it requires a **new pre-reduction kinetic construction**, provisionally called `QGR-L1`, rather than adding four passive fields to L0.

## Anti-overfitting guard

QGR-L1 is not promoted yet. In particular we may not select one of the two surviving ten-component Hessians because it resembles the Fierz-Pauli action or gives desired GR phenomenology.

A valid selection principle must be derived prospectively from QGR ingredients already motivated independently: incidence/composition, refinement consistency, finite definition, causal normalization, and the pair-incidence Lorentzian form.

## Exact next gate — Iter004-G6

`QGR-ITER004-G6-SELECT_OR_REJECT_L1_KINETIC_FROM_RELATIONAL_PRINCIPLES`

1. characterize the two exact gauge-compatible ten-component Hessian directions invariantly;
2. determine whether incidence/refinement/composition distinguishes one combination without reference to continuum GR;
3. test whether the selected combination has the same causal cone as the independently derived pair-incidence form `C=J-I`;
4. test whether an onsite mass deformation is forbidden by the derived derivative symmetry;
5. if the two-dimensional freedom cannot be reduced by a pre-existing QGR principle, record `BLOCKED_UNDERDETERMINED_L1` rather than choosing the GR-like member by hand.

Candidate-program readiness remains **30%** until this selection problem is resolved.

## Reproducibility

`code/qgr_iter004_g5_second_moment_arena.py`
