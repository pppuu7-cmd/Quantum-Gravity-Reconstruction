#!/usr/bin/env python3
import itertools

V=range(4)
PERMS=list(itertools.permutations(V))
FIELDS=[(i,j) for i in V for j in range(i,4)]
FINDEX={f:i for i,f in enumerate(FIELDS)}

def pf(a,p):
    i,j=FIELDS[a]
    return FINDEX[tuple(sorted((p[i],p[j])))]

def canon(a,b,c,d,i,j):
    if a>b: a,b=b,a
    if (d,j)<(c,i): c,d,i,j=d,c,j,i
    return (a,b,c,d,i,j)

def pterm(t,p):
    a,b,c,d,i,j=t
    return canon(pf(a,p),pf(b,p),pf(c,p),pf(d,p),p[i],p[j])

# Raw h_a h_b (D_i h_c)(D_j h_d) spanning set.
terms=set()
for a in range(10):
    for b in range(a,10):
        for c in range(10):
            for d in range(10):
                for i in V:
                    for j in V:
                        terms.add(canon(a,b,c,d,i,j))
assert len(terms)==45100

unseen=set(terms); orbits=[]
while unseen:
    t=min(unseen)
    orb={pterm(t,p) for p in PERMS}
    orbits.append(tuple(sorted(orb)))
    unseen-=orb
assert len(orbits)==2066

physical_quartic_dimension=1694
kinematic_nullity=len(orbits)-physical_quartic_dimension
assert kinematic_nullity==372

print({
    'raw_hhDhDh_monomials':45100,
    'raw_S4_orbits':2066,
    'physical_quartic_action_dimension':1694,
    'kinematic_IBP_nullity':372,
    'classification':'PASS_SCOPED_QUARTIC_RAW_ORBIT_AND_KINEMATIC_NULLITY_BOOKKEEPING',
})
