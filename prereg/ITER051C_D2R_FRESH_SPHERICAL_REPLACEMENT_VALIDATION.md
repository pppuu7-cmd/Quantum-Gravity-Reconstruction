# Iter051C-D2R — fresh spherical replacement held-out validation

Preregistered before implementation and before production results.

## Purpose
Test whether the fixed Weyl^3 response candidate `A + I - 2 sqrt(-g) D`, with `c6` symbolic/unfixed, reproduces independent exact spherical reduced Euler-Lagrange targets on a fresh panel when `D` is evaluated with the independently implemented nested fourth-order five-point covariant stencil qualified by D2N.

Historical G51C and D2 failures remain terminal and are not rewritten by this gate.

## Frozen panel
Twelve fresh `(profile, radius)` lanes, none identical to the D2 or D2N scientific points:
`(0,1.07),(1,1.11),(2,0.91),(0,1.41),(1,1.52),(2,1.63),(3,1.175),(3,1.190),(3,1.195),(3,1.205),(3,1.210),(3,1.335)`.

Five-point steps are frozen to `h=(2e-3,1e-3,5e-4)`.

## Frozen controls and thresholds
Each lane must have Lorentzian stencil-domain signature, metric inverse residual `<=2e-11`, nonzero vector target norm `>1e-10`, five-point final-step vector change `<=5e-5`, and historical `A+I+2sqrt(-g)D` vector residual `>=1e-2`.

For target components with `|target| >= 1e-5` (ordinary scale): component relative residual `<=2e-4`.
For target components with `|target| < 1e-5` (near-null scale): absolute error `<=2e-9`; when `|target|>1e-10`, predicted sign must match exact sign.
Additionally each lane must have vector relative residual `<=1e-4` and maximum component absolute error `<=2e-7`.

No coefficient fitting, retuning, threshold relaxation, profile replacement or lane deletion is permitted after viewing production output.

## Frozen interpretation
- 12/12 valid and PASS => `PASS_SCOPED_G51C_D2R_FRESH_SPHERICAL_REPLACEMENT_VALIDATION`; this may authorize a separately preregistered full-EOM replacement gate.
- Any valid scientific lane failure => `SCIENTIFIC_FAIL_G51C_D2R_FRESH_SPHERICAL_REPLACEMENT_VALIDATION`.
- Missing/invalid lanes => infrastructure/numerical invalid, not scientific PASS.

A PASS is finite-panel validation only, not a global variational theorem and not a complete 4D quantum-gravity result. Theory established remains 0%; `c6` remains unfixed; `beta=1` remains unauthorized.
