# Iter054J Preregistration — Weyl3 Continuum-Survival Scaling Trilemma

Date: 2026-09-14
Gate: `ITER054J-WEYL3-CONTINUUM-SURVIVAL-SCALING-TRILEMMA`

## Frozen question

Using only a diagnostic power-law family `c6(h)=cbar6*h^(-s)`, what scaling threshold is necessary to retain a finite nonzero Weyl3 correction on fixed physical-frequency/curvature bands, how does the singular higher-derivative proxy branch scale simultaneously, and can any one pure power law satisfy both nonzero continuum survival and branch decoupling?

## Frozen assumptions

- This family is diagnostic only; it is not a physical assignment or renormalization law.
- `cbar6` is symbolic, finite, nonzero and independent of h.
- Physical `k` and nonzero finite `Cbar` are held fixed independently of h.
- Start from the already-certified Iter054I proxy identities `rho=|c6*Cbar| h^4 k^2` and `k_HD=1/(h^2 sqrt(|c6*Cbar|))`.
- Therefore under `c6(h)=cbar6*h^(-s)`, freeze `rho~h^(4-s)` and `k_HD~h^(s/2-2)`.

## Frozen lanes

### A0 — symbolic exponent census
Must return the exact exponents `4-s` for rho and `s/2-2` for k_HD and classify the three regimes:
- `s<4`: rho -> 0, k_HD -> infinity;
- `s=4`: rho -> finite nonzero, k_HD -> finite nonzero;
- `s>4`: rho diverges, k_HD -> 0.

### A1 — rational witness panel
Use frozen rational s panel `{0,2,7/2,4,9/2,6}` and decreasing rational h. Require each case to match the preregistered asymptotic regime for both rho and k_HD.

### B0 — compatibility/trilemma proof
Freeze the logical obligations:
- finite nonzero fixed-band Weyl3 survival requires `4-s=0`, hence `s=4`;
- branch decoupling to infinite physical frequency requires `s/2-2<0`, hence `s<4`;
- these conditions are mutually incompatible for a single pure power-law scaling.
The lane must fail closed if it finds an s satisfying both.

### B1 — authority/anti-overclaim controls
Must preserve:
- no physical regulator dependence of c6 authorized;
- no physical cutoff/refinement-stop scale derived;
- no finite-h order-reduced treatment authorized;
- no beta=1 authorization;
- no ghost/unitarity/hyperbolicity claim;
- no quantum amplitude/measure transition;
- theory established remains 0%.

## Frozen aggregate classification

PASS only if all lanes are valid/pass, with exact classification:

`PASS_SCOPED_ITER054J_POWERLAW_CONTINUUM_SURVIVAL_TRILEMMA__C6_RUNNING_NOT_AUTHORIZED`

Otherwise fail closed with lane evidence preserved.

## Interpretation lock

A PASS establishes only a proxy-level asymptotic compatibility obstruction for the frozen pure power-law family. It does not establish that c6 runs with h, does not derive a renormalization group law or microscopic scale, does not prove a global covariant Weyl3 theorem, and does not authorize physical ghost, stability, hyperbolicity, unitarity, UV-completion, experimental-confirmation, or theory-established claims.
