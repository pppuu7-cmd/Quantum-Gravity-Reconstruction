# Iter057E derivation — G3-origin Weyl3 parity/degree decomposition

Date: 2026-09-15
Gate: `ITER057E-G3-ORIGIN-WEYL3-LINEARIZATION-PARITY-DEGREE-DECOMPOSITION`
Prospective preregistration: `c6ff3a2cdc5d2fc4ad45e397aa838827eb2aff2c`

## 1. Exact inversion symmetry of the source background

The Iter057D source metric is

`g00=1+2Phi`, `gij=-(1-2Phi)delta_ij`, `g0i=0`,

with

`Phi=(kappa/2)(y1^2+y2^2-2y3^2)`.

Under the exact coordinate involution

`P:y^a -> -y^a`,

`Phi(-y)=Phi(y)` and therefore

`P^* gbar = gbar`.

The origin is a fixed point of `P` and

`dP|_0 = -I`.

Thus `P` is an exact local isometry of the frozen source metric, not an approximate weak-field symmetry.

## 2. Naturality of the Euler operator and its linearization

The Iter056X tensor

`E_W3[g] = 1/2 g I3 - P_R.R - 2 nabla nabla P_R`

is constructed naturally from the metric, its Levi-Civita connection and curvature by tensor contraction and covariant differentiation. Therefore for any diffeomorphism `phi`,

`E_W3[phi^* g] = phi^* E_W3[g]`.

Linearize this identity about the `P`-invariant background `gbar`. If

`L := D E_W3[gbar]`

is the linearized rank-two metric operator, then

`L[P^* h] = P^* L[h]`.

This is an exact equivariance relation for the full local fourth-order operator.

## 3. Fixed-point parity of local derivative coefficients

Write the local operator at the origin schematically as

`(Lh)_ab(0) = sum_{m=0}^4 A_ab{}^{cd|mu1...mum}(0) partial_mu1...partial_mum h_cd(0)`.

Under `P`, every covariant tensor index contributes one factor of `-1` from `dP=-I`.

- The input perturbation `h_cd` has two tensor indices, so its tensor-index factor is `(-1)^2=+1`.
- The output `Lh` has two tensor indices, giving another `+1`.
- Each coordinate derivative contributes one additional `-1`.

Therefore an `m`-derivative term acquires exactly the parity factor

`(-1)^m`.

At the fixed point the background coefficient tensor `A_m(0)` must equal its pullback under the exact background isometry. Equivariance therefore requires

`A_m(0) = (-1)^m A_m(0)`.

Hence

**`A_m(0)=0` for every odd `m`.**

For a fourth-order operator the only allowed derivative orders are therefore

`m=4,2,0`.

Equivalently, for the homogeneous covector decomposition,

**`L_W3(k) = L4(k) + L2(k) + L0`**

with

**`L3(k)=0`, `L1(k)=0`.**

This conclusion uses only exact source inversion symmetry plus tensorial naturality; it does not assume a field equation, gauge condition, or high-frequency approximation.

## 4. Agreement with the source-jet identities

The same result is visible directly from Iter057D:

- `Gamma(0)=0`;
- `nabla C(0)=0`;
- `nabla P_R(0)=0`;
- the first derivatives of every even background coefficient vanish at the origin.

Thus the coefficient derivatives that could multiply `partial^3 h` or `partial h` vanish. The parity proof is stronger because it establishes the cancellation at the level of the complete natural operator rather than term by term.

## 5. Identification of the degree-four block

Only the double-covariant-derivative sector of Iter056X can generate four perturbation derivatives. At the fixed point its degree-four part comes from

`-2 partial partial [ (partial P_R / partial R) . delta R_principal(h) ]`.

The curvature Hessian `partial P_R/partial R = partial^2 I3/partial R^2` is exactly the algebraic object used in the Iter054B/C principal-Hessian construction. Contracting it with two principal metric-to-curvature maps gives the `k4` Weyl3 metric symbol already audited by Iter054C and reused by Iter057A-C.

Therefore, up to the already-fixed common convention and global symbolic `c6` multiplier,

**`L4 = M4_Weyl3`**

of the existing principal-symbol chain.

No new `k4` object is introduced by Iter057E.

## 6. Exact dependency map for the degree-two block

The degree-two Weyl3 block is not determined by `L4` alone. It receives source-owned contributions from several classes.

### 6.1 Algebraic Euler terms

The variations of

`1/2 g I3`

and

`- P_R.R`

contain `delta R_principal ~ partial^2 h`. Therefore they directly contribute algebraic-background-curvature coefficients multiplying two perturbation derivatives.

These terms depend only on the local background `C`, `R`, `P_R` and the algebraic first/second curvature derivatives of `I3`.

### 6.2 Metric-explicit part of delta P

`P_R(g,R)` has explicit metric dependence through Weyl projection and index raising. The part of `delta P_R` algebraic in `h` is acted on by the outer two derivatives in `-2 nabla nabla P_R`, producing additional degree-two terms with coefficients algebraic in the background curvature.

### 6.3 Background connection/curvature acting on the curvature-response delta P

Even at a normal-coordinate point with `Gamma=0`, a second covariant derivative of a tensor is not identical to a second ordinary derivative at subleading degree: derivatives of the background connection are fixed by the background curvature. Terms of the form

`(partial Gamma)_bar * delta P_R[delta R_principal]`

therefore contribute at degree two.

### 6.4 Second derivatives of the curvature-Hessian coefficient

Write the curvature-linear part schematically as

`delta P_R = H_RR(y) . delta R + ...`,

where `H_RR=partial^2 I3/partial R^2` is linear in the background Weyl tensor for the cubic invariant.

Then

`partial^2 [H_RR(y) delta R]`

contains

`H_RR partial^2 delta R`  -> degree four,

`2 (partial H_RR) partial delta R` -> degree three,

`(partial^2 H_RR) delta R` -> degree two.

At the G3 origin `partial H_RR` / `nabla H_RR` vanishes because `nabla C=0`, eliminating the degree-three term. But `partial^2 H_RR`, equivalently the source-determined second curvature/Weyl coefficient jet, can be nonzero and contributes to `L2`.

### 6.5 Variation of the outer covariant derivatives

The variation of the Levi-Civita connections in `nabla nabla P_R` generates `partial delta Gamma * P_R`, hence degree-two terms. Terms proportional to `delta Gamma * nabla P_R` would be degree one, but `nabla P_R(0)=0`; parity requires their complete odd-degree sector to vanish in any event.

## 7. Degree-zero block

`L0` can receive contributions from:

- purely algebraic metric variation of the determinant/index/projector structure;
- second background coefficient derivatives acting on algebraic-in-`h` parts of `delta P_R`;
- the source-owned background `nabla nabla P_R` and its metric variation.

It is source-determined but is not part of the highest mixed-order characteristic data targeted immediately after this gate.

## 8. Consequence for the Iter057C two-block certificate

Iter057C proves an exact statement for

`M2_Einstein + lambda M4_Weyl3`

on its frozen null-cone algebraic panel.

Iter057E now shows that the full local G3-origin Weyl3 linearization has an additional **degree-two** block `L2_Weyl3`. On directions where the degree-four block is rank deficient, this degree-two correction competes at the same derivative order as the Einstein block.

Therefore the Iter057C two-block result is a genuine high-order structural certificate but is **insufficient by itself** to determine the full mixed-order local characteristic operator on the source-owned G3 background.

The next required construction is explicitly

`M2_total(k) = M2_Einstein(k) + c6 L2_Weyl3(k)`

together with the already-certified

`c6 L4_Weyl3(k)`.

Only after `L2_Weyl3` is constructed source-faithfully may the full mixed-order characteristic question be sharpened.

## Frozen obligation disposition

- A exact inversion symmetry: **SATISFIED**.
- B natural rank-two operator equivariance: **SATISFIED**.
- C derivative parity tracking: **SATISFIED**.
- D `k4+k2+k0` decomposition and odd-block vanishing: **SATISFIED**.
- E `L4` identity with existing Weyl3 principal block: **SATISFIED**.
- F source dependency map for `L2`: **SATISFIED**.
- G Iter057C sufficiency audit: **INSUFFICIENT FOR FULL LOCAL OPERATOR; `L2_Weyl3` REQUIRED**.
- H claim locks: **PRESERVED**.
