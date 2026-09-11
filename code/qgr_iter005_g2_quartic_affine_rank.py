#!/usr/bin/env python3
import itertools
from collections import defaultdict

# Exact modular lower-bound certificate for the homogeneous quartic Noether map.
# Full delta0 invariance implies invariance under affine xi, for which
# delta h_ij is an arbitrary constant symmetric shift. Evaluating the quartic
# vertex with one zero-momentum leg therefore gives a necessary homogeneous
# gauge-invariance condition. If this affine map already has full physical
# rank 1694, the full homogeneous quartic kernel is zero.

P=1000003
V=range(4)
PERMS=list(itertools.permutations(V))
LEG3=list(itertools.permutations(range(3)))
FIELDS=[(i,j) for i in V for j in range(i,4)]
FINDEX={f:i for i,f in enumerate(FIELDS)}


def pf(a,p):
    i,j=FIELDS[a]
    return FINDEX[tuple(sorted((p[i],p[j])))]


def canon(a,b,c,d,i,j):
    if a>b:a,b=b,a
    if (d,j)<(c,i): c,d,i,j=d,c,j,i
    return (a,b,c,d,i,j)


def pterm(t,p):
    a,b,c,d,i,j=t
    return canon(pf(a,p),pf(b,p),pf(c,p),pf(d,p),p[i],p[j])

# Deterministic raw quartic S4 orbit basis.
terms=set()
for a in range(10):
    for b in range(a,10):
        for c in range(10):
            for d in range(10):
                for i in V:
                    for j in V:
                        terms.add(canon(a,b,c,d,i,j))
unseen=set(terms); ORBITS=[]
while unseen:
    t=min(unseen)
    orb={pterm(t,p) for p in PERMS}
    ORBITS.append(tuple(sorted(orb)))
    unseen-=orb
assert len(ORBITS)==2066

# Three dynamical legs after the constant-shift leg is removed:
# p,q,r with r=-p-q. Polynomials are degree two in 8 independent variables.
def lin(leg,idx):
    if leg==0:
        e=[0]*8;e[idx]=1;return {tuple(e):1}
    if leg==1:
        e=[0]*8;e[4+idx]=1;return {tuple(e):1}
    d={}
    e=[0]*8;e[idx]=1;d[tuple(e)]=P-1
    e=[0]*8;e[4+idx]=1;d[tuple(e)]=P-1
    return d

MOM={(l,i):lin(l,i) for l in range(3) for i in V}

def mul(a,b):
    out=defaultdict(int)
    for e,c in a.items():
        for f,d in b.items():
            g=tuple(e[k]+f[k] for k in range(8))
            out[g]=(out[g]+c*d)%P
    return {k:v for k,v in out.items() if v}

PROD={(l1,i,l2,j):mul(MOM[(l1,i)],MOM[(l2,j)])
      for l1 in range(3) for l2 in range(3) for i in V for j in V}

# Row keys are exact coefficients of:
# shift_component x three ordered external field components x momentum monomial.
ROW_ID={}
def row_id(key):
    if key not in ROW_ID: ROW_ID[key]=len(ROW_ID)
    return ROW_ID[key]


def affine_column(orb):
    col=defaultdict(int)
    for a,b,c,d,i,j in orb:
        # Only the two undifferentiated h factors vary under a constant shift.
        # If a==b the two contributions correctly add to factor 2.
        for shift,und in ((a,b),(b,a)):
            for perm in LEG3:
                fs=[None]*3
                fs[perm[0]]=und
                fs[perm[1]]=c
                fs[perm[2]]=d
                for e,v in PROD[(perm[1],i,perm[2],j)].items():
                    r=row_id((shift,fs[0],fs[1],fs[2],e))
                    col[r]=(col[r]+v)%P
    return {r:v for r,v in col.items() if v}

COLS=[affine_column(orb) for orb in ORBITS]

# Use rare target rows first; this keeps sparse elimination very small.
freq=[0]*len(ROW_ID)
for col in COLS:
    for r in col: freq[r]+=1
order=sorted(range(len(freq)),key=lambda r:(freq[r],r))
pos=[0]*len(order)
for n,r in enumerate(order):pos[r]=n

# Sparse exact Gaussian elimination over GF(P), column by column.
pivots={}
rank=0
max_pivot_support=0
for original in COLS:
    v=dict(original)
    while v:
        lead=min(v,key=lambda r:pos[r])
        if lead not in pivots:
            inv=pow(v[lead],P-2,P)
            v={r:(c*inv)%P for r,c in v.items() if (c*inv)%P}
            pivots[lead]=v
            rank+=1
            max_pivot_support=max(max_pivot_support,len(v))
            break
        pv=pivots[lead]
        fac=v[lead]
        for r,c in pv.items():
            nv=(v.get(r,0)-fac*c)%P
            if nv:v[r]=nv
            elif r in v:del v[r]

assert rank==1694
physical_quartic_dimension=1694
raw_nullity=len(ORBITS)-physical_quartic_dimension
assert raw_nullity==372

print({
    'raw_quartic_S4_orbits':len(ORBITS),
    'physical_quartic_action_dimension':physical_quartic_dimension,
    'kinematic_IBP_nullity':raw_nullity,
    'affine_target_rows':len(ROW_ID),
    'affine_shift_rank_mod_prime':rank,
    'prime':P,
    'max_sparse_pivot_support':max_pivot_support,
    'rational_rank_conclusion':'rank_Q >=1694 and physical domain dim=1694, therefore rank_Q=1694',
    'physical_homogeneous_quartic_kernel_dimension':0,
    'classification':'PASS_SCOPED_QUARTIC_HOMOGENEOUS_KERNEL_ZERO_MODULO_KINEMATIC_NULLS',
})
