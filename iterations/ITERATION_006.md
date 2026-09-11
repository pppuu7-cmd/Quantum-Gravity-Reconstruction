# QGR Iteration 006 — Quantum Measure / Composition and Projective Refinement Reconstruction

Date: 2026-09-12
Status: `COMPLETE / REGULAR_REFINEMENT_CONNECTED_STATE_MEASURE_COMPOSITION_LAYER_CLOSED_SCOPED`
Current task completion: **100%**
Candidate-program readiness: **68%**
Active candidate: **QGR-L1**

## Objective

Construct the state/measure/composition layer for QGR without importing the early toy projector, normalized noncompact-Haar averaging, arbitrary history weights, or a separate continuum theory.

The iteration is closed only on the explicit **regular Lorentzian refinement domain**. Degenerate metric configurations and genuine singularities are not declared solved.

## G1 — 24-history normalization

The 24 maximal `B4` histories support

`branch amplitude magnitude = 1/sqrt(24)`

and

`coarse channel weight = 1/24`.

The original `K_alpha=a P_sys` ansatz is retired as fundamental because the physical field sector is a constraint quotient rather than the image of a preferred covariant `10x10` projector.

Classification: `PASS_SCOPED_HISTORY_REGISTER_NORMALIZATION`.

## G2 — state-space reconstruction

### Direct covariance interpretation

For Hermitian `X_i`, a symmetrized second moment is positive semidefinite. Therefore Lorentzian QGR `G` cannot be an ordinary quantum covariance matrix.

Classification: `FAIL_SCOPED_DIRECT_HERMITIAN_COVARIANCE_INTERPRETATION_OF_G`.

### Positive kinematic state space

Define

`Q_13={G=G^T | signature(G)=(1,3), det G != 0}`.

The congruence action `G->A^T G A` has `Sym^2` Jacobian `|det A|^5`, while `|det G|` gains `|det A|^2`. Hence

`dmu(G)=|det G|^(-5/2)d^10G`

is congruence invariant and

`H_kin=L^2(Q_13,dmu)`

is a natural positive kinematic Hilbert space.

### Physical quotient at the symmetric seed

For every fundamental cover covector `e_i`,

- `rank H=4`;
- `dim ker H=6`;
- `rank R=4`;
- `im R subset ker H`.

Thus

`dim[ker H/im R]=2`.

The four-cover seed physical space has dimension `8`. `S4` acts unitarily between physical quotient fibers and is a symmetry, not the field-gauge projector.

Records:

- `results/ITER006_G2_STATE_SPACE_AND_PROJECTOR_AUDIT.md`
- `results/ITER006_G2C_SEED_PHYSICAL_HILBERT_AND_UNITARY_HISTORY.md`

## G3 — history transport from the same response field

The first jets `D_iG_jk` determine the torsion-free compatible connection

`Gamma^k_ij=(1/2)G^{kl}(D_iG_lj+D_jG_li-D_lG_ij)`.

Thus history ordering differs through curvature/holonomy of the same QGR connection rather than arbitrary branch functions.

Invertible quasi-invariant configuration maps admit the linear Koopman/Radon-Nikodym lift

`(U_alpha psi)(G)=[d(F_alpha*mu)/dmu(G)]^(1/2) psi(F_alpha^-1 G)`.

Composition is exact.

Records:

- `results/ITER006_G3A_DERIVED_HISTORY_TRANSPORT.md`
- `results/ITER006_G3B_CONTROLLED_CONFIGURATION_TRANSPORT.md`

## G4 — finite frame/holonomy lift

The response can be lifted as

`G=F^T C F`, `Q_13 ~= O(C)\GL(4)`, `16-6=10`.

For edge `v->w`,

`A_wv=F_w^-1 L_wv F_v`

is internal-Lorentz gauge invariant and satisfies

`A_wv^T G_w A_wv=G_v`.

The six-dimensional endpoint ambiguity is the Lorentz connection fiber, not six new physical couplings.

Record: `results/ITER006_G4_FRAME_HOLONOMY_LIFT.md`.

## G5 — local finite torsion-free uniqueness

The finite plaquette equation is

`e_i(v)+L_i^-1 e_j(v+i)=e_j(v)+L_j^-1 e_i(v+j)`.

At the symmetric seed its exact `24x24` connection Jacobian has

- rank `24`;
- determinant `11664` in the recorded rational Lie-algebra basis;
- zero homogeneous kernel.

Hence the identity-connected root is locally unique by the implicit-function theorem.

Record: `results/ITER006_G5_DISCRETE_LEVI_CIVITA_UNIQUENESS.md`.
Code: `code/qgr_iter006_g5_discrete_torsion_rank.py`.

## G6/G7 — curved coarse observable algebra

A local coarse state containing only `G` loses loop holonomy and is not projectively closed.

Classification: `FAIL_SCOPED_GENERIC_CURVED_G_ONLY_PROJECTIVE_CLOSURE`.

The exact strong-curvature repair is the path-groupoid data

`X_Gamma={(G_v,A_e) | A_e^T G_t A_e=G_s}`.

For path `p=e_n...e_1`,

`A_p=A_(e_n)...A_(e_1)`.

Coarse blocking is exact and associative. Loop holonomy is retained. On a connected graph, a spanning-tree description leaves `b1=E-V+1` fundamental cycle holonomies.

In the weak-curvature local limit the off-shell Levi-Civita curvature sector has `20` independent components after Riemann symmetries and first Bianchi.

Records:

- `results/ITER006_G6_PROJECTIVE_CLOSURE_AND_HOLONOMY.md`
- `results/ITER006_G7A_WEAK_CURVATURE_OBSERVABLE_COUNT.md`
- `results/ITER006_G7B_STRONG_CURVATURE_PATH_GROUPOID_CLOSURE.md`

## G8 — normalized quantum composition and physical algebra

For each history,

`K_alpha=24^(-1/2) exp(iS_alpha/hbar) U_alpha`.

On the verified real-action domain,

`sum K_alpha^dagger K_alpha=I`.

Thus the coherent history-register map is an isometry and the traced coarse map is CPTP, with no free branch modulus.

The exact pullback algebra gives the nilpotent BRST differential

`sG=L_cG`, `sc=-(1/2)[c,c]`, `s^2=0`.

Physical observables are represented algebraically by `H^0(s)`. Physical states may be taken operationally as positive normalized functionals on the physical `*`-algebra. Gauge-covariant CPTP blocking preserves positivity and normalization.

Records:

- `results/ITER006_G8A_NORMALIZED_INTERACTING_HISTORY_INSTRUMENT.md`
- `results/ITER006_G8C_BRST_CONSTRAINT_DESCENT.md`
- `results/ITER006_G8D_OPERATIONAL_PHYSICAL_POSITIVITY.md`

## G8B — coarea branch measure: scope correction

The regular-root coarea expression

`w_r proportional to j_Haar(L_r)/|det(dT/domega)_r|`

is mathematically valid as a diagnostic for isolated auxiliary roots, but G10 shows that **summing all coarse torsion roots is not the physical connection prescription**. The connection was already fixed as a derived object by the first-jet Levi-Civita construction.

Therefore G8B is retained as a local diagnostic, not as a fundamental sum over disconnected finite-cell connection branches.

Record: `results/ITER006_G8B_REGULAR_STRATUM_RIGGING_AND_BRANCH_MEASURE.md`.

## G9 — genuinely curved nonlinear branch

A deterministic noninfinitesimal conformal-frame toy has a regular identity-connected nonlinear torsion root with

- residual about `2e-14`;
- parameter norm about `0.468`;
- smallest Jacobian singular value about `0.349`;
- condition number about `23.1`;
- six nonzero plaquette holonomies with `||H-I||` about `0.129..0.249`;
- metric-preservation error about `1e-15`;
- `12/12` local restarts returning to the same branch.

Classification: `NUMERICALLY_VERIFIED_FINITE_CURVATURE_REGULAR_TORSION_BRANCH_WITH_NONZERO_HOLONOMY`.

Record: `results/ITER006_G9_FINITE_CURVATURE_TORSION_BRANCH_AUDIT.md`.

## G10A — global all-root finiteness is false

At the exact flat seed eliminate the Lorentz matrices by defining

`y_ij=L_i^-1 e_j`.

Torsion gives

`y_ij-y_ji=e_j-e_i`.

Using six unordered vectors leaves `24` variables. Preservation of the three-vector Gram matrix at each vertex gives exactly `24` quadratic equations.

The identity solution is regular: the reduced Jacobian has exact determinant

`47,775,744 = 2^16 * 3^6`.

However the same system also contains disconnected singular branches. A recorded rank-22 root was continued for 50 predictor/corrector steps while maintaining full residual of order `1e-14`; the solution norm grew from about `10.93` to above `30.2` while rank remained `22`.

Thus there is a noncompact two-dimensional torsion solution manifold already at the flat seed.

Classification:

`REFUTED_IN_SCOPE_ALL_TORSION_ROOTS_FINITE__DISCONNECTED_NONCOMPACT_FINITE_CELL_BRANCH_EXISTS`.

This is an explicit negative result and is retained as such.

Records:

- `results/ITER006_G10A_GLOBAL_TORSION_BRANCH_COUNTEREXAMPLE.md`
- `code/qgr_iter006_g10a_seed_runaway_branch.py`

## G10B — physical connection survives through refinement matching

The G10A counterexample does **not** invalidate the physical QGR connection because the latter was fixed before G10 by the same-realization chain

`G,DG -> infinitesimal compatible connection -> finite transport`.

On the exact flat seed `DG=0`; therefore the physical finite branch must approach `L=I`. The disconnected noncompact branches fail this already-fixed requirement.

### Regular refinement-domain theorem

For a regular Lorentzian frame field on a compact patch with bounded frame, inverse frame, and first/second jets, normalize each sufficiently small cell by its local frame. At `h=0` the torsion problem is the regular symmetric seed. The parameter-dependent implicit-function theorem therefore yields a unique identity-connected local root for sufficiently small `h`, uniformly on the compact patch.

Its expansion is

`L_e(h)=I+h omega_e[G,DG]+O(h^2)`,

where `omega_e` is fixed by the linearized torsion equation and is the same Levi-Civita connection already obtained from the QGR first jets.

Strong-curvature coarse transport is **not** defined by re-solving the coarse polynomial. It is the ordered product of the fine principal transports. Standard product-integral convergence then gives the path-ordered connection transport as mesh size tends to zero.

### Numerical refinement certificate

On the G9 curved conformal family, for

`h=1,1/2,1/4,1/8,1/16`,

identity-connected solves give approximately

`max ||L-I|| = 0.5692, 0.2906, 0.1485, 0.07519, 0.03785`.

The observed order tends to one. At `h=1/16`, the scaled finite connection differs from the independently solved linearized connection by about `0.0066` in the recorded 24-parameter norm.

For a fixed physical path subdivided into `N=1,2,4,8,16` cells, successive product differences are approximately

`0.0338, 0.0185, 0.00972, 0.00499`.

Classification:

`PASS_SCOPED_REGULAR_REFINEMENT_CONNECTED_DISCRETE_LEVI_CIVITA_TRANSPORT_EXISTS_AND_DEFINES_STRONG_CURVATURE_COARSE_TRANSPORT_BY_PRODUCT_LIMIT`.

Records:

- `results/ITER006_G10B_REFINEMENT_CONNECTED_PRINCIPAL_CONNECTION.md`
- `code/qgr_iter006_g10b_refinement_connected_transport.py`

## Iter006 conclusion

The state/measure/composition/refinement layer is closed **for regular Lorentzian configurations with controlled refinement**:

1. positive kinematic state space exists;
2. physical gauge content is a quotient/BRST algebra, not a toy projector;
3. exact path-groupoid coarse observables retain strong-curvature holonomy;
4. normalized coherent history composition is isometric and coarse evolution CPTP;
5. the derived connection has a unique local identity-connected root and a controlled refinement/product limit;
6. global summation over every algebraic coarse torsion root is explicitly rejected by counterexample, not silently assumed away.

## Remaining claim locks

Iter006 does **not** establish:

- all-orders local nonlinear QGR dynamics;
- a full continuum/RG theorem for the interacting field measure;
- a normalized phenomenological observable/comparator;
- equivalence principle corrections or experimental prediction;
- an independent KMQGB pass;
- KMQGB `NEW_REQUIRED`.

Degenerate `det G=0` and genuine singular configurations remain outside the regular refinement theorem.

## Progress accounting

- Iter006 completion: **100%**.
- Candidate-program readiness: **68%**.
- These are construction-roadmap metrics, not probabilities of correctness.
