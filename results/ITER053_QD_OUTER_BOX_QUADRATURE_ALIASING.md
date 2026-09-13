# Iter053-QD — outer-box quadrature aliasing diagnostic

Gate: `ITER053-QD-COMPACT-SUPPORT-QUADRATURE-CONDITIONING`

Authority:
- preregistration: `8625318f69e3104b4dc67ada0f716394fb775de5`
- implementation: `49fa54a281ad4741e45fccf5de6078fc85882a36`
- aggregate: `a6e62f43e22c777f2ea67ef7aa7fbe921999da6e`
- workflow: `76e5b85f76249a3111edd48221d056829c7e08df`
- production head: `32c1da71923a4e023183f78d9bb8205cb99ae19f`
- run: `34770383463`
- aggregate job: `103758873038`
- summary artifact: `10321557741`
- digest: `sha256:001adec3865c9d0083e842fccbc99676b914eeed6bb5e862c07008d0f1570c6b`

Classification: **`PASS_DIAGNOSTIC_ITER053_OUTER_BOX_QUADRATURE_ALIASING_CONFIRMED`**.

All A4+B2+C2 = 8/8 diagnostic lanes were found, control-valid and confirmed the preregistered aliasing hypothesis.

Key aggregate facts:
- outer-box GL3 nonzero compact-support tensor nodes: exactly **1**;
- outer-box GL4 nonzero compact-support tensor nodes: exactly **16**;
- minimum pure-bump error improvement from outer-box GL4 to support-domain GL5: `1.2101080028298477e14`;
- worst direct outer GL3->GL4 change: `1.095706792000514`.

Representative A0 makes the mechanism explicit. On the outer box, direct-action quadrature changed from `5.782863658152479e-4` (GL3, one nonzero node) to `-4.7170435918646406e-5` (GL4, 16 nonzero nodes) to `8.18705064009736e-6` (GL5, 81 nonzero nodes). On the exact support cube, all tensor nodes are informative; the pure polynomial bump integral is exact to machine precision already at GL5. However the direct action integral itself still changed by `0.14809207057851922` from support GL4 to GL5 for A0, and the aggregate worst support GL4->GL5 change was larger. Therefore this diagnostic identifies the outer-box aliasing defect but does **not** yet establish a converged support-domain scientific quadrature.

Interpretation lock: numerical diagnostic only. It does not reclassify Iter053, does not test the H5 integrated identity, does not fix `c6`, and does not establish a global theorem or QGR correctness. A separate QD2 direct-action convergence diagnostic was prospectively preregistered before selecting any replacement H5 quadrature.
