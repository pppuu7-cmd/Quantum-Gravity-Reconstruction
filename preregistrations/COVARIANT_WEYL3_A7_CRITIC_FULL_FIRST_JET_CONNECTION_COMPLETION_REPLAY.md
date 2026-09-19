# Preregistration — COVARIANT_WEYL3_A7_CRITIC_FULL_FIRST_JET_CONNECTION_COMPLETION_REPLAY

Date: 2026-09-19
Status: **FROZEN BEFORE FULL FIRST-JET CORRECTED REPLAY**

## Parent authorities

- Original Fi first-jet localization: `07ad77de0506a3de5e7db601e2cfc8b5edc37c5c`, run `35404041767`.
- Partial-to-covariant conversion sign authority: `81fcf14aa119eb00a9522c0d5e694fe1290b54ea`, run `35412025556`.
- Corrected Critic slot-00 closure: `7770e086992d43368a5a4d23ee0ff6b272d4c156`, run `35412201058`, classification `CORRECTED_CRITIC_SLOT00_EXACTLY_MATCHES_RESEARCHER`.

Historical results are immutable.

## Scientific question

When the same independently derived partial-to-covariant connection completion is applied prospectively to every Critic first-jet slot `(i,j)` with `i,j in {0,1,2,3}`, does the complete corrected Critic first-jet tensor agree exactly with the frozen Researcher direct-metric first-jet tensor, including the diagonal scalar first-IBP transfer?

## Frozen corrected construction

Reconstruct the original Critic Palatini `Fi[i]` polynomials exactly on `OFFSHELL_A / d=7`.

For every `i,j` derive independently the complete 256-component conversion tensor from:
- repository metric second jets;
- frozen perturbation values `h_ab`;
- `partial_r phi_i = delta_ri`;
- background connection derivative direction `j`;
- the tensor identity `partial partial = covariant Hessian - C_nabla`;
- repository Riemann second-derivative ordering.

For each Riemann component and each `i`, augment the Critic variation polynomial by

`sum_j x^j K_conversion_abcd(i,j)`.

This must leave every pointwise `Fi[i]` unchanged.

No frozen Researcher value, Researcher helper, parent connection target, or parent transfer target may appear in the corrected Critic implementation.

## Independent frozen Researcher reference

A separate workflow job must execute the exact historical Researcher first-jet implementation blob from commit `f6a94c190b1df7ab388cf4f33ffed88a09ebca15`.

The corrected Critic job must not import or read this reference job.

Comparison is terminal-only after both artifacts are serialized.

## Frozen comparisons

Compare:
1. all four pointwise `Fi[i]`;
2. all 16 ordered first-jet slots `d_j Fi[i]`;
3. for every slot, frozen source classes in the original order;
4. all four diagonal `-d_iFi[i]`;
5. scalar first-IBP transfer.

Record the first residual slot and first residual source class if any.

## Mandatory controls

- exact rational arithmetic;
- exact original Critic reconstruction;
- all 16 independently derived conversion tensors serialized;
- every corrected pointwise `Fi[i]` equals original Critic pointwise `Fi[i]`;
- only `CONNECTION_JET` changes in the Critic source ledgers;
- source reconstructions exact in all 16 slots;
- exact historical Researcher blob/provenance lock;
- target-blind corrected Critic serialization before comparison;
- no tolerance, sign fitting, slot-specific tuning, free-index permutation, or post-hoc repair.

## Frozen terminal taxonomy

- `CORRECTED_CRITIC_FULL_FIRST_JET_EXACT_MATCH`
- `CORRECTED_CRITIC_RESIDUAL_FIRST_JET_DIVERGENCE`
- `BLOCKED_EXECUTION_OR_PROVENANCE`

## Interpretation ceiling

A terminal full exact match would close the entire prospectively frozen Fi first-jet interface and the scalar first-IBP transfer discrepancy on the frozen witness. It still would not retroactively alter the historical parent FAIL. Reclassification of the parent covariant directional-variation certificate would require a separate prospectively frozen corrected parent replay.

`c6=SYMBOLIC_UNFIXED`; corrected Q10 locked; `theory_established=0%`; no experimental, global QGR, quantum-unitarity, UV-completion, physical-c6, or new-physics claim.
