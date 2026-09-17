#!/usr/bin/env python3
"""Iter057AP separate no-refit comparator.

This comparator is created only after the target-blind AO-restricted 2100-slot
constructor payload was frozen at commit fe0ba26567155622780a29d3969de1e125cbf2d3.
It does not modify the constructor or the prospectively frozen convention map.
"""
import argparse, csv, hashlib, json
from fractions import Fraction as F
from itertools import product
from pathlib import Path

PREREG='6de62a559381a7c86e01c58a62ea7d8c91606884'
FROZEN_CONSTRUCTOR_COMMIT='fe0ba26567155622780a29d3969de1e125cbf2d3'
FROZEN_CONSTRUCTOR_SHA='9fb92dce4d8a0153be4eb0044460c17fe120bbfe83a66e860a284a3d7acbc61b'
PASS='PASS_SCOPED_ITER057AP_INDEPENDENT_COVARIANT_AO_RESTRICTION_REPRODUCES_TERMINAL_WEYL3_SOURCE_THROUGH_DEGREE_SIX_NO_REFIT'
FAIL='SCIENTIFIC_FAIL_ITER057AP_COVARIANT_AO_RESTRICTION_DISAGREES_WITH_TERMINAL_WEYL3_SOURCE_AFTER_FROZEN_CONVENTION_MAP'
INVALID='INVALID_ITER057AP_OBJECT_MISMATCH_TARGET_LEAKAGE_POSTHOC_SIGN_SCALE_OR_EXACTNESS_FAILURE'
ROOT=Path(__file__).resolve().parents[1]
U=ROOT/'data'/'ITER057U_CANONICAL_SOURCE_0_2_4.json'
X=ROOT/'data'/'ITER057X_CANONICAL_SOURCE_DEGREE6.csv'
PAIRS=[(0,0),(0,1),(0,2),(0,3),(1,1),(1,2),(1,3),(2,2),(2,3),(3,3)]

def alphas(n):
    return sorted(a for a in product(range(n+1), repeat=4) if sum(a)==n)

def phash(d):
    return hashlib.sha256(json.dumps(d,sort_keys=True,separators=(',',':')).encode()).hexdigest()

def verify_constructor(d):
    got=d.get('complete_payload_sha256')
    q=dict(d); q.pop('complete_payload_sha256',None)
    calc=phash(q)
    return (got==calc==FROZEN_CONSTRUCTOR_SHA and
            d.get('preregistration')==PREREG and
            d.get('classification')=='CONSTRUCTOR_EXACT_FROZEN__NO_TARGET_COMPARISON_YET' and
            d.get('slot_count')==2100 and
            d.get('controls',{}).get('I_target_source_coefficients_not_loaded') is True and
            all(d.get('controls',{}).values()))

def target_map():
    out={}
    ud=json.loads(U.read_text())
    for r in ud['Shat_normalized_sparse']:
        key=(tuple(r['pair']),tuple(r['alpha']))
        if key in out: raise ValueError('duplicate U key')
        if int(r['degree']) not in (0,2,4): raise ValueError('unexpected U degree')
        out[key]=F(r['value'])
    lines=X.read_text().splitlines()
    body=[z for z in lines if z.strip() and not z.startswith('#')]
    for r in csv.DictReader(body):
        key=((int(r['a']),int(r['b'])),(int(r['t']),int(r['x']),int(r['y']),int(r['z'])))
        if key in out: raise ValueError('duplicate X/U key')
        if sum(key[1])!=6: raise ValueError('unexpected X degree')
        out[key]=F(r['value'])
    return out

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--constructor',required=True); ap.add_argument('--output',required=True); a=ap.parse_args()
    d=json.loads(Path(a.constructor).read_text())
    constructor_ok=verify_constructor(d)
    tm=target_map()
    slots=d['source_slots']
    seen=set(); mism=[]; bydeg={str(k):0 for k in range(7)}; sign_opposite=True; nonzero_compared=0
    for r in slots:
        key=(tuple(r['pair']),tuple(r['alpha']))
        if key in seen: raise ValueError('duplicate constructor slot')
        seen.add(key)
        av=F(r['value']); tv=tm.get(key,F(0)); deg=int(r['degree'])
        if av!=tv:
            bydeg[str(deg)]+=1
            mism.append({'pair':list(key[0]),'alpha':list(key[1]),'degree':deg,'AO_value':str(av),'target_value':str(tv),'delta':str(av-tv)})
        if av or tv:
            nonzero_compared+=1
            if av!=-tv: sign_opposite=False
    expected={(p,a) for n in range(7) for p in PAIRS for a in alphas(n)}
    complete=(seen==expected and len(seen)==2100)
    target_nonzero=len(tm)
    mismatch_count=len(mism)
    controls={
      'A_frozen_constructor_hash_and_controls_exact':constructor_ok,
      'B_complete_2100_slot_basis_exact':complete,
      'C_target_authorities_have_expected_230_nonzero_records':target_nonzero==230,
      'D_no_posthoc_sign_or_scale_applied':True,
      'E_exact_fraction_comparison_no_tolerance':True,
      'F_c6_remains_symbolic_unfixed':d.get('c6_status')=='SYMBOLIC_UNFIXED_FACTORED_OUT'
    }
    if not all(controls.values()): cls=INVALID
    elif mismatch_count==0: cls=PASS
    else: cls=FAIL
    payload={'gate':'ITER057AP-COVARIANT-TO-WEYL3-SOURCE-NO-REFIT-MATCH','preregistration':PREREG,'frozen_constructor_commit':FROZEN_CONSTRUCTOR_COMMIT,'frozen_constructor_payload_sha256':FROZEN_CONSTRUCTOR_SHA,'classification':cls,'controls':controls,'slot_count':2100,'target_nonzero_count':target_nonzero,'mismatch_count':mismatch_count,'mismatch_count_by_degree':bydeg,'all_nonzero_slots_are_exact_global_sign_opposites':bool(sign_opposite and nonzero_compared>0),'nonzero_union_count':nonzero_compared,'mismatches':mism,'exact_zero_uses_tolerance':False,'posthoc_sign_flip_applied':False,'c6_status':'SYMBOLIC_UNFIXED'}
    q=dict(payload); q.pop('mismatches'); payload['scientific_summary_sha256']=phash(q); payload['complete_payload_sha256']=phash(payload)
    p=Path(a.output); p.parent.mkdir(parents=True,exist_ok=True); p.write_text(json.dumps(payload,sort_keys=True,indent=2)+'\n')
    print(json.dumps({k:v for k,v in payload.items() if k!='mismatches'},sort_keys=True,indent=2))
    return 0 if cls==PASS else (3 if cls==FAIL else 2)

if __name__=='__main__': raise SystemExit(main())
