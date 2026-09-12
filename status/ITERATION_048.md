# QGR Iter048 — symmetry-reduced variational response of the Weyl^3 correction

Date: 2026-09-13
Status: PREREGISTERED BEFORE IMPLEMENTATION / PRODUCTION

## Scientific question

Iter047 established only a metric-level activation map for the already-selected QGR six-derivative operator `c6 * Weyl^3`. A nonzero invariant does not by itself prove a nonzero contribution to the equations of motion.

Iter048 therefore asks the stronger but still explicitly scoped question:

> In a lapse-retaining axisymmetric Bianchi-I reduction, does the coefficient of `c6` in the generalized Euler–Lagrange response of `sqrt(-g) Weyl^3` become nonzero on the exact Ricci-flat Kasner background, while vanishing exactly in the conformally-flat isotropic subspace?

This is a **symmetry-reduced variational gate**. It is not the full covariant six-derivative field equation.

## Frozen reduced geometry

Use

`ds^2 = -N(t)^2 dt^2 + a(t)^2 dx^2 + b(t)^2(dy^2 + dz^2)`.

Construct Riemann, Ricci, scalar curvature and the Weyl tensor directly from this metric, with the same `W3` contraction convention frozen in Iter047.

Define the coefficient of `c6` in the reduced six-derivative Lagrangian density

`L6 = N a b^2 W3`.

`c6` itself is **not** assigned a numerical value; production works with the coefficient multiplying `c6`.

Because `L6` depends on second time derivatives of `a,b` and on the first derivative of `N`, derive the generalized Euler–Lagrange operator before imposing any background:

`E_q[L6] = dL6/dq - d/dt(dL6/dq') + d^2/dt^2(dL6/dq'')`,

for `q in {N,a,b}` (terms absent when the corresponding derivative is absent).

## Frozen analytic certificate for power laws

For the frozen power-law family

`N=1, a=t^p, b=t^q`, with `t>0`, the production derivation must reproduce exactly:

`L6 = (4/9) t^(p+2q-6) (p-1)^3 (p-q)^3`,

`E_N = -(8/9) t^(p+2q-6) (p-1)^2 (p-q)^3 (p-3q+5)`,

`E_a = -(8/9) t^(2q-6) (p-1)^2 (p-q)^2 (p^2-pq-p-9q^2+34q-30)`,

`E_b = +(8/9) t^(p+q-6) (p-1)^2 (p-q)^2 (p^2-4pq+5p-6q^2+28q-30)`.

These formulae are frozen prospectively as exact analytic targets, not fitted thresholds.

For the exact axisymmetric vacuum Kasner exponents

`p=-1/3, q=2/3`, production must give exactly

`L6 = 256/(243 t^5)`,

`E_N = 1024/(243 t^5)`,

`E_a = 4096/(243 t^(14/3))`,

`E_b = -5632/(243 t^(17/3))`.

Thus the preregistered prediction is that the `Weyl^3` correction is variationally active on this reduced Kasner branch for any nonzero `c6`.

## Frozen production matrix — 24 scientific lanes

### Stream A — exact Kasner variational activation (6 lanes)
Use the exact axisymmetric Kasner profile `N=1, a=t^-1/3, b=t^2/3` at six frozen positive rational times.

Required per lane:
- the reduced geometry is Ricci-flat before adding the correction;
- `W3 = 256/(243 t^6)` exactly;
- all three preregistered reduced responses `E_N,E_a,E_b` agree exactly with the frozen formulas above;
- all three are nonzero at the lane witness.

### Stream B — conformally-flat isotropic negative controls (6 lanes)
Use six frozen nontrivial positive scale-factor profiles with `a(t)=b(t)=s(t)` and frozen lapse profiles `N(t)`.

Required per lane after deriving `E_N,E_a,E_b` **before** imposing isotropy:
- Weyl tensor and `W3` vanish exactly after `a=b=s` substitution;
- `E_N=E_a=E_b=0` exactly after the same substitution;
- at least one Riemann component is nonzero at the frozen witness, except one explicitly frozen Minkowski control allowed as a zero-curvature sanity lane.

This tests that generic curvature is not mistaken for a six-derivative Weyl response.

### Stream C — generic anisotropic power-law formula audit (6 lanes)
Use six preregistered rational `(p,q)` pairs away from `p=q`, `p=1`, and accidental response zeros.

Required per lane:
- independently substitute the pair into the fully derived reduced Euler–Lagrange expressions;
- exact agreement with all four frozen analytic power-law formulae (`L6,E_N,E_a,E_b`);
- `W3 != 0` and at least one reduced response nonzero.

Frozen pairs:
`(-1/2,1/3), (1/4,3/4), (-2/3,1/2), (2/5,-1/5), (3/2,1/4), (-1/4,5/6)`.

### Stream D — exact reparameterization/action-density control (6 lanes)
Take the Kasner solution and perform frozen monotone time reparameterizations `t = tau^m`, with
`m in {1/2, 2/3, 3/2, 2, 3, 4}`,
so that
`N(tau)=m tau^(m-1)`, `a(tau)=tau^(-m/3)`, `b(tau)=tau^(2m/3)`.

Required per lane:
- direct metric reconstruction remains Ricci-flat exactly;
- direct `W3 = 256/(243 tau^(6m))` exactly;
- the reduced density transforms as a one-dimensional density,
  `L6_tau = (dt/dtau) * [256/(243 t^5)]_(t=tau^m) = 256 m /(243 tau^(4m+1))`, exactly;
- `W3` and `L6_tau` are nonzero.

This stream is a coordinate/reparameterization anti-artifact control. It does not require individual reduced Euler–Lagrange components to transform as scalars.

## Frozen aggregate classifier
Expected lanes: 24 = A6 + B6 + C6 + D6.

- Full PASS iff all 24 files are present, controls are valid, and all frozen exact criteria pass:
  `PASS_SCOPED_WEYL3_SYMMETRY_REDUCED_VARIATIONAL_RESPONSE`
- Some scientific criteria fail with valid implementation controls:
  `PARTIAL_SCOPED_WEYL3_SYMMETRY_REDUCED_VARIATIONAL_RESPONSE`
- Broad scientific failure:
  `FAIL_SCOPED_WEYL3_SYMMETRY_REDUCED_VARIATIONAL_RESPONSE`
- Missing lanes / invalid geometry / analytic-certificate mismatch indicating implementation failure:
  `ITER048_CONTROL_OR_IMPLEMENTATION_INVALID`

No threshold or target may be weakened after production inspection.

## Interpretation locks

Even a full PASS establishes only that, **within this lapse-retaining axisymmetric Bianchi-I reduction**, the coefficient of `c6` in the reduced variational equations is nonzero on Kasner and zero in the tested conformally-flat isotropic subspace.

A PASS does **not**:
- derive the complete four-dimensional covariant Euler–Lagrange tensor of `Weyl^3`;
- prove that the corrected theory has or lacks a nearby Kasner solution;
- determine the numerical value or sign of `c6`;
- prove generic strong-field stability, renormalizability, quantum unitarity, or experimental confirmation;
- raise `theory established` above 0%.
