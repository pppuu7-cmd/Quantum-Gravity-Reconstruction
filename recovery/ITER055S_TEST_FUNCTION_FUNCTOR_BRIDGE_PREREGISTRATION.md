# Iter055S preregistration — test-function/readout functor versus candidate-owned smearing profile

Date: 2026-09-14
Gate: `ITER055S-TEST-FUNCTION-FUNCTOR-BRIDGE`

## Frozen question
Do Iter055M/R overstate the need for QGR itself to select one smearing profile? Can the established G6F linearized one-particle sector instead support a covariant **family for all admissible external test/readout functions**, with profile choice belonging to observable/preparation data, while leaving only the map to the finite B3 configuration sector as candidate-owned missing structure?

## Frozen authority
- G6F characteristic one-particle Hilbert/pairing and finite-frame action;
- G6G/G6H explicit preparation/readout dependence;
- G6C/G6E finite shared-B3 configuration/cylindrical observable structure;
- Iter055J–R results, without rewriting them.

## Frozen candidate mathematical map under audit
For a smooth compactly supported spacetime test tensor `F_ab(x)` (or a sufficiently regular Schwartz-class probe), take its Fourier transform, restrict to the future characteristic null cone, and descend/project to the physical G6F quotient fiber. Denote the resulting Hilbert-dual section `phi_F(k)`. The associated one-particle observable is the bounded pairing

`B_F[a] = <phi_F, a>_Hchar`

whenever `phi_F in H_char`.

This is tested as an observable/readout **functorial class**, not as a unique QGR kernel.

## Frozen obligations
1. Determine whether compactly supported smooth / Schwartz test tensors yield square-integrable restricted kernels on the G6F future-null-cone measure after physical quotient projection.
2. Check finite-frame covariance when test tensor and state transform together.
3. Check consistency with G6G/G6H source statements that preparation/readout profiles are externally specified and not universal QGR numbers.
4. Determine whether this removes radial-profile nonuniqueness as a candidate-parameter problem, or merely reclassifies it as observable choice.
5. Separately test whether the test-function functor supplies an explicit map to the **finite shared-B3 configuration label/fibers** of G6C/G6E. A collar-localized spacetime probe is not automatically the exact finite B3 restriction map.
6. Do not claim a full interacting boundary bridge or channel from the linearized observable functor.

## Frozen classifications
- `PASS_SCOPED_ITER055S_TEST_FUNCTION_FUNCTOR_MAKES_PROFILE_CHOICE_OBSERVABLE_DATA__FINITE_B3_SECTOR_ATTACHMENT_STILL_BLOCKED` if the one-particle test-function map is bounded/covariant for a broad source-compatible probe class and profile nonuniqueness is correctly interpreted as observable choice, but no exact finite-B3 sector attachment follows.
- `PASS_SCOPED_ITER055S_TEST_FUNCTION_FUNCTOR_ALSO_SUPPLIES_SOURCE_DEFINED_FINITE_B3_ATTACHMENT` only if current authority additionally gives the exact attachment/intertwiner to the G6C/G6E boundary sector.
- `FAIL_SCOPED_ITER055S_SOURCE_ONE_PARTICLE_SECTOR_DOES_NOT_SUPPORT_COVARIANT_TEST_FUNCTION_FUNCTOR` if the proposed broad test class fails Hilbert-dual boundedness/covariance.
- `INVALID_PROVENANCE_ITER055S_LINEARIZED_PAIRING_OR_BOUNDARY_OBJECT_UNRESOLVED` only if the source identities cannot be fixed.

## Interpretation ceiling
A scoped PASS may remove “choose one universal profile” from the candidate-dynamics obligations and retain profiles as external observable/preparation data. It cannot by itself identify the finite B3 quantum sector, define interacting boundary dynamics, calibrate h, fix beta/c6/Weyl3 treatment, prove regulator removal/unitarity/UV/GR recovery, or establish experiment/theory.

No GitHub Actions run is preregistered; this is a functional/source audit.
