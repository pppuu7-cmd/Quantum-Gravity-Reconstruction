# QGR Iter005-G1A — cubic potential census

Date: 2026-09-11
Status: `PASS_SCOPED_ZERO_DERIVATIVE_CUBIC_SECTOR_EXCLUDED`

## Question

Before searching for nonlinear self-coupling, how much purely algebraic cubic freedom is allowed by the finite `S4` symmetry of the QGR-L1 field, and does the already derived derivative gauge symmetry remove it?

## Exact S4 census

The active unreduced field is

`H = Sym^2(W4)`

with character

`chi_H=[10,4,2,1,0]`

on the five conjugacy classes of `S4`.

Using

`chi_Sym3(g) = [chi(g)^3 + 3 chi(g) chi(g^2) + 2 chi(g^3)]/6`,

the symmetric-cube character is

`[220,32,12,4,0]`.

Its trivial-representation multiplicity is exactly

`20`.

Therefore `S4` symmetry alone permits **20 independent zero-derivative cubic invariants** of the ten-component QGR-L1 response field.

This is an important negative control: finite permutation symmetry by itself is far too weak to determine nonlinear dynamics.

## Gauge elimination of the entire potential sector

Now retain the derivative gauge law already selected in Iter004:

`delta_0 h_ij = D_i xi_j + D_j xi_i`.

Consider a constant field configuration `h` and an affine gauge parameter `xi`. Its first difference/gradient is an arbitrary constant `4x4` matrix. The symmetric part therefore spans the entire ten-dimensional space `Sym^2(W4)`.

Hence on constant fields the linear gauge transformation produces an arbitrary constant translation in the ten field components.

A zero-derivative cubic potential `V_3(h)` would have variation

`delta_0 V_3 = (dV_3/dh) . delta_0 h`.

For a derivative quadratic action, constant `h` carries no derivative kinetic term. A local first nonlinear correction to the transformation cannot provide a derivative-action contribution that cancels an arbitrary algebraic variation for every constant `h` and arbitrary constant symmetric gauge shift.

Therefore gauge invariance requires the cubic algebraic potential to be constant. At cubic order this means

`V_3 = 0`.

So all **20/20** `S4`-allowed zero-derivative cubic directions are excluded by the already derived gauge structure.

Classification:

`PASS_SCOPED_20_S4_CUBIC_POTENTIALS_CENSUSED_AND_ALL_EXCLUDED_BY_DERIVED_AFFINE_GAUGE_SHIFT`.

## Scientific consequence

The first nonlinear census does not create a large potential-function freedom. The surviving nonlinear problem is pushed into derivative self-coupling, where a genuine Noether consistency test is required.

This does **not** prove a unique nonlinear completion. It only removes the entire algebraic cubic sector.

## Exact next gate

`QGR-ITER005-G1B-TWO_DERIVATIVE_CUBIC_CENSUS_AND_NOETHER_SYSTEM`

1. enumerate local `S4`-invariant cubic terms with exactly two first-neighbor derivatives;
2. quotient obvious integration-by-parts / field-permutation redundancies;
3. derive the most general first nonlinear gauge correction allowed by relational frame composition;
4. solve `delta_0 S_3 + delta_1 S_2 = 0` as an exact linear system in cubic couplings and gauge-correction coefficients;
5. count surviving coupling directions before any comparison with Einstein-Hilbert.

## Reproducibility

`code/qgr_iter005_g1a_cubic_potential_census.py`
