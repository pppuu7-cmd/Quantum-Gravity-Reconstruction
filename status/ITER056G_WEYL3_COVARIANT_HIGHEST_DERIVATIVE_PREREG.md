# Iter056G — Weyl3 covariant highest-derivative reduction audit

Status: PROSPECTIVELY FROZEN
Date: 2026-09-14

## TARGET HYPOTHESIS
For the four-dimensional metric functional

S1[g] = integral sqrt(|g|) I3(C),

where I3(C) is the parity-even cubic Weyl scalar already used by QGR and c6 remains symbolic/unfixed, determine whether the apparently fourth-differential-order part of its metric Euler-Lagrange tensor can be reduced, on a lower-order Einstein shell, by covariant Weyl/Bianchi identities and curvature commutators to expressions containing at most first covariant derivatives of Weyl plus algebraic curvature terms.

## EXACT OBJECT
Use the standard diffeomorphism-covariant f(Riemann) Euler-Lagrange form

E_ab = -1/2 g_ab L + P_a{}^{cde} R_{bcde} - 2 nabla^c nabla^d P_{acdb}

with the appropriate symmetric completion implied by the Riemann symmetries, where P^{abcd} = partial L / partial R_abcd. For L=I3(C), P is algebraic and quadratic in Weyl. The audit concerns only the differential-order content of the double-divergence term and its reduction on an Einstein background R_ab = Lambda g_ab (including Lambda=0).

## DEPENDENCY
Iter056E found derivative loss for a naive fixed-Sobolev all-order recursion. Iter056F found no repository-authoritative covariant Weyl3 reduction/tame identity. Iter056G supplies the missing covariant analytic certificate or a sharp obstruction.

## FROZEN IDENTITIES ALLOWED
Only tensor identities valid on every smooth four-dimensional Einstein metric may be used:
- Weyl algebraic symmetries and tracelessness;
- differential Bianchi identity;
- on Einstein metrics, nabla^a C_abcd = 0;
- covariant-derivative commutators;
- consequences derived algebraically from the preceding identities.
No special Petrov type, symmetry reduction, conformal flatness, coordinate gauge, Fourier ansatz, or field equation beyond the lower-order Einstein equation is allowed.

## POSITIVE CONTROL
Recover the known fact that the full double divergence of a tensor linear in Weyl can lose its apparent highest derivatives on an Einstein shell when the divergence-free Weyl identity applies directly.

## NEGATIVE CONTROL
Do not replace nabla C by zero. Only the divergence of Weyl is zero on a generic Einstein metric; generic covariant derivatives of Weyl need not vanish.

## PASS
PASS_SCOPED_ITER056G_EINSTEIN_SHELL_REMOVES_WEYL3_FOURTH_METRIC_DERIVATIVES if the complete double-divergence contribution for P~C*C can be reduced covariantly so that no second covariant derivative of Weyl remains; first-derivative-squared and algebraic curvature terms may remain. This is only a differential-order certificate on Einstein backgrounds, not a convergence theorem or historical physical treatment selector.

## FAIL
SCIENTIFIC_FAIL_SCOPED_ITER056G_IRREDUCIBLE_SECOND_WEYL_DERIVATIVE_REMAINS_ON_GENERIC_EINSTEIN_SHELL if an explicit covariant tensor component/irreducible structure containing a second covariant derivative of Weyl survives all allowed Einstein/Bianchi/commutator identities.

## BLOCKED
BLOCKED_OBJECT_DEFINITION_ITER056G if the exact QGR I3 contraction or P-tensor convention cannot be fixed from repository authority strongly enough to distinguish the complete double-divergence tensor from a surrogate.

## INVALID
INVALID_ITER056G if a special background, gauge, post-hoc identity, or non-frozen field equation is used as if generic.

## INTERPRETATION CEILING
Even PASS does not establish convergence of the c6 expansion, strong hyperbolicity of the full higher-derivative theory, quantum consistency, unitarity, UV completion, a physical exact-vs-order-reduced selector, or a fixed value/running of c6. FAIL concerns only the generic Einstein-shell differential-order reduction of this Weyl3 source.
