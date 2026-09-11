# QGR Iteration 003 — 4D Lorentzian/GR Seed Gate

Date: 2026-09-11
Status: `ACTIVE / BOOLEAN_CAUSAL_CELL_SEED_CONSTRUCTED`
Current task completion: **25%**
Canonical candidate-program readiness: **24%**
Physical ansatz promoted: **NO**
Lead architecture: **A / CCRC**

## Objective

Test whether the A/CCRC architecture can move beyond a directed chain toward a genuinely branching/recombining causal complex with a derived local dimension notion, while preserving exact rigidity and without inserting a background metric or Einstein-Hilbert action.

## Predeclared fatal rule

Reject A/CCRC in its current reconstruction form if obtaining a 4D Lorentzian/GR regime requires any of the following solely to hit the target:

- inserting a continuum background metric;
- assuming an Einstein-Hilbert action;
- choosing an arbitrary continuum/spectral function after the fact;
- adding gate-specific free coefficients with no generating principle;
- switching to a different realization for the GR limit.

## Seed construction — Boolean causal cell `B_d`

Define the events of `B_d` as all subsets of a set of `d` independent relational generators. The causal order is set inclusion:

`S -> T` when `S` is a proper subset of `T`, with elementary causal links given by adding one generator.

This gives a finite directed acyclic branching/recombining causal complex without a metric input.

### Derived combinatorial dimension

The number of rank-`r` events is

`N_r = C(d,r)`.

Hence the rank-generating polynomial is

`R_d(x) = sum_r C(d,r)x^r = (1+x)^d`.

The integer `d` is therefore recoverable directly from relational-order data, for example from `N_1=d` together with the binomial rank profile.

For the first 4-direction seed:

`B_4: N_r = (1,4,6,4,1)`

with exactly `2^4=16` events.

No continuum dimension or metric is inserted to obtain this `d=4` combinatorial dimension.

### Branching/recombination

From the bottom event to the top event of `B_d`, each maximal causal history is an ordering of the `d` generators. Therefore the number of maximal chains is exactly

`N_paths = d!`.

For `B_4`, `N_paths=24`.

## CCRC gluing on `B_d`

Retain the already-tested nontrivial CCRC label projector

`P = I - J/3`,

with `P^2=P`.

Along any `d`-step maximal causal chain,

`P^d = P`.

If all symmetry-related maximal chains carry an equal weight `w_d`, then exact coarse/refinement consistency requires

`d! * w_d * P = P`.

For nonzero `P`, this fixes the equal-chain weight uniquely:

`w_d = 1/d!`.

Thus for `B_4`, the symmetry-compatible refinement weight is fixed to

`w_4 = 1/24`.

This is not introduced as a tunable coupling; it is forced by path multiplicity + exact coarse-kernel closure in the scoped construction.

Reproducibility: `code/qgr_iter003_boolean_causal_cell.py`.

## Scoped result

`PASS_SCOPED_DERIVED_COMBINATORIAL_DIMENSION_AND_UNIQUE_PATH_NORMALIZATION`

Established in scope:

- branching/recombining causal complex exists;
- a dimension count can be derived from pure relational order data;
- `d=4` can be represented by a 16-event `B_4` cell with binomial rank profile `(1,4,6,4,1)`;
- CCRC projector gluing remains exact along every causal chain;
- symmetric path normalization is fixed to `1/d!` by refinement consistency, with no continuous coefficient freedom added.

## Critical boundary

This is **not yet 4D Lorentzian gravity**.

A combinatorial `d=4` does not by itself provide:

- Lorentzian signature;
- approximate local Lorentz invariance;
- metric/tetrad degrees of freedom;
- a massless spin-2 excitation;
- Einstein dynamics;
- the equivalence principle;
- continuum locality;
- physical clock/rod observables.

The current construction is therefore a seed only.

## Strongest new insight

The first non-chain refinement test did **not** immediately reintroduce arbitrary amplitude weights. Instead, branching multiplicity plus exact projector closure fixes the symmetric path weight factorially.

This strengthens A/CCRC as a rigidity architecture, but creates the next decisive question: can the same relational structure produce Lorentzian tensor dynamics rather than merely a finite causal combinatorics?

## Exact next gate — Iter003-G2

`QGR-ITER003-G2-LORENTZIAN-TENSOR-SEED`

1. Introduce no background metric.
2. Define the most general small perturbation of local relational incidence/gluing data around the symmetric `B_4` seed consistent with causal orientation.
3. Decompose perturbations into symmetry sectors before choosing dynamics.
4. Identify whether a tensor-like traceless sector exists that can propagate nontrivially under exact composition/refinement.
5. Test whether obtaining such a sector requires arbitrary functions or manually inserting continuum spin-2 structure.
6. Separate clearly: combinatorial dimension, causal order, Lorentzian signature, and GR dynamics must not be conflated.

If no candidate tensor/Lorentzian sector arises without importing continuum GR structure, record a scoped failure and redesign rather than inserting Einstein dynamics by hand.
