# QGR Iter047 — exact Weyl^3 curvature-class activation map

Date: 2026-09-13
Status: `PASS_SCOPED_EXACT_WEYL3_CURVATURE_CLASS_ACTIVATION_MAP`

## Authority and provenance
- Preregistration: `status/ITERATION_047.md`
- Preregistration commit: `dbd3745ad1082141790502b8423240771112ee03`
- Implementation commit: `bb44a0b2721dca861c84e7de55b482cd79bc9b25`
- Aggregate commit: `cb018321e7a061e2d82f558c68ed0e14d051ceb2`
- Workflow commit: `84280ed3fef58d10e3759e63b5b7277c08dc9497`
- Production trigger/head: `2c731e9a14c288e6e359c160476bc4bb0e78b801`
- Authoritative run: `34719070003`
- Aggregate job: `103621600017`
- Aggregate artifact: `10305937870`
- Aggregate digest: `sha256:7249e022a4b39241a5d61234c982e7b932b2eb9245c468c36f9ca1b54a35d2fb`

Frozen criteria were fixed prospectively and were not changed after production inspection.

## Terminal aggregate
The frozen aggregate consumed all **24/24** scientific lane artifacts with valid controls:
- A: 6/6 type-N pp-wave scalar-invariant blindness;
- B: 6/6 Schwarzschild/Petrov-D activation;
- C: 6/6 Kasner anisotropic Ricci-flat activation;
- D: 6/6 conformally-flat FLRW controls.

Terminal classification:

`PASS_SCOPED_EXACT_WEYL3_CURVATURE_CLASS_ACTIVATION_MAP`

`c6` remained `SYMBOLIC_UNFIXED` throughout.

## Representative exact witnesses
### Type-N pp-wave
A0 had nonzero curvature (`8` nonzero Riemann components), exact Ricci-flatness, nonzero Weyl tensor, yet
- `W2 = 0`;
- `W3 = 0`.

Thus the cubic scalar Weyl operator is algebraically blind on this nontrivial type-N witness. This explains why the exact nonlinear pp-wave PASS in Iter046 cannot by itself test a `c6*Weyl^3` correction.

### Schwarzschild / Petrov-D
B0 reproduced exactly
- `W2 = 48 M^2/r^6`;
- `W3 = 96 M^3/r^9`;
with exact cubic mass scaling and exact ninth-power radial scaling. For the frozen witness `M=1/5`, `r=3`, `W3=32/820125 != 0`.

### Kasner
C0 with exponents `(-1/3, 2/3, 2/3)` gave exactly
- `W2 = 64/(27 t^4)`;
- `W3 = 256/(243 t^6)`;
with exact `t^-4` and `t^-6` scaling and Ricci-flatness.

### Conformally-flat control
All six spatially-flat FLRW controls had nonzero Riemann curvature at their frozen witnesses while the Weyl tensor, `W2`, and `W3` vanished exactly.

## Scientific interpretation
The already-selected QGR six-derivative operator `Weyl^3` has a sharply curvature-class-dependent activation pattern:
- it is exactly blind on the tested type-N pp-wave and conformally-flat sectors;
- it is nonzero on tested Petrov-D Schwarzschild and anisotropic Ricci-flat Kasner sectors.

This is an **operator/invariant activation map** only. It identifies where a `c6` correction can in principle matter, but it is not yet a calculation of the correction to the field equations.

## Claim guard
This result does **not**:
- determine `c6`;
- prove that Schwarzschild or Kasner remain solutions once `c6 != 0`;
- derive the full covariant Euler-Lagrange tensor of `Weyl^3`;
- prove generic nonlinear stability, renormalizability, quantum unitarity, or experimental confirmation.

`theory established` remains **0%**.

## Next frontier
The next decisive step is variational: derive/test the coefficient of `c6` in an actual curved-background Euler-Lagrange response, with `c6` left symbolic. A symmetry-reduced Bianchi-I gate is acceptable if its scope is stated exactly and it is not promoted to the full covariant six-derivative equation.
