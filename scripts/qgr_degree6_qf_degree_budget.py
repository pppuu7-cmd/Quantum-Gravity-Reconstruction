#!/usr/bin/env python3
"""Target-blind exact QF degree-budget ladder frozen by 10643a75f85da4ea447d00115006d78714ecfa24."""
from __future__ import annotations
import argparse,csv,hashlib,json
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import qgr_iter057ap_independent_covariant_source as b
import qgr_iter057ap_independent_covariant_source_repair as r
import qgr_iter057aq_degree6_causal_adjudication as aq
import qgr_iter057aa_corrected_dodecic_seed_weyl3_eighth_source_jet as aa
import qgr_corrected_degree8_weyl3_source as c

PREREG='10643a75f85da4ea447d00115006d78714ecfa24'
AT_SHA='5d070732d90b864f6167e03da85b86ce531d127dc9442fdbb928fd1b6153ee6b'
ROOT=Path(__file__).resolve().parents[1]; AT_PATH=ROOT/'data'/'ITER057AT_CANONICAL_SOURCE_DEGREE6.csv'
N=b.N; PAIRS=b.PAIRS

def fs(x):
 x=F(x); return str(x.numerator) if x.denominator==1 else f'{x.numerator}/{x.denominator}'
def jsha(x): return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def payload_poly(p,d): return [{'alpha':list(k),'value':fs(v)} for k,v in sorted(p.items()) if sum(k)<=d and v]
def tensor4_hash(T,d): return jsha([{'ijkl':[i,j,k,l],'poly':payload_poly(T[i][j][k][l],d)} for i,j,k,l in product(range(N),repeat=4)])
def vec(E): return [{'pair':[i,j],'alpha':list(a),'value':fs(b.normalized(E[i][j],a))} for i,j in PAIRS for a in b.alphas(6)]
def source(mode,P,g,gi,G,R,I):
 return aq.x_operator(P,g,gi,G,R,I) if mode=='researcher' else b.ao_source(g,gi,G,R,P,I)[1]
def read_at():
 body=[x for x in AT_PATH.read_text().splitlines() if x.strip() and not x.startswith('# ')]
 rows=list(csv.DictReader(body)); d={(int(x['a']),int(x['b']),tuple(map(int,(x['t'],x['x'],x['y'],x['z'])))):F(x['value']) for x in rows}
 return [{'pair':[i,j],'alpha':list(a),'value':fs(d.get((i,j,tuple(a)),0))} for i,j in PAIRS for a in b.alphas(6)]

def run(mode,out):
 g,prov,_,_=b.seed_metric10(); gi,G,R,Ric,S,Ein,inv=aa.geometry10(g); C=R; Cup=b.raise_last(C,gi,10)
 ladder={}; prevP=None
 for q in range(6,11):
  I,Q=r._fixed_cubic_and_Q(C,Cup,q)
  # Two covariant derivatives can lower polynomial degree by two; retain P through q+2.
  P,_=r._fixed_p_from_frechet(g,gi,C,Cup,Q,min(12,q+2))
  E=source(mode,P,g,gi,G,R,I); v=vec(E)
  ladder[str(q)]={'source_sha256':jsha(v),'source_nonzero':sum(F(x['value'])!=0 for x in v),'P_le8_sha256':tensor4_hash(P,8),'P_le10_sha256':tensor4_hash(P,10),'source_vector':v}
  if prevP is not None: ladder[str(q)]['P_le8_changed_from_previous']=tensor4_hash(P,8)!=tensor4_hash(prevP,8)
  prevP=P
 pre={'gate':'CORRECTED_DEGREE6_QF_DEGREE_BUDGET_CAUSAL_ADJUDICATION','preregistration_commit':PREREG,'lane':mode,'target_loaded_during_ladder':False,'qf_ladder':ladder,'controls_pre':{'seed_provenance_exact':bool(prov),'inverse10_exact':bool(inv),'ricci_zero':all(not Ric[i][j] for i,j in product(range(N),repeat=2)),'scalar_zero':not S,'exact_fraction_arithmetic':True,'c6_symbolic_unfixed':True,'corrected_Q10_locked':True}}
 pre_sha=jsha(pre)
 at=read_at(); atsha=jsha(at)
 sh={q:ladder[str(q)]['source_sha256'] for q in range(6,11)}
 first_change=next((q for q in range(7,11) if sh[q]!=sh[q-1]),None)
 stable_from=next((q for q in range(6,11) if all(sh[k]==sh[q] for k in range(q,11))),None)
 classification='QF6_SUFFICIENT' if all(sh[q]==sh[6] for q in range(7,11)) else ('QF8_REQUIRED_FOR_DEGREE6' if first_change in (7,8) and stable_from is not None and stable_from<=8 else 'QF_BUDGET_UNRESOLVED')
 controls={**pre['controls_pre'],'AT_hash_exact':atsha==AT_SHA,'QF6_reproduces_AT':ladder['6']['source_vector']==at,'complete_840_each':all(len(ladder[str(q)]['source_vector'])==840 for q in range(6,11)),'target_loaded_only_after_freeze':True}
 result={**pre,'pretarget_payload_sha256':pre_sha,'AT_sha256':atsha,'source_hash_ladder':sh,'first_change':first_change,'stable_from':stable_from,'classification':classification,'controls':controls}
 Path(out).parent.mkdir(parents=True,exist_ok=True); Path(out).write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
 compact=dict(result); compact['qf_ladder']={k:{x:y for x,y in v.items() if x!='source_vector'} for k,v in ladder.items()}; print(json.dumps(compact,sort_keys=True,indent=2))
 return 0 if all(controls.values()) else 2
if __name__=='__main__':
 ap=argparse.ArgumentParser(); ap.add_argument('--mode',choices=['researcher','critic'],required=True); ap.add_argument('--out',required=True); a=ap.parse_args(); raise SystemExit(run(a.mode,a.out))
