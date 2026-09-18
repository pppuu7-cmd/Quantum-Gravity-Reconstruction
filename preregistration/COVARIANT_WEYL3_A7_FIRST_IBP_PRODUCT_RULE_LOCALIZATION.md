# Prospective preregistration — COVARIANT_WEYL3_A7_FIRST_IBP_PRODUCT_RULE_LOCALIZATION

Status: **FROZEN BEFORE IMPLEMENTATION / NO REPAIR AUTHORIZED**
Date: 2026-09-19

## Parent terminal authority

Parent lower-order localization:
- gate: `COVARIANT_WEYL3_A7_LOWER_ORDER_COVARIANTIZATION_IBP_LOCALIZATION`;
- run: `35403445578`;
- durable result commit: `6ccfededab41dbe01b071916a5aa746491273276`;
- classification: `LOWER_ORDER_LOCALIZED_EXACT`.

The parent gate established, on the unchanged `OFFSHELL_A / d=7` witness:
- lower-order `F0-volume` before IBP: exact match;
- pointwise ordered `Fi`: exact match;
- first exact divergence: `FIRST_DERIVATIVE_IBP_TRANSFER`;
- second-derivative lower-order transfer: exact match;
- A7 principal and volume controls remain exact.

The frozen first-transfer scalar difference is

`-86355995554365317186893343264769708206041673/20078237934709401683903064632959076352000000`.

The smallest ordered coordinate witness already serialized target-blind in the parent artifacts is `i=0`.

For `-d_0 F_0`:

Researcher:
`43977684225232401744358310400305192156031283/25865232290557867013685792372725281247232000`

Critic:
`13469266506757221030260385050166541/4364950942592885650296098808000000`

Exact difference:
`-433508011369185071313333891829231313950116629/312885874482554842907489423863612273152000000`.

Do not replace this witness, coordinate, sign, normalization, parent discrepancy, or lane lineage.

## Scientific question

Why do the independently frozen pointwise `F_0` coefficients agree, while their transferred derivative `-d_0 F_0` disagrees?

The gate asks for the first exact disagreement in the product-rule anatomy of that one frozen transfer component.

## Frozen causal decomposition

Each lane must independently reconstruct the same `-d_0 F_0` component and serialize these ordered classes before cross-comparison:

1. `IBP1_DCOEFF_TIMES_DH`
   - derivative acts on the background coefficient tensor/density multiplying first derivatives of the perturbation;
   - Critic representation is the `-(d_0 K) * S_0(h_1)` part of its independently constructed scalar-test coefficient, with `K=sqrt(-g)P`;
   - Researcher must derive the homologous contribution independently from the direct metric directional-variation lineage, not by importing the Critic formula.

2. `IBP1_COEFF_TIMES_D2H`
   - derivative acts on the frozen first-derivative perturbation jet;
   - Critic representation is the `-K * d_0 S_0(h_1)` / second-perturbation-jet part;
   - Researcher must derive the homologous contribution independently.

3. `IBP1_DGAMMA_TIMES_H_COMPLETION`
   - derivative of pointwise-vanishing connection-times-`h` structures that can contribute because `Gamma(0)=0` but `dGamma(0)` need not vanish;
   - this class is zero only if independently established by the lane, never by convention.

4. `IBP1_OTHER_FROZEN_CONNECTION_INDEX_COMPLETION`
   - any remaining lower-order connection/index completion required by the lane's prospectively fixed derivation after classes 1-3;
   - its formula must be frozen in a separate implementation binding before production;
   - it may not be defined as a cross-lane fitted residual.

The exact sum of classes 1-4 must reconstruct each lane's already terminal parent `i=0` transfer value exactly.

## Controls

Mandatory:
- exact parent run/artifact/payload provenance;
- same `OFFSHELL_A / d=7 / i=0`;
- exact pointwise `F_0` agreement retained as a control;
- exact A7 principal and volume controls retained;
- exact rational/symbolic arithmetic only;
- `Gamma(0)=0` and frozen `dGamma` provenance;
- target-blind serialization before comparison;
- no shared scientific helper for the tested decomposition;
- `c6=SYMBOLIC_UNFIXED`;
- corrected Q10 remains LOCKED.

## Frozen comparison order

Compare classes in exactly this order:

1. `IBP1_DCOEFF_TIMES_DH`
2. `IBP1_COEFF_TIMES_D2H`
3. `IBP1_DGAMMA_TIMES_H_COMPLETION`
4. `IBP1_OTHER_FROZEN_CONNECTION_INDEX_COMPLETION`

Stop causal interpretation at the first exact nonzero difference while still verifying exact reconstruction of both parent `i=0` transfer values.

## Frozen terminal taxonomy

Only these scientific classifications are allowed:

- `LOCALIZED_IBP1_DCOEFF_TIMES_DH_MISMATCH`
- `LOCALIZED_IBP1_COEFF_TIMES_D2H_MISMATCH`
- `LOCALIZED_IBP1_DGAMMA_TIMES_H_COMPLETION_MISMATCH`
- `LOCALIZED_IBP1_OTHER_CONNECTION_INDEX_COMPLETION_MISMATCH`
- `IBP1_PRODUCT_RULE_CLASSES_MATCH__DEEPER_LOCALIZATION_REQUIRED`
- `IBP1_PRODUCT_RULE_DECOMPOSITION_DISAGREES`
- `BLOCKED_EXECUTION_OR_PROVENANCE`

Do not add or rename a category after inspecting the result.

## Independence

Researcher lineage remains direct metric directional variation plus explicit IBP.

Critic lineage remains independent P/Palatini/Euler/Taylor reconstruction.

For the tested product-rule classes:

`derive independently -> serialize/hash -> cross-compare`.

No lane may read the other lane's class values before its own payload is frozen.

## Forbidden

No:
- sign fitting;
- scale fitting;
- c6 fitting;
- Weyl normalization change;
- panel/witness/coordinate replacement;
- index remapping;
- post-result class movement;
- symmetry reduction;
- formula correction in this gate.

## Claim ceiling

This successor can only localize the already terminal first-IBP discrepancy. It cannot repair the parent scientific FAIL, establish a global variational theorem, determine physical `c6`, unlock corrected Q10, establish QGR, unitarity, UV completion, or new physics.

`theory_established = 0%`.
