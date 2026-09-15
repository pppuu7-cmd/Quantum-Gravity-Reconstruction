# General affine Bianchi compatibility theorem

Date: 2026-09-16

## Scope

This theorem concerns only the frozen four-variable homogeneous trace-reversed principal operator used by the QGR local Einstein-seed completions. It is a finite-dimensional exact-algebra statement. It does not establish convergence of the seed series, a global solution, a value or running for `c6`, or any quantum-gravity claim.

Let a pure trace-reversed metric correction have coordinate degree `n >= 2`. Write the frozen output as

- `G_b = d^a hbar_ab`, homogeneous degree `n-1`;
- `E_ab = -(1/2) Box hbar_ab`, homogeneous degree `n-2`.

For the integral row convention used by the audit define `F'_ab = 2 E_ab = -Box hbar_ab`.

## Compatibility operator

Define

`C_b(G,F') = Box G_b + d^a F'_ab`.

Because partial derivatives commute,

`C_b(M_n hbar) = Box(d^a hbar_ab) - d^a Box(hbar_ab) = 0`.

Hence `im(M_n)` is contained in `ker(B_n)`, where `B_n` is the coefficient matrix of `C`.

There are exactly

`Z_n = 4*C(n,3)`

independent degree-`n-3` compatibility coefficients for `n >= 3` and zero for `n=2`.

## Full row rank of the compatibility operator

Use dual homogeneous variables `y_0,...,y_3` and

`q(y) = -y_0^2 + y_1^2 + y_2^2 + y_3^2`.

The transpose map `B_n^T` sends four homogeneous multipliers `lambda_b` of degree `n-3` to a row relation whose gauge part contains `q lambda_b`. If `B_n^T lambda = 0`, then every `q lambda_b = 0`. The polynomial ring over `QQ` is an integral domain and `q` is nonzero, so every `lambda_b=0`.

Therefore `B_n^T` is injective and

`rank(B_n) = 4*C(n,3)`.

Equivalently, `B_n` is surjective onto the complete compatibility space.

## Sufficiency of the Bianchi conditions

The previously proved all-degree rank theorem gives

`rank(M_n) = rows(M_n) - 4*C(n,3)`.

Since `rank(B_n)=4*C(n,3)`,

`dim ker(B_n) = rows(M_n) - rank(B_n) = rank(M_n) = dim im(M_n)`.

Together with `im(M_n) subset ker(B_n)`, equality follows:

`im(M_n) = ker(B_n)`.

Thus for every `n >= 2` and every affine target `y=(G,F')`,

**`M_n x = y` has an exact rational solution if and only if `B_n y = 0`.**

When compatible, the full affine solution space has dimension

`nullity(M_n) = 6 n^2 + 20 n + 10`.

This is an exact theorem; no genericity assumption, numerical tolerance, or probabilistic rank statement is used.

## Consequence for source-specific gates

For a zero-gauge target, `G=0`, the exact solvability condition reduces to

`d^a F'_ab = 0`,

or equivalently in the unscaled convention

`d^a E_ab = 0`.

Therefore a complete exact Bianchi contraction test plus the structural rank theorem already implies augmented-rank equality. A separate augmented RREF can remain as a preregistered control, but it is mathematically redundant once those two ingredients are established.

For Iter057W this theorem is consistent with the independent sparse reproduction: the `480` exact compatibility contractions vanish and the direct computation also found `rank(M)=rank([M|r])=2050`.

The frozen W protocol must nevertheless remain unchanged until terminalization; this theorem does not retroactively relax its preregistered obligations.

## Reproducible audit

The companion script constructs both `M_n` and `B_n` independently for each degree. It checks the integer identity `B_n M_n = 0` entry by entry, computes both ranks over two odd prime fields, verifies the theorem dimensions, and applies a deterministic incompatible unit-source control.

Reproduce the standard audit with

```bash
python code/qgr_general_affine_bianchi_compatibility_audit.py \
  --min-n 2 --max-n 12 \
  --primes 1000003,1000033 \
  --out general_affine_bianchi_compatibility_audit.json
```

The verified run for every `n=2,...,12` satisfies:

- `B_n M_n` has zero nonzero entries exactly;
- `rank(B_n)=4*C(n,3)` over both primes;
- `rank(M_n)=n*(5*n^2+12*n-5)/3` over both primes;
- `left-nullity(M_n)=rank(B_n)`;
- the deterministic incompatible control has nonzero Bianchi image.

In particular:

| n | M shape | rank(M) | rank(B) | affine solution dimension |
|---:|---:|---:|---:|---:|
| 4 | `180 x 350` | 164 | 16 | 186 |
| 6 | `574 x 840` | 494 | 80 | 346 |
| 8 | `1320 x 1650` | 1096 | 224 | 554 |
| 10 | `2530 x 2860` | 2050 | 480 | 810 |
| 12 | `4316 x 4550` | 3436 | 880 | 1114 |

The result turns the full Bianchi family into a complete exact affine-solvability certificate for all future gates using this same frozen homogeneous operator.