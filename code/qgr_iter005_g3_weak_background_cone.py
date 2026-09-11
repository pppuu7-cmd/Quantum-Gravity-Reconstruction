#!/usr/bin/env python3
from fractions import Fraction
from collections import defaultdict
import itertools

V=range(4)
FIELDS=[(i,j) for i in V for j in range(i,4)]
FINDEX={f:i for i,f in enumerate(FIELDS)}
F=Fraction


def eye(n):return [[F(int(i==j)) for j in range(n)] for i in range(n)]
def T(A):return [list(x) for x in zip(*A)]
def mm(A,B):return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
def inv(A):
    n=len(A); M=[list(A[i])+eye(n)[i] for i in range(n)]
    for c in range(n):
        p=next(r for r in range(c,n) if M[r][c]); M[c],M[p]=M[p],M[c]
        z=1/M[c][c]; M[c]=[x*z for x in M[c]]
        for r in range(n):
            if r!=c and M[r][c]:
                z=M[r][c]; M[r]=[M[r][j]-z*M[c][j] for j in range(2*n)]
    return [r[n:] for r in M]

def rank(A):
    M=[list(r) for r in A]; m=len(M); n=len(M[0]); rr=0
    for c in range(n):
        p=next((i for i in range(rr,m) if M[i][c]),None)
        if p is None:continue
        M[rr],M[p]=M[p],M[rr]
        z=1/M[rr][c]; M[rr]=[x*z for x in M[rr]]
        for i in range(m):
            if i!=rr and M[i][c]:
                z=M[i][c]; M[i]=[M[i][j]-z*M[rr][j] for j in range(n)]
        rr+=1
        if rr==m:break
    return rr

C=[[F(0 if i==j else 1) for j in V] for i in V]
E=inv(C)


def gamma_terms(mu,beta,rho):
    return [(1,mu,FINDEX[tuple(sorted((beta,rho)))]),
            (1,beta,FINDEX[tuple(sorted((mu,rho)))]),
            (-1,rho,FINDEX[tuple(sorted((mu,beta)))])]

# Exact quadratic principal Hessian of the connection density around a constant
# background with contravariant response B=G^{-1}. Overall sqrt(det G) is
# irrelevant for rank/characteristics.
def hessian(B,k):
    coeff=defaultdict(Fraction)
    for mu,nu,alpha,beta,rho,sigma in itertools.product(V,repeat=6):
        pref=B[mu][nu]*B[alpha][rho]*B[beta][sigma]
        if not pref:continue
        for overall,A1,A2 in ((1,gamma_terms(mu,beta,rho),gamma_terms(nu,alpha,sigma)),
                              (-1,gamma_terms(mu,nu,rho),gamma_terms(alpha,beta,sigma))):
            for s1,i,c in A1:
                for s2,j,d in A2:
                    coeff[(c,d,i,j)] += F(overall*s1*s2,4)*pref
    H=[[F(0) for _ in range(10)] for __ in range(10)]
    for (c,d,i,j),co in coeff.items():
        v=-co*k[i]*k[j]
        if c==d:H[c][c]+=2*v
        else:H[c][d]+=v;H[d][c]+=v
    return H

def gauge(k):
    R=[[F(0) for _ in V] for __ in range(10)]
    for a,(i,j) in enumerate(FIELDS):
        R[a][j]+=k[i];R[a][i]+=k[j]
    return R

def null_form(B,k):return sum(k[i]*B[i][j]*k[j] for i in V for j in V)
def kills(H,R):return all(sum(H[i][j]*R[j][mu] for j in range(10))==0 for i in range(10) for mu in V)
def mv(A,x):return [sum(A[i][j]*x[j] for j in range(len(x))) for i in range(len(A))]

# Nontrivial rational local-frame deformations. G_down=A^T E A and
# G_up=A^{-1} C A^{-T}; this preserves Lorentzian inertia exactly.
AS=[
    [[F(1),F(1,5),0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]],
    [[1,0,0,0],[F(1,7),1,F(1,6),0],[0,0,1,0],[0,0,0,1]],
    [[F(6,5),0,F(1,8),0],[0,F(9,10),0,F(1,9)],[0,0,1,0],[0,0,0,F(11,10)]],
]
AS=[[[F(x) for x in row] for row in A] for A in AS]
NULL_BASE=[
    [1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1],
    [1,1,1,-1],[1,2,3,F(-11,6)],[2,-1,3,F(-1,4)],
]
NONNULL_BASE=[[1,1,1,1],[1,2,3,4],[1,-1,2,5]]

rows=[]
for A in AS:
    Ai=inv(A); B=mm(mm(Ai,C),T(Ai)); AT=T(A)
    for base in NULL_BASE:
        k=mv(AT,[F(x) for x in base]); H=hessian(B,k); R=gauge(k)
        assert null_form(B,k)==0
        assert rank(R)==4 and rank(H)==4 and kills(H,R)
        assert 10-rank(H)-rank(R)==2
        rows.append(('null',rank(H),rank(R),2))
    for base in NONNULL_BASE:
        k=mv(AT,[F(x) for x in base]); H=hessian(B,k); R=gauge(k)
        assert null_form(B,k)!=0
        assert rank(R)==4 and rank(H)==6 and kills(H,R)
        rows.append(('nonnull',rank(H),rank(R),0))

print({
    'rational_backgrounds_tested':len(AS),
    'null_covectors_per_background':len(NULL_BASE),
    'nonnull_covectors_per_background':len(NONNULL_BASE),
    'all_null_H_rank':4,
    'all_nonnull_H_rank':6,
    'gauge_rank':4,
    'physical_null_modes_on_cone':2,
    'characteristic_form':'K_hbar(k)=k_i G_up^{ij} k_j',
    'classification':'PASS_SCOPED_LOCAL_WEAK_BACKGROUND_CHARACTERISTIC_STABILITY',
    'guard':'global hyperbolicity and strong-background behavior remain open',
})
