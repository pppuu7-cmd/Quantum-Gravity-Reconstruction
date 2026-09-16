# Post-Iter057Z provisional unrestricted Q10 response — independent reproduction

Date: 2026-09-16

Status: **INDEPENDENT REPRODUCIBLE PROVISIONAL PASS — NOT CANONICAL UNTIL OFFICIAL ITER057Z R12 AUTHORITY IS CONSUMED**

Execution-start main authority: `d19502242077854c26df51cbc636ce7f2b8e7dfd`. At that point Iter057Z was still `PROSPECTIVELY_PREREGISTERED__IMPLEMENTATION_NOT_YET_LAUNCHED`.

During reproducibility verification auto-research subsequently added official Iter057Z implementation `a7f8198bdb41c5667ea47b2689731e238307fc94`, pre-production payload freeze `8ccccdea0954e70b0337d2db39470699e7342957`, and Ubuntu/Windows reproduction launches. No official terminal Iter057Z result or canonical ordered R12 coefficient authority was consumed by this calculation.

## Question

On the independently reproduced dodecic Einstein seed and the independently reproduced provisional Weyl3 source through coordinate degree eight, can the terminal lower first-order response `Q2+Q4+Q6` be extended first by an independently reconstructed `Q8`, and then by a completely unrestricted pure degree-ten trace-reversed response `Q10`, so that covariant de Donder gauge vanishes through degree nine and `DG_g[qhat]-Shat` vanishes through coordinate degree eight?

This is deliberately a provisional research gate. It does not assign an official post-Z iteration name and does not create canonical coefficient authority while official Iter057Z remains unterminated.

## Independent inputs and method

The evaluator consumes terminal Iter057S and Iter057V artifacts for `Q2/Q4` and `Q6`, the already-terminal seed authorities through R10, the independently twice-reproduced R12 coefficient set, and the independently reproduced provisional Weyl3 source through degree eight.

It does **not** copy the official Iter057Y Q8 coefficient list. Instead it reconstructs Q8 from the lower response/source authorities using the complete unrestricted exact degree-eight affine complex, verifies the complete Iter057Y controls, and only then uses that reconstructed lower response in the new Q10 solve.

All polynomial arithmetic is exact Python `Fraction` arithmetic and all rank/RREF operations are exact over SymPy `QQ`. No floating rank, zero tolerance, finite difference, restricted ansatz, lower-response refit, or seed mutation is used.

## Internal Iter057Y reconstruction control

The independent Q8 reconstruction reproduced the known terminal structural/result invariants:

- exact matrix shape `1320 x 1650`;
- matrix nnz `5280`;
- `rank(M)=rank([M|r])=1096`;
- left-nullity/Bianchi rank `224`;
- nullity `554`;
- all `224/224` actual compatibility contractions zero;
- fresh pre-Q8 degree-seven gauge residual count `79`;
- fresh pre-Q8 degree-six field/source residual count `140`;
- deterministic particular Q8: `180` nonzero normalized coefficients;
- exact affine residual zero;
- full lower replay through gauge degree seven and field/source degree six zero.

The independently reconstructed ordered Q8 particular has digest

`97e9b07860807a0a5072f021f08619dafa9b39c3bd5a82beba86c0319c458b70`.

## New unrestricted Q10 result

The pure coordinate-degree-ten symmetric trace-reversed response contains

`10*C(13,3)=2860`

unknown normalized coefficients. The complete target complex contains

- de Donder degree nine: `4*C(12,3)=880` rows;
- field/source degree eight: `10*C(11,3)=1650` rows;
- total exact matrix shape `2530 x 2860`;
- matrix nnz `10120`.

Exact source-independent/source-specific controls give

- `rank(M)=2050`;
- `rank([M|r])=2050`;
- left-nullity `480`;
- nullity `810`;
- complete canonical Bianchi family count/rank `480/480`;
- Bianchi family annihilates the principal matrix exactly;
- all `480/480` compatibility contractions with the actual curved residual vanish exactly.

The fresh lower-response residual before Q10 is nontrivial:

- degree-nine covariant de Donder residual: `139` nonzero normalized slots;
- degree-eight field/source residual: `260` nonzero normalized slots.

Setting the 810 homogeneous directions to zero only to select a deterministic particular solution gives **320 nonzero normalized Q10 coefficients**. All 810 homogeneous directions remain mathematically unfixed.

The complete ordered Q10 particular digest is

`0c45f835157d78870d01dc105f9b3c6ec77d1c9ac2fe6e24ca00d6ad8417ba81`.

Every affine row vanishes exactly after Q10 is inserted.

## Independent full replay

After inserting Q10, a separate replay rebuilt the background geometry and response tensors and verified:

- independent dodecic background inverse/vacuum controls through coordinate degree ten: exact;
- covariant de Donder condition through degree nine: exact zero;
- reduced `DG_g[qhat]-Shat` through coordinate degree eight: exact zero in all ten independent components;
- independent unreduced covariant linearized Ricci/scalar/Einstein `DG_g[qhat]-Shat` through coordinate degree eight: exact zero in all ten independent components;
- pure degree-ten Q10 preserves the complete previously fixed response through order nine.

Research-branch classification:

`REPRODUCIBLE_PROVISIONAL_PASS_POST_ITER057Z_UNRESTRICTED_ONSHELL_O_C6_Q2_Q4_Q6_Q8_Q10_RESPONSE_MATCHES_PROVISIONAL_WEYL3_SOURCE_THROUGH_EIGHTH_EVEN_ORDER__NOT_CANONICAL_UNTIL_OFFICIAL_Z`

## Reproducibility

Two complete successful clean execution paths produced byte-identical result JSON and byte-identical ordered Q10 coefficient JSON.

A self-contained reproduction bundle was then assembled, unpacked into a fresh directory, and executed using only relative bundled inputs. The fresh execution exited successfully and reproduced both files byte-for-byte.

Stable hashes:

- complete result JSON SHA-256: `a90a9d5285d3bad465768ce4d01fa8dff6803dd6ce78f2f7c199c219ea7f4071`;
- ordered Q10 JSON SHA-256: `dca8044895e54df88aa77b9754d3b2852ded98fa899b76677692d63984fae0c4`;
- Q10 CSV SHA-256: `349dda686e60f9a4558e041176e6d25f10850c2446ed04dec6bbc1eead5227ab`;
- scientific payload SHA-256: `a8aab3f39baa057f89e8b1fbdb1485e9cc5f54064842e1569837afb06795e72a`;
- self-contained reproduction ZIP SHA-256: `94d45a7ac7ebeb4e8311ee10b47cbad16830d5a618e99e0c7751ae514ddb542a`.

## Promotion lock

Official Iter057Z pre-production payload freeze reports two identical official local exact reproductions, but its ordered R12 coefficient authority has not yet been consumed here. Therefore neither the provisional degree-eight source nor this Q10 response is promoted to canonical authority by this certificate.

Once official Iter057Z terminalizes, the first required operation is an exact ordered coefficient comparison between official canonical R12 and the independent R12 used here. If they are identical, the degree-eight source and Q10 chain can be replayed directly against the official seed. If they differ by a legitimate homogeneous degree-twelve freedom, the degree-eight Weyl3 source and Q10 response must be recomputed on the official canonical R12 rather than promoted by assumption.

## Scope ceiling

This establishes only a reproducible finite local provisional first-order `O(c6)` Taylor response through coordinate degree eight conditional on the independent R12 seed choice. It does not establish an all-orders/convergent solution, an open-neighborhood/global/asymptotic solution, a value/sign/running of `c6`, `beta=1`, physical characteristics, strong hyperbolicity, ghosts/stability, quantum unitarity, regulator removal, a global interacting measure, UV completion, experimental confirmation, new physics, or QGR correctness.

`c6` remains symbolic/unfixed and theory established remains `0%`.
