# Iter051C-D2Z — exact spherical near-zero conditioning map

Date: 2026-09-13
Gate: `ITER051C-D2Z-EXACT-SPHERICAL-ZERO-CONDITIONING`

## Prospective authority
Preregistered before implementation/production. This is an exact symbolic diagnostic independent of the numerical D2/D2N double-divergence evaluation. It does not change the terminal D2 FAIL or any frozen threshold.

## Question
For the sole D2 failed spherical profile
`F=2+r/8+r^2/12`, `N=1+r/5`, `S=3/2+r+r^3/50`,
is the exact Iter049 angular reduced Weyl^3 Euler–Lagrange coefficient `E_S(r)` genuinely close to a simple positive real zero near the D2 witness `r=6/5`, making componentwise relative error strongly ill-conditioned there?

## Frozen exact computation
Use only the generic exact symbolic Iter049 radial-gauge-unfixed Euler–Lagrange authority. Substitute the B3 profile exactly with rational coefficients, simplify `E_F(r),E_N(r),E_S(r)` to rational functions, factor/together `E_S`, and analyze the numerator polynomial/rational numerator exactly where possible.

Report:
- exact/simplified `E_S(r)` expression string and numerator/denominator degrees;
- exact `E_S(6/5)` and high-precision decimal;
- high-precision `E_F,E_N,E_S` at `6/5`;
- all real positive numerator roots found at >=40-digit working precision;
- nearest positive root `r0` to `6/5` and distance `|r0-6/5|`;
- `dE_S/dr` at `6/5` and at `r0`;
- dimensionless relative radial condition indicator `kappa_r = |r E_S'(r)/E_S(r)|` at `6/5`;
- amplitude ratio `|E_S|/max(|E_F|,|E_N|)` at `6/5`.

## Frozen descriptive classes
`DIAGNOSTIC_EXACT_NEAR_ZERO_CONDITIONING_CONFIRMED` iff:
- an isolated positive real numerator root exists within `0.1` of `6/5`;
- `|dE_S/dr|` at that root is nonzero at 30-digit precision;
- `kappa_r >= 100` at `6/5`;
- `|E_S|/max(|E_F|,|E_N|) <= 1e-3` at `6/5`.

Otherwise:
`DIAGNOSTIC_EXACT_NEAR_ZERO_CONDITIONING_NOT_CONFIRMED`.

Algebra/authority construction failure:
`ITER051C_D2Z_IMPLEMENTATION_INVALID`.

## Interpretation lock
This exact map can establish conditioning of the chosen reduced component, not correctness of the numerical full tensor. Even a confirmed near-zero does not turn D2 into PASS. D2N's independent five-point result remains separately required before any replacement validation is authorized. `c6` stays unfixed and theory established stays 0%.
