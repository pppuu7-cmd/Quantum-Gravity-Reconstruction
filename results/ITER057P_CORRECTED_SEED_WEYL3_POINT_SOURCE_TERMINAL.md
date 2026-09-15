# Iter057P terminal result — corrected Einstein-seed Weyl3 point-source reset

Date: 2026-09-15
Gate: `ITER057P-CORRECTED-SEED-WEYL3-POINT-SOURCE-RESET`
Preregistration: `4c79629d38d2de28385fa059365b1b50e8c165cf`
Implementation: `85ab7559e08dd7806db803c8d98fcebe303212c5`
Workflow head: `d731980784137d78928ba63da37b276475f1796d`
Actions run: `34955879708`
Job: `104337691800`
Artifact: `10391063819` (`iter057p-corrected-seed-weyl3-point-source`)
Artifact digest: `sha256:cb25ac2c9bfd0512cb9f6acb1d808c6c38c340636960068291dd0c96b402dc2a`

## Terminal classification

**`PASS_SCOPED_ITER057P_CORRECTED_EINSTEIN_SEED_WEYL3_POINT_SOURCE_EXACTLY_RESET__SECOND_SOURCE_JET_REQUIRES_SEXTIC_SEED`**

This is exactly the prospectively frozen maximum scoped PASS.

## Exact corrected-seed source

The Iter057O quartic seed preserves the origin metric and Riemann/Weyl tensor, hence the algebraic Weyl-cubic scalar remains

`I3(0)=96 kappa^3`.

The algebraic insertion is also unchanged at the origin:

`B^{ii}/kappa^3=(-72,72,72,72)`.

However the quartic seed changes the curvature second jet and therefore the double-divergence sector. The exact new values are

`D^{ii}(0)/kappa^3=(132,180,180,-228)`.

Using the authoritative Iter056X formula

`E_W3^{ab}=(1/2)g^{ab}I3-B^{ab}-2D^{ab}`,

the corrected lower-index point source is

**`E_W3,ab(0)/kappa^3 = diag(-240,-384,-384,432)`**

with all off-diagonal components exactly zero.

At the frozen `kappa=2/25` this is

- `E_00=-384/3125`;
- `E_11=E_22=-3072/15625`;
- `E_33=3456/15625`.

## Comparison with old G3/H0 source

The historical uncompleted G3/H0 point source was

`E_old/kappa^3=diag(48,-208,-208,368)`.

The corrected-seed shift is therefore

`Delta E/kappa^3=diag(-288,-176,-176,64)`.

Thus every nonzero diagonal component changes, despite the pointwise Riemann/Weyl tensor itself being preserved.

This is the expected fourth-derivative sensitivity of the Weyl3 Euler tensor and directly confirms the Iter057O source-reset lock.

## Exact controls

Every frozen control passed:

- inverse identity through the needed degree;
- corrected seed Ricci/scalar zero through coordinate degree two;
- `P.R=3I3` at the origin;
- symmetry of `E_W3_ab`;
- exact trace Ward identity `g^{ab}E_W3_ab=-I3`;
- full-inversion parity of the seed;
- vanishing first covariant derivatives of the Euler source at the origin from even parity plus `Gamma(0)=0`.

No numerical tolerance or finite difference is used.

## Consequence

The next `O(c6)` quadratic correction must use

`S_ab=-E_W3,ab[g_seed]/A_E`

with the corrected source above. The old Iter057L/M G3-source coefficients remain valid only under their historical off-shell/fixed-G3 scopes and must not be transplanted to the corrected Einstein seed.

The corrected-seed **second coordinate jet** of `E_W3` is not yet authoritative: it can depend on sixth metric derivatives. Iter057Q is therefore the required parallel zeroth-order sextic seed completion before that second source jet is reconstructed.

## Scope ceiling

This PASS supplies only the corrected-seed Weyl3 point source. It does not establish the source second jet, an open-neighborhood `O(c6)` correction, an all-orders Ricci-flat seed, physical characteristics, hyperbolicity, ghosts, stability, unitarity, regulator removal, UV completion, experiment, or QGR correctness.

`c6` remains symbolic/unfixed; `beta=1` remains unauthorized; theory established remains `0%`.