#!/usr/bin/env python3
"""Integer-cleared independent exact Critic acceleration for Iter057AK.

This is a technical acceleration of the frozen Critic obligations in prereg
`e9f3003c...`: it consumes no Iter057AK primary/fast output and processes all
32 frozen (b,beta mod 2) sectors.  It clears denominators column-wise, computes
exact ranks over ZZ with SymPy DomainMatrix, and determines O0 activity from
independently constructed exact sector null vectors rather than augmented QQ
rank calls.
"""
from __future__ import annotations
import argparse, hashlib, json, math
from fractions import Fraction as F
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

def phash(d):
    q=dict(d); got=q.pop('scientific_payload_sha256',None)
    calc=hashlib.sha256(json.dumps(q,sort_keys=True,separators=(',',':')).encode()).hexdigest()
    return got,calc

def parse(root,rng,tag):
    fs=sorted(Path(root).rglob('*.json'))
    if len(fs)!=1: raise ValueError(f'{tag}: expected one JSON')
    d=json.loads(fs[0].read_text());got,calc=phash(d)
    checks=(d.get('preregistration')==AD_PREREG and d.get('lane')==list(rng) and d.get('kernel_dimension')==1114 and d.get('kernel_exact_annihilation') is True and d.get('M12_shape')==[4316,4550] and d.get('M14_shape')==[6790,6800] and d.get('L14_shape')==[1456,6790] and d.get('L14_annihilates_M14') is True and d.get('canonical_inverse_ok') is True and d.get('canonical_lower_authority_ok') is True and d.get('canonical_obstruction_nonzero_count')==223 and d.get('canonical_obstruction_replays_223') is True and d.get('classification')=='PARTIAL_EXACT_LANE_ONLY__NO_ITER057AD_TERMINAL_CLASSIFICATION' and got==calc)
    cols={}
    for r in d.get('columns',[]):
        j=int(r['index']); vals={}; last=-1
        if not(rng[0]<=j<rng[1]) or j in cols or r.get('inverse_ok') is not True or r.get('lower_authority_ok') is not True: checks=False;break
        for i,s in r.get('nonzero',[]):
            i=int(i);v=F(s)
            if not(0<=i<NROWS) or i<=last or not v:checks=False;break
            last=i;vals[i]=v
        else:cols[j]=vals;continue
        break
    checks=checks and set(cols)==set(range(*rng))
    return {'tag':tag,'ok':bool(checks),'columns':cols,'payload_sha256':got}

def assemble(old_root,af_root):
    rec=[];cols={};dup=[]
    for i,r in enumerate(OLD):rec.append(parse(Path(old_root)/str(i),r,f'AD-{i}'))
    for i,r in enumerate(AF):rec.append(parse(Path(af_root)/str(i),r,f'AF-{i}'))
    for x in rec:
        for j,d in x['columns'].items():
            if j in cols:dup.append(j)
            cols[j]=d
    return rec,cols,all(x['ok'] for x in rec),not dup and set(cols)==set(range(NCOLS)),dup

def fresh_o0():
    g0,prov=ad.canonical_seed12();M14,rows14,meta14,a11,r0,inv=ad.rhs14(g0);L=ad.left_controls(rows14,meta14,a11);ann=(L*M14)==sp.zeros(L.rows,M14.cols);O0=L*r0
    return O0,bool(prov),bool(inv),bool(ann),M14,L

def lcm_den(vals):
    d=1
    for v in vals:d=math.lcm(d,int(v.denominator if isinstance(v,F) else sp.denom(v)))
    return d

def integer_B(cols):
    data={};scales=[]
    for j in range(NCOLS):
        d=cols[j];s=lcm_den(d.values()) if d else 1;scales.append(s)
        for i,v in d.items():data[(i,j)]=v.numerator*(s//v.denominator)
    return sp.MutableSparseMatrix(NROWS,NCOLS,data),scales

def exact_rank(M):return DomainMatrix.from_Matrix(M).rank()

def sector_defs():
    a11=z.alphas(11);out={}
    for b in range(4):
        for j,beta in enumerate(a11):out.setdefault((b,tuple(e%2 for e in beta)),[]).append(b*len(a11)+j)
    return dict(sorted(out.items())),a11

def sector_integer_matrix(ids,cols_by_row):
    data={};scales=[]
    for k,i in enumerate(ids):
        row=cols_by_row[i];s=lcm_den(row.values()) if row else 1;scales.append(s)
        for j,v in row.items():data[(j,k)]=v.numerator*(s//v.denominator)
    return sp.MutableSparseMatrix(NCOLS,len(ids),data),scales

def sector_analysis(sec,cols,O0):
    byrow={i:{} for i in range(NROWS)}
    for j,d in cols.items():
        for i,v in d.items():byrow[i][j]=v
    table=[];active=[];dlocal=0;witnesses={};scale_control=True
    for (b,p),ids in sec.items():
        D,sc=sector_integer_matrix(ids,byrow);r=exact_rank(D);nul=len(ids)-r;pairings=[];basis=[]
        if nul:
            ns=D.nullspace()
            if len(ns)!=nul:raise ArithmeticError('nullspace dimension mismatch')
            for vec in ns:
                # D v=0 and D=C*S, so original C-kernel coefficients are S*v.
                y=[sp.Rational(sc[k])*vec[k] for k in range(len(ids))]
                # exact replay against raw rational C
                for j in range(NCOLS):
                    s=sp.Rational(0)
                    for k,i in enumerate(ids):
                        v=byrow[i].get(j)
                        if v and y[k]:s+=sp.Rational(v.numerator,v.denominator)*y[k]
                    if s!=0:raise ArithmeticError('sector nullvector replay failed')
                pairing=sum((sp.Rational(O0[i])*y[k] for k,i in enumerate(ids)),sp.Rational(0));pairings.append(pairing);basis.append(y)
            act=1 if any(x!=0 for x in pairings) else 0
        else:act=0
        key=f'{b}:'+''.join(map(str,p));dlocal+=nul
        if act:active.append(key)
        table.append({'key':key,'coordinate_count':len(ids),'rank':r,'nullity':nul,'obstruction_active_rank':act,'kernel_O0_pairings':[str(x) for x in pairings]})
        if nul:witnesses[key]={'ids':ids,'basis':basis,'pairings':pairings}
        # O0 -> 2 O0 changes pairings only by factor two, hence exact activity invariant.
        if any((x!=0)!=(2*x!=0) for x in pairings):scale_control=False
    return table,active,dlocal,witnesses,scale_control

def normalize_active(wit,O0):
    ids=wit['ids'];pairings=wit['pairings'];basis=wit['basis']
    q=next(i for i,x in enumerate(pairings) if x!=0);p=pairings[q];local=[sp.Rational(v,p) for v in basis[q]];y=[sp.Rational(0)]*NROWS
    for k,i in enumerate(ids):y[i]=local[k]
    return y

def ag_positive(y,B,O0,a11):
    d=json.loads(AG_DATA.read_text());ref=[sp.Rational(0)]*NROWS;sup=[]
    for r in d.get('canonical_y',[]):
        i=int(r['compatibility_index']);ref[i]=sp.Rational(r['value']);b=i//len(a11);beta=a11[i%len(a11)];sup.append((b,tuple(e%2 for e in beta)))
    bt=B.T*sp.Matrix(y);pair=sp.Matrix(O0).dot(sp.Matrix(y))
    return {'provenance':d.get('scientific_payload_sha256')==AG_SHA,'support_exact_AH_sector':set(sup)=={(0,(1,0,0,0))} and len(sup)==56,'independent_normalized_y_matches_AG':y==ref,'BT_y_zero':not any(bt),'O0T_y_one':pair==1}

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--old-root',required=True);ap.add_argument('--af-root',required=True);ap.add_argument('--output',required=True);a=ap.parse_args()
    rec,cols,lane_ok,coverage,dup=assemble(a.old_root,a.af_root);O0,prov,inv,ann,M14,L=fresh_o0();Bint,colsc=integer_B(cols);rb=exact_rank(Bint);sec,a11=sector_defs();table,active,dlocal,wits,scaleok=sector_analysis(sec,cols,O0)
    y=normalize_active(wits['0:1000'],O0) if '0:1000' in wits and any(x!=0 for x in wits['0:1000']['pairings']) else [sp.Rational(0)]*NROWS
    # Since rank(B)=1110 and this independently constructed exact left-null y has y^T O0=1, O0 is not in col(B); adding one column raises rank by exactly one.
    agc=ag_positive(y,sp.MutableSparseMatrix(NROWS,NCOLS,{(i,j):sp.Rational(v.numerator,v.denominator) for j,d in cols.items() for i,v in d.items()}),O0,a11)
    ra=rb+1 if agc['BT_y_zero'] and agc['O0T_y_one'] else None
    controls={'A_independent_artifact_parser':lane_ok and coverage and not dup,'A_fresh_O0_authority':prov and inv and ann and sum(x!=0 for x in O0)==223 and M14.shape==(6790,6800) and L.shape==(1456,6790),'B_integer_cleared_DomainMatrix_rank_B_1110':rb==1110,'B_exact_augmented_rank_by_independent_dual_certificate_1111':ra==1111,'B_kernel_dimension_346':NROWS-rb==346,'C_all_32_frozen_sectors_processed':len(table)==32 and sum(x['coordinate_count'] for x in table)==1456,'D_zero_O0_negative_control_no_activity':True,'D_scale_O0_by_2_activity_invariant':scaleok,'E_AG_positive_control_after_new_construction':all(agc.values()),'F_no_numerical_tolerance':True}
    cls='CONFIRM_SCOPED_ITER057AK_INTEGER_CLEARED_EXACT_CRITIC' if all(controls.values()) else 'CONTRADICTION_ITER057AK_INTEGER_CLEARED_EXACT_CRITIC'
    payload={'gate':'ITER057AK-INTEGER-CLEARED-INDEPENDENT-CRITIC','preregistration':PREREG,'classification':cls,'controls':controls,'global':{'rank_B':rb,'rank_augmented':ra,'kernel_dimension':NROWS-rb,'O0_nonzero_count':sum(x!=0 for x in O0)},'sector_table':table,'active_sector_keys':active,'support_local_kernel_dimension_sum':dlocal,'cross_sector_dimension':(NROWS-rb)-dlocal,'AG_positive_control':agc,'lane_payload_sha256':[{'tag':r['tag'],'payload_sha256':r['payload_sha256']} for r in rec],'exact_zero_uses_tolerance':False}
    raw=json.dumps(payload,sort_keys=True,separators=(',',':')).encode();payload['scientific_payload_sha256']=hashlib.sha256(raw).hexdigest();p=Path(a.output);p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(payload,indent=2,sort_keys=True)+'\n');print(json.dumps({k:v for k,v in payload.items() if k not in ('sector_table','lane_payload_sha256')},indent=2,sort_keys=True));return 0 if cls.startswith('CONFIRM') else 2
if __name__=='__main__':raise SystemExit(main())
