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

Artifacts:
- primary `10520393688`, digest `sha256:edfc076c8f191033b34acf2a9acdc3948a941e7a62d53c3b1741e4740974bf79`;
- independent `10520580260`, digest `sha256:312181e0e21d49e0d9f054d7ae81a3a3f3ea2eaa636fae8630925446100e8291`;
- terminal `10520764537`, digest `sha256:c690ff6ca5d21f67e0208595904b289480863db905e163b607d258ebdfd1f98e`.

Terminal payload SHA256:

`d9583cde175969f84971acf82f7ee2cef1d7052f9407e9c3e213d0bf1e5ee844`

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

- algebraic `P.R` contribution: `c11c5abfb59891e93b7d85ffd1cf44fc733df8753404028c472bbbe1d46a5534`;
- double-covariant-divergence contribution: `27fa490a169995271880cbe045ee01b3a498ac087bfd1ac889e20bda10e6d1ac`;
- metric-times-I3 contribution: `792594319750a629693ec3c01cb164a12e0ddc1748a806299386ece31ee88803`;
- index-lowering contribution: `96761bbfcfba5caf9b6691150242ddd8092a18cb6ca48b1511249d48660080b4`.

Because the exact polynomial/tensor discrepancy is already present before target serialization and survives both tested sufficient seed boundaries, the frozen classifier selects the generalized-constructor-formula-mismatch outcome rather than a serialization/basis or truncation-order explanation.

## Historical first attempt

Run `35274901385` remains an implementation-invalid diagnostic attempt. Before any terminal scientific use, a boundary-control defect was identified: the R10 diagnostic boundary was incorrectly required to be vacuum through coordinate degree ten even though its role in this diagnostic only requires the lower sufficient ceiling; the R12 layer is the layer that cancels the degree-ten Einstein residual. The repair was prospectively frozen at `b2f4c513bdd8ffbbb37202e0b7b756f626d920ec`. No payload from the invalid attempt is promoted.

## Consequence for the DAG

This result does **not** alter or reclassify Iter057AT. It localizes the current higher-order inconsistency: the generalized corrected degree-eight constructor does not reduce to the exact corrected degree-six AT producer even before serialization.

Therefore:
- the provisional corrected degree-eight source remains non-authoritative;
- corrected Q10 remains LOCKED;
- the next highest-information exact gate is a same-seed operator-identity comparison between the historical AT-producing Frechet construction and the generalized construction, with special attention to the prospectively identifiable Frechet degree cutoffs before the downstream Euler assembly;
- no sign, scale, normalization or `c6` fitting is authorized.

`c6 = SYMBOLIC_UNFIXED`.

`theory_established = 0%`.
