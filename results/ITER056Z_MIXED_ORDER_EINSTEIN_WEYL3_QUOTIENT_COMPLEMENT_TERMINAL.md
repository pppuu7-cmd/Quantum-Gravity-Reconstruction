# Iter056Z terminal result — Einstein/Weyl3 mixed-order quotient complement

Date: 2026-09-15
Gate: `ITER056Z-MIXED-ORDER-EINSTEIN-WEYL3-QUOTIENT-COMPLEMENT-CERTIFICATE`
Prospective preregistration: `f22452dbb2491b64ab40df42e59660f96d0e99eb`
Upstream rank theorem: `8368407bcf7b379fa2040b88f7a8fc3b3b4e3501`

## Terminal classification

**`PASS_SCOPED_ITER056Z_EINSTEIN_K2_SYMBOL_COMPLEMENTS_WEYL3_K4_QUOTIENT_KERNEL_FOR_NONNULL_COVECTORS`**

The statement is local, principal-symbolic, and restricted to non-null covectors `k^2 != 0`. It is not a characteristic/hyperbolicity theorem.

## 1. Exact quotient cross-section

For a symmetric perturbation `h_ab`, define the de Donder functional

`F_b(h) = k^a h_ab - (1/2) k_b h`,

with `h=gbar^{ab}h_ab`.

A principal pure-gauge perturbation is

`G_k(xi)_ab = k_a xi_b + k_b xi_a`.

Its trace is `2 k.xi`, and therefore

`F_b(G_k xi)`

`= k^a(k_a xi_b+k_b xi_a) - (1/2)k_b(2k.xi)`

`= k^2 xi_b`.

Hence for `k^2 != 0`, every gauge orbit intersects `F=0` exactly once: given arbitrary `h`, choose

`xi_b = - F_b(h)/k^2`.

Uniqueness follows because `F(G_k xi)=0` implies `xi=0` for non-null `k`.

Thus the de Donder slice is an exact six-dimensional linear cross-section of the ten-dimensional symmetric-tensor space modulo the four-dimensional diffeomorphism gauge subspace.

This use of de Donder is only quotient linear algebra. It is **not** a claim that ordinary second-order de Donder gauge by itself supplies a justified gauge fixing for the full fourth/mixed-order hyperbolicity problem.

## 2. Einstein principal symbol in the same curvature convention

Use the same local all-lowered Riemann principal convention as the Iter054C Weyl map:

`delta R_abcd|_pr = (1/2)(k_c k_b h_ad + k_d k_a h_bc - k_d k_b h_ac - k_c k_a h_bd)`.

Contracting gives

`delta R_bd|_pr = (1/2)(k_b k^a h_ad + k_d k^c h_bc - k_b k_d h - k^2 h_bd)`

and

`delta R|_pr = k^a k^b h_ab - k^2 h`.

Therefore the principal linearized Einstein tensor is

`sigma2_E(h)_bd`

`= (1/2)(k_b F_d + k_d F_b - gbar_bd k.F)`

`  - (1/2) k^2 (h_bd - (1/2)gbar_bd h)`.

No scalar proxy or symmetry reduction is used.

## 3. Restriction to the unique quotient slice

On `F=0`,

**`sigma2_E(h)_ab = -(1/2) k^2 R(h)_ab`**, 

where the trace-reversal map is

`R(h)_ab = h_ab - (1/2) gbar_ab h`.

In four dimensions trace reversal is an involution:

`R(R(h)) = h`.

Moreover `F(h)=0` is equivalent to transversality of the trace-reversed tensor:

`k^a R(h)_ab = F_b(h) = 0`.

Thus trace reversal gives a linear isomorphism

`de Donder quotient slice  <->  transverse symmetric output tensors`.

Both spaces have dimension six for non-null `k`. Since `k^2 != 0`, multiplication by `-(1/2)k^2` is also invertible. Consequently

**`rank sigma2_E_bar(k) = 6`**

on the six-dimensional diffeomorphism quotient for every non-null covector.

Equivalently, the Einstein degree-two quotient symbol is injective and has no nonzero quotient kernel away from the metric null cone.

## 4. Exact complement of the Weyl3 high-order kernel

Iter056Y proved for the same non-null quotient that

`rank sigma4_W3_bar(k) <= 5`,

so

`dim ker sigma4_W3_bar(k) >= 1`.

Let `[h]` be any nonzero quotient class in that kernel. Then

`sigma4_W3_bar(k)[h] = 0`.

But the Einstein quotient symbol is injective, so necessarily

**`sigma2_E_bar(k)[h] != 0`**.

Therefore every nonzero Weyl3 fourth-order quotient-kernel direction is controlled nontrivially by the lower-order Einstein principal block for `k^2 != 0`.

This proves the frozen complement statement without choosing a numerical value or sign of `c6`.

## 5. Conformally-flat control

If the background is conformally flat, `Cbar=0`. The cubic curvature Hessian vanishes and hence

`sigma4_W3_bar(k)=0`

on all six quotient directions.

For every non-null `k`, the Einstein symbol remains rank six on the quotient. Thus all quotient directions reduce consistently to the ordinary second-order Einstein principal structure in this control sector.

## 6. Structural PDE consequence

Combining Iter056Y and Iter056Z gives an exact local order hierarchy for non-null covectors:

- the Weyl3 degree-four block is intrinsically quotient-rank-deficient;
- the Einstein degree-two block is quotient-nondegenerate;
- any high-order-null quotient direction is therefore lower-order-controlled rather than unconstrained.

Hence the full exact-truncation linearized operator must be treated as a genuinely **mixed-order** system. A schematic notation is

`M(k) = M2_E(k) + c6 M4_W3(k) + lower Weyl3 degrees`,

with the understanding that different quotient directions can have different leading differential orders and that a Douglis-Nirenberg-compatible assignment may be required.

This is stronger than merely observing a finite rank deficiency: it proves that the missing high-order rank is complemented by the Einstein block away from `k^2=0`.

## 7. What is still open

This result does not determine the characteristic roots of the mixed-order system because characteristics require analysis through and near the null cone `k^2=0`, exactly where the non-null quotient cross-section argument changes character and the Einstein symbol loses invertibility.

It does not establish:

- strong or symmetric hyperbolicity;
- an open-region real-characteristic theorem;
- diagonalizability or a symmetrizer;
- gauge-constraint propagation for a full mixed-order gauge formulation;
- an energy estimate;
- physical mode count or ghost residue/sign;
- a preferred exact versus order-reduced treatment;
- stability, quantum unitarity, or UV completion.

## 8. Production decision

No GitHub Actions run was launched. All statements are exact consequences of the prospectively frozen linear-algebraic gate and the already-certified principal curvature convention. A sampled numerical panel would not strengthen the non-null isomorphism theorem.

## Claim locks

`c6` remains symbolic/unfixed; `beta=1` remains unauthorized; no physical treatment is selected; no hyperbolicity/ghost/energy/unitarity/UV/experiment/theory-establishment claim is authorized. `theory established = 0%`.