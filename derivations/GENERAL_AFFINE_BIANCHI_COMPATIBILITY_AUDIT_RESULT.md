# General affine Bianchi compatibility audit result

Date: 2026-09-16

Gate: `GENERAL-AFFINE-BIANCHI-COMPATIBILITY-THEOREM`

Independent local exact execution of the committed audit logic was run over the two odd primes `1000003` and `1000033` for every homogeneous degree `n=2,...,12`.

Result: **PASS**.

For every tested degree:

- the integer sparse composition `B_n M_n` has exactly `0` nonzero entries;
- `rank(M_n)` reaches the closed theorem bound over both primes;
- `rank(B_n)=4*C(n,3)` over both primes;
- `left-nullity(M_n)=rank(B_n)`;
- a deterministic unit target touched by `B_n` is rejected by a nonzero compatibility image.

| n | M shape | rank(M) | rank(B) | B*M nnz |
|---:|---:|---:|---:|---:|
| 2 | `26 x 100` | 26 | 0 | 0 |
| 3 | `80 x 200` | 76 | 4 | 0 |
| 4 | `180 x 350` | 164 | 16 | 0 |
| 5 | `340 x 560` | 300 | 40 | 0 |
| 6 | `574 x 840` | 494 | 80 | 0 |
| 7 | `896 x 1200` | 756 | 140 | 0 |
| 8 | `1320 x 1650` | 1096 | 224 | 0 |
| 9 | `1860 x 2200` | 1524 | 336 | 0 |
| 10 | `2530 x 2860` | 2050 | 480 | 0 |
| 11 | `3344 x 3640` | 2684 | 660 | 0 |
| 12 | `4316 x 4550` | 3436 | 880 | 0 |

Both primes returned the same displayed ranks in every row.

Canonical compact-payload digest for this local two-prime execution, before adding the digest field itself:

`sha256:e3686d06ad84c90658e81cf8f266d0a1407280799d2a1e336bed077d5d0a2d8b`

The algebraic proof establishes the exact characteristic-zero theorem; the modular executions are independent implementation audits and nonzero-minor certificates, not a substitute for the proof.

A branch-local GitHub Actions workflow was also launched from commit `e6e240affde09ab75ef9a936caac05b68a36c5c6` to execute the committed script independently on Ubuntu and upload its JSON payload.
