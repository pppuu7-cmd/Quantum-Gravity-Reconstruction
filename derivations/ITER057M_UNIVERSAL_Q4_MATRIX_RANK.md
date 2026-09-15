# Iter057M universal quartic matrix exact rank checkpoint

Date: 2026-09-15
Gate: `ITER057M-GENERAL-QAB-SECOND-EVEN-JET-QUARTIC-EXTENSION`
Prospective preregistration: `9760ca0324dce13cf141a9f93b6ff69ea4c75605`
Common basis authority: `19e76eb481d1cfd6c77b168ebe6320822510624b`

## Scope

This checkpoint evaluates the source-independent exact linear map from the unrestricted quartic trace-reversed jet `Q4_ab,cdef` to the frozen Iter057M cubic de Donder rows and quadratic reduced-field rows. It does **not** yet classify Iter057M because the exact G3/H0 source/operator right-hand side and independent unreduced substitution remain required by the preregistration.

No numerical rank, tolerance, fitted coefficient, symmetry ansatz, or value/sign of `c6` is used.

## Frozen bases

Use the canonical bases frozen in `19e76eb...`:

- symmetric tensor pair `(ab)`: 10 entries;
- completely symmetric rank-four derivative multi-index `|alpha|=4`: 35 entries;
- unrestricted quartic unknown vector: `10*35=350` exact entries;
- cubic monomial basis `|alpha|=3`: 20 entries;
- quadratic monomial basis `|alpha|=2`: 10 entries.

The raw row count is therefore

- cubic de Donder: `4*20=80` rows;
- quadratic field equation: `10*10=100` rows;
- combined matrix: `180 x 350`.

Normalized Taylor coefficients are used exactly as required by the common architecture.

## Universal Q4 coefficients

At the target orders, the Q4 contribution is source independent.

For the cubic de Donder coefficient,

`G_b[alpha] | Q4 = eta^{ac} Q4_ab,alpha+e_c`, `|alpha|=3`.

For the quadratic reduced-field coefficient,

`F_ab[alpha] | Q4 = -(1/2) eta^{mn} Q4_ab,alpha+e_m+e_n`, `|alpha|=2`.

All background-connection/curvature corrections multiplying Q4 enter at degree four or higher and therefore do not alter this Iter057M matrix. They instead contribute to the exact right-hand side through the already-fixed Q2/background/source data.

## Exact sparse linear algebra

The matrix was assembled over the rationals with the exact frozen basis and contains 720 nonzero entries.

Exact row reduction gives

`shape(M) = (180,350)`,

`rank(M) = 164`,

`nullity(M) = 350-164 = 186`,

and therefore

`dim left-null(M) = 180-164 = 16`.

These are exact rational ranks, not floating estimates.

## Structure of the 16 row dependencies

Every left-null relation mixes four cubic-gauge rows with four quadratic-field rows. There are exactly four such coefficient relations for each free tensor index `b=0,1,2,3`, giving `4*4=16` total.

They are the normalized-Taylor coefficient form of the source-independent linearized Bianchi identity relating divergence of the reduced field operator to the wave operator acting on the de Donder vector. Schematically,

`nabla^a DG_ab = 0`

reduces at the Q4 principal coefficient level to

`partial^a F_ab[Q4] - (compatible second-derivative combination of G_b[Q4]) = 0`.

As one explicit exact relation from the computed left-null basis,

`(1/2) G_0[(0,0,0,3)]`
`+(1/2) G_0[(0,0,2,1)]`
`+(1/2) G_0[(0,2,0,1)]`
`-(1/2) G_0[(2,0,0,1)]`
`-F_00[(1,0,0,1)]`
`+F_01[(0,1,0,1)]`
`+F_02[(0,0,1,1)]`
`+F_03[(0,0,0,2)] = 0`

identically for every Q4. The remaining 15 relations are its coordinate/index companions in the frozen basis.

## Consequence for the source RHS

There are no source-independent algebraic compatibility conditions beyond these 16 Bianchi-type relations. Thus for the affine system

`M vec(Q4)=r`,

consistency is equivalent to the exact G3/H0 right-hand side satisfying all 16 left-null contractions.

The Iter056X Noether identity strongly predicts these contractions will vanish when `r` is assembled from one common exact source/operator representation, but the Iter057M preregistration explicitly requires source/Noether coefficients to be verified rather than assumed. Therefore this checkpoint does **not** promote the prediction to PASS.

If the 16 exact RHS contractions vanish, then

`rank([M|r])=rank(M)=164`

and an exact particular Q4 exists with a 186-dimensional homogeneous freedom before any later gauge/boundary choices. If any contraction is exactly nonzero, it is an immediate exact inconsistency witness for the frozen quartic extension system.

## Source-jet audit status

A finite-degree exact polynomial implementation was started to expose the G3/H0 Weyl3 source second jet more cheaply than the historical Iter057K full-rational evaluator. Its scalar controls reproduced the exact Weyl-cubic magnitude and the cubic homogeneity contraction `P.R=3 I3`. However, a component-level discrepancy was detected in the sign of the double-divergence block `D^{ab}=nabla_mu nabla_nu P^{mu(ab)nu}` relative to the later Iter057J component record.

Because scalar trace/homogeneity controls alone do not resolve that component discrepancy, no source-second-jet numbers from that accelerated implementation are consumed here. The discrepancy must be resolved against the authorized Iter056X/Iter057K lineage before the Iter057M RHS is frozen.

This is a control success: potentially inconsistent source data were rejected before matrix augmentation or scientific classification.

## Status

Established exactly in this checkpoint:

- canonical source-independent Q4 matrix realized;
- exact dimensions `180 x 350`;
- exact `rank(M)=164`;
- exact quartic nullity `186`;
- exact left-null dimension `16`;
- all source-independent compatibility conditions identified as Bianchi/de Donder relations.

Still required before Iter057M classification:

1. exact authorized G3/H0 source second jet and degree-two operator RHS;
2. exact evaluation of the 16 compatibility contractions / source Noether coefficients;
3. if consistent, one exact particular Q4;
4. independent unreduced covariant substitution through quadratic order.

No Actions production run is authorized from this checkpoint alone. `c6` remains symbolic/unfixed; `beta=1` remains unauthorized; finite local jets are not open-neighborhood/global solutions; theory established remains `0%`.