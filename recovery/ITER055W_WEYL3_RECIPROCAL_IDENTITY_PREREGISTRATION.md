# Iter055W preregistration — Weyl3 reciprocal survival/decoupling identity

Date: 2026-09-14
Gate: `ITER055W-WEYL3-RECIPROCAL-SURVIVAL-DECOUPLING-IDENTITY`

## Frozen question
Within the same formal reduced/fixed-background scaling object already used by Iter054I/J, does an exact reciprocal identity make the incompatibility between fixed-band nonzero Weyl3 survival and formal higher-derivative root-scale decoupling independent of the pure-power ansatz for `c6(h)`?

## Frozen source identities
Use only the Iter054I/J formal identities on a fixed Weyl-active background and fixed nonzero physical frequency `k`:

`rho(h,k) = A(h) h^4 k^2`,

`k_HD(h) = 1 / (h^2 sqrt(A(h)))`,

where for this diagnostic gate `A(h)>0` is an arbitrary positive function or sequence representing the magnitude entering the same formal object. In the original Iter054I source `A=|c6*Cbar|` with regulator-independent symbolic `c6` and fixed bounded curvature coefficient. Allowing arbitrary `A(h)` here is a mathematical control only; it does not authorize physical running of `c6` or the background curvature.

Freeze a fixed nonzero Weyl-active background coefficient and fixed physical `k != 0`. Handle the exact Weyl-flat sector separately.

## Frozen obligations
1. Algebraically derive or refute `rho(h,k) * k_HD(h)^2 = k^2` for every `h` where `A(h)>0`.
2. Do not assume a power law, monotonicity, differentiability or existence of a beta function for `A(h)`.
3. Prove the asymptotic implications for any sequence `h_n -> 0`:
   - if `k_HD(h_n) -> infinity`, then `rho(h_n,k) -> 0`;
   - if `rho(h_n,k) -> rho_*` with `0<rho_*<infinity`, then `k_HD(h_n) -> |k|/sqrt(rho_*)`, finite nonzero;
   - if `rho(h_n,k) -> infinity`, then `k_HD(h_n) -> 0`;
   - if `k_HD(h_n) -> K_*` finite nonzero, then `rho(h_n,k) -> k^2/K_*^2` if the limit exists.
4. Treat `Cbar=0` as the separate exact-zero correction sector; do not divide by zero or assign a finite `k_HD` there.
5. State explicitly that `k_HD` is a **formal higher-derivative characteristic/root scale** in this frozen diagnostic model, not an established physical ghost pole/mode.
6. State explicitly that arbitrary `A(h)` is a diagnostic necessity test and does not authorize `c6(h)` running, regulator dependence of physical couplings, a cutoff, or order reduction.

## Frozen classifications
- `PASS_SCOPED_ITER055W_ANSATZ_INDEPENDENT_SURVIVAL_DECOUPLING_INCOMPATIBILITY__C6_RUNNING_NOT_AUTHORIZED` if the exact reciprocal identity holds and proves the frozen implications without a power-law assumption.
- `FAIL_SCOPED_ITER055W_RECIPROCAL_IDENTITY_DOES_NOT_FOLLOW_FROM_ITER054I_OBJECT` if the identities do not imply the claimed reciprocal relation.
- `INVALID_PROVENANCE_ITER055W_ITER054I_J_OBJECTS_NOT_SAME_SCALING_MODEL` only if the source formulas cannot be used consistently as one frozen diagnostic object.

## Interpretation ceiling
A PASS strengthens Iter054J from a pure-power diagnostic to an ansatz-independent necessity theorem **inside the same formal scaling model**. It does not authorize running `c6`, select exact versus order-reduced/EFT dynamics, prove a physical extra mode/ghost, strong hyperbolicity, unitarity, UV completion, regulator removal, GR recovery, experiment or theory establishment.

No GitHub Actions run is preregistered; this is an exact algebraic/asymptotic gate.
