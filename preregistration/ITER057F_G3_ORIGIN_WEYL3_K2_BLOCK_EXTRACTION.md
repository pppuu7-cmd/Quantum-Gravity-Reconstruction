# Iter057F preregistration — G3-origin Weyl3 degree-two block extraction

Date: 2026-09-15
Gate: `ITER057F-G3-ORIGIN-WEYL3-DEGREE2-BLOCK-EXTRACTION`

## Motivation

Iter057E proves that the full local Weyl3 linearization on the source-owned G3/H0 inversion-fixed origin has only degrees `4,2,0`. The degree-four block is already the Iter054C curvature-Hessian symbol. The missing object needed for the full mixed-order characteristic operator is therefore the degree-two Weyl3 block `L2_Weyl3`.

The corrected Iter051C-D3 five-point full-EOM evaluator already computes the complete covariant Weyl3 Euler density coefficient using the authoritative `A+I-2 sqrt(-g) D5` sign. This gate reuses that evaluator rather than creating a second full-EOM engine.

## Frozen source background and convention

Use the existing G3/H0 metric with `kappa=0.08=2/25`, evaluated at the source origin.

For compatibility with the existing Iter054C exact principal-symbol code and the Iter051C full-EOM evaluator convention, use the global `(-,+,+,+)` signature representation of the same source geometry:

`g00=-(1+2Phi)`,

`gij=(1-2Phi)delta_ij`,

`Phi=(kappa/2)(x^2+y^2-2z^2)`.

This is a frozen signature-convention translation `g_-=-g_+`, not a new metric deformation or physical normalization. All exact comparison objects in this gate use the same `(-,+,+,+)` convention.

Freeze

`k=(1,1,0,0)`

which is exactly null under `eta=diag(-1,1,1,1)`.

Use the existing 10 symmetric-metric basis elements from Iter054C.

## Frozen perturbation family

For basis tensor `H_j`, define

`g_ab(x;epsilon,s,j) = gbar_ab(x) + epsilon H_j,ab cos(s k_mu x^mu)`.

The metric class must provide analytic `g`, `partial g`, and `partial partial g` to the full-EOM evaluator; no finite-difference metric derivatives are allowed.

At the origin, parity implies the exact linearized response polynomial

`R_j(s) = L0_j + s^2 L2_j + s^4 L4_j`.

## Frozen numerical extraction panel

Use frequency training points

`s = 0, 1, 2`

and held-out control

`s_hold = 3/2`.

Use central perturbation-amplitude differences at

`epsilon = 2e-4, 1e-4`.

Use corrected five-point double-divergence stencil spacings

`h_D = 1e-3, 5e-4`.

For each `(epsilon,h_D,s)` compute

`R_j(s) = [E_W3(gbar+epsilon H_j cos(sk.x)) - E_W3(gbar-epsilon H_j cos(sk.x))] / (2 epsilon)`

at the origin using `assemble_minus5` only.

From training responses define exactly

`A = R(1)-R(0)`,

`B = R(2)-R(0)`,

`L4 = (B-4A)/12`,

`L2 = A-L4`,

`L0 = R(0)`.

No fitted polynomial degree or post-output frequency selection is allowed.

## Frozen lane structure

Ten independent scientific lanes, one per symmetric-metric input basis element, `fail-fast:false`.

Each lane emits its `4x4` matrices `L0,L2,L4` for all two epsilon values and both `h_D` values, plus controls. Aggregate runs only after all ten lane artifacts exist.

## Frozen controls

A. **Source/signature validity.** All nested `±4 h_D` stencil metric points for both perturbation signs must remain finite, invertible and Lorentzian in the frozen `(-,+,+,+)` convention.

B. **Amplitude linearization convergence.** At finest `h_D=5e-4`, compare the extracted `L2,L4` between `epsilon=2e-4` and `1e-4`. Require relative Frobenius changes <= `5e-3`, using denominator floor `1e-10`.

C. **Stencil convergence.** At finest `epsilon=1e-4`, compare `L2,L4` between `h_D=1e-3` and `5e-4`. Require relative Frobenius changes <= `1e-2`, floor `1e-10`.

D. **Held-out frequency.** At finest `(epsilon,h_D)=(1e-4,5e-4)`, predict

`R(3/2)=L0+(9/4)L2+(81/16)L4`

and require relative Frobenius residual <= `3e-3`, floor `1e-10`.

E. **Exact degree-four control.** Construct the exact G3/H0 continuum Weyl tensor at the origin in the same `(-,+,+,+)` principal-curvature convention, convert it to the Iter054C bivector operator, and compute the exact `Q` matrix for the frozen `k`.

For each lane j, convert the extracted `L4_j` output tensor to the bilinear column

`B_ij = sum_ab H_i,ab (L4_j)_ab`.

No fitted scale/sign is allowed. Require direct relative residual of this numerical column against exact `Q[:,j]` <= `2e-2`.

A systematic convention mismatch fails/invalidates the gate; it may not be repaired after seeing output by multiplying by an empirical factor.

F. **Aggregate symmetry.** The assembled numerical `L4` bilinear matrix must be symmetric within relative Frobenius residual `<=2e-3` and agree with exact `Q` within `2e-2`.

G. **Degree-two gauge control.** Assemble the degree-two output operator from all ten lanes. For each of the four exact pure-gauge input tensors

`h_ab=k_a xi_b+k_b xi_a`,

require the numerical `L2` output norm divided by `max(||L2||,1e-10)` <= `5e-3`.

H. **L2 result is measured, not presumed.** Record its norm, rank at frozen numerical tolerance, trace structure and action on the two-dimensional non-gauge Einstein null complement. No PASS predicate requires `L2` to be nonzero or to have a desired sign/rank.

## Frozen classifications

Maximum PASS if A-G hold:

`PASS_SCOPED_ITER057F_G3_ORIGIN_WEYL3_K2_BLOCK_EXTRACTED_WITH_EXACT_K4_CONTROL`.

`INVALID_ITER057F_FULL_EOM_EXTRACTION_OR_CONVENTION_CONTROL` if source/signature, exact `L4`, convergence, held-out-frequency, symmetry or gauge controls fail.

There is no scientific FAIL tied to a preferred `L2` rank/sign; any controlled `L2` result is retained.

## Interpretation ceiling

This is a finite-precision computational extraction at one source-owned background point and one null covector. It does not establish a global covariant closed form for `L2`, the full characteristic variety, strong/symmetric hyperbolicity, physical birefringence, ghost content, stability, energy, treatment selection, unitarity or UV completion.

`c6` remains symbolic/unfixed; `beta=1` unauthorized; theory established remains 0%.