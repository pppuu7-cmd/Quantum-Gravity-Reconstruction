# Corrected degree-eight -> degree-six reduction discrepancy localization — terminal result

Date: 2026-09-18
Gate: `CORRECTED_DEGREE8_DEGREE6_REDUCTION_DISCREPANCY_LOCALIZATION`
Status: **TERMINAL DIAGNOSTIC LOCALIZATION**

Preregistration: `ffc110bfd2067d13d135577141154b2aab8626be`
Initial diagnostic implementation: `0114c580fbaf505b553a871a76af973fb8282b9b`
Initial workflow: `e0240be7fc2c1d5d80e0c181cc52d090822a65cc`
Boundary-control repair preregistration: `b2f4c513bdd8ffbbb37202e0b7b756f626d920ec`
Boundary-repaired implementation: `e9d8f4b4113881f8bd5ef0494dc7039c2b2c14d9`
Repaired workflow head on main: `8c414c3196b426a977af9465cd24e862c221924a`
Execution-only branch head: `1646cbf8347110477f8c3920c81e3aac28723288`
Execution PR: `#29`, closed unmerged after production.

Authoritative Actions run: `35276104151`
Primary job: `105387003387`
Independent job: `105387003716`
Terminal job: `105391477932`

Authoritative artifacts from the completed run:
- primary `10520996172`, digest `sha256:57a47af56d4db2b16c7d4874acebc65faf825c21c988989a4c838fdf5d1cce5b`;
- independent `10521176638`, digest `sha256:b90de5fb90f0874b7d8d4108019699a479305aa0ae65a068368217ef012eee88`;
- terminal `10521606016`, digest `sha256:d9844904345d0a098579148c319f9b303dd50235469a78f486a4d9775829369d`.

Terminal payload SHA256:

`d9583cdee72a12424525d713cfbc78674db33d070de76af7e7215afe43a8178c`

## Terminal classification

**`LOCALIZED_GENERALIZED_CONSTRUCTOR_FORMULA_MISMATCH`**

Frozen terminal reason:

`discrepancy persists before serialization across both tested truncation boundaries`

## Exact result

The two independently assembled Euler-source lanes were executed outcome-blind with respect to the AT coefficient target until both local decompositions had been frozen.

For both `R10` and `R12` seed boundaries, and in both the primary and independent AO-style lanes, the final ordered degree-six source projection has the same SHA256:

`2f15c55c0b326966c821141e43e245e3715f93fc9f4b9ee720179f31b1e28b6d`

The authoritative Iter057AT ordered 840-vector remains:

`5d070732d90b864f6167e03da85b86ce531d127dc9442fdbb928fd1b6153ee6b`

Thus:
- primary R10 != AT;
- primary R12 != AT;
- independent R10 != AT;
- independent R12 != AT.

Adding the R12 seed layer does not change the degree-six generalized projection. The discrepancy is therefore not localized to R12 truncation-order coupling.

The prospectively frozen decomposition hashes are also invariant between R10 and R12 and agree between the independent lanes:

- algebraic `P.R` contribution: `577fed39c331d3199cd2d9af148d128b95dbfed82bf1fa3e9c3855a58795499c`;
- double-covariant-divergence contribution: `c2a774b5180ce92f94f3b7f88795e38c100c65f0e0d0bad3e80a96bcff42fc37`;
- metric-times-I3 contribution: `5feff63cc6976d8cfb4e506800e7f897b449ef5d0c0e33d0785cef7a608eae58`;
- index-lowering contribution: `f21effc428ec1e7150d906de4ff88b7000f2661352c04c6869279567b3da410d`.

Both primary and independent lane controls were all true, including the boundary-specific vacuum controls, exact arithmetic, AT ordered-hash reconstruction, and reproduction of the parent generalized-constructor hash.

Because the exact polynomial/tensor discrepancy is already present before target serialization and survives both tested sufficient seed boundaries, the frozen classifier selects the generalized-constructor-formula-mismatch outcome rather than a serialization/basis or truncation-order explanation.

## Historical first attempt

Run `35274901385` remains an implementation-invalid diagnostic attempt. Before any terminal scientific use, a boundary-control defect was identified: the R10 diagnostic boundary was incorrectly required to be vacuum through coordinate degree ten even though its role in this diagnostic only requires the lower sufficient ceiling; the R12 layer is the layer that cancels the degree-ten Einstein residual. The repair was prospectively frozen at `b2f4c513bdd8ffbbb37202e0b7b756f626d920ec`. No payload from the invalid attempt is promoted.

## Provenance correction

The first durable write of this result, commit `d9384e9e98f536862354a02983e0916ddf61e05d`, was made from stale intermediate artifact metadata. Before using that record as authority for any subsequent gate, the completed run was re-read directly. This commit corrects only artifact IDs/digests, component hashes, and terminal payload SHA256 to the immutable completed-run values above. The terminal classification and scientific interpretation are unchanged.

## Consequence for the DAG

This result does **not** alter or reclassify Iter057AT. It localizes the current higher-order inconsistency: the generalized corrected degree-eight constructor does not reduce to the exact corrected degree-six AT producer even before serialization.

The exact AT producer has now been recovered from commit `c4e7ccc05ea1b8f4967379fc370812dfa99cce03`. It uses the same corrected Frechet machinery but the source-degree-six construction is frozen as:

- `seed_metric10()` plus `geometry8(g)`;
- `Cup = raise_last(C,gi,8)`;
- `I3,QF = _fixed_cubic_and_Q(C,Cup,6)`;
- `PF = _fixed_p_from_frechet(...,QF,8)`;
- degree-six downstream Euler assembly (`aq.x_operator` in the primary lane, AO covariant assembly independently).

The generalized degree-eight constructor instead uses the higher-order geometry together with `_fixed_cubic_and_Q(...,8)` and `_fixed_p_from_frechet(...,10)`. The next exact falsifier is therefore a prospectively frozen same-seed cutoff/intermediate-object identity test that changes these construction ceilings one at a time before any AT target comparison.

Therefore:
- the provisional corrected degree-eight source remains non-authoritative;
- corrected Q10 remains LOCKED;
- no sign, scale, normalization or `c6` fitting is authorized.

`c6 = SYMBOLIC_UNFIXED`.

`theory_established = 0%`.
