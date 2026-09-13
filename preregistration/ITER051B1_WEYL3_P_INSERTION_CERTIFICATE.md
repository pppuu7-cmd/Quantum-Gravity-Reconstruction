# Iter051B1 — Weyl^3 P-Insertion Certificate (Prospective Preregistration)

Date frozen: 2026-09-13
Status at freeze: **NO Iter051B1 production result inspected; implementation not yet committed.**

## Scientific question
For the actual four-dimensional cubic Weyl invariant

`I3 = C_ab^{  cd} C_cd^{  ef} C_ef^{  ab}`

at fixed Lorentzian metric, can an explicit curvature covector/tensor insertion `P = d I3 / d R_abcd`, projected onto the algebraic-Riemann subspace, be independently reconstructed and certified before connection-response/full-EOM assembly?

This gate is Weyl^3-specific. A generic rank-4 surrogate or another symmetry reduction is not admissible.

## Frozen construction
Eight independent lanes, `lane=0..7`, with deterministic seeds `6101 + 131*lane`.

For each lane:
1. construct an algebraic Riemann tensor `R_abcd` from an independent metric-second-jet witness using the already validated Iter050 construction;
2. compute `I3(R,g)` at Minkowski metric;
3. reconstruct the unconstrained component derivative by complex-step differentiation of the complete Weyl^3 scalar with step `h = 1e-30` over all 256 covariant Riemann components;
4. project that derivative onto the algebraic-Riemann tensor subspace by pair antisymmetry, pair exchange symmetry, and subtraction of the four-form/first-Bianchi component; call the result `P`;
5. test `P:dR` against an **independent analytic Weyl directional derivative** on six held-out algebraic `dR` witnesses not used to construct `P`;
6. test the cubic Euler/homogeneity identity `P:R = 3 I3`;
7. recompute `P` after two fixed nontrivial Lorentz-frame changes and compare it with the contravariant four-index transformation law implied by `R' = A^T R A ...`;
8. verify algebraic Riemann symmetries/first Bianchi for `P`;
9. use an independently generated conformally-flat curvature witness as a null: because `C=0`, cubic Weyl `I3` and its first curvature derivative must vanish;
10. require a nonzero generic calibration (`|I3|` and `||P||`) so a zero implementation cannot pass.

`c6` is kept symbolic/factored out: this gate certifies the coefficient-free insertion associated with `I3`; it does not determine `c6`.

## Frozen thresholds
A lane is structurally valid only if its input Riemann witness satisfies pair antisymmetry, pair exchange symmetry, first Bianchi and Weyl trace controls within `1e-11` (Weyl trace within `1e-10`).

A lane PASS requires all of:
- `P` algebraic-Riemann symmetry/Bianchi residual `<= 2e-11`;
- worst held-out directional derivative relative residual `<= 2e-10`, with absolute fallback `<= 2e-11` when the reference magnitude is `<1e-8`;
- Euler identity relative residual `<= 2e-10`;
- worst Lorentz-frame `P` covariance relative residual `<= 2e-9`;
- scalar `I3` covariance relative residual `<= 1e-10`;
- conformally-flat null `|I3| <= 1e-11` and `||P||_F <= 2e-10`;
- nonzero calibration `|I3| > 1e-7` and `||P||_F > 1e-6`.

Aggregate PASS requires **8/8 valid and 8/8 lane PASS**. `fail-fast:false` is mandatory.

## Frozen terminal outputs
Only these scientific classifications are permitted:
- `PASS_SCOPED_WEYL3_P_INSERTION_CERTIFICATE`
- `SCIENTIFIC_FAIL_G51B1_WEYL3_P_INSERTION_CERTIFICATE`
- `INFRASTRUCTURE_OR_NUMERICAL_FAIL_G51B1` if the frozen predicates were not actually evaluated.

No threshold may be weakened after viewing production results. A technical implementation failure may be repaired minimally under a new authoritative retry head without changing the frozen science.

## Interpretation lock
Even an 8/8 PASS establishes only a finite numerical/covariant certificate for the **algebraic Weyl^3 curvature insertion** on the frozen generic panel. It does not establish the connection-response/double-divergence of the actual Weyl^3 `P`, does not assemble the complete metric Euler-Lagrange tensor, does not fix `c6`, does not authorize `beta=1`, does not prove positivity/unitarity, and is not experimental confirmation. Theory established remains `0%`.

A PASS authorizes only a separately preregistered Weyl^3-specific **connection-response / covariant derivative** gate before final full-EOM assembly.
