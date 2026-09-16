#!/usr/bin/env python3
"""Fast exact discriminator for the already-preregistered Iter057AK sector hypothesis.

Not a terminal authority: it intentionally skips the expensive full-kernel rank/S3
work and independently computes only the prospectively frozen sector ranks and
fresh canonical O0 activity from immutable Iter057AD/AF column artifacts.
"""
from __future__ import annotations
import argparse, hashlib, json
from fractions import Fraction as F
from pathlib import Path
from flint import fmpq, fmpq_mat
import qgr_iter057z_dodecic_einstein_seed_completion as z
import qgr_iter057ag_dual_obstruction_witness as ag

PREREG='e9f3003c7a7b2e776961f60f5e4f493c6744b146'
NROWS=1456;NCOLS=1114

def fq(x):
    if not isinstance(x,F): x=F(str(x))
    return fmpq(x.numerator,x.denominator)

def sectors():
    a11=z.alphas(11); out={}
    for b in range(4):
        for j,beta in enumerate(a11):
            out.setdefault((b,tuple(e%2 for e in beta)),[]).append(b*len(a11)+j)
    return dict(sorted(out.items()))

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--old-root',required=True);ap.add_argument('--af-root',required=True);ap.add_argument('--output',required=True);a=ap.parse_args()
    recs,cols,lane_ok,coverage,dup=ag.assemble(Path(a.old_root),Path(a.af_root))
    M14,rows14,L,r0,O0,prov,inv,ann=ag.canonical_object()
    byrow={i:{} for i in range(NROWS)}
    for j,d in cols.items():
        for i,v in d.items():byrow[i][j]=v
    table=[];active=[];dlocal=0
    for (b,p),ids in sectors().items():
        M=fmpq_mat(NCOLS,len(ids));Q=fmpq_mat(NCOLS+1,len(ids))
        for k,i in enumerate(ids):
            for j,v in byrow[i].items():x=fq(v);M[j,k]=x;Q[j,k]=x
            Q[NCOLS,k]=fq(O0[i])
        r=int(M.rank());ar=int(Q.rank());nul=len(ids)-r;act=ar-r;key=f'{b}:'+''.join(map(str,p))
        dlocal+=nul
        if act:active.append(key)
        table.append({'key':key,'coordinate_count':len(ids),'rank':r,'nullity':nul,'rank_with_O0_row':ar,'obstruction_active_rank':act})
    authority=lane_ok and coverage and not dup and prov and inv and ann and sum(x!=0 for x in O0)==223
    ah=[x for x in table if x['key']=='0:1000'][0]
    unique=(active==['0:1000'] and ah['nullity']==1 and ah['obstruction_active_rank']==1)
    payload={'gate':'ITER057AK-FAST-SECTOR-DISCRIMINATOR','preregistration':PREREG,'authority_controls_ok':authority,'sector_table':table,'support_local_kernel_dimension_sum':dlocal,'cross_sector_dimension_using_frozen_AF_kernel_dim':346-dlocal,'active_sector_keys':active,'unique_AH_channel_hypothesis':unique,'classification':'DIAGNOSTIC_SUPPORTS_FROZEN_PASS_HYPOTHESIS' if authority and unique else ('DIAGNOSTIC_FALSIFIES_FROZEN_PASS_HYPOTHESIS' if authority else 'DIAGNOSTIC_AUTHORITY_FAILURE'),'exact_zero_uses_tolerance':False}
    raw=json.dumps(payload,sort_keys=True,separators=(',',':')).encode();payload['scientific_payload_sha256']=hashlib.sha256(raw).hexdigest();p=Path(a.output);p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(payload,indent=2,sort_keys=True)+'\n');print(json.dumps(payload,indent=2,sort_keys=True));return 0 if authority else 2
if __name__=='__main__':raise SystemExit(main())
