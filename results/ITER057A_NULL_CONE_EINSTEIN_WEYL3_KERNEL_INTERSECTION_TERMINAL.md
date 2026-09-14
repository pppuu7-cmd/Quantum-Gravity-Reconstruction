# Iter057A terminal result — null-cone Einstein/Weyl3 quotient-kernel intersection

Date: 2026-09-15
Gate: `ITER057A-NULL-CONE-EINSTEIN-WEYL3-QUOTIENT-KERNEL-INTERSECTION`
Prospective preregistration: `100849c18508b89cc36dade42ed18053916097c7`
Implementation: `f6df330f980fef2cde997ead7fe1a128ec8fa274`
Production head/workflow: `039e610f79aff02034a34c9f183c926297caa042`

## Authoritative production

- workflow run: `34904311442`
- job: `104177299559`
- conclusion: `success` (implementation completed; scientific classification is carried in the frozen output)
- artifact: `iter057a-null-cone-summary`, id `10372565865`
- artifact ZIP digest: `sha256:95fd17b39e49bd05b3bba938bd3dda41690a93b3a4f019a09b715c7ab6f2b182`
- 24 exact cases: 12 frozen rational Weyl backgrounds x 2 frozen null covectors

Green CI is not interpreted as scientific PASS. The preregistered scientific hypothesis failed in every valid case.

## Terminal classification

**`SCIENTIFIC_FAIL_ITER057A_COMMON_NULL_CONE_KERNEL_HYPOTHESIS_ON_FROZEN_PANEL`**

This is a scientifically valid negative result. It does not invalidate Iter056X/Y/Z or the earlier principal-symbol certificates.

## Frozen controls

All controls A-E were valid in all 24 cases:

- both covectors satisfy `k^2=0` exactly;
- pure-gauge matrix rank = 4;
- Einstein symbol annihilates all four gauge columns exactly;
- Weyl3 symbol annihilates all four gauge columns exactly;
- Einstein symbol rank = 4, nullity = 6;
- Weyl3 correction symbol rank = 4, nullity = 6, exactly reproducing the Iter054D null-covector diagnostic.

There were zero INVALID cases.

## Frozen hypothesis result

The preregistered hypothesis predicted that the two non-gauge Einstein null classes and the two non-gauge Weyl3 null classes would coincide, which would require

`dim(ker M2 ∩ ker M4) - dim(gauge) = 2`.

Instead, in **all 24/24 exact cases**,

`dim(ker M2 ∩ ker M4) = 5`

and

**`quotient_kernel_intersection_dim = 5 - 4 = 1`**.

Therefore the common-null-polarization hypothesis is false on the frozen panel.

## Stronger exact diagnostic

For each null covector, the Einstein kernel has dimension 6 and can be decomposed into the four gauge directions plus a two-dimensional non-gauge complement.

On that two-dimensional GR non-gauge kernel complement, every frozen Weyl background gave

**`rank(M4 restricted as a map) = 1`**.

Thus one linear combination of the two GR null classes remains in the Weyl3 kernel, while one independent GR null class is mapped nontrivially by the Weyl3 `k4` operator.

A second, subtler exact fact also held in all 24 cases:

**the Weyl3 bilinear form restricted to the two-dimensional GR null complement has rank 0**, even though the corresponding operator map has rank 1.

So the Weyl3 correction does not generate a nonzero self-bilinear on that two-dimensional GR null-polarization subspace; instead the nonzero image of one GR null class couples outside that subspace. This distinction is important for any future characteristic determinant or residue interpretation.

## Scientific consequence

The ordinary GR null cone is **not** represented on this frozen panel by two quotient classes that are simultaneously annihilated by both the Einstein `k2` and Weyl3 `k4` symbols.

Only one non-gauge common kernel class survives in every tested case.

This makes a simple “both GR polarizations remain untouched on the same light cone” continuation unavailable. The next mixed-order analysis must explicitly track the off-subspace coupling produced by `M4` and the rank of the combined operator near/on the null cone.

The result is compatible with, but does not yet prove, polarization splitting or a shifted additional characteristic branch. Such language is not authorized until the full combined quotient pencil is analyzed.

## What is not established

This SCIENTIFIC_FAIL does not establish:

- birefringence as a physical theorem;
- a shifted causal cone;
- complex characteristics;
- failure of strong hyperbolicity;
- an extra propagating physical mode or ghost;
- instability or negative energy;
- a preferred exact versus order-reduced treatment;
- a value/sign/running of `c6`;
- quantum nonunitarity or UV failure.

The tested backgrounds are exact local algebraic Weyl witnesses, not a theorem for arbitrary solutions of the full nonlinear equations.

## Claim locks

`c6` remains symbolic/unfixed; `beta=1` remains unauthorized; no physical Weyl3 treatment is selected; theory established remains `0%`; historical FAIL/INVALID/BLOCKED results remain immutable.