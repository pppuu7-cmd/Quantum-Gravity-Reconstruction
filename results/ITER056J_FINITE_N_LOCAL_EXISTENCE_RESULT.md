# Iter056J — conditional finite-N local existence result

Date: 2026-09-14
Preregistration commit: `988a39962ead180f00b42a600fd4b7b60a8c6d37`

## Classification

`PASS_SCOPED_CONDITIONAL_ITER056J_EVERY_FIXED_FINITE_ORDER_TRUNCATION_HAS_SEQUENTIAL_LOCAL_SOLUTION`

## Proof structure

Fix a finite truncation order N and a target Sobolev index s above the fixed algebra/product threshold.

### Step 0 — background
Assume the lower-order background `g_0` exists on a local time slab and belongs to the Iter056H budget class `H^{s+2N}`. This is an explicit hypothesis of the prospective candidate theorem; Iter056J does not derive the lower-order Einstein local-existence theory.

### Induction hypothesis
Suppose `g_1,...,g_{n-1}` have already been constructed on a common local time interval and possess at least the regularities assigned by Iter056H:

`g_j in H^{s+2(N-j)}`.

### Source construction
By Iter056B, the n-th coefficient equation is triangular:

`L0 g_n = S_n[g_0,...,g_{n-1}]`,

so the source is known before solving for `g_n`.

By Iter056G, the reduced source uses at most third derivatives of already-known metric coefficients in the Einstein-shell representation. The Iter056H budget therefore places `S_n` in the Sobolev source space required for the target regularity

`g_n in H^{s+2(N-n)}`.

### Constraint compatibility
By Iter056I, after the lower coefficient equations hold, the source automatically satisfies the background linearized Bianchi/constraint compatibility condition. Thus there is no independent coefficient-order source obstruction requiring post-hoc tuning.

### Hyperbolic solve
By the conditional Iter056D assumption, the gauge-fixed operator `L0` is strongly hyperbolic and is the same lower-order principal operator acting on each new coefficient. Standard local linear hyperbolic well-posedness therefore gives a unique local coefficient solution for compatible initial data in the assigned regularity class.

### Finite common interval
Repeat the argument for n=1,...,N. Because N is finite, the intersection of the finitely many coefficient existence intervals contains a sufficiently short nonzero common local interval. Hence all coefficients through order N coexist on that interval.

## Result

For every fixed finite N, under the explicitly frozen lower-order gauge/hyperbolicity and compatible-data assumptions, the prospective formal order-reduced hierarchy is locally solvable coefficient by coefficient with the conservative regularity budget

`g_n in H^{s+2(N-n)}`,

and in particular `g_N in H^s`.

## What this closes

Within the prospective order-reduced candidate mathematics, the combination of:
- triangular hierarchy (Iter056B),
- conditional inherited hyperbolicity (Iter056D),
- covariant derivative reduction (Iter056G),
- finite regularity budget (Iter056H), and
- recursive Bianchi compatibility (Iter056I)

is sufficient for conditional local solvability of every fixed finite truncation.

The remaining primary obstruction in this branch is therefore not an internal finite-N PDE inconsistency. It is the absence of a QGR-authoritative physical principle selecting this order-reduced formal sector as the dynamics rather than the exact higher-derivative theory or another treatment.

## Claim ceiling

This result does not establish:
- convergence as N→infinity;
- an exact solution of the full higher-derivative equations;
- global existence;
- a historical/physical QGR order-reduction selector;
- quantum unitarity or quantum consistency;
- UV completion;
- fixed/running c6;
- beta=1;
- theory establishment.

`theory established = 0%` remains unchanged.
