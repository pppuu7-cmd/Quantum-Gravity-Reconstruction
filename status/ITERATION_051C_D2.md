# Iter051C-D2 — independent Palatini sign derivation and held-out validation

Date: 2026-09-13
Gate: `ITER051C-D2-VARIATIONAL-SIGN-AND-HELDOUT-VALIDATION`

## Prospective authority
This file is committed before D2 implementation and production. D2 is a diagnostic/validation gate created only after terminal G51C and D1. It does not rewrite either historical result and no threshold below may be weakened after production.

Historical authority retained:
- Iter051C: `SCIENTIFIC_FAIL_G51C_FULL_WEYL3_EOM_ASSEMBLY`, run `34741060700`.
- Iter051C-D1: `DIAGNOSTIC_LOCALIZED_G51C_COEFFICIENT_PATTERN`, run `34741524418`; its fitted `(A,I,J)≈(1,1,-2)` is diagnostic only and is NOT used as a fit in D2.

`c6` remains symbolic/unfixed throughout.

## Independent analytic sign derivation frozen before production
Use the same convention as G51C:

`δ[√(-g) I3] = H^{mn} δg_mn + total derivative`,

with all-lower curvature as the independent curvature slot for the algebraic derivative and

`P^{abcd}=∂I3/∂R_abcd`

projected to exact Riemann algebraic symmetries.

The curvature-response part of the variation is split as

`δR_abcd = δg_ae R^e_bcd + g_ae δR^e_bcd`.

The first term is the already-defined lowering insertion

`I^{mn}=√(-g) sym[P^{m b c d} R^n_bcd]`.

For the connection term, Palatini gives

`δR^e_bcd = ∇_c δΓ^e_db - ∇_d δΓ^e_cb`.

Antisymmetry of `P` in `(c,d)` gives a factor two. After the first integration by parts and insertion of

`δΓ^e_db = 1/2 g^{ef}(∇_d h_bf + ∇_b h_df - ∇_f h_db)`, `h_mn=δg_mn`,

the projected Riemann symmetries, pair exchange, and the covariant derivative ordering fixed in G51B0-R1/B2 reduce the coefficient of symmetric `h_mn` to

`-2 √(-g) D^{mn}`,

where the project convention is

`D^{mn}=∇_b∇_a P^{a m b n}`.

Therefore the **prospectively derived candidate** tested in D2 is

`H_D2^{mn}=A^{mn}+I^{mn}-2√(-g)D^{mn}`.

The historical G51C formula `A+I+2√(-g)D` is retained unchanged as a frozen negative control. No coefficient is fitted in D2.

## Frozen production matrix — 20 scientific lanes

### Stream A — 8 held-out Bianchi-I exact reduced-EL witnesses
These `(p,q,t)` witnesses are disjoint from the six G48/D1 fit witnesses:
1. `(-3/4, 1/5, 4/5)`
2. `(1/3, -2/5, 5/4)`
3. `(2/3, 1/6, 7/6)`
4. `(4/3, -1/4, 9/8)`
5. `(5/4, 2/5, 6/5)`
6. `(-1/3, 3/5, 7/5)`
7. `(3/4, -1/2, 5/3)`
8. `(7/5, 1/3, 11/10)`.

Compare `H_D2` to the exact generalized reduced Euler–Lagrange formulas independently derived in Iter048/G48 using
- `E_N=-2 H^{00}` at `N=1`,
- `E_a=2 a H^{11}`,
- `E_b=2 b(H^{22}+H^{33})`.

Required per lane:
- valid Lorentz/inverse controls;
- all three exact target components `>1e-10` in absolute value;
- corrected maximum relative residual `<=5e-4`;
- corrected final-step change `<=2e-4`;
- historical `+2D` negative-control relative residual `>=1e-2`.

### Stream B — 4 held-out spherical exact reduced-EL profiles
Use the generic exact radial-gauge-unfixed Iter049 Euler–Lagrange authority, but on four new polynomial profiles not used in the Iter049 production matrix:

B0: `F=1+r/6+r^2/25`, `N=1+r^2/8`, `S=1+r+r^2/13`, `r=5/4`.

B1: `F=3/2+r^2/10`, `N=1+r/7+r^2/30`, `S=2+r/3+r^3/40`, `r=4/3`.

B2: `F=1+r/4+r^3/60`, `N=4/3+r^2/9`, `S=1+r/2+r^2/7`, `r=3/4`.

B3: `F=2+r/8+r^2/12`, `N=1+r/5`, `S=3/2+r+r^3/50`, `r=6/5`.

At `theta=pi/2`, map the 4D coefficient to exact spherical reduced coefficients by
- `E_F=-2 F H^{tt}`,
- `E_N=2 N H^{rr}`,
- `E_S=2 S(H^{θθ}+H^{φφ})`.

Required per lane:
- Lorentz/inverse controls valid on all derivative stencils;
- exact targets nonzero (`min abs >1e-10`);
- corrected maximum relative residual `<=1e-3`;
- corrected final-step change `<=4e-4`;
- historical `+2D` negative-control residual `>=1e-2`.

This is deliberately a different symmetry reduction from D1 and no D1 fitted coefficient enters the calculation.

### Stream C — 4 fresh generic 4D covariance/symmetry witnesses
Use fresh deterministic polynomial metric seeds `[121003,121211,121417,121621]` and determinant-one constant Lorentz maps. Recompute `H_D2` independently in both frames.

Required:
- valid Lorentz/inverse controls;
- nonzero `||H_D2||>1e-7`;
- symmetry residual `<=3e-7`;
- final-step change `<=2e-3`;
- full density-coefficient covariance residual `<=1e-3`.

### Stream D — 4 fresh conformally-flat FLRW null controls
Use four nontrivial spatially-flat isotropic polynomial scale factors distinct from G51C Stream C. Required:
- nonzero Riemann norm `>1e-6`;
- `|I3|<=2e-10`;
- `||P||<=3e-9`;
- `||H_D2||<=2e-7`;
- valid Lorentz/inverse controls.

## Frozen numerical derivative schedule
Reuse the independently closed G51B2/G51C central derivative schedule
`h=[1e-3,5e-4,2.5e-4]`
and existing complex-step algebraic derivatives. No production fitting is permitted.

## Aggregate classification
Full D2 PASS requires all 20 unique scientific lanes, all controls valid, and 20/20 lane PASS:

`PASS_DIAGNOSTIC_G51C_D2_INDEPENDENT_SIGN_AND_HELDOUT_VALIDATION`

A valid mismatch is

`SCIENTIFIC_FAIL_G51C_D2_SIGN_OR_HELDOUT_VALIDATION`.

Missing/invalid controls or implementation failure is

`ITER051C_D2_CONTROL_OR_IMPLEMENTATION_INVALID`.

## Interpretation lock
Even full D2 PASS does **not** establish the full covariant six-derivative EOM. It only independently supports the analytically derived sign/order convention and authorizes construction of a separately preregistered replacement full-EOM gate (`G51C-R1`) with no threshold reuse or retroactive rewriting. It does not determine `c6`, authorize `beta=1`, establish theory correctness, prove absolute energy positivity or quantum unitarity, or constitute experimental confirmation. `theory_established_pct` remains 0.
