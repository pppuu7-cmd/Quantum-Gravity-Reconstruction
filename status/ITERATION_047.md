# QGR Iter047 — exact Weyl^3 curvature-class activation map

Date: 2026-09-13
Status: PREREGISTERED BEFORE IMPLEMENTATION / PRODUCTION

## Scientific question

The QGR program has already isolated the leading six-derivative curvature operator as the cubic Weyl invariant, with coefficient `c6` still unfixed. Iter046 tests an exact nonlinear pp-wave sector of the two-derivative action, but a type-N radiative geometry can be algebraically blind to scalar Weyl invariants. The present gate asks a different, independent question:

> On exact metric geometries belonging to distinct curvature classes, where is the QGR `Weyl^3` operator exactly inactive and where is it exactly nonzero, and does its curvature scaling follow the frozen cubic prediction without fitting `c6`?

This is an **operator-activation / invariant gate**, not the full Euler-Lagrange equation of the six-derivative theory. A PASS must not be reported as a corrected black-hole solution, generic nonlinear stability, or a determination of `c6`.

## Frozen invariant convention

In four dimensions construct the metric Weyl tensor directly from Riemann/Ricci/scalar curvature,

`C_abcd = R_abcd - 1/2 (g_ac R_bd - g_ad R_bc - g_bc R_ad + g_bd R_ac) + R/6 (g_ac g_bd - g_ad g_bc)`.

Raise the final pair and define

- `W2 = C_ab^{ cd} C_cd^{ ab}`;
- `W3 = C_ab^{ cd} C_cd^{ ef} C_ef^{ ab}`.

The QGR correction density is proportional to `c6 * W3`; `c6` remains symbolic/unfixed throughout this gate.

## Frozen production matrix — 24 scientific lanes

### Stream A — type-N pp-wave blindness (6 lanes)
Use six nontrivial exact harmonic pp-wave profiles drawn from the already frozen polynomial profile family, at finite nonzero amplitudes.

Required per lane:
- metric nondegenerate;
- full Riemann tensor nonzero;
- Ricci tensor and scalar curvature exactly zero;
- `W2 == 0` exactly;
- `W3 == 0` exactly.

Interpretation: the scalar cubic Weyl operator is blind on these type-N witnesses even though the spacetime is curved.

### Stream B — Schwarzschild/Petrov-D activation and scaling (6 lanes)
Use exact Schwarzschild metrics with frozen positive rational masses and evaluate the symbolic invariants before any numerical substitution.

Required per lane:
- Ricci tensor and scalar curvature exactly zero;
- exact `W2 = 48 M^2/r^6`;
- exact `W3 = 96 M^3/r^9` under the frozen contraction convention;
- nonzero `W3` for `M != 0`;
- the lane's frozen mass/radius substitutions agree exactly with cubic mass scaling and ninth-power radial scaling.

No claim is made that Schwarzschild remains a solution after adding nonzero `c6`.

### Stream C — Kasner Ricci-flat anisotropic activation (6 lanes)
Use permutations of the exact vacuum Kasner exponents `(-1/3, 2/3, 2/3)` and frozen rational positive times.

Required per lane:
- Ricci tensor and scalar curvature exactly zero;
- `W2 != 0` and `W3 != 0` at the frozen witness;
- invariants obey exact dimensional time scaling `W2 ~ t^-4`, `W3 ~ t^-6` between the lane's two frozen times.

This is independent of static spherical symmetry.

### Stream D — conformally-flat control (6 lanes)
Use spatially flat FLRW metrics with six frozen nontrivial scale factors (power-law / low-degree polynomial witnesses) chosen so that Riemann curvature is nonzero at the frozen evaluation point.

Required per lane:
- metric nondegenerate at the witness;
- Riemann tensor nonzero;
- Weyl tensor exactly zero;
- `W2 == 0` and `W3 == 0` exactly.

This control ensures nonzero curvature by itself is not being mistaken for Weyl^3 activation.

## Frozen aggregate classifier

Expected lanes: 24 = A6 + B6 + C6 + D6.

- Full PASS iff all 24 files are present, every control is valid, and every lane passes its frozen exact criterion:
  `PASS_SCOPED_EXACT_WEYL3_CURVATURE_CLASS_ACTIVATION_MAP`
- Some scientific criteria fail with valid implementation controls:
  `PARTIAL_SCOPED_WEYL3_CURVATURE_CLASS_ACTIVATION_MAP`
- Broad scientific failure:
  `FAIL_SCOPED_WEYL3_CURVATURE_CLASS_ACTIVATION_MAP`
- Missing lanes / invalid geometry / implementation-control failure:
  `ITER047_CONTROL_OR_IMPLEMENTATION_INVALID`

Thresholds and analytic targets are frozen by this preregistration and must not be weakened after production output is inspected.

## Interpretation locks

Even a full PASS establishes only an exact metric-level activation map of the already-selected cubic Weyl operator. It does **not**:
- fix `c6`;
- prove the six-derivative Euler-Lagrange correction is nonzero on every Weyl-active metric;
- establish a corrected Schwarzschild/Kasner solution;
- establish strong-field stability, renormalizability, quantum unitarity, or experimental confirmation;
- raise `theory established` above 0%.

Iter047 is scientifically independent of the terminal classification of Iter046 and may execute in parallel with the Iter046 aggregate barrier.
