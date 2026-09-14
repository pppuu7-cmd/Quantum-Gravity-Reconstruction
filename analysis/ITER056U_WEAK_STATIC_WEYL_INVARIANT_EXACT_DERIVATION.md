# Iter056U exact derivation — weak-static tidal Hessian controls leading Weyl invariants

Date: 2026-09-14
Preregistration: `727c5305526f03ca373fd035084bfa19ea4bc728`
Hypothesis chronology: `15b92915502aebd4accda7d812b8c6ddbc917c74`

## 1. Frozen metric perturbation

Use `eta=diag(+1,-1,-1,-1)` and

`g_00=1+2 Phi`,

`g_0i=0`,

`g_ij=-(1-2 Phi) delta_ij`,

with

`Phi=(kappa/2) x^i H_ij x^j`,

where `H=H^T` is constant and `Tr(H)=0`.

Thus the metric perturbation is

`h_00=2 Phi`,

`h_0i=0`,

`h_ij=2 Phi delta_ij`.

All time derivatives vanish and

`partial_i partial_j Phi = kappa H_ij`.

The derivation below is exact at linear order in the metric perturbation. The full weak metric has nonlinear curvature corrections starting at `O(kappa^2)`.

## 2. Linearized Riemann tensor

With the preregistered convention

`R_{rho sigma mu nu}^{(1)} = 1/2 (d_mu d_sigma h_{rho nu} + d_nu d_rho h_{sigma mu} - d_nu d_sigma h_{rho mu} - d_mu d_rho h_{sigma nu})`,

direct substitution gives

`R_{0i0j}^{(1)} = -kappa H_ij`,

`R_{0ijk}^{(1)} = 0`,

and

`R_{ijkl}^{(1)} = kappa (delta_il H_jk + delta_jk H_il - delta_ik H_jl - delta_jl H_ik)`.

These formulas are tensorial under constant spatial orthogonal rotations.

## 3. Linearized Ricci-flatness is exactly the trace-free condition

Contracting with `eta`, before imposing trace-free H, gives

`Ric_{00}^{(1)} = kappa Tr(H)`,

`Ric_{0i}^{(1)} = 0`,

`Ric_{ij}^{(1)} = kappa Tr(H) delta_ij`,

and

`R_scalar^{(1)} = -2 kappa Tr(H)`.

Therefore the frozen tidal condition `Tr(H)=0` implies

`Ric_{mu nu}^{(1)}=0`, `R_scalar^{(1)}=0`.

Hence throughout the allowed domain

`C_{abcd}^{(1)}=R_{abcd}^{(1)}`.

This proves preregistered predicates A and B.

## 4. Electric and magnetic Weyl parts

For the static frame,

`E_ij := C_{0i0j}^{(1)} = -kappa H_ij`.

Because every `C_{kl0j}^{(1)}` vanishes in this static `g_0i=0`, `partial_0 h=0` ansatz,

`B_ij := (1/2) epsilon_i^{ kl} C_{kl0j}^{(1)} = 0`.

Thus the leading Weyl tensor is purely electric and its electric tidal tensor is exactly the frozen Hessian up to the universal factor `-kappa`.

This proves C and D. The argument explicitly depends on stationarity and cannot be transferred to boosted/non-static sectors.

## 5. Quadratic invariant coefficient

Because `H` is real symmetric, choose a spatial orthogonal frame in which

`H=diag(lambda1,lambda2,lambda3)`, `lambda1+lambda2+lambda3=0`.

The Lorentz scalar

`J2=C_abcd C^abcd`

is invariant under this spatial rotation. Direct contraction of the diagonal pure-electric components gives

`J2^{leading}=8 kappa^2 (lambda1^2+lambda2^2+lambda3^2)`.

Therefore for arbitrary trace-free symmetric H,

`J2 = 8 kappa^2 Tr(H^2) + O(kappa^3)`.

Writing `I2=Tr(H^2)`, the preregistered coefficient `8` is confirmed exactly.

## 6. Cubic invariant coefficient in the repository convention

Use exactly the preregistered/repository contraction

`J3=C_ab^{ cd} C_cd^{ ef} C_ef^{ ab}`,

with the last pair of each Weyl factor raised by `eta`, matching `qgr_iter010_g2_common.py::weyl_cubic`.

In the same diagonal spatial frame, direct contraction gives

`J3^{leading}=16 kappa^3 (lambda1^3+lambda2^3+lambda3^3)`.

Hence for arbitrary trace-free symmetric H,

`J3 = 16 kappa^3 Tr(H^3) + O(kappa^4)`.

Writing `I3=Tr(H^3)`, the frozen coefficient `16` and its sign are confirmed under the preregistered Riemann convention.

This also analytically explains the two central numerical signatures of Iter040/041: cubic amplitude power approximately 3 and a shape-independent leading ratio `W3/Tr(H^3)` at fixed kappa.

## 7. Scale-free invariant bridge

For nonzero H and positive kappa,

`J3/J2^(3/2)`

has leading weak-field limit

`[16 kappa^3 I3] / [8 kappa^2 I2]^(3/2)`

`= (1/sqrt(2)) I3/I2^(3/2)`.

Thus with

`chi=I3/I2^(3/2)`,

we obtain

`J3/J2^(3/2) -> chi/sqrt(2)`.

Squaring removes all sign and square-root convention issues:

`J3^2/J2^3 -> (1/2) I3^2/I2^3 = chi2/2`.

This is a calibration-free leading continuum relation. The overall weak-field amplitude kappa cancels exactly from the limiting shape ratio.

## 8. Cubic-null family

If `I3=0` but `H != 0`, then

`J3=O(kappa^4)`

while

`J2=8 kappa^2 I2+O(kappa^3)`

with `I2>0` for a nonzero real symmetric H.

Therefore the trace-free cubic-null family has nonzero leading Weyl curvature but zero leading Weyl cubic invariant. This is exactly the analytic structure tested numerically by Iter040 H2 and Iter041's rotated null controls.

## 9. Frozen validation substitutions

### Iter040 H0 = diag(1,1,-2)

`I2=6`, `I3=-6`.

Predicted:

`J2=48 kappa^2+O(kappa^3)`,

`J3=-96 kappa^3+O(kappa^4)`.

### Iter040 H1 = diag(1,2,-3)

`I2=14`, `I3=-18`.

Predicted:

`J2=112 kappa^2+O(kappa^3)`,

`J3=-288 kappa^3+O(kappa^4)`.

### Iter040 H2 = diag(1,-1,0)

`I2=2`, `I3=0`.

Predicted:

`J2=16 kappa^2+O(kappa^3)`,

`J3=O(kappa^4)`.

### Iter041 off-diagonal G0

From Iter056T exact held-out arithmetic:

`I2=399/200`, `I3=5901/8000`.

Predicted:

`J2=(399/25) kappa^2+O(kappa^3)`,

`J3=(5901/500) kappa^3+O(kappa^4)`.

### Iter041 off-diagonal G3

`I2=403/200`, `I3=-2109/8000`.

Predicted:

`J2=(403/25) kappa^2+O(kappa^3)`,

`J3=-(2109/500) kappa^3+O(kappa^4)`.

The off-diagonal cases require no special calculation beyond the generic theorem because spatial orthogonal diagonalization leaves the scalar contractions invariant.

## 10. Traceful negative control

Take the preregistered

`H_bad=diag(1,1,1)`.

Then `Tr(H_bad)=3`, so before Weyl trace subtraction

`Ric_{00}^{(1)}=3 kappa`,

`Ric_{ij}^{(1)}=3 kappa delta_ij`,

`R_scalar^{(1)}=-6 kappa`.

Thus `Riemann != Weyl` and the pure trace-free tidal formulas cannot be applied. This confirms that the trace-free restriction is substantive rather than cosmetic.

## 11. Stationarity negative-domain control

The vanishing magnetic part followed from `h_0i=0` and `partial_0 h=0`. A boost or genuine time dependence creates mixed curvature components and can give nonzero magnetic Weyl. Therefore this derivation explicitly does not subsume the later Iter042 boosted magnetic-Weyl sector.

## 12. Norm firewall

Iter040 records `weyl_norm=np.linalg.norm(W)`, the Euclidean component norm of the finite Weyl array. That diagnostic is **not** `sqrt(J2)` in Lorentz signature.

Accordingly this proof analytically controls:

- the repository cubic contraction `J3`;
- the Lorentz scalar `J2` defined here;
- their invariant ratio.

It does not re-interpret Iter040's Euclidean array norm as a Lorentz scalar.

## Frozen classification supported by the derivation

`PASS_SCOPED_ITER056U_LINEARIZED_WEAK_STATIC_WEYL_INVARIANTS_ARE_ANALYTICALLY_CONTROLLED_BY_TIDAL_I2_I3`

## Interpretation ceiling

This is a leading linearized weak-static continuum result only. It does not identify microscopic and continuum amplitudes, prove nonlinear curvature emergence, fix `beta` or `c6`, establish a micro→continuum dynamical map, choose exact versus order-reduced higher-derivative dynamics, prove global measure/regulator removal, quantum unitarity, UV completion, full GR recovery, experiment, new physics, or QGR correctness.