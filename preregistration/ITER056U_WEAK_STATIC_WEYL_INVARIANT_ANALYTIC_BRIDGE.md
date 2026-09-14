# Iter056U preregistration — weak-static tidal Hessian to Weyl-invariant analytic bridge

Date: 2026-09-14

Gate: `ITER056U-WEAK-STATIC-TIDAL-HESSIAN-TO-WEYL-INVARIANT-ANALYTIC-BRIDGE`

## Chronology

Hypothesis-generation note committed before this gate:

`15b92915502aebd4accda7d812b8c6ddbc917c74`.

The candidate coefficients and sign convention are frozen by that note and may not be altered after derivation/validation.

## Parent authority

- Iter056S/T establish, conditionally on the G2 Lorentzian/spatial interpretation, an exact spectral-invariant bridge from the source-owned B4 balanced pair sector to the full real symmetric trace-free 3x3 tidal Hessian shape space.
- Iter040/041 numerically establish a calibration-free weak-static Weyl3 response law across diagonal training and generic off-diagonal held-out trace-free tidal Hessians.
- The current gate asks whether the continuum weak-static arrow can be derived analytically at leading weak-field order.

## Frozen metric and conventions

Use signature `eta=diag(+1,-1,-1,-1)` and the continuum metric family already represented by the G3/Iter040 tetrad:

`g_00=1+2 Phi`,

`g_0i=0`,

`g_ij=-(1-2 Phi) delta_ij`,

with

`Phi=(kappa/2) x^i H_ij x^j`,

where `H` is a constant real symmetric trace-free 3x3 matrix.

Treat `kappa` as a formal weak-field amplitude and retain only the linearized Weyl tensor `C^(1)=O(kappa)`. Statements about quadratic/cubic invariants are therefore their leading nonzero orders.

Freeze the linearized Riemann convention:

`R_{rho sigma mu nu}^{(1)} = 1/2 (d_mu d_sigma h_{rho nu} + d_nu d_rho h_{sigma mu} - d_nu d_sigma h_{rho mu} - d_mu d_rho h_{sigma nu})`.

Freeze the cubic contraction to the repository convention:

`J3 = C_ab^{ cd} C_cd^{ ef} C_ef^{ ab}`,

where the last pair on each Weyl factor is raised with `eta` as in `code/qgr_iter010_g2_common.py::weyl_cubic`.

## Frozen theorem predicates

For arbitrary constant symmetric trace-free `H`, derive exactly:

A. `R_00^(1)=0`, `R_0i^(1)=0`, `R_ij^(1)=0`, `R^(1)=0`.

B. Therefore `C^(1)=R^(1)`.

C. For the static observer:

`E_ij = C_0i0j^(1) = -kappa H_ij`.

D. The magnetic Weyl tensor vanishes:

`B_ij = 0`.

E. With

`I2=Tr(H^2)`, `I3=Tr(H^3)`,

the Lorentz-contracted quadratic and frozen cubic invariants satisfy

`J2 := C_abcd C^abcd = 8 kappa^2 I2 + O(kappa^3)`,

`J3 := C_ab^{ cd} C_cd^{ ef} C_ef^{ ab} = 16 kappa^3 I3 + O(kappa^4)`.

The coefficients `8` and `16` and the positive sign of the cubic coefficient are frozen and may not be changed after inspection.

F. For nonzero `H` and positive `kappa`,

`J3/J2^(3/2) -> (1/sqrt(2)) chi`,

where `chi=I3/I2^(3/2)`, and exactly at leading invariant order

`(J3^2/J2^3) -> (1/2) chi2`,

where `chi2=I3^2/I2^3`.

G. Cubic-null tidal shapes `I3=0` remain Weyl-cubic null at leading order while allowing `J2>0` for nonzero H.

## Frozen validation panel

After the generic derivation, validate algebraically on:

1. Iter040 H0=`diag(1,1,-2)`;
2. Iter040 H1=`diag(1,2,-3)`;
3. Iter040 cubic-null H2=`diag(1,-1,0)`;
4. Iter041 off-diagonal G0;
5. Iter041 off-diagonal G3.

These are validation substitutions only; the generic proof must not be inferred from them.

## Frozen negative controls

### Traceful Hessian

Use `H_bad=diag(1,1,1)` in the same metric ansatz. Require the linearized Ricci tensor/scalar not to vanish. This demonstrates that the trace-free restriction is substantive and that one may not replace Riemann by Weyl without Ricci subtraction outside the frozen tidal domain.

### Stationarity / magnetic control

The proof of `B=0` must explicitly use the static `g_0i=0`, `partial_0 h=0` structure. The gate must not generalize `B=0` to boosted/non-static Iter042-like sectors.

## Frozen repository cross-check

The resulting leading-order cubic law may be compared descriptively with Iter040/041's pre-existing numerical facts:

- `W3` amplitude slope approximately 3;
- `W3/Tr(H^3)` shape universality;
- cubic-null transfer.

Those finite-h numerical outputs may not alter the analytic formulas or terminal classification.

Also retain the firewall that Iter040's `np.linalg.norm(W)` is not the Lorentz scalar `sqrt(J2)`.

## Frozen terminal classifications

1. `PASS_SCOPED_ITER056U_LINEARIZED_WEAK_STATIC_WEYL_INVARIANTS_ARE_ANALYTICALLY_CONTROLLED_BY_TIDAL_I2_I3`
   - iff A–G and both negative controls hold exactly under the frozen convention.

2. `SCIENTIFIC_FAIL_ITER056U_WEAK_STATIC_WEYL_INVARIANT_HYPOTHESIS`
   - iff the generic exact derivation contradicts one of the frozen coefficients/signs/predicates while conventions/implementation are valid.

3. `INVALID_AUDIT_ITER056U_CONVENTION_OR_DOMAIN_MISMATCH`
   - iff the metric or contraction convention cannot be matched to the frozen repository definitions well enough to interpret the test.

## Interpretation ceiling

PASS would establish only the leading **linearized weak-static continuum kinematic invariant arrow**

`trace-free tidal Hessian H -> pure-electric Weyl C^(1) -> J2,J3`.

Combined with Iter056T, this would give a conditional kinematic shape chain from the G2 balanced pair sector to continuum weak-static Weyl invariant ratios. It would not establish a same-realization orientation/amplitude map, nonlinear curvature emergence, coefficient matching to `c6`, microscopic dynamics, exact versus order-reduced treatment selection, global measure/regulator removal, quantum unitarity, UV completion, full GR recovery, experiment, new physics, or QGR correctness.

`c6` remains symbolic/unfixed; `beta=1` remains unauthorized; theory established remains 0%.