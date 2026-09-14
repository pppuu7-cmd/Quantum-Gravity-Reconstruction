# Iter057B terminal result — null-cone two-block symbolic pencil rank

Date: 2026-09-15
Gate: `ITER057B-NULL-CONE-TWO-BLOCK-EINSTEIN-WEYL3-SYMBOLIC-PENCIL-RANK`
Prospective preregistration: `9045d51c4b542122c171756488333e20655012a4`
Implementation: `7cc8ed42c11ea84c516e81822c3cc5aa9da08fa7`
Production head/workflow: `04394e51061b6cca851ba1960e810e06d1855f72`

## Authoritative production

- workflow run: `34904668488`
- job: `104178441738`
- job conclusion: `success`
- artifact: `iter057b-two-block-pencil-summary`, id `10372107245`
- artifact ZIP digest: `sha256:f00f59419c74b71bef88392e6f36401886d7a0f0d13aa49f2fe8f8e80cc86462`
- frozen panel: 12 exact rational Weyl backgrounds x 2 exact null covectors = 24 cases

Green CI is not scientific PASS. The frozen maximum-PASS criterion was not satisfied.

## Terminal classification

**`PARTIAL_SCOPED_ITER057B_GENERIC_NONZERO_MULTIPLIER_RANK5_ALL_NONZERO_NOT_CERTIFIED`**

This classification is exactly the prospectively frozen fallback. It is not upgraded post hoc.

## Frozen object

For each case the audited two-block symbolic pencil is

`M(lambda) = M2_Einstein + lambda M4_Weyl3`,

where `lambda` is a formal relative multiplier only. No numerical/sign choice for physical `c6` is made.

## Frozen controls

All Iter057A object controls were reproduced in all 24 cases:

- the two frozen covectors satisfy `k^2=0` exactly;
- pure-gauge rank is 4;
- `rank M2=4`, `nullity M2=6`;
- `rank M4=4`, `nullity M4=6`;
- both symbols annihilate all four pure-gauge columns;
- the full common kernel of `M2` and `M4` has dimension 5.

There were zero INVALID cases.

## Generic symbolic-rank result

For every one of the 24 cases, an exact nonzero 5x5 minor polynomial of `M(lambda)` was constructed. Therefore

**`rank M(lambda)=5` over the rational-function field `Q(lambda)` in 24/24 cases.**

Equivalently, rank five holds for generic symbolic multiplier values on the frozen panel.

The common five-dimensional kernel gives the independent upper bound `rank<=5`, so the generic rank is exactly five rather than merely at least five.

## Why maximum PASS was not achieved

The preregistration deliberately required a stronger all-nonzero certificate: at least one exact 5x5 minor in each case had to factor as a pure nonzero monomial

`c * lambda^m`, `m>=1`.

The deterministic frozen candidate-minor construction found **0/24** such monomial minors.

Instead, candidate minors contained additional factors. For example, the first frozen null covector/background case produced

`lambda^2 * (28338 lambda - 5005) / 624624`.

Thus one candidate minor alone does not certify rank five for every nonzero `lambda`, and the maximum-PASS condition is not met.

## Post-terminal diagnostic that does not change classification

After the frozen criterion was known to fail, the nonzero rational roots of the deterministic candidate minors for the first null covector were checked against the **full 10x10 matrix** rather than the selected minor. In those diagnostic checks, the full matrix still had rank five at the candidate-minor roots.

This shows that a zero of one chosen maximal minor need not be a true rank-drop point. However, this was not the preregistered all-nonzero certificate, so it cannot promote Iter057B beyond PARTIAL.

The appropriate successor is a separately preregistered exact reduced-pencil or coprime/maximal-minor certificate.

## Scientific consequence

On the frozen local null-cone panel, the two-block Einstein plus Weyl3 symbol has a stable exact structure for generic multiplier:

- four gauge directions remain in the common kernel;
- one additional non-gauge common kernel class remains;
- the generic two-block rank is five;
- the second GR non-gauge null class is therefore lifted by the Weyl3 `k4` block for generic multiplier.

This is consistent with Iter057A's quotient-intersection dimension one. It does **not** yet prove rank five for every nonzero multiplier, nor does it establish a full characteristic polynomial.

## Interpretation ceiling

This audit includes only the blocks `M2_Einstein + lambda M4_Weyl3`. The full linearization of the covariant Iter056X Weyl3 Euler tensor on a curved background also contains lower-degree-in-`k` Weyl3 terms. Those terms are not included here.

Therefore this PARTIAL result does not establish:

- birefringence or a shifted causal cone;
- the complete mixed-order characteristic variety;
- strong/symmetric hyperbolicity or well-posedness;
- gauge-constraint propagation or an energy estimate;
- physical mode count, ghost sign/residue, stability;
- exact versus order-reduced treatment selection;
- a value/sign/running of `c6`;
- quantum unitarity or UV completion.

`c6` remains symbolic/unfixed; `beta=1` remains unauthorized; theory established remains `0%`; historical FAIL/INVALID/BLOCKED/PARTIAL classifications remain immutable.