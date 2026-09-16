#!/usr/bin/env python3
"""Iter057AG exact dual obstruction witness for terminal Iter057AF.

Prospective definition frozen at 11dfc1e4db79ff691fe121ab38281f3532f931bf.
The witness y is the free-variables-zero exact-RREF solution of
    B^T y = 0,  O0^T y = 1.
It is then lifted to the original affine rows as w^T = y^T L.
"""
from __future__ import annotations
import argparse, hashlib, json
from fractions import Fraction as F
from pathlib import Path
import sympy as sp
from flint import fmpq, fmpq_mat
import qgr_iter057ad_branch_obstruction as ad
import qgr_iter057af_rank_only_aggregate as afr

PREREG='11dfc1e4db79ff691fe121ab38281f3532f931bf'
PASS='PASS_SCOPED_ITER057AG_EXACT_DUAL_OBSTRUCTION_WITNESS_CERTIFIES_ITER057AF_BRANCH_INCONSISTENCY'
BLOCKED='BLOCKED_ITER057AG_EXACT_DUAL_OBSTRUCTION_WITNESS_NOT_TECHNICALLY_REALIZED'
INVALID='INVALID_ITER057AG_CONSUMED_AF_AUTHORITY_OR_EXACTNESS_CONTROL_CONTRADICTION'
NROWS=1456; NCOLS=1114

def ff(x):
    if isinstance(x,F): return x
    if isinstance(x,sp.Rational): return F(int(x.p),int(x.q))
    return F(str(x))

def assemble(old_root:Path,af_root:Path):
    records=[]; cols={}; dup=[]
    for i,rng in enumerate(afr.OLD_RANGES): records.append(afr.consume(old_root/str(i),rng,f'AD-{i}'))
    for i,rng in enumerate(afr.AF_RANGES): records.append(afr.consume(af_root/str(i),rng,f'AF-{i}'))
    controls=all(all(r['checks'].values()) for r in records)
    for r in records:
        for j,d in r['columns'].items():
            if j in cols: dup.append(j)
            cols[j]=d
    coverage=(not dup and set(cols)==set(range(NCOLS)))
    return records,cols,controls,coverage,dup

def canonical_object():
    g0,prov=ad.canonical_seed12()
    M14,rows14,meta14,a11,r0,inv=ad.rhs14(g0)
    L=ad.left_controls(rows14,meta14,a11)
    ann=(L*M14)==sp.zeros(L.rows,M14.cols)
    O0=L*r0
    return M14,rows14,L,r0,O0,bool(prov),bool(inv),bool(ann)

def canonical_y(cols,O0):
    # 1114 B^T rows + one frozen normalization row; final column is RHS.
    A=fmpq_mat(NCOLS+1,NROWS+1)
    for j,d in cols.items():
        for i,v in d.items(): A[j,i]=fmpq(v.numerator,v.denominator)
    for i,x in enumerate(O0):
        v=ff(x); A[NCOLS,i]=fmpq(v.numerator,v.denominator)
    A[NCOLS,NROWS]=fmpq(1)
    R,rank=A.rref()
    piv=[]
    for r in range(rank):
        p=None
        for c in range(NROWS):
            if R[r,c] != 0:
                p=c; break
        if p is None:
            if R[r,NROWS] != 0: raise ArithmeticError('inconsistent normalized witness system')
            continue
        piv.append((r,p))
    if len({p for _,p in piv})!=len(piv): raise ArithmeticError('duplicate RREF pivots')
    y=[F(0)]*NROWS
    for r,p in piv:
        # RREF pivot is 1; free coordinates are prospectively set to zero.
        if R[r,p] != 1: raise ArithmeticError('nonunit RREF pivot')
        y[p]=F(str(R[r,NROWS]))
    return y,int(rank),[p for _,p in piv]

def residuals(cols,O0,y):
    bt=[]
    for j in range(NCOLS):
        s=F(0)
        for i,v in cols[j].items(): s += v*y[i]
        bt.append(s)
    norm=sum((ff(O0[i])*y[i] for i in range(NROWS)),F(0))
    return bt,norm

def induced_w(L,y):
    w={}
    for (i,j),x in L.todok().items():
        if y[i]:
            v=w.get(j,F(0))+y[i]*ff(x)
            if v: w[j]=v
            elif j in w: del w[j]
    return w

def verify_original(rows14,r0,w,ncols):
    res={}
    for i,wi in w.items():
        for j,x in rows14[i].items():
            v=res.get(j,F(0))+wi*ff(x)
            if v: res[j]=v
            elif j in res: del res[j]
    dot=sum((wi*ff(r0[i]) for i,wi in w.items()),F(0))
    return res,dot

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--old-root',required=True);ap.add_argument('--af-root',required=True);ap.add_argument('--source-run',type=int,required=True);ap.add_argument('--source-head',required=True);ap.add_argument('--output',required=True);a=ap.parse_args()
    recs,cols,lane_controls,coverage,dup=assemble(Path(a.old_root),Path(a.af_root))
    M14,rows14,L,r0,O0,prov,inv,ann=canonical_object(); o0nz=sum(x!=0 for x in O0)
    rb=ra=None
    if lane_controls and coverage and prov and inv and ann and o0nz==223:
        rb,ra=afr.exact_ranks(cols,O0)
    authority_ok=(a.source_head==afr.AF_SOURCE_HEAD and rb==1110 and ra==1111 and M14.shape==(6790,6800) and L.shape==(1456,6790))
    y=[];sysrank=None;piv=[];bt=[];norm=None;w={};origres={};wdot=None
    if authority_ok:
        y,sysrank,piv=canonical_y(cols,O0)
        bt,norm=residuals(cols,O0,y)
        w=induced_w(L,y)
        origres,wdot=verify_original(rows14,r0,w,M14.cols)
    controls={
      'A_lane_payload_controls_exact':lane_controls,
      'A_complete_unique_coverage_0_1113':coverage and not dup,
      'A_B_shape_1456x1114':coverage and len(cols)==1114,
      'A_B_nnz_80982':sum(len(d) for d in cols.values())==80982,
      'A_canonical_O0_nonzero_223':o0nz==223,
      'A_L14_annihilates_M14':ann,
      'A_lower_authority_ok':prov,
      'A_inverse_ok':inv,
      'B_exact_rank_B_1110':rb==1110,
      'B_exact_augmented_rank_1111':ra==1111,
      'C_rref_witness_system_rank_1111':sysrank==1111,
      'D_y_nonzero':bool(y) and any(y),
      'D_BT_y_exact_zero_1114':bool(bt) and all(v==0 for v in bt),
      'D_O0T_y_exact_one':norm==1,
      'E_w_nonzero':bool(w),
      'E_wT_M14_exact_zero_6800':authority_ok and not origres,
      'E_wT_r0_exact_one':wdot==1,
      'F_no_numerical_tolerance':True,
    }
    passed=all(controls.values())
    cls=PASS if passed else (INVALID if (lane_controls and coverage and (rb not in (None,1110) or ra not in (None,1111))) else BLOCKED)
    ysp=[{'compatibility_index':i,'value':str(v)} for i,v in enumerate(y) if v]
    wsp=[{'affine_row_index':i,'value':str(v)} for i,v in sorted(w.items())]
    payload={'gate':'ITER057AG-EXACT-DUAL-OBSTRUCTION-WITNESS','preregistration':PREREG,'source_run':a.source_run,'source_head':a.source_head,'classification':cls,'controls':controls,'B_shape':[NROWS,NCOLS],'B_nnz':sum(len(d) for d in cols.values()),'rank_B':rb,'rank_augmented_B_minus_O0':ra,'canonical_obstruction_nonzero_count':o0nz,'witness_system_rank':sysrank,'witness_pivot_count':len(piv),'y_nonzero_count':len(ysp),'w_nonzero_count':len(wsp),'BT_y_nonzero_count':sum(v!=0 for v in bt),'O0T_y':str(norm) if norm is not None else None,'wT_M14_nonzero_count':len(origres),'wT_r0':str(wdot) if wdot is not None else None,'canonical_y':ysp,'induced_w':wsp,'lane_payload_sha256':[{'tag':r['tag'],'payload_sha256':r['payload_sha256']} for r in recs],'exact_zero_uses_tolerance':False,'scope':'compact exact dual certificate for the frozen finite local Iter057AF obstruction only; no global/all-orders/quantum claim'}
    raw=json.dumps(payload,sort_keys=True,separators=(',',':')).encode();payload['scientific_payload_sha256']=hashlib.sha256(raw).hexdigest();p=Path(a.output);p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(payload,indent=2,sort_keys=True)+'\n')
    print(json.dumps({k:v for k,v in payload.items() if k not in ('canonical_y','induced_w','lane_payload_sha256')},indent=2,sort_keys=True)); return 0 if passed else 2
if __name__=='__main__': raise SystemExit(main())
