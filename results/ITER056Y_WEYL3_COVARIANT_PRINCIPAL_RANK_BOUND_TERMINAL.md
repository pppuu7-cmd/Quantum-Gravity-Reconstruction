# Iter056Y terminal result — covariant Weyl3 principal-rank bound

Date: 2026-09-15
Gate: `ITER056Y-WEYL3-COVARIANT-PRINCIPAL-RANK-BOUND-AND-MIXED-ORDER-OBLIGATION`
Prospective preregistration: `1bbace13da050dc671200ec46dfae9981ae3c406`
Upstream covariant variation: `7162882d6a22ad567b8cee0a02868922bf7b0e85`

## Terminal classification

**`PASS_SCOPED_ITER056Y_WEYL3_K4_SYMBOL_RANK_BOUND_FORCES_MIXED_ORDER_PHYSICAL_QUOTIENT_ANALYSIS`**

Here “physical quotient” in the frozen classification means the local symmetric-metric perturbation space modulo infinitesimal diffeomorphism directions. It is **not** yet a count of propagating physical modes or a quantum physical Hilbert space.

## 1. Principal-symbol object

Let `E_W3^{ab}[g]` be the Iter056X covariant Euler response and linearize it about an arbitrary smooth background `gbar`:

`delta E_W3^{ab}[h] = sigma4^{ab}(k)[h] + lower homogeneous degree in k`,

where `sigma4(k)` denotes only the homogeneous degree-four metric principal symbol. `c6` is an overall symbolic multiplier and plays no role in the rank bound for nonzero `c6`.

The result below concerns nonzero **non-null** covectors `k_a`, `k^2 != 0`.

## 2. Noether identity forces transverse output at k4

Iter056X established the exact off-shell identity

`nabla_a E_W3^{ab}=0`.

Linearizing gives

`nabla_bar_a delta E_W3^{ab} + delta Gamma^a_ac Ebar^{cb} + delta Gamma^b_ac Ebar^{ac}=0`.

The first term differentiates a fourth-order metric operator and therefore contains the degree-five principal part

`k_a sigma4^{ab}(k)[h]`.

The connection-variation terms contain only one derivative of `h` multiplying the fixed background response and cannot contribute at degree five. Therefore the degree-five identity is exactly

**`k_a sigma4^{ab}(k)[h] = 0`**

for every symmetric `h_ab`.

Thus the image of the pure Weyl3 `k4` symbol lies in the transverse symmetric-tensor subspace.

## 3. Trace identity forces traceless output at k4

Iter056X also established the exact four-dimensional trace identity

`g_ab E_W3^{ab} = - I3`.

Linearizing,

`h_ab Ebar_W3^{ab} + gbar_ab delta E_W3^{ab} = - delta I3`.

The first term contains no derivatives of `h`. Since `I3` is algebraic in curvature, `delta I3` contains at most second derivatives of `h`. Hence neither side apart from `gbar_ab delta E_W3^{ab}` contains a degree-four contribution. Therefore its degree-four part must vanish:

**`gbar_ab sigma4^{ab}(k)[h] = 0`**.

So the image of `sigma4(k)` is simultaneously transverse and traceless.

## 4. Exact output dimension for non-null k

The space of symmetric rank-two tensors in four dimensions has dimension 10.

Define

`T_k : Sym^2 -> V`,

`(T_k t)^b = k_a t^{ab}`.

For `k^2 != 0`, `T_k` is surjective. Given any vector `v^b`, one explicit symmetric preimage is

`t^{ab} = (k^a v^b + k^b v^a)/k^2 - (k.v) k^a k^b/(k^2)^2`,

for which `k_a t^{ab}=v^b`.

Therefore the transverse subspace has dimension

`10 - 4 = 6`.

On that transverse subspace the trace condition is independent when `k^2 != 0`. An explicit transverse tensor with nonzero trace is

`pi^{ab} = gbar^{ab} - k^a k^b/k^2`,

which obeys

`k_a pi^{ab}=0`,

while in four dimensions

`gbar_ab pi^{ab}=4-1=3 != 0`.

Therefore imposing tracelessness removes one further independent dimension. The simultaneous transverse-traceless output space has exact dimension

**`dim TT(k) = 10 - 4 - 1 = 5`**

for every non-null `k`.

Consequently

**`rank sigma4(k) <= 5`**.

This is an exact algebraic upper bound; the rank may be lower on special backgrounds or covectors. In particular, on a conformally flat background the Weyl3 `k4` symbol vanishes entirely.

## 5. Four exact input gauge null directions

At principal order an infinitesimal diffeomorphism generates

`h_ab = k_a xi_b + k_b xi_a`.

The principal linearized Riemann/Weyl tensor of such a perturbation vanishes identically, hence so does the Weyl3 curvature-Hessian `k4` response. Therefore

`sigma4(k)[k_(a xi_b)] = 0`.

For `k^2 != 0`, the map

`G_k : xi_b -> k_a xi_b + k_b xi_a`

is injective. If `G_k xi=0`, contraction with `k^a` gives

`k^2 xi_b + k_b(k.xi)=0`.

Contract once more with `k^b`:

`2 k^2(k.xi)=0`.

Since `k^2 != 0`, `k.xi=0`, and then `xi_b=0`. Thus the gauge subspace has exact dimension 4.

The local metric perturbation quotient by these diffeomorphism directions therefore has dimension

**`10 - 4 = 6`**.

The principal symbol descends to a map from this six-dimensional quotient because the gauge subspace lies in its kernel.

## 6. Exact quotient rank/nullity consequence

The descended Weyl3 fourth-order symbol has a six-dimensional domain but image contained in the five-dimensional transverse-traceless space. Therefore, by rank-nullity,

**`rank sigma4_bar(k) <= 5`**

and

**`dim ker sigma4_bar(k) >= 1`**

for every non-null covector `k`.

This is the new structural result of Iter056Y.

The pure Weyl3 fourth-order correction is therefore **intrinsically rank-deficient on the diffeomorphism quotient**. It cannot be a uniformly nondegenerate fourth-order principal operator on all six quotient directions.

The statement is an upper/lower bound, not an assertion that the generic rank is always exactly five or the quotient nullity always exactly one.

## 7. Independent consistency with Iter054C/D

Only after deriving the exact bound, compare with the earlier finite exact panels:

- Iter054C independently certified four pure-gauge principal null directions and nonzero Weyl-active `k4` activation.
- Iter054D independently certified that a fourth-order gauge completion lifts the four gauge null directions while leaving the quotient bilinear invariant.
- Iter054D also found correction-only rank 4 / nullity 6 on its **null-covector** diagnostic panel. This does not contradict Iter056Y: the present exact dimension theorem is explicitly for `k^2 != 0`, and it is only an upper bound `rank<=5`.

Iter056Y is stronger in a different sense: it supplies a background-independent covariant rank obstruction for every non-null covector, rather than another sampled rank panel.

## 8. PDE consequence — mixed order is mandatory

Because at least one non-gauge quotient direction is annihilated by the pure `k4` block for every non-null `k`, the full Einstein plus Weyl3 linearized equations cannot be treated as a uniformly fourth-order system on the entire six-dimensional diffeomorphism quotient.

At least one quotient direction is necessarily controlled at leading order by lower-degree pieces, including the Einstein `k2` symbol and/or lower-order Weyl3 terms.

Therefore the correct local characteristic object is a **mixed-order principal pencil**, schematically

`M_phys(k) = M2_phys(k) + c6 M4_phys(k)`,

with order assignments handled in a mixed-order / Douglis-Nirenberg-compatible way rather than by declaring `M4` alone to be the complete physical principal operator.

This sharpens the unresolved obligation left by Iter054D.

## 9. What this does not prove

The rank deficiency does **not** by itself imply:

- failure of strong hyperbolicity of the mixed Einstein+Weyl3 system;
- complex characteristics;
- an additional physical ghost;
- instability or negative energy;
- a physical exact-vs-order-reduced treatment choice;
- quantum nonunitarity;
- a value/sign/running of `c6`.

Mixed-order systems may or may not be hyperbolic; that requires analysis of the full mixed-order pencil, not of `M4` alone.

The six-dimensional quotient used here is a local diffeomorphism quotient of symmetric metric perturbations, not a claim that six propagating physical gravitational modes exist.

## 10. Production decision

No GitHub Actions production was launched. The gate asks for an exact consequence of already-certified covariant identities and finite-dimensional rank-nullity. A numerical matrix panel cannot strengthen the universal rank bound and would duplicate Iter054C/D rather than test a new computational hypothesis.

## Claim locks

`c6` remains symbolic/unfixed; `beta=1` remains unauthorized; no physical Weyl3 treatment is selected; no strong-hyperbolicity, energy, ghost, unitarity, UV-completion, experiment, or theory-establishment claim is authorized. `theory established = 0%`.