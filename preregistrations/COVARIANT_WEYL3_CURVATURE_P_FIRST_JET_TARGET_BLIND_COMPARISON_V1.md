# COVARIANT_WEYL3_CURVATURE_P_FIRST_JET_TARGET_BLIND_COMPARISON_V1

Status: PROSPECTIVE PREREGISTRATION. This file is frozen before any new comparison with historical residuals.

## Fixed inputs

1. Curvature-derived object is fixed by `theory/covariant/QGR_WEYL3_CURVATURE_P_FIRST_JET_V1.md` at defining-source commit `fac9939927903213d2f834e8460ff4865dbd9897`:
   `P_R = 3 c6 Pi_g^*[C o C]`,
   `nabla_e P_R = 3 c6 Pi_g^*[(nabla_e C)oC + C o(nabla_e C)]`,
   with `c6=SYMBOLIC_UNFIXED`.
2. Historical generic-P results remain immutable, including tensor-only, tensor-density, and primitive-decomposition classifications. They may be consumed only after the curvature-derived instantiation has been generated from the fixed formulas above.
3. Iter049 authority and all programme claim locks remain unchanged.

## Target-blind execution order

A. Construct a finite exact-rational/algebraic witness panel for `(g,R,nabla R,h,...)` without reading any historical mismatch coefficient or residual value. The panel must contain at least one nonzero Weyl tensor and at least one nonzero Weyl first jet.

B. From each witness compute `C=Pi_g[R]`, `nabla C=Pi_g[nabla R]`, then instantiate `P_R` and `nabla P_R` only from the frozen formulas. No coefficient, sign, contraction, witness value, or normalization may be selected from a historical residual.

C. Independently evaluate the direct directional-variation lane and the covariant functional-derivative lane on exactly the same witnesses and conventions. The implementation must preserve the Frechet pairing convention for antisymmetric pairs and must state whether a tensor or density object is being differentiated.

D. Only after A-C are frozen may the comparator read the two outputs and classify them.

## Frozen classifications

- `PASS_SCOPED_CURVATURE_P_FIRST_JET_DIRECTIONAL_COVARIANT_EXACT_MATCH`: all preregistered witnesses agree exactly and all controls pass.
- `FAIL_SCOPED_CURVATURE_P_FIRST_JET_DIRECTIONAL_COVARIANT_MISMATCH`: at least one exact nonzero difference occurs with controls passing; record the first lexicographic witness and exact difference without repair.
- `BLOCKED_CURVATURE_P_FIRST_JET_COMPARISON_IMPLEMENTATION`: the independent lanes cannot be implemented without introducing an unpreregistered convention or object.
- `INFRASTRUCTURE_FAILURE`: provenance/source-lock/execution failure prevents scientific classification.

No tolerance weakening, post-hoc sign flip, fitted correction, witness deletion, or third symmetry reduction is allowed.

## Required controls

- exact arithmetic or symbolic exact-zero adjudication;
- nonzero `C` control;
- nonzero `nabla C` control;
- Weyl trace control;
- algebraic Riemann/pair-symmetry control;
- symbolic `c6` factorization control (no `c6` fixing/running);
- source/provenance lock to the preregistered formulas;
- independent lane construction before comparison;
- frozen aggregate consumed in addition to raw lane outputs/logs.

## Scope lock

Even a full PASS is a finite target-blind certificate for the preregistered witness panel. It is not a proof of the complete global 4D covariant Weyl^3 Euler-Lagrange tensor, not a global theorem, not quantum closure, and not experimental confirmation. `theory_established=0%` remains locked.