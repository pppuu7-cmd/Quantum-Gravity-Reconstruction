#!/usr/bin/env python3
"""QGR Iter014 / G12 — triadic-event identifiability audit.

Question: after G10/G11, can a minimal 3-event microscopic interface mechanism
select a unique S4-symmetric elementary-null cubic *shape*, and does it also
fix its amplitude?

We work in the homogeneous cubic monomial basis on q=(q0..q3).  Exact rational
linear algebra is used throughout.  The audit constructs the subspace obeying:
  1) S4 permutation invariance,
  2) elementary-axis nullity P(t e_i)=0,
  3) genuine triadic support: every surviving monomial touches >=2 directions,
  4) pair-locality control: monomials touching exactly 2 directions only.

The expected result is deliberately claim-locked:
  * symmetry + axis-null + pair-locality select one cubic shape,
    proportional to sum_{i!=j} q_i^2 q_j = p1*p2-p3;
  * a genuine 3-direction monomial sector adds one independent shape;
  * no homogeneous linear constraint can determine the overall real coupling.

Thus a 3-event mechanism can provide a structural carrier for nonlinearity, but
an independent microscopic amplitude/normalization law is still required.
"""
from __future__ import annotations

import argparse, itertools, json, random
from fractions import Fraction

N=4
# exponent tuples of total degree 3
MON=[e for e in itertools.product(range(4), repeat=N) if sum(e)==3]
IDX={e:i for i,e in enumerate(MON)}
PERMS=list(itertools.permutations(range(N)))

def perm_exp(e,p):
    out=[0]*N
    for i,a in enumerate(e): out[p[i]]=a
    return tuple(out)

def rank_frac(rows):
    A=[[Fraction(x) for x in r] for r in rows if any(x for x in r)]
    if not A: return 0
    m,n=len(A),len(A[0]); r=0
    for c in range(n):
        piv=next((i for i in range(r,m) if A[i][c]),None)
        if piv is None: continue
        A[r],A[piv]=A[piv],A[r]
        z=A[r][c]; A[r]=[x/z for x in A[r]]
        for i in range(m):
            if i!=r and A[i][c]:
                z=A[i][c]; A[i]=[A[i][j]-z*A[r][j] for j in range(n)]
        r+=1
        if r==m: break
    return r

def nullity(rows,n): return n-rank_frac(rows)

def symmetry_rows(active):
    pos={j:k for k,j in enumerate(active)}; rows=[]
    for p in PERMS:
        for j in active:
            k=IDX[perm_exp(MON[j],p)]
            if k not in pos: continue
            row=[0]*len(active); row[pos[j]]=1; row[pos[k]]-=1
            rows.append(row)
    return rows

def axis_rows(active):
    pos={j:k for k,j in enumerate(active)}; rows=[]
    for i in range(N):
        row=[0]*len(active)
        e=tuple(3 if j==i else 0 for j in range(N))
        if e in IDX and IDX[e] in pos: row[pos[IDX[e]]]=1
        rows.append(row)
    return rows

def support_size(e): return sum(a>0 for a in e)

def eval_poly(coeff,q):
    s=Fraction(0)
    for c,e in zip(coeff,MON):
        if not c: continue
        t=Fraction(c)
        for qi,a in zip(q,e): t*=Fraction(qi)**a
        s+=t
    return s

def pair_shape():
    # coefficients of sum_{i!=j} q_i^2 q_j
    c=[0]*len(MON)
    for i in range(N):
        for j in range(N):
            if i==j: continue
            e=[0]*N; e[i]=2; e[j]=1; c[IDX[tuple(e)]]+=1
    return c

def triple_shape():
    # coefficients of sum_{i<j<k} q_i q_j q_k
    c=[0]*len(MON)
    for comb in itertools.combinations(range(N),3):
        e=[0]*N
        for i in comb: e[i]=1
        c[IDX[tuple(e)]]+=1
    return c

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--lane',type=int,default=0); ap.add_argument('--out',default='g12.json')
    a=ap.parse_args(); rng=random.Random(910241+a.lane)

    all_active=list(range(len(MON)))
    pair_active=[j for j,e in enumerate(MON) if support_size(e)<=2]
    genuine_active=[j for j,e in enumerate(MON) if support_size(e)>=2]

    C_all=symmetry_rows(all_active)+axis_rows(all_active)
    C_pair=symmetry_rows(pair_active)+axis_rows(pair_active)
    C_genuine=symmetry_rows(genuine_active)+axis_rows(genuine_active)
    dim_all=nullity(C_all,len(all_active))
    dim_pair=nullity(C_pair,len(pair_active))
    dim_genuine=nullity(C_genuine,len(genuine_active))

    ps=pair_shape(); ts=triple_shape()
    # randomized exact permutation and elementary-null checks
    perm_err=0; axis_err=0; independent_witness=0
    for _ in range(128):
        q=[rng.randint(-5,5) for _ in range(N)]
        p=PERMS[rng.randrange(len(PERMS))]
        qp=[0]*N
        for i,x in enumerate(q): qp[p[i]]=x
        if eval_poly(ps,q)!=eval_poly(ps,qp) or eval_poly(ts,q)!=eval_poly(ts,qp): perm_err+=1
        i=rng.randrange(N); t=rng.randint(-7,7); ax=[0]*N; ax[i]=t
        if eval_poly(ps,ax)!=0 or eval_poly(ts,ax)!=0: axis_err+=1
        # witness that pair and triple shapes are not proportional
        if eval_poly(ps,q)*eval_poly(ts,[1,1,0,0]) != eval_poly(ts,q)*eval_poly(ps,[1,1,0,0]):
            independent_witness+=1

    # Amplitude identifiability: homogeneous constraints define a linear subspace;
    # if a nonzero vector is allowed, any scalar multiple is allowed. Test with exact samples.
    scale_tests=0
    for lam in [-7,-3,-1,2,5,11]:
        coeff=[lam*x for x in ps]
        ok=True
        for _ in range(32):
            q=[rng.randint(-4,4) for _ in range(N)]
            p=PERMS[rng.randrange(len(PERMS))]; qp=[0]*N
            for i,x in enumerate(q): qp[p[i]]=x
            ok &= eval_poly(coeff,q)==eval_poly(coeff,qp)
        for i in range(N):
            ax=[0]*N; ax[i]=3; ok &= eval_poly(coeff,ax)==0
        scale_tests += int(ok)

    passed=(dim_all==2 and dim_pair==1 and dim_genuine==2 and perm_err==0 and axis_err==0 and independent_witness>0 and scale_tests==6)
    result={
      'lane':a.lane,'n_monomials':len(MON),'dim_s4_axisnull_all':dim_all,
      'dim_pairlocal_s4_axisnull':dim_pair,'dim_genuine_s4_axisnull':dim_genuine,
      'permutation_failures':perm_err,'axis_null_failures':axis_err,
      'independent_witness_count':independent_witness,'amplitude_scale_tests_passed':scale_tests,
      'conclusion':'unique pair-local cubic shape, but overall coupling remains unidentifiable from homogeneous symmetry/null constraints; adding true 3-direction events adds a second shape',
      'claim_lock':'finite four-variable microscopic tensor census; not a derivation of GR or continuum quantum gravity',
      'passed':passed}
    with open(a.out,'w') as f: json.dump(result,f,indent=2,sort_keys=True)
    print(json.dumps(result,indent=2,sort_keys=True))
    raise SystemExit(0 if passed else 1)
if __name__=='__main__': main()
