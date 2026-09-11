# QGR Iter006-G8B — regular-stratum rigging and canonical torsion-branch measure

Date: 2026-09-11
Status: `PASS_SCOPED_LOCAL_REGULAR_STRATUM_RIGGING / GLOBAL_STRONG_CURVATURE_FINITE_MEASURE_BLOCKED`

## Question

Can QGR remove gauge redundancy and assign relative weights to possible finite torsion-free connection branches without pretending that the noncompact internal Lorentz group has a normalized Haar probability measure?

## 1. Internal Lorentz redundancy is removed algebraically

The frame lift uses

`G_v=F_v^T C F_v`,

and edge holonomies `L_wv in O(C)`. Under a local internal Lorentz change

`F_v -> Lambda_v F_v`,
`L_wv -> Lambda_w L_wv Lambda_v^-1`,

with `Lambda_v^T C Lambda_v=C`, the combination

`A_wv=F_w^-1 L_wv F_v`

is invariant.

Therefore the finite-complex configuration may be represented directly by gauge-invariant `(G_v,A_e)` subject to metric compatibility. No normalized average over `O(1,3)` is required for this redundancy.

Classification:

`PASS_SCOPED_INTERNAL_LORENTZ_REDUNDANCY_REMOVED_BY_GAUGE_INVARIANT_VARIABLES_WITHOUT_GROUP_AVERAGING`.

## 2. Local derivative/frame quotient on a regular stratum

The remaining QGR frame/derivative redundancy acts on the response configurations. At the symmetric seed its generator rank is exactly four per characteristic fiber, and the physical quotient has dimension two.

Consider a finite-complex patch where the relevant constraint-generator rank is constant and the gauge action is locally free. By the constant-rank theorem the configuration patch admits local coordinates `(y,theta)` in which `theta` parameterizes the gauge orbit and `y` parameterizes a transverse quotient.

Equivalently choose any local regular gauge slice

`chi^a(x)=0`

such that

`det(D chi . R) != 0`.

The quotient density may be written locally as

`dmu_phys = dmu_kin delta(chi) |det(D chi . R)|`,

with the determinant evaluated on the same QGR constraint generators `R`.

This is a Jacobian from change of variables, not a new physical coupling. On overlap of regular slices, ordinary change-of-variables gives the same local quotient integral for gauge-invariant observables.

This establishes a **local regular-stratum rigging construction**. It does not establish a single global slice or the absence of Gribov/degenerate strata.

Classification:

`PASS_SCOPED_LOCAL_REGULAR_STRATUM_PHYSICAL_QUOTIENT_MEASURE`.

## 3. Multiple torsion-free connection branches

The finite discrete connection is constrained by the torsion equations

`T(F,L)=0`.

Near the symmetric seed, G5 proved that the connection Jacobian is nonsingular with recorded determinant `11664`, so there is one locally unique branch.

For a generic strong-curvature configuration there may instead be several solutions `L_r`.

QGR must not assign arbitrary probabilities to such branches.

Use the invariant (unnormalized) group measure on the finite-dimensional connection variables and impose the torsion equations by a delta distribution. On a regular patch with isolated roots, standard delta/coarea reduction gives a discrete induced measure

`w_r proportional to j_Haar(L_r) / |det(dT/domega)_(L_r)|`,

where `j_Haar` is the invariant-measure density in the chosen local connection coordinates `omega`.

All relative factors are determined by the group geometry and the already fixed torsion equations. The arbitrary global normalization of Haar measure cancels when the resulting finite branch measure is normalized on a fixed finite complex.

Near the seed this construction is finite because there is one regular root and `det J != 0`.

## 4. Exact boundary of the result

This does **not** prove that the generic strong-curvature solution set is always finite and regular.

The branch measure becomes unresolved if the torsion solution set develops

- continuous components;
- infinitely many relevant roots;
- singular roots with `det(dT/domega)=0`;
- nonintegrable escape to noncompact connection directions.

Those possibilities are now the precise remaining finiteness blocker, replacing the earlier vague statement that noncompact Haar normalization is impossible.

## Classification

`PASS_SCOPED_REGULAR_FINITE_BRANCH_MEASURE_DERIVED__BLOCKED_GLOBAL_STRONG_CURVATURE_ROOT_FINITENESS_AND_SINGULAR_STRATA`.

## Next gate

Construct a nontrivial strong-curvature finite-cell torsion system beyond the implicit-function neighborhood and determine whether its solution set is finite/regular, then test whether the resulting branch instrument remains projectively consistent under two-level blocking.
