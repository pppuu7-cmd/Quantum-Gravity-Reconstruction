# QGR Iter006-G3B — controlled quantum transport on configuration space

Date: 2026-09-11
Status: `PASS_SCOPED_KINEMATIC_LINEAR_QUANTUM_TRANSPORT_ARCHITECTURE / PHYSICAL_QUOTIENT_OPEN`

## Problem

G3A derives a classical branch transport from `G` and its compatible connection, but the resulting transport is configuration dependent. A naive expression `U_alpha[G]` inserted directly as a state-dependent Kraus operator would risk nonlinear quantum evolution.

## Resolution — transport the configuration, not the quantum state nonlinearly

Let the full fine QGR configuration be denoted `bold G`, living on a configuration space `X` with the kinematic measure induced from the local Lorentzian response measure.

For each refinement history `alpha`, the QGR connection/composition rule defines a deterministic configuration map

`F_alpha : X -> X`.

The map may be nonlinear in `G`; that is not a problem. If `F_alpha` is invertible and quasi-invariant with respect to the kinematic measure `mu`, it induces the standard linear Koopman/Radon-Nikodym unitary

`(U_alpha psi)(G) = [ d(F_alpha* mu)/dmu (G) ]^(1/2) psi(F_alpha^(-1)(G))`

with the equivalent convention obtained by exchanging pushforward/pullback derivatives.

The Radon-Nikodym factor is determined by `F_alpha` and `mu`; it is not an independent history coupling.

## Exact linearity and unitarity

The map `psi -> U_alpha psi` is linear even though `F_alpha` is a nonlinear function of the classical configuration.

By change of variables,

`<U_alpha psi, U_alpha phi> = <psi,phi>`.

Thus the configuration dependence of the classical transport does not imply state-dependent nonlinear quantum mechanics.

## Composition

If histories concatenate according to the already derived classical transport rule

`F_(alpha,beta) = F_beta o F_alpha`,

then Radon-Nikodym derivatives satisfy the chain rule and the induced quantum maps satisfy

`U_(alpha,beta) = U_beta U_alpha`

(up to the fixed pullback convention).

Therefore the history-register isometry

`V psi = 24^(-1/2) sum_alpha |alpha> tensor U_alpha psi`

is exactly normalized whenever each branch map is a unitary of this form.

At two refinement levels, the combined isometry contains `24^2` branches with amplitude magnitude `24^-1`, and tracing history labels produces the same channel as composing the two one-level coarse channels.

## Coarse observable algebra

For observables that do not resolve the internal history label, the reduced channel is

`E(rho) = (1/24) sum_alpha U_alpha rho U_alpha^dagger`.

This is CPTP by construction. It gives a derived marginal rule for all observables, including second moments, rather than choosing separately between `mean of second moments` and `second moment of the mean`.

History-sensitive observables may instead be retained on the enlarged Hilbert space; the architecture does not force premature decoherence.

## Physical-constraint boundary

This result is kinematic. To descend to the physical QGR state space, each `F_alpha` must map QGR constraint/gauge orbits to constraint/gauge orbits. The compatible connection is covariant under the previously derived pullback law, so equivariance is a natural candidate, but a discrete all-configuration proof is still required.

Also still required:

- an explicit finite-complex definition of `F_alpha` beyond the frozen-background/infinitesimal transport;
- proof of invertibility or at least a well-defined isometric quantum instrument on the relevant domain;
- proof of quasi-invariance / control of the Radon-Nikodym factor for the actual QGR fine measure;
- preservation of the physical two-mode constraint quotient;
- a finite amplitude/measure definition, not merely a kinematic Hilbert measure.

Classification:

`PASS_SCOPED_CONFIGURATION_DEPENDENT_HISTORY_TRANSPORT_CAN_BE_QUANTIZED_LINEarly_BY_KOOPMAN_RADON_NIKODYM_LIFT_WITH_EXACT_PROJECTIVE_COMPOSITION__PHYSICAL_QGR_DESCENT_OPEN`.

## Exact next gate

`QGR-ITER006-G4-DISCRETE_CONNECTION_MAP_AND_CONSTRAINT_EQUIVARIANCE`

Construct the actual finite-cell map `F_alpha` from QGR first-neighbor data and prove or refute:

1. finite map existence without arbitrary interpolation;
2. gauge/constraint equivariance;
3. quasi-invariance of the candidate measure;
4. preservation of the two-mode physical sector;
5. two-level projective consistency on a nontrivial curved toy configuration.
