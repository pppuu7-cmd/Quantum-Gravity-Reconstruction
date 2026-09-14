# Iter057A preregistration — null-cone Einstein/Weyl3 quotient-kernel intersection

Date: 2026-09-15
Gate: `ITER057A-NULL-CONE-EINSTEIN-WEYL3-QUOTIENT-KERNEL-INTERSECTION`

## Motivation

Iter056Y/Z establish the exact non-null structure: the Weyl3 `k4` quotient symbol is rank-deficient, while the Einstein `k2` quotient symbol is nondegenerate for `k^2 != 0`. The unresolved characteristic question is therefore concentrated on the metric null cone, where the Einstein quotient symbol itself becomes singular.

Iter054D previously recorded a diagnostic fact: for each of two frozen null covectors and 12 exact rational Weyl-active backgrounds, the correction-only Weyl3 10x10 symbol had rank 4 / nullity 6. That result did not compare its two non-gauge null classes with the two familiar Einstein null-polarization classes.

## Frozen hypothesis

On the existing exact Iter054C/D panel, the two non-gauge null classes of the Weyl3 `k4` symbol coincide with the two non-gauge null classes of the Einstein `k2` symbol at the same null covector.

This is a finite exact panel hypothesis, not a global theorem.

## Frozen objects

Use exactly the Iter054C rational local-background construction:

- `W_seed = background_operator(seed)` for `seed=0,...,11`;
- the same symmetric-metric basis and the same exact metric-to-Weyl principal map;
- no new background tuning.

Use exactly the two Iter054D null covectors:

- `k0=(1,1,0,0)`;
- `k1=(5,3,4,0)`;

with metric `eta=diag(-1,1,1,1)`, so `k^2=0` exactly.

For each of 24 cases construct:

1. `M4=Q(W_seed,k)` from the exact Iter054C Weyl3 curvature-Hessian symbol;
2. `M2` from the principal linearized Einstein tensor derived by contracting the **same** principal Riemann convention used by Iter054C;
3. the exact 10x4 pure-gauge matrix `K(k)` with columns `h_ab=k_a xi_b+k_b xi_a`.

## Frozen controls and predicates

A. `k^2=0` exactly for both covectors.

B. Gauge map rank is exactly 4 for each nonzero null covector.

C. Both symbols annihilate all four gauge columns exactly:

`M2 K = 0`, `M4 K = 0`.

D. Einstein null-cone control:

`rank M2 = 4`, `nullity M2 = 6`, hence quotient-kernel dimension `6-4=2`.

E. Weyl3 reproduction control:

`rank M4 = 4`, `nullity M4 = 6` in every case, reproducing the prior Iter054D correction-only diagnostic on the exact same panel.

F. Kernel-intersection object:

Compute exactly

`dim(ker M2 ∩ ker M4)`

as the nullity of the vertically stacked linear map `[M2; M4]`.

Since the four-dimensional gauge subspace lies in the intersection, define

`q_intersection_dim = dim(ker M2 ∩ ker M4) - 4`.

The frozen common-null-polarization hypothesis predicts

`q_intersection_dim = 2`

for all 24 cases.

G. Negative result handling: if any structurally valid case has `q_intersection_dim<2`, do not tune the background/covector panel and do not redefine the quotient. Record the hypothesis as scientifically false/partial on the frozen panel.

## Frozen classifications

Maximum PASS if A-F pass in all 24 cases:

`PASS_SCOPED_ITER057A_GR_AND_WEYL3_SHARE_TWO_NONGAUGE_NULL_CONE_KERNEL_CLASSES_ON_FROZEN_PANEL`.

Scientific FAIL if implementation/controls A-E are valid but F fails in at least one case:

`SCIENTIFIC_FAIL_ITER057A_COMMON_NULL_CONE_KERNEL_HYPOTHESIS_ON_FROZEN_PANEL`.

INVALID if any object/provenance/control A-E is not reproduced:

`INVALID_ITER057A_NULL_CONE_SYMBOL_OR_PROVENANCE_CONTROL`.

## Interpretation ceiling

Even a full PASS would establish only exact kernel alignment on the frozen local algebraic-background panel. It would not prove that the full mixed-order characteristic polynomial has only the GR light cone, would not establish strong hyperbolicity, constraint propagation, energy positivity, physical mode count, ghost absence, stability, or a preferred exact/order-reduced treatment.

`c6` remains symbolic/unfixed; `beta=1` unauthorized; theory established remains 0%.