# Iter057C preregistration — reduced null-cone pencil maximal-minor GCD certificate

Date: 2026-09-15
Gate: `ITER057C-NULL-CONE-REDUCED-TWO-BLOCK-PENCIL-MAXIMAL-MINOR-GCD-CERTIFICATE`

## Motivation

Iter057B established exact generic rank five for the two-block pencil

`M(lambda)=M2_Einstein + lambda M4_Weyl3`

in all 24 frozen null-cone cases, but its stronger preregistered requirement of finding one monomial 5x5 minor in each full 10x10 matrix was not met. Candidate-minor zeros were not sufficient to infer full rank drops.

The mathematically correct invariant test is the common zero set of **all maximal minors after quotienting the fixed common kernel**. Since the parameter is univariate, this common zero set is encoded exactly by the polynomial gcd of all nonzero maximal minors.

## Frozen objects and panel

Reuse exactly the Iter057A/B panel and definitions:

- exact rational Weyl backgrounds `background_operator(seed)`, `seed=0,...,11`;
- null covectors `k0=(1,1,0,0)` and `k1=(5,3,4,0)`;
- exact Einstein principal symbol `M2` from the same Riemann convention;
- exact Weyl3 Hessian symbol `M4=Q(W,k)`;
- exact pure-gauge columns `K(k)`;
- one formal indeterminate `lambda`.

No new background, covector, basis, normalization, sign choice or numerical value of `c6` is allowed.

## Frozen controls

A. Reproduce the Iter057A/B exact object controls in all 24 cases:

- `k^2=0`;
- `rank K=4`;
- `rank M2=4`, `rank M4=4`;
- `M2 K=0`, `M4 K=0`;
- `dim(ker M2 ∩ ker M4)=5`;
- `rank M2+M4=5` at `lambda=1` as a generic-rank control.

Any failure is INVALID, not scientific evidence.

## Frozen quotient construction

B. Compute the exact five-dimensional common kernel

`N = ker([M2; M4])`.

Construct a deterministic 10x5 domain-complement matrix `B` by scanning the standard coordinate basis vectors `e0,...,e9` in lexicographic order and appending a vector iff it increases the rank of the current matrix starting from the five common-kernel basis columns. Stop only when `[N B]` has rank 10.

This rule is fixed before outputs and is independent of `lambda`.

Because `M2 N=M4 N=0`, the full-pencil rank equals the rank of the reduced 10x5 pencil

`U(lambda) = (M2 + lambda M4) B`.

## Frozen maximal-minor polynomial construction

C. Enumerate **all 252** five-row subsets of the 10 rows of `U(lambda)` in lexicographic order. For each subset form the corresponding 5x5 determinant polynomial.

Each entry of `U(lambda)` is affine in `lambda`, so every determinant has degree at most five. To avoid unnecessary symbolic-expression swell while remaining exact, freeze the polynomial reconstruction rule:

- evaluate the determinant exactly at `lambda = 0,1,2,3,4,5`;
- reconstruct the unique degree-<=5 polynomial by exact rational interpolation;
- verify the reconstructed polynomial at the independent exact point `lambda=6`;
- an interpolation-verification failure is INVALID.

Zero determinant polynomials are retained as zeros but excluded from the gcd update.

## Frozen gcd certificate

D. Compute the monic polynomial gcd over `Q[lambda]` of **all nonzero** maximal-minor polynomials.

Because a 10x5 matrix has rank below five exactly when all of its 5x5 minors vanish, the nonzero roots of this gcd are exactly the nonzero multiplier values at which the reduced/full pencil rank drops below five.

E. Maximum PASS requires, in every one of the 24 cases,

`gcd(maximal minors) = lambda^m`

up to a nonzero rational unit, for some integer `m>=1`.

The factor `lambda^m` is expected because `rank M(0)=4`. A pure power of `lambda` proves that there is **no nonzero common root**, hence

`rank M(lambda)=5 for every lambda != 0`

on that frozen case.

F. If the gcd has any additional irreducible factor, record the exact factor and classify the all-nonzero hypothesis as scientifically false/partial. Do not remove roots or switch minors after seeing the result.

G. Independently verify `rank M(0)=4` and, for any rational nonzero root produced by an additional linear gcd factor, verify the full 10x10 exact rank directly. Algebraic irrational roots need not be numerically approximated for the classification; the exact gcd factor itself is sufficient evidence of a possible common zero over the algebraic closure.

## Frozen classifications

Maximum PASS if A-E and interpolation verification all hold in all 24 cases:

`PASS_SCOPED_ITER057C_TWO_BLOCK_NULL_CONE_PENCIL_RANK5_FOR_ALL_NONZERO_SYMBOLIC_MULTIPLIERS_ON_FROZEN_PANEL`.

Scientific FAIL if controls are valid and at least one case has a gcd with a nonzero-root factor:

`SCIENTIFIC_FAIL_ITER057C_TWO_BLOCK_PENCIL_HAS_NONZERO_SYMBOLIC_RANK_DROP_ON_FROZEN_PANEL`.

INVALID if controls, quotient construction, interpolation or provenance fail:

`INVALID_ITER057C_REDUCED_PENCIL_OR_GCD_CERTIFICATE`.

## Interpretation ceiling

This gate still audits only `M2_Einstein + lambda M4_Weyl3`. It does not include lower-degree Weyl3 terms from the full linearization of the covariant Iter056X Euler tensor on curved backgrounds. Therefore even maximum PASS is not a full characteristic or hyperbolicity theorem and does not authorize birefringence/cone-shift, ghost, stability, energy, treatment, unitarity, UV-completion, or experimental claims.

`c6` remains symbolic/unfixed; `beta=1` remains unauthorized; theory established remains 0%.