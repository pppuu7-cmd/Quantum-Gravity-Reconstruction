# Iter057M fast exact source-jet equivalence audit — terminal implementation result

Date: 2026-09-15
Parent gate: `ITER057M-GENERAL-QAB-SECOND-EVEN-JET-QUARTIC-EXTENSION`
Audit preregistration: `253fc53238ac58bbe4395e154e188e3d865217c2`
Fast candidate: `f9181c7dda617ce4061fa90e73164e6cdbecd714`
Independent symbolic reference: `9c92a854fea23228162db591b7e62e7794594040`
Workflow head: `0f10ac644060d712e3edbd48fa2ef6bdced1fbe1`
Actions run: `34954206549`
Job: `104332193998`
Artifact: `10390318470` (`iter057m-fast-source-equivalence`)
Artifact digest: `sha256:ab331b2093e7d26e1d5f609f08e81c70739bb79d88a9a210a73ffc5b8155cd92`

## Classification

**`PASS_SCOPED_ITER057M_FAST_EXACT_SOURCE_JET_COMPONENT_EQUIVALENCE`**

This is an implementation/equivalence classification inside the active Iter057M gate. It is not the terminal scientific classification of Iter057M.

## Exact comparison

The workflow executed two independent implementations:

1. the custom exact rational finite-Taylor evaluator `qgr_iter057m_exact_g3_weyl3_source_jet.py`;
2. a separate ordinary-SymPy symbolic tensor implementation of the Iter056X analytic formula `P=3 Pi_W Pi_R[C^2]`, with symbolic `kappa`, no import from the candidate evaluator, and no downstream fitted target.

The comparison step reports all six frozen checks `true`:

- candidate controls pass;
- independent reference control `P.R-3I3=0` passes;
- exact `I3` match;
- exact diagonal double-divergence `D` match;
- exact algebraic insertion `B=P.R` match;
- exact Euler-tensor component match.

No numerical tolerance is used.

The common exact origin values in the frozen `(-,+,+,+)` presentation are

`I3(0)/kappa^3 = 96`,

`D^{ii}(0)/kappa^3 = (-12, 92, 92, -196)`,

`B^{ii}(0)/kappa^3 = (-72, 72, 72, 72)`,

`E_W3,ii(0)/kappa^3 = (48, -208, -208, 368)`.

The fast candidate independently also passed its stronger coefficient-jet controls:

- `P.R=3I3` at the origin;
- `g^{ab}E_W3,ab=-I3` through coordinate degree two;
- `nabla_a E_W3^{ab}=0` through coordinate degree one;
- symmetry of `E_W3_ab` through coordinate degree two.

## Consequence for Iter057M

The component sign used by the fast finite-Taylor evaluator is now independently exact-controlled. The earlier opposite-sign component table recorded in the Iter057J derivation is not compatible with either of the two independent implementations in this audit.

The fast finite-Taylor representation may therefore be consumed as the exact source-jet implementation for Iter057M, subject to the remaining parent-gate obligations: full source-second-jet use, exact Q4 construction, canonical Noether compatibility, and independent unreduced substitution.

The historical Iter057K-lineage replay run `34952811799` remains an additional independent cross-check if/when it completes; its runtime is not required by this equivalence result.

## Scope locks

This PASS validates implementation equivalence only. It does not establish an open-neighborhood solution, physical characteristics, hyperbolicity, ghosts, stability, unitarity, regulator removal, UV completion, experimental confirmation, or QGR correctness. `c6` remains symbolic/unfixed; `beta=1` remains unauthorized; theory established remains `0%`.