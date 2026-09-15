# Iter057V preproduction operator/order audit

Date: 2026-09-15
Preregistration: `d6f6cd791e101e6492a33c43d31e8886b2875dd9`.
Implementation: `a5e27a662ce78720f203d27dff5cf03b2853bbf4`.
Production head: `a188315615c1b2fa17987758af534334c5f76051`.

This note is recorded while production is running and before its scientific result is consumed. It changes no decision criterion.

## 1. Why the new Q6 principal block is the universal 574 x 840 complex

The new trace-reversed response jet is pure degree six. At field degree four, two derivatives reduce it to degree four. Any multiplication by a non-flat background correction begins at coordinate degree two and therefore contributes only at degree six or above. Connection corrections begin at degree one and multiply a first derivative of Q6 of degree five, again contributing at degree six or above.

Therefore the Q6 contribution at the frozen target orders is exactly the flat principal block:

- de Donder degree five: ordinary divergence of Q6;
- field degree four: `-1/2 Box Q6` in the trace-reversed de Donder reduction.

This is the same source-independent polynomial complex already exact-certified in Iter057Q: 840 columns, 574 rows, rank 494, left-nullity 80 and nullity 346. These numbers do not imply affine consistency for Iter057V.

## 2. Where the genuinely new curved information lives

The fixed Iter057S Q2/Q4 response does couple to the canonical curved background at target degree four/five:

- inverse-metric degree two/four times derivatives of Q2/Q4;
- connection degree one/three times Q2/Q4 derivatives;
- curvature degree zero/two times raised Q2/Q4 in the reduced Einstein operator.

Those terms are recomputed from the canonical background and appear only in the affine RHS. Reusing the old Iter057S RHS would therefore be invalid.

## 3. Background-jet ceiling for the response operator

For `qbar = Q2 + Q4 + Q6`, the covariant response through field degree four and gauge degree five depends on the zeroth-order metric only through its quartic jet:

- a degree-six background metric term produces connection degree five and curvature degree four; coupled to the minimum Q2 response these first enter beyond the requested response order;
- the pure degree-eight Iter057T correction enters still later.

Thus truncating the *operator evaluation* to the canonical Iter057T four-jet is exact at the frozen V target order. This does not discard or mutate the Iter057T seed: its higher jets remain essential for the Iter057U source degree four and are already consumed there. The implementation separately checks the frozen Iter057T R8 provenance/pure-degree-eight property.

## 4. Compatibility interpretation

The complete 80-dimensional left-null space is the discrete homogeneous Bianchi/de Donder compatibility complex. For the actual V affine RHS:

- all 80 contractions zero and `rank([M|r])=494` means the unrestricted Q6 continuation is locally compatible at this finite order;
- any exact nonzero contraction (or augmented-rank increase) is a preregistered scientific obstruction for the unrestricted Q6 response, not an ansatz artifact;
- numerical near-zero is never accepted.

The production run must still construct a particular exact Q6 and pass independent unreduced covariant substitution before PASS.

All scope/claim locks remain unchanged: `c6` symbolic/unfixed, `beta=1` unauthorized, theory established `0%`.
