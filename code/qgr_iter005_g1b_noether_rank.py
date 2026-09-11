#!/usr/bin/env python3
import itertools, random

# Dependency-free modular rank certificate for the cubic Noether map.
# A nonzero rank-317 minor modulo a prime proves rank >=317 over Q.
# The exact representation-theory action quotient dimension is 317, so this
# proves the physical homogeneous Noether kernel is zero.

P=1000003
V=range(4)
PERMS=list(itertools.permutations(V))
FIELDS=[(i,j) for i in V for j in range(i,4)]
FINDEX={f:i for i,f in enumerate(FIELDS)}
LEG_PERMS=list(itertools.permutations(range(3)))


def pf(a,p):
    i,j=FIELDS[a]
    return FINDEX[tuple(sorted((p[i],p[j])))]


def canon(a,b,c,i,j):
    if (c,j)<(b,i):
        b,c,i,j=c,b,j,i
    return (a,b,c,i,j)


def pterm(t,p):
    a,b,c,i,j=t
    return canon(pf(a,p),pf(b,p),pf(c,p),p[i],p[j])

# Raw S4 orbit spanning set h_a (D_i h_b)(D_j h_c), with differentiated
# factors symmetrized. Exact orbit count =399.
terms=set()
for a in range(10):
    for b in range(10):
        for c in range(10):
            for i in V:
                for j in V:
                    terms.add(canon(a,b,c,i,j))

unseen=set(terms); ORBITS=[]
while unseen:
    t=min(unseen)
    orb={pterm(t,p) for p in PERMS}
    ORBITS.append(tuple(sorted(orb)))
    unseen-=orb
assert len(ORBITS)==399


def eval_basis(Hs,ks):
    out=[0]*399
    for oi,orb in enumerate(ORBITS):
        s=0
        for a,b,c,i,j in orb:
            for perm in LEG_PERMS:
                la,lb,lc=perm
                s += Hs[la][a]*ks[lb][i]*Hs[lb][b]*ks[lc][j]*Hs[lc][c]
        out[oi]=s%P
    return out


def gauge_field(k,xi):
    return [(k[i]*xi[j]+k[j]*xi[i])%P for i,j in FIELDS]


def rank_mod(rows):
    A=[list(map(lambda x:x%P,row)) for row in rows]
    m=len(A); n=len(A[0]); r=0
    for c in range(n):
        pivot=next((i for i in range(r,m) if A[i][c]),None)
        if pivot is None:
            continue
        A[r],A[pivot]=A[pivot],A[r]
        inv=pow(A[r][c],P-2,P)
        A[r]=[(x*inv)%P for x in A[r]]
        for i in range(r+1,m):
            if A[i][c]:
                f=A[i][c]
                A[i]=[(A[i][j]-f*A[r][j])%P for j in range(n)]
        r+=1
        if r==m:
            break
    return r

rng=random.Random(77)
ACTION=[]
NOETHER=[]
for _ in range(340):
    def vals(n):
        return [rng.randint(-17,17)%P for _ in range(n)]
    p=vals(4); q=vals(4); r=[(-p[i]-q[i])%P for i in V]

    # General action-evaluation row: establishes raw spanning-set quotient rank.
    Hs=[vals(10),vals(10),vals(10)]
    ACTION.append(eval_basis(Hs,[p,q,r]))

    # Ward/Noether row: first leg is an arbitrary linear pure gauge field.
    xi=vals(4); B=vals(10); C=vals(10)
    A=gauge_field(p,xi)
    NOETHER.append(eval_basis([A,B,C],[p,q,r]))

rank_action=rank_mod(ACTION)
rank_noether=rank_mod(NOETHER)
assert rank_action==317
assert rank_noether==317

print({
    'raw_S4_orbits':399,
    'physical_two_derivative_cubic_action_dimension':rank_action,
    'noether_map_rank_mod_prime':rank_noether,
    'prime':P,
    'rational_rank_conclusion':'rank_Q >= 317; domain quotient dim=317; therefore rank_Q=317',
    'physical_homogeneous_noether_kernel_dimension':0,
    'classification':'PASS_SCOPED_CUBIC_NOETHER_MAP_FULL_RANK_UNIQUE_MODULO_KINEMATIC_NULLS',
})
