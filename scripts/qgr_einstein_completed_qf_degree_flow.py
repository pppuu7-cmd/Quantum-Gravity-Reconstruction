#!/usr/bin/env python3
"""Exact target-blind adjudication frozen by 8a5e1e9186d8b8b81f401158b8ca04b38f05de66."""
import argparse,csv,hashlib,json
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import qgr_iter057ap_independent_covariant_source as b
import qgr_iter057ap_independent_covariant_source_repair as r
import qgr_iter057aa_corrected_dodecic_seed_weyl3_eighth_source_jet as aa
PREREG='8a5e1e9186d8b8b81f401158b8ca04b38f05de66'; AT_SHA='5d070732d90b864f6167e03da85b86ce531d127dc9442fdbb928fd1b6153ee6b'
ROOT=Path(__file__).resolve().parents[1]; AT=ROOT/'data'/'ITER057AT_CANONICAL_SOURCE_DEGREE6.csv'; N=b.N; PAIRS=b.PAIRS

def fs(x):
 x=F(x); return str(x.numerator) if x.denominator==1 else f'{x.numerator}/{x.denominator}'
def sha(x): return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def vec(T): return [{'pair':[i,j],'alpha':list(a),'value':fs(b.normalized(T[i][j],a))} for i,j in PAIRS for a in b.alphas(6)]
def mat0(): return b.pmat()
def lower(E,g,deg=6):
 O=mat0()
 for a,c in product(range(N),repeat=2):
  v={}
  for i,j in product(range(N),repeat=2): v=b.add(v,b.mul(b.mul(g[a][i],g[c][j],deg),E[i][j],deg))
  O[a][c]=b.trunc(v,deg)
 return O
def degree_profile(T,maxd):
 counts={str(d):0 for d in range(maxd+1)}; rows=[]
 def addpoly(tag,p):
  for a,v in sorted(p.items()):
   d=sum(a)
   if d<=maxd and v: counts[str(d)]+=1; rows.append([tag,list(a),fs(v)])
 # tensors here are nested 2/3/4 arrays
 def walk(x,idx=()):
  if isinstance(x,dict): addpoly(list(idx),x)
  else:
   for k,y in enumerate(x): walk(y,idx+(k,))
 walk(T); return {'counts':counts,'hash':sha(rows),'rows':rows}
def build_terms(P,g,gi,G,R,I):
 # zero-derivative algebraic P.R
 def bone(a,bb):
  v={}
  for c,d,e,f in product(range(N),repeat=4): v=b.add(v,b.mul(b.mul(P[a][c][d][e],gi[bb][f],6),R[f][c][d][e],6))
  return b.trunc(v,6)
 B=mat0()
 for a,bb in product(range(N),repeat=2): B[a][bb]=b.scale(b.add(bone(a,bb),bone(bb,a)),F(1,2))
 # one-derivative stage
 FD=[[[{} for _ in range(N)] for _ in range(N)] for _ in range(N)]
 for m,bb,n in product(range(N),repeat=3):
  v={}
  for a in range(N):
   t=b.deriv(P[a][m][bb][n],a)
   for rr in range(N):
    t=b.add(t,b.mul(G[a][a][rr],P[rr][m][bb][n],7)); t=b.add(t,b.mul(G[m][a][rr],P[a][rr][bb][n],7)); t=b.add(t,b.mul(G[bb][a][rr],P[a][m][rr][n],7)); t=b.add(t,b.mul(G[n][a][rr],P[a][m][bb][rr],7))
   v=b.add(v,t)
  FD[m][bb][n]=b.trunc(v,7)
 # two-derivative stage
 D=mat0()
 for m,n in product(range(N),repeat=2):
  v={}
  for bb in range(N):
   t=b.deriv(FD[m][bb][n],bb)
   for rr in range(N):
    t=b.add(t,b.mul(G[m][bb][rr],FD[rr][bb][n],6)); t=b.add(t,b.mul(G[bb][bb][rr],FD[m][rr][n],6)); t=b.add(t,b.mul(G[n][bb][rr],FD[m][bb][rr],6))
   v=b.add(v,t)
  D[m][n]=b.trunc(v,6)
 metric=mat0()
 for a,bb in product(range(N),repeat=2): metric[a][bb]=b.scale(b.mul(gi[a][bb],I,6),F(1,2))
 alg=mat0(); div=mat0()
 for a,bb in product(range(N),repeat=2): alg[a][bb]=b.neg(B[a][bb]); div[a][bb]=b.scale(D[a][bb],-2)
 terms_up={'algebraic_PR':alg,'double_divergence':div,'metric_I3':metric}
 terms_down={k:lower(v,g) for k,v in terms_up.items()}
 total=mat0()
 for a,bb in product(range(N),repeat=2): total[a][bb]=b.trunc(b.add(b.add(terms_down['algebraic_PR'][a][bb],terms_down['double_divergence'][a][bb]),terms_down['metric_I3'][a][bb]),6)
 # isolate nontrivial metric lowering relative to background eta lowering
 eta=[[{(0,0,0,0):F(b.ETA[i])} if i==j and b.ETA[i] else {} for j in range(N)] for i in range(N)]
 upsum=mat0()
 for a,bb in product(range(N),repeat=2): upsum[a][bb]=b.add(b.add(alg[a][bb],div[a][bb]),metric[a][bb])
 eta_down=lower(upsum,eta); ild=mat0()
 for a,bb in product(range(N),repeat=2): ild[a][bb]=b.sub(total[a][bb],eta_down[a][bb])
 return total,terms_down,FD,D,ild

def read_at():
 body=[x for x in AT.read_text().splitlines() if x.strip() and not x.startswith('# ')]
 rows=list(csv.DictReader(body)); d={(int(x['a']),int(x['b']),tuple(map(int,(x['t'],x['x'],x['y'],x['z'])))):F(x['value']) for x in rows}
 return [{'pair':[i,j],'alpha':list(a),'value':fs(d.get((i,j,tuple(a)),0))} for i,j in PAIRS for a in b.alphas(6)]
def run(mode,out):
 g,prov,rows,meta=aa.seed_metric12(); gi,G,R,Ric,S,Ein,inv=aa.geometry10(g)
 seed={'r12_provenance_exact':bool(prov),'r12_rows_469':len(rows)==469,'inverse10_exact':bool(inv),'ricci10_zero':all(not Ric[i][j] for i,j in product(range(N),repeat=2)),'scalar10_zero':not S,'einstein10_zero':all(not Ein[i][j] for i,j in product(range(N),repeat=2))}
 if not all(seed.values()):
  result={'gate':'CORRECTED_DEGREE6_EINSTEIN_COMPLETED_QF_DEGREE_FLOW_ADJUDICATION','lane':mode,'preregistration':PREREG,'seed_controls':seed,'classification':'UNRESOLVED_EINSTEIN_COMPLETED_QF_DEGREE_FLOW','target_loaded':False}; Path(out).write_text(json.dumps(result,sort_keys=True,indent=2)+'\n'); print(json.dumps(result)); return 2
 C=R; Cup=b.raise_last(C,gi,10); ladder={}
 for q in range(6,11):
  I,Q=r._fixed_cubic_and_Q(C,Cup,q); P,_=r._fixed_p_from_frechet(g,gi,C,Cup,Q,min(12,q+2)); E,terms,FD,D,ild=build_terms(P,g,gi,G,R,I); v=vec(E)
  ladder[str(q)]={'source_sha256':sha(v),'source_nonzero':sum(F(x['value'])!=0 for x in v),'term_sha256':{k:sha(vec(t)) for k,t in terms.items()}|{'index_lowering':sha(vec(ild))},'degree_flow':{'P':degree_profile(P,10),'one_covariant_derivative':degree_profile(FD,7),'two_covariant_derivatives':degree_profile(D,6)},'source_vector':v}
 # serialize/freeze target-blind evidence hash before target read
 pre={'gate':'CORRECTED_DEGREE6_EINSTEIN_COMPLETED_QF_DEGREE_FLOW_ADJUDICATION','lane':mode,'preregistration':PREREG,'seed_controls':seed,'target_loaded_during_ladder':False,'ladder':ladder,'c6':'SYMBOLIC_UNFIXED','corrected_Q10_locked':True}; pre_sha=sha(pre)
 av=read_at(); ash=sha(av); hs=[ladder[str(q)]['source_sha256'] for q in range(6,11)]; first=next((q for q in range(7,11) if hs[q-6]!=hs[q-7]),None)
 stable=next((q for q in range(6,11) if len(set(hs[q-6:]))==1),None); witness_complete=all(set(ladder[str(q)]['term_sha256'])=={'algebraic_PR','double_divergence','metric_I3','index_lowering'} for q in range(6,11))
 if len(set(hs))==1: cls='QF6_SUFFICIENT_ON_EINSTEIN_COMPLETED_SEED'
 elif first==8 and stable==8 and witness_complete: cls='QF8_REQUIRED_ON_EINSTEIN_COMPLETED_SEED'
 elif stable is not None and witness_complete: cls='OTHER_QF_THRESHOLD_ON_EINSTEIN_COMPLETED_SEED'
 else: cls='UNRESOLVED_EINSTEIN_COMPLETED_QF_DEGREE_FLOW'
 controls={**seed,'AT_hash_exact':ash==AT_SHA,'complete_840_each':all(len(ladder[str(q)]['source_vector'])==840 for q in range(6,11)),'target_loaded_only_after_freeze':True,'term_witnesses_complete':witness_complete,'exact_fraction_arithmetic':True}
 result={**pre,'pretarget_payload_sha256':pre_sha,'AT_sha256':ash,'QF6_matches_historical_AT':ladder['6']['source_vector']==av,'first_change':first,'stable_from':stable,'classification':cls,'controls':controls}
 Path(out).parent.mkdir(parents=True,exist_ok=True); Path(out).write_text(json.dumps(result,sort_keys=True,indent=2)+'\n'); compact=dict(result); compact['ladder']={q:{k:v for k,v in z.items() if k!='source_vector'} for q,z in ladder.items()}; print(json.dumps(compact,sort_keys=True,indent=2)); return 0 if all(controls.values()) else 2
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--mode',choices=['researcher','critic'],required=True);p.add_argument('--out',required=True);a=p.parse_args();raise SystemExit(run(a.mode,a.out))
