#!/usr/bin/env python3
"""Iter013-G11: composition/gluing cocycle identifiability audit.

G10 showed that current QGR structural constraints leave a two-dimensional
S4-symmetric elementary-null cubic sector, reduced to one free coefficient
under strong pair-locality.  A natural next idea is to fix that coefficient by
composition/gluing consistency.

This audit separates two logically distinct requirements.

1) Associativity of action composition.  For any candidate polynomial P define
   the binary gluing defect (interaction/interface action)
       delta_P(x,y) = P(x+y) - P(x) - P(y).
   Associativity requires the cocycle identity
       delta(x,y)+delta(x+y,z) = delta(y,z)+delta(x,y+z).
   But because delta is a coboundary of P, this identity is automatic for *any*
   P.  Therefore composition associativity alone cannot identify either cubic
   shape or coefficient.

2) Strict zero-interface additivity on disjoint supports.  If one additionally
   demanded delta_P(x,y)=0 whenever x and y have disjoint microscopic support,
   then every mixed cubic monomial is forbidden.  Combined with the inherited
   elementary-axis null condition, the only S4-symmetric cubic is P=0.  Thus a
   nonzero cubic completion necessarily requires a physical interface/gluing
   term or additional microscopic higher-event data; naive strict additivity
   cannot produce it.

All statements are checked with exact integer/rational linear algebra in
independent lanes.  No GR/Regge/continuum nonlinear action is imported.
"""
import argparse, json
from fractions import Fraction
import numpy as np

ap=argparse.ArgumentParser(); ap.add_argument('--lane',type=int,required=True); a=ap.parse_args()
rng=np.random.default_rng(13011 + 104729*a.lane)

def invs(q):
    q=[int(v) for v in q]
    p1=sum(q); p2=sum(v*v for v in q); p3=sum(v*v*v for v in q)
    return (p1**3,p1*p2,p3)

def B1(q):
    x,y,z=invs(q); return x-z

def B2(q):
    x,y,z=invs(q); return y-z

def P(q,coef):
    c1,c2=map(int,coef)
    return c1*B1(q)+c2*B2(q)

def add(x,y): return [int(a)+int(b) for a,b in zip(x,y)]
def defect(x,y,coef): return P(add(x,y),coef)-P(x,coef)-P(y,coef)

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
    return r

# A. Associativity/cocycle is automatic for arbitrary coefficients.
cocycle_exact=True
nonzero_defects=0
for _ in range(256):
    x=list(map(int,rng.integers(-4,5,size=4)))
    y=list(map(int,rng.integers(-4,5,size=4)))
    z=list(map(int,rng.integers(-4,5,size=4)))
    coef=list(map(int,rng.integers(-7,8,size=2)))
    if coef==[0,0]: coef=[1,-2]
    lhs=defect(x,y,coef)+defect(add(x,y),z,coef)
    rhs=defect(y,z,coef)+defect(x,add(y,z),coef)
    if lhs!=rhs:
        cocycle_exact=False; break
    nonzero_defects += int(defect(x,y,coef)!=0)

# B. Determine how many coefficient directions strict disjoint-support
# additivity removes. Rows are coefficients multiplying B1 and B2 defects.
rows=[]
for _ in range(128):
    # choose a nontrivial partition of the four microscopic directions
    mask=np.array([True,True,False,False])
    rng.shuffle(mask)
    x=[0]*4; y=[0]*4
    for i in range(4):
        if mask[i]:
            v=int(rng.integers(-5,6)); x[i]=v if v else 1
        else:
            v=int(rng.integers(-5,6)); y[i]=v if v else -1
    rows.append([defect(x,y,[1,0]), defect(x,y,[0,1])])
disjoint_constraint_rank=rank_exact(rows)
remaining_dim_after_strict_disjoint_additivity=2-disjoint_constraint_rank

# C. Pair-local sector is B2 up to a free coefficient. Show that its interface
# defect is generically nonzero on disjoint support, hence strict additivity
# would force that coefficient to zero.
pairlocal_nonzero=0
pairlocal_trials=128
for _ in range(pairlocal_trials):
    idx=list(map(int,rng.permutation(4)))
    cut=int(rng.integers(1,4)); A=idx[:cut]; C=idx[cut:]
    x=[0]*4; y=[0]*4
    for i in A:
        v=int(rng.integers(-6,7)); x[i]=v if v else 2
    for i in C:
        v=int(rng.integers(-6,7)); y[i]=v if v else -2
    pairlocal_nonzero += int(defect(x,y,[0,1])!=0)

# D. The inherited elementary null property remains exact for both cubic bases.
axis_null=all(B1([t if i==k else 0 for i in range(4)])==0 and
              B2([t if i==k else 0 for i in range(4)])==0
              for k in range(4) for t in range(-8,9))

# E. Associativity provides zero independent linear coefficient constraints:
# evaluate the cocycle residual separately for each basis.
assoc_rows=[]
for _ in range(64):
    x=list(map(int,rng.integers(-5,6,size=4)))
    y=list(map(int,rng.integers(-5,6,size=4)))
    z=list(map(int,rng.integers(-5,6,size=4)))
    row=[]
    for coef in ([1,0],[0,1]):
        r=(defect(x,y,coef)+defect(add(x,y),z,coef)
           -defect(y,z,coef)-defect(x,add(y,z),coef))
        row.append(r)
    assoc_rows.append(row)
associativity_constraint_rank=rank_exact(assoc_rows)

pass_gate=(cocycle_exact and nonzero_defects>0 and axis_null
           and associativity_constraint_rank==0
           and disjoint_constraint_rank==2
           and remaining_dim_after_strict_disjoint_additivity==0
           and pairlocal_nonzero>0)

out={
 'gate':'ITER013-G11-GLUING-COCYCLE-IDENTIFIABILITY',
 'lane':a.lane,
 'associativity_cocycle_exact':cocycle_exact,
 'associativity_constraint_rank_on_cubic_coefficients':associativity_constraint_rank,
 'random_nonzero_interface_defects':nonzero_defects,
 'disjoint_support_additivity_constraint_rank':disjoint_constraint_rank,
 'remaining_cubic_dimension_after_strict_disjoint_additivity':remaining_dim_after_strict_disjoint_additivity,
 'pairlocal_disjoint_nonzero_fraction':pairlocal_nonzero/pairlocal_trials,
 'elementary_axis_null_exact':axis_null,
 'classification':('ASSOCIATIVITY_DOES_NOT_IDENTIFY_CUBIC_AND_STRICT_ADDITIVITY_KILLS_NONZERO_CUBIC' if pass_gate else 'GLUING_AUDIT_REQUIRES_FOLLOWUP'),
 'next_physics_requirement':'A nonzero nonlinear completion needs microscopic interface/higher-event information beyond formal associativity; the gluing defect itself must be physically derived or independently constrained.',
 'pass':pass_gate,
 'claim_guard':'This is an exact algebraic identifiability result for the current four-variable QGR cubic sector. It does not derive a nonlinear gravitational vertex. It shows that associativity of composition is automatically satisfied by the coboundary gluing defect and therefore cannot fix the cubic coupling, while imposing zero interaction across every disjoint gluing would overconstrain the sector to zero.'
}
print(json.dumps(out,sort_keys=True))
if not pass_gate: raise SystemExit(2)
