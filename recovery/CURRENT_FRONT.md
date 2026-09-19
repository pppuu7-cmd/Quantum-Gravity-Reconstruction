# QGR Current Research Front

Updated: 2026-09-19

## Programme status
`candidate_program_roadmap_readiness = 100%` is infrastructure/roadmap readiness only. `theory_established = 0%`. No experimental confirmation. `c6=SYMBOLIC_UNFIXED`; `beta=1` unauthorized.

## Preserved authority
Iter049 `ITER049-WEYL3-SPHERICALLY-REDUCED-VARIATIONAL-RESPONSE` remains authoritative at retry run `34719948722`, preregistration `72b21197d594ab6c5f36a34dfbd18a68b97d0a1d`, retry head `c8e574b2a78ae02c3e1476ef1daf7efc8268c342`; initial run `34719814120` remains diagnostic/non-authoritative. Iter048 terminal PASS 24/24 remains do-not-repeat. Historical covariant FAIL and generic-P diagnostics remain immutable.

## Curvature-dependent Weyl3 P / first jet v1 — terminal scoped PASS
Gate: `COVARIANT_WEYL3_CURVATURE_P_FIRST_JET_CONSTRUCTION_V1`.
Preregistration: `d081640ffed1122d314c835ac54fca3277ef1de9`.
Defining source: `theory/covariant/QGR_WEYL3_CURVATURE_P_FIRST_JET_V1.md`, commit `fac9939927903213d2f834e8460ff4865dbd9897`.
Durable result: `results/COVARIANT_WEYL3_CURVATURE_P_FIRST_JET_CONSTRUCTION_V1.md`, commit `a3e94fe07a9134842bb0c558fda4b2488cda6330`.
Classification: `PASS_SCOPED_CURVATURE_WEYL3_P_AND_FIRST_JET_DEFINED`.
Actions scientific run: not required by the frozen abstract construction gate.

With `C=Pi_g[R]`, `I3=C_ab{}^cd C_cd{}^ef C_ef{}^ab`, and symbolic `c6`, the Frechet curvature derivative is

`P_R = 3 c6 Pi_g^*[C o C]`.

Metric compatibility gives `nabla Pi_g=0`, hence

`nabla_e P_R = 3 c6 Pi_g^*[(nabla_e C) o C + C o (nabla_e C)]`.

The variational pairing fixes antisymmetric-pair normalization without component-coordinate ambiguity. Intrinsic pair-symmetry, Weyl-trace, Euler homogeneity `P_R:R=3L6`, jet product-rule, symbolic-c6 and target-blindness controls pass at the abstract tensor-map level.

This closes only the earlier missing-object-definition blocker. It does not establish that any historical residual is repaired and does not establish the complete 4D Weyl3 Euler-Lagrange tensor.

## Quantum front
The finite-cylinder kinematic amplitude-space and generic external action-phase map remain scoped PASS objects. Physical-action selection remains terminal BLOCKED; no physical measure, Hamiltonian, Born rule, physical unitarity or continuum limit is authorized.

## Next bounded step
Do not open another scientific gate in this iteration. On the next iteration reread recovery/front/latest commits and all Actions. The next allowed covariant step is one separately prospectively preregistered target-blind comparison that instantiates the frozen curvature-derived P/first-jet object. It must not read a historical residual to choose coefficients/signs/contractions. No third symmetry reduction.

## Locks
`theory_established=0%`; no experimental confirmation; `c6=SYMBOLIC_UNFIXED`; corrected Q10 LOCKED; `beta=1` unauthorized; finite panels are not global theorems; G45 does not prove absolute energy positivity or quantum unitarity; G35-G37 distant roots do not authorize physical weights; KMQGB `NEW_REQUIRED` unauthorized; classical != quantum; diagnostic != closure.