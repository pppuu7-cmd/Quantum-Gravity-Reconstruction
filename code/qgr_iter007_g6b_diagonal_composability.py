#!/usr/bin/env python3
import argparse, itertools, json, math

P=argparse.ArgumentParser(); P.add_argument('--output',required=True); args=P.parse_args()
D=4
one=(1,1,1,1)
base=(0,0,0,0)

def add(a,b): return tuple(x+y for x,y in zip(a,b))

def cell_vertices(n):
    return {tuple(n[i]+b[i] for i in range(D)) for b in itertools.product([0,1],repeat=D)}

def cell_edges(n):
    out=set()
    for d in range(D):
        for b in itertools.product([0,1],repeat=D-1):
            x=list(n); t=0
            for j in range(D):
                if j==d: continue
                x[j]+=b[t]; t+=1
            out.add((tuple(x),d))
    return out

def cell_plaquettes(n):
    out=set()
    for i in range(D):
        for j in range(i+1,D):
            other=[k for k in range(D) if k not in (i,j)]
            for b in itertools.product([0,1],repeat=2):
                x=list(n); x[other[0]]+=b[0]; x[other[1]]+=b[1]
                out.add((tuple(x),i,j))
    return out

A_V,A_E,A_P=cell_vertices(base),cell_edges(base),cell_plaquettes(base)
classes={}
serial=[]
for delta in itertools.product([0,1],repeat=D):
    if delta==(0,0,0,0): continue
    w=sum(delta)
    B_V,B_E,B_P=cell_vertices(delta),cell_edges(delta),cell_plaquettes(delta)
    source_B=delta
    target_A=one
    composable=(source_B==target_A)
    rec={
      'shift':delta,
      'hamming_weight':w,
      'intersection_dimension':D-w,
      'shared_vertices':len(A_V&B_V),
      'shared_edges':len(A_E&B_E),
      'shared_plaquettes':len(A_P&B_P),
      'diagonal_morphisms_composable':composable,
    }
    classes.setdefault(str(w),[]).append(rec)
    if composable: serial.append(rec)

assert {int(k):len(v) for k,v in classes.items()}=={1:4,2:6,3:4,4:1}
assert len(serial)==1 and tuple(serial[0]['shift'])==one
# Face-neighbour cells are weight-1 shifts: shared B3 but diagonal endpoints do not match.
for rec in classes['1']:
    assert rec['intersection_dimension']==3
    assert rec['shared_vertices']==8 and rec['shared_edges']==12 and rec['shared_plaquettes']==6
    assert rec['diagonal_morphisms_composable'] is False
# The only serially composable diagonal neighbour is shifted by (1,1,1,1): cells share one vertex only.
s=serial[0]
assert s['shared_vertices']==1 and s['shared_edges']==0 and s['shared_plaquettes']==0

out={
  'lane':'DIAGONAL_PATH_GROUPOID_COMPOSABILITY',
  'shift_class_multiplicities':{k:len(v) for k,v in sorted(classes.items())},
  'face_adjacent_shift_weight':1,
  'face_adjacent_diagonal_composable':False,
  'unique_serial_diagonal_shift':list(one),
  'serial_diagonal_shared_support':{'vertices':1,'edges':0,'plaquettes':0},
  'classification':'PASS_SCOPED_FACE_ADJACENT_B4_HISTORY_INSTRUMENTS_ARE_NOT_SERIAL_PATH_GROUPOID_MORPHISMS__ONLY_OPPOSITE_VERTEX_TOUCHING_DIAGONALS_COMPOSE',
  'scientific_interpretation':'A one-cell history instrument transports between the two opposite vertices of its B4 cell. Two cells sharing a B3 face have different diagonal sources/targets, so their diagonal history morphisms are not composable. The only translated unit cell whose diagonal starts at the first diagonal target is shifted by (1,1,1,1); the two cells then share only that endpoint and no fine edges or plaquettes.',
  'consequence':'Sequentially applying one history channel for every face-adjacent four-cell to the same carrier is not authorized by the already-derived path-groupoid law. Such adjacent cells belong to an overlapping local-algebra problem, not to serial path evolution.',
  'guard':'This statement concerns the existing B4 opposite-vertex history instrument. It does not rule out a future multi-cell field observable or local-net construction on face-overlapping cells.'
}
open(args.output,'w').write(json.dumps(out,indent=2,sort_keys=True)+'\n')
print(json.dumps(out,sort_keys=True))
