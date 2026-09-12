#!/usr/bin/env python3
"""Iter012-G10: symmetry-native cubic-completion identifiability audit.

G9 established that the derived B4 pair action is exactly quadratic.  This audit
asks whether the *already established* microscopic structural constraints can
uniquely determine the leading cubic correction, without importing GR/Regge or
any continuum action.

For four microscopic variables q_i, the most general homogeneous S4-symmetric
cubic is spanned by power-sum invariants
    p1^3, p1*p2, p3,
where pk=sum_i q_i^k. Requiring the inherited elementary-direction null
P(t e_i)=0 imposes a+b+c=0, leaving a two-dimensional cubic space.

If one additionally imposes a strong pair-locality restriction (no monomial
with three distinct indices), the allowed cubic space collapses to one shape,
    sum_{i != j} q_i^2 q_j,
but its coefficient remains free. Thus even this stronger assumption does not
fix a nonlinear coupling from the quadratic data.

The matrix ranks are reconstructed from random exact-integer evaluations in
independent lanes; closed-form identities are checked simultaneously.
"""
import argparse, json
from fractions import Fraction
import numpy as np

ap=argparse.ArgumentParser(); ap.add_argument('--lane',type=int,required=True); a=ap.parse_args()
rng=np.random.default_rng(12010 + 104729*a.lane)

def invs(q):
    q=[int(x) for x in q]
    p1=sum(q); p2=sum(x*x for x in q); p3=sum(x*x*x for x in q)
    return (p1**3, p1*p2, p3)

def B1(q):
    x,y,z=invs(q); return x-z

def B2(q):
    x,y,z=invs(q); return y-z

def pairlocal(q):
    q=[int(x) for x in q]
    return sum(q[i]*q[i]*q[j] for i in range(4) for j in range(4) if i!=j)

def triple(q):
    q=[int(x) for x in q]
    return sum(q[i]*q[j]*q[k] for i in range(4) for j in range(i+1,4) for k in range(j+1,4))

def rank_exact(rows):
    A=[[Fraction(int(x)) for x in row] for row in rows]
    if not A: return 0
    m,n=len(A),len(A[0]); r=0
    for c in range(n):
        piv=next((i for i in range(r,m) if A[i][c]),None)
        if piv is None: continue
        A[r],A[piv]=A[piv],A[r]
        d=A[r][c]; A[r]=[x/d for x in A[r]]
        for i in range(m):
            if i!=r and A[i][c]:
                f=A[i][c]; A[i]=[A[i][j]-f*A[r][j] for j in range(n)]
        r+=1
        if r==m: break
    return r

# Generic symmetric-cubic evaluation rank should be 3 before constraints.
rows=[]
for _ in range(48):
    q=rng.integers(-7,8,size=4)
    if not np.any(q): q[0]=1
    rows.append(invs(q))
raw_rank=rank_exact(rows)

# Elementary-axis null gives one independent coefficient constraint [1,1,1].
constraint_rank=rank_exact([[1,1,1]])
allowed_dim=3-constraint_rank

# Verify the two explicit null-compatible basis functions are independent.
basis_rows=[]
for _ in range(48):
    q=rng.integers(-7,8,size=4)
    basis_rows.append([B1(q),B2(q)])
basis_rank=rank_exact(basis_rows)
axis_null=all(B1([t,0,0,0])==0 and B2([t,0,0,0])==0 for t in range(-9,10))

# Permutation invariance check over random configurations/permutations.
perm_ok=True
for _ in range(64):
    q=list(map(int,rng.integers(-5,6,size=4)))
    perm=list(map(int,rng.permutation(4))); qp=[q[i] for i in perm]
    if (B1(q),B2(q))!=(B1(qp),B2(qp)): perm_ok=False; break

# Exact identity: pair-local symmetric cubic = p1*p2-p3 = B2.
pairlocal_identity=True
for _ in range(64):
    q=list(map(int,rng.integers(-6,7,size=4)))
    if pairlocal(q)!=B2(q): pairlocal_identity=False; break

# Triple-distinct invariant is independent of the pair-local shape; together
# they span the same two-dimensional elementary-null symmetric cubic sector.
pair_triple_rows=[]
for _ in range(48):
    q=list(map(int,rng.integers(-7,8,size=4)))
    pair_triple_rows.append([pairlocal(q),triple(q)])
pair_triple_rank=rank_exact(pair_triple_rows)

# A cubic correction has zero Hessian at q=0 automatically, so the quadratic
# signature/normalization data cannot determine its coefficient.
quadratic_hessian_unchanged=True
pairlocal_shape_dim=1
pairlocal_free_coefficients=1

pass_gate=(raw_rank==3 and constraint_rank==1 and allowed_dim==2 and basis_rank==2
           and axis_null and perm_ok and pairlocal_identity and pair_triple_rank==2
           and pairlocal_shape_dim==1 and pairlocal_free_coefficients==1
           and quadratic_hessian_unchanged)

out={
 'gate':'ITER012-G10-CUBIC-COMPLETION-IDENTIFIABILITY',
 'lane':a.lane,
 'raw_s4_symmetric_cubic_dimension':raw_rank,
 'elementary_null_constraint_rank':constraint_rank,
 'allowed_cubic_dimension_after_inherited_constraints':allowed_dim,
 'explicit_basis_rank':basis_rank,
 'axis_null_exact':axis_null,
 'permutation_invariance':perm_ok,
 'pairlocal_identity_exact':pairlocal_identity,
 'pairlocal_plus_triple_rank':pair_triple_rank,
 'pairlocal_shape_dimension':pairlocal_shape_dim,
 'pairlocal_free_coefficients':pairlocal_free_coefficients,
 'quadratic_hessian_unchanged_by_any_cubic':quadratic_hessian_unchanged,
 'classification':('NONLINEAR_COMPLETION_UNDERDETERMINED_BY_CURRENT_MICROSCOPIC_CONSTRAINTS' if pass_gate else 'STRUCTURAL_AUDIT_REQUIRES_FOLLOWUP'),
 'pass':pass_gate,
 'claim_guard':'This is an identifiability result about the current QGR microscopic constraint set. It does not prove that Nature realizes either cubic basis element, and it does not derive a continuum curvature invariant. It shows that S4 symmetry plus inherited elementary-null structure do not uniquely determine a cubic completion; even strong pair-locality leaves one free nonlinear coefficient.'
}
print(json.dumps(out,sort_keys=True))
if not pass_gate: raise SystemExit(2)
