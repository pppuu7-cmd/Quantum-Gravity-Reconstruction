# Iter057M exact unrestricted quartic extension

Date: 2026-09-15
Gate: `ITER057M-GENERAL-QAB-SECOND-EVEN-JET-QUARTIC-EXTENSION`
Prospective preregistration: `9760ca0324dce13cf141a9f93b6ff69ea4c75605`
Parent Iter057L PASS: `24de1e6d28cfd78327b79568ac2398337c309ac4`

## Result

The unrestricted first-order nonconformal correction extends through the next nontrivial even G3/H0 source jet. An exact quartic trace-reversed jet exists that satisfies de Donder gauge through cubic coordinate order and the full unreduced linearized Einstein equation through quadratic order.

All calculations are exact rational/symbolic. No fitted coefficient, tolerance-based zero, restricted Q4 ansatz, fixed `c6`, or new background primitive is used.

## A. Exact Weyl3 source second jet

The exact source evaluator is `code/qgr_iter057m_exact_g3_weyl3_source_jet.py`, commit `f9181c7dda617ce4061fa90e73164e6cdbecd714`.

It implements the exact finite Taylor ring implied by the source-owned G3/H0 metric. Because the metric is exactly quadratic, exposing `E_W3` through coordinate degree two requires `P=dI3/dR` only through degree four. This is an exact finite-jet calculation, not a numerical truncation.

The component convention and analytic Iter056X normalization were independently validated by the prospectively frozen equivalence audit:

- preregistration `253fc53238ac58bbe4395e154e188e3d865217c2`;
- independent ordinary-SymPy reference `9c92a854fea23228162db591b7e62e7794594040`;
- workflow head `0f10ac644060d712e3edbd48fa2ef6bdced1fbe1`;
- Actions run `34954206549`, job `104332193998`;
- artifact `10390318470`, digest `sha256:ab331b2093e7d26e1d5f609f08e81c70739bb79d88a9a210a73ffc5b8155cd92`;
- durable audit result `688994108d3b28d9cdf7d7926236bece78222a94`.

The independent implementations agree exactly on

`I3(0)/kappa^3 = 96`,

`D^{ii}(0)/kappa^3 = (-12,92,92,-196)`,

`P.R insertion^{ii}(0)/kappa^3 = (-72,72,72,72)`,

`E_W3,ii(0)/kappa^3 = (48,-208,-208,368)`

in the frozen `(-,+,+,+)` presentation.

Define `Shat_ab=A_E S_ab=-E_W3_ab`. At `kappa=2/25`, the evaluator exposes all normalized coordinate second coefficients exactly. The compact factorized source values are

`Shat^(0)_ab/kappa^3 = diag(-48,208,208,-368)`.

The nonzero normalized quadratic coefficients `Shat_ab[alpha]/kappa^4`, with `alpha=(t,x,y,z)`, are:

- `00`: `(0,2,0,0)=-2912/3`, `(0,0,2,0)=-2912/3`, `(0,0,0,2)=-16064/3`;
- `11`: `(0,2,0,0)=7136/3`, `(0,0,2,0)=6880/3`, `(0,0,0,2)=-19328/3`;
- `12`: `(0,1,1,0)=128/3`;
- `13`: `(0,1,0,1)=-7264/3`;
- `22`: `(0,2,0,0)=6880/3`, `(0,0,2,0)=7136/3`, `(0,0,0,2)=-19328/3`;
- `23`: `(0,0,1,1)=-7264/3`;
- `33`: `(0,2,0,0)=-14624/3`, `(0,0,2,0)=-14624/3`, `(0,0,0,2)=14528/3`.

All time-containing second coefficients not listed above vanish exactly.

The same source evaluator passes identically:

- `P.R=3I3` at the origin;
- `g^{ab}E_W3_ab=-I3` through coordinate degree two;
- `nabla_a E_W3^{ab}=0` through coordinate degree one;
- symmetry of `E_W3_ab` through degree two.

Thus obligation A and the source side of G are satisfied.

## B-C. Exact operator coefficient jet and unrestricted Q4 space

The common normalized Taylor architecture was frozen before the solve in `19e76eb481d1cfd6c77b168ebe6320822510624b`.

The full unrestricted Q4 space has

- 10 symmetric tensor components `(ab)`;
- 35 completely symmetric rank-four derivative multi-indices;
- 350 exact unknowns.

No component/static/diagonal/conformal/plane-wave/spherical restriction is imposed.

The source-independent exact matrix is implemented in `code/qgr_iter057m_universal_q4_matrix.py`, corrected commit `d6533f3da3347cc6a8f76028040296c32cc50128`; derivation checkpoint `8a6a5a56f646b4c96fec4ac50ab392203d26475a`.

It gives exactly

`shape(M)=(180,350)`, `nnz(M)=720`,

`rank(M)=164`, `nullity(M)=186`, `left-nullity(M)=16`.

A canonical rank-16 Bianchi basis spans the complete left nullspace. For every free tensor index `b` and degree-one coordinate `j`, the exact affine identity is

`Y_(b,j)^T r = [nabla^a S_ab]_(degree-one,j)`.

This identity was proved symbolically for arbitrary algebraically independent `S^(0)` and `S^(2)`, not merely for the G3 numerical values. Hence the only affine compatibility conditions are precisely the sixteen Noether coefficients.

This satisfies obligations B, C and the structural part of G.

## D-E. Exact gauge and field solve

The exact constructor is `code/qgr_iter057m_q4_exact_constructor.py`, commit `40613aeca24383fc143e3e653e2aaee53dd30286`.

For the authorized G3/H0 source jet it finds

`rank([M|r])=rank(M)=164`,

all sixteen canonical compatibility contractions exactly zero, and one exact particular Q4 with the 186-dimensional homogeneous freedom retained by the matrix nullspace.

Choosing the canonical pivot particular solution by setting the free directions to zero produces only 32 nonzero normalized Q4 coefficients. The complete exact list is durably reproducible from the constructor and is also recorded in `derivations/ITER057M_DIAGNOSTIC_Q4_CANDIDATE_PENDING_SOURCE_AUDIT.md` (`cbc7bd1fa45e293a416992d3e9370fb946b34f92`); after the independent source equivalence PASS above, those source-specific values are now consumed as controlled exact evidence rather than merely diagnostic values.

The exact matrix residual is zero in all 180 rows. In particular:

- de Donder gauge is satisfied through cubic order;
- the reduced field equation is satisfied through quadratic order;
- gauge/free directions remain explicit as the 186-dimensional homogeneous solution space.

This satisfies obligations D and E.

## F. Independent unreduced control

Reduced-only self-consistency is not used as the final control.

The independent control `code/qgr_iter057m_q4_unreduced_control.py`, commit `1235e6a1909a7163733c8b76cb18200ece094cd0`, converts the trace-reversed correction back to the metric perturbation and recomputes the direct unreduced covariant linearized Ricci/Einstein variation.

Fresh-run provenance:

- workflow head `489bfbd845a98decad44aa271f0f6d3d810f116d`;
- Actions run `34954412091`;
- job `104332863586`;
- artifact `10390657547`, digest `sha256:78aca057d3fd2ef4db1d7e746e188c625a02eda14c41c902fcee642bf886208c`.

The job reports exactly:

- all four de Donder components equal zero through coordinate degree three;
- all ten independent components of `DG_ab-S_ab` equal zero through coordinate degree two;
- no tolerance is used.

The aggregate checks are all true:

`source_controls`, `rank_augmented_equals_rank`, `compatibility_16_zero`, `particular_residual_zero`, `unreduced_controls`.

This satisfies obligation F and independently reconfirms D-E.

## G. Noether/source compatibility

The universal coefficient identity

`Y_(b,j)^T r=[nabla^a S_ab]_(1,j)`

combined with the exact source evaluation `nabla_a E_W3^{ab}=0` through degree one gives all sixteen concrete compatibility conditions identically zero.

The constructor independently reports the literal vector

`(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)`.

Thus G is satisfied without deleting equations or assuming compatibility post hoc.

## Frozen-obligation disposition

- A exact source second jet: **SATISFIED**.
- B exact operator coefficient jet: **SATISFIED**.
- C unrestricted 350-component Q4 space: **SATISFIED**.
- D de Donder through cubic order: **SATISFIED**.
- E exact field equation through quadratic order: **SATISFIED**.
- F independent unreduced substitution: **SATISFIED**.
- G exact Noether/source compatibility: **SATISFIED**.

Therefore the prospective Iter057M maximum scoped PASS criterion is met exactly.

## Scope ceiling

This is a finite local Taylor certificate through the second even source order. It does not prove existence or convergence on an open neighborhood, does not construct global/asymptotic boundary data, and does not establish physical characteristics, strong hyperbolicity, mode/ghost content, stability, unitarity, regulator removal, UV completion, experiment, or QGR correctness.

`c6` remains symbolic/unfixed; `beta=1` remains unauthorized; theory established remains `0%`.