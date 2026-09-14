# Iter055P terminal result — cell-relative covariant smearing class and boundary causal type

Date: 2026-09-14
Preregistration: `cab24dfced6e38f77b5034cf5f868a08817eb9c6`

## Terminal classification

`PASS_SCOPED_PARTIAL_ITER055P_CELL_RELATIVE_CLASS_EXISTS_FOR_SPACELIKE_B3_TIMELIKE_NORMAL__TIMELIKE_B3_NEEDS_EXTRA_ANCHOR`

## 1. Spacelike B3 / future-timelike normal: nonempty normalized class exists

On a regular spacelike B3 face let `n` be the future-timelike unit normal supplied by the Iter055O normal line plus time orientation. In the rest frame of `n`, every future null momentum can be written with

`E = n.k > 0`,

and the invariant null-cone measure has radial form

`dmu = C * E dE dOmega`

for a fixed convention-dependent constant `C`.

For any radial shape satisfying

`integral_0^infinity s |f(s)|^2 ds < infinity`,

define the envelope factor

`phi_(h,n)(k) = h f(h E)`.

Then

`||phi_(h,n)||^2 = C integral dOmega integral_0^infinity E dE h^2 |f(hE)|^2`

and the substitution `s=hE` gives

`||phi_(h,n)||^2 = C integral dOmega integral_0^infinity s |f(s)|^2 ds`,

independent of `h`.

Thus the symbolic microscopic refinement scale can parameterize a nonempty norm-controlled envelope class even though G7A leaves its absolute physical calibration unfixed.

A complete physical Hilbert-dual kernel also contains angular/polarization/tensor structure. G6F already establishes nontrivial physical quotient fibers and admissible physical wavepacket sections, so the radial class is nonempty; Iter055P does **not** select a unique polarization/tensor section.

## 2. Exact refinement/dilation law

The massless cone measure scales as

`dmu(r k) = r^2 dmu(k)`.

Hence the dilation operator

`(D_r a)(k) = r a(r k)`

is unitary on the scalar radial part of the one-particle `L2` measure (and acts fiberwise on the physical quotient when the quotient data are transported accordingly).

If refinement sends

`h -> h/r`,

then

`phi_(h/r,n)(k) = (h/r) f((h/r)E)`

which equals

`D_(1/r) phi_(h,n)(k) = (1/r) phi_(h,n)(k/r)`.

Therefore the class has an exact norm-preserving scale-covariant refinement law without knowing the numerical physical value of `h`.

## 3. Lorentz covariance at class level

Because the envelope depends on the scalar `n.k`, transforming both data together,

`n -> Lambda n`, `k -> Lambda k`,

preserves the profile argument. Combined with the invariant cone measure, the family transforms covariantly. No preferred coordinate frame is introduced by the class itself.

This differs from Iter055N's forbidden universal fixed profile: the kernel is now relationally anchored by the physical boundary normal.

## 4. Timelike B3 / spacelike normal: one normal is insufficient

Let the unit normal be spacelike. In a Lorentz frame take it along one spatial axis. For future null momentum `k=r(1,hat p)`, write `u` for the cosine of the angle to the normal. Then

`n.k` is proportional to `r u`.

For an envelope depending only on this relational scalar,

`phi(k)=h f(h r u)`,

the norm contains

`h^2 integral_0^infinity r dr integral_{-1}^{1} du |f(h r u)|^2`.

With `t=h r u`, the angular integral becomes

`1/(h r) integral_{-h r}^{h r} |f(t)|^2 dt`.

Therefore the full norm is proportional to

`integral_0^infinity ds F(s)`,

where

`F(s)=integral_{-s}^{s}|f(t)|^2 dt`.

For any nonzero measurable `f` with nonzero square-integral on some bounded interval, `F(s)` is bounded below by a positive constant for all sufficiently large `s`. The final integral diverges.

Thus no nonzero square-integrable full-cone envelope can depend only on `h(n.k)` when `n` is spacelike. Geometrically, arbitrarily large null momenta nearly tangent to the timelike boundary have `n.k` near zero, so this single scalar does not control the ultraviolet directions.

A timelike B3 therefore needs additional relational data, such as a timelike boundary observer/velocity, another independent normal/frame vector, a source/preparation momentum, or a more structured tensor/kernel construction. No such extra datum is selected here.

## 5. Absolute scale remains a separate blocker

The class-level refinement relation uses symbolic `h` internally. It does not lift the G7A degeneracy

`h -> lambda h`, `kappa -> lambda^2 kappa`.

Consequently the bridge may be formulated dimensionlessly on the spacelike-B3 scope before absolute calibration, but no absolute detector frequency, length, decoherence rate or experimental scale follows.

## Scientific consequence

The bridge problem is now causally stratified:

### Spacelike B3
`embedded B3 + metric -> future-timelike normal n`

`(n,h) -> nonempty covariant normalized radial smearing class with exact refinement dilation`

but profile shape, angular/polarization structure, B3 observable attachment and refinement coefficients remain unfixed.

### Timelike B3
`spacelike normal + h`

is insufficient by itself to produce a nonzero full-cone `L2` envelope. An additional relational anchor is mathematically required.

The next highest-information question is whether QGR already contains a source-defined timelike relational datum on the boundary/readout sector and, independently, whether refinement/locality can reduce the free radial shape `f` on the spacelike-B3 sector.

## Claim ceiling

No concrete kernel, full all-boundary bridge, interacting quantum channel, absolute `h`, beta/c6 fixing, Weyl3 treatment, regulator removal, full unitarity, UV completion, GR recovery, experiment or theory establishment follows. Theory established remains 0%.

No GitHub Actions run was required; this is an exact measure/scaling result.
