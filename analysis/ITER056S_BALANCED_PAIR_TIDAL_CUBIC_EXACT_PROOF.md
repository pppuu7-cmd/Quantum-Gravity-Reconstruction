# Iter056S exact proof — balanced B4 pair tensor as a traceless spatial cubic-shape sector

Date: 2026-09-14
Preregistration: `f3e0daf1f164953c382753867ccba80852ec8283`
Hypothesis-generation chronology: `e89913217b12ff37cadcf7510d77e954fac55ecb`

This proof is generic in `(a,b)` and therefore implies all eight frozen held-out lanes. The separately launched GitHub Actions workflow is a reproducibility harness only; the mathematical classification below does not depend on runner availability.

## 1. Frozen G2 balanced sector

In edge order `(01,02,03,12,13,23)`, Iter003-G2 gives

`TT1=(0,1,-1,-1,1,0)`

`TT2=(1,0,-1,-1,0,1)`.

For

`x=a TT1+b TT2`,

we have exactly

`x01=b`, `x02=a`, `x03=-(a+b)`,

`x12=-(a+b)`, `x13=a`, `x23=b`.

Embed these as the off-diagonal entries of the symmetric zero-diagonal pair tensor

```
H(a,b) = [[0,       b,       a, -(a+b)],
          [b,       0, -(a+b),       a],
          [a, -(a+b),       0,       b],
          [-(a+b), a,       b,       0]].
```

Every row sum is zero. Therefore for the distinguished symmetric vector

`t=(1,1,1,1)^T`

we have

`H t=0`.

Thus the source-owned G2 balanced tensor acts entirely on the sum-zero three-dimensional subspace that G2 identifies as the spatial complement of the symmetric direction in its conditional Lorentzian seed.

## 2. Exact fixed eigenbasis

Define four mutually orthogonal vectors

`t  = ( 1, 1, 1, 1)`,

`v_a=(-1, 1,-1, 1)`,

`v_b=(-1,-1, 1, 1)`,

`v_c=( 1,-1,-1, 1)`.

Direct multiplication gives, for arbitrary `a,b`,

`H t   = 0`,

`H v_a = 2a v_a`,

`H v_b = 2b v_b`,

`H v_c = -2(a+b) v_c`.

This is stronger than a numerical spectral check: the eigenvectors are independent of `(a,b)`.

After normalization by `1/2`, `{v_a,v_b,v_c}` is a fixed orthonormal basis of the sum-zero spatial subspace. Hence the spatial restriction is exactly

`H_sp = diag(2a, 2b, -2(a+b))`

in that source-derived basis.

Therefore its characteristic polynomial is

`lambda (lambda-2a)(lambda-2b)(lambda+2(a+b))`,

and its spatial trace vanishes identically.

## 3. Exact cubic invariant

Because the fourth eigenvalue is zero,

`Tr(H^3)=Tr(H_sp^3)`.

Using the exact spatial eigenvalues,

`Tr(H_sp^3) = (2a)^3+(2b)^3+[-2(a+b)]^3`

`= 8[a^3+b^3-(a+b)^3]`

`= -24 a b (a+b)`.

Likewise

`det(H_sp)=(2a)(2b)[-2(a+b)]=-8ab(a+b)`

and, as expected for a traceless 3x3 tensor,

`Tr(H_sp^3)=3 det(H_sp)`.

Thus the balanced pair sector carries a nontrivial exact cubic invariant, with exact null loci `a=0`, `b=0`, or `a+b=0`.

## 4. Frozen H0 tidal-shape lane

For the preregistered H0 lane `a=b=3/2`,

`spec(H_sp)=(3,3,-6)=3(1,1,-2)`.

Therefore the source-owned G2 balanced pair sector contains **exactly** the eigenvalue shape of the G3/Iter040 weak-static H0 tidal Hessian `diag(1,1,-2)`, up to an overall amplitude and spatial basis orientation.

This is a shape statement only. No amplitude identification `a ↔ kappa`, no `beta`, no `c6`, and no continuum dynamical identification is made.

## 5. S4 covariance and cubic invariance

A generator permutation `p in S4` acts on the pair tensor by permutation conjugation

`H -> P H P^T`.

Because every permutation matrix satisfies

`P t=t`,

the sum-zero spatial subspace is preserved. Conjugation preserves the characteristic polynomial and all traces:

`Tr[(P H P^T)^n]=Tr(H^n)`.

Therefore for all 24 generator permutations:

- the zero symmetric mode is preserved;
- the spatial spectrum is preserved as a multiset;
- `Tr(H^2)` and `Tr(H^3)` are exactly invariant.

The 2D balanced sector is permuted within itself by the G2 S4 action, so this is the required exact covariance/invariance statement.

## 6. Frozen fixed-basis check

The preregistered orthonormal basis

`u1=(1,-1,0,0)/sqrt(2)`,

`u2=(1,1,-2,0)/sqrt(6)`,

`u3=(1,1,1,-3)/sqrt(12)`

is another orthonormal basis of the same sum-zero spatial subspace. Let `Q=[u1 u2 u3]` and `K=Q^T H Q`.

Because `Q Q^T` is the orthogonal projector onto the invariant spatial subspace and `H` vanishes on `t`, the matrices `K` and `H_sp` are related by a 3D orthogonal change of basis. Hence exactly

`Tr(K)=0`,

`Tr(K^2)=Tr(H^2)`,

`Tr(K^3)=Tr(H^3)`,

`det(K)=-8ab(a+b)`.

This proves the preregistered basis-independence predicates without numerical approximation to the square roots.

## 7. Frozen null and negative controls

### Cubic-null lane

For `a=5/3`, `b=-5/3`, the tensor is nonzero but `a+b=0`; therefore

`Tr(H^3)=0`

exactly, as preregistered.

### Unbalanced negative control

Add `delta(E_01+E_10)`, `delta=1/7`, without compensating any other edge. Then row 0 and row 1 each acquire nonzero row sum `delta`, so

`H_bad t != 0`.

Thus the control is rejected by the G2 balanced-sector zero-mode condition exactly.

## 8. Held-out lane implication

The proof is polynomial/algebraic in arbitrary rational `a,b`. Consequently every frozen held-out lane G0–G5 and the two special lanes satisfies the exact identities above. There is no lane-dependent fitting or threshold.

## Classification supported by the exact proof

`PASS_SCOPED_CONDITIONAL_ITER056S_BALANCED_PAIR_SECTOR_HAS_EXACT_TIDAL_CUBIC_SHAPE_BRIDGE`

The word **conditional** is essential: the underlying G2 decomposition into a Lorentzian symmetric-time direction plus spatial sum-zero subspace inherits G2's explicit null-link hypothesis, which was not derived from earlier CCRC axioms.

## Interpretation ceiling

This exact result establishes a kinematic representation/invariant bridge only:

`source-owned B4 balanced pair tensor`

` -> exact traceless symmetric tensor on the G2 spatial subspace`

` -> exact cubic invariant`

with the G3/Iter040 H0 eigenvalue shape present as one balanced direction.

It does **not** establish that a microscopic pair perturbation is physically the G3 tidal Hessian on one realized geometry; it does not identify amplitudes, `beta`, `kappa`, `c6`, curvature normalization, branch phases, a global micro→continuum map, a dynamical treatment, quantum measure closure, or QGR correctness.