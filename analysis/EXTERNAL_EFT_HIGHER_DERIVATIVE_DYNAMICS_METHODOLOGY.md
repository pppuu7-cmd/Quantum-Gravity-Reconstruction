# External methodology audit — higher-derivative gravity EFT dynamics

Date: 2026-09-14

Status: **BACKGROUND METHODOLOGY ONLY — NOT QGR AUTHORITY**.

This note records external literature relevant to designing a future QGR-specific gate for `MISSING_WEYL3_DYNAMICAL_TREATMENT_AUTHORITY`. It does not import a dynamical prescription into QGR, does not fix `c6`, and does not authorize discarding or accepting any higher-derivative branch.

## Why this audit exists

Current QGR repository authority treats `c6 Weyl^3` as an independent six-derivative Wilson/correction direction with perturbative power counting, but does not yet derive whether the corresponding corrected equations are to be interpreted as:

1. exact fundamental higher-derivative evolution;
2. perturbative/reduction-of-order EFT evolution;
3. a well-posed EFT reformulation/regularization with auxiliary or fiducial modes outside the physical cutoff sector;
4. some QGR-specific alternative.

External literature shows that these possibilities are materially different and therefore the choice cannot be made post hoc after seeing the QGR spectrum.

## Primary methodological sources

### Simon 1990 — perturbative constraints for higher-derivative effective actions

Jonathan Z. Simon, “Higher-derivative Lagrangians, nonlocality, problems, and solutions,” Phys. Rev. D 41, 3720 (1990).
DOI: https://doi.org/10.1103/PhysRevD.41.3720

The paper analyzes pathologies of unconstrained higher-derivative systems and argues for perturbative constraints in classes of effective/nonlocal theories. Its example emphasizes that perturbatively relevant solutions need not coincide with the unrestricted exact solution space of a truncated higher-derivative equation.

Methodological implication for QGR: if QGR derives an EFT treatment, exact roots of the truncated quartic symbol cannot automatically be identified with physical modes without checking perturbative validity.

### Simon 1991 — nonperturbative pseudosolutions of corrected semiclassical equations

Jonathan Z. Simon, “Stability of flat space, semiclassical gravity, and higher derivatives,” Phys. Rev. D 43, 3308 (1991).
DOI: https://doi.org/10.1103/PhysRevD.43.3308

The paper emphasizes that many additional solutions of higher-derivative corrected equations lie outside the perturbative framework that generated the effective equations and calls these nonperturbative “pseudosolutions.”

Methodological implication for QGR: a high-frequency branch appearing only when the higher-derivative correction becomes order unity must be classified separately from a pathology occurring on the perturbatively connected low-energy branch.

### Parker & Simon 1993 — reduction of order in semiclassical gravity

Leonard Parker and Jonathan Z. Simon, “Einstein equation with quantum corrections reduced to second order,” Phys. Rev. D 47, 1339 (1993).
DOI: https://doi.org/10.1103/PhysRevD.47.1339

They construct reduced second-order equations for first-order semiclassical corrections, retaining the perturbatively relevant solution sector while eliminating the unrestricted higher-derivative branches.

Methodological implication for QGR: if order reduction is chosen, the exact reduction rule, retained order, initial-data map and constraint compatibility must be derived prospectively rather than deleting undesirable roots ad hoc.

### Donoghue 1994 — gravity as EFT and scale separation

John F. Donoghue, “General relativity as an effective field theory: The leading quantum corrections,” Phys. Rev. D 50, 3874 (1994).
DOI: https://doi.org/10.1103/PhysRevD.50.3874

This establishes the general low-energy EFT viewpoint in which known low-energy effects are separated from unknown high-energy contributions.

Methodological implication for QGR: any EFT interpretation requires an explicit validity domain/cutoff statement. A branch at scales where omitted operators are unsuppressed cannot be treated as controlled solely because it solves a finite truncation.

### Reall & Warnick 2021/2022 — classical equations of motion of truncated EFTs

Harvey S. Reall and Claude M. Warnick, “Effective field theory and classical equations of motion,” arXiv:2105.12028.
https://arxiv.org/abs/2105.12028

They study how truncated higher-derivative EFT equations can approximate a UV theory despite finite-order equations not necessarily being well posed, and propose a well-posed approach to EFT evolution.

Methodological implication for QGR: well-posedness and UV-approximation are separate requirements from merely writing the raw higher-derivative Euler-Lagrange equation.

### Kovács & Reall 2020 — strongly hyperbolic EFT formulations at weak coupling

Áron D. Kovács and Harvey S. Reall, “Well-Posed Formulation of Scalar-Tensor Effective Field Theory,” Phys. Rev. Lett. 124, 221101 (2020).
DOI: https://doi.org/10.1103/PhysRevLett.124.221101

Related: “Well-posed formulation of Lovelock and Horndeski theories,” Phys. Rev. D 101, 124003 (2020).
DOI: https://doi.org/10.1103/PhysRevD.101.124003

These works show that modified harmonic formulations can yield strong hyperbolicity/well-posed initial value problems in appropriate weak-coupling EFT regimes.

Methodological implication for QGR: a physical stability gate should test a properly gauge-fixed/constraint-compatible evolution system rather than interpreting a gauge-degenerate raw symbol alone.

### Davies & Reall 2022 — field redefinitions and well-posed Einstein-Maxwell EFT

Iain Davies and Harvey S. Reall, “Well-posed formulation of Einstein-Maxwell effective field theory,” Phys. Rev. D 106, 104019 (2022).
DOI: https://doi.org/10.1103/PhysRevD.106.104019

They use field redefinitions and modified harmonic gauge to obtain a well-posed formulation when EFT corrections are small.

Methodological implication for QGR: allowed field-redefinition/EOM equivalence must be part of any claim that an extra raw root is a physical invariant rather than representation-dependent.

### Figueras, Held & Kovács 2024 — general polynomial higher-derivative gravity EFTs

Pau Figueras, Aaron Held and Áron D. Kovács, “Well-posed initial value formulation of general effective field theories of gravity,” arXiv:2407.08775.
https://arxiv.org/abs/2407.08775

They argue that polynomial higher-derivative vacuum gravity EFTs, including cubic truncations, can be augmented by suitable regularising terms obtainable by field redefinitions and formulated as second-order nonlinear wave systems. The added fiducial massive modes may be placed above the cutoff.

Methodological implication for QGR: the alternatives are not limited to naive exact evolution versus traditional equation-level reduction of order. A QGR-specific treatment gate should also account for well-posed EFT reformulations and explain which variables/modes are physical inside the validity domain.

### Gavassino, Kovács & Reall 2026 — initial data for unphysical EFT modes

Lorenzo Gavassino, Áron D. Kovács and Harvey S. Reall, “Initial data of effective field theories of relativistic viscous fluids and gravity,” Phys. Rev. D 113, 124022 (2026).
DOI: https://doi.org/10.1103/ft2b-m8hv

They propose applying reduction of order to initial data for unphysical modes in well-posed EFT formulations, specifying those data from the physical modes rather than simply deleting the auxiliary dynamics.

Methodological implication for QGR: the future treatment gate must state the physical initial-data manifold, not only a dispersion relation or characteristic polynomial.

### Reall & Santos 2019 — six/eight derivative vacuum gravity as EFT corrections

Harvey S. Reall and Jorge E. Santos, “Higher derivative corrections to Kerr black hole thermodynamics,” JHEP 04 (2019) 021.
DOI: https://doi.org/10.1007/JHEP04(2019)021

They explicitly treat six- and eight-derivative curvature terms as higher-derivative corrections in gravitational EFT and note that four-derivative pure-gravity terms can be eliminated by field redefinitions in the matter-free case.

Methodological implication for QGR: the repository’s own six-derivative/Wilson terminology is consistent with a standard gravitational-EFT use case, but this external consistency does not itself choose QGR’s dynamical treatment.

## Requirements this literature motivates for a future QGR-specific gate

A valid QGR `WEYL3_DYNAMICAL_TREATMENT` gate should prospectively freeze and derive, from QGR rather than importing a preferred external prescription:

1. **status of the truncation:** exact fundamental equation, perturbative EFT, well-posed regularized EFT, or another derived QGR object;
2. **validity domain:** explicit small parameters and background/wave-covector regime;
3. **field-redefinition/EOM quotient:** what transformations are allowed and which spectrum/observable statements are invariant;
4. **gauge/constraint formulation:** gauge fixing, Bianchi/constraint propagation and hyperbolicity object;
5. **initial-data space:** which data are physical and how any auxiliary/unphysical mode data are fixed;
6. **branch criterion:** how to distinguish branches continuously connected to QGR-L1 from nonperturbative/high-cutoff branches;
7. **role of `c6`:** remain symbolic/unfixed unless separate matching authority exists;
8. **counterexample-first controls:** backgrounds/covectors where any proposed reduction or regularization fails;
9. **PASS/FAIL/BLOCKED/INVALID:** frozen before spectrum results;
10. **interpretation ceiling:** no unitarity or quantum claim from classical well-posedness alone.

## Non-import firewall

This literature does **not** establish that QGR must use reduction of order, must use a particular regularization, or must accept/reject extra roots. The next QGR gate must choose/derive the treatment from QGR construction principles and existing repository authority. External methods are comparison/control options only.

## Claim ceiling

No QGR dynamical-treatment authority, stability certificate, ghost theorem, value/sign of `c6`, quantum consistency, UV completion or theory establishment follows from this note.