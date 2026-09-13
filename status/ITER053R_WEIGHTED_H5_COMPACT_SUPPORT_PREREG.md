# Iter053R prospective preregistration — weighted-H5 compact-support Weyl3 action variation replacement

Frozen on 2026-09-13 **after** terminal diagnostic QD/QD2/QD3/QD3M, but **before any Iter053R implementation or production evidence**.

## Gate
`ITER053R-WEYL3-WEIGHTED-H5-COMPACT-SUPPORT-ACTION-VARIATION`

## Motivation and authority boundary
The original Iter053 production remains permanently classified `ITER053_NUMERICAL_OR_INFRASTRUCTURE_FAIL`; it is not rewritten. QD established severe outer-box support aliasing, QD2 independently converged the direct support-domain action variation by GL8, QD3M validated the Gauss-Jacobi moments/normalization, and QD3 prospectively passed its diagnostic `promising` criterion with weighted GJ3 H5 bulk vs direct GL8 relative residual `3.407157652190216e-07` on A0 and wrong-sign residual `1.944220429443305`.

These diagnostics justify a **fresh scientific replacement gate**. They are not pooled as evidence for Iter053R PASS.

## Scientific question
For a prospectively frozen genuinely four-dimensional A4+B2+C2 panel, does the compact-support directional derivative

`d/dε ∫ sqrt(-g(ε)) W3[g(ε)] d4x |0`

agree with

`∫ H5^{ab} h_ab d4x`,

where `H5 = A + I - 2 sqrt(-g) D5`, when the known bump factor is integrated with its exact Gauss-Jacobi weight rather than an outer-box tensor rule?

## Frozen panel
Use the same scientific lane structure as Iter053, `fail-fast:false`:
- **A**: four generic compact-support 4D lanes.
- **B**: two conformally-flat/null lanes.
- **C**: two determinant-one linear-coordinate covariance lanes.

To avoid using QD3 pilot evidence as a scored lane, **A0 is not sufficient by itself**: terminal classification requires all A4+B2+C2 lanes. Existing Iter053 seeds may be reused only as predetermined panel identifiers; no seed selection, dropping or replacement is permitted after Iter053R implementation begins.

## Frozen integration strategy
For every compact perturbation `h_ab=B p_ab`, with support radius `a=0.24` and
`B=prod_i (1-(x_i/a)^2)^4`, evaluate the H5 bulk with tensor Gauss-Jacobi `alpha=beta=4`.

Frozen H5 weighted orders:
- coarse `GJ2` = 16 H5 nodes;
- fine `GJ3` = 81 H5 nodes.

The direct action derivative is independently evaluated on support-domain Gauss-Legendre `GL7` and `GL8`, with symmetric five-point epsilon stencil and finest epsilon `5e-5`. The H5 coordinate derivative step remains `5e-4`.

No weighted order, support radius, H5 derivative step, epsilon, lane, seed or threshold may be retuned after production evidence is visible.

## Frozen validity controls
A lane is invalid rather than scientific FAIL if:
- Lorentzian signature fails at any required node/epsilon point;
- metric inverse residual exceeds `3e-11`;
- any scored output is non-finite;
- compact-support boundary construction/control fails at `1e-13`;
- for C lanes, `|det L-1| > 2e-12` or transformed metric/perturbation algebra residual exceeds `3e-11`.

## Frozen scientific thresholds
### Generic A lanes
All four must satisfy:
- `|direct_GL8| >= 1e-10`;
- direct epsilon final-step relative change `<=5e-4`;
- direct GL7->GL8 relative change `<=5e-4`;
- weighted H5 GJ2->GJ3 relative change `<=2e-3`;
- fine `direct_GL8` vs `bulk_GJ3` relative residual `<=3e-3`;
- coarse-to-fine identity-residual absolute change `<=3e-3`.

### Null B lanes
Both must satisfy:
- integrated `|direct_GL8| <=5e-8`;
- integrated `|bulk_GJ3| <=5e-8`;
- sampled `|W3| <=2e-10`;
- sampled `||P|| <=3e-9`;
- sampled `||H5|| <=3e-7`.

### Covariance C lanes
Both coordinate frames independently satisfy the applicable A thresholds, and:
- direct integrated covariance relative residual `<=2e-3`;
- weighted-H5 bulk covariance relative residual `<=2e-3`.

## Frozen negative control
Evaluate the historical wrong sign
`H5_wrong = A + I + 2 sqrt(-g) D5`
on every generic A lane.

Requirements:
- wrong-sign integrated residual is larger than correct-sign residual on **every** A lane;
- at least one A lane has wrong-sign residual `>=1e-2`.

No coefficient fit, sign scan or lane-specific convention is permitted.

## Frozen terminal classifier
After consuming every raw A4+B2+C2 artifact and frozen aggregate, only:
- `PASS_SCOPED_ITER053R_WEYL3_WEIGHTED_H5_COMPACT_SUPPORT_ACTION_VARIATION_CERTIFICATE`
- `SCIENTIFIC_FAIL_ITER053R_WEYL3_WEIGHTED_H5_COMPACT_SUPPORT_ACTION_VARIATION`
- `ITER053R_IMPLEMENTATION_OR_CONTROL_INVALID`
- `ITER053R_NUMERICAL_OR_INFRASTRUCTURE_FAIL`

are allowed.

## Interpretation lock
Even full PASS is a finite genuinely-4D compact-support computational certificate. It is not a global functional-derivative theorem, not experimental confirmation, not quantum amplitude/measure closure and not a complete quantum-gravity theory. `c6` remains symbolic/unfixed; `beta=1` remains unauthorized; `theory established=0%`.

The still-running original-contract retry `34769958632` remains independent authority and must be classified under its own frozen GL3/GL4 contract. Its result cannot alter this preregistration retroactively.
