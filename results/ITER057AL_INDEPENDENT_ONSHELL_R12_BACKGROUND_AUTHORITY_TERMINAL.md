# Iter057AL terminal result — independent on-shell R12 background authority

Date: 2026-09-16
Gate: `ITER057AL-INDEPENDENT-ONSHELL-R12-BACKGROUND-AUTHORITY`
Preregistration: `c712f5034963048a8ab9a4ad812a47000a89be47`
Frozen seed manifest: `eabf19dbf32463127bd574032742a116e18267a6`
Manifest payload SHA256: `1e58ef49d36ac75efdd066f6b55ce2e48d9d8bce0307a9283ebe4483b026888f`
Generic exact engine: `1a0ca23cc4314cf525b57fc116b57dd534f34bad`
Candidate solver: `23861f16aef96dd641ec88cb11da0650cd2328c2`
Independent validator: `567dc13b83d3d82d4766393f4b76d827c351f76a`
Production head: `84652b0610b437332db6ce403578372a665802bc`
Actions run: `35150321723`
Durable aggregate authority: `983b6be90004077a76b3476c9854f5eba4542399`

## Terminal classification

**`PASS_SCOPED_ITER057AL_INDEPENDENT_ONSHELL_R12_BACKGROUND_AUTHORITY_ESTABLISHED`**

## Prospectively frozen seed rule and independence

Before any nonlinear completion outcome, the finite exact family

`q_r = kappa*(r*x^2 + (2-r)*y^2 - 2*z^2)`

was frozen at `r = 1/2, 1/3, 1/4`.  Each seed is static and spatially harmonic exactly, so the linear trace-reversed G2 datum satisfies the same flat de Donder and linear vacuum equations as the canonical programme seed.

Independence from the canonical AF seed and from the other candidates was frozen through

`J = (tr E^3)^2 / (tr E^2)^3`, `E_ij = R_0i0j(0)`,

which is invariant under spatial orthogonal relabel/rotation and nonzero overall rescaling.  The exact values are

- canonical AF reference `r=1`: `J=1/6`;
- `AL-R1-2`: `J=162/2197`;
- `AL-R1-3`: `J=2025/59582`;
- `AL-R1-4`: `J=392/20577`.

All four values are distinct.

## Exact nonlinear completion

All three frozen candidates completed through pure trace-reversed degrees `R4,R6,R8,R10,R12` using exact rational arithmetic.  For every candidate the exact principal systems and free-zero particulars gave:

| layer | shape | rank = augmented rank | left nullity | nullity | particular nonzero | compatibility nonzero |
|---|---:|---:|---:|---:|---:|---:|
| R4 | 180 x 350 | 164 | 16 | 186 | 21 | 0 |
| R6 | 574 x 840 | 494 | 80 | 346 | 69 | 0 |
| R8 | 1320 x 1650 | 1096 | 224 | 554 | 153 | 0 |
| R10 | 2530 x 2860 | 2050 | 480 | 810 | 283 | 0 |
| R12 | 4316 x 4550 | 3436 | 880 | 1114 | 469 | 0 |

For every candidate, independent final replay gives exact inverse identity, Ricci/scalar/Einstein zero through coordinate degree 10, and flat de Donder zero through degree 11.

## Production evidence

Run `35150321723` completed all matrix jobs and the independent validator successfully.

- `AL-R1-2`: job `104976691359`, artifact `10468622720`, digest `sha256:5228156631499dc69f6770ac56a44c9fed8410e24688728d541540c2d1cdef67`, scientific payload SHA256 `264a23631367dae8fb5e77d133f733428cfef9e673a4cd632380d484fde205e8`.
- `AL-R1-3`: job `104976691419`, artifact `10468837671`, digest `sha256:53ec55e0f99dec4eac538ac369136bc8808f7a6855d01f68d7e48dc4db029d45`, scientific payload SHA256 `6fdf87a15d783e601c02c63b49cfd55a45b83eb258d5decf4ca1e46b5ad0141a`.
- `AL-R1-4`: job `104976691209`, artifact `10468978252`, digest `sha256:93009fefb07e858cd50f335a96210d8b3405ff4cfc94dce6d50b6d7ebc809cdf`, scientific payload SHA256 `5484179f3d86414918d0aed05e4c5a63dca802f4f8f1631c8259e8bf576c9fc5`.
- independent validator: job `104976989991`, artifact `10468263262`, digest `sha256:4251ac1295579c7a7985e199dbb9d35e5183891e0725c61a33b9bd0195c50f2c`, scientific payload SHA256 `14829afb3c694939a769eb0c6f64b334e019271d186bac3e91197ee6e7c0b86f`.

A separate local consumer recomputed all four canonical JSON scientific payload hashes and verified all candidate controls, all five exact layer ranks/augmented ranks/compatibility counts, and all validator controls directly from the raw artifacts.

## Held-out firewall

The held-out rule was frozen before nonlinear completion: among surviving candidates, the lexicographically first seed serialization is construction/training and the lexicographically last is held out.  Since all three candidates survive:

- construction/training seed: **`AL-R1-2`**;
- additional independent authority: **`AL-R1-3`**;
- held-out seed: **`AL-R1-4`**.

No R14 affine residual, `O0`, obstruction map, dual witness, obstruction sector or cross-background comparison quantity was computed or consumed anywhere in Iter057AL.

## Scientific consequence and ceiling

For the first time in this programme there are multiple exact, source-faithful, on-shell local R12 background authorities that are inequivalent to the original AF seed by a frozen curvature-shape invariant.  This removes the formulation blocker that prevented a genuine held-out cross-background obstruction test.

This does **not** say that the AF obstruction persists on any new background.  It establishes only the prerequisite independent finite local backgrounds.  `c6` remains symbolic/unfixed, `beta=1` remains unauthorized, finite local Taylor data are not a global/all-orders theorem, and theory established remains `0%`.

## Next gate

The next gate is prospectively frozen held-out no-refit R14 obstruction transport on `AL-R1-4`.  It must compare only structural exact quantities fixed before seeing held-out R14 data: compatibility obstruction existence, exact rank/augmented-rank defect, obstruction-quotient dimension, and existence of a normalized exact dual witness.  No coefficient equality, parity/S3 support or generator matching is required unless independently justified before outcome.
