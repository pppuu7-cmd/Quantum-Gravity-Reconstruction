# Iter055Y preregistration — Weyl3 survival implies resolved formal HD scale

Date: 2026-09-14
Gate: `ITER055Y-WEYL3-SURVIVAL-VS-RESOLVED-FORMAL-HD-SCALE`

## Frozen question
Within the same formal Iter054I/J/Iter055W scaling object, if a nonzero Weyl3 correction is kept finite on a fixed nonzero physical frequency as `h -> 0`, does the associated formal higher-derivative root scale necessarily enter every fixed nonzero dimensionless resolved refinement band `0<q<=q_max` rather than remaining hidden above the microscopic cutoff/resolution scale?

## Frozen definitions
For fixed physical `k != 0` and arbitrary positive diagnostic `A(h)`:

`rho(h,k)=A(h) h^4 k^2`,

`k_HD(h)=1/[h^2 sqrt(A(h))]`,

`q_HD(h)=h k_HD(h)`.

Use the exact Iter055W identity `rho k_HD^2=k^2`. Arbitrary `A(h)` is diagnostic only and does not authorize physical running.

## Frozen obligations
1. If `rho(h,k) -> rho_*` with `0<rho_*<infinity`, derive the limit of `k_HD` and `q_HD`.
2. Prove that for every fixed `q_max>0`, finite nonzero survival implies `q_HD<q_max` for all sufficiently small `h`.
3. Prove the converse bound: if the formal HD scale is kept uniformly outside a fixed resolved band, `q_HD>=q0>0`, then `rho(h,k)<=k^2 h^2/q0^2 ->0`.
4. Make no pure-power assumption.
5. Treat this only as a formal characteristic/root-scale statement. No physical mode, ghost, instability or cutoff interpretation is authorized.
6. Do not promote a fixed `q_max` to a source-derived physical detector/cutoff band; it is an arbitrary dimensionless diagnostic band.

## Frozen classifications
- `PASS_SCOPED_ITER055Y_NONZERO_FIXED_BAND_WEYL3_SURVIVAL_FORCES_FORMAL_HD_SCALE_INTO_ANY_FIXED_Q_BAND__PHYSICAL_MODE_NOT_AUTHORIZED` if the implications hold exactly.
- `FAIL_SCOPED_ITER055Y_SURVIVAL_DOES_NOT_FORCE_FORMAL_HD_SCALE_INTO_RESOLVED_Q_BAND` if the frozen identities admit a counterexample.
- `INVALID_PROVENANCE_ITER055Y_SCALING_OBJECT_INCONSISTENT` only if Iter055W cannot be used as the parent identity.

## Interpretation ceiling
A PASS is a formal model-construction constraint: an exact-HD candidate version that insists on nonzero continuum Weyl3 survival cannot simultaneously claim the extra formal root is hidden above every fixed refinement-resolved q-band merely by coefficient scaling. It does not select exact-HD dynamics, make the root physical, authorize order reduction/running/cutoff, or establish stability, unitarity, UV completion, GR recovery, experiment or theory establishment.

No GitHub Actions run is preregistered; this is exact algebra/asymptotics.
