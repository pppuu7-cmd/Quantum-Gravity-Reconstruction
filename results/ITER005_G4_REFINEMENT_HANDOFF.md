# QGR Iter005-G4 — same-realization refinement handoff

Date: 2026-09-11
Status: `PARTIAL_KINEMATIC_REFINEMENT_EXISTS__DYNAMIC_REFINEMENT_BLOCKED_BY_MEASURE_COMPOSITION_AMBIGUITY`

## Objective

After local quadratic/cubic/quartic closure and weak-background characteristic stability, determine whether QGR can enter a same-realization refinement/coarse-graining program without splicing in a separate continuum theory.

## Exact coherent refinement structure retained from the Boolean seed

For one symmetric `B4` cell there are

`4! = 24`

maximal causal histories and exact equal-history normalization

`w_4 = 1/24`.

Under an `n`-level coherent refinement in which every level repeats the same normalized local cell structure,

- history count: `(4!)^n`;
- weight of one fine history: `(1/4!)^n`;
- total normalized history weight: `1`.

Thus the original path-normalization/refinement rule extends multiplicatively without introducing a new scalar weight.

This is a valid exact **coherent-sector kinematic tower**.

## Second-moment functoriality

The QGR-L1 local field is

`G in Sym^2(W4)`.

For a linear rank-1 frame map `R`, the induced second-moment map is canonically

`G -> Sym^2(R) G`.

Therefore ordinary deterministic frame relabelings/refinements have a natural action on the same ten-component field arena, and the pullback transformation law remains functorial.

This establishes a same-realization kinematic handoff at the level of deterministic maps.

## The first genuine coarse-graining ambiguity

A block containing multiple fine frame realizations exposes two distinct natural operations.

### A. Mixture / marginal second moment

If coarse-graining means marginalizing a mixture of fine realizations with normalized weights `w_alpha`, then

`G_mix = sum_alpha w_alpha G_alpha`.

This is closed linearly on `Sym^2(W4)`.

### B. Second moment of a composed/averaged rank-1 frame

If the coarse rank-1 frame is first composed or averaged,

`e_bar = sum_alpha w_alpha e_alpha`,

then

`G_comp = e_bar e_bar^T`.

For deterministic fine vectors,

`G_mix - G_comp = sum_alpha w_alpha (e_alpha-e_bar)(e_alpha-e_bar)^T`.

The right-hand side is the fine-frame covariance. It is generically nonzero.

For stochastic/quantum fine frames the analogous expression requires cross-correlations between fine realizations. Those cross-correlations are not specified by the present local second-moment field alone.

## Exact counterexample

For two equally weighted fine frames

`e1=(1,0,0,0)`,

`e2=(0,1,0,0)`,

one has

`G_mix = diag(1/2,1/2,0,0)`,

while

`G_comp = (1/4) [[1,1,0,0],[1,1,0,0],[0,0,0,0],[0,0,0,0]]`.

They are not equal.

Thus the current QGR ontology does not uniquely determine which coarse second moment is physically correct.

## Scientific decision

QGR must **not** choose one refinement prescription merely because it preserves the desired local action.

The next stage requires a primitive measure/amplitude/composition object that fixes how fine relational-frame realizations combine. Only then can projective consistency and same-realization coarse dynamics be tested without post-hoc selection.

Classification:

`PARTIAL_PASS_KINEMATIC_SAME_REALIZATION_TOWER__BLOCKED_DYNAMIC_COARSE_GRAINING_UNTIL_MEASURE_OR_COMPOSITION_OBJECT_IS_DEFINED`.

## Consequence for roadmap

Local nonlinear closure is sufficiently advanced to activate R5, but R5 begins with a measure/composition reconstruction problem rather than with a chosen RG rule.

Required next questions:

1. what is the primitive fine-grained amplitude/probability object over relational-frame histories;
2. how are correlations between adjacent/fine cells represented;
3. which marginal/composition rule is forced by normalization and causal gluing;
4. whether the induced map closes on `G` alone or requires a controlled hierarchy of higher moments;
5. whether QGR-L1 local couplings are stable/relevant under that induced coarse map.

## Scope guard

No continuum limit, RG fixed point, quantum measure, or macroscopic GR theorem is claimed here.

## Reproducibility

`code/qgr_iter005_g4_refinement_handoff.py`
