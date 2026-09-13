# Iter051C preregistration — full Weyl^3 EOM assembly/covariance/identity

Date frozen: 2026-09-13
Status at freeze: Iter051B2 terminal PASS already recorded; no Iter051C target results inspected because implementation does not yet exist.

## Gate
`ITER051C-FULL-WEYL3-EOM-ASSEMBLY-COVARIANCE-IDENTITY`

## Scientific target
Assemble the local Euler-Lagrange tensor contribution for the scalar density `sqrt(-g) * c6 * Weyl^3` from the independently certified algebraic metric-density response and Weyl^3 `P(R,g)` connection-response/double-divergence layers, keeping `c6` symbolic/factorized. This gate is the first authorized full-assembly test; it is not a quantum-amplitude or unitarity gate.

## Frozen panel
Use at least 4 independent nondegenerate Lorentzian metric/curvature jet seeds not reused as tuning points. Every lane must retain the same Weyl^3 convention and P convention used by Iter051B1/B2. No symmetry-reduced ansatz is allowed.

## Frozen predicates
A lane is valid only if all structural prerequisites hold:
1. Lorentzian metric determinant is negative and inverse residual <= `1e-11`.
2. Curvature/P algebraic-Riemann residual <= `2e-10`.
3. Both algebraic and double-divergence pieces have Frobenius norm > `1e-8` on non-null lanes so covariance/symmetry tests are nontrivial.
4. Conformally-flat/zero-Weyl control gives assembled Weyl^3 EOM norm <= `5e-9` after the same assembly path.

A valid lane passes only if all scientific predicates hold:
A. **Symmetry:** assembled `E_{mu nu}` antisymmetric residual <= `2e-8` relative Frobenius norm.
B. **Frame covariance:** under each of two predetermined proper Lorentz transformations, transformed direct assembly agrees with tensor-transformed original assembly with relative residual <= `5e-7`.
C. **Independent assembly agreement:** two independently coded index-contraction routes for the algebraic curvature/P part plus the certified double-divergence piece agree with relative residual <= `5e-7`.
D. **Directional metric-density consistency:** contraction of the assembled algebraic (no derivative-of-delta-g) contribution against predetermined symmetric metric directions agrees with the independently evaluated local metric-density directional response to relative residual <= `2e-6`.
E. **c6 factorization:** repeating one predetermined lane with symbolic/numeric scale factors `c6 = 0.37` and `c6 = -1.9` must scale the complete assembled tensor linearly with relative residual <= `2e-12`; no value of c6 is fitted.
F. **Null negative control:** deliberately flipping the sign of the double-divergence term or using a wrong P-index placement must be detected by at least one control residual > `1e-5`; otherwise the gate is invalid because the audit lacks discriminating power.

## Frozen interpretation rule
- All lanes valid and all predicates A–F pass: `PASS_SCOPED_FULL_COVARIANT_WEYL3_EOM_ASSEMBLY_CERTIFICATE`.
- Valid lanes exist but any scientific predicate A–E fails: `SCIENTIFIC_FAIL_G51C_FULL_WEYL3_EOM_ASSEMBLY`.
- Structural prerequisite or discriminating-control F fails: `BLOCKED_OR_INVALID_G51C_ASSEMBLY_AUDIT` unless the first causal failure is demonstrably infrastructure/numerical; such a repair must be separate and may not change this frozen science.

## Scope locks
Even a PASS is a finite-panel computational certificate for the classical six-derivative Weyl^3 Euler-Lagrange assembly. It does not establish QGR as correct, does not fix `c6`, does not authorize `beta=1`, does not prove global identities for arbitrary geometries, does not establish quantum unitarity/absolute energy positivity, and is not experimental confirmation. KMQGB `NEW_REQUIRED` remains unauthorized.
