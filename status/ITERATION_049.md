# QGR Iter049 — spherically reduced Weyl^3 variational response

Date: 2026-09-13
Status: PREREGISTERED BEFORE IMPLEMENTATION / PRODUCTION

## Scientific question

Iter048 showed that the coefficient of the still-unfixed `c6` in `sqrt(-g) Weyl^3` gives a nonzero generalized variational response in a lapse-retaining axisymmetric Bianchi-I reduction. That is a genuine dynamical result, but it is one symmetry class.

Iter049 asks an independent question:

> If the `Weyl^3` term is varied in a radial-gauge-unfixed static spherically symmetric reduction, before imposing Schwarzschild/Petrov-D, is its reduced Euler-Lagrange response nonzero on Schwarzschild, zero on conformally-flat constant-curvature controls, and consistent with exact radial-reparameterization covariance?

This is a second **symmetry-reduced variational gate**. Even a full PASS is not the complete four-dimensional covariant `Weyl^3` Euler-Lagrange tensor.

`c6` remains symbolic/unfixed; production computes only the coefficient multiplying it.

## Frozen generic spherical reduction

Use coordinates `(t,r,theta,phi)` and retain three independent radial functions:

`ds^2 = -F(r)^2 dt^2 + N(r)^2 dr^2 + S(r)^2 (dtheta^2 + sin(theta)^2 dphi^2)`.

No areal-radius gauge `S=r` and no Schwarzschild relation `FN=1` may be imposed before variation.

Construct Riemann, Ricci, scalar curvature and the Weyl tensor directly from the generic metric, with the Iter047/048 `W3` contraction convention.

Strip only the universal angular factor `sin(theta)` from `sqrt(-g)`. Define the coefficient of `c6` in the one-dimensional reduced density

`L6 = F N S^2 W3`.

For the direct generic metric calculation define

`Q = -F N^3 - F N S S'' + F N (S')^2 + F S N' S' + N S^2 F'' - N S F' S' - S^2 F' N'`.

The production derivation must reproduce exactly

`W3 = -4 Q^3 / (9 F^3 N^9 S^6)`,

`L6 = -4 Q^3 / (9 F^2 N^8 S^4)`.

Derive generalized radial Euler-Lagrange operators **before background substitution**:

`E_q = dL6/dq - d/dr(dL6/dq') + d^2/dr^2(dL6/dq'')`,

for `q in {F,N,S}` with absent terms naturally zero.

## Frozen Schwarzschild certificate

Only after the generic variation substitute

`F = sqrt(1-2M/r)`, `N = 1/F`, `S=r`, with `r>2M>0`.

The exact frozen targets are

`W3 = 96 M^3/r^9`,

`L6 = 96 M^3/r^7`,

`E_F = -48 M^2 (-32M+15r) / (r^(13/2) sqrt(r-2M))`,

`E_N = -48 M^2 (-8M+3r) sqrt(r-2M) / r^(15/2)`,

`E_S = 96 M^2 (-22M+9r) / r^8`.

The production witnesses must avoid the isolated radii at which one numerator accidentally vanishes.

## Frozen radial Noether identity

Because the radial coordinate was not gauge-fixed before variation, the generic reduced operators must satisfy the exact identity

`E_F F' + E_S S' - N (E_N)' = 0`.

This is frozen as a covariance/implementation certificate and must be derived from the generic production expressions, not imposed.

## Frozen production matrix — 24 scientific lanes

### Stream A — Schwarzschild/Petrov-D variational activation (6 lanes)
Use six frozen positive rational `(M,r)` witnesses with `r/M in {3,4,5,6,8,10}`.

Required per lane:
- generic geometry/variation performed before Schwarzschild substitution;
- Schwarzschild Ricci tensor and scalar curvature vanish exactly;
- exact agreement with all five frozen Schwarzschild formulae `W3,L6,E_F,E_N,E_S`;
- `E_F,E_N,E_S` all nonzero at the lane witness.

Frozen masses: `M in {1/5,1/4,1/3,2/5,1/2,3/5}` paired in order with the radius ratios above.

### Stream B — conformally-flat constant-curvature negative controls (6 lanes)
Use three de Sitter and three anti-de Sitter static-patch witnesses:

`F=sqrt(1-sigma H^2 r^2)`, `N=1/F`, `S=r`,

with `sigma=+1` for de Sitter and `sigma=-1` for anti-de Sitter.

Use frozen positive rational `H in {1/7,1/6,1/5}` for each sign and frozen radii inside the de Sitter static patch.

Required per lane after generic variation:
- Riemann tensor nonzero at the witness;
- Weyl tensor exactly zero;
- `W3=L6=E_F=E_N=E_S=0` exactly.

### Stream C — exact radial-reparameterization anti-artifact controls (6 lanes)
Start from Schwarzschild and perform

`R(rho)=rho^m`, with `m in {1/2,2/3,3/2,2,3,4}`,

so

`F(rho)=sqrt(1-2M/R(rho))`,
`N(rho)=R'(rho)/sqrt(1-2M/R(rho))`,
`S(rho)=R(rho)`.

Required per lane:
- direct reconstructed geometry remains Ricci-flat exactly;
- `W3 = 96 M^3/R^9` exactly;
- the reduced density obeys the exact one-dimensional density law
  `L6_rho = R' * 96 M^3/R^7`;
- `W3` and `L6_rho` are nonzero at the frozen witness.

Use frozen `M=1/5` and a positive witness `rho` chosen so `R>2M`.

### Stream D — radial Noether identity / generic-profile audit (6 lanes)
Use six frozen nontrivial positive generic profiles `(F,N,S)` with no Schwarzschild or constant-curvature relation. The profiles are fixed in implementation from low-degree rational polynomials and are not fitted to output.

Required per lane:
- at the generic symbolic level, `E_F F' + E_S S' - N(E_N)'` simplifies exactly to zero;
- after the lane profile substitution, the same identity remains exactly zero as a function of radius;
- at least two of `E_F,E_N,E_S` are nonzero at the frozen positive witness, so the identity is not a trivial all-zero check;
- metric determinant is nonzero at the witness.

## Frozen aggregate classifier

Expected lanes: 24 = A6 + B6 + C6 + D6.

- Full PASS iff all 24 scientific files are present, controls are valid, and every frozen exact criterion passes:
  `PASS_SCOPED_WEYL3_SPHERICALLY_REDUCED_VARIATIONAL_RESPONSE`
- Some scientific criteria fail with valid controls:
  `PARTIAL_SCOPED_WEYL3_SPHERICALLY_REDUCED_VARIATIONAL_RESPONSE`
- Broad scientific failure:
  `FAIL_SCOPED_WEYL3_SPHERICALLY_REDUCED_VARIATIONAL_RESPONSE`
- Missing lanes, invalid geometry, or generic certificate failure indicating implementation/control invalidity:
  `ITER049_CONTROL_OR_IMPLEMENTATION_INVALID`

No scientific threshold, analytic target, witness family, or interpretation lock may be weakened after production inspection.

## Interpretation locks

Even a full PASS establishes only an independent static-spherical symmetry-reduced variational response of the `Weyl^3` coefficient. It does **not**:
- derive the complete 4D covariant six-derivative Euler-Lagrange tensor;
- determine `c6`;
- prove Schwarzschild is or is not an exact solution of the corrected full theory without solving the combined equations;
- establish generic strong-field stability, renormalizability, quantum unitarity, or experimental confirmation;
- raise `theory established` above 0%.
