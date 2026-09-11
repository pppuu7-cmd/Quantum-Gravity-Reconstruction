#!/usr/bin/env python3
import argparse, itertools, json, math

P=argparse.ArgumentParser(); P.add_argument('--output',required=True); args=P.parse_args()
D=4
k=0
PERMS=list(itertools.permutations(range(D)))

def path_edges(base,seq):
    x=list(base); out=[]
    for d in seq:
        out.append((tuple(x),d)); x[d]+=1
    return out

A=[path_edges((0,0,0,0),p) for p in PERMS]
baseB=[0,0,0,0]; baseB[k]=1
B=[path_edges(tuple(baseB),p) for p in PERMS]
# The union region of two face-neighbour B4 cubes along direction k is the
# 2x1x1x1 box. A maximal monotone path uses k twice and each other direction once.
global_seqs=sorted(set(itertools.permutations([0,0,1,2,3])))
assert len(global_seqs)==math.factorial(5)//math.factorial(2)==60
global_edges={s:set(path_edges((0,0,0,0),s)) for s in global_seqs}

compatible=[]
for ia,ea in enumerate(A):
    for ib,eb in enumerate(B):
        union=set(ea)|set(eb)
        if len(union)!=5: continue
        matches=[s for s,eg in global_edges.items() if eg==union]
        if matches:
            assert len(matches)==1
            compatible.append((ia,ib,matches[0]))
assert len(compatible)==6
compatible_global={x[2] for x in compatible}
assert len(compatible_global)==6
# They are precisely the global paths whose repeated overlap direction is first and last.
assert all(s[0]==k and s[-1]==k for s in compatible_global)
assert sum(1 for s in global_seqs if s[0]==k and s[-1]==k)==6

out={
  'lane':'OVERLAPPING_RECTANGULAR_GLOBAL_PATH_CENSUS',
  'two_face_adjacent_local_history_pairs':24*24,
  'global_monotone_histories_in_2x1x1x1_union':len(global_seqs),
  'local_history_pairs_whose_edge_union_is_one_global_monotone_path':len(compatible),
  'fraction_of_global_paths_representable_as_two_complete_overlapping_cell_diagonals':len(compatible_global)/len(global_seqs),
  'compatible_global_path_characterization':'repeated overlap direction appears first and last; middle three directions are arbitrary',
  'classification':'PASS_SCOPED_GLOBAL_PATHS_ON_A_FACE_OVERLAP_REGION_DO_NOT_FACTOR_INTO_TWO_INDEPENDENT_B4_DIAGONAL_HISTORY_REGISTERS',
  'scientific_interpretation':'The natural 2x1x1x1 union has only 60 monotone global paths, not 24^2=576 independent local diagonal pairs. Only 6 global paths (10%) can be written as the union of two complete overlapping-cell diagonal histories, namely those that enter the shared face immediately, traverse its three directions, and leave in the repeated direction last.',
  'consequence':'A face-overlap field region requires a global path/local-algebra description; assigning one independent 24-history channel to each overlapping cell overcounts the global path alternatives.',
  'guard':'This is an exact combinatorial statement for the minimal cubical two-cell completion. It does not itself choose the quantum amplitude measure for arbitrary larger regions.'
}
open(args.output,'w').write(json.dumps(out,indent=2,sort_keys=True)+'\n')
print(json.dumps(out,sort_keys=True))
