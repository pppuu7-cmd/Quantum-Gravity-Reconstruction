# Iter056E terminal result — derivative loss in the naive fixed-Sobolev formal hierarchy

Date: 2026-09-14
Preregistration: `02c632207ccfcd5d39e967c525e7ae65ed1713b2`

## Terminal classification

`PASS_SCOPED_ITER056E_NAIVE_FIXED_SOBOLEV_ALL_ORDER_RECURSION_HAS_DERIVATIVE_LOSS__NO_CONVERGENCE_OR_PHYSICAL_FAILURE_CLAIM`

## 1. Regularity bookkeeping

Iter056B gives

`L0 g_n = S_n[g0,...,g_(n-1)]`,

where the new coefficient is acted on only by the lower-order operator `L0`.

Assume, as frozen in the preregistration, a standard strongly-hyperbolic estimate at Sobolev order `s` in which an inhomogeneous source must lie schematically in `H^(s-1)` to control the solution in `H^s`.

If a term in `S_n` contains `q` derivatives of a previously determined coefficient, schematically `D^q g_(n-1)`, then placing that source in `H^(s-1)` requires

`g_(n-1) in H^(s+q-1)`

up to the usual product/Moser assumptions and lower-order coefficient regularity.

Therefore a hypothesis that every coefficient merely lies in one fixed `H^s` is not closed for any genuinely higher-derivative source with `q>1`, absent an additional structural cancellation or a different functional framework.

This does not change the Iter056D principal symbol statement: the current unknown `g_n` is still evolved by the lower-order hyperbolic operator. The obstruction is loss of regularity through the known source.

## 2. Why the loss can accumulate with perturbative order

At order `n+1`, the Taylor coefficient of the higher-derivative functional contains terms such as

`D E1[g0] g_n`

plus multilinear expressions in earlier coefficients. If the top part of `D E1` has differential order `q`, then the next solve demands higher regularity of `g_n` than is delivered by the same fixed-level energy estimate.

Thus, without extra estimates, the recursion is naturally organized on a descending regularity ladder rather than a single Sobolev space. For any fixed finite truncation `N`, sufficiently smooth initial/background data can in principle supply a finite regularity budget. What is not obtained is a uniform all-order fixed-`H^s` closure.

## 3. Weyl3 derivative count

The local correction under discussion is algebraic in curvature,

`S1[g] = integral sqrt(|g|) C^3`,

with no covariant derivatives of curvature in the Lagrangian density.

A curvature tensor contains two derivatives of the metric. In the metric variation, the `delta Riemann` term carries two derivatives of `delta g`; after integration by parts, the generic Euler-Lagrange structure contains up to two derivatives acting on `dL/dRiemann`. Since `dL/dRiemann` is quadratic in curvature, generic terms can therefore contain up to four derivatives of the metric.

Hence the metric Euler-Lagrange differential order is generically fourth order (`q<=4`, with fourth-order terms allowed). This must not be confused with the EFT label "six-derivative interaction": `C^3` has six derivatives in operator/power counting because each curvature contributes two, but its metric field equation is not generically sixth differential order.

Under the frozen standard hyperbolic bookkeeping, an uncancelled fourth-order source term requires schematically `g_(n-1) in H^(s+3)` to place the source in `H^(s-1)`. The exact Sobolev indices depend on formulation, dimension, constraints and product estimates; the robust conclusion is the existence of positive derivative loss, not the numeral `3` as a formulation-independent invariant.

## 4. What could still close the hierarchy

Iter056E does not rule out any of the following, but none is currently established for QGR:

- special on-shell/Bianchi/gauge cancellations that lower the effective derivative order of the source;
- explicit order-reduction identities using lower-order equations to replace higher derivatives before estimating the source;
- analytic or Gevrey function spaces that tolerate controlled derivative growth;
- tame/Nash-Moser type estimates with smoothing;
- a finite perturbative truncation supplied with a sufficiently large regularity budget;
- a formulation-specific weighted Sobolev hierarchy with proved uniform bounds.

A future gate must establish one of these prospectively rather than assume it after seeing the obstruction.

## Scientific consequence

The prospective order-reduced architecture has now passed three structural checks and exposed one new mathematical limitation:

- Iter056B: only `L0` acts on each new coefficient;
- Iter056C: the first Weyl3 source has the required covariant Noether/Bianchi compatibility;
- Iter056D: lower-order strong hyperbolicity is conditionally inherited coefficient by coefficient;
- Iter056E: this by itself does **not** give all-order Sobolev closure because the known sources can lose derivatives.

Therefore the next high-information question is not another principal-symbol test. It is whether the Weyl3 source admits a prospective **equation-of-motion reduction/tame source identity** that lowers its effective derivative demand on lower-order coefficients while preserving covariance and the Iter056C compatibility identity.

## Claim ceiling

No historical QGR physical treatment is authorized. No convergence or Borel summability of the formal series, no divergence theorem, no physical instability, no ghost statement, no exact higher-derivative well-posedness, no global interacting measure, no regulator removal, no `c6` fixing/running, no `beta=1`, no UV completion, no experimental confirmation and no theory establishment follows. Theory established remains 0%.

No GitHub Actions run was required; the result is exact regularity/derivative-counting analysis.