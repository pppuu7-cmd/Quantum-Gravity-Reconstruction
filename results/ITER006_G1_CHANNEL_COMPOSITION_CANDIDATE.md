# QGR Iter006-G1 — history-isometry / CP-channel composition candidate

Date: 2026-09-11
Status: `PASS_SCOPED_CHANNEL_LEVEL_NORMALIZATION_AND_ASSOCIATIVITY`

## Problem

Iter005-G4 showed that generic coarse second moments depend on whether one marginalizes fine realizations or first composes their rank-1 frames. QGR therefore needs a primitive composition object that decides what information is retained at coarse scale.

## Algebraic candidate

For `N=24` symmetry-related refinement histories, introduce an orthogonal history register and a candidate physical projector `P=P^dagger=P^2`.

Take equal branch Kraus operators

`K_alpha = a P`.

The Stinespring isometry is

`V = sum_alpha |alpha> tensor K_alpha`.

Requiring isometry on the physical `P` subspace gives

`V^dagger V = sum_alpha K_alpha^dagger K_alpha = N |a|^2 P = P`,

therefore

`|a|=1/sqrt(N)=1/sqrt(24)`.

Tracing the history register gives

`E(rho)=sum_alpha K_alpha rho K_alpha^dagger = P rho P`.

Each history contributes weight `|a|^2=1/24` at the coarse channel level.

## Multi-level composition

At `n` identical refinement levels:

- number of fine histories: `24^n`;
- magnitude of each branch Kraus amplitude: `24^(-n/2)`;
- each branch channel weight: `24^-n`;
- total Kraus normalization: `24^n * 24^-n P = P`;
- because `P^2=P`, the idealized coarse channel remains `rho -> P rho P`.

Thus normalization and associativity reproduce the old factorial coarse weight without declaring `1/24` itself to be a quantum amplitude.

## Coherence versus marginalization

Before tracing the history register, `V|psi>` is a coherent state over history labels. After tracing, histories form a CP mixture. Hence the framework can represent both coherent fine histories and projective coarse marginals in one object.

The coarse second-moment map becomes a mixture only for observables in the coarse algebra that do not act on the discarded history register. This makes the mixture-vs-coherent question an observable-algebra question rather than an arbitrary numerical prescription.

## Remaining blocker

The early CCRC projector was only a finite toy label-space object. QGR has not yet constructed the physical state space and physical projector corresponding to QGR-L1.

Therefore this result establishes only the algebraic architecture of a possible quantum refinement channel.

Classification:

`PASS_SCOPED_HISTORY_ISOMETRY_EXPLAINS_1_OVER_24_COARSE_WEIGHT_AND_MULTI_LEVEL_NORMALIZATION__PHYSICAL_STATE_SPACE_OPEN`.

## Reproducibility

`code/qgr_iter006_g1_channel_composition.py`
