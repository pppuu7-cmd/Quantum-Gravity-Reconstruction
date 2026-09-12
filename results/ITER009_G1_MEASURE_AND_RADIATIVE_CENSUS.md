# QGR Iter009 G1 — interacting-measure obstruction and radiative operator census

Date: 2026-09-12
Status: `BLOCKED_SCOPED_NAIVE_GLOBAL_VACUUM_WEIGHT / FINITE_OPERATOR_ROUTE_REMAINS_OPEN / HIGHER_DERIVATIVE_CLOSURE_OPEN`

GitHub Actions run `34662453224`: five lanes + aggregate `SUCCESS`.

## G1-1 — invariant scale-orbit measure

The QGR kinematic reference measure

`dmu(G)=|det G|^(-5/2) d^10G`

is invariant under global positive scaling `G -> s^2 G`. The corresponding subgroup is `R_+` with Haar measure

`ds/s = d(log s)`.

Its invariant volume is infinite in both logarithmic directions. Therefore the measure is a valid positive reference measure for `L^2(Q_13,dmu)` but is not, by itself, a normalized global vacuum probability distribution.

Classification:
`BLOCKED_SCOPED_CONGRUENCE_INVARIANT_Q13_MEASURE_HAS_INFINITE_NONCOMPACT_SCALE_ORBIT_VOLUME_AND_IS_NOT_A_NORMALIZED_GLOBAL_VACUUM_PROBABILITY_MEASURE`.

## G1-2 — exact flat scale zero mode

On the uniform family

`G_v=s^2 E`

for every vertex/cell, all finite differences vanish. The refinement-connected torsion-free connection is flat, curvature is zero, and the active zero-cosmological local action is exactly zero. Hence

`exp(iS/hbar)=1`

for the entire noncompact scale orbit.

The Lorentzian action phase therefore does not even provide oscillatory suppression of this exact mode. Combining the invariant measure with the action phase as the naive weight `exp(iS/hbar)dmu` does not cure the noncompact scale-volume obstruction.

Classification:
`BLOCKED_SCOPED_LORENTZIAN_ACTION_PHASE_DOES_NOT_REGULARIZE_THE_UNIFORM_FLAT_SCALE_ZERO_MODE`.

This does **not** rule out operator/algebraic quantum dynamics or normalized `L^2` states.

## G1-3 — Z2 refinement superselection

The two global flat line-bundle sectors are the two characters of `pi_1(Q_13)=Z2`.

Every configuration-space map homotopic to the identity induces the identity automorphism on `Z2`, and therefore preserves each character separately. The verified regular refinement-connected transport is identity-connected.

Thus, within this transport class, local/history evolution is block diagonal in the global `Z2` label.

Classification:
`PASS_SCOPED_REFINEMENT_CONNECTED_IDENTITY_HOMOTOPY_TRANSPORT_PRESERVES_THE_TWO_Z2_FLAT_QUANTUM_SECTORS_AS_SUPERSELECTION_SECTORS`.

## G1-4 — four-derivative local metric census

At four derivatives, parity-even local curvature-squared densities may be represented by

- `Riemann^2`,
- `Ricci^2`,
- `R^2`.

In four dimensions the Euler density

`E4=Riemann^2-4 Ricci^2+R^2`

removes one bulk direction modulo topology, while `Box R` is a total derivative. Therefore the parity-even local bulk quotient has dimension **2**.

Classification:
`BLOCKED_SCOPED_TWO_INDEPENDENT_PARITY_EVEN_FOUR_DERIVATIVE_LOCAL_METRIC_BULK_DIRECTIONS_REMAIN_SYMMETRY_ALLOWED_IN_4D`.

This is an operator census, not a statement that either coefficient is actually generated.

## G1-5 — continuum power counting

For a connected 4D diagram built from two-derivative gravity vertices and `1/p^2` propagators,

`omega=4L+2V-2I`.

Using `L=I-V+1` gives exactly

`omega=2L+2`.

Thus generic superficial power counting allows four-derivative structures at one loop, six-derivative structures at two loops, and progressively higher orders thereafter, before special gauge/on-shell cancellations.

Classification:
`BLOCKED_SCOPED_CONTINUUM_TWO_DERIVATIVE_GRAVITY_POWER_COUNTING_ALLOWS_PROGRESSIVELY_HIGHER_DERIVATIVE_COUNTERTERM_ORDERS__MICROSCOPIC_QGR_MUST_CONTROL_THEIR_COEFFICIENTS_OR_SUPPRESSION`.

This is **not** a calculation of a nonzero loop divergence.

## Consolidated classification

`BLOCKED_SCOPED_NAIVE_GLOBAL_INTERACTING_VACUUM_MEASURE_IS_NOT_NORMALIZED_ALONG_THE_FLAT_SCALE_ZERO_MODE__TWO_DERIVATIVE_LOCAL_ACTION_IS_NOT_QUANTUM_CLOSED_BY_SYMMETRY_POWER_COUNTING__Z2_SECTORS_ARE_REFINEMENT_SUPERSELECTED`.

## Important positive boundary

Iter006 already proved an exact finite-level operator statement:

`K_alpha=24^(-1/2) exp(iS_alpha/hbar) U_alpha`,

with `sum K_alpha^dagger K_alpha=I` on the verified domain. Multiplication by a real action phase and the quasi-invariant Koopman/Radon-Nikodym branch lift are unitary there.

Therefore failure of the naive normalized global vacuum weight does not imply failure of finite-network interacting operator dynamics.

However Iter006 explicitly scoped `S_alpha` to the then-verified local action truncation and did not supply an all-refinement unique finite-cell action functional or a continuum interacting measure theorem.

## Next gate

`QGR-ITER009-G2-FINITE-OPERATOR-DYNAMICS-AND-FINITE-CELL-EFFECTIVE-ACTION-CLOSURE`

1. prove finite serial operator/CPTP closure independently of global vacuum-measure normalization;
2. audit the repository for a unique exact finite-cell action functional beyond continuum/local action matching;
3. if absent, quantify the first finite-refinement ambiguity in the two-dimensional curvature-squared bulk space rather than choosing coefficients by hand;
4. state sufficient conditions for an infinite-refinement operator limit and test whether current QGR proves them;
5. preserve the Z2 block structure throughout.
