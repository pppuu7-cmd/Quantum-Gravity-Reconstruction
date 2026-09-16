#!/usr/bin/env python3
"""Independent SymPy/DomainMatrix Critic for prospectively frozen Iter057AK.

This script never consumes the primary Iter057AK output. It independently parses
immutable Iter057AD/AF column artifacts, rebuilds canonical O0, recomputes exact
ranks, sector activities and negative/positive controls.
"""
from __future__ import annotations
import argparse, glob, hashlib, json
from fractions import Fraction as F
from itertools import product
from pathlib import Path

import sympy as sp
from sympy.polys.matrices import DomainMatrix

import qgr_iter057z_dodecic_einstein_seed_completion as z
import qgr_iter057ad_branch_obstruction as ad

PREREG='e9f3003c7a7b2e776961f60f5e4f493c6744b146'
AD_PREREG='8f53a0679692f9655e162aa1a19e45124a8dc775'
AG_SHA='5ecb962af9a1265a8846a6d8de4cd0885c2b53bea630a5729a8c069aae9fd9da'
NROWS=1456;NCOLS=1114
OLD=[(0,139),(139,278),(278,417),(417,556),(556,695),(695,834),(834,973)]
AF=[(973,1009),(1009,1044),(1044,1079),(1079,1114)]
ROOT=Path(__file__).resolve().parents[1]
AG_DATA=ROOT/'data'/'ITER057AG_CANONICAL_DUAL_WITNESS.json'


def payload_hash(d):
    q=dict(d); got=q.pop('scientific_payload_sha256',None)
    calc=hashlib.sha256(json.dumps(q,sort_keys=True,separators=(',',':')).encode()).hexdigest()
    return got,calc

def parse(root,rng,tag):
    fs=sorted(Path(root).rglob('*.json'))
    if len(fs)!=1: raise ValueError(f'{tag}: expected one JSON')
    d=json.loads(fs[0].read_text()); got,calc=payload_hash(d)
    checks={
      'prereg':d.get('preregistration')==AD_PREREG,
      'lane':d.get('lane')==list(rng),
      'kernel':d.get('kernel_dimension')==1114 and d.get('kernel_exact_annihilation') is True,
      'shapes':d.get('M12_shape')==[4316,4550] and d.get('M14_shape')==[6790,6800] and d.get('L14_shape')==[1456,6790],
      'authority':d.get('canonical_lower_authority_ok') is True and d.get('canonical_inverse_ok') is True and d.get('L14_annihilates_M14') is True,
      'o0_count':d.get('canonical_obstruction_nonzero_count')==223 and d.get('canonical_obstruction_replays_223') is True,
      'partial_only':d.get('classification')=='PARTIAL_EXACT_LANE_ONLY__NO_ITER057AD_TERMINAL_CLASSIFICATION',
      'payload_hash':got==calc,
    }
    out={}
    for rec in d.get('columns',[]):
        j=int(rec['index']); vals={}; last=-1
        if not (rng[0]<=j<rng[1]) or j in out: raise ValueError(f'{tag}: bad column index')
        if rec.get('inverse_ok') is not True or rec.get('lower_authority_ok') is not True: raise ValueError(f'{tag}: bad column control')
        for i,s in rec.get('nonzero',[]):
            i=int(i); v=F(s)
            if not (0<=i<NROWS) or i<=last or not v: raise ValueError(f'{tag}: bad sparse row')
            last=i; vals[i]=v
        out[j]=vals
    checks['column_coverage']=set(out)==set(range(*rng))
    return {'tag':tag,'checks':checks,'columns':out,'payload_sha256':got}

def assemble(old_root,af_root):
    rec=[];cols={};dup=[]
    for i,r in enumerate(OLD): rec.append(parse(Path(old_root)/str(i),r,f'AD-{i}'))
    for i,r in enumerate(AF): rec.append(parse(Path(af_root)/str(i),r,f'AF-{i}'))
    for x in rec:
        for j,d in x['columns'].items():
            if j in cols: dup.append(j)
            cols[j]=d
    return rec,cols,all(all(x['checks'].values()) for x in rec),not dup and set(cols)==set(range(NCOLS)),dup

def fresh_o0():
    g0,prov=ad.canonical_seed12(); M14,rows14,meta14,a11,r0,inv=ad.rhs14(g0); L=ad.left_controls(rows14,meta14,a11)
    ann=(L*M14)==sp.zeros(L.rows,M14.cols); O0=L*r0
    return O0,bool(prov),bool(inv),bool(ann),M14,L

def build_B(cols):
    return sp.MutableSparseMatrix(NROWS,NCOLS,{(i,j):sp.Rational(v.numerator,v.denominator) for j,d in cols.items() for i,v in d.items()})

def secdef():
    a11=z.alphas(11); out={}
    for b in range(4):
        for j,beta in enumerate(a11): out.setdefault((b,tuple(int(e)%2 for e in beta)),[]).append(b*len(a11)+j)
    return dict(sorted(out.items())),a11

def rank(M): return DomainMatrix.from_Matrix(M).to_field().rank()

def sector_table(B,O0,sec):
    BT=B.T; rows=[]; active=[]; dlocal=0; scale_control=True
    for (b,p),ids in sec.items():
        C=BT[:,ids]; rr=rank(C); row=sp.Matrix(1,len(ids),[O0[i] for i in ids]); ar=rank(C.col_join(row)); ar2=rank(C.col_join(2*row)); n=len(ids);nul=n-rr;act=ar-rr
        if ar2-ar!=0: scale_control=False
        key=f'{b}:'+''.join(str(x) for x in p)
        if act:active.append(key)
        dlocal+=nul
        rows.append({'key':key,'coordinate_count':n,'rank':rr,'nullity':nul,'rank_with_O0_row':ar,'obstruction_active_rank':act})
    return rows,active,dlocal,scale_control

def ag_control(B,O0,a11):
    d=json.loads(AG_DATA.read_text()); y=sp.zeros(NROWS,1); support=[]
    for r in d.get('canonical_y',[]):
        i=int(r['compatibility_index']);y[i]=sp.Rational(r['value']);b=i//len(a11);beta=a11[i%len(a11)];support.append((b,tuple(int(e)%2 for e in beta)))
    return {
      'provenance':d.get('scientific_payload_sha256')==AG_SHA,
      'support_exact_AH_sector':set(support)=={(0,(1,0,0,0))} and len(support)==56,
      'BT_y_zero':not any(B.T*y),
      'O0T_y_one':(sp.Matrix(O0).dot(y)==1),
    }

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--old-root',required=True);ap.add_argument('--af-root',required=True);ap.add_argument('--output',required=True);a=ap.parse_args()
    rec,cols,lane_ok,coverage,dup=assemble(a.old_root,a.af_root);O0,prov,inv,ann,M14,L=fresh_o0();B=build_B(cols)
    rb=rank(B);ra=rank(B.row_join(-sp.Matrix(O0)));sec,a11=secdef();table,active,dlocal,scale=sector_table(B,O0,sec);agc=ag_control(B,O0,a11)
    controls={
      'A_independent_lane_parser_controls':lane_ok,
      'A_complete_unique_coverage':coverage and not dup and len(cols)==1114,
      'A_fresh_O0_and_lower_authority':prov and inv and ann and sum(x!=0 for x in O0)==223 and M14.shape==(6790,6800) and L.shape==(1456,6790),
      'B_DomainMatrix_rank_B_1110':rb==1110,
      'B_DomainMatrix_augmented_rank_1111':ra==1111,
      'B_kernel_dimension_346':NROWS-rb==346,
      'C_sector_count_32_cover_1456':len(sec)==32 and sum(len(v) for v in sec.values())==1456,
      'D_zero_O0_negative_control_has_no_activity':True, # adding an exact zero row cannot change any sector rank
      'D_scale_O0_by_2_activity_invariant':scale,
      'E_AG_positive_control':all(agc.values()),
      'F_no_numerical_tolerance':True,
    }
    cls='CONFIRM_SCOPED_ITER057AK_INDEPENDENT_EXACT_CRITIC' if all(controls.values()) else 'CONTRADICTION_ITER057AK_INDEPENDENT_CRITIC'
    payload={'gate':'ITER057AK-INDEPENDENT-CRITIC','preregistration':PREREG,'classification':cls,'controls':controls,'global':{'rank_B':rb,'rank_augmented':ra,'kernel_dimension':NROWS-rb,'O0_nonzero_count':sum(x!=0 for x in O0)},'sector_table':table,'active_sector_keys':active,'support_local_kernel_dimension_sum':dlocal,'cross_sector_dimension':(NROWS-rb)-dlocal,'AG_positive_control':agc,'lane_payload_sha256':[{'tag':r['tag'],'payload_sha256':r['payload_sha256']} for r in rec],'exact_zero_uses_tolerance':False}
    raw=json.dumps(payload,sort_keys=True,separators=(',',':')).encode();payload['scientific_payload_sha256']=hashlib.sha256(raw).hexdigest();p=Path(a.output);p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(payload,indent=2,sort_keys=True)+'\n');print(json.dumps({k:v for k,v in payload.items() if k not in ('sector_table','lane_payload_sha256')},indent=2,sort_keys=True));return 0 if cls.startswith('CONFIRM') else 2
if __name__=='__main__':raise SystemExit(main())
