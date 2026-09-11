# QGR Iter006-G8A — normalized interacting history instrument

Date: 2026-09-11
Status: `PASS_SCOPED_EXACT_HISTORY_INSTRUMENT_NORMALIZATION_CONDITIONAL_ON_UNITARY_BRANCH_TRANSPORT`

## Question

Can the 24-history refinement be given an interacting quantum composition rule without introducing arbitrary history-dependent probabilities, phases, or normalization functions?

## Inputs already fixed by QGR

1. The `B4` refinement has exactly 24 symmetry-equivalent maximal ordering histories.
2. History normalization fixed the branch amplitude magnitude to `1/sqrt(24)`.
3. A finite configuration map `F_alpha` that is invertible and quasi-invariant induces a unitary Koopman/Radon-Nikodym operator `U_alpha` on the kinematic configuration Hilbert space.
4. QGR has a real local action through the verified quadratic+cubic+quartic orders, and its connection/transport data are generated from the same response/frame variables.

## Branch operators

For each history define

`K_alpha = 24^(-1/2) exp(i S_alpha / hbar) U_alpha`,

where `S_alpha` is the real QGR action evaluated on the corresponding branch/configuration history in the currently verified local truncation.

Multiplication by `exp(i S_alpha/hbar)` is unitary because `S_alpha` is real. Therefore

`K_alpha^dagger K_alpha = (1/24) I`.

Summing all 24 histories gives the exact completeness relation

`sum_alpha K_alpha^dagger K_alpha = I`.

No history-dependent modulus is available or required.

## History-register isometry

Define

`V psi = sum_alpha |alpha> tensor K_alpha psi`.

Then

`V^dagger V = I`.

Thus `V` is an exact isometry on the scoped Hilbert domain.

The history register retains relative action phases coherently. Interference is therefore available before the history label is discarded.

## Coarse channel

Tracing the history register gives

`E(rho)=sum_alpha K_alpha rho K_alpha^dagger`.

Because of the completeness relation, `E` is completely positive and trace preserving.

The branch **channel weight** is `1/24`, while the branch **amplitude magnitude** is `1/sqrt(24)`. The action contributes only a unit-modulus phase.

## Multi-level composition

If branch configuration maps compose and their Koopman lifts satisfy

`U_(beta o alpha)=U_beta U_alpha`,

then an `n`-level history has branch magnitude `24^(-n/2)`. There are `24^n` histories, so the completeness normalization remains exact at every finite level.

Action phases add under ordinary local action composition when the action is evaluated on the concatenated history; no extra normalization function is introduced.

## Constraint descent criterion

If a branch operator intertwines the QGR constraint equivalence relation,

`U_alpha R_g = R_(phi_alpha(g)) U_alpha`,

and the branch action is gauge invariant on the verified domain, then `K_alpha` maps equivalent kinematic states to equivalent states and descends to the corresponding physical quotient/rigging space.

This criterion is exact, but generic curved constraint descent has not yet been globally proved.

## Classification

`PASS_SCOPED_EXACT_NORMALIZED_INTERACTING_HISTORY_INSTRUMENT_WITH_NO_FREE_BRANCH_WEIGHTS`.

## Boundaries

This does not yet prove:

- a globally defined physical rigging space on arbitrary strong-curvature configurations;
- that every generic QGR branch map is invertible/quasi-invariant;
- all-orders gauge invariance of an exact interacting QGR action;
- finiteness of a sum over multiple strong-curvature torsion-free connection branches;
- a continuum/RG theorem or normalized phenomenological observable.

The result is an exact finite-level normalization theorem for the currently reconstructed history instrument, not an all-orders quantum-gravity completion.
