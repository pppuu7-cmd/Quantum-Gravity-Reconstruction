# Iter057F3 preregistration — full-tensor-normalized G3-origin Weyl3 degree-two extraction

Date: 2026-09-15
Gate: `ITER057F3-G3-ORIGIN-WEYL3-DEGREE2-BLOCK-FULL-TENSOR-NORMALIZATION`

## Historical / timing lock

This gate is frozen after:

- historical Iter057F basis lanes 8 and 7 exposed two independent control-definition issues;
- the exact representation theorem `I3_full = 8 tr(W^3)` was derived and committed as `725c1e180641e05bc5701ccbb193bd34168e8dd2`;
- the old Iter057G trace target and Iter057F2 controls were explicitly invalidated pre-output by `57f4a2a478b3bf909a4091b089cd84bc04701c15` and `00462929e746331767bdf3445ad3c6e9e10ee46c`.

Iter057F and Iter057F2 remain immutable under their own contracts. This successor does not reclassify them.

No Iter057F3 numerical output exists at freeze.

## Scientific object — unchanged extraction panel

Reuse exactly the frozen source/computation object from Iter057F/F2:

- source-owned G3/H0 origin;
- global `(-,+,+,+)` representation of the same source metric;
- `kappa=0.08=2/25`;
- null covector `k=(1,1,0,0)`;
- ten symmetric metric basis inputs in Iter054C order;
- perturbation `g_ab=gbar_ab+epsilon H_j,ab cos(s k.x)`;
- full corrected Euler evaluator `A+I-2 sqrt(-g)D5`;
- training frequencies `s=0,1,2`;
- held-out `s=3/2`;
- epsilon panel `2e-4,1e-4`;
- five-point double-divergence stencil panel `h_D=1e-3,5e-4`;
- exact even extraction

  `R(s)=L0+s^2 L2+s^4 L4`,

  `L4=[R(2)-R(0)-4(R(1)-R(0))]/12`,

  `L2=R(1)-R(0)-L4`.

No frequency, epsilon, stencil, source, covector or basis changes are allowed.

## Exact full-tensor normalization objects

Construct the same exact Iter054C six-bivector `Q` matrix from the G3/H0 background and frozen k.

The exact bridge theorem gives the full-EOM fourth-order target

**`Q_full = 8 Q_Iter054C`.**

The exact full-EOM trace-Ward target is

**`T_full = 8 T_bivector = (-48,96,0,0,-48,0,0,-144,0,144)/625`**

in basis order `(00,01,02,03,11,12,13,22,23,33)`.

Both targets are fixed before numerical production. No fitted sign/scale is permitted.

The exact zero-column pattern of `Q_full` is the same as Q and must be exactly `[8]`.

## Frozen performance-equivalence control

A memoized five-point evaluator may be used only if, on a frozen G3 source instance, it reproduces the original `assemble_minus5` output with

- relative Frobenius residual <= `1e-12`;
- max absolute residual <= `1e-12`.

Failure blocks scientific lanes.

## Frozen lane controls

A. Source/signature validity identical to Iter057F.

B. `L2` amplitude convergence: finest-stencil `epsilon=2e-4 -> 1e-4` relative change <= `5e-3` for all lanes.

C. `L2` stencil convergence: finest-epsilon `h_D=1e-3 -> 5e-4` relative change <= `1e-2` for all lanes.

D. Held-out frequency: at finest extraction,

`R(3/2)_pred=L0+(9/4)L2+(81/16)L4`

must match direct full-EOM response within relative Frobenius residual <= `3e-3`.

E. Nonzero full-tensor `L4` columns (`j != 8`):

- direct no-fit finest column residual against `Q_full[:,j]` <= `2e-2`;
- `L4` amplitude relative change <= `5e-3`;
- `L4` stencil relative change <= `1e-2`.

F. Exact-null `L4` column `j=8`: for every extraction point in the 2x2 epsilon/stencil panel require

`||Bcol_8||_2 / ||Q_full||_F <= 2e-2`.

No relative-to-zero amplitude/stencil predicate is imposed.

G. Aggregate full-tensor `L4`:

- bilinear symmetry residual <= `2e-3`;
- direct exact relative residual `||B4-Q_full||/||Q_full|| <= 2e-2`.

H. Exact full-tensor trace-Ward identity. At finest extraction, for every lane require

`abs(trace_eta(L2_j)-T_full,j) / max(abs(T_full,j), ||L2_j||_F, 1e-10) <= 1e-2`.

Aggregate trace-vector residual against `T_full` must be <= `5e-3`.

I. The prior isolated `L2[k_(a xi_b)]=0` control is deliberately excluded: pre-output methodology audit `e3d9826...` showed it is not a valid standalone curved-background subprincipal Ward identity.

J. Report, but do not optimize for:

- `L2` Frobenius norm;
- singular values/numerical rank at frozen tolerance `max(sigma_max*1e-8,1e-12)`;
- trace vector;
- image rank/singular values on the two-dimensional non-gauge Einstein null complement.

No desired `L2` rank/sign is a PASS predicate.

## Frozen classifications

Maximum PASS if performance equivalence and all A-H controls pass:

`PASS_SCOPED_ITER057F3_G3_ORIGIN_WEYL3_K2_BLOCK_EXTRACTED_WITH_EXACT_FULL_TENSOR_NORMALIZATION`.

INVALID if any cache/source/convergence/held-out/full-tensor-L4/trace-Ward control fails:

`INVALID_ITER057F3_FULL_EOM_EXTRACTION_OR_FULL_TENSOR_CONTROL`.

There is no scientific FAIL tied to a preferred measured `L2` rank/sign.

## Interpretation ceiling

This remains a finite-precision local extraction at one source-owned background point and one null covector. It does not establish the full characteristic variety, strong/symmetric hyperbolicity, physical cone splitting, ghost content, stability, energy, treatment selection, unitarity, UV completion, experiment, or QGR correctness.

`c6` remains symbolic/unfixed; `beta=1` unauthorized; theory established remains 0%.