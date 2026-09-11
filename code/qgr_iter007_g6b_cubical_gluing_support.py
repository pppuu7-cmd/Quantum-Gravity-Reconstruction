#!/usr/bin/env python3
import argparse, itertools, json, math
from collections import Counter

P=argparse.ArgumentParser(); P.add_argument('--output',required=True); args=P.parse_args()
D=4
ZERO=(0,0,0,0)
SHIFT=(1,0,0,0)
PERMS=list(itertools.permutations(range(D)))

def vertices(base):
    return {tuple(base[i]+b[i] for i in range(D)) for b in itertools.product([0,1],repeat=D)}

def edges(base):
    out=set()
    for d in range(D):
        for b in itertools.product([0,1],repeat=D-1):
            x=list(base); t=0
            for j in range(D):
                if j==d: continue
                x[j]+=b[t]; t+=1
            out.add((tuple(x),d))
    return out

def plaquettes(base):
    out=set()
    for i in range(D):
        for j in range(i+1,D):
            other=[k for k in range(D) if k not in (i,j)]
            for b in itertools.product([0,1],repeat=2):
                x=list(base); x[other[0]]+=b[0]; x[other[1]]+=b[1]
                out.add((tuple(x),i,j))
    return out

def path_edges(base,p):
    x=list(base); out=[]
    for d in p:
        out.append((tuple(x),d)); x[d]+=1
    return out

VA,VB=vertices(ZERO),vertices(SHIFT)
EA,EB=edges(ZERO),edges(SHIFT)
PA,PB=plaquettes(ZERO),plaquettes(SHIFT)
assert len(VA)==16 and len(EA)==32 and len(PA)==24
assert len(VA&VB)==8
assert len(EA&EB)==12
assert len(PA&PB)==6

# A shared three-face is B3. Rank-preserving Boolean-lattice automorphisms are
# exactly permutations of its three atoms, hence 3! discrete maps. If inherited
# relational direction labels are retained, the identity label map is canonical;
# forgetting labels leaves only six symmetry-equivalent choices, not a continuum.
face_automorphisms=math.factorial(3)
assert face_automorphisms==6

Apaths=[set(path_edges(ZERO,p)) for p in PERMS]
Bpaths=[set(path_edges(SHIFT,p)) for p in PERMS]
overlap_hist=Counter(len(a&b) for a in Apaths for b in Bpaths)
assert overlap_hist==Counter({0:504,1:54,2:12,3:6}), overlap_hist
mean_shared=sum(k*v for k,v in overlap_hist.items())/(24*24)
assert abs(mean_shared-1/6)<1e-15

# Face counts f_r(B_n)=2^(n-r) C(n,r); record both cell and shared face.
def fvector(n):
    return [2**(n-r)*math.comb(n,r) for r in range(n+1)]
assert fvector(4)==[16,32,24,8,1]
assert fvector(3)==[8,12,6,1]

out={
  'lane':'CUBICAL_FACE_GLUING_AND_SUPPORT',
  'B4_fvector_vertices_to_cells':fvector(4),
  'shared_B3_fvector_vertices_to_3faces':fvector(3),
  'face_adjacent_shared_vertices':len(VA&VB),
  'face_adjacent_shared_edges':len(EA&EB),
  'face_adjacent_shared_plaquettes':len(PA&PB),
  'rank_preserving_B3_face_automorphisms':face_automorphisms,
  'local_history_pair_shared_edge_histogram':{str(k):v for k,v in sorted(overlap_hist.items())},
  'mean_shared_edges_per_uniform_local_history_pair':mean_shared,
  'classification':'PASS_SCOPED_MINIMAL_INCIDENCE_PRESERVING_B4_FACE_GLUING_HAS_SHARED_B3_SUPPORT_AND_ONLY_DISCRETE_S3_RELABELING_FREEDOM',
  'scientific_interpretation':'In the minimal direction-labelled cubical completion of the B4 seed, two face-neighbour cells identify one full B3 face: 8 vertices, 12 oriented edges and 6 plaquettes. The abstract face gluing has only the six S3 atom relabelings; retaining inherited direction labels picks the identity representative. Adjacent cell operator supports therefore overlap substantially and cannot be assumed tensor-factor independent.',
  'guard':'This is the minimal incidence-preserving two-cell completion of direction-labelled B4 cells. It does not prove that the full global CCRC complex is uniquely a Z4 hypercubic lattice or that overlapping Hilbert algebras tensor-factor.'
}
open(args.output,'w').write(json.dumps(out,indent=2,sort_keys=True)+'\n')
print(json.dumps(out,sort_keys=True))
