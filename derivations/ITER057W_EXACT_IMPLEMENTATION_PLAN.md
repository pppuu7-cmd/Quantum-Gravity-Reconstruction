# Iter057W exact implementation architecture

Gate: `ITER057W-DECIC-EINSTEIN-SEED-COMPLETION`
Preregistration authority: `7e6336d195985b2059966eda64859da86c9e9d15`.
Status: implementation architecture derived; scientific criteria unchanged.

## Canonical input

Replay the terminal Iter057T particular `R8` exactly and reconstruct the same canonical metric seed `g8 = eta + G2 + R4 + R6 + R8`. No lower coefficient may be changed. The new unknown is the complete normalized pure degree-ten trace-reversed symmetric jet `Rbar10_ab[alpha]`, with 10 symmetric pairs and all 286 degree-ten four-variable multi-indices: 2860 columns.

## Exact nonlinear residual lane

Extend the Iter057T polynomial evaluator from coordinate degree 6 to degree 8. Because the perturbation begins at degree 2, the inverse metric through degree 8 requires the Neumann series through `h^4`:

`g^{-1}=eta-eta h eta+eta h eta h eta-eta h eta h eta h eta+eta h eta h eta h eta h eta`.

Truncate inverse products through degree 8, Christoffels through degree 9 before differentiation, and Ricci/scalar/Einstein through degree 8. Before adding R10 require exact replay of Einstein degrees 0,2,4,6 and directly extract the full degree-8 residual `G8_ab`.

## Frozen principal affine system

Use the same normalized Taylor convention as Iter057T. Rows are ordered as:

1. de Donder degree 9: `(b, alpha9)`, 4*220 = 880 rows;
2. Einstein degree 8: `((a,b), alpha8)`, 10*165 = 1650 rows.

Columns are `((a,b), alpha10)`, 10*286 = 2860. The flat principal map is unchanged in form from Iter057T, shifted by two degrees. Exact structural targets remain preregistered: rank 2050, left-nullity 480, nullity 810.

The affine RHS is zero in gauge rows and minus the normalized coefficients of `G8_ab/kappa^5` in field rows. This scaling is bookkeeping only and does not fit or fix any physical parameter.

## Complete Bianchi compatibility family

Construct all 4*C(10,3)=480 canonical left-null vectors indexed by `(b,beta7)`, using the same derivative identity as Iter057T shifted from beta5 to beta7. Verify both that every vector annihilates M exactly and that their count equals the exact left-nullity. PASS requires every contraction with the actual affine RHS to be exactly zero.

## Exact solve and independent replay

Compute exact `rank(M)` and `rank([M|r])`; numerical rank/tolerances are forbidden. If consistent, set all free columns to zero only as a deterministic canonical choice, solve pivot columns exactly, and retain the full 810-dimensional homogeneous freedom as unfixed. Convert the resulting trace-reversed Rbar10 to metric R10, require it to be pure degree 10, then independently recompute the unreduced nonlinear Levi-Civita/Ricci/scalar/Einstein construction through degree 8. All ten Einstein components and de Donder residuals must vanish exactly.

## Computational optimization lock

The 2530x2860 matrix is sparse with at most four nonzeros per gauge row and four per field row. Build it directly as an exact sparse/domain matrix; do not densify before elimination. Structural rank and Bianchi annihilation may be computed independently of the affine residual. The nonlinear residual/replay and linear-system lanes are scientifically independent controls and may run in parallel, but no terminal classification is allowed until their frozen evidence is aggregated.

## Scope lock

A PASS would establish only the next finite zeroth-order local Taylor layer through Einstein coordinate degree 8. It would not establish an all-orders/convergent seed, an open-neighborhood/global solution, Weyl3 source degree 6, the next O(c6) response, strong hyperbolicity, ghost/stability, quantum unitarity, regulator removal, UV completion, experiment, new physics, or QGR correctness. `c6` remains symbolic/unfixed and theory established remains 0%.
