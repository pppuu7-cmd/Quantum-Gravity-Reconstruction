# Iter057J superseding component-coefficient correction audit

Date: 2026-09-15
Original Iter057J preregistration: `0f4d3cf9e1482029382dd158aa8feef89a8d736a`
Original exact derivation: `02b842b784023307fd64616f3594afae9824ed35`
Original terminal result: `3b70ce21c9406f13c07631b763ad908f65f4499c`
Independent exact source-component equivalence result: `688994108d3b28d9cdf7d7926236bece78222a94`
Actions run: `34954206549`

## Correction status

This note **supersedes the numerical coefficient of the Iter057J witness only**. It does not erase or rewrite the historical derivation/result commits and does not change the preregistered scientific classification.

The original record used a double-divergence component table with the opposite overall sign for

`D^{ab}=nabla_mu nabla_nu P^{mu(ab)nu}`.

Two independent exact implementations now agree on the corrected values in the frozen `(-,+,+,+)` G3/H0 presentation:

`I3(0)/kappa^3 = 96`,

`D^{ii}(0)/kappa^3 = (-12,92,92,-196)`,

`P.R insertion^{ii}(0)/kappa^3 = (-72,72,72,72)`,

`E_W3,ii(0)/kappa^3 = (48,-208,-208,368)`.

The comparison is exact: all candidate/reference equality checks passed in Actions run `34954206549`, artifact `10390318470`, digest `sha256:ab331b2093e7d26e1d5f609f08e81c70739bb79d88a9a210a73ffc5b8155cd92`.

## Corrected Iter057J witness

With the finite nonzero Einstein normalization factored out,

`Hbar_ab := A_E H_ab = (1/2) E_W3_ab - (1/6) g_ab E_W3`.

At the frozen origin the corrected exact source gives

`E_W3 = g^{ab}E_W3_ab = -96 kappa^3`,

and therefore

`Hbar_00 = (1/2)(48 kappa^3) - (1/6)(-1)(-96 kappa^3)`

`          = 8 kappa^3`.

For the preregistered counterexample-first component `(e,c,a,b)=(0,0,1,1)`, staticity and the origin connection structure still give exactly

`[nabla_0 nabla_0 Hbar_11]_0=0`,

`[nabla_0 nabla_1 Hbar_01]_0=0`.

The source curvature convention gives

`R_011{}^0(0)=kappa`.

Hence the corrected obstruction is

**`Kbar_0011 = -R_011{}^0 Hbar_00 = -8 kappa^4`.**

At the frozen production value `kappa=2/25`,

**`Kbar_0011 = -128/390625 != 0`.**

Thus the original coefficient `16 kappa^4` / `256/390625` is superseded by `-8 kappa^4` / `-128/390625`.

## Scientific classification

The Iter057J prospective decision rule required only one exact nonzero component to reject the conformal continuation candidate. The corrected component is still exactly nonzero for every `kappa != 0`.

Therefore the terminal classification remains unchanged:

**`SCIENTIFIC_FAIL_ITER057J_CONFORMAL_OPEN_NEIGHBORHOOD_CONTINUATION_FIRST_PROLONGATION_OBSTRUCTED`**.

Only the witness coefficient is corrected. The scope remains conformal continuation only; the later Iter057L and Iter057M results independently demonstrate unrestricted nonconformal local-jet continuation through the first two even source orders.

## Claim locks

No inference about physical characteristics, hyperbolicity, ghosts, stability, unitarity, regulator removal, UV completion, experiment, or QGR correctness follows from this correction. `c6` remains symbolic/unfixed; `beta=1` remains unauthorized; theory established remains `0%`.