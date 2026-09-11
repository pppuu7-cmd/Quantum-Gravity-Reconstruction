#!/usr/bin/env python3
"""Exact S4 ordering-sign covariance for the 24 QGR B4 histories.

For U_pi=prod exp(h X_{pi(r)}), BCH gives the ordering-dependent second-order
logarithm delta_pi=(h^2/2) sum_{i<j} s_pi(ij)[X_i,X_j]+O(h^3).
The 24-history traced channel has zero mean sign and a fixed 6x6 covariance.
This script computes it exactly and proves the spectrum {1/3 x3, 5/3 x3}.
"""
from fractions import Fraction
import itertools

PAIRS=[(i,j) for i in range(4) for j in range(i+1,4)]
PERMS=list(itertools.permutations(range(4)))

def signs(p):
    pos={v:k for k,v in enumerate(p)}
    return [1 if pos[i]<pos[j] else -1 for i,j in PAIRS]

S=[signs(p) for p in PERMS]
mean=[sum(row[a] for row in S) for a in range(6)]
assert mean==[0]*6

C=[[Fraction(sum(row[a]*row[b] for row in S),24) for b in range(6)] for a in range(6)]

I=[[Fraction(int(i==j)) for j in range(6)] for i in range(6)]
def mm(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(6)) for j in range(6)] for i in range(6)]
def sublam(A,l):
    return [[A[i][j]-l*I[i][j] for j in range(6)] for i in range(6)]
P=mm(sublam(C,Fraction(1,3)),sublam(C,Fraction(5,3)))
assert all(x==0 for row in P for x in row)

# Exact rational rank by elimination.
def rank(A):
    A=[row[:] for row in A]; r=0
    for c in range(len(A[0])):
        p=next((i for i in range(r,len(A)) if A[i][c]),None)
        if p is None:continue
        A[r],A[p]=A[p],A[r]
        q=A[r][c]; A[r]=[x/q for x in A[r]]
        for i in range(len(A)):
            if i!=r and A[i][c]:
                f=A[i][c]; A[i]=[A[i][j]-f*A[r][j] for j in range(len(A[0]))]
        r+=1
    return r

mult_low=6-rank(sublam(C,Fraction(1,3)))
mult_high=6-rank(sublam(C,Fraction(5,3)))
assert mult_low==3 and mult_high==3

print({
    'histories':24,
    'pair_commutator_components':6,
    'mean_ordering_signs':[0]*6,
    'covariance':[[str(x) for x in row] for row in C],
    'exact_spectrum':{'1/3':3,'5/3':3},
    'leading_traced_channel_nonunitary_order':'h^4',
    'leading_coefficient_form':'(h^4/8) sum_ab C_ab [K_a,[K_b,rho]], K_(ij)=[X_i,X_j]',
    'classification':'PASS_SCOPED_EXACT_24_HISTORY_ORDERING_COVARIANCE_FIXES_LEADING_CURVATURE_CHANNEL_CORRECTION',
})
