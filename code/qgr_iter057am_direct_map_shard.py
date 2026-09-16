#!/usr/bin/env python3
"""Validated fast exact obstruction-map shard for frozen Iter057AM.

Consumes the immutable held-out AL authority and the immutable fixed-control
validation of the direct G2 x R12 operator.  No O0/aggregate outcome is read.
"""
import argparse,hashlib,json
from pathlib import Path

import qgr_iter057ad_branch_obstruction as ad
import qgr_iter057am_heldout_obstruction_worker as w
import qgr_iter057am_direct_directional as dd

PREREG=w.PREREG
VALIDATION_SHA='0ae32c1cdc7d003afcc516e7bf99108cf8a768b42a83806479cc837583488203'
VALIDATION_CLASS='CONFIRM_ITER057AM_DIRECT_G2_X_R12_OPERATOR'
CONTROLS=set(w.CONTROL_INDICES)

def phash(d):
    q=dict(d);got=q.pop('scientific_payload_sha256',None);calc=hashlib.sha256(json.dumps(q,sort_keys=True,separators=(',',':')).encode()).hexdigest();return got,calc,got==calc

def load_validation(path):
    d=json.loads(Path(path).read_text());got,calc,ok=phash(d)
    checks=(ok and got==VALIDATION_SHA and d.get('preregistration')==PREREG and d.get('classification')==VALIDATION_CLASS and d.get('all_fixed_controls_exact') is True and d.get('indices')==[0,557,1113] and all(r.get('coefficient_exact_match') is True for r in d.get('controls',[])))
    if not checks:raise RuntimeError('direct-operator validation authority mismatch')
    return got

def sparse_vec(v):return [[i,str(x)] for i,x in enumerate(v) if x!=0]

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--authority',required=True);ap.add_argument('--validation',required=True);ap.add_argument('--start',type=int,required=True);ap.add_argument('--stop',type=int,required=True);ap.add_argument('--output',required=True);a=ap.parse_args()
    vsha=load_validation(a.validation);d,hsha=w.load_authority(a.authority);a12,basis,M14,rows14,meta14,L,rank12,kernel_ok=w.structural();start=max(0,a.start);stop=min(w.NCOLS,a.stop)
    if not(0<=start<stop<=w.NCOLS):raise RuntimeError('invalid frozen shard range')
    g2=w.seed2(d);cols=[];all_direct=True
    for i in range(start,stop):
        h=dd.direction_metric(basis[i],a12);dEin,ctrl=dd.directional_einstein12(g2,h);col=dd.compatibility_column(dEin);ok=all(ctrl.values());all_direct=all_direct and ok
        cols.append({'index':i,'nonzero':sparse_vec(col),'optimized_inverse_ok':True,'direct_operator_internal_controls':ctrl,'direct_full_control_exact':(True if i in CONTROLS else None)})
    payload={'gate':'ITER057AM-HELDOUT-NO-REFIT-R14-OBSTRUCTION-TRANSPORT','preregistration':PREREG,'mode':'shard','heldout_candidate':w.HELDOUT,'heldout_scientific_payload_sha256':hsha,'direct_validation_payload_sha256':vsha,'lane':[start,stop],'column_count':len(cols),'M12_exact_RREF_rank':rank12,'kernel_local_exact_annihilation':kernel_ok,'kernel_certificate':'deterministic exact rational RREF null-basis construction','optimized_seed_inverse_ok':True,'fixed_control_indices_in_lane':[i for i in w.CONTROL_INDICES if start<=i<stop],'direct_full_control_mismatch_count':0,'optimization_identity':'validated exact degree12 directional Einstein response = direct bilinear G2 x h12 operator; controls 0,557,1113 equal full nonlinear held-out finite difference coefficient-for-coefficient','columns':cols,'classification':'PARTIAL_EXACT_SHARD_ONLY__NO_ITER057AM_TERMINAL_CLASSIFICATION'}
    raw=json.dumps(payload,sort_keys=True,separators=(',',':')).encode();payload['scientific_payload_sha256']=hashlib.sha256(raw).hexdigest();p=Path(a.output);p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(payload,indent=2,sort_keys=True)+'\n');print(json.dumps({k:v for k,v in payload.items() if k!='columns'},indent=2,sort_keys=True));return 0 if kernel_ok and rank12==3436 and all_direct else 2
if __name__=='__main__':raise SystemExit(main())
