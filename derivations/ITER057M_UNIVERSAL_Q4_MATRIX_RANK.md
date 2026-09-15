# Iter057M universal quartic matrix exact rank and canonical compatibility checkpoint

Date: 2026-09-15
Gate: `ITER057M-GENERAL-QAB-SECOND-EVEN-JET-QUARTIC-EXTENSION`
Prospective preregistration: `9760ca0324dce13cf141a9f93b6ff69ea4c75605`
Common basis authority: `19e76eb481d1cfd6c77b168ebe6320822510624b`
Original rank checkpoint: `5a00b06241c3bc034c02bb8d8abe9a1bd63c599a`

## Scope

This checkpoint evaluates the source-independent exact linear map from the unrestricted quartic trace-reversed jet `Q4_ab,cdef` to the frozen Iter057M cubic de Donder rows and quadratic reduced-field rows, then fixes a canonical Bianchi basis for its complete left nullspace.

It does **not** terminalize Iter057M: the authorized G3/H0 Weyl3 source second jet, one exact particular Q4, and independent unreduced substitution are still required by the preregistration.

No numerical rank, tolerance, fitted coefficient, restricted Q4 ansatz, or value/sign of `c6` is used.

## Frozen bases

Use the canonical bases frozen in `19e76eb...`:

- symmetric tensor pair `(ab)`: 10 entries;
- completely symmetric rank-four derivative multi-index `|alpha|=4`: 35 entries;
- unrestricted quartic unknown vector: `10*35=350` exact entries;
- cubic monomial basis `|alpha|=3`: 20 entries;
- quadratic monomial basis `|alpha|=2`: 10 entries.

The raw row count is

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

All background-connection/curvature corrections multiplying Q4 enter at higher coordinate degree and therefore belong to the affine right-hand side through the fixed Q2/background/source data, not to M.

## Exact sparse linear algebra

The rational sparse matrix contains 720 nonzero entries. Exact row reduction gives

`shape(M)=(180,350)`,

`rank(M)=164`,

`nullity(M)=350-164=186`,

`dim left-null(M)=180-164=16`.

These are exact rational ranks, not floating estimates.

## Canonical 16-vector Bianchi basis

A generic computer-algebra nullspace routine is free to return arbitrary linear combinations of left-null vectors. In particular, one SymPy basis vector has a larger support and must **not** be interpreted as an additional compatibility relation.

The physically canonical basis is instead fixed directly from the coefficient form of

`partial^a F_ab + (1/2) Box G_b = 0`

for the Q4 principal map.

For each `b=0..3` and each degree-one coordinate index `j=0..3`, define a row vector `Y_(b,j)` by

`Y_(b,j) . rows`

`= sum_a eta^{aa} F_(a b)[e_a+e_j]`

`  + (1/2) sum_m eta^{mm} G_b[2e_m+e_j]`.

Each `Y_(b,j)` has exactly four field entries and four gauge entries. Direct exact multiplication gives

`Y_(b,j)^T M = 0`

for all 16 pairs `(b,j)`, and exact row reduction of the `16 x 180` matrix formed by these vectors gives

`rank(Y)=16`.

Since `dim left-null(M)=16`, these sixteen canonical Bianchi vectors form a complete basis of the entire left nullspace.

Thus there are no source-independent compatibility conditions beyond the Bianchi/de Donder relations.

One representative is

`(1/2) G_0[(0,0,0,3)]`
`+(1/2) G_0[(0,0,2,1)]`
`+(1/2) G_0[(0,2,0,1)]`
`-(1/2) G_0[(2,0,0,1)]`
`-F_00[(1,0,0,1)]`
`+F_01[(0,1,0,1)]`
`+F_02[(0,0,1,1)]`
`+F_03[(0,0,0,2)] = 0`.

The other fifteen are exactly the `(b,j)` companions of the formula above.

## Exact affine RHS / Noether identity

The next structural check was performed before inserting any Weyl3 component values.

Parameterize an arbitrary symmetric even source by ten independent constants `S_ab^(0)` and one hundred independent normalized quadratic coefficients `S_ab^(2)[alpha]`. Construct the fixed Iter057L Q2 from the universal exact right inverse and use the exact G3/H0 metric, inverse, connection and origin curvature jets to assemble:

- the Q2/background contribution to the cubic de Donder RHS;
- the Q2/background contribution to the quadratic reduced-field RHS;
- the affine system `M Q4 = r(S^(0),S^(2))`.

Independently expand the source divergence

`N_b := nabla^a S_ab`

through degree one in the same normalized Taylor basis.

For **all sixteen** canonical Bianchi vectors, exact symbolic simplification with all 110 source coefficients algebraically independent gives

`Y_(b,j)^T r = N_b[e_j]`

identically.

No source equations, diagonal G3 specialization, numerical values, or tolerances are used in this equality. It is an exact coefficient identity of the frozen G3 geometry + Iter057L Q2 construction.

Therefore the affine Iter057M quartic system is consistent **iff** the sixteen degree-one Noether coefficients of the supplied source vanish. Equivalently, for a correctly assembled authorized Weyl3 source satisfying the exact Iter056X Noether identity,

`rank([M|r])=rank(M)=164`.

This proves the structural compatibility map, but the preregistration still requires the actual authorized source second jet to be exposed/controlled and an explicit Q4 to be substituted back into the unreduced equation; those obligations are not waived by the abstract identity.

## Source-component audit status

A finite-degree exact polynomial implementation was developed to expose the G3/H0 Weyl3 source second jet more cheaply than the historical full-rational Iter057K evaluator. It reproduces sensitive scalar controls including cubic homogeneity `P.R=3 I3` and the trace Ward identity. However, a component-level sign discrepancy was detected in the double-divergence block `D^{ab}=nabla_mu nabla_nu P^{mu(ab)nu}` relative to the component table recorded later in the Iter057J derivation.

No accelerated source-second-jet values are consumed while that discrepancy is open.

A prospective minimal audit was frozen in `f087b579e0c13714178bfc43e9a8e2f7fa907312`, implemented in `64a4e08274f950d1ce5513de35a097f3b376da34`, and launched from workflow commit `5daa9511ec59a4ef28f49a13172bdf019999f0fd`. It evaluates only the four diagonal origin components directly through the already-authorized Iter057K exact lineage. This is a convention/source audit, not a new scientific gate.

## Status

Established exactly:

- unrestricted source-independent Q4 matrix realized;
- exact dimensions `180 x 350`, `nnz=720`;
- exact `rank(M)=164`, nullity `186`, left-nullity `16`;
- a canonical rank-16 Bianchi basis of the complete left nullspace;
- exact generic affine identity `Y_(b,j)^T r = [nabla^a S_ab]_(degree 1,j)` for all 16 compatibility equations.

Still required before Iter057M terminal classification:

1. settle the authorized Weyl3 component/source-second-jet convention audit;
2. expose the actual exact G3/H0 `S^(2)` and verify its Noether coefficients in the common representation;
3. construct one exact particular Q4 (186 homogeneous directions remain);
4. independently substitute into the unreduced covariant linearized Einstein expression through quadratic order.

No terminal PASS/FAIL is assigned here. `c6` remains symbolic/unfixed; `beta=1` remains unauthorized; finite local jets are not open-neighborhood/global solutions; theory established remains `0%`.