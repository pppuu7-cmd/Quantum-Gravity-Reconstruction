# Iter055M terminal result — source selection of a covariant smearing/refinement kernel

Date: 2026-09-14
Preregistration: `29c13b57d5a9a44f974a5405d3a9dcdbfa2299c3`

## Terminal classification

`BLOCKED_OBJECT_DEFINITION_ITER055M_SMEARING_KERNEL_PROFILE_AND_REFINEMENT_FAMILY_NOT_SOURCE_SELECTED`

## 1. B3/B4 geometry fixes matching support, not a Hilbert-dual profile

G6C/G6E fix the shared B3 configuration variable, exact finite-cell variable intersection/fiber-product structure, positive boundary-measure disintegration, and the fact that quantum gluing must be organized over one shared physical boundary label. They do not supply a square-integrable kernel on the G6F future-null-cone Hilbert space, a physical smearing scale, or a map from the null-cone Hilbert dual to the B3 metric/connection variables.

The finite-sector dimensions used in the G6C algebraic witness are explicitly a matching surrogate; they are not a physical kernel construction.

## 2. G6G wavepacket profile is explicitly preparation/readout dependent

The G6G narrow-packet detector comparator states in its source docstring that it is a

`specified ... preparation/readout comparator, not a universal QGR number`.

Its output guard again says that the result remains preparation/readout dependent and that the absolute microscopic scale is not fixed. The normalized exponential envelope and fixed TT polarization therefore cannot be promoted to a candidate-owned boundary bridge kernel.

## 3. G6H validates multiple profiles rather than selecting one

G6H's broadband envelope validation checks at least the distinct benchmark radial profiles `m0` and `m1` and verifies the integration machinery against both. This is evidence that the observable machinery accepts a profile family; it is not source authority selecting one unique profile.

G6H also establishes useful scale-independence of certain overlap/Wigner data under overall null-energy rescaling, but that does not define the physical shape/support/refinement kernel needed for the Iter055L sector bridge.

## 4. Iter053 compact-support bump is a numerical/scientific-test perturbation, not a bridge law

The Iter053 compact-support action code freezes

`SUPPORT = 0.24`

and uses the one-dimensional bump

`b(s) = [1-(s/SUPPORT)^2]^4`

inside the support. These parameters are part of the prospectively fixed functional-variation test object. The code does not derive the exponent, support scale or tensor-product bump as a universal QGR readout/bridge kernel, and the object acts as a compact perturbation used to test integrated action variation.

Therefore the Iter053 bump cannot be recycled post hoc as the missing quantum sector bridge.

## 5. No refinement kernel family is source-defined

Existing refinement/gluing results constrain how already-defined geometric/configuration objects compose, but the audited authority does not give a concrete Hilbert-dual family `phi_cell` together with a law such as

`phi_coarse = sum_f M_cf phi_f`

with source-fixed coefficients/profile, normalization and physical scale.

Iter055L proves that such a relation is the correct class-level requirement once kernels exist; Iter055M finds that the actual kernels and coefficients are not presently selected.

## Scientific consequence

The current QGR source chain determines the **type** of mathematically admissible minimal bridge — bounded physical smearing on the established one-particle Hilbert space — but not a concrete member of that class.

The missing object is now localized to:

`candidate-owned covariant smearing profile + physical scale/support + B3 attachment + refinement law`.

Wavepacket envelopes may be externally specified preparations/readouts; compact-support bumps may be test functions; neither role makes them a universal candidate dynamics/bridge law.

Accordingly, a concrete kernel family must be declared explicit new candidate input or independently derived from an additional physical principle before exact Iter009-G6-to-boundary intertwining and interacting quantum dynamics selection become operational.

## Next highest-information gate

Before proposing a particular Gaussian/bump/cell-average, test whether a **universal nonzero Lorentz-covariant square-integrable kernel can exist without extra relational/frame/scale data**. If full finite-frame invariance itself forces any scalar kernel to be constant on the nonzero future null cone, the constant is non-normalizable and a concrete smearing profile necessarily has to be attached covariantly to additional physical data (boundary normal, detector/preparation, cell geometry/scale, etc.). This can be decided analytically before choosing a new candidate version.

## Claim ceiling

No concrete sector bridge, interacting boundary channel, dynamics axiom, beta/c6 fixing, Weyl3 treatment, regulator removal, full unitarity, UV completion, GR recovery, experiment or theory establishment follows. Theory established remains 0%.

No GitHub Actions run was needed: this is a source-authority audit.
