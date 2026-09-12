#!/usr/bin/env python3
import itertools,json

vertices=range(4)
edges=list(itertools.combinations(vertices,2))
edge_index={e:i for i,e in enumerate(edges)}
triples=list(itertools.combinations_with_replacement(range(len(edges)),3))
perms=list(itertools.permutations(vertices))

def map_edge(e,p):
    return tuple(sorted((p[e[0]],p[e[1]])))

def map_triple(t,p):
    return tuple(sorted(edge_index[map_edge(edges[i],p)] for i in t))

seen=set();orbits=[]
for t in triples:
    if t in seen: continue
    orb={map_triple(t,p) for p in perms}
    seen|=orb
    orbits.append((t,orb))
assert len(triples)==56
assert len(orbits)==6
representatives=[]
for t,orb in orbits:
    representatives.append({
      'edges':[list(edges[i]) for i in t],
      'orbit_size':len(orb)
    })
# The six orbit types are exact combinatorial finite-cell possibilities before matrix identities,
# Bianchi relations or continuum projection are imposed. S4 symmetry alone therefore does not
# select one cubic plane-holonomy monomial pattern.
out={
 'gate':'ITER010-G2-FINITE-CELL-CUBIC-ORBIT-AMBIGUITY',
 'plane_labels':[list(e) for e in edges],
 'degree3_multisets_before_symmetry':len(triples),
 'S4_vertex_permutation_orbits':len(orbits),
 'orbit_representatives':representatives,
 'classification':'PASS_SCOPED_S4_FINITE_CELL_SYMMETRY_ALONE_LEAVES_SIX_CUBIC_PLANE_LABEL_ORBIT_TYPES_BEFORE_CURVATURE_IDENTITIES_AND_DOES_NOT_SELECT_A_UNIQUE_WEYL_CUBED_DISCRETIZATION',
 'guard':'This orbit count is an upper-level combinatorial ambiguity census, not a claim that all six survive as independent continuum Weyl^3 scalars after Bianchi/EOM identities.'
}
print(json.dumps(out,sort_keys=True))
