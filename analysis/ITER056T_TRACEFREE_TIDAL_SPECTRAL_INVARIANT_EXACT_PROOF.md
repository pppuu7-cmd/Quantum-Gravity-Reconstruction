# Iter056T exact proof — G2 balanced pair sector equals the trace-free tidal spectral-shape space

Date: 2026-09-14
Preregistration: `a523b77242b2f0861d119883ce32859526b3ab8b`
Parent exact bridge: Iter056S `44fea262eb1b29f05b5f07cceb7ed9b6724b0b84`
Held-out repository source inspected only after preregistration: `status/ITERATION_041.md`

## 1. Generic theorem

Iter056S proves that the source-owned G2 balanced pair tensor restricts to the three-dimensional sum-zero spatial subspace with exact spectrum

`spec(H_B4,sp) = (2a, 2b, -2(a+b))`.

Now let `T` be any real symmetric trace-free 3x3 tensor. By the real spectral theorem there exists `R in O(3)` and real eigenvalues `(lambda1,lambda2,lambda3)` such that

`T = R diag(lambda1,lambda2,lambda3) R^T`,

with

`lambda1+lambda2+lambda3=0`.

Choose any ordering of the eigenvalues and set

`a=lambda1/2`, `b=lambda2/2`.

Then

`-2(a+b)=-(lambda1+lambda2)=lambda3`.

Therefore

`spec(H_B4,sp)=spec(T)`.

Conversely, every real `(a,b)` produces a real trace-free spectrum. Thus the G2 balanced pair sector and the real symmetric trace-free 3x3 tidal tensors have exactly the same **spectral quotient** after modding out spatial orthogonal rotations and eigenvalue permutations.

This is an exact two-parameter spectral-shape equivalence; it is not a numerical approximation.

## 2. Exact invariant equality

For the common spectrum,

`I2 = Tr(T^2) = lambda1^2+lambda2^2+lambda3^2`

and

`I3 = Tr(T^3) = lambda1^3+lambda2^3+lambda3^3`.

The G2 balanced tensor has the identical eigenvalues, so

`I2_B4 = I2_T`,

`I3_B4 = I3_T`.

Because `lambda1+lambda2+lambda3=0`, the elementary identity

`x^3+y^3+z^3-3xyz=(x+y+z)(x^2+y^2+z^2-xy-yz-zx)`

gives

`I3 = 3 lambda1 lambda2 lambda3 = 3 det(T)`.

The same identity was already proved in Iter056S for the G2 spatial tensor:

`I3_B4 = 3 det(H_B4,sp)`.

Hence determinant, quadratic invariant and cubic invariant are exactly identical under the spectral map.

For every nonzero tensor, the scale-free shape variables

`chi = I3 / I2^(3/2)`

and

`chi2 = I3^2 / I2^3`

are therefore identical. `chi2` avoids any square-root/sign convention and is an exact algebraic spectral invariant. `chi` retains the sign of the cubic invariant once the positive real square root of `I2` is chosen.

## 3. Cubic-null locus

For a nonzero real trace-free 3-spectrum, `I3=0` iff the determinant is zero. Hence one eigenvalue is zero and the remaining two sum to zero:

`(lambda,-lambda,0)`

up to permutation.

Under the G2 map this is precisely one of

`a=0`, `b=0`, or `a+b=0`,

which is the exact cubic-null locus found in Iter056S.

Thus the cubic-null shape family agrees globally in the spectral quotient.

## 4. Iter040 training shapes are all inside the same two-parameter space

The frozen Iter040 matrices map immediately:

- `H0=(1,1,-2)` -> `(a,b)=(1/2,1/2)`;
- `H1=(1,2,-3)` -> `(a,b)=(1/2,1)`;
- `H2=(1,-1,0)` -> `(a,b)=(1/2,-1/2)`;
- `H3=(2,-1,-1)` -> `(a,b)=(1,-1/2)`;

up to eigenvalue permutation.

Therefore Iter056S's H0 coincidence was not isolated: all four original calibration-free Weyl3 training shapes lie in the exact G2 balanced spectral-shape manifold.

## 5. Held-out Iter041 domain validation

The Iter056T preregistration explicitly froze the requirement to inspect Iter041 **after** freezing the theorem candidate. Iter041's preregistered held-out matrices are:

```
G0 = [[ 1,     7/20, -1/5],
      [ 7/20, -1/4,   3/20],
      [-1/5,   3/20, -3/4]]

G1 = [[ 7/10, -2/5,  3/10],
      [-2/5,   4/5, -1/10],
      [ 3/10, -1/10,-3/2]]

G2 = [[ 7/5,   1/4,  9/20],
      [ 1/4,  -9/10,-7/20],
      [ 9/20, -7/20,-1/2]]

G3 = [[ 9/20, 11/20,-1/4],
      [11/20,  7/20, 2/5],
      [-1/4,   2/5, -4/5]]

G4 = [[11/10,-1/5,  1/2],
      [-1/5, -3/10, 1/4],
      [ 1/2,  1/4, -4/5]]

G5 = [[ 9/10, 9/20, 1/10],
      [ 9/20,-6/5,-3/10],
      [ 1/10,-3/10,3/10]]
```

Every matrix is manifestly real, symmetric and exactly trace-free, so each lies in the generic theorem's domain. None was used in Iter040 or in the Iter056T preregistration.

Their exact spectral invariants are:

| held-out | `I2=Tr(G^2)` | `I3=Tr(G^3)` | `det(G)=I3/3` | `chi2=I3^2/I2^3` |
|---|---:|---:|---:|---:|
| G0 | `399/200` | `5901/8000` | `1967/8000` | `78961/1152312` |
| G1 | `39/10` | `-393/200` | `-131/200` | `17161/263640` |
| G2 | `759/200` | `7119/4000` | `2373/4000` | `1877043/32388554` |
| G3 | `403/200` | `-2109/8000` | `-703/8000` | `4447881/523606616` |
| G4 | `529/200` | `3027/4000` | `1009/4000` | `9162729/296071778` |
| G5 | `589/200` | `-5769/4000` | `-1923/4000` | `33281361/408672938` |

The corresponding exact characteristic polynomials are of the trace-free form

`p(lambda)=lambda^3-(I2/2)lambda-det`:

- G0: `(8000 lambda^3 - 7980 lambda - 1967)/8000`;
- G1: `(200 lambda^3 - 390 lambda + 131)/200`;
- G2: `(4000 lambda^3 - 7590 lambda - 2373)/4000`;
- G3: `(8000 lambda^3 - 8060 lambda + 703)/8000`;
- G4: `(4000 lambda^3 - 5290 lambda - 1009)/4000`;
- G5: `(4000 lambda^3 - 5890 lambda + 1923)/4000`.

Because each matrix is real symmetric, all three roots are real. Taking any two roots and setting `a=lambda1/2`, `b=lambda2/2` constructs the corresponding G2 balanced tensor; the third root is forced by trace zero. Therefore every held-out off-diagonal Iter041 shape has an exact G2 spectral representative.

For display only, one ordered numerical choice of `(lambda1,lambda2,lambda3)` and `(a,b)` is:

- G0: `(-0.83939254,-0.26518702,1.10457956)`, `(a,b)≈(-0.41969627,-0.13259351)`;
- G1: `(-1.54110949,0.35977969,1.18132980)`, `(a,b)≈(-0.77055475,0.17988985)`;
- G2: `(-1.18121191,-0.33191982,1.51313174)`, `(a,b)≈(-0.59060596,-0.16595991)`;
- G3: `(-1.04479998,0.08789482,0.95690516)`, `(a,b)≈(-0.52239999,0.04394741)`;
- G4: `(-1.03910707,-0.19647187,1.23557894)`, `(a,b)≈(-0.51955353,-0.09823594)`;
- G5: `(-1.35206077,0.35752019,0.99454059)`, `(a,b)≈(-0.67603039,0.17876009)`.

These decimal roots are not scientific inputs and are not needed for the proof.

## 6. Held-out rotations

Iter041 also preregistered proper rotations of the off-diagonal G0 tensor and of the cubic-null tensor `N0=diag(1,-1,0)`.

For every orthogonal `R`,

`T -> R T R^T`

is an orthogonal similarity, so its eigenvalue multiset, characteristic polynomial, `I2`, `I3`, determinant, `chi` and `chi2` are exactly unchanged.

Thus all Iter041 rotated held-out lanes map to the **same G2 spectral point** as their unrotated parent. Orientation is intentionally quotiented and is not reconstructed from `(a,b)`.

## 7. Frozen negative controls

### Nonzero trace

A symmetric tensor with nonzero trace has eigenvalues whose sum is nonzero. It therefore cannot equal `(2a,2b,-2(a+b))` for any real `(a,b)`. The map rejects it unless a trace-removal operation is separately authorized; silently projecting out the trace is forbidden.

### Antisymmetric perturbation

An antisymmetric matrix is outside the real symmetric tidal domain and is not covered by the real orthogonal spectral theorem used here. It is rejected rather than mapped.

### Orientation reconstruction

Many tensors `R T R^T` share the same spectral pair `(a,b)`. Hence orientation cannot be recovered from the spectral data. Any attempt to claim an orientation-level micro→G3 map from this theorem would violate the preregistered scope.

## 8. Relation to Iter041's independent numerical result

Iter041 previously found 24/24 held-out numerical Weyl3 transfer lanes PASS, including six generic off-diagonal trace-free shapes, rotated cubic-null controls, and rotation covariance. That result is independent support that the continuum-proxy Weyl3 kernel is controlled by the same tidal cubic invariant across this broader shape domain.

Iter056T does not reclassify or depend on the numerical accuracy of that run. It proves that the **tidal shape domain used there** is exactly the same spectral-invariant domain already present in the source-owned G2 balanced pair sector, conditional on the G2 spatial interpretation.

## Classification supported by the proof

`PASS_SCOPED_CONDITIONAL_ITER056T_G2_BALANCED_PAIR_CUBIC_IS_EXACT_TRACEFREE_TIDAL_SPECTRAL_SHAPE_INVARIANT`

## Interpretation ceiling

The theorem is spectral/invariant and conditional only. It does not supply:

- an orientation-level same-realization tensor identification;
- a microscopic event amplitude to `kappa` map;
- `beta=1` or any physical beta value;
- a coefficient relation to `c6`;
- a derivation of Weyl curvature from B4;
- a micro→continuum dynamical map;
- a higher-derivative treatment selector;
- global measure/regulator removal, quantum unitarity, UV completion, full GR recovery, experiment, new physics, or QGR correctness.

The Iter003-G2 null-link/Lorentzian assumption remains explicit. Theory established remains `0%`; `c6` remains symbolic/unfixed; `beta=1` remains unauthorized.