# Iter056B terminal result — generic formal order-reduction hierarchy

Date: 2026-09-14
Preregistration: `298292c78132930fdaf9753842f7d3fd50952369`

## Terminal classification

`PASS_SCOPED_ITER056B_FORMAL_HIERARCHY_USES_ONLY_LOWER_ORDER_LINEARIZED_OPERATOR_ON_EACH_NEW_COEFFICIENT__PHYSICAL_QGR_TREATMENT_NOT_AUTHORIZED`

## 1. Formal setup

Let

`E[g,lambda] = E0[g] + lambda E1[g]`

and assume

`g(lambda)=g0 + delta g`,

`delta g = sum_(n>=1) lambda^n g_n`,

with `E0[g0]=0`.

Expand both functionals in Frechet-Taylor series about `g0`.

## 2. First two nontrivial orders

At order `lambda^0`:

`E0[g0]=0`.

At order `lambda^1`:

`D E0[g0] g1 + E1[g0] = 0`.

Writing

`L0 := D E0[g0]`,

the first correction obeys

`L0 g1 = -E1[g0]`.

At order `lambda^2`:

`L0 g2`

`+ (1/2) D^2 E0[g0](g1,g1)`

`+ D E1[g0] g1 = 0`.

Thus

`L0 g2 = -[(1/2)D^2E0(g1,g1) + D E1 g1]`.

Even though `E1` may contain higher derivatives, its linearization acts only on the already-known lower-order coefficient `g1` at this order.

## 3. Arbitrary-order proof

The Taylor expansion is

`E0[g0+delta g] = sum_(m>=0) (1/m!) D^m E0[g0](delta g,...,delta g)`.

Because `delta g` starts at order `lambda^1`, the coefficient of `lambda^n` involving the **new** coefficient `g_n` can arise from the `m=1` term only:

`D E0[g0] g_n = L0 g_n`.

For any `m>=2`, a contribution at order `lambda^n` is indexed by positive integers

`j1+...+jm=n`, `jr>=1`.

Hence every `jr <= n-1`; no such term can contain `g_n`.

Now consider

`lambda E1[g0+delta g]`.

To contribute at total order `lambda^n`, the Taylor expansion of `E1` is needed only through order `lambda^(n-1)`. Every coefficient entering that expansion is therefore among

`g0,g1,...,g_(n-1)`.

In particular, `D E1[g0] g_n` first appears at total order `lambda^(n+1)`, not `lambda^n`.

Therefore, at every `n>=1`, the hierarchy has the exact form

`L0 g_n = S_n[g0,g1,...,g_(n-1)]`,

where `S_n` is completely determined once all lower perturbative orders have been solved.

## 4. Meaning of “order reduced” in this theorem

If `E0` is second order and `E1` contains fourth/sixth/higher derivatives, those higher derivatives can still appear inside `S_n` acting on previously determined lower-order fields. The theorem does **not** make the source derivative-free.

What it proves is stronger and more precise for branch selection: the differential operator acting on the new unknown `g_n` at every perturbative order is the same lower-order linearized operator `L0`.

Thus the singular higher-derivative homogeneous solution sector of the exact mixed-order equation is absent from the regular formal hierarchy unless it is inserted through a separate nonperturbative sector.

## 5. Gauge and constraint caveat

For generally covariant gravity `L0` has gauge degeneracy before gauge fixing/constraint treatment. Iter056B does not assert invertibility.

A QGR-specific perturbative candidate version would still need:

- gauge variables/gauge condition;
- constraint propagation/compatibility;
- boundary/initial data;
- a function space/norm;
- existence/uniqueness for the lower-order linearized solve;
- control of the higher-derivative source terms;
- convergence or remainder estimates if claims go beyond formal asymptotics.

The structural theorem survives this caveat: whatever admissible lower-order reduction is chosen, the new perturbative coefficient is not acted on by `D E1` at the same order.

## Scientific consequence

Iter056A showed on an exact scalar control that regular formal-series membership removes the singular fast branch. Iter056B generalizes the underlying mechanism to a broad functional equation: an explicitly perturbative higher-derivative correction produces a recursive hierarchy governed at each new order by the lower-order linearized operator.

This gives a mathematically coherent architecture for a **separately versioned perturbative/order-reduced candidate formulation** of QGR once the actual Weyl3 Euler-Lagrange source and gauge/constraint structure are supplied.

It remains distinct from historical QGR authority. Iter054G-R still controls the physical claim: current QGR has not selected this treatment.

## Next highest-information gate

Test the first perturbative Einstein+Weyl3 equation at the level of covariance/constraints without needing a component-expanded Weyl3 EOM. For a diffeomorphism-invariant correction action `S1[g]=integral sqrt(|g|) Weyl^3`, Noether covariance should imply an off-shell covariant divergence identity for its Euler-Lagrange tensor. Prospectively determine whether this makes the first-order source `-E1[g0]` compatible with the linearized Einstein Bianchi identity on a lower-order background. This would close one necessary constraint-consistency obligation of a future perturbative candidate version while still not selecting it physically.

## Claim ceiling

No historical QGR treatment is source-authorized. No full Weyl3 component EOM, gauge fixing, solvability, convergence/remainder theorem, strong hyperbolicity, physical mode/ghost statement, c6 running, finite cutoff, quantum unitarity, UV completion, regulator removal, full GR recovery, experiment or theory establishment follows. Theory established remains 0%.

No GitHub Actions run was required; the result is exact formal functional analysis.
