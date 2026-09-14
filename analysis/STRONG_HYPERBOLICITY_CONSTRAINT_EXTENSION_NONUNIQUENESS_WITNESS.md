# Exact witness — constraint-extension choices can change hyperbolicity without changing physical constrained dynamics

Date: 2026-09-14

Status: outcome-independent mathematical control / interpretation aid. Not a QGR strong-hyperbolicity verdict.

## Purpose

Explain why a physical equation or characteristic root set is insufficient to define a strong-hyperbolicity question unless the gauge/constraint propagation system is also fixed.

## Frozen toy family

Let the state be

`U=(u,c)^T`

with physical constraint

`c=0`.

Consider the one-dimensional first-order systems

`partial_t U = A(a,b) partial_x U`

with

`A(a,b) = [[1,b],[0,a]]`.

The physical constrained dynamics are the same for every `a,b`:

- if `c=0` initially and the constraint equation preserves `c=0`, then `partial_t c = a partial_x c` keeps `c=0`;
- on that constraint surface, the first equation reduces exactly to `partial_t u = partial_x u`, because the `b partial_x c` term vanishes.

Thus all members of the family have the same physical constrained evolution for `u`.

## Two exact extensions

### Extension D — diagonalizable

Choose `a=2`, `b=1`:

`A_D = [[1,1],[0,2]]`.

Its characteristic polynomial is

`(mu-1)(mu-2)`

with two real distinct eigenvalues and a complete eigenbasis. It is diagonalizable.

### Extension J — defective

Choose `a=1`, `b=1`:

`A_J = [[1,1],[0,1]]`.

Its characteristic polynomial is

`(mu-1)^2`.

It has only one independent eigenvector and is a Jordan block, hence is not diagonalizable.

Nevertheless, on the exact physical constraint surface `c=0`, both extensions reduce to the same equation

`partial_t u = partial_x u`.

## Consequence

Strong hyperbolicity is a property of the full evolution formulation, including how constraints/gauge variables propagate off the physical constraint surface. It is not determined solely by the reduced physical equation evaluated after imposing constraints.

Therefore a QGR strong-hyperbolicity claim requires an explicit constraint propagation subsystem or an equivalent formulation-independent theorem. An unspecified choice of constraint additions could change the eigensystem while leaving constrained physical solutions unchanged.

This exact witness is complementary to Iter054F's same-characteristic-polynomial diagonalizable-vs-Jordan control:

- Iter054F A1 shows root/characteristic-polynomial data alone do not determine eigenvector completeness;
- the present witness shows even the same constrained physical dynamics do not determine the off-constraint principal evolution formulation.

## QGR interpretation ceiling

This does not show QGR is non-hyperbolic. It shows why a QGR-specific strong-hyperbolicity gate cannot be well posed until gauge and constraint propagation are fixed prospectively.

No physical spectrum, ghost, energy, unitarity, `c6`, `beta=1`, quantum-measure, UV-completion, GR-recovery or experimental conclusion follows.
