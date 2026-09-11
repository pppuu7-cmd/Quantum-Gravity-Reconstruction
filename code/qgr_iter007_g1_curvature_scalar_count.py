#!/usr/bin/env python3
"""Exact algebraic count for one-curvature scalar contractions.

At total derivative order two, a metric-compatible torsion-free construction can
contain at most one Riemann tensor.  With no extra tensors, the three pairings
of its four indices by two inverse metrics reduce to one nonzero scalar:
  g^{ac}g^{bd} R_abcd = R,
  g^{ad}g^{bc} R_abcd = -R,
  g^{ab}g^{cd} R_abcd = 0.

The script verifies these identities exactly on a generic formal algebraic
curvature tensor represented as a symmetric bilinear form on Lambda^2.
"""
from fractions import Fraction
import itertools

N=4
pairs=[(i,j) for i in range(N) for j in range(i+1,N)]
pidx={p:k for k,p in enumerate(pairs)}

# Generic exact symmetric bilinear form on Lambda^2; distinct coefficients.
S=[[Fraction(0) for _ in range(6)] for __ in range(6)]
q=1
for a in range(6):
    for b in range(a,6):
        S[a][b]=S[b][a]=Fraction(q)
        q+=1

def sign_pair(i,j):
    if i==j:return 0,None
    if i<j:return 1,(i,j)
    return -1,(j,i)

def R(a,b,c,d):
    s1,p1=sign_pair(a,b); s2,p2=sign_pair(c,d)
    if s1==0 or s2==0:return Fraction(0)
    return s1*s2*S[pidx[p1]][pidx[p2]]

# Use the identity inverse metric: contraction identities depend only on the
# pair antisymmetries.  (The symmetric-pair exchange is already in S.)
C1=sum(R(a,b,a,b) for a in range(N) for b in range(N))
C2=sum(R(a,b,b,a) for a in range(N) for b in range(N))
C3=sum(R(a,a,c,c) for a in range(N) for c in range(N))
assert C1!=0
assert C2==-C1
assert C3==0

print({
    'naive_double_metric_pairings':3,
    'pairing_relations':['C2=-C1','C3=0'],
    'nonzero_scalar_contraction_dimension':1,
    'classification':'PASS_SCOPED_ONE_RIEMANN_METRIC_ONLY_SCALAR_SPACE_IS_ONE_DIMENSIONAL',
})
