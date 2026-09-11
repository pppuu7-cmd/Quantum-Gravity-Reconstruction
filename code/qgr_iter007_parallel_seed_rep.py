#!/usr/bin/env python3
import argparse, json, itertools
from fractions import Fraction
import qgr_iter006_g2c_seed_physical_hilbert as seed

P=argparse.ArgumentParser(); P.add_argument('--output',required=True); args=P.parse_args()
V=range(4); PERMS=list(itertools.permutations(V)); FIELDS=seed.FIELDS

# Exact physical representatives at each null cover: ker H intersect Euclidean orthogonal complement of im R.
def transpose(A): return [list(r) for r in zip(*A)]
def matvec(A,v): return [sum(A[i][j]*v[j] for j in range(len(v))) for i in range(len(A))]
def stack(A,B): return [list(r) for r in A]+[list(r) for r in B]

def phys_basis(i):
    k=[0,0,0,0]; k[i]=1
    A=stack(seed.H(k),transpose(seed.R(k)))
    q=seed.nullspace(A,10)
    assert len(q)==2
    return q

Q=[phys_basis(i) for i in V]

def cycle_type(p):
    seen=set(); ls=[]
    for i in V:
        if i in seen: continue
        j=i;n=0
        while j not in seen:
            seen.add(j);n+=1;j=p[j]
        ls.append(n)
    return tuple(sorted(ls,reverse=True))

def det2(a,b,c,d): return a*d-b*c

def coords2(basis,v):
    # basis is list of two 10-vectors. Pick an invertible two-row minor.
    for r in range(10):
        for s in range(r+1,10):
            a,b=basis[0][r],basis[1][r]; c,d=basis[0][s],basis[1][s]
            D=det2(a,b,c,d)
            if D:
                x=(v[r]*d-b*v[s])/D
                y=(a*v[s]-v[r]*c)/D
                assert all(x*basis[0][t]+y*basis[1][t]==v[t] for t in range(10))
                return x,y
    raise RuntimeError('degenerate basis')

# Character of the 8D direct sum of the four two-dimensional physical cover fibers.
char_sets={}
for p in PERMS:
    T=seed.perm_field_matrix(p)
    tr=Fraction(0)
    for i in V:
        if p[i]!=i: continue
        for a in range(2):
            v=matvec(T,Q[i][a])
            x,y=coords2(Q[i],v)
            tr += x if a==0 else y
    char_sets.setdefault(cycle_type(p),set()).add(tr)
assert all(len(v)==1 for v in char_sets.values())

# Standard class order: e, transposition, double transposition, 3-cycle, 4-cycle.
order=[(1,1,1,1),(2,1,1),(2,2),(3,1),(4,)]
char8=[next(iter(char_sets[c])) for c in order]
assert char8==[8,0,0,-1,0], char8

sizes=[1,6,3,8,6]
irreps={
 '1':[1,1,1,1,1],
 '3':[3,1,-1,0,-1],
 '2':[2,0,2,-1,0],
 '3prime':[3,-1,-1,0,1],
 'sign':[1,-1,1,1,-1],
}
def inner(chi,psi): return sum(Fraction(s)*a*b for s,a,b in zip(sizes,chi,psi))/24
mult8={name:int(inner(char8,ch)) for name,ch in irreps.items()}
assert mult8=={'1':0,'3':1,'2':1,'3prime':1,'sign':0}

# Signed two-form / ordered-pair representation carried by ordering commutators.
PAIRS=[(i,j) for i in V for j in range(i+1,4)]; PI={x:i for i,x in enumerate(PAIRS)}
def signed_pair_trace(p):
    tr=0
    for a,(i,j) in enumerate(PAIRS):
        x,y=p[i],p[j]
        pair=(x,y) if x<y else (y,x); sign=1 if x<y else -1
        if PI[pair]==a: tr+=sign
    return tr
pair_sets={}
for p in PERMS: pair_sets.setdefault(cycle_type(p),set()).add(signed_pair_trace(p))
char6=[next(iter(pair_sets[c])) for c in order]
assert char6==[6,0,-2,0,0]
mult6={name:int(inner(char6,ch)) for name,ch in irreps.items()}
assert mult6=={'1':0,'3':1,'2':0,'3prime':1,'sign':0}

# Exact ordering covariance; its two eigenspaces are the two 3D irreps.
def signs(p):
    pos={v:k for k,v in enumerate(p)}
    return [1 if pos[i]<pos[j] else -1 for i,j in PAIRS]
S=[signs(p) for p in PERMS]
C=[[Fraction(sum(r[a]*r[b] for r in S),24) for b in range(6)] for a in range(6)]
# Spectral projectors: low=(5I-3C)/4, high=(3C-I)/4.
def signed_pair_matrix(p):
    M=[[Fraction(0) for _ in range(6)] for __ in range(6)]
    for a,(i,j) in enumerate(PAIRS):
        x,y=p[i],p[j]; pair=(x,y) if x<y else (y,x); sign=1 if x<y else -1
        M[PI[pair]][a]=sign
    return M
def trace_product(A,B): return sum(sum(A[i][j]*B[j][i] for j in range(len(A))) for i in range(len(A)))
I=[[Fraction(int(i==j)) for j in range(6)] for i in range(6)]
Plo=[[Fraction(5*I[i][j]-3*C[i][j],4) for j in range(6)] for i in range(6)]
Phi=[[Fraction(3*C[i][j]-I[i][j],4) for j in range(6)] for i in range(6)]
clo=[];chi=[]
for ct in order:
    p=next(p for p in PERMS if cycle_type(p)==ct); Rp=signed_pair_matrix(p)
    clo.append(trace_product(Plo,Rp)); chi.append(trace_product(Phi,Rp))
assert clo==irreps['3prime']
assert chi==irreps['3']

# End(E2)=1 + sign + E2, so no linear S4-equivariant map from 3+3' ordering labels to operators on isolated E2 alone.
charE=irreps['2']; charEnd=[x*x for x in charE]
hom_order_to_EndE=sum(int(inner(char6,ch))*int(inner(charEnd,ch)) for ch in irreps.values())
# More directly decompose EndE.
multEnd={name:int(inner(charEnd,ch)) for name,ch in irreps.items()}
assert multEnd=={'1':1,'3':0,'2':1,'3prime':0,'sign':1}
assert hom_order_to_EndE==0

out={
 'lane':'SEED_PHYSICAL_REPRESENTATION',
 'physical_8d_character':[str(x) for x in char8],
 'physical_8d_decomposition':'2 + 3 + 3prime',
 'ordering_commutator_character':[str(x) for x in char6],
 'ordering_commutator_decomposition':'3 + 3prime',
 'covariance_eigenvalue_1_over_3_irrep':'3prime',
 'covariance_eigenvalue_5_over_3_irrep':'3',
 'End_E2_decomposition':'1 + sign + 2',
 'linear_equivariant_maps_ordering6_to_EndE2':0,
 'classification':'PASS_SCOPED_PHYSICAL_SEED_8D_EQUALS_2_PLUS_3_PLUS_3PRIME_AND_ORDERING_NOISE_LIVES_IN_3_PLUS_3PRIME',
 'scientific_interpretation':'The full four-cover physical seed space contains both ordering-noise irreps plus the 2D polarization irrep. An isolated two-mode E sector cannot receive a linear S4-equivariant operator directly from the six ordering labels; a concrete purity readout must specify directional/fiber transport or a quadratic contraction.',
 'guard':'This is an exact symmetric-seed representation theorem, not yet a curved-background two-mode transfer matrix.'
}
open(args.output,'w').write(json.dumps(out,indent=2,sort_keys=True)+'\n')
print(json.dumps(out,sort_keys=True))
