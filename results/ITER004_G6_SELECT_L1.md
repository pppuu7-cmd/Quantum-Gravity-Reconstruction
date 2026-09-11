# QGR Iter004-G6 — selection of the linearized gauge-closed L1 branch

Date: 2026-09-11
Status: `PASS_SCOPED_UNIQUE_CAUSAL_TWO_MODE_DERIVATIVE_GAUGE_CLOSED_LINEARIZED_BRANCH`

## Starting point

G5 established a natural unreduced ten-component response arena

`Sym^2(W4)`

built from the existing four rank-1 relational directions. The complete local `S4`-invariant quadratic two-derivative Noether problem leaves a two-dimensional family of nonzero Hessians under

`delta h_ij = k_i xi_j + k_j xi_i`.

G6 must select or reject this family **without using continuum GR as the target criterion**.

## Internal QGR selection data fixed before G6

Three pieces of structure were already derived independently:

1. the pair-incidence causal form

   `C = J-I`;

2. its directional characteristic polynomial

   `K_C(k)=k^T C k = 2 sum_{i<j} k_i k_j`;

3. an exact two-dimensional physical quotient in the old Boolean pair sector.

Therefore G6 is allowed to demand that an unreduced linearized theory:

- preserve the previously derived incidence null cone;
- reproduce exactly two physical null modes on that cone, not three or more.

These requirements are independent of any comparison with the Einstein equations.

## Exact two-branch reduction

Choose a deterministic exact rational basis `(H0,H1)` for the two-dimensional derivative-gauge-compatible Hessian space and write

`H(t)=H0+t H1`.

At a fundamental cover covector, e.g. `k=e0`, the gauge directions occupy the components `(00,01,02,03)`. The determinant of the complementary six-dimensional block factorizes exactly as

`det H_phys-like(e0;t) = -(t+1)^4 (2t-1)^2 / 4`.

Hence the condition that a fundamental cover direction be characteristic leaves exactly two projective branches:

- `t=-1`;
- `t=1/2`.

By `S4`, the same statement holds for all four elementary cover directions.

## Two-mode selection

At `t=-1`, the full ten-component Hessian at an incidence-null cover covector has rank **3**. Since the derivative gauge map has four independent directions, the total nullity is seven, i.e. there are **three** additional non-gauge null modes.

At `t=1/2`, the Hessian rank is **4**. The total nullity is six, giving exactly

`6 - 4 = 2`

additional physical null modes beyond gauge.

The `t=-1` branch is therefore inconsistent with the independently derived two-dimensional physical quotient, while `t=1/2` matches it exactly.

Thus, up to overall normalization,

`QGR-L1 := H0 + (1/2) H1`

is uniquely selected within the frozen G5 family.

Classification:

`PASS_SCOPED_UNIQUE_TWO_MODE_BRANCH_SELECTED_BY_PRIOR_QGR_CAUSAL_AND_QUOTIENT_DATA`.

## Nontrivial incidence-cone checks

The selected branch was tested not only on the four coordinate covers but on nontrivial rational covectors satisfying

`K_C(k)=0`.

Examples include

- `(1,1,1,-1)`;
- `(1,2,3,-11/6)`;
- `(2,-1,3,-1/4)`.

At each tested incidence-null covector the selected Hessian has rank **4**.

At representative non-null covectors such as

- `(1,1,1,1)`;
- `(1,2,3,4)`;
- `(1,-1,2,5)`

the rank is **6**.

This is consistent with the selected branch using the previously derived incidence cone as its physical characteristic cone.

## Onsite mass audit

The complete degree-zero `S4`-invariant symmetric mass-matrix space on `Sym^2(W4)` has **7** permutation-orbit coefficients.

Imposing the same derivative Noether identity on that entire onsite space gives constraint rank **7**.

Therefore

`dim allowed nonzero onsite mass deformations = 0`.

This is the first QGR result in which linearized masslessness is structurally protected rather than imposed by setting a parameter to zero.

Classification:

`PASS_SCOPED_DERIVATIVE_NOETHER_SYMMETRY_FORBIDS_ALL_S4_INVARIANT_ONSITE_QUADRATIC_MASS_DEFORMATIONS`.

## A posteriori continuum sanity check — not a selection criterion

Only **after** the QGR-internal selection above, the selected Hessian was compared algebraically with the standard massless Fierz-Pauli quadratic kinetic operator written in the tetrahedral null-frame whose contravariant bilinear form is

`C=J-I`.

They coincide up to an overall normalization.

This is treated solely as an a posteriori consistency check. The Fierz-Pauli form was not used to choose `t=1/2`; choosing it by resemblance to GR would have violated the anti-overfitting constitution.

The coincidence is scientifically useful because it shows that the independently reconstructed linearized sector lands on the known consistent massless spin-2 kinetic structure, but it does **not** establish nonlinear GR, diffeomorphism invariance, or a quantum-gravity theory.

## QGR-L1 status

QGR-L1 is promoted only as

`PROPOSED_LINEARIZED_GAUGE_CLOSED_CAUSAL_TWO_MODE_CANDIDATE`.

Established in scope:

- natural 10-component unreduced second-moment arena from existing rank-1 data;
- local derivative gauge/Noether identity;
- unique branch after incidence-cone + independently derived two-mode selection;
- same incidence characteristic cone on tested nontrivial rational null covectors;
- exactly two additional physical null modes on that cone;
- all `S4`-invariant onsite quadratic mass terms forbidden;
- a posteriori equality, up to scale, to the standard massless spin-2/Fierz-Pauli linear kinetic structure in the `C` null-frame.

Not established:

- nonlinear closure of the gauge/constraint algebra;
- exact microscopic origin of continuum-like local frame transformations beyond the linear response construction;
- interacting self-coupling;
- Einstein equations;
- equivalence principle;
- continuum/refinement theorem;
- finite quantum measure/amplitude definition for the interacting theory;
- normalized observables;
- independent KMQGB pass.

## Iter004 decision

The original Iter004 blocker — lack of a structurally protected massless derivative constraint — is **closed at linearized level** by QGR-L1.

QGR-L0 is retained as the six-component Lorentzian seed but is superseded as the active linearized candidate by QGR-L1.

## Exact next gate

The next scientifically legitimate problem is nonlinear consistency, not further tuning of the quadratic action:

`QGR-ITER005-NONLINEAR-CONSTRAINT-AND-SELF-COUPLING-CLOSURE`.

Required first questions:

1. can the derivative gauge law be generated from finite relational composition beyond first order rather than merely linearized response;
2. does the gauge algebra close without introducing arbitrary functions;
3. does consistent self-coupling force a unique interaction or expose an obstruction;
4. does the nonlinear theory preserve the incidence causal cone / local Lorentz regime;
5. can refinement/coarse-graining be defined on the same realization;
6. fail closed if Einstein-Hilbert is inserted by hand as the interaction.

## Reproducibility

`code/qgr_iter004_g6_select_l1.py`
