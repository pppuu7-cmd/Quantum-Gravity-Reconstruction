# COVARIANT_WEYL3_A7_CONNECTION_TENSOR_COMPONENT_LOCALIZATION — prospective preregistration

Date: 2026-09-19
Status: **FROZEN BEFORE COMPONENT SERIALIZATION / NO REPAIR AUTHORIZED**

## Parent authorities

1. Fi-jet source localization:
   - result commit `07ad77de0506a3de5e7db601e2cfc8b5edc37c5c`;
   - first source divergence `CONNECTION_JET` at `(i,j)=(0,0)`.

2. Two-identity adjudication:
   - result commit `267743ee78ea0ebd51fd697003cc1207a9d9032b`;
   - classification `CONNECTION_IDENTITY_DERIVATIONS_DISAGREE`;
   - Lane A and Lane B scalar contractions are exact sign opposites.

3. Neutral polynomial adjudication:
   - result commit `d44e785efb222c857bfece31a3a09bed447999fe`;
   - classification `DUAL_POLYNOMIAL_EXTRACTION_MATCHES_NEITHER`;
   - neutral tensor SHA256 `e3797c7dade7f4de601ba047be48b0ed73278333e01719e3b0d97588e783deb8`.

Frozen witness remains `OFFSHELL_A/d=7/(i,j)=(0,0)`.

## Scientific question

At which first exact four-index component do the three already frozen connection constructions disagree, and are any two complete tensors exactly equal or exact negatives?

This gate does not introduce a new connection formula. It materializes the full 256-component tensors from the already frozen constructions for causal comparison.

## Three target-blind lanes

### Lane A
Reproduce the already frozen tensor-Hessian connection construction from preregistration `d76dea1...` and serialize all 256 exact components.

### Lane B
Reproduce the already frozen direct hand-expanded GammaGamma connection construction from preregistration `d76dea1...` and serialize all 256 exact components.

### Lane C
Reproduce the already frozen direct bivariate dual-polynomial extraction from preregistration `ed829c5...` and serialize all 256 extracted `[eps*x]` components.

Each lane must:
- use exact rational arithmetic;
- retain the same point P only for scalar control, not to define tensor components;
- serialize/hash before any cross-lane comparison;
- not import either other lane's implementation helper.

## Frozen component order

Serialize and compare in exact lexicographic order:

`(a,b,c,d)`, with each index ranging `0,1,2,3` and `d` varying fastest.

The comparator must record the first index slot where the three values are not all equal.

## Frozen pairwise relations

The comparator must additionally determine over all 256 components:

- `A_EQ_B`
- `A_EQ_C`
- `B_EQ_C`
- `A_EQ_NEG_B`
- `A_EQ_NEG_C`
- `B_EQ_NEG_C`

using exact componentwise equality only.

It must also reproduce each parent scalar contraction with the frozen P object as a control.

## Frozen terminal taxonomy

- `CONNECTION_TENSOR_ALL_THREE_EXACT_MATCH`
- `CONNECTION_TENSOR_COMPONENT_DIVERGENCE_LOCALIZED`
- `BLOCKED_EXECUTION_OR_PROVENANCE`

No additional scientific label is authorized after result inspection.

## Claim ceiling

A tensor-component localization does not itself decide which formula is correct and does not authorize repair. Any correction or convention change requires a separate prospective gate.

`c6=SYMBOLIC_UNFIXED`.
Corrected Q10 remains LOCKED.
`theory_established=0%`.
