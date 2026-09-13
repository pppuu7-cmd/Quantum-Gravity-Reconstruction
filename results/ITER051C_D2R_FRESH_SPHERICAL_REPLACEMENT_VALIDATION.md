# Iter051C-D2R — Fresh spherical replacement validation

Date: 2026-09-13

## Frozen gate
`ITER051C-D2R-FRESH-SPHERICAL-REPLACEMENT-VALIDATION`

Preregistration commit: `2597fb51bc087a4332d5974db38e0641bfacccba`
Implementation commit: `2b45b84a7d6c7cdb8f23d38408c211f63f0ff497`
Aggregate classifier commit: `f354def364e765fefe5de1d66ccddc1885a2ebe1`
Workflow commit: `8f41ec289e996433a75a69f13b3f22215d167184`
Authoritative production head: `a5f1021f8596f8e00a4a39f0d366eb276de3b397`
Authoritative run: `34744139101`
Aggregate job: `103689280172`
Aggregate artifact: `10312909946`
Aggregate digest: `sha256:714f66fb514d9046e82a8ede2e4350bf3586989060469dbcdcc415ba22f830c0`

## Raw evidence consumed
All 12 lane artifacts were produced and downloaded by the frozen aggregate step; all artifact digests verified. The aggregate found 12/12 expected lanes, 12/12 structurally valid, 12/12 frozen PASS, 0 parse errors.

Frozen aggregate diagnostics:
- worst absolute component error: `1.5270905373565569e-09`;
- worst final-step change: `6.047761854580956e-09`;
- worst vector relative residual: `7.3382674860456824e-09`;
- minimum historical `+2D` vector residual: `1.4228139519895726`.

Representative raw lane 0: all three components PASS; vector relative residual `1.9559703710038416e-09`; final-step change `1.340580847217261e-09`; historical `+2D` residual `1.9848261850478663`.

## Scientific classification
`PASS_SCOPED_G51C_D2R_FRESH_SPHERICAL_REPLACEMENT_VALIDATION`

This establishes only that the independently implemented five-point covariant-derivative route validates the `-2D` Weyl^3 symmetry-reduced response on the prospectively frozen fresh spherical panel, including near-null points, without coefficient fitting and with the historical `+2D` form retained as a strong negative control.

It does **not** rewrite the historical G51C or G51C-D2 failures. It does **not** establish a full four-dimensional covariant Weyl^3 Euler-Lagrange tensor, a global theorem, a fixed value of `c6`, experimental confirmation, absolute energy positivity, or quantum unitarity.

## Authorization
D2R PASS authorizes exactly one separately preregistered replacement full-EOM validation using the five-point covariant derivative and the `-2D` sign. Historical G51C and D2 results remain terminal provenance records.
