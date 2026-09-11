# QGR Iter006-G8D — operational physical positivity and CPTP coarse descent

Date: 2026-09-11
Status: `PASS_SCOPED_OPERATIONAL_POSITIVITY_AND_NORMALIZED_PHYSICAL_CHANNEL`

## Question

BRST cohomology supplies the generic algebraic constraint quotient, but a positive-definite BRST Hilbert inner product has not been constructed. Can QGR nevertheless define positive normalized physical states and coarse evolution without adding a new probabilistic structure?

## Physical observable algebra

Let

`A_phys = H^0(s)`

be the ghost-number-zero BRST cohomology represented by gauge-invariant observables on the positive kinematic configuration Hilbert space.

For operational purposes, use the represented `*`-algebra of bounded physical observables (or a suitable common dense observable domain when unbounded operators are required).

## Physical states as positive functionals

Define a physical state to be a positive normalized linear functional

`omega:A_phys -> C`

such that

`omega(O^dagger O) >= 0`,

`omega(1)=1`.

Any positive normalized kinematic density operator `rho` induces such a state by restriction:

`omega_rho(O)=Tr(rho O)`, `O in A_phys`.

If `rho' = U_g rho U_g^dagger` is gauge related to `rho` and `O` is physical/invariant, then cyclicity gives

`omega_(rho')(O)=omega_rho(O)`.

Thus the operational physical state depends only on the gauge-equivalence class as tested by physical observables.

This supplies positivity without requiring a normalized average over the noncompact gauge group and without requiring a positive-definite ghost-extended inner product.

## Coherent versus coarse evolution

Before discarding the history register, the 24-history map is an isometry

`V^dagger V=I`.

After tracing the history register, the evolution is the CPTP map

`E(rho)=sum_alpha K_alpha rho K_alpha^dagger`,

with

`sum_alpha K_alpha^dagger K_alpha=I`.

Its dual map is

`E*(O)=sum_alpha K_alpha^dagger O K_alpha`.

The dual is completely positive and unital:

`E*(1)=1`.

If the branch operators intertwine the BRST/gauge action, `E*` maps `A_phys` into itself.

Therefore the induced physical-state evolution

`omega' = omega o E*`

remains positive and normalized:

`omega'(O^dagger O)>=0`,

`omega'(1)=1`.

## Replacement principle

QGR therefore has the following scoped quantum-consistency principle:

- **coherent fine description:** isometric history-register evolution;
- **physical coarse description after history information is discarded:** completely positive trace-preserving evolution on states / unital completely positive evolution on observables;
- **physical positivity:** positivity of normalized functionals on the BRST-invariant observable algebra.

This is an operational replacement for demanding a globally positive BRST-vector inner product at the present stage.

## Classification

`PASS_SCOPED_OPERATIONAL_POSITIVE_PHYSICAL_STATE_SPACE_AND_CPTP_PROJECTIVE_COARSE_EVOLUTION`.

## Boundary

This result does not prove:

- that the full strong-curvature torsion solution set always yields a finite normalized branch instrument;
- all-orders interacting gauge invariance beyond the verified local action order;
- existence of every desired unbounded observable on a common self-adjoint domain;
- continuum/RG convergence;
- a normalized phenomenological observable/comparator.

The dominant remaining Iter006 blocker is global strong-curvature branch finiteness/singular-stratum control, not local positivity.
