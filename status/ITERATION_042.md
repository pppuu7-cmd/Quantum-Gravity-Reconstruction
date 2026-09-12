# Iteration 042 — Lorentz-boosted non-static / magnetic-Weyl covariance gate

Date: 2026-09-12
Status: `PREREGISTERED / READY FOR IMPLEMENTATION`

## Motivation

Iter040 established a calibration-free Weyl^3 response law on frozen weak static tidal profiles. Iter041 then transferred that law prospectively to held-out generic off-diagonal trace-free tidal tensors, rotated nulls and held-out rotations (24/24 PASS). Further densification of the same static electric-tidal family is therefore low-information.

Iter042 moves to a genuinely new **observer / coordinate sector without adding fields**. Start from the same authorized weak static vacuum tidal metric and apply a global Lorentz boost to the Minkowski coordinates. In the boosted coordinates the same geometry has:

- time-space off-diagonal metric/tetrad components;
- explicit coordinate-time dependence of the tidal profile;
- a nonzero magnetic Weyl part for generic boosted observers;
- unchanged continuum scalar Weyl invariants.

This is a covariance and magnetic-Weyl bridge, not yet a new independent radiative spacetime.

No `beta` or `c6` fitting occurs. No new field components are introduced beyond the existing ten-component symmetric metric / second-moment arena and existing six-generator connection/torsion closure.

## Frozen construction

Use Minkowski signature `eta=diag(1,-1,-1,-1)` and the existing static tidal tetrad in Minkowski coordinates,

`F_old(y)=diag(sqrt(1+2 Phi(y)), sqrt(1-2 Phi(y)), sqrt(1-2 Phi(y)), sqrt(1-2 Phi(y)))`,

with

`Phi(y)=(kappa/2) y_spatial^T H y_spatial`,

for a symmetric trace-free spatial Hessian H.

For a frozen boost velocity vector `v`, define the standard Lorentz matrix `Lambda(v)` by

- `gamma=(1-|v|^2)^(-1/2)`;
- `Lambda_00=gamma`;
- `Lambda_0i=Lambda_i0=-gamma v_i`;
- `Lambda_ij=delta_ij + (gamma-1) v_i v_j / |v|^2`.

Let `y_old = Lambda(v)^(-1) y_new` and freeze the boosted tetrad

`F_boost(y_new) = F_old(y_old) Lambda(v)^(-1)`.

Then exactly at the metric level

`g_boost(y_new)=Lambda(v)^(-T) g_old(y_old) Lambda(v)^(-1)`.

Map this tetrad into the existing QGR barycentric basis exactly as in G40/G41 and solve the same nonlinear torsion closure. The finite-cell curvature/Weyl proxy is unchanged except for this boosted tetrad source.

## Frozen source shapes

Use two already-authorized non-null shapes only as underlying geometries:

- `H0 = diag(1,1,-2)` from G40;
- `G0 = [[1.00,0.35,-0.20],[0.35,-0.25,0.15],[-0.20,0.15,-0.75]]` from the **held-out** G41 set.

Their purpose here is not another shape scan; it is to provide two geometrically distinct controls for the new boost/magnetic sector.

## Frozen boost vectors

Primary boosts:

- `V0=(0.15,0,0)`;
- `V1=(0.25,0,0)`;
- `V2=(0,0.20,0)`;
- `V3=(0.16,0.12,0.08)`.

All velocities are in units c=1 and have norm < 0.3.

Frozen small-velocity magnitude grid for velocity-response lanes:
`speed=[0.08,0.12,0.18,0.24]`.

Frozen G0 direction vectors for the velocity-response family:
- `d0=(1,0,0)`;
- `d1=(0,1,0)`;
- `d2=(0,0,1)`;
- `d3=(1,1,1)/sqrt(3)`.

## Frozen electric / magnetic diagnostics

From the all-lowered finite-cell Weyl proxy in the boosted Minkowski frame define

`E_ij = C_{0 i 0 j}`

and diagnostic magnetic part

`B_ij = (1/2) epsilon_{i k l} C_{k l 0 j}`

with spatial indices i,j,k,l in {1,2,3} and the ordinary orientation `epsilon_123=+1`.

The magnetic diagnostic is used only for observer-sector emergence/parity/scaling. Scalar Lorentz-covariance promotion uses separately contracted Weyl invariants, not Euclidean E/B norms.

Define the quadratic scalar proxy by raising all four indices with eta:

`W2 = C_abcd C^abcd`.

Retain the existing G40 cubic scalar `W3`.

## Inherited numerical controls

Every scientific lane requires:
- torsion residual `<3e-9`;
- minimum connection-Jacobian singular value `>1e-8`;
- metric compatibility error `<1e-7`;
- finite curvature/Weyl values;
- exact boost Lorentz check `||Lambda^T eta Lambda-eta|| < 1e-12`;
- direct tetrad-metric boost identity error `<1e-11` at all checked sample points.

Control failure is not scientific FAIL.

## Stream A — magnetic-Weyl emergence (6 lanes)

Use `(H0,V0)`, `(H0,V1)`, `(H0,V3)`, `(G0,V0)`, `(G0,V2)`, `(G0,V3)` at `h=0.05`, `kappa=0.04`.

Each lane also evaluates its own v=0 control at identical h,kappa,H.

PASS requires:
- inherited controls valid;
- boosted magnetic norm `||B_boost|| > 1e-8`;
- magnetic-to-electric ratio `||B_boost||/max(||E_boost||,1e-30) > 0.01`;
- boosted magnetic norm exceeds the unboosted magnetic norm by a factor > 5, unless unboosted `||B||<1e-10`, in which case only `||B_boost||>1e-8` is required.

This establishes a nontrivial magnetic observer sector numerically; it does not establish a new physical spacetime.

## Stream B — scalar Lorentz-invariance under refinement (6 lanes)

Use the same six `(H,V)` pairs as Stream A at `h=[0.10,0.075,0.05]`, fixed `kappa=0.04`.

At each h compare boosted and unboosted scalar proxies `W2` and `W3`.

PASS requires:
- inherited controls valid at all h;
- finest relative W2 discrepancy `<0.05`;
- finest relative W3 discrepancy `<0.05`;
- each discrepancy decreases coarse -> fine, or both its coarse and fine values are already `<1e-3`.

This is finite-cell covariance evidence only; it is not an analytic Lorentz-invariance theorem for the full QGR construction.

## Stream C — boost-reversal magnetic parity (4 lanes)

Use `(H0,0.15*x)`, `(H0,0.20*y)`, `(G0,0.15*x)`, `(G0,0.16*x+0.12*y+0.08*z)` at `h=[0.10,0.075,0.05]`, `kappa=0.04`, evaluating both +v and -v.

For each h define

`parity_error = ||B(+v)+B(-v)|| / max(0.5*(||B(+v)||+||B(-v)||),1e-30)`.

PASS requires inherited controls, nonzero magnetic norms for both signs, finest parity error `<0.10`, and error decreases coarse -> fine or both coarse/fine are `<1e-3`.

The frozen expectation is odd magnetic response under boost reversal for an originally purely-electric static tidal geometry, up to finite-cell errors.

## Stream D — boosted amplitude law (4 lanes)

Use `(H0,V0)`, `(H0,V3)`, `(G0,V0)`, `(G0,V3)` at fixed `h=0.05` and
`kappa=[0.025,0.04,0.06,0.08,0.10]`.

PASS requires inherited controls and log-log slopes:
- boosted `|W3|` vs kappa in `[2.70,3.30]`;
- boosted `||B||` vs kappa in `[0.80,1.20]`.

## Stream E — small-velocity magnetic response (4 lanes)

Use G0 and directions d0,d1,d2,d3. For each lane evaluate speeds `[0.08,0.12,0.18,0.24]` at `h=0.05`, `kappa=0.04`.

PASS requires:
- inherited controls valid;
- every nonzero-speed magnetic norm `>1e-8`;
- `||B||` strictly increases over the frozen speed grid;
- endpoint growth `||B(0.24)||/||B(0.08)|| > 2.0`.

No exact power-law exponent is required because finite Lorentz transformation is not exactly linear at these velocities.

## Production matrix

- A magnetic emergence: 6 lanes;
- B scalar covariance/refinement: 6 lanes;
- C boost parity: 4 lanes;
- D boosted amplitude law: 4 lanes;
- E velocity response: 4 lanes;
- total **24 scientific lanes** + aggregate;
- `fail-fast:false`;
- safe maximum parallelism up to 24.

## Terminal classifications

Full PASS:
`PASS_SCOPED_NONSTATIC_MAGNETIC_WEYL_LORENTZ_COVARIANCE_BRIDGE`
if all 24 frozen lanes pass with valid controls.

Partial scientific result:
`PARTIAL_SCOPED_NONSTATIC_MAGNETIC_WEYL_COVARIANCE`
if controls are valid but at least one frozen scientific relation fails.

Control-invalid:
`CONTROL_INVALID_OR_INCOMPLETE_ITER042`
if expected lanes are missing or boost/torsion/metric controls invalidate interpretation.

## Decision logic after terminal result

- Full PASS: the boosted observer sector is a successful bridge but not an independent dynamical spacetime. Do not keep scanning boosts. Next gate must introduce a genuinely independent time-dependent/radiative or magnetic-Weyl geometry (e.g. a preregistered weak TT-wave / non-collinear wave superposition or another independently derived vacuum curvature family) and test same-field torsion/refinement there.
- Partial: localize whether magnetic emergence, scalar covariance, parity, amplitude or velocity behavior fails; do not weaken thresholds.
- Control invalid: repair implementation/control only; do not make scientific claims.

## Claim locks

- theory established remains **0%**;
- a boosted static spacetime is not a new dynamical solution even though its coordinate representation is time-dependent and its magnetic Weyl part is observer-dependent;
- finite-cell covariance evidence is not a global Lorentz-covariance theorem;
- `beta` remains an explicit matching/calibration parameter under Iter039;
- `beta=1` is not authorized as physics;
- `c6` remains unfixed and is not fitted here;
- no experimental confirmation;
- no physical branch weights from G35–G37 distant roots;
- KMQGB `NEW_REQUIRED` remains unauthorized absent independent benchmark authority.
