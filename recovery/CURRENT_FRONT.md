# QGR Current Research Front

Updated: 2026-09-14
Primary active front: `POST-ITER054Z / G3-TO-G8A PHASE-FREE CHANNEL OBJECT BRIDGE`
Project phase: `MODEL_CONSTRUCTION / QUANTUM AMPLITUDE-MEASURE SOURCE REALIZATION`

## Canonical claim locks

- Repository infrastructure readiness: **100%**.
- Candidate-program roadmap readiness: **99% internal bookkeeping only**, not probability of correctness.
- Theory established: **0%**.
- `beta=1`: not authorized.
- `c6`: symbolic/unfixed.
- Full covariant Weyl3 metric EOM as a global theorem: **not established**.
- Strong hyperbolicity / Weyl3 well-posedness: **not established**.
- Physical exact-vs-order-reduced Weyl3 treatment selector: **absent**.
- Global interacting measure/regulator removal: **not established**.
- No physical ghost/spectrum, unitarity, UV completion, full GR recovery, experimental confirmation or new-physics claim.

GitHub main + terminal Actions/results are authoritative. Historical FAIL/INVALID/BLOCKED results remain immutable.

## Recovered auto-research chain

The substantive auto-research/action chain through Iter054Z and the historical G25-G38/G31-G37 programmes has been re-read against preregistrations, implementations, terminal results and Actions rather than commit titles alone.

Important durable facts:

- exact lower-order/two-derivative QGR action exists and has scoped Noether closure;
- exact higher-derivative finite-cell Weyl3 microscopic action is not defined by current authority;
- G25-G28: specified sources can be converted to lower-order on-shell phases; primitive composition fixes `J(n)=beta*n`, but `beta` is not fixed; exact beta-free phase ratios exist only in their common-conformal count sector and are not mapped to the 24 G3/B4 ordering histories;
- G31-G32: local curvature lift and conditional projective-limit action integration exist, but absolute phase normalization remains open;
- G33-G37/G37C: finite algebraic branch structure is nontrivial, but no physical extra same-realization branch was authorized from the strongest distant roots;
- Iter054S: source-ordered fine-to-coarse transport blocking on the Weyl-active G3 realization is a scoped finite-panel PASS;
- Iter054T/U/W/X/Y: source/history action realization is missing at both lower-order and Weyl3 levels, while the lower-order action itself is genuine;
- Iter054V: order-blind event-attached additive action cannot distinguish the 24 permutations;
- Iter054Z: the operational role of unresolved branch phases has now been split exactly between the coarse CP channel and the fine history-register dilation.

## Iter054Z — terminal operational phase-semantics BLOCKED

Preregistration `9c78ba250c97e2853c731d26faa07b4f054639a1`.
Durable result `e239959034118fe7002120ae988455443166760f`.

Classification:

`BLOCKED_OBJECT_DEFINITION_ITER054Z_G8A_HISTORY_COHERENCE_SEMANTICS_NOT_FIXED`.

Exact subresults:

1. For arbitrary independent branch phases `theta_alpha`,
   `K'_alpha=e^{i theta_alpha}K_alpha` gives exactly
   `K'_alpha rho K'_alpha^dagger=K_alpha rho K_alpha^dagger`.
   Therefore all branch CP maps and the history-forgotten CPTP channel
   `E(rho)=sum_alpha K_alpha rho K_alpha^dagger`
   are phase insensitive.
2. The fine isometry transforms as
   `V'=(D_theta tensor I)V`, where `D_theta` is diagonal on the history register. Thus mere presence of coherent amplitudes in an auxiliary history basis does not by itself fix a physical relative-phase reference.
3. G8A states that coherent interference is available before the history label is discarded, but the audited G8A-G8D/G5A/G6C/G6D chain does not define a fixed noncommuting history-register mixer/readout/decoherence functional whose convention is independent of the Kraus representation.
4. G8D identifies the operational physical coarse evolution after history discard as the CPTP channel. G5A channel/purity and G6D branch-overlap purity are invariant under independent branch rephasings.

Durable interpretation:

- unresolved `S_alpha` is **not an upstream blocker for the already-defined coarse CPTP channel**;
- unresolved `S_alpha` remains open for a future/current fine coherent-history observable only if QGR supplies a canonical phase reference/mixer;
- do not rewrite G25-G32 or Iter054T-Y; they remain valid source/action results, but their operational necessity is now scope-dependent.

## Object-identity warning for the next gate

Do not feed Iter054S 4x4 geometric/path transport matrices directly into the G8A Kraus formula as if they were already Hilbert-space unitary operators.

Iter054S computes ordered products of Lorentz/metric-compatible 4x4 finite transports on the G3 Weyl-active tidal realization. G8A, by contrast, assumes a branch **finite configuration map** whose Koopman/Radon-Nikodym implementation is unitary on the kinematic configuration Hilbert space.

A source-faithful phase-free coarse-channel test therefore requires a bridge:

`G3 geometric/history transport data -> complete invertible configuration map F_alpha -> quasi-invariant configuration measure -> unitary U_alpha -> G8A CP map`.

Until this bridge is established, a channel computation using the 4x4 classical matrices themselves would be a wrong-object surrogate.

## Current highest-information question

Prospectively audit whether pre-existing QGR authority already closes the object bridge above in the **same Weyl-active G3/B4 realization**.

If the bridge exists, the next admissible scientific gate is direct phase-free cylindrical/refinement consistency of the coarse CPTP channel using Iter054S blocking.

If the bridge is absent, terminalize the exact missing object and do not manufacture a finite-dimensional Kraus channel from classical transport matrices.

This channel-object bridge is now higher priority than further action-phase normalization work for the coarse operational layer.
