# Iter054K Preregistration — General-Scaling Fixed-Band No-Go

Date frozen: 2026-09-14

Gate: `ITER054K-WEYL3-GENERAL-SCALING-FIXED-BAND-NOGO`

## Motivation

Iter054J established the continuum-survival trilemma only for the diagnostic pure-power family `c6(h)=cbar6 h^(-s)`. The frozen Iter054H/I/J normalization contains a stronger exact algebraic relation that does not require a power-law ansatz.

## Frozen definitions

For fixed nonzero physical frequency `k`, fixed finite nonzero background curvature scale `Cbar`, regulator `h>0`, and arbitrary positive nonzero diagnostic coefficient magnitude `a(h)=|c6(h) Cbar|`:

`rho(h,k) = a(h) h^4 k^2`,

`k_HD(h) = 1/(h^2 sqrt(a(h)))`.

No physical regulator dependence of `c6` is authorized by introducing `a(h)`; it is only an arbitrary positive diagnostic function/sequence.

## Frozen target identity

The gate must verify exactly

`rho(h,k) * k_HD(h)^2 = k^2`,

or equivalently

`rho(h,k) = (k/k_HD(h))^2`.

## Frozen lanes

### A0 — exact identity

Use exact rational perfect-square controls for `a` and rational `h,k`. Require exact equality `rho*k_HD^2 = k^2` on every case. Include a deliberate malformed branch scale `k_bad=1/(h*sqrt(a))` that must fail the identity for at least one nontrivial case.

### A1 — arbitrary diagnostic sequences

Use frozen positive non-power-law families sampled at `h_n=2^-n`, including:

- `a_n = exp(sqrt(n))`;
- `a_n = (1+n)^3 * (1 + 1/(n+1))`;
- `a_n = h_n^-4 * (1 + 1/(n+1))`;
- `a_n = h_n^-4 / (1+n)^2`;
- `a_n = h_n^-4 * (1+n)^2`.

Check the numerical identity to relative tolerance `1e-12` and classify only the induced `rho`/`k_HD` behavior. These families are controls, not physical models.

### B0 — general compatibility theorem encoded as limit implications

At fixed nonzero `k`, require the frozen algebraic implications:

1. `k_HD -> infinity` implies `rho -> 0`;
2. `rho -> rho0`, `0<rho0<infinity`, implies `k_HD -> |k|/sqrt(rho0)`, finite/nonzero;
3. `rho -> infinity` implies `k_HD -> 0`.

The gate may use constructed positive sequences for each limit class, but the terminal statement must be tied to the exact identity, not empirical extrapolation from a finite panel.

### B1 — authority / anti-overclaim locks

Require all of:

- `c6_running_authorized=false`;
- `physical_cutoff_derived=false`;
- `finite_h_order_reduction_authorized=false`;
- `ghost_unitarity_hyperbolicity_claim=false`;
- `quantum_transition_authorized=false`;
- `beta_one_authorized=false`;
- `theory_established_pct=0`.

## Frozen terminal PASS classification

Only if A0/A1/B0/B1 are all valid and PASS:

`PASS_SCOPED_ITER054K_GENERAL_FIXED_BAND_CONTINUUM_SURVIVAL_NOGO__C6_RUNNING_NOT_AUTHORIZED`

## Interpretation lock

A PASS establishes only that, within the already frozen proxy normalization, **no arbitrary positive regulator dependence of `c6` can simultaneously keep a finite nonzero Weyl3 correction at fixed nonzero physical frequency and send the associated singular branch to infinite physical frequency**. This is stronger than the Iter054J pure-power result but remains a compatibility/no-go statement for the proxy normalization.

It does not establish a physical running law, renormalization group flow, microscopic cutoff, UV completion, full covariant Weyl3 EOM theorem, strong hyperbolicity, ghost content, unitarity, quantum amplitude/measure closure, experimental confirmation, or correctness of QGR. `c6` remains unfixed and `beta=1` remains unauthorized.
