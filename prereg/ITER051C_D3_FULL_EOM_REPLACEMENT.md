# Iter051C-D3 preregistration — five-point full-EOM replacement

Frozen before implementation on 2026-09-13.

## Scientific question
Does the replacement Weyl^3 Euler-response assembly using the independently validated five-point covariant derivative and the `A + I - 2 sqrt(-g) D5` sign pass mutually independent generic, anisotropic variational, conformally-flat-null, and covariance controls without coefficient fitting?

## Scope
This is a finite computational certificate only. Even a full PASS does not constitute a global analytic theorem for arbitrary 4D metrics, does not fix `c6`, and does not establish QGR as a correct or complete quantum-gravity theory.

Historical G51C and G51C-D2 failures remain terminal and are never rewritten.

## Frozen implementation
- Algebraic `A` and lowering-insertion `I` are inherited unchanged from the audited G51C implementation.
- The second-divergence term is computed only through the independent nested five-point covariant derivative already used in D2N/D2R.
- Assembly is fixed as `H5 = A + I - 2 sqrt(-g) D5`.
- No coefficient fitting, sign search, or post-result threshold adjustment is allowed.
- Stencil sequence: `h = 2e-3, 1e-3, 5e-4`.

## Frozen panel
16 independent lanes:
- A0–A3: four fresh generic polynomial metrics, seeds `141003,141211,141421,141631`; check signature/inverse/algebraic controls, nonzero response, symmetry and h-convergence.
- B0–B5: six fresh anisotropic Bianchi-I points `(p,q,t)` = `(-0.7,0.2,0.85)`, `(0.2,0.65,1.15)`, `(-0.4,0.9,1.35)`, `(0.55,-0.15,1.6)`, `(1.25,0.35,1.9)`, `(-0.15,0.72,2.4)` against exact reduced variational targets.
- C0–C2: three conformally-flat FLRW controls using fresh times `0.55,0.85,1.25`; require Weyl^3 response to remain numerically null while curvature is nonzero.
- D0–D2: three fresh generic polynomial metrics, seeds `151007,151219,151433`, under fixed Lorentz transformations from the existing audited transform helpers; test tensor covariance.

## Frozen criteria
All lanes must be structurally valid.

A lanes:
- inverse residual `<= 2e-11`;
- Riemann/P algebraic residuals `<= 2e-9`;
- `||H5|| > 1e-7`;
- symmetry residual `<= 3e-7`;
- final-step relative change `<= 8e-4`.

B lanes:
- exact target components all `> 1e-10` in magnitude;
- each component relative residual `<= 1e-3`;
- vector relative residual `<= 5e-4`;
- final-step relative change `<= 8e-5`;
- historical `+2D` control residual `>= 1e-2`.

C lanes:
- curvature norm `> 1e-6`;
- `|I3| <= 2e-10`;
- `||P|| <= 3e-9`;
- `||H5|| <= 2e-7`.

D lanes:
- determinant/metric/inverse transform controls `<= 2e-11` (and `|det L-1| <= 2e-12`);
- base `||H5|| > 1e-7`;
- covariance relative residual `<= 1.5e-3`;
- base final-step change `<= 8e-4`.

## Frozen classifier
PASS iff 16/16 expected lanes are present, parseable, control-valid and lane-PASS.

PASS label: `PASS_SCOPED_G51C_D3_FIVEPOINT_FULL_EOM_REPLACEMENT_CERTIFICATE`.
FAIL label: `SCIENTIFIC_FAIL_G51C_D3_FIVEPOINT_FULL_EOM_REPLACEMENT` unless the first causal failure is demonstrably infrastructure/implementation/numerical invalidity, in which case no scientific classification is assigned and only a minimal repair preserving this preregistration is permitted.

## Interpretation lock
A PASS may mark the finite-panel full-EOM replacement certificate as established for these controls and may authorize the next genuinely covariant directional-variation/full-functional-derivative certificate. It may not set `theory established > 0`, fix `c6`, authorize `beta=1`, claim experimental confirmation, or convert finite panels into global theorems.
