# QGR Iter004-G3 — Exact Tensor-Representation Audit

Date: 2026-09-11
Status: `PASS_SCOPED_TENSOR_REPRESENTATION_STRUCTURE / CONTINUOUS_SPIN2_NOT_ESTABLISHED`

## Question

Is the six-dimensional Boolean pair space merely an ad hoc collection of pair variables, or does it carry the exact finite-group structure expected of a symmetric rank-2 tensor built from three spatial directions?

## Exact character calculation

Let `V_3` be the standard three-dimensional irreducible representation of `S_4`, obtained from the four-vertex permutation representation after removing the trivial one-dimensional component.

For conjugacy classes

`e, (12), (12)(34), (123), (1234)`, 

the character is

`chi_V3 = [3,1,-1,0,-1]`.

The symmetric square has character

`chi_Sym2(V3)(g) = [chi_V3(g)^2 + chi_V3(g^2)]/2`, 

which evaluates exactly to

`[6,2,2,0,0]`.

The six-dimensional permutation representation on unordered pairs of four Boolean generators has the same character, because the entries count fixed 2-subsets under the same five conjugacy classes:

`chi_pair6 = [6,2,2,0,0]`.

Therefore

`pair6 ~= Sym^2(V_3)`

as an exact `S_4` representation.

## Irreducible decomposition

Using the exact `S_4` character table,

`Sym^2(V_3) = 1 + 3 + 2`.

The four-dimensional rank-1 redefinition image `im(M^T)` is equivariantly isomorphic to the four-vertex permutation representation

`4 = 1 + 3`.

Hence the quotient is exactly

`pair6 / im(M^T) = 2`.

## Structural interpretation

The six Boolean pair variables are therefore not an arbitrary six-component field: at finite `S_4` level they have exactly the representation content of a symmetric rank-2 tensor built from a three-dimensional standard representation.

The quotient count

`6 - (1+3) = 2`

has a precise representation-theoretic origin.

This substantially strengthens the interpretation of the two physical pair modes. However, the result must not be overread.

## Critical guard

A two-dimensional `S_4` irrep is **not** by itself a continuous Lorentz/Poincare helicity-2 representation.

If continuous rotational/Lorentz symmetry emerges, the full `1+3+2` finite-group content and the constraint/redefinition sector must be embedded consistently into that larger symmetry. A fixed two-dimensional subspace cannot simply be declared a globally covariant spin-2 field.

Thus the result supports the tensor/constraint architecture but simultaneously sharpens the next requirement: continuous symmetry and constraint closure must be derived together.

## Classification

`PASS_SCOPED_BOOLEAN_PAIR_SPACE_IS_EXACTLY_SYM2_OF_STANDARD_S4_THREE_REP_AND_RANK1_REDEFINITION_IMAGE_IS_1_PLUS_3_LEAVING_EXACT_2D_QUOTIENT__NO_CONTINUOUS_SPIN2_OR_GRAVITON_CLAIM`

## Next implication

The mass/gauge problem should be posed on the **full six-component tensor-like pair space plus four lower-rank constraint/redefinition directions**, not only on the already reduced two-component quotient. This is the correct arena for testing a future continuous constraint algebra.

Reproducibility: `code/qgr_iter004_g3_tensor_rep_audit.py`.
