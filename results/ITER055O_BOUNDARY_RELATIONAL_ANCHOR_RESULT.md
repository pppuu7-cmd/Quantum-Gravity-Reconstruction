# Iter055O terminal result — boundary relational smearing anchor: direction versus physical scale

Date: 2026-09-14
Preregistration: `d85444875d4dc9f93d8cdcb6e08144318d4c86f6`

## Terminal classification

`PASS_SCOPED_PARTIAL_ITER055O_BOUNDARY_DIRECTION_ANCHOR_EXISTS__PHYSICAL_SMEARING_SCALE_UNFIXED`

## 1. Shared B3 is an embedded boundary subcomplex, not only an abstract label

G6C/G6E define neighboring B4 regions by their finite path-groupoid incidence data and identify the shared B3 exactly as the intersection of their vertex and edge sets. The gluing/restriction theorem uses this embedded shared face as one physical boundary variable, with a canonical restriction map from each B4 region to the same B3 data.

In the representative incidence realization used by the source, the two B4 cells are displaced in one cell direction, so the shared face is spanned by the remaining three edge directions. More invariantly, the embedded B3 tangent subspace is fixed by the shared-face incidence data inside the local four-dimensional cell.

Thus, on the regular cell domain, the boundary geometry determines a one-dimensional **conormal line**: the annihilator of the three-dimensional tangent subspace of the shared B3 face.

## 2. Physical metric converts the conormal line into a covariant normal line

Let `m_a` be any nonzero representative of the face conormal line and let `G^{ab}` be the inverse physical metric on the regular branch. Define

`v^a = G^{ab} m_b`.

Under an allowed finite frame change, the embedded face tangent space, its conormal line and the metric transform together. Therefore `v` transforms as a vector and the line `[v]` is frame-covariant; no external observer or preferred coordinate frame is introduced.

On a non-null regular face, where

`G^{ab} m_a m_b != 0`, 

a normalized representative can be formed:

`n^a = G^{ab}m_b / sqrt(|G^{cd}m_c m_d|)`.

The overall sign is the usual coorientation choice. When the ordered neighboring-region pair supplies an A-to-B coorientation, the sign may be chosen accordingly; without that ordering the physically source-defined object is the normal line rather than an oriented unit vector. This sign qualification does not remove the direction/frame anchor.

Null faces are outside this normalized subcase and are not promoted by this result.

## 3. No source-fixed physical smearing scale follows from the boundary geometry

The embedded face and metric determine direction and causal character, but not a unique radial width or ultraviolet scale for an `L2` kernel on the characteristic cone.

G7A already gives the decisive scale authority. The continuum gravitational normalization has only the form

`a_cont = c_geom * kappa / h^2`,

with exact rank-one logarithmic Jacobian `[1,-2]`. The transformation

`h -> lambda h`,
`kappa -> lambda^2 kappa`

leaves the continuum normalization unchanged. Existing QGR authority does not fix `kappa` separately or identify `h` with the Planck length.

Therefore the microscopic cell scale cannot be converted into a source-fixed absolute physical smearing width by the present normalization chain.

## 4. Negative controls

The missing scale cannot be supplied by:

- the unit coordinate edge of the finite cell, which is a combinatorial/coordinate convention rather than an independently calibrated physical length;
- G6G/G6H packet widths, which are explicitly preparation/readout dependent;
- Iter053 `SUPPORT=0.24` or its `q^4` bump, which belong to a frozen functional-variation test;
- `beta`, which remains unfixed;
- `c6`, which remains unfixed;
- declaring `h=l_P` or `kappa=1`, explicitly forbidden by G7A without new authority.

## Scientific consequence

Iter055N required extra relational data for any nonzero covariant smearing family. Iter055O shows that QGR already supplies **part** of that data:

`shared B3 embedding + physical metric -> covariant boundary normal/conormal line`

on the regular non-null boundary domain.

What remains missing is not an arbitrary frame direction but a physical radial scale/profile and its refinement law. The bridge can therefore be parameterized covariantly relative to the boundary normal, but it cannot yet be assigned a source-fixed physical width.

This partial PASS narrows the next gate. It is no longer necessary to invent an observer direction. The open question is whether the existing microscopic cell parameter `h` can define a **scale-covariant internal refinement family** (even though its absolute physical calibration is unfixed), and whether refinement/locality can constrain the dimensionless profile shape without post-hoc tuning.

## Claim ceiling

- direction/frame anchor: established only on the regular embedded non-null shared-B3 scope, up to ordinary coorientation/sign;
- physical smearing scale: not fixed;
- concrete kernel/refinement family: not established;
- no interacting boundary dynamics selected;
- no `beta` or `c6` fixing;
- no Weyl3 treatment selector, global regulator removal, full quantum unitarity, UV completion, GR recovery, experiment or theory establishment.

No GitHub Actions run was needed; this is a source/geometric authority result.
