# Iter056H — finite-order Sobolev budget result

Date: 2026-09-14
Preregistration commit: `efd833bdd346a2a0f3aaa00aa69843a54b721a2f`

## Classification

`PASS_SCOPED_ITER056H_FINITE_ORDER_TRUNCATION_HAS_EXPLICIT_HS_PLUS_2N_REGULARITY_BUDGET`

## Frozen assumptions used

1. Formal hierarchy from Iter056B:
   `L0 g_n = S_n[g_0,...,g_{n-1}]`.
2. Conditional lower-order strongly-hyperbolic estimate from Iter056D.
3. Einstein-shell reduced Weyl3 source differential-order bound from Iter056G: the source contains at most third derivatives of already-known lower-order metric coefficients.
4. Standard local energy bookkeeping: obtaining `g_n in H^r` requires `S_n in H^{r-1}`.

## Inductive derivative budget

Let the desired final truncation accuracy be through order N, and require the top coefficient `g_N` at target regularity `H^s`, where s is above the fixed algebra/product threshold.

Because each source can contain up to three derivatives of lower-order known coefficients, to place `S_n` in `H^{r-1}` it is sufficient to have each required lower coefficient in

`H^{(r-1)+3} = H^{r+2}`.

Thus one recursion step costs at most two Sobolev derivatives in this conservative bookkeeping.

Define

`r_n = s + 2(N-n)`.

Then:
- `r_N = s`;
- if `g_j` for `j<n` are available at the regularities required by the induction, the source for the n-th equation is controlled at `H^{r_n-1}` provided the lower coefficients are available at `H^{r_n+2}`;
- but `r_{n-1} = r_n+2`, so the recursive budget closes exactly.

Therefore it is sufficient to supply the background/lower data at

`g_0 in H^{s+2N}`

and propagate the hierarchy so that

`g_n in H^{s+2(N-n)}`

or better for `0<=n<=N`.

Examples:
- N=1: background `H^{s+2}` suffices for `g_1 in H^s`;
- N=2: background `H^{s+4}`, intermediate `g_1 in H^{s+2}`, final `g_2 in H^s`;
- N=3: background `H^{s+6}`, then `H^{s+4}`, `H^{s+2}`, `H^s`.

The growth is linear in finite truncation order N and is finite for every fixed N.

## Scientific meaning

Iter056E remains correct that there is no naive closure in one fixed Sobolev space uniformly across all perturbative orders. Iter056H shows that this does **not** obstruct any fixed finite truncation: after the Iter056G covariant reduction, a simple explicit linear regularity budget suffices under the conditional hyperbolic assumptions.

This distinguishes two statements that must not be conflated:
- all-order fixed-H^s closure: not established and naively fails;
- any fixed finite-N formal truncation with increasing input regularity: conditionally well-defined under the stated assumptions.

## Claim ceiling

This result does not establish:
- convergence as N→infinity;
- uniform-in-N tame estimates;
- Nash-Moser closure;
- exact higher-derivative dynamics;
- a physical QGR order-reduction selector;
- global existence;
- quantum consistency/unitarity;
- UV completion;
- fixed/running c6 or beta=1.

`theory established = 0%` remains unchanged.
