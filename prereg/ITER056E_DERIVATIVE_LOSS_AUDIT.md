# Iter056E preregistration — derivative-loss audit for the formal order-reduced hierarchy

Date: 2026-09-14

## Frozen question

Given the Iter056B hierarchy

`L0 g_n = S_n[g0,...,g_(n-1)]`,

with `L0 = D E0[g0]` the lower-order hyperbolic operator and `E1` a higher-derivative local correction, does a fixed Sobolev regularity class close coefficient-by-coefficient under standard inhomogeneous hyperbolic estimates, or does the recursion generically demand increasing regularity of lower coefficients?

## Frozen assumptions

1. Work only at the level of the already-authorized formal hierarchy; do not promote it to historical QGR physical treatment authority.
2. Let the gauge-fixed lower-order problem admit a standard strong-hyperbolic energy estimate with source regularity one spatial derivative below the solution norm, schematically `F in H^(s-1) -> U in H^s`.
3. Let the highest differential order of the local correction functional `E1` acting on its metric argument be `q>1`; no post-hoc cancellation, smoothing, special background identity or field redefinition may be assumed.
4. For the local algebraic-curvature action `sqrt(|g|) C^3`, use only the generic variational fact that an action depending algebraically on curvature but not derivatives of curvature yields Euler-Lagrange terms containing at most two covariant derivatives acting on `dL/dRiemann`, hence generically up to fourth derivatives of the metric (`q<=4`, with fourth-order terms generically allowed).
5. A PASS for non-closure means only that the naive fixed-Sobolev all-order recursion is not closed by existing estimates. It does not prove divergence of the formal series, physical inconsistency, or impossibility of analytic/Gevrey/tame/Nash-Moser control.

## Frozen tests

A. Derive the regularity requirement on `g_(n-1)` coming from a source term with `q` derivatives under the standard hyperbolic estimate.

B. Determine whether a fixed `H^s` assumption on every coefficient is sufficient when `q>1` without extra structure.

C. Specialize the derivative count to curvature-cubic Weyl3, carefully distinguishing the name "six-derivative operator" in EFT power counting from the differential order of the metric Euler-Lagrange equation.

D. State the minimal remaining mathematical routes that could remove the obstruction (special cancellations/order reduction identities, analytic/Gevrey scale, tame estimates with a regularity ladder, or a finite-order truncation with enough initial smoothness) without authorizing any of them.

## Frozen terminal ceiling

Maximum allowed positive classification:

`PASS_SCOPED_ITER056E_NAIVE_FIXED_SOBOLEV_ALL_ORDER_RECURSION_HAS_DERIVATIVE_LOSS__NO_CONVERGENCE_OR_PHYSICAL_FAILURE_CLAIM`

No GitHub Actions load is permitted unless a genuinely computational subproblem appears.