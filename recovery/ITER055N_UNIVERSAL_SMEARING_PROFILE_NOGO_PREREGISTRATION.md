# Iter055N preregistration — universal square-integrable smearing profile no-go

Date: 2026-09-14
Gate: `ITER055N-UNIVERSAL-L2-SMEARING-PROFILE-NOGO`

## Frozen question
Can QGR choose a nonzero square-integrable scalar smearing envelope on the nonzero future null cone that is universal under the full finite-frame/Lorentz action, without attaching the profile to additional relational/frame/scale data?

## Frozen object
A scalar envelope `phi(k)` in the Hilbert dual of the G6F one-particle characteristic space, with `k` on the nonzero future null cone and the existing invariant null-cone measure.

The tested universality requirement is strict:

`phi(Lambda k)=phi(k)` almost everywhere for every proper orthochronous finite-frame/Lorentz transformation `Lambda` in the already-used QGR frame action.

No boundary normal, detector four-velocity, source momentum, cell scale, timelike clock, cutoff or profile parameter may be supplied in this gate.

## Frozen obligations
1. Determine the Lorentz orbits on the nonzero future null cone, including whether boosts along a null direction rescale its energy.
2. Deduce the form of any measurable scalar profile invariant on the full orbit.
3. Check square-integrability with the actual G6F null-cone measure.
4. Distinguish invariant fixed profile from a **covariant family** `phi_q(k)` attached to extra physical data `q`; the latter is not ruled out but is not universal source-free input.
5. Do not infer a no-go for polarization/tensor kernels or relationally anchored profiles beyond the frozen scalar universality claim.

## Frozen classifications
- `PASS_SCOPED_ITER055N_NONZERO_UNIVERSAL_L2_SMEARING_PROFILE_EXISTS_WITHOUT_EXTRA_RELATIONAL_DATA` only if a nonzero square-integrable invariant scalar envelope exists on the full nonzero future cone.
- `FAIL_SCOPED_ITER055N_NO_NONZERO_UNIVERSAL_L2_SMEARING_PROFILE__RELATIONAL_PROFILE_DATA_REQUIRED` if Lorentz transitivity forces an invariant scalar profile to be constant almost everywhere and the invariant measure makes every nonzero constant non-square-integrable.
- `INVALID_PROVENANCE_ITER055N_FRAME_ACTION_OR_MEASURE_NOT_FIXED` only if the existing source does not determine the Lorentz action or null-cone measure needed for the proof.

## Interpretation ceiling
A FAIL would show only that a concrete bridge profile must be relationally anchored/covariant rather than a universal fixed scalar envelope. It would not select the relational anchor, kernel, dynamics, beta, c6, Weyl3 treatment, regulator removal, unitarity, UV completion, GR recovery or experiment.

No GitHub Actions run is preregistered; this is an exact representation/measure-theory gate.
