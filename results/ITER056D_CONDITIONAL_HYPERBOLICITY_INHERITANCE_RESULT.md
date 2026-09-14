# Iter056D terminal result — conditional lower-order hyperbolicity inheritance in the formal perturbative hierarchy

Date: 2026-09-14
Preregistration: `48542590c8bd292bc4eaa9ad9666d0e7eab4eee2`

## Terminal classification

`PASS_SCOPED_CONDITIONAL_ITER056D_FORMAL_ORDER_REDUCED_COEFFICIENT_EQUATIONS_INHERIT_LOWER_ORDER_STRONG_HYPERBOLICITY__QGR_GAUGE_OBJECT_STILL_MISSING`

## 1. Principal symbol is unchanged by the prescribed perturbative source

Iter056B gives at every formal order

`L0 g_n = S_n[g0,...,g_(n-1)]`,

where the new unknown `g_n` appears only through the lower-order linearized operator `L0`.

Fix any admissible gauge/constraint reduction of `L0` and write its first-order-in-time principal form schematically as

`partial_t U_n + A^i(x) partial_i U_n + B(x) U_n = F_n(x)`,

where `F_n` is determined by previously solved perturbative orders.

The principal symbol at spatial covector `xi` is

`P0(x,xi)=A^i(x) xi_i`.

The inhomogeneous source `F_n` contains no derivatives of the **new** unknown `U_n`, so it does not enter `P0` at all.

Therefore all characteristic speeds, eigenspaces, diagonalizers and any frozen lower-order symmetrizer are exactly those of the lower-order homogeneous gauge-fixed problem.

## 2. Strong-hyperbolicity inheritance is exact under the frozen assumptions

Assume the lower-order principal system is strongly hyperbolic on an open domain: for example it admits a uniformly bounded complete eigenbasis, or equivalently in the frozen formulation a uniformly positive symmetrizer `H(x,xi)` with the required regularity/bounds.

Because the principal matrix is unchanged, the same diagonalizer/symmetrizer applies to the `n`-th perturbative coefficient equation.

Thus the higher-derivative Weyl3 correction does not create a new principal characteristic branch **inside this formal order-reduced coefficient equation**. Its effect appears through the source constructed from lower perturbative orders.

This is exactly different from the unresolved exact mixed-order equation of Iter054E/F, whose principal object contains the formal singular branch.

## 3. Conditional energy estimate

For a strongly hyperbolic lower-order system, the standard inhomogeneous estimate has schematic form

`||U_n(t)|| <= C exp(c t) [ ||U_n(0)|| + integral_0^t ||F_n(s)|| ds ]`

in the norm/function space supplied by the chosen lower-order formulation, with the usual modifications for variable coefficients and Sobolev order.

The estimate shows the precise remaining obligation: control the regularity/size of `F_n` and the initial/boundary data. The source can be large or contain high derivatives of lower-order coefficients; hyperbolicity inheritance does not by itself bound it.

## 4. Extension to every formal perturbative order

Iter056B proves that the same `L0` multiplies every new `g_n`. Hence the principal-symbol argument repeats unchanged at all orders of the regular formal hierarchy, provided the lower-order fields make `S_n` regular enough for the chosen inhomogeneous problem.

No `D E1[g0] g_n` term appears at the same perturbative order, so the exact higher-derivative principal operator is never reintroduced into the equation for the current unknown coefficient.

## 5. Constraint/gauge caveat

Iter056C establishes the first-order covariant Noether/Bianchi source compatibility. Iter056D does not supply the actual QGR gauge reduction, full constraint propagation system, boundary conditions or function space.

If a later source violates the compatibility conditions of the chosen lower-order constrained formulation, solvability can still fail even though the principal symbol is hyperbolic. That is a source/constraint problem, not a change in the principal characteristic matrix.

## Scientific consequence

A future **versioned perturbative/order-reduced QGR candidate** has a coherent conditional PDE architecture:

- regular formal-series sector excludes the singular branch in the control (Iter056A);
- every perturbative coefficient is governed by the lower-order linearized operator (Iter056B);
- the first Weyl3 source is covariantly conserved/Bianchi-compatible (Iter056C);
- any independently supplied strongly hyperbolic lower-order gauge formulation is inherited coefficient-by-coefficient (Iter056D).

This is materially different from exact higher-derivative QGR and does not retroactively select the perturbative treatment for the historical candidate.

## Next highest-information gate

The next mathematical risk is **derivative loss in the sources**. Even though the new unknown is acted on by a lower-order hyperbolic operator, `S_n` can contain higher derivatives of already-known coefficients through `E1`. Determine prospectively whether a standard Sobolev hierarchy closes without increasing required regularity at every perturbative order, or whether the formal recursion suffers derivative loss that prevents uniform all-order control. This can first be tested abstractly by derivative counting and then, if needed, on the Weyl3 variational source structure.

## Claim ceiling

No historical QGR physical treatment is authorized. No QGR-specific gauge reduction, exact-HD hyperbolicity, all-order source regularity, convergence/remainder theorem, physical ghost/mode statement, c6 running, cutoff, quantum unitarity, UV completion, regulator removal, full GR recovery, experiment or theory establishment follows. Theory established remains 0%.

No GitHub Actions run was required; the result is exact conditional principal-symbol/PDE reasoning.
