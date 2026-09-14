# Iter054I Preregistration — Regulator-Limit Asymptotic Weyl3 Separation

Date: 2026-09-14
Gate: `ITER054I-WEYL3-REGULATOR-LIMIT-ASYMPTOTIC-SEPARATION`

## Frozen question

Assuming only the already-authorized removable-regulator interpretation of `h`, does the Weyl3 principal correction decouple uniformly on fixed compact physical-frequency/curvature sets as `h -> 0`, while the singular higher-derivative proxy branch is driven to infinite physical frequency? Where does this asymptotic statement fail to be uniform when physical frequencies scale with inverse powers of `h`?

## Frozen assumptions

- `c6` remains symbolic, finite, h-independent and unfixed.
- Positive-sector background curvature obeys `0 < |Cbar| <= Cmax` with `Cmax` fixed independently of h.
- Positive compact physical-frequency band obeys `|k| <= K` with `K` fixed independently of h.
- `chi = |c6| h^2 |Cbar|`, `q=|k|h`.
- Frozen unit-channel proxy: `rho = chi q^2 = |c6 Cbar| h^4 k^2` and `q_HD=chi^-1/2`.
- Therefore `k_HD=q_HD/h = 1/(h^2 sqrt(|c6 Cbar|))` for `Cbar != 0`.
- Weyl-flat `Cbar=0` is a separate exact-zero sector; no division by zero is permitted.

## Frozen lanes

### A0 — symbolic asymptotics
Must verify exactly:
- `rho = |c6 Cbar| h^4 k^2`;
- on fixed `K,Cmax`, `sup rho <= |c6| Cmax K^2 h^4 -> 0`;
- `k_HD ~ h^-2` and diverges for finite nonzero `|c6 Cbar|`;
- `k_HD/K -> infinity` for fixed K.

### A1 — rational convergence panel
Use fixed positive rational values of `|c6 Cbar|` and K with decreasing rational h. Require monotone decrease of worst-band rho proportional to h^4 and monotone increase of k_HD proportional to h^-2. Include exact ratio checks under `h -> h/2`: rho factor `1/16`, k_HD factor `4`.

### B0 — nonuniform inverse-h frequency controls
Take `k(h)=h^-p` with frozen `p` panel `{0,1,3/2,2,5/2}`. Since `rho ~ h^(4-2p)` require:
- p<2: rho -> 0;
- p=2: rho -> finite nonzero constant for nonzero coefficient;
- p>2: rho diverges.
This lane is mandatory and prevents overclaiming uniform decoupling over unbounded physical-frequency families.

### B1 — authority/anti-overclaim controls
Must preserve:
- no finite-h physical cutoff derived;
- no finite-h physical order-reduced treatment authorized;
- no c6 fixing;
- no beta=1 authorization;
- no ghost/unitarity/hyperbolicity claim;
- no quantum amplitude/measure transition;
- Iter007 no-derived-stop-scale result remains compatible.

## Frozen aggregate classification

PASS only if all lanes are valid/pass, with exact classification:

`PASS_SCOPED_ITER054I_FIXED_BAND_REGULATOR_LIMIT_WEYL3_ASYMPTOTIC_DECOUPLING__FINITE_H_PHYSICAL_TREATMENT_NOT_AUTHORIZED`

Otherwise fail closed with the lane evidence preserved.

## Interpretation lock

A PASS is an asymptotic continuum statement only. It does not create a physical discretization scale, resolved physical band, all-orders remainder theorem, finite-h treatment selector, strong-hyperbolicity theorem, ghost classification, unitarity result, UV completion, experimental confirmation or theory establishment.
