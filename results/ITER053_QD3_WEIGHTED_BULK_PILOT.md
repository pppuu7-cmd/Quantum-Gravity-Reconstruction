# Iter053-QD3 — Weighted Bulk Gauss–Jacobi Pilot

Date: 2026-09-13
Gate: `ITER053-QD3-WEIGHTED-BULK-GAUSS-JACOBI-PILOT`
Classification: **`PASS_DIAGNOSTIC_ITER053_WEIGHTED_GJ3_BULK_PILOT_PROMISING`**

## Authority
- Preregistration commit: `b12b8f1fbf8605a17d7b35191812323b1c61dde8`
- Implementation commit: `471781570e1216c455e490681493e9e41ce078cd`
- Workflow commit: `3c8e5640176ebe96abc826de7b7986728d61bfc3`
- Production head: `ec14bd4c5ec7ebe8523bb7c06e789d20fdcef89f`
- Run: `34770675902`
- Job: `103759575844`
- Artifact: `10322517083`
- Artifact digest: `sha256:5d7d7d616660a3843a097c4cd23305ee473df16c14c8b323015284926dd89bcf`

## Frozen result
The exact bump-weighted tensor Gauss–Jacobi pilot used `h=B p` with weight `(1-u^2)^4` and compared the expensive H5 bulk response against independently converged support-domain direct action variation.

- GJ2 bulk: `9.065790207702158e-06` on 16 weighted nodes.
- GJ3 bulk: `9.066610617407998e-06` on 81 weighted nodes.
- GJ2→GJ3 bulk relative change: `9.048692399614629e-05`.
- Direct GL7: `9.066614167699168e-06`.
- Direct GL8: `9.066613706546225e-06`.
- Direct GL7→GL8 relative change: `5.086275142547632e-08`.
- GJ3 bulk vs direct GL8 relative residual: `3.407157652190216e-07`.
- Historical wrong-sign GJ3 vs direct GL8 relative residual: `1.944220429443305`.
- Signature controls: valid.
- Max inverse residual: `4.440892098500626e-16` for weighted bulk and `5.551115123125783e-16` for direct GL7/GL8.

The preregistered `promising` condition is satisfied. QD3M independently established that the Gauss–Jacobi moments/normalization are exact to the frozen numerical tolerance, so the weighted result is not explained by a weight/Jacobian-normalization defect.

## Scientific interpretation
This is **diagnostic numerical evidence only**. It shows that the previous outer-box GL3/GL4 failure is consistent with quadrature/support aliasing and that the prospectively defined weighted H5 integration strategy is numerically promising on the A0 pilot.

It does **not** reclassify the original Iter053 production, does not establish the full A4+B2+C2 compact-support variational identity, does not fix `c6`, and does not establish the QGR theory. No evidence is pooled post hoc into the original frozen classifier.

## Authorization consequence
A fresh prospectively preregistered weighted-H5 scientific replacement gate is now scientifically justified. That gate must freeze its panel, seeds/controls, weighted quadrature orders, convergence thresholds, H5=`A+I-2sqrt(-g)D5`, covariance tests, null controls, and interpretation before production. The still-running fresh retry `34769958632` remains independent authority under the original GL3/GL4 contract and must be consumed separately when terminal.
