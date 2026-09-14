# D5 canonical-lattice cache equivalence — terminal infrastructure PASS

Date: 2026-09-14

Gate: `D5-CANONICAL-CACHE-EQUIVALENCE`
Run: `34793411230`
Head: `43b844f691a716c0f678b9ed20c7ddb3fa140140`
Aggregate job: `103822309604`
Scientific authority: **none**

## Frozen classification

`D5_CANONICAL_CACHE_EQUIVALENCE_PASS`

The prospectively frozen 16-lane matrix completed with:

- expected lanes: `16`;
- found lanes: `16`;
- all valid: `true`;
- all pass: `true`;
- worst cached-vs-historical D relative residual: `3.0138740385466435e-12`;
- worst cached-vs-historical H5 relative residual: `3.0062091790262304e-12`;
- minimum corrupted-cache negative-control difference: `0.0007985885551649203`.

Frozen equivalence thresholds were `1e-9` for D/H and `1e-6` minimum effect for the deliberately corrupted cache control. The observed equivalence residuals are therefore roughly three orders of magnitude below the D/H tolerance, while the minimum negative-control effect is roughly three orders of magnitude above its required floor.

The cache uses exactly 129 unique canonical P/Weyl lattice points per H5 evaluation instead of approximately 290 historical repeated P/Weyl requests, without changing the nested five-point stencil, connection terms, A/I terms, H5 sign or `h=5e-4`.

## Aggregate artifact

- summary artifact `10327914830`;
- digest `sha256:e4fdb3ce144cb5f9621eaa5c4548e2202a3ff8ed081313cc479adc9b80741472`.

## Raw artifact provenance

- B1-p0 `10329435145`, `sha256:5e5448d9ff764fab02161c0d1d84fc5df9adb912c2940d1dc320aa3aaf07efc8`;
- C1-p0 `10329375271`, `sha256:3ae696a56d2acaf6821dd22a920c585bf1b692d9f90da851fb9ef9155023ea8c`;
- A1-p1 `10329355250`, `sha256:448dbc54e270b4c525a6017392c4f4ffaaef4e30e5fe360cba80c3524db600bc`;
- A2-p1 `10329325337`, `sha256:0cfa6e8f7dd6f387712b97cd57657d8a05a1af0f71bdd595ee1e4f214960bd31`;
- A3-p1 `10329275672`, `sha256:057fa6c989197ef7d58694071c403d26f6eb927df1ae1cb2e4a703563348d43f`;
- A1-p0 `10329230665`, `sha256:43b4382ffe59ab00f3ee5ccd114c5c228cc1df43dd064700892e7b5eac2b4fe0`;
- A0-p1 `10329215648`, `sha256:a8994c29b3e80e2cf88d62e507dd1f130630fe255b7a23d02f023a1350754d2f`;
- A3-p0 `10329210610`, `sha256:c6e418474b7b4d89142c2ac609a75557f6585ddba028b0d48116f2ed171e62b9`;
- A2-p0 `10329180775`, `sha256:6945e74e34f02fb0627a6b5789cc748c8700d97fdbb31eb0c80fa6b2766dfcf3`;
- C0-p0 `10329006043`, `sha256:6d675ab92dc6ceac563b1f5ea84c33c4effdbfea4be2d58dddf0b37a3ed607db`;
- A0-p0 `10328966094`, `sha256:5e14d9c2291c0ca9fdd45e6f986b794c2101a63307a468488c80372fc442e23e`;
- C1-p1 `10328709588`, `sha256:93459e54545f528deb73ba1b1b1e5875b310ac9f7689b87def939a952bd4a56c`;
- B0-p0 `10328594974`, `sha256:ae9a9f352e63e18968af0277b7c66459c907dccda23c8cfdc9f77a8029c4e4fe`;
- C0-p1 `10327814479`, `sha256:9de1606e7145907f89df8b05f8eb79cafe83fdc5beb1f8b7d270d89a880ecaf7`;
- B0-p1 `10327774678`, `sha256:bf95d752e79ee8a99c1e26f6d3b90f4e77467070f8eeade1a82e804a71c75e3c`;
- B1-p1 `10327694715`, `sha256:231443f23b70c602ce38cee4af0f213d9bcecfd5ba25a0575077630e8ba5cb56`.

## Static object-identity support

Separate code audit `analysis/D5_CACHE_OBJECT_IDENTITY_STATIC_AUDIT.md` established that the candidate cache evaluates the same historical

`geometry -> complex_step_gradient -> project_algebraic_riemann`

P object, the same inner/outer five-point coefficients, the same `b0.first_cov`, center connection additions and final

`A + I - 2 sqrt(-g) D`

formula. Only repeated evaluation reuse and canonical coordinate assembly differ.

## Authorized future implementation use

This PASS authorizes only a **prospective implementation choice** in a later scientific gate whose H5 derivative step is the tested `h=5e-4` and whose metric family/object lies inside the stated Iter053R-derived scope. It does not retroactively alter any active or historical result.

The conditional Iter053U gate was preregistered before this result and explicitly allowed adopting the cache only after a separate terminal equivalence PASS before final implementation freeze. That condition is now satisfied. Iter053U may therefore freeze the validated cache as its H5 backend before trigger creation, while keeping all Iter053U scientific criteria unchanged.

## Claim ceiling

This is infrastructure/implementation equivalence only. It is not functional-variation closure, does not classify Iter053T or Iter053U, does not change `c6`, `beta`, stability, unitarity, quantum consistency, UV completion, GR recovery or theory establishment.