#!/usr/bin/env python3
"""Finite regular boundary-disintegration audit for two face-overlapping B4 regions.

The purpose is deliberately narrower than proving conditional independence.  It verifies the
exact coordinate fiber-product support and records the correct measure-theoretic conclusion:
a positive regular physical measure can be disintegrated over the shared B3 pushforward even
when the two exclusive sides remain conditionally correlated.
"""
from fractions import Fraction as F
import argparse,itertools,json
P=argparse.ArgumentParser();P.add_argument('--output',required=True);args=P.parse_args()
D=4

def vertices(base):
 return {tuple(base[i]+bit[i] for i in range(D)) for bit in itertools.product([0,1],repeat=D)}
def edges(base):
 vs=vertices(base);out=set()
 for v in vs:
  for d in range(D):
   w=list(v);w[d]+=1;w=tuple(w)
   if w in vs:out.add((v,w,d))
 return out
A0=(0,0,0,0);B0=(1,0,0,0)
VA,VB=vertices(A0),vertices(B0);EA,EB=edges(A0),edges(B0)
VF=VA&VB;EF=EA&EB;VU=VA|VB;EU=EA|EB
assert (len(VA),len(EA),len(VF),len(EF),len(VU),len(EU))==(16,32,8,12,24,52)

def variables(V,E):
 f={('h',v,a) for v in V for a in range(10)}
 c={('conn',e,m) for e in E for m in range(6)}
 return f|c
XA,XB,XF,XU=variables(VA,EA),variables(VB,EB),variables(VF,EF),variables(VU,EU)
assert len(XA)==len(XB)==352 and len(XF)==152 and len(XU)==552
assert XA&XB==XF and XA|XB==XU
assert len(XA)+len(XB)-len(XF)==len(XU)

# Exact finite correlated witness for disintegration without conditional factorization.
# a and c denote exclusive-side coarse labels, b the shared-boundary label.
raw={}
for a,b,c in itertools.product([0,1],repeat=3):
 raw[(a,b,c)]=F(1+a+2*b+3*c+2*a*c+b*a,1)
Z=sum(raw.values());p={x:w/Z for x,w in raw.items()}
nu={b:sum(w for (a,bb,c),w in p.items() if bb==b) for b in [0,1]}
cond={(a,b,c):p[(a,b,c)]/nu[b] for a,b,c in itertools.product([0,1],repeat=3)}
# reconstruction p(a,b,c)=nu(b)p(a,c|b)
assert all(nu[b]*cond[(a,b,c)]==p[(a,b,c)] for a,b,c in itertools.product([0,1],repeat=3))
# Show that disintegration does not imply product conditional independence.
viol=[]
for b in [0,1]:
 pa={a:sum(cond[(a,b,c)] for c in [0,1]) for a in [0,1]}
 pc={c:sum(cond[(a,b,c)] for a in [0,1]) for c in [0,1]}
 for a,c in itertools.product([0,1],repeat=2):
  if cond[(a,b,c)]!=pa[a]*pc[c]:viol.append((a,b,c))
assert viol

out={
 'lane':'BOUNDARY_MEASURE_DISINTEGRATION',
 'B4_vertices':16,'B4_edges':32,'shared_B3_vertices':8,'shared_B3_edges':12,
 'union_vertices':24,'union_edges':52,'B4_configuration_dim':352,'shared_B3_configuration_dim':152,'union_configuration_dim':552,
 'fiber_product_dimension_identity':'352+352-152=552','exact_variable_set_intersection_is_shared_B3':True,
 'finite_correlated_disintegration_reconstructs_exactly':True,'conditional_factorization_counterexample_count':len(viol),
 'classification':'PASS_SCOPED_REGULAR_FINITE_POSITIVE_MEASURE_DISINTEGRATION_OVER_SHARED_B3__CONDITIONAL_INDEPENDENCE_NOT_REQUIRED_OR_DERIVED',
 'scientific_interpretation':'On the finite regular path-groupoid configuration domain the union variables are exactly one copy of A-exclusive data, one copy of the shared B3 data, and one copy of B-exclusive data. Any positive sigma-finite regular physical density on this finite-dimensional stratum therefore admits the standard pushforward/conditional disintegration over the shared-boundary restriction map. The boundary measure is the pushforward of the same physical measure, not a new adjustable weight. Conditional factorization of the two exclusive sides does not follow and is explicitly not assumed.',
 'quantum_gluing_consequence':'The positive Hilbert measure may be organized as a direct integral over shared-boundary labels. Interaction/action phases and derivative constraints can remain inside each conditional fiber; no product history law for overlapping cells is inferred.',
 'guard':'This is a regular-stratum disintegration/existence result. It does not prove global control of singular gauge strata, nor conditional independence, nor a factorized interacting path-integral amplitude.'
}
open(args.output,'w').write(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,sort_keys=True))
