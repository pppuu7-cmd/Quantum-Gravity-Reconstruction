# Iter052 — Weyl3 genuinely 4D covariant directional variation

Date: 2026-09-13

## Frozen gate
`ITER052-WEYL3-4D-COVARIANT-DIRECTIONAL-VARIATION`

Prospective preregistration: `c49084e54428042cf59e5ac083ee49f0614a3de0`.
Scientific implementation: `b9da6cdfc424d712b80db935f16f89c00f8f5b9f`.
Frozen aggregate: `79dff35e80c5095688d898b78bb78d7b80768657`.
Workflow: `ff68b12968fdce2b6c220880009c256406309a65`.

The initial production run `34748588704` remains permanently `ITER052_IMPLEMENTATION_OR_CONTROL_INVALID`: lane C2 used a determinant-one coordinate control whose constructed transform had `det L = 1.000000003317951`, violating the frozen control tolerance. Its scientific identity residuals were small, but it is not admissible terminal evidence. Authority record: `888c3d398dee4785f094037a6ad56929e18da671`.

Control-only correction: `da0957ee8f818195435e3804c2611b1411a01a98`. It changes only the construction of the determinant-one transform; scientific identity, metrics, perturbations, witnesses, finite-difference steps and thresholds are unchanged.

## Authoritative retry
- head: `d82370f18c76caebd5aa4ee567cb450a882d7bad`
- run: `34748813339`
- aggregate job: `103702164522`
- summary artifact: `10315226969`
- summary digest: `sha256:b4b8c4b75046541f25b6a5f3f469e2d59e94c2b6571a6f1645b6e94f53f82009`

All 12 fresh raw lane artifacts were present and consumed by the frozen aggregate. No evidence from the invalid initial run was pooled into the retry classification.

## Frozen identity

`d/dε [sqrt(-g) W3](g+ε h)|_{ε=0} = H5^{ab} h_ab + ∂_μ Θ^μ`

with

`H5 = A + I - 2 sqrt(-g) D5`

and the independently evaluated boundary current

`Θ^μ = 2 sqrt(-g) [P^{μ(αβ)ν} ∇_ν h_{αβ} - h_{αβ} ∇_ν P^{μ(αβ)ν}]`.

`c6` is symbolic/unfixed and is not fitted in this gate.

## Terminal scientific classification

**`PASS_SCOPED_ITER052_WEYL3_4D_COVARIANT_DIRECTIONAL_VARIATION_CERTIFICATE`**

Fresh retry aggregate:
- expected lanes: 12
- found lanes: 12
- valid lanes: 12
- PASS: 12
- FAIL: 0
- controls valid: true
- streams: A6 + B3 + C3
- parse errors: none

Worst frozen diagnostics:
- A direct step change: `2.2454009841693144e-10`
- A identity relative residual: `2.0319192562122008e-09`
- A identity-residual step-change absolute: `1.4031547766917923e-09`
- B `||H||`: `5.32275825898538e-26`
- B `||P||`: `5.1320734159286665e-33`
- B absolute identity mismatch: `1.789685316967841e-20`
- C base identity relative residual: `1.3767967976953127e-09`
- C transformed identity relative residual: `2.4005443702369267e-09`
- C direct covariance relative residual: `7.863429053040412e-11`
- C RHS covariance relative residual: `2.439292835420146e-09`

## Interpretation lock
This is a finite, genuinely four-dimensional computational directional-variation certificate for the frozen panel. It is stronger than the earlier symmetry-reduced checks, but it is **not** a global functional-analytic theorem and does not establish a complete quantum-gravity theory. Historical G51C and D2 scientific failures remain unchanged. `c6` remains unfixed, `beta=1` remains unauthorized, and theory established remains 0%.

## Next authorized gate
A stronger integrated compact-support action-variation certificate is authorized for prospective preregistration. It must test the integrated Weyl3 action with compactly supported perturbations so that the boundary-current contribution vanishes independently, include quadrature/refinement controls and held-out covariance/null controls, and must not reuse another symmetry-reduced minisuperspace panel as its primary evidence.