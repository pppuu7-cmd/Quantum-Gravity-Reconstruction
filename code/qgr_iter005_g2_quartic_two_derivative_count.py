#!/usr/bin/env python3
from fractions import Fraction

# Exact representation-theory count of local bosonic quartic vertices with
# total momentum degree two after momentum conservation / IBP quotient.
# Spatial symmetry: S4 on relational directions.
# Leg symmetry: S4 on four identical field legs.

sizes=[1,6,3,8,6]
# class order: e, (12), (12)(34), (123), (1234)
chi_H=[10,4,2,1,0]      # H=Sym^2(W4)
chi_W4=[4,2,0,1,0]
chi_U3=[3,1,-1,0,-1]    # standard 3D leg-momentum rep after k1+k2+k3+k4=0
sq=[0,0,0,3,2]
cube=[0,1,2,0,4]
fourth=[0,0,0,3,0]
cycle_types=[
    [1,1,1,1],
    [2,1,1],
    [2,2],
    [3,1],
    [4],
]

def power_class(g,L):
    if L==1:return g
    if L==2:return sq[g]
    if L==3:return cube[g]
    if L==4:return fourth[g]
    raise ValueError

def field_tensor_char(g,leg_class):
    out=1
    for L in cycle_types[leg_class]:
        out*=chi_H[power_class(g,L)]
    return out

def momentum_sym2_char(g,leg_class):
    chiA=chi_W4[g]*chi_U3[leg_class]
    chiA2=chi_W4[sq[g]]*chi_U3[sq[leg_class]]
    return Fraction(chiA*chiA+chiA2,2)

weighted=Fraction(0)
for gi,gs in enumerate(sizes):
    for li,ls in enumerate(sizes):
        weighted += gs*ls*field_tensor_char(gi,li)*momentum_sym2_char(gi,li)

dim=weighted/(24*24)
assert dim==1694

print({
    'field':'H=Sym^2(W4), dim 10',
    'quartic_bosonic_leg_group':'S4',
    'momentum_conservation_leg_rep':'U3 standard representation of S4',
    'total_derivative_degree':2,
    'physical_S4_invariant_quartic_vertex_dimension':int(dim),
    'classification':'PASS_SCOPED_COMPLETE_KINEMATIC_QUARTIC_TWO_DERIVATIVE_VERTEX_COUNT_1694',
    'guard':'Noether consistency and quartic uniqueness are not implied by this count',
})
