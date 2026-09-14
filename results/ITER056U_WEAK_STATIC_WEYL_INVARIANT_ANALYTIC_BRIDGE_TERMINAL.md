# Iter056U terminal result — weak-static tidal Hessian to Weyl-invariant analytic bridge

Date: 2026-09-14
Gate: `ITER056U-WEAK-STATIC-TIDAL-HESSIAN-TO-WEYL-INVARIANT-ANALYTIC-BRIDGE`

Hypothesis-generation note: `15b92915502aebd4accda7d812b8c6ddbc917c74`
Prospective preregistration: `727c5305526f03ca373fd035084bfa19ea4bc728`
Exact derivation: `02eb50e397bdbcb999cfe515d4596955c8e45d48`

## Terminal classification

**`PASS_SCOPED_ITER056U_LINEARIZED_WEAK_STATIC_WEYL_INVARIANTS_ARE_ANALYTICALLY_CONTROLLED_BY_TIDAL_I2_I3`**

## Exact leading weak-field result

For the same weak-static continuum metric family used by G3/Iter040,

`Phi=(kappa/2) x^i H_ij x^j`,

with constant real symmetric trace-free tidal Hessian `H`, the frozen linearized Riemann convention gives

`Ric_{mu nu}^{(1)}=0`,

so `C^(1)=R^(1)`.

The static-observer Weyl decomposition is

`E_ij=-kappa H_ij`,

`B_ij=0`.

Writing

`I2=Tr(H^2)`, `I3=Tr(H^3)`,

the leading Lorentz-contracted Weyl invariants are

`J2=C_abcd C^abcd = 8 kappa^2 I2 + O(kappa^3)`,

`J3=C_ab^{ cd} C_cd^{ ef} C_ef^{ ab} = 16 kappa^3 I3 + O(kappa^4)`

under the preregistered/repository cubic contraction convention.

Therefore for positive kappa and nonzero H,

`J3/J2^(3/2) -> (1/sqrt(2)) * I3/I2^(3/2)`,

and

`J3^2/J2^3 -> (1/2) * I3^2/I2^3`.

The weak-field amplitude cancels from these shape ratios.

## Controls

- Cubic-null nonzero trace-free H has nonzero leading `J2` but zero leading `J3`.
- The traceful negative control `H_bad=diag(1,1,1)` has nonzero linearized Ricci tensor and scalar, so the trace-free replacement `C=R` is not valid outside the frozen domain.
- `B=0` depends explicitly on stationarity and `g_0i=0`; no claim is made for boosted/non-static sectors.
- Iter040's Euclidean component `np.linalg.norm(W)` is not reinterpreted as the Lorentz invariant `sqrt(J2)`.

## Relation to previous QGR results

Iter040/041 had already found numerically that, across diagonal training and generic off-diagonal held-out trace-free tidal Hessians,

- Weyl norm scales approximately linearly with kappa;
- the repository Weyl cubic scales approximately as kappa^3;
- `W3/Tr(H^3)` is shape-universal in the tested weak-static panel;
- cubic-null shapes transfer under refinement/rotation.

Iter056U supplies the leading analytic continuum reason for the cubic part of that pattern. The numerical finite-h evidence remains independent and is not reclassified.

Combined with Iter056T, the conditional kinematic invariant chain is now

`B4 G2 balanced pair spectral invariants (I2,I3)`

` == trace-free tidal Hessian spectral invariants (I2,I3)`

` -> leading weak-static Weyl invariants (J2,J3)`.

At the scale-free level,

`chi_B4 = I3/I2^(3/2)`

maps to

`chi_Weyl = J3/J2^(3/2) = chi_B4/sqrt(2)`

in the positive-kappa weak-field limit, conditional on the G2 spatial interpretation.

## Interpretation ceiling

This PASS is an analytic linearized weak-static continuum bridge only. It does not establish:

- a pointwise or orientation-level same-realization microscopic→G3 map;
- an amplitude map from microscopic pair data to kappa;
- `beta=1` or a physical beta value;
- a coefficient identity fixing `c6`;
- nonlinear Weyl curvature emergence from B4;
- microscopic→continuum dynamics;
- a physical exact/order-reduced higher-derivative treatment selector;
- global interacting measure/regulator removal;
- quantum unitarity, UV completion, full GR recovery, experimental confirmation, new physics, or QGR correctness.

Theory established remains `0%`; `c6` remains symbolic/unfixed; `beta=1` remains unauthorized.

## Highest-information successor

The main remaining ambiguity on this new bridge is no longer spectral shape. It is **amplitude/source normalization and same-realization attachment**.

A successor should prospectively ask whether any already-owned B4 quantity supplies an amplitude coordinate for the balanced pair tensor that maps to the weak-static `kappa` without setting `beta=1` or choosing a response unit by convention.

If no such source-owned normalization exists, the correct result is a sharply localized amplitude-map blocker. If a beta-free normalized observable can bypass absolute amplitude while retaining nontrivial Weyl3 sensitivity, test that object instead of forcing a normalization.