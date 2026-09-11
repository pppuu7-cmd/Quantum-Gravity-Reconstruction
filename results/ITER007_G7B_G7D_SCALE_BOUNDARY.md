# QGR Iter007 G7B-G7D — Physical-scale boundary and one-coupling reduction

Date: 2026-09-12
Status: `ITER007_SCALE_GATE_CLOSED_NEGATIVELY_SCOPED / ONE_DIMENSIONLESS_MICROSCOPIC_COUPLING_REMAINS`

## G7B — existing quantum normalization and metric-only matter do not fix the scale

GitHub Actions run `34659478647`: four lanes plus aggregate `SUCCESS`.

Classification:
`BLOCKED_SCOPED_EXISTING_QGR_QUANTUM_NORMALIZATION_DOES_NOT_FIX_KAPPA_AND_METRIC_ONLY_MATTER_COVARIANCE_DOES_NOT_SUPPLY_A_DERIVED_SECOND_SCALE`.

Results:

1. For
   `K_alpha=24^(-1/2) exp(i kappa s_alpha/hbar) U_alpha`,
   branch modulus/completeness are independent of real `kappa`; only the phase changes. Projective composition is exact for arbitrary `kappa`.
2. The current configuration measure
   `|det G|^(-5/2)d^10G`
   is exactly neutral under `G->s^2G`, because the coordinate Jacobian `s^20` cancels the determinant weight `s^-20`.
3. A local metric-only scalar probe has allowed two-derivative data `Z`, `m^2`, `xi`. Canonical field rescaling removes `Z` but not the independent matter mass/curvature data.
4. Multiple species can share the same high-frequency metric cone while retaining different canonically meaningful matter parameters. Therefore covariance alone does not derive universal matter normalization.

## G7C — no current nonzero refinement stop scale

GitHub Actions run `34659644866`: four lanes plus aggregate `SUCCESS`.

Classification:
`BLOCKED_SCOPED_CURRENT_CCRC_QGR_HAS_NO_DERIVED_NONZERO_STOP_SCALE__H_IS_EITHER_REMOVED_REGULATOR_WITH_VANISHING_H4_EFFECT_OR_REQUIRES_A_NEW_PHYSICAL_DISCRETENESS_PRINCIPLE`.

Results:

1. Along fixed continuum gravity normalization, `h->0` requires `kappa~h^2`; the normalized history correction then vanishes as `h^4`.
2. The current Lorentzian response space `Q_13` is continuous and contains arbitrary positive rescaling orbits; its invariant measure does not generate a scale.
3. The naive canonical route `T*Q_13` has exact symplectic form `omega=dtheta`; ordinary prequantization integrality therefore cannot quantize `kappa`.
4. B4 incidence/history/S4 counts are dimensionless and unchanged under global rescaling of the physical embedding.

Thus:
- if `h` is a removed regulator, the scoped local continuum retains GR and the leading finite-history effect disappears;
- if `h>0` is physical, a new prospectively derived spectrum/clock/amplitude/refinement-stop principle is required.

## G7D — reduce the ambiguity to one dimensionless coupling

GitHub Actions run `34659779779`: four lanes plus aggregate `SUCCESS`.

Classification:
`PARTIAL_SCOPED_ABSOLUTE_SCALE_AMBIGUITY_REDUCED_TO_ONE_DIMENSIONLESS_MICROSCOPIC_COUPLING_G_KAPPA_OVER_HBAR__G_REMAINS_UNFIXED_AND_MATTER_CLOCK_CALIBRATION_OPEN`.

Restore physical units. Since `kappa` multiplies a dimensionless microscopic action functional, it has units of action. Define

`g = kappa/hbar`

and

`ell_Q^2 = hbar/a_cont`.

With the G7A continuum matching

`a_cont = c_geom kappa/h^2`,

one obtains

`h^2 = c_geom g ell_Q^2`.

Therefore, once the continuum normalization and `hbar` are fixed, the unresolved freedom is equivalent to **one dimensionless microscopic action normalization `g`**, not an independently arbitrary new length.

A generic leading G6H history effect may be written schematically as

`loss = C_prep (h^2 R_eff)^2 + ...`

and hence

`loss = C_prep c_geom^2 g^2 (ell_Q^2 R_eff)^2 + ...`.

`C_prep` is preparation/readout dependent as independently established by G6F-G6H.

Pure classical vacuum gravity does not operationally determine the overall Einstein-Hilbert coefficient: multiplying the vacuum action by any nonzero constant leaves the classical vacuum solution set unchanged. Operational calibration therefore ultimately requires quantum phase information and/or a matter/clock normalization.

No current authoritative QGR rule fixes `g=1` or any other value. Setting `hbar=1` is a unit convention and does not fix a dimensionless coupling.

## Iter007 conclusion

Iter007 has answered its distinguishability/observable question in both directions:

- **positive:** a normalized, cutoff-free, curved broadband two-mode 24-history comparator is derived for specified preparations and its leading refinement order is robustly `O(h^4)` on the repaired G9 benchmark;
- **negative:** the present QGR/CCRC realization does not derive the absolute value of the remaining dimensionless microscopic coupling `g` or a nonzero physical refinement stop scale.

This negative boundary is part of the result. It must not be hidden by setting `g=1`, `h=l_P`, or importing a matter normalization ad hoc.

## Next research stage

`Iter008 — Physical Scale and Relational Matter Reconstruction`.

Prospective routes:

1. derive a nontrivial discrete geometric spectrum/refinement stop from the same CCRC ontology;
2. derive a relational clock/matter sector whose normalization is fixed by the same microscopic realization and supplies an operational second scale;
3. derive a nontrivial microscopic amplitude/symplectic topology that can quantize or otherwise determine `g`.

Any route must preserve the already frozen G-sector results and fail closed if it merely adds a desired scale by convention.
