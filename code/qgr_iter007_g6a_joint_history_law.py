#!/usr/bin/env python3
import argparse,json,itertools
from fractions import Fraction
P=argparse.ArgumentParser();P.add_argument('--output',required=True);a=P.parse_args()
perms=list(itertools.permutations(range(4)))
pairs=[(i,j) for i in range(4) for j in range(i+1,4)]
def s(p):
 pos={x:k for k,x in enumerate(p)}
 return tuple(1 if pos[i]<pos[j] else -1 for i,j in pairs)
S=[s(p) for p in perms]
C=[[Fraction(sum(x[i]*x[j] for x in S),24) for j in range(6)] for i in range(6)]
rev={p:tuple(reversed(p)) for p in perms}
idx={p:i for i,p in enumerate(perms)}
# Three exact joint laws with identical uniform 1/24 marginals.
laws={
 'product':[(i,j,Fraction(1,576)) for i in range(24) for j in range(24)],
 'synchronized':[(i,i,Fraction(1,24)) for i in range(24)],
 'reversed':[(i,idx[rev[p]],Fraction(1,24)) for i,p in enumerate(perms)],
}
def audit(rows):
 m1=[sum(w*S[i][u] for i,j,w in rows) for u in range(6)]
 m2=[sum(w*S[j][u] for i,j,w in rows) for u in range(6)]
 cross=[[sum(w*S[i][u]*S[j][v] for i,j,w in rows)-m1[u]*m2[v] for v in range(6)] for u in range(6)]
 summ=[[2*C[u][v]+cross[u][v]+cross[v][u] for v in range(6)] for u in range(6)]
 # marginals exactly uniform
 marg1=[sum(w for i,j,w in rows if i==k) for k in range(24)]
 marg2=[sum(w for i,j,w in rows if j==k) for k in range(24)]
 assert all(x==Fraction(1,24) for x in marg1+marg2)
 return cross,summ
res={}
for name,rows in laws.items():
 cross,summ=audit(rows)
 res[name]={
  'cross_covariance':[[str(x) for x in r] for r in cross],
  'sum_sign_variance_trace':str(sum(summ[i][i] for i in range(6))),
 }
assert res['product']['sum_sign_variance_trace']=='12'
assert res['synchronized']['sum_sign_variance_trace']=='24'
assert res['reversed']['sum_sign_variance_trace']=='0'
out={
 'lane':'JOINT_HISTORY_LAW',
 'all_three_local_marginals':'uniform 1/24 exactly',
 'sum_sign_variance_trace':{k:v['sum_sign_variance_trace'] for k,v in res.items()},
 'classification':'BLOCKED_LOCAL_1_OVER_24_HISTORY_NORMALIZATION_DOES_NOT_FIX_CROSS_CELL_CORRELATIONS',
 'scientific_interpretation':'The same exact local history law permits product accumulation, factor-two synchronized enhancement, or complete second-order cancellation under a reversed correlation. Therefore no network decoherence coefficient is authorized until the microscopic joint history law is derived. Choosing the reversed law now would be post-hoc tuning.',
 'guard':'These are countermodels for identifiability, not claims that synchronized or reversed histories are physically realized.',
 'details':res
}
open(a.output,'w').write(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,sort_keys=True))
