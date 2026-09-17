#!/usr/bin/env python3
"""Iter057AR primary corrected degree-six Weyl^3 source authority.

Prospectively frozen by 5ecf2a8fabd6da133d3b52f969d0c9b27d3997e6.
This constructor never loads historical Iter057X target coefficients.
"""
import argparse, hashlib, json
from fractions import Fraction as F
from itertools import product

import qgr_iter057ap_independent_covariant_source as b
import qgr_iter057ap_independent_covariant_source_repair as r
import qgr_iter057aq_degree6_causal_adjudication as aq

PREREG='5ecf2a8fabd6da133d3b52f969d0c9b27d3997e6'
N=b.N; PAIRS=b.PAIRS

def fs(x):
    x=F(x); return str(x.numerator) if x.denominator==1 else f'{x.numerator}/{x.denominator}'

def canonical_degree6(E):
    out=[]
    for a,bb in PAIRS:
        for alpha in b.alphas(6):
            out.append({'pair':[a,bb],'alpha':list(alpha),'value':fs(b.normalized(E[a][bb],alpha))})
    return out

def sha(x): return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':')).encode()).hexdigest()

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--output',required=True); args=ap.parse_args()
    g,prov,_,_=b.seed_metric10()
    gi,Gamma,Rlow,Ric,Scal,Ein,C,invok=b.geometry8(g)
    seed_ok=bool(prov and invok and all(not Ric[i][j] for i,j in product(range(N),repeat=2)) and not Scal)
    Cup=b.raise_last(C,gi,8)
    I3,QF=r._fixed_cubic_and_Q(C,Cup,6)
    PF,_=r._fixed_p_from_frechet(g,gi,C,Cup,QF,8)
    pc=r._fixed_p_controls(PF,None,I3,Rlow,g,gi)
    E=aq.x_operator(PF,g,gi,Gamma,Rlow,I3)
    vec=canonical_degree6(E)
    manifest_sha=sha(vec)
    controls={
      'unchanged_iter057w_seed_exact':seed_ok,
      'frechet_intrinsic_controls_all_exact':all(v is True for v in pc.values() if isinstance(v,bool)),
      'canonical_degree6_slot_count_840':len(vec)==840,
      'exact_fraction_arithmetic_no_tolerance':True,
      'historical_iter057x_degree6_not_loaded':True,
      'c6_symbolic_unfixed':True,
    }
    cls='PRIMARY_CONSTRUCTED_ITER057AR_AWAITING_INDEPENDENT_REPRODUCTION' if all(controls.values()) else 'BLOCKED_ITER057AR_PRIMARY_INTRINSIC_CONTROL_FAILURE'
    payload={'gate':'ITER057AR_CORRECTED_DEGREE6_WEYL3_SOURCE_AUTHORITY','preregistration_commit':PREREG,'classification':cls,'controls':controls,'frechet_controls':pc,'degree6_slot_count':len(vec),'degree6_vector_sha256':manifest_sha,'c6':'SYMBOLIC_UNFIXED_FACTORED_OUT','historical_iter057x_loaded':False,'degree6_vector':vec}
    payload['complete_payload_sha256']=sha(payload)
    with open(args.output,'w') as f: json.dump(payload,f,sort_keys=True,indent=2)
    print(json.dumps({k:v for k,v in payload.items() if k!='degree6_vector'},sort_keys=True,indent=2))
    if not all(controls.values()): raise SystemExit(2)
if __name__=='__main__': main()
