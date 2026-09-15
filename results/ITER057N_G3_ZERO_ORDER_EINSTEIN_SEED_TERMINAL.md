# Iter057N terminal result — G3/H0 zeroth-order Einstein-seed neighborhood audit

Date: 2026-09-15
Gate: `ITER057N-G3-ZERO-ORDER-EINSTEIN-SEED-NEIGHBORHOOD-AUDIT`
Preregistration: `ebaead95ba38dc4521b57477c54bf7d4f1b11c83`
Implementation: `842d50cc3e5b471d4a2565321b0c86d570b7ad52`
Workflow head: `c38a7c3c8f88cfcdef8cfe9ab38340acf37992cc`
Actions run: `34954958651`
Job: `104334672800`
Artifact: `10390394884` (`iter057n-g3-zero-order-einstein-audit`)
Artifact digest: `sha256:ca6fd31f23b52f760a5cb85da6db8fd1945a4cc891b27e84e6cfbc0e006585a4`

## Terminal classification

**`SCIENTIFIC_FAIL_SCOPED_ITER057N_FIXED_G3_SEED_HAS_NONZERO_C6_ZERO_ORDER_EINSTEIN_RESIDUAL__SEED_CORRECTION_REQUIRED_BEFORE_OPEN_NEIGHBORHOOD_C6_SERIES`**

This is exactly the prospectively frozen scientific-FAIL classification. It applies only to the fixed exact G3/H0 metric as the `c6^0` neighborhood seed.

## Exact result

The origin statements remain exactly true:

`R_ab(0)=0`, `R(0)=0`, `G_ab(0)=0`.

However the first nonlinear coordinate jet is nonzero. In the frozen `(-,+,+,+)` presentation,

`G_00 = 3 kappa^2 (x^2+y^2+4 z^2) + O(|x|^4)`,

`G_11 = kappa^2 (x^2-y^2-16 z^2) + O(|x|^4)`,

`G_12 = 2 kappa^2 x y + O(|x|^4)`,

`G_13 = -4 kappa^2 x z + O(|x|^4)`,

`G_22 = -kappa^2 (x^2-y^2+16 z^2) + O(|x|^4)`,

`G_23 = -4 kappa^2 y z + O(|x|^4)`,

`G_33 = -kappa^2 (7x^2+7y^2-4z^2) + O(|x|^4)`.

There are 15 nonzero normalized second-derivative coefficients. A simple exact witness is

`partial_x^2 G_00(0)/kappa^2 = 6 != 0`.

The scalar curvature has the nonzero quadratic jet

`R = 10 kappa^2 (x^2+y^2+4 z^2) + O(|x|^4)`.

## Exact controls

Every frozen control passed:

- Ricci origin zero;
- scalar origin zero;
- Einstein origin zero;
- contracted Bianchi identity through degree one;
- exact Einstein trace identity `g^{ab}G_ab=-R`;
- direct full-rational `G_00` factorization.

The latter is

`G_00 = -3 kappa^2 (x^2+y^2+4z^2) (1+kappa x^2+kappa y^2-2 kappa z^2)`

`       / (kappa x^2+kappa y^2-2kappa z^2-1)^3`,

an exact rational component, not a Taylor-only diagnostic. It independently proves that the nonzero quadratic coefficient is genuine.

No numerical tolerance was used.

## Perturbative consequence

For the frozen formal expansion

`g = g0 + c6 q + O(c6^2)`,

the nonzero tensor above appears at order `c6^0`. An `O(c6)` correction cannot cancel it while `c6` remains a regular symbolic expansion parameter. Doing so would require changing the zeroth-order seed or introducing forbidden inverse powers/tuning of `c6`.

Therefore the existing Iter057L/M first-order correction jets cannot be promoted, on the **fixed exact G3/H0 seed**, to an open-neighborhood perturbative Einstein+Weyl3 background.

## What survives

This result does not invalidate:

- G3/H0 as a source-owned local operator/Weyl probe;
- the exact frozen-origin curvature and Weyl data;
- Iter057F3 off-shell operator reconstruction;
- Iter057L pointwise/general quadratic correction algebra;
- Iter057M exact quartic `O(c6)` coefficient-system certificate.

Those results remain finite/local/off-shell certificates under their stated scopes.

## Required successor

The next scientifically admissible constructor is a separate **`c6^0` Einstein-seed completion**. A quartic metric correction can preserve the origin metric, connection and curvature while changing the degree-two Einstein residual.

Crucially, such a quartic seed correction changes fourth metric derivatives at the origin. Since the Weyl3 Euler tensor contains the double-divergence of `P` and is generically fourth order in the metric, `E_W3(0)` must be recomputed on the corrected Einstein seed. The old G3/H0 Weyl3 source jet cannot be carried over automatically.

## Claim locks

This scoped FAIL does not show that no local Ricci-flat/Einstein completion with the same frozen curvature exists, nor that Einstein+Weyl3 is inconsistent. It only rejects the unchanged G3/H0 metric as the zeroth-order neighborhood seed.

`c6` remains symbolic/unfixed; `beta=1` remains unauthorized; theory established remains `0%`; no experimental, hyperbolicity, ghost, stability, unitarity, regulator-removal or UV-completion claim is authorized.