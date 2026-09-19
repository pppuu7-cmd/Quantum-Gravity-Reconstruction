# QGR Weyl3 target-blind witness panel V1

Status: EXECUTION INPUT for preregistered gate `COVARIANT_WEYL3_CURVATURE_P_FIRST_JET_TARGET_BLIND_COMPARISON_V1`.

This file implements step A only. It is frozen before reading any historical generic-P mismatch coefficient or residual value. It does not classify the gate and it does not alter any scientific threshold, sign, contraction, normalization, or claim lock.

## Conventions

Work at one normal-coordinate point in four dimensions with

`g_ab = diag(-1,1,1,1)` and `partial_e g_ab = 0`.

All numbers below are exact integers/rationals. Riemann tensors use the algebraic symmetries

`R_abcd=-R_bacd=-R_abdc=R_cdab`, `R_a[bcd]=0`.

The Weyl projection is the standard 4D trace-free projection associated with the frozen metric convention in `theory/covariant/QGR_WEYL3_CURVATURE_P_FIRST_JET_V1.md`. No value of `c6` is chosen.

## Construction family

For an ordered orthogonal two-plane `(p,q)` define the unit plane-curvature algebraic tensor

`K[pq]_abcd = A_ab A_cd`,

where `A_pq=+1`, `A_qp=-1`, and all other `A_ab=0`.

Each `K[pq]` has the required antisymmetry, pair exchange symmetry and algebraic Bianchi identity. Linear combinations therefore do too.

For the first-jet input use the same algebraic tensor family independently in each derivative slot. This is an algebraic pointwise jet witness; no field equation is imposed.

## Frozen witnesses

Lexicographic order is W0, W1, W2.

### W0

`R = 2 K[01] + 3 K[23]`

`nabla_0 R = 5 K[01] - 2 K[23]`

`nabla_1 R = K[02] + 2 K[13]`

all other `nabla_e R = 0`.

Directional metric perturbation:

`h_ab = diag(2,-1,3,-2)` with additionally `h_01=h_10=1`.

### W1

`R = K[01] - 2 K[02] + 4 K[13] + 3 K[23]`

`nabla_0 R = 2 K[03] + K[12]`

`nabla_2 R = -3 K[01] + 2 K[23]`

all other `nabla_e R = 0`.

`h_00=-1, h_11=2, h_22=1, h_33=3, h_02=h_20=2`, all other components zero.

### W2

`R = 3 K[03] + 2 K[12] - K[01] + K[23]`

`nabla_1 R = 4 K[02] - K[13]`

`nabla_3 R = 2 K[01] + 3 K[23]`

all other `nabla_e R = 0`.

`h_00=1, h_11=-3, h_22=2, h_33=-1, h_13=h_31=1`, all other components zero.

## Mandatory pre-comparison controls

Before either lane may compare outputs, an implementation must verify exactly for every witness:

1. algebraic Riemann/pair symmetries and Bianchi identity for `R` and every nonzero `nabla_e R`;
2. `C=Pi_g[R]` is nonzero for at least one witness;
3. `nabla C=Pi_g[nabla R]` is nonzero for at least one witness;
4. all Weyl traces vanish exactly;
5. `P_R` and `nabla P_R` are instantiated only from defining-source commit `fac9939927903213d2f834e8460ff4865dbd9897`;
6. the common symbolic factor `c6` remains unfixed and is factored rather than numerically assigned.

If any witness fails an algebraic prerequisite, the gate is `BLOCKED_CURVATURE_P_FIRST_JET_COMPARISON_IMPLEMENTATION`; the witness must not be silently edited after lane outputs are inspected.

## Scope

This panel is deliberately finite and target-blind. Passing it can only support the preregistered finite scoped certificate. It cannot establish the complete global 4D Weyl3 Euler-Lagrange tensor, quantum closure, or experimental confirmation. `theory_established=0%` remains locked.
