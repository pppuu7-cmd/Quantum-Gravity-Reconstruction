# Iter056D preregistration — conditional lower-order hyperbolicity inheritance in the formal perturbative hierarchy

Date: 2026-09-14
Gate: `ITER056D-CONDITIONAL-LOWER-ORDER-HYPERBOLICITY-INHERITANCE`

## Frozen question
Given the Iter056B hierarchy

`L0 g_n = S_n[g0,...,g_(n-1)]`,

if one supplies a fixed lower-order gauge/constraint reduction of `L0` that is strongly hyperbolic on an open covector/background domain, does every perturbative coefficient equation inherit exactly that lower-order principal symbol/hyperbolicity structure because the Weyl3 correction appears only in a prescribed inhomogeneous source?

This is a conditional PDE theorem for a future order-reduced candidate version, not historical QGR treatment authority and not a construction of the missing gauge reduction of Iter054F.

## Frozen assumptions
1. A lower-order gauge-reduced linear operator `L0^gf` is fixed independently of the higher-derivative result.
2. On the frozen open domain, `L0^gf` has a strongly hyperbolic first-order-in-time formulation (or equivalent) with uniformly complete eigenvectors / positive symmetrizer / energy estimate in the chosen standard sense.
3. At perturbative order `n`, `S_n` is a known source built only from already-determined lower-order coefficients and has the regularity required by the inhomogeneous problem.
4. Constraint/source compatibility required by the chosen lower-order formulation is assumed or independently verified; Iter056C supplies only the first covariant divergence compatibility at action level.
5. No claim is made about convergence of the full perturbation series or the exact mixed-order equation.

## Frozen obligations
1. Show that adding a prescribed inhomogeneous source does not alter the principal symbol of the equation for `g_n`.
2. Show that the characteristic speeds/eigenvectors/symmetrizer of the homogeneous principal system are therefore those of the lower-order gauge-fixed formulation.
3. State the corresponding conditional energy/Duhamel estimate form and identify source regularity dependence.
4. Extend the structural statement to every formal order using Iter056B.
5. Separate this from exact-HD strong hyperbolicity: the exact mixed-order equation has a different principal object and remains BLOCKED by Iter054F/G-R.
6. Do not infer that QGR already supplies a suitable gauge, boundary conditions, constraint system or function space.

## Frozen classifications
- `PASS_SCOPED_CONDITIONAL_ITER056D_FORMAL_ORDER_REDUCED_COEFFICIENT_EQUATIONS_INHERIT_LOWER_ORDER_STRONG_HYPERBOLICITY__QGR_GAUGE_OBJECT_STILL_MISSING` if the principal/hyperbolicity inheritance is exact under the frozen assumptions.
- `FAIL_SCOPED_ITER056D_INHOMOGENEOUS_WEYL3_SOURCE_CHANGES_PRINCIPAL_SYMBOL_OF_NEW_COEFFICIENT_EQUATION` if the source necessarily modifies the principal operator at the same perturbative order.
- `INVALID_ITER056D_ASSUMPTIONS_DO_NOT_DEFINE_A_HYPERBOLIC_LOWER_ORDER_PROBLEM` only if the conditional statement cannot be posed consistently.

## Interpretation ceiling
A PASS is conditional mathematical support for a separately versioned perturbative candidate formulation. It does not provide the missing QGR gauge/evolution object, prove source regularity at all orders, convergence/remainder control, exact-HD hyperbolicity, physical treatment authority, unitarity, UV completion, regulator removal, GR recovery, experiment or theory establishment.

No GitHub Actions run is preregistered; this is exact PDE/principal-symbol reasoning.
