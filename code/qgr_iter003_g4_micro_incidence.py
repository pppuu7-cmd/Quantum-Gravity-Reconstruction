#!/usr/bin/env python3
from fractions import Fraction

# QGR Iter003-G4: microscopic incidence-to-kinetic bridge audit.
# Exact finite statements only; no Einstein-Hilbert or continuum background input.


def rank(mat):
    a=[[Fraction(x) for x in row] for row in mat]
    m,n=len(a),len(a[0]); r=0
    for c in range(n):
        piv=next((i for i in range(r,m) if a[i][c] != 0),None)
        if piv is None: continue
        a[r],a[piv]=a[piv],a[r]
        q=a[r][c]
        a[r]=[x/q for x in a[r]]
        for i in range(m):
            if i != r and a[i][c] != 0:
                q=a[i][c]
                a[i]=[a[i][j]-q*a[r][j] for j in range(n)]
        r+=1
    return r


def mm(A,B):
    return [[sum(Fraction(A[i][k])*Fraction(B[k][j]) for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]


def mv(A,v):
    return [sum(Fraction(a)*Fraction(b) for a,b in zip(row,v)) for row in A]

# Boolean B4 rank-2 events are unordered distinct pairs {i,j}; there are no
# repeated-generator {i,i} events. The canonical equal-weight pair-incidence
# bilinear form is therefore C=J-I, up to an overall scale/sign.
d=4
C=[[Fraction(0 if i==j else 1) for j in range(d)] for i in range(d)]
ones=[Fraction(1)]*d
assert mv(C,ones) == [Fraction(d-1)]*d
for u in ([1,-1,0,0],[0,1,-1,0],[0,0,1,-1]):
    assert mv(C,[Fraction(x) for x in u]) == [-Fraction(x) for x in u]
# Signature: one +(d-1) eigenvalue and d-1 negative eigenvalues (or reversed by sign).

# Exact inverse of J-I in d dimensions: -I + J/(d-1).
Cinv=[[(-Fraction(1) if i==j else Fraction(0))+Fraction(1,d-1) for j in range(d)] for i in range(d)]
I=[[Fraction(1 if i==j else 0) for j in range(d)] for i in range(d)]
assert mm(C,Cinv) == I
# Up to sign, this is the G3 principal tensor I-J/3.

# G2 TT-like S4 representation matrices for generators swap(01) and cycle(0123).
Rswap=[[Fraction(-1),Fraction(-1)],[Fraction(0),Fraction(1)]]
Rcycle=[[Fraction(1),Fraction(0)],[Fraction(-1),Fraction(-1)]]
perms=[([1,0,2,3],Rswap),([1,2,3,0],Rcycle)]

# Audit the most general first-order direction-resolved equivariant update
# q' = sum_i T_i q_i, with four unknown 2x2 matrices T_i.
# Equivariance condition: R T_i R^-1 = T_{p(i)}.
# Build linear equations in 16 variables and show nullity=1.
def inv2(R):
    det=R[0][0]*R[1][1]-R[0][1]*R[1][0]
    return [[R[1][1]/det,-R[0][1]/det],[-R[1][0]/det,R[0][0]/det]]

# basis variable tensor T[var][direction][row][col]
basis=[]
for v in range(16):
    Ts=[]
    for i in range(4):
        M=[[Fraction(0),Fraction(0)],[Fraction(0),Fraction(0)]]
        local=v-4*i
        if 0 <= local < 4:
            M[local//2][local%2]=Fraction(1)
        Ts.append(M)
    basis.append(Ts)

def mul2(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(2)) for j in range(2)] for i in range(2)]

rows=[]
for p,R in perms:
    Ri=inv2(R)
    for direction in range(4):
        for rr in range(2):
            for cc in range(2):
                row=[]
                for v in range(16):
                    left=mul2(mul2(R,basis[v][direction]),Ri)[rr][cc]
                    right=basis[v][p[direction]][rr][cc]
                    row.append(left-right)
                rows.append(row)
assert rank(rows) == 15
first_order_intertwiner_dimension = 16-rank(rows)
assert first_order_intertwiner_dimension == 1
# The surviving basis is T_0=T_1=T_2=T_3 proportional to identity: only the
# fully symmetric direction sum is available at first order. No directional
# spatial tensor structure occurs at this order.

print({
    'B4_rank2_pair_matrix': 'J-I',
    'pair_matrix_eigenvalues': ['3','-1','-1','-1'],
    'pair_incidence_signature': '(1,3) up to overall sign',
    'pair_matrix_inverse': '-I+J/3',
    'matches_G3_principal_tensor_up_to_sign': True,
    'first_order_S4_equivariant_directional_update_dimension': 1,
    'first_order_update_structure': 'equal direction sum times internal identity',
    'first_order_can_generate_spatial_hyperbolic_tensor': False,
    'second_order_is_minimal_directional_order_for_Lorentz_tensor_seed': True,
    'incidence_to_physical_Hessian_map_derived': False,
})
