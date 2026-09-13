# Iter051C-D1 — Assembly-term localization diagnostic

Date: 2026-09-13
Gate: `ITER051C-D1-ASSEMBLY-TERM-LOCALIZATION`

## Authority and scope
This diagnostic was preregistered after the terminal Iter051C full-assembly failure and does not alter or erase that historical failure. It decomposes the exact G48 reduced Euler–Lagrange response into the three previously constructed pieces

- `A`: algebraic metric-density contribution,
- `I = sqrt(-g) sym(P·R)`: curvature-lowering insertion,
- `J = sqrt(-g) D`, with `D^{mn}=∇_b∇_a P^{a m b n}`: covariant double-divergence contribution.

The fitted coefficients are diagnostic only. They are not replacement authority for the failed frozen assembly and do not fix `c6`.

## Prospective provenance
- preregistration commit: `6eae32508dacccf0a2be6a947bfa84707a5aa9c4`
- implementation commit: `a4f412632ffbbdb1989ec8049fc7e363133d03ae`
- aggregate commit: `39437929740a8105e63c7cf291147fda247ad4aa`
- workflow commit: `32e91be9d5ee619b1752a16c629097c23b301372`
- production head: `a705020e9f0b5779c39ddf62174bd000db84a735`
- authoritative run: `34741524418`
- aggregate job: `103682017568`
- summary artifact: `10313265535`
- summary artifact digest: `sha256:38dcc34cf1502bef249ad315461e35a0ac3ad4ad02df3f58e1a3826d52829412`

## Terminal diagnostic result
Classification: **`DIAGNOSTIC_LOCALIZED_G51C_COEFFICIENT_PATTERN`**.

All six frozen Bianchi-I diagnostic witnesses were present and controls were valid. The stacked response matrix had full rank 3.

Best-fit coefficients multiplying `(A,I,J)`:

`(0.9999999910360834, 0.9999999923600963, -1.9999999868098797)`.

Key frozen metrics:
- global fitted relative residual: `1.642818965188329e-07`;
- historical `A + I + 2 J` residual: `2.042500869567214`;
- diagnostic sign-flipped `A + I - 2 J` residual: `5.359533167345127e-06`;
- maximum leave-one-out coefficient spread: `7.345974766392648e-05`;
- maximum leave-one-out relative residual: `2.2509928275044167e-07`;
- term norms: `||A||=162.1878350144779`, `||I||=336.08173548162484`, `||J||=580.1481575629347`;
- exact target norm: `1146.4004973628516`.

## Interpretation
The frozen panel strongly localizes the Iter051C mismatch to the overall sign/order convention of the double-divergence contribution: keeping the already-tested `A` and `I` coefficients at `+1` while reversing the `J` coefficient from `+2` to `-2` nearly closes the independent exact G48 reduced response.

This is **not** permission to replace the failed formula by fit. The next required step is an independent Palatini/index-symmetry derivation of the sign and a held-out validation panel not used in this diagnostic. Only after that may a separately preregistered replacement full-EOM gate be authorized.

Historical Iter051C remains `SCIENTIFIC_FAIL_G51C_FULL_WEYL3_EOM_ASSEMBLY`.

## Claim locks
- `c6` remains symbolic/unfixed;
- `beta=1` is not authorized;
- full covariant six-derivative EOM are not established;
- theory established remains `0%`;
- this finite diagnostic is not experimental confirmation, a global theorem, an energy-positivity proof, or a quantum-unitarity proof.
