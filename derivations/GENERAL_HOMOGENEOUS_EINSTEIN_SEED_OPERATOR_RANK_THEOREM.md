# General homogeneous Einstein-seed operator rank theorem

Date: 2026-09-16

## Result

For the frozen four-variable trace-reversed homogeneous principal operator used by the QGR quartic/sextic/octic/decic Einstein-seed completions, let a pure metric correction have coordinate degree `n >= 2`.

The unrestricted symmetric trace-reversed correction has

`U_n = 10*C(n+3,3)`

normalized coefficients.  The frozen linear system has

- `G_n = 4*C(n+2,3)` degree-`n-1` de Donder rows;
- `F_n = 10*C(n+1,3)` degree-`n-2` trace-reversed Einstein rows;
- `R_n = G_n + F_n` total rows;
- exactly `4 R_n` nonzero matrix entries.

The complete left kernel is the canonical contracted-Bianchi family and has dimension

`B_n = 4*C(n,3)`.

Therefore, for every `n >= 2`, the exact rational rank and nullity are

`rank(M_n) = R_n - B_n = n*(5 n^2 + 12 n - 5)/3`,

`nullity(M_n) = U_n - rank(M_n) = 6 n^2 + 20 n + 10`.

No numerical-rank tolerance is involved.

## Algebraic proof of left-kernel completeness

Use dual coefficient variables `y_0,...,y_3` for the normalized Taylor rows and write

`q(y) = -y_0^2 + y_1^2 + y_2^2 + y_3^2`.

A general linear dependence among the rows is represented by four homogeneous gauge multipliers `g_b(y)` of degree `n-1` and ten symmetric field multipliers `f_ab(y)` of degree `n-2`.

The transpose of the frozen principal matrix gives, for every independent symmetric component, the polynomial identities

- diagonal: `y^a g_a - (1/2) q f_aa = 0`;
- off diagonal: `y^a g_b + y^b g_a - (1/2) q f_ab = 0`, `a < b`,

where `y^a = eta^{aa} y_a`.

From each diagonal equation, `q` divides `y^a g_a`.  The polynomial `q` is coprime to every coordinate `y_a`, so `q` must divide every `g_a`.  Hence there are homogeneous `lambda_a(y)` of degree `n-3` such that

`g_a = (q/2) lambda_a`.

Substitution back into the diagonal and off-diagonal equations forces

`f_aa = y^a lambda_a`,

`f_ab = y^a lambda_b + y^b lambda_a` for `a < b`.

This is exactly the canonical contracted-Bianchi row relation used in the existing QGR implementations.  Conversely, direct substitution shows every such `lambda` annihilates the matrix.

Multiplication by the nonzero polynomial `q` is injective, so the map from the four `lambda_a` is injective.  The homogeneous degree-`n-3` polynomial space in four variables has dimension `C(n,3)`.  Thus the complete left kernel has dimension exactly

`4*C(n,3)`.

Rank-nullity then gives the formulas above.  For `n=2`, the degree `n-3` space is absent and the left kernel is zero, which agrees with the same closed formula interpreted as `C(2,3)=0`.

## Independent exact implementation audit

The accompanying script constructs the same frozen sparse matrix directly.  It multiplies each field row by two, converting all nonzero entries to `+/-1`, and computes rank over the exact finite field `GF(1000003)`.

A rank-`r` minor nonzero modulo this odd prime is a nonzero integer minor and therefore certifies `rank_QQ >= r`.  The proved Bianchi left kernel gives `rank_QQ <= R_n-B_n`.  When the modular rank reaches that upper bound, the rational rank is fixed exactly.

A single reproducible run verifies every degree `n=2,...,12`.  Separate exact runs were also performed for `n=13,...,18`; all hit the closed-form rank.

| n | rows x unknowns | rank | left-nullity | nullity | nnz |
|---:|---:|---:|---:|---:|---:|
| 2 | 26 x 100 | 26 | 0 | 74 | 104 |
| 3 | 80 x 200 | 76 | 4 | 124 | 320 |
| 4 | 180 x 350 | 164 | 16 | 186 | 720 |
| 5 | 340 x 560 | 300 | 40 | 260 | 1360 |
| 6 | 574 x 840 | 494 | 80 | 346 | 2296 |
| 7 | 896 x 1200 | 756 | 140 | 444 | 3584 |
| 8 | 1320 x 1650 | 1096 | 224 | 554 | 5280 |
| 9 | 1860 x 2200 | 1524 | 336 | 676 | 7440 |
| 10 | 2530 x 2860 | 2050 | 480 | 810 | 10120 |
| 11 | 3344 x 3640 | 2684 | 660 | 956 | 13376 |
| 12 | 4316 x 4550 | 3436 | 880 | 1114 | 17264 |
| 13 | 5460 x 5600 | 4316 | 1144 | 1284 | 21840 |
| 14 | 6790 x 6800 | 5334 | 1456 | 1466 | 27160 |
| 15 | 8320 x 8160 | 6500 | 1820 | 1660 | 33280 |
| 16 | 10064 x 9690 | 7824 | 2240 | 1866 | 40256 |
| 17 | 12036 x 11400 | 9316 | 2720 | 2084 | 48144 |
| 18 | 14250 x 13300 | 10986 | 3264 | 2314 | 57000 |

## Recovery of existing production cases

The theorem reproduces the structural invariants already seen in the exact production chain:

- degree 4 / Iter057O operator: rank `164`, left-nullity `16`, nullity `186`;
- degree 6 / Iter057Q and Iter057V operator: rank `494`, left-nullity `80`, nullity `346`;
- degree 8 / Iter057T operator: rank `1096`, left-nullity `224`, nullity `554`;
- degree 10 / Iter057W operator: rank `2050`, left-nullity `480`, nullity `810`.

Thus the Iter057W structural audit is one member of an all-degree algebraic law rather than an isolated matrix-rank accident.

## Immediate prediction

If a future frozen gate uses the same unrestricted degree-12 principal operator, its structural invariants are fixed before any source calculation:

- matrix shape `4316 x 4550`;
- nnz `17264`;
- exact rank `3436`;
- exact left-nullity/Bianchi dimension `880`;
- exact homogeneous freedom/nullity `1114`.

Likewise, a future degree-8 first-order response uses the already-known `1320 x 1650`, rank `1096`, left-nullity `224`, nullity `554` operator.

These statements do **not** establish affine compatibility for any future source.  They do not determine a particular solution, nonlinear replay, convergence, an all-orders Einstein seed, the value of `c6`, or any quantum-gravity claim.  Each source-specific gate must still test all Bianchi contractions and augmented-rank consistency exactly.

## Reproduction

From repository root:

```bash
python code/qgr_general_seed_operator_rank_audit.py --max-n 12 --out general_seed_rank_audit.json
```

For the extended audit:

```bash
python code/qgr_general_seed_operator_rank_audit.py --min-n 13 --max-n 18 --out general_seed_rank_audit_13_18.json
```

The standard `n=2..12` result generated in this research iteration passed every control with exact finite-field arithmetic.
