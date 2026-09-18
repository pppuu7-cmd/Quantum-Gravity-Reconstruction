# COVARIANT_WEYL3_DIRECTIONAL_VARIATION_SEED_PANEL_FREEZE

Date: 2026-09-18
Status: PROSPECTIVE / FROZEN BEFORE IMPLEMENTATION OR AGREEMENT INSPECTION
Parent preregistration: `8c21ee233423deaff52d0fa552c027fa065a53a7`

This file only makes the already-required finite covariant witness panel concrete. It does not alter the parent scientific criterion, invariant convention, sign, normalization, `c6`, outcome vocabulary, or claim locks.

## Representation

Use one 4D Lorentzian point-jet at x=0 per seed, in coordinates `(x0,x1,x2,x3)`. Store covariant metric jets

`g[a,b; i1...ik] = partial_{i1}...partial_{ik} g_ab |0`, k=0..4,

with exact rational entries, symmetric in `(a,b)` and in derivative indices. Perturbation jets `h[a,b; i1...ik]` are stored for k=0..2 with the same symmetries. No symmetry reduction, radial gauge, static ansatz, or field equation is imposed.

For all non-flat seeds set `g[a,b]=diag(-1,1,1,1)` at order 0 and first metric derivatives to zero. This is a local normal-coordinate representation, not a restriction on curvature: second and higher jets are nonzero and generic. All curvature, covariant-derivative, direct-variation, integration-by-parts, and Euler-source witnesses must be reconstructed from these jets by each lane independently.

## Deterministic exact generator

Canonical unordered pair rank: `p(a,b)=min(a,b)*4+max(a,b)`.
For a sorted derivative multi-index `I=(i1,...,ik)`, define

`N_s(a,b,I) = ((s+3)*17 + 19*p(a,b) + sum((j+1)*(I[j]+1)*23 for j=0..k-1) + 29*k + 7*(a+1)*(b+1))`.

For metric jets of order k>=2 use

`g_s[a,b;I] = sign(N_s) * (1 + (N_s mod 11)) / (13 + ((N_s//11) mod 17))`,

where `sign(N)=+1` if `N mod 4` is 0 or 1 and `-1` otherwise. Populate all permutations from the canonical sorted I and symmetric `(a,b)` value. Seed labels use s=11 and s=23.

For perturbation direction d use the independent integer

`M_d(a,b,I) = ((d+5)*31 + 37*p(a,b) + sum((j+2)*(I[j]+1)*41 for j=0..k-1) + 43*k + 5*(a+2)*(b+3))`

and

`h_d[a,b;I] = sign(M_d) * (1 + (M_d mod 13)) / (17 + ((M_d//13) mod 19))`, k=0..2,

with the same canonical symmetrization. Direction labels use d=7 and d=19.

The formulas above, rather than implementation output, are authoritative. A lane must serialize the full generated jet tables and SHA256 them before computing agreement.

## Frozen panel

- `FLAT_CONTROL`: Minkowski metric with every derivative jet through order 4 exactly zero. Evaluate both perturbation directions d=7,19. This is the Ricci-flat/Einstein control; Weyl3 and its first variation are expected to vanish at the flat point for the cubic invariant, but the implementation must derive rather than hard-code this.
- `OFFSHELL_A`: metric jet generator s=11 through order 4, perturbations d=7 and d=19.
- `OFFSHELL_B`: metric jet generator s=23 through order 4, perturbations d=7 and d=19.

Thus the frozen panel has six seed/direction cells. `OFFSHELL_A/B` are accepted as off-shell witnesses only if independently computed controls show at least one nonzero Ricci component and nonzero scalar curvature in each seed. If that precondition fails, the gate is BLOCKED; seeds must not be replaced post hoc.

## Required target-blind serialization order

For each lane, before reading the other lane or any candidate Euler-contraction output, serialize: generated metric/perturbation jet tables and hashes; inverse/determinant point controls; Riemann/Ricci/scalar/Weyl tensors and algebraic/Bianchi controls; Weyl and required covariant-derivative jets; direct `delta(sqrt(-g) I3)` decomposition into h, dh, d2h coefficients; the integration-by-parts current convention and resulting bulk coefficient; independently constructed Euler-source ingredients; final contraction; exact discrepancy; per-cell hashes.

Researcher and Critic must not share helper code implementing curvature variation, integration by parts, or the Euler source. Shared files may contain only this frozen data-generation specification and generic canonical JSON/hash utilities.

## Frozen adjudication

The parent PASS criterion is unchanged. All six cells must satisfy the parent exact-zero discrepancy requirement and both lanes must reproduce all frozen controls. Any scientific nonzero discrepancy is retained as localization evidence. Any generator/serialization/execution defect is BLOCKED and requires a separately preregistered execution-only repair before retry.

## Locks

`theory_established=0%`; no experimental confirmation; `beta=1` unauthorized; `c6=SYMBOLIC_UNFIXED`; corrected Q10 LOCKED; finite covariant panel is not a global theorem; no quantum-unitarity, regulator-removal, UV-completion, unique-theory, new-physics, or KMQGB `NEW_REQUIRED` claim is authorized.