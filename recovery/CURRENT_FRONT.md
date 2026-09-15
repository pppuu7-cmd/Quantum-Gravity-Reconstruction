# QGR Current Research Front

Updated: 2026-09-15
Primary active front: `ITER057R / CORRECTED EINSTEIN-SEED WEYL3 SECOND SOURCE JET`
Project phase: `ONSHELL BACKGROUND SEED COMPLETION AND WEYL3 RESET PROGRAMME`

## Canonical claim locks

- Repository infrastructure readiness: **100%**.
- Candidate-program roadmap readiness: **99% internal bookkeeping only**, not probability of correctness.
- Theory established: **0%**.
- No experimental confirmation.
- `beta=1`: not authorized.
- `c6`: symbolic/unfixed; running/fitting not authorized.
- No physical Weyl3 treatment selector, strong hyperbolicity, ghost/stability, quantum unitarity, regulator removal or UV completion is established.
- Finite local Taylor/symbol certificates are not open-neighborhood/global theorems.

## Consumed seed/background authority

### Iter057N — fixed G3 seed FAIL

Terminal result `32c6f1b077d72a616f52dc41bbef8a39ba0cf1af` proves the unchanged exact G3/H0 seed has a nonzero `c6^0` Einstein residual at coordinate degree two. A simple exact witness is

`partial_x^2 G_00(0)/kappa^2 = 6`.

This rejects only the unchanged G3 metric as a neighborhood zeroth-order seed.

### Iter057O — quartic Einstein-seed completion PASS

Terminal `679a3d73d589fc9161bdf2209f25bb4b7c785fd6`, Actions run `34955436259`.

An unrestricted quartic correction with 21 nonzero canonical-pivot coefficients cancels the full quadratic Einstein residual while preserving the origin metric, connection and curvature. Exact matrix rank `164`, nullity `186`, all 16 Bianchi compatibilities zero, and direct nonlinear `G_ab=0` through coordinate degree two.

### Iter057P — corrected-seed Weyl3 point-source reset PASS

Terminal `3c8e8d54cf7c4685945f3d30284544bbba75c338`, Actions run `34955879708`.

The quartic seed preserves `I3(0)/kappa^3=96` but changes the derivative sector and hence the Weyl3 Euler point source to

`E_W3,ab(0)/kappa^3 = diag(-240,-384,-384,432)`.

The old uncompleted-G3 point source must not be reused.

### Iter057Q — sextic Einstein-seed completion PASS

Preregistration `afc9098e6de828e8647aad5b1d8316b29f0b61a0`.
Implementation `d70dc4e53e1e3ae5db95162978c9e89c618f38ba`.
Terminal result `c4f1c5c01205a6991e7215e3824111e1f36d1436`.
Actions run `34956377793`, job `104339311005`.
Artifact `10391933651`, digest `sha256:8b1a0afe28bbb71de0b6413c24193f8dfc3dcadbb26b78d3f008f11b2508155d`.

Classification:

`PASS_SCOPED_ITER057Q_SEXTIC_EINSTEIN_SEED_COMPLETES_THROUGH_QUARTIC_EINSTEIN_ORDER__WEYL3_SECOND_SOURCE_JET_CAN_NOW_BE_RECOMPUTED`.

Exact results:

- full unrestricted sextic space: 840 coefficients;
- exact matrix `574 x 840`, nnz `2296`;
- rank `494`, augmented rank `494`;
- nullity `346`, left-nullity `80`;
- all 80 canonical Bianchi compatibility contractions exactly zero;
- one canonical particular sextic correction with 69 nonzero normalized coefficients;
- correction is pure degree six and preserves all seed derivatives through order five;
- direct nonlinear Ricci/scalar/Einstein tensors vanish through coordinate degree four.

Therefore the canonical seed six-jet is now fixed and is sufficient to define the corrected-seed Weyl3 source through coordinate degree two.

## Active Iter057R gate

Preregistration: `582ff376a59458270b7074d5470dedfba85896af`.
Gate: `ITER057R-CORRECTED-SEED-WEYL3-SECOND-SOURCE-JET`.
Corrected implementation: `3db68ebc21b5bac124c3a7206d7a74d87645c142`.
Workflow head: `cc41b51e6ae0601140bdc699e9c7b41e5fd1560d`.
Actions run: `34956884376`.
Terminal classification: none yet.

The evaluator replays the exact Iter057Q canonical sextic seed and performs full four-dimensional exact Fraction polynomial algebra:

`metric degree 6 -> curvature/Weyl degree 4 -> P degree 4 -> D,E_W3 degree 2`.

Frozen controls include:

- Iter057Q seed replay;
- inverse identity through the needed degree;
- seed Ricci/scalar zero through coordinate degree four;
- `P.R=3 I3` through degree four;
- Euler-tensor symmetry;
- trace Ward through degree two;
- Noether divergence through degree one;
- even-parity/first-derivative control;
- exact replay of the Iter057P point source.

The output must expose the complete normalized

`Shat_ab=A_E S_ab=-E_W3_ab`

at order zero and coordinate degree two, including any time-containing/off-diagonal coefficients.

## Next bounded step

Consume Actions run `34956884376` only after all exact controls pass.

If Iter057R passes, the next constructor must **restart** the `O(c6)` quadratic/quartic correction on the Einstein-completed seed. It may reuse the universal polynomial-complex machinery of Iter057L/M, but not the old off-shell G3 source coefficients or background degree-two operator RHS.

No fixed/fitted `c6`, old-source substitution, restricted symmetry ansatz, numerical exact-zero decision, physical characteristic inference, or all-orders neighborhood claim is allowed.
