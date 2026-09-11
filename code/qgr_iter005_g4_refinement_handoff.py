#!/usr/bin/env python3
from fractions import Fraction

F=Fraction

# Exact coherent Boolean refinement normalization.
for n in range(1,9):
    histories=24**n
    weight=F(1,24)**n
    assert histories*weight==1

# Exact second-moment mixture vs composed-frame counterexample.
e1=[F(1),0,0,0]
e2=[0,F(1),0,0]
w=[F(1,2),F(1,2)]

def outer(a,b):return [[a[i]*b[j] for j in range(4)] for i in range(4)]
def add(A,B):return [[A[i][j]+B[i][j] for j in range(4)] for i in range(4)]
def scale(A,s):return [[s*A[i][j] for j in range(4)] for i in range(4)]

Gmix=add(scale(outer(e1,e1),w[0]),scale(outer(e2,e2),w[1]))
ebar=[w[0]*e1[i]+w[1]*e2[i] for i in range(4)]
Gcomp=outer(ebar,ebar)
Cov=[[Gmix[i][j]-Gcomp[i][j] for j in range(4)] for i in range(4)]
assert Gmix!=Gcomp

# Verify covariance identity sum w (e-e_bar)(e-e_bar)^T.
Cov2=[[F(0) for _ in range(4)] for __ in range(4)]
for wa,e in zip(w,(e1,e2)):
    d=[e[i]-ebar[i] for i in range(4)]
    Cov2=add(Cov2,scale(outer(d,d),wa))
assert Cov==Cov2

print({
    'coherent_refinement_levels_checked':8,
    'normalization_identity':'24^n * (1/24)^n = 1',
    'mixture_second_moment':Gmix,
    'second_moment_of_mean_frame':Gcomp,
    'covariance_difference':Cov,
    'mixture_equals_composed':False,
    'classification':'PARTIAL_KINEMATIC_REFINEMENT_EXISTS__DYNAMIC_REFINEMENT_REQUIRES_MEASURE_OR_COMPOSITION_OBJECT',
})
