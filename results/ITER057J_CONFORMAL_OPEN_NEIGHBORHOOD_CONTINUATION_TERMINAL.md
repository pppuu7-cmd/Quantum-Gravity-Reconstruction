# Iter057J terminal result — conformal open-neighborhood continuation obstruction

Date: 2026-09-15
Gate: `ITER057J-OPEN-NEIGHBORHOOD-FIRST-ORDER-BACKGROUND-CONTINUATION`
Preregistration: `0f4d3cf9e1482029382dd158aa8feef89a8d736a`
Reduction: `5e1775dd83da8b952ea0463bfef946eb7692f632`
Exact derivation: `02b842b784023307fd64616f3594afae9824ed35`

## Terminal classification

**`SCIENTIFIC_FAIL_ITER057J_CONFORMAL_OPEN_NEIGHBORHOOD_CONTINUATION_FIRST_PROLONGATION_OBSTRUCTED`**

The preregistered first nontrivial Hessian-prolongation tensor is

`K_ecab=[nabla_e nabla_c H_ab-nabla_e nabla_a H_cb]_0-R_ca b{}^d(0)H_ed(0)`.

With the finite nonzero Einstein normalization factored out, `Kbar=A_E K`, the exact source-owned G3/H0 evaluation gives the counterexample-first component

**`Kbar_0011 = 16 kappa^4`.**

Therefore for every nonzero G3 source amplitude `kappa`, the required condition `K_ecab=0` fails exactly. At the frozen production value `kappa=2/25`,

**`Kbar_0011 = 256/390625 != 0`.**

This is sufficient under the prospective Iter057J decision rule; no empirical tolerance is involved.

## Independent controls

The exact symbolic evaluation also reproduces:

- `I3(0)=-96 kappa^3` in the source `(+---)` convention;
- `P.R=3 I3`;
- `g_ab E_W3^{ab}=-I3` through the quadratic source jet required by the prolongation;
- `Hbar_ab(0)=kappa^3 diag(-16,96,96,-192)`;
- 24 nonzero ordered components of `Kbar`, all proportional to `kappa^4`;
- the same `Kbar` tensor after global conversion to the `(-,+,+,+)` convention used by the Iter057F production implementation.

The simplest component is especially robust because its differentiated-H terms vanish exactly by staticity and the frozen-origin connection structure:

`Kbar_0011=-R_011{}^0 Hbar_00=-(kappa)(-16 kappa^3)=16 kappa^4`.

## Auto-work / provenance audit

Before terminalization, repository automation was checked for competing work. No commit newer than the synchronized Iter057J front and no GitHub Actions run after that synchronization existed before this derivation was written. Historical Iter057F3 automation was separately re-audited: its authoritative run `34907701856` contains cache-equivalence, ten independent basis lanes, and an aggregate job, with the lane and summary artifacts still present and unexpired. That prior PASS is used only as validated operator provenance; it is not substituted for the new exact Iter057J obstruction.

No new numerical production run is required for this terminal decision because the preregistered criterion is exact and an exact symbolic nonzero component has been obtained. A numerical finite-difference diagnostic was attempted after the symbolic target was fixed but exceeded the local execution limit and is not used as evidence.

## Scientific scope

This FAIL rejects only the **specific Iter057I conformal Hessian continuation** as an open-neighborhood first-order correction on the frozen G3/H0 source.

It does **not** establish that:

- no nonconformal first-order correction exists;
- no Weyl-active on-shell Einstein+Weyl3 background exists;
- Einstein+Weyl3 dynamics is inconsistent;
- physical characteristics, hyperbolicity, ghosts, stability, unitarity, regulator removal, or UV completion have been determined.

The next scientifically meaningful branch is therefore a prospectively preregistered **nonconformal first-order background correction / local on-shell construction** (or another independently justified on-shell background), rather than a higher prolongation of the now-rejected conformal candidate.

`c6` remains symbolic/unfixed; `beta=1` remains unauthorized; theory established remains `0%`; there is no experimental confirmation.