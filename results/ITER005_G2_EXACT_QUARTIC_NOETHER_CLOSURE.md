# QGR Iter005-G2 — exact quartic Noether existence certificate

Date: 2026-09-11
Status: `PASS_SCOPED_EXACT_QUARTIC_NOETHER_EXISTENCE`

## Question

Does the already fixed QGR-L1 quadratic theory plus its independently derived unique cubic self-coupling admit a local two-derivative quartic completion satisfying

`delta_0 S4 + delta_1 S3 = 0`

without inserting a known continuum quartic vertex or fitting a new physical coupling?

## Prospective construction used for the witness

The unreduced QGR-L1 response field is the symmetric second moment

`G in Sym^2(W4)`.

The nonlinear relational-frame rule derived before the cubic Noether solve is the pullback rule, whose expansion gives

`delta_0 h_ij = D_i xi_j + D_j xi_i`

and

`delta_1 h_ij = xi^k D_k h_ij + h_kj D_i xi^k + h_ik D_j xi^k`.

The incidence form is fixed independently as

`C = J-I`.

Using `E=C^{-1}` as the symmetric background response, construct the torsion-free compatible connection of `G=E+h` and the local two-derivative connection-density combination

`sqrt(|det G|) G^{ij} (Gamma^k_{i l} Gamma^l_{j k} - Gamma^k_{ij} Gamma^l_{k l})`.

This object was not selected by comparison with Einstein equations. It is used here as a candidate certificate generator because it is built only from the already selected second-moment field, its inverse, its first derivatives, and the already derived pullback transformation law.

## Lower-order nontrivial checks

The connection density was Taylor-expanded about `E`.

### Quadratic order

Its quadratic Hessian equals the previously selected QGR-L1 Hessian with one overall factor:

`S2_connection = -2 S2_QGR`.

No relative quadratic coefficient was fitted.

### Cubic order

The complete cubic action was expanded in the same deterministic 399 raw `S4` orbit basis used by the independent QGR cubic Noether solve.

After momentum conservation, the fully symmetrized exact cubic vertex contains 8,808 nonzero rational coefficient entries on each side, and

`S3_connection + 2 S3_QGR = 0`

coefficient by coefficient.

Thus the connection-density route reproduces the already independently derived 75-coefficient rational cubic solution with the **same** overall normalization factor as at quadratic order. This is a nontrivial cross-check, not a fitting condition.

## Quartic prediction

The quartic coefficient is therefore fixed by the same expansion; no new quartic coupling is introduced.

In the 2,066 raw quartic `S4` orbit basis, the generated quartic vertex has

- **1,089 nonzero raw orbit coefficients**;
- rational denominators only `1, 2, 4, 8` after normalization to the QGR quadratic/cubic convention.

The known physical quartic action quotient remains 1,694-dimensional before the Noether equation is imposed.

## Exact quartic Noether certificate

The generated `S4` was varied with the already fixed linear transformation `delta_0`. Independently, the already fixed cubic QGR vertex `S3` was varied with the already fixed nonlinear relational pullback term `delta_1`.

Momentum conservation was imposed with one gauge leg and three independent field legs. Both sides were expanded exactly over rational numbers in independent field components, gauge components, and momentum monomials.

Results:

- nonzero coefficients in `delta_0 S4`: **259,596**;
- nonzero coefficients in `delta_1 S3`: **259,596**;
- union support size: **259,596**;
- nonzero coefficients in `delta_0 S4 + delta_1 S3`: **0**.

Therefore

`delta_0 S4 + delta_1 S3 == 0`

holds exactly coefficient by coefficient.

Classification:

`PASS_SCOPED_EXACT_RATIONAL_QUARTIC_NOETHER_EXISTENCE_CERTIFICATE`.

## What this closes

This closes the **existence** part of the quartic blocker: QGR-L1 plus the independently fixed cubic self-coupling has at least one exact local two-derivative quartic continuation with no new fitted physical coefficient.

## What remains open

This result does **not yet** prove:

- that the physical homogeneous quartic Noether kernel is zero;
- uniqueness of `S4` modulo the 372 kinematic/IBP null directions;
- all-orders nonlinear completion;
- weak-background characteristic-cone stability;
- a same-realization refinement/continuum theorem;
- a quantum measure or finite interacting amplitude;
- equivalence principle or experimental predictions;
- an independent KMQGB pass.

The next strict gate is therefore the homogeneous quartic-kernel audit. A known geometric interpretation of the certificate must not be used to skip that audit.

## Reproducibility

`code/qgr_iter005_g2_exact_quartic_noether_certificate.py`
