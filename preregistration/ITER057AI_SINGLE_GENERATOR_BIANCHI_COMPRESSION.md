# Iter057AI — Single-Generator Bianchi/Noether Compression of the Dual Certificate

Status: PROSPECTIVELY PREREGISTERED; no Iter057AI implementation or production evidence exists at this commit.  
Date: 2026-09-16.

## Purpose

Determine whether the terminal Iter057AH localization of the Iter057AG dual certificate admits an exact closed-form compression to one scalar generating polynomial under the frozen Bianchi/Noether left-row construction. This is a structural rewrite of the existing finite-order certificate, not a new branch search and not a change to the scientific object.

## Frozen inputs

Consume exactly:

- Iter057AG canonical witness `data/ITER057AG_CANONICAL_DUAL_WITNESS.json` at commit `79f447491834eaa67c2516d50433be619f098dd2`;
- Iter057AG terminal result `057f6c9699c1e81cfe3042a711715bc65850f6e3`;
- Iter057AH preregistration `9b55fb87f89456bb04d325c534cde025fcb9ad2e`;
- Iter057AH exact localization authority `data/ITER057AH_DUAL_WITNESS_LOCALIZATION.json` corrected at `e4c82732af6a0a150c5f2aa245e58a63b2d09c13`;
- Iter057AH terminal result `15f95a32fe45a8602cb2fdf38a42804211277a81`;
- unchanged Iter057AD/Iter057AC `left_controls`, `rhs14`, `system` ordering and Minkowski signature `ETA=(-1,1,1,1)`.

No witness rescaling/reordering, support pruning, gauge-row deletion, tensor-row deletion, numerical tolerance, branch refit or c6 choice is permitted.

## Prospectively frozen test

Let the exact canonical compatibility generating polynomials be

`Y_b(t,x,y,z)=sum_beta y_(b,beta) t^beta_t x^beta_x y^beta_y z^beta_z`.

Let the exact induced affine-row generating polynomials from the already-defined `w^T=y^T L` be

- `W_G,b(t,x,y,z)` for gauge rows `('G',b,alpha13)`,
- `W_F,ab(t,x,y,z)` for field rows `('F',(a,b),alpha12)`.

The gate directly tests, without altering any coefficients, whether the terminal AH support localizes the full induced witness to the following single-generator identities:

`W_G,0 = (1/2)*(-t^2+x^2+y^2+z^2)*Y_0`,

`W_G,1=W_G,2=W_G,3=0`,

`W_F,00 = -t*Y_0`,

`W_F,01 =  x*Y_0`,

`W_F,02 =  y*Y_0`,

`W_F,03 =  z*Y_0`,

and every other `W_F,ab` is zero.

These identities are a frozen exact test; failure may not be repaired by changing the target formula.

## Symmetric-invariant compression

Because Iter057AH terminally established full `S3` invariance under permutations of `(x,y,z)` and an exact factor `Y_0 = C*t*Q_10`, construct

`u=t^2`, `e1=x^2+y^2+z^2`, `e2=x^2 y^2+x^2 z^2+y^2 z^2`, `e3=x^2 y^2 z^2`.

Prospectively require exact symmetric reduction of the primitive degree-10 factor `Q_10` to a unique rational/integer polynomial `R_5(u,e1,e2,e3)` with zero remainder under exact symmetric-polynomial reduction. Serialize `R_5` and independently substitute back to recover `Q_10` exactly. No desired factorization of `R_5` is imposed.

## Exact controls

PASS requires:

1. Frozen AG/AH provenance and exact canonical `y` reconstruction.
2. Exact reconstruction of `w=y^T L`.
3. Exact equality of every `W_G`/`W_F` polynomial to the prospectively frozen single-generator formulas above.
4. Exact replay `w^T M14=0` and `w^T r0=1`.
5. Exact symmetric-invariant reduction `Q_10 -> R_5` with zero remainder and exact back-substitution.
6. No numerical zero/rank tolerance.

PASS label:

`PASS_SCOPED_ITER057AI_DUAL_CERTIFICATE_COMPRESSES_TO_SINGLE_S3_SCALAR_BIANCHI_GENERATOR`

Contradiction with frozen AG/AH authority is INVALID. Pure implementation inability is BLOCKED.

## Scope ceiling

A PASS is only an exact algebraic compression of the existing finite local Taylor-jet obstruction certificate. The words Bianchi/Noether describe the frozen left-row construction; they do not authorize a new physical gauge, causality, stability, global no-go, all-orders or quantum-gravity claim.

Claim locks remain unchanged: theory established `0%`; no experimental confirmation; `beta=1` unauthorized; `c6` symbolic/unfixed; no c6 running/fitting; no quantum unitarity, regulator removal, UV completion, strong hyperbolicity, physical-ghost/stability or KMQGB `NEW_REQUIRED` claim is authorized.
