# Exact Gauss-Jacobi moment fingerprint of the Iter053R legacy double-weight path

Date: 2026-09-14
Status: retrospective analytic diagnosis using the frozen Iter053R quadrature rule and already-terminal Iter053R aggregate/raw values. No partial evidence from active Iter053T productions is used. This note does not reclassify Iter053R or substitute for either active Iter053T classifier.

## Question

The source-level audit shows that the transformed legacy Iter053R weighted reducer effectively inserts one extra compact-support factor

`B(u)=prod_i (1-(u_i/A)^2)^4`

inside a tensor Gauss-Jacobi rule whose external weight already represents the first `B(u)`.

Can this object mismatch alone quantitatively explain the two conspicuous historical signatures of the terminal C-lane failure?

1. the transformed/base fine weighted ratio near `0.3075`;
2. the transformed weighted GJ2->GJ3 relative change near `0.292`.

A useful analytic control is the constant-reduced-integrand limit, in which all variation comes only from the accidental extra support factor.

## One-dimensional support moments

Scale to `t=u/A in [-1,1]`. The intended Jacobi weight is

`w(t)=(1-t^2)^4`.

For a constant reduced integrand, the correct one-dimensional weighted integral is proportional to

`I4 = integral_{-1}^1 (1-t^2)^4 dt = 256/315`.

The legacy extra-B continuum integral would instead contain

`I8 = integral_{-1}^1 (1-t^2)^8 dt`,

and

`I8/I4 = 1792/2431`.

In four tensor-product dimensions, the exact continuum constant-integrand suppression is therefore

`(I8/I4)^4 = 10312216477696 / 34925275077121`

`= 0.29526514694372075...`.

This continuum value is not expected to equal the actual Iter053R GJ3 ratio exactly, because the geometric contraction `H:p` is not constant and GJ3 does not exactly integrate the remaining degree-eight extra factor.

## Frozen GJ2 fingerprint

Iter053R uses `roots_jacobi(q,4,4)`.

For q=2 the Jacobi nodes are exactly

`t = +/- 1/sqrt(11)`.

At both nodes the accidental extra factor is

`(1-t^2)^4 = (10/11)^4`.

Because all q=2 symmetric weights see the same factor, the one-dimensional legacy/correct ratio is exactly `(10/11)^4`, and the four-dimensional tensor-product ratio is

`R2 = (10/11)^16`

`= 10000000000000000 / 45949729863572161`

`= 0.21762913579014878...`.

## Frozen GJ3 fingerprint

For q=3, symmetry gives nodes

`t = 0, +/- sqrt(3/13)`.

With the `(1-t^2)^4` Jacobi weight, the exact normalized node weights are obtained from the zeroth and second weighted moments. Writing the central weight as `w0` and each outer weight as `w1`, one obtains

`w0 = 1024/2079`,

`w1 = 1664/10395`,

with total `w0+2 w1 = 256/315`.

The normalized one-dimensional average of the accidental extra support factor is therefore

`r3 = [w0 + 2 w1 (1-3/13)^4] / (256/315)`

`= 17980/24167`

`= 0.7439897380725783...`.

Thus the four-dimensional constant-integrand legacy/correct GJ3 ratio is exactly

`R3 = r3^4`

`= 104510217024160000 / 341107264278244321`

`= 0.3063851989352829...`.

## Frozen GJ2->GJ3 change predicted by the accidental extra B

Using the same relative-change convention as Iter053R,

`Delta23 = |R3-R2| / max(|R2|,|R3|)`

and here `R3>R2`, so

`Delta23 = (R3-R2)/R3`

`= 593856122131774300241121 / 2049986442286836800241121`

`= 0.28968782909086244...`.

Therefore the **support-weight error by itself**, even before any detailed geometry is included, predicts:

- fine GJ3 transformed/base suppression approximately `0.3064`;
- GJ2->GJ3 relative change approximately `0.2897`.

## Comparison with immutable historical Iter053R C evidence

From the already-terminal Iter053R raw C artifacts:

### C0

- transformed/base fine weighted ratio: `0.3075515201936711`;
- transformed GJ2->GJ3 change: `0.29241022512664006`.

Difference from the constant-integrand B^2 fingerprint:

- ratio absolute difference: `0.0011663212583882254`;
- ratio relative difference versus `R3`: about `0.0038067` (0.38%);
- GJ2->GJ3 change excess over `Delta23`: `0.002722396035777619`.

### C1

- transformed/base fine weighted ratio: `0.3074418708400629`;
- transformed GJ2->GJ3 change: `0.2921168408364991`.

Difference from the constant-integrand B^2 fingerprint:

- ratio absolute difference: `0.0010566719047800377`;
- ratio relative difference versus `R3`: about `0.0034488` (0.34%);
- GJ2->GJ3 change excess over `Delta23`: `0.0024290117456366445`.

Thus two independent C seeds reproduce the pure support-weight fingerprint to substantially better than one percent in the fine suppression ratio, and within about `2.4e-3` to `2.7e-3` absolute in the coarse/fine relative-change statistic.

The remaining small difference is naturally attributable to the fact that the true reduced contraction `H:p` varies over the support, whereas this control deliberately sets it constant.

## Scientific interpretation

This is a highly specific mechanistic fingerprint:

1. source inspection independently predicts that the transformed legacy path contains one extra `B`;
2. the frozen Gauss-Jacobi nodes/weights then analytically predict a large q-dependent suppression with no adjustable parameter;
3. the predicted GJ3 suppression and GJ2->GJ3 drift nearly reproduce both terminal C lanes despite their different metric/perturbation seeds;
4. the base C paths were already generic PASS and direct coordinate covariance was machine-level.

This makes a generic physical covariance failure or random quadrature instability a much less economical explanation of the historical Iter053R pattern than the deterministic wrapper-depth double-weight defect.

It does **not** prove that the corrected numerical implementation passes its prospectively frozen obligations. The two active Iter053T productions remain authoritative for that question.

## Claim ceiling

- Iter053R remains historical `SCIENTIFIC_FAIL_ITER053R_WEYL3_WEIGHTED_H5_COMPACT_SUPPORT_ACTION_VARIATION`;
- no active Iter053T verdict is inferred from this note;
- no full A4+B2+C2 corrected replacement PASS is claimed;
- no global functional-variation theorem follows;
- `c6` remains symbolic/unfixed;
- `beta=1` remains unauthorized;
- theory established remains `0%`.
