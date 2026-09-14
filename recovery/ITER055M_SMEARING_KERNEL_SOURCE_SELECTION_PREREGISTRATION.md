# Iter055M preregistration — source selection of a covariant smearing/refinement kernel

Date: 2026-09-14
Gate: `ITER055M-SMEARING-KERNEL-SOURCE-SELECTION`

## Frozen question
Does existing QGR authority already select a concrete covariant Hilbert-dual smearing/refinement kernel family inside the Iter055L `SMEAR` class, with fixed shape/support/normalization/scale and refinement law, or is kernel/profile selection genuinely new candidate-defining input?

## Frozen authority set
Audit only existing source structures already present in QGR:

1. Iter007-G6C/G6E finite B3/B4 boundary geometry, boundary restriction and measure disintegration;
2. Iter007-G6F/G6G/G6H one-particle wavepacket/readout/broadband constructions;
3. compact-support perturbation/bump structures used in Iter053-series functional-variation tests;
4. local observable/preparation definitions in the one-particle/readout line;
5. existing refinement/coarse-graining kernel relations if any are explicitly source-defined.

Do not introduce a new Gaussian width, bump exponent, bandlimit, detector response, finite-element basis, cell average, sampling rule, Sobolev scale or physical cutoff.

## Frozen obligations
A source-selected kernel family must supply, from existing authority rather than convenience:

1. a concrete physical kernel/test-function family in the G6F Hilbert dual;
2. normalization and physical support/scale;
3. finite-frame covariance/transformation law;
4. metric-versus-connection observable relation if both B3 data types are claimed;
5. mapping from kernels to the shared B3 boundary structure;
6. refinement/coarse-graining compatibility fixing how fine kernels compose to coarse kernels;
7. a distinction between candidate-owned kernels and externally specified state preparation/detector/readout envelopes.

A shape used merely as a numerical test function or compact-support regulator is not candidate authority unless its physical role and parameters are fixed independently of that test.

## Frozen classifications
- `PASS_SCOPED_ITER055M_EXISTING_QGR_SOURCE_SELECTS_CANONICAL_COVARIANT_SMEARING_REFINEMENT_KERNEL_FAMILY` only if all frozen obligations are already source-defined with no tunable profile/scale.
- `BLOCKED_OBJECT_DEFINITION_ITER055M_SMEARING_KERNEL_PROFILE_AND_REFINEMENT_FAMILY_NOT_SOURCE_SELECTED` if the repository contains useful wavepackets/bumps/geometry but none is authorized as a unique physical bridge kernel with all required identities.
- `INVALID_PROVENANCE_ITER055M_KERNEL_SOURCE_AUDIT_INCONSISTENT` only if the fixed sources conflict on the identity of an allegedly canonical kernel.

## Interpretation ceiling
PASS would define only the sector bridge profile, not interacting dynamics. BLOCKED would establish that a concrete kernel/refinement family must be declared explicit new candidate input before exact one-particle-to-boundary intertwining and interacting dynamics tests can be operational. Neither outcome fixes beta, c6, Weyl3 treatment, regulator removal, full quantum unitarity, UV completion, GR recovery, experiment or theory establishment.

No GitHub Actions run is preregistered because this is a source-authority audit.
