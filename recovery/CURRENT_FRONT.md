# QGR Current Research Front

Updated: 2026-09-11
Active iteration: `Iter003`
Project phase: `MODEL_CONSTRUCTION_ACTIVE / PRE_ANSATZ`
Active roadmap stage: `R3 gate — 4D Lorentzian/GR seed`

## Canonical status

- Repository infrastructure readiness: **100%**
- Candidate-program readiness: **24%** (unchanged; still no promotable physical ansatz)
- Iter003 completion: **25%**
- Physical ansatz promoted: **NO**
- Lead architecture: `A / CCRC`
- Theory established: **NO**
- Independent benchmark passed: **NO**
- KMQGB `NEW_REQUIRED` authorization: **NO**

## Iter002 closed result

Two prospective kill rounds selected A/CCRC as the unique current lead architecture. B, C and E acquired scoped standalone failures; D remains only partially viable. Issue #1 is closed as completed.

## Iter003 seed result

A branching/recombining metric-free causal test object has been constructed using the Boolean causal cell `B_d`.

Events are subsets of `d` independent relational generators, ordered by set inclusion. The rank profile is purely combinatorial:

`N_r = C(d,r)` and `R_d(x)=(1+x)^d`.

Thus `d` is recoverable from relational-order data rather than supplied by a continuum metric.

For `B_4`:

- events: `16`;
- rank profile: `(1,4,6,4,1)`;
- maximal monotone causal chains: `4! = 24`;
- derived combinatorial direction count: `d=4`.

Retaining the Iter002 CCRC projector `P=I-J/3`, each chain has kernel `P^4=P`. Equal-chain symmetry plus exact coarse consistency requires

`24 * w_4 * P = P`,

therefore the path weight is uniquely fixed to

`w_4 = 1/24`.

More generally `w_d=1/d!` on the symmetric `B_d` cell.

Classification: `PASS_SCOPED_DERIVED_COMBINATORIAL_DIMENSION_AND_UNIQUE_PATH_NORMALIZATION`.

Reproducibility: `code/qgr_iter003_boolean_causal_cell.py`.
Detailed record: `iterations/ITERATION_003.md`.

## Why this matters

The first branching/recombining extension did not require a new tunable amplitude weight. Path multiplicity plus refinement closure fixed the symmetric normalization combinatorially. This is consistent with the QGR rigidity objective and avoids repeating a major class of underdetermination seen in benchmark work.

## Critical boundary

`d=4` here means a derived **combinatorial direction count**, not yet physical 4D Lorentzian spacetime.

Still unproved:

- Lorentzian signature;
- approximate local Lorentz invariance;
- metric/tetrad degrees of freedom;
- propagating massless spin-2 sector;
- Einstein dynamics;
- equivalence principle;
- continuum locality;
- normalized clock/rod observable.

No readiness increase is granted for merely matching the number four.

## Active scientific gate — Iter003-G2

`QGR-ITER003-G2-LORENTZIAN-TENSOR-SEED`

1. Perturb local incidence/gluing data around symmetric `B_4` without a background metric.
2. Decompose perturbations into symmetry sectors before choosing dynamics.
3. Look for a nontrivial traceless tensor-like sector that survives causal gluing/refinement.
4. Test multi-cell composition; a mode existing only in one isolated cell does not count.
5. Determine whether any candidate Lorentzian signature or hyperbolic propagation structure arises intrinsically.
6. Reject the branch in its present form if continuum GR structure must be inserted by hand.

## Fatal criterion

If 4D Lorentzian/GR recovery requires inserting a background metric, Einstein-Hilbert term, arbitrary continuum/spectral function, or gate-specific coefficients solely to hit GR, A/CCRC fails the reconstruction objective in its current form.

## KMQGB synchronization

Last inspected KMQGB head remains `f503c39177012879a80bf767282a15d0c441e2f9` (Iter324-325 merge). Its finite-source-`i-epsilon` result reinforces, but does not change, the QGR prospective finite-definition rule. D7 remains unauthorized in the inspected snapshot.

## Recovery pointers

- `recovery/state.json`
- `iterations/ITERATION_003.md`
- `code/qgr_iter003_boolean_causal_cell.py`
- GitHub issue #2 — Iter003 4D Lorentzian/GR seed gate

## Exact next action

Begin the symmetry-sector perturbation analysis around `B_4`. The next useful milestone is not another combinatorial dimension count; it is evidence for or against an intrinsically generated Lorentzian tensor-like propagating sector.
