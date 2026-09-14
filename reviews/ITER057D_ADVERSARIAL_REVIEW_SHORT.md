# Iter057D short adversarial review

Reviewed terminal Constructor result `e0f305be490a979f9c0dfa626a8e4e4e2f47fb3f` against prospective preregistration `5697e6789d33b9edfb5d94d00f90c03b3e14a771`.

Current recovery files lag main: they still name Iter056X active, while the latest commit window has advanced through terminal Iter057D and a newer nonterminal Iter057E derivation. This review therefore uses the newest terminal result visible in the latest-ten-commit window and does not issue a verdict on Iter057E.

Counterexample-first check: the obvious failure mode would be that the frozen quadratic metric supplies only curvature at the origin but not the coefficient derivatives required by the covariant Weyl3 Euler linearization. That counterexample does not work. For the explicit source metric, `g(y)` is even, `g^{-1}(y)` is even wherever locally invertible, the Levi-Civita connection is odd, and curvature/Weyl tensors are even. Hence at `y=0`, `Gamma=0` and `nabla C=0`, while `nabla nabla C` and the corresponding derivatives of `P=dI3/dR` are fixed uniquely by differentiating the same analytic source metric. Linearizing `E_W3 = 1/2 g I3 - P.R - 2 nabla nabla P` therefore needs no independent background derivative datum beyond that source-owned metric jet.

The trace-free H0 Hessian gives exact Ricci/scalar cancellation at the frozen origin because first metric derivatives vanish there, so the local Ricci tensor depends only on the frozen second derivatives. The corrected nonzero cubic invariant is sufficient as a Weyl-activity witness; its convention-dependent sign is not used to infer dynamics.

Scope firewall: this closes only **background-jet adequacy at the single frozen G3/H0 origin**. It does not provide the full mixed-degree linearized operator, a neighborhood/global characteristic theorem, hyperbolicity, mode/ghost content, treatment selection, absolute micro-to-tidal calibration, or quantum consistency. The fact that ordinary derivatives of `g_ab` above second order vanish must not be extended to inverse-metric, connection, curvature, or Weyl coefficient derivatives; those generally do not vanish, only remain source-determined.

Chronology is clean: preregistration preceded derivation, the Weyl-cubic sign correction occurred before terminalization, and no post-hoc normalization was introduced. No Actions run was needed for this exact source-identity/jet-adequacy gate. Historical FAIL/BLOCKED states remain intact; `c6` is symbolic/unfixed; `beta=1` is unauthorized; classical/local certification is not quantum closure; theory established remains `0%`.

VERDICT: CONFIRMED_SCOPED