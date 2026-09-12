#!/usr/bin/env python3
import argparse,itertools,json,random,cmath,math
P=argparse.ArgumentParser();P.add_argument('--output',required=True);args=P.parse_args()
# Algebraic path-groupoid test using deterministic complex unit-modulus edge factors as a compact stand-in
# for branch unitaries: ordered products along prefixes must compose exactly.
rng=random.Random(20260912)
# one edge phase for each Boolean subset S and unused direction i
edges={}
for mask in range(16):
  for i in range(4):
    if not (mask>>i)&1:
      th=rng.uniform(-math.pi,math.pi);edges[(mask,i)]=cmath.exp(1j*th)
rows=[];max_comp=0.0
for p in itertools.permutations(range(4)):
  mask=0;prod=1+0j;prefix=[1+0j]
  for i in p:
    e=edges[(mask,i)];prod=e*prod;mask|=1<<i;prefix.append(prod)
  # split after every rank and verify suffix*prefix = full product
  for r in range(5):
    mask=0
    for i in p[:r]:mask|=1<<i
    suffix=1+0j;m=mask
    for i in p[r:]:suffix=edges[(m,i)]*suffix;m|=1<<i
    err=abs(suffix*prefix[r]-prod);max_comp=max(max_comp,err)
  rows.append({'history':''.join(map(str,p)),'final_modulus':abs(prod)})
assert max_comp<1e-12
assert max(abs(r['final_modulus']-1) for r in rows)<1e-12
out={'lane':'CLOCK_CONDITIONED_EDGE_TRANSPORT_COMPOSITION','history_count':24,'max_prefix_suffix_composition_error':max_comp,'all_final_transport_moduli_unity':True,'classification':'PASS_SCOPED_INTRINSIC_RANK_CONDITIONING_IS_COMPATIBLE_WITH_EXACT_PATH_GROUPOID_TRANSPORT_COMPOSITION','scientific_interpretation':'Conditioning histories by Boolean rank does not conflict with the already-derived path-groupoid composition law. Every maximal history is the ordered product of four one-tick edge transports, and splitting/recombining at any rank gives exactly the same full transport. The compact test uses unit-modulus edge factors because the statement is composition-theoretic; the same associativity is the one already proved for the finite QGR maps/unities.','guard':'This lane tests compatibility of rank conditioning with composition, not the detailed curved 4x4 QGR transport matrices and not physical edge phases.'}
open(args.output,'w').write(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,sort_keys=True))