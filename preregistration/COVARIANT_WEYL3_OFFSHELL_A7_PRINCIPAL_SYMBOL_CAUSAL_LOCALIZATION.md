# COVARIANT_WEYL3_OFFSHELL_A7_PRINCIPAL_SYMBOL_CAUSAL_LOCALIZATION

Date: 2026-09-18
Status: PROSPECTIVE / SCIENTIFIC LOCALIZATION ONLY
Parent terminal result: `SCIENTIFIC_FAIL_COVARIANT_WEYL3_DIRECTIONAL_VARIATION_DISCREPANCY`
Parent run: `35367461999`
Parent durable result commit: `e26208cec90566001b65640775d2e58d0429bf5c`

## Frozen counterexample

Use exactly the first counterexample under the parent frozen cell order:

- seed: `OFFSHELL_A`
- seed parameter: `s=11`
- direction: `d=7`
- parent Researcher artifact: `10556807770`, digest `sha256:db22b1855d1c37db856036ea6e73a27a1e82daece704fa9322a5d959059a0143`
- parent Critic artifact: `10556747806`, digest `sha256:1002a866b1351dbed586c3b2ba1b77cc5a9ae0e07f72ef435d659ea29f4b0bb3`
- Researcher parent cell witness SHA256: `69c1c0db798cc921c5ca4c45ca0a61f0d38a35392c75707a5c3e78ff03b9134d`
- Critic parent cell witness SHA256: `09d544faf078bd7b4046ad1d7d0f768a489d93ff912effddfcbaf8d838d8b19b`
- Critic parent point-P SHA256: `21095bed2a18f7a5fa2484961c75d4cd7589115d6a6f664f0b3eee8697cdd4fe`

Do not replace this cell or direction.

## Frozen scientific question

The parent gate establishes exact agreement through metric jets, Riemann, Ricci, scalar, Weyl and `I3`, but exact disagreement between the direct bulk derivative and independent Euler contraction on all four off-shell cells.

This localization gate asks two ordered questions on the smallest counterexample.

### Stage V — volume / determinant identity

Independently evaluate the direct density-volume contribution

`V_direct = delta(sqrt(-g)) * I3`

for `delta g_ab = h_ab phi` at `phi=1`, and the Euler metric contribution

`V_Euler = (1/2) g^{ab} I3 h_ab`.

Require exact equality.

This stage is fixed before principal-symbol comparison.

### Stage P — highest-derivative principal symbol

Let the Critic parent object `P^{abcd}` be the exact algebraic Frechet derivative satisfying the frozen `P.R = 3 I3` control.

At the normal-coordinate point, the highest-derivative metric variation is

`delta R_abcd |_(d2 h) = 1/2( d_c d_b h_ad + d_d d_a h_bc - d_c d_a h_bd - d_d d_b h_ac )`.

For the frozen perturbation `h_ab(x) phi(x)`, construct, without reading the Researcher second-derivative coefficients, the ten exact coefficients of `d_i d_j phi` predicted by

`P^{abcd} delta R_abcd |_(d2 phi)`.

Compare them only after both ten-vectors have been serialized and hashed.

The Researcher ten-vector is the already frozen `Fij` vector from the parent direct-variation witness.

## Target-blind chronology

1. Reproduce/pin the parent Researcher and Critic counterexample witnesses.
2. Serialize/hash Researcher `Fij` vector.
3. Independently construct and serialize/hash Critic-P principal-symbol vector.
4. Only then compare.
5. No sign flip, multiplicative fitting, normalization change, Weyl convention change, panel change, or index remapping after comparison.

## Mandatory controls

- exact parent cell and jet hashes;
- exact parent Researcher and Critic witness hashes;
- exact parent point-P hash;
- all parent self-controls remain true;
- exact rational arithmetic, no tolerance;
- normal-coordinate `Gamma(0)=0`;
- Riemann/Weyl common-domain equality remains exact;
- off-shell Ricci and scalar preconditions remain true;
- `c6 = SYMBOLIC_UNFIXED`;
- corrected Q10 remains LOCKED.

Any control/reproduction failure is `BLOCKED`, not scientific evidence.

## Allowed terminal classifications

1. `LOCALIZED_DETERMINANT_OR_METRIC_INDEX_CONVENTION_MISMATCH`
   - Stage V is nonzero.

2. `LOCALIZED_P_FRECHET_PRINCIPAL_SYMBOL_MISMATCH`
   - Stage V passes exactly;
   - Stage P ten-vector differs exactly.

3. `PRINCIPAL_SYMBOL_AND_VOLUME_MATCH__LOWER_ORDER_COVARIANTIZATION_OR_IBP_LOCALIZATION_REQUIRED`
   - Stage V passes exactly;
   - Stage P ten-vector agrees exactly;
   - parent bulk discrepancy remains nonzero.

4. `SCIENTIFIC_FAIL_PARENT_DISCREPANCY_NOT_REPRODUCIBLE_UNDER_FROZEN_COUNTEREXAMPLE`
   - parent terminal discrepancy cannot be reproduced while all controls pass.

5. `BLOCKED_COVARIANT_WEYL3_A7_PRINCIPAL_SYMBOL_LOCALIZATION_EXECUTION_OR_PROVENANCE_FAILURE`
   - any mandatory control or exact provenance check fails.

No classification from this gate repairs or reclassifies the parent terminal scientific FAIL.

## Claim ceiling

This is causal localization of one already terminal counterexample. It does not establish a global variational theorem, does not determine `c6`, does not unlock corrected Q10, and does not authorize any quantum-gravity completion claim.
