# Iter055U terminal result — continuum-to-B3 attachment: candidate structure or readout convention

Date: 2026-09-14
Preregistration: `c4eed2450f6e07e157e1a3f31c8e0c783514f372`

## Terminal classification

`PASS_SCOPED_ITER055U_ATTACHMENT_IS_CANDIDATE_OWNED_UP_TO_B3_REPARAMETERIZATION__ARBITRARY_READOUT_MAPS_ARE_INEQUIVALENT`

## 1. Ordinary target-coordinate reparameterization preserves the kernel

Let `C1,C2 : H_char -> V_B3` be bounded linear coarse maps into the same finite-dimensional boundary coordinate space. If they differ only by an invertible reparameterization of the finite B3 coordinates,

`C2 = M C1`, `M in GL(V_B3)`,

then

`ker C2 = ker C1`

and the rank is unchanged.

Thus the nullspace of the continuum-to-boundary map is an invariant of ordinary finite-target coordinate changes. It records which continuum one-particle perturbations are invisible to the finite boundary state.

## 2. Inequivalent bounded coarse readouts exist immediately

Because the G6F physical one-particle Hilbert is nontrivial and infinite-dimensional, choose two normalized non-collinear physical sections `phi1,phi2 in H_char`. Define scalar coarse readouts

`C1[a]=<phi1,a>`,
`C2[a]=<phi2,a>`.

Both are bounded legitimate Iter055S readouts. But

`ker C1 = phi1^perp`,
`ker C2 = phi2^perp`,

which are different when `phi1` and `phi2` are not collinear. For a one-dimensional target, the only invertible reparameterizations are multiplication by a nonzero scalar, so these maps are manifestly inequivalent.

The same witness embeds into any larger finite B3 target: keep all but one bounded coordinate functional fixed and replace one independent functional by another outside their finite span. The resulting maps can have the same target dimension/rank yet different kernels and therefore are not related by an invertible target-coordinate change.

Hence “choose any finite family of bounded test functions” is a valid **measurement/readout freedom** but not a unique identification of the microscopic boundary state.

## 3. Finite B3 variables are candidate configuration data, not only detector outputs

G6C/G6E define B3 variables by restricting the finite graph configuration `X_Gamma`, whose primitive data are response forms at vertices and compatible finite transports on edges. The shared B3 enters the exact fiber-product gluing of neighboring candidate configuration spaces and the boundary measure disintegration.

Iter006-G7B further shows that `G_v`, edge/path transports and loop holonomies are retained in the strong-curvature coarse observable/configuration algebra and participate in exact associative blocking. Their role is therefore internal to the candidate's state/geometry architecture.

Changing which continuum perturbations are mapped to the same `G_v,A_e` state is stronger than changing a detector test function.

## 4. No source theorem establishes attachment-scheme independence

The audited QGR chain contains no theorem that replacing one inequivalent continuum-to-B3 attachment by another with a different nullspace leaves the induced microscopic dynamics, gluing, blocking, continuum channel recovery or physical predictions unchanged.

Iter055S establishes covariance and legitimacy of arbitrary external one-particle readouts only. It does not prove that arbitrary readout maps can be identified with the candidate's finite graph coordinates.

Therefore a claim that the finite B3 boundary dynamics recovers the G6F/Iter009-G6 continuum sector requires either:

1. a source-defined candidate-owned attachment `C_h` (up to invertible finite B3 reparameterization / other explicitly proven equivalences), or
2. a new theorem proving recovery/predictions independent of the relevant attachment class.

Neither currently exists.

## Scientific consequence

The micro-continuum attachment is a genuine candidate-construction obligation, not a cosmetic packet-profile choice.

The distinction is now sharp:

- external `phi` in `H_char`: observable/preparation choice, already allowed by Iter055S;
- map identifying continuum perturbations with finite candidate variables `G_v,A_e`: candidate-owned structural input unless a scheme-independence theorem is established.

This prevents using arbitrary detector/test profiles to hide the missing emergence map.

## Next highest-information gate

Before proposing a new finite-element map, audit whether the existing **microscopic-to-continuum derivation itself** implicitly supplies the opposite-direction linearization/Jacobian. In particular inspect the derivation of continuum response `q`, discrete differences `Dq`, weak-curvature `G+Riemann` matching and any map from fine response/connection variables to continuum fields. If a source-defined microscopic -> continuum map `R_h` exists, test whether its adjoint/dual or a right inverse can canonically induce the required observable attachment on a controlled subspace. If only asymptotic power counting exists, record the emergence map itself as the missing candidate object rather than inventing a discretization.

## Claim ceiling

No attachment map is selected; no boundary dynamics, absolute h, beta/c6 fixing, Weyl3 treatment, regulator removal, full quantum unitarity, UV completion, GR recovery, experiment or theory establishment follows. Theory established remains 0%.

No GitHub Actions run was required; the result is exact linear algebra plus source-role analysis.
