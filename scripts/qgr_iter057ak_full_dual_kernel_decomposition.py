#!/usr/bin/env python3
"""Iter057AK exact decomposition of the terminal Iter057AF dual kernel.

Scientific object frozen at preregistration e9f3003c7a7b2e776961f60f5e4f493c6744b146.
No Iter057AG coefficients are consumed until the new B/O0 decomposition and
normalized witness have been constructed from immutable Iter057AD/AF columns.
"""
from __future__ import annotations
import argparse, hashlib, json
from fractions import Fraction as F
from itertools import permutations, product
from pathlib import Path

import sympy as sp
from flint import fmpq, fmpq_mat

import qgr_iter057z_dodecic_einstein_seed_completion as z
import qgr_iter057ag_dual_obstruction_witness as ag

PREREG='e9f3003c7a7b2e776961f60f5e4f493c6744b146'
PASS='PASS_SCOPED_ITER057AK_FULL_DUAL_KERNEL_DECOMPOSITION_IDENTIFIES_UNIQUE_AH_PARITY_OBSTRUCTION_CHANNEL'
FAIL='SCIENTIFIC_FAIL_ITER057AK_UNIQUE_AH_PARITY_OBSTRUCTION_CHANNEL_HYPOTHESIS_FALSE'
BLOCKED='BLOCKED_ITER057AK_COMPLETE_EXACT_DUAL_KERNEL_DECOMPOSITION_NOT_TECHNICALLY_REALIZED'
INVALID='INVALID_ITER057AK_AUTHORITY_EXACTNESS_OR_NO_REFIT_CONTROL_FAILURE'
AG_DATA_COMMIT='79f447491834eaa67c2516d50433be619f098dd2'
AG_DATA_SHA='5ecb962af9a1265a8846a6d8de4cd0885c2b53bea630a5729a8c069aae9fd9da'
NROWS=1456; NCOLS=1114
ROOT=Path(__file__).resolve().parents[1]
AG_DATA=ROOT/'data'/'ITER057AG_CANONICAL_DUAL_WITNESS.json'


def ff(x):
    if isinstance(x,F): return x
    if isinstance(x,sp.Rational): return F(int(x.p),int(x.q))
    return F(str(x))

def fq(x):
    x=ff(x); return fmpq(x.numerator,x.denominator)

def ftxt(x):
    x=ff(x); return str(x.numerator) if x.denominator==1 else f'{x.numerator}/{x.denominator}'

def assemble_exact(old_root,af_root):
    recs,cols,controls,coverage,dup=ag.assemble(Path(old_root),Path(af_root))
    return recs,cols,bool(controls),bool(coverage),list(dup)

def canonical_o0():
    M14,rows14,L,r0,O0,prov,inv,ann=ag.canonical_object()
    return M14,rows14,L,r0,O0,bool(prov),bool(inv),bool(ann)

def matrices(cols,O0):
    A=fmpq_mat(NCOLS,NROWS)       # B^T
    Aug=fmpq_mat(NCOLS+1,NROWS)  # [B^T ; O0^T]
    byrow={i:{} for i in range(NROWS)}
    nnz=0
    for j,d in cols.items():
        for i,v in d.items():
            q=fq(v); A[j,i]=q; Aug[j,i]=q; byrow[i][j]=v; nnz+=1
    for i,x in enumerate(O0): Aug[NCOLS,i]=fq(x)
    return A,Aug,byrow,nnz

def rref_kernel(A):
    R,rank=A.rref(); rank=int(rank)
    piv=[]
    for r in range(rank):
        p=None
        for c in range(A.ncols()):
            if R[r,c] != 0:
                p=c; break
        if p is None: raise ArithmeticError('RREF row without pivot')
        if R[r,p] != 1: raise ArithmeticError('nonunit RREF pivot')
        piv.append(p)
    pset=set(piv); free=[c for c in range(A.ncols()) if c not in pset]
    K=fmpq_mat(A.ncols(),len(free))
    for j,f in enumerate(free):
        K[f,j]=fmpq(1)
        for r,p in enumerate(piv):
            if R[r,f] != 0: K[p,j]=-R[r,f]
    return R,rank,piv,free,K

def sectors(a11):
    out={}
    for b in range(4):
        for j,beta in enumerate(a11):
            key=(b,tuple(int(e)%2 for e in beta))
            out.setdefault(key,[]).append(b*len(a11)+j)
    return dict(sorted(out.items()))

def sector_matrix(ids,byrow,O0):
    M=fmpq_mat(NCOLS,len(ids)); Q=fmpq_mat(NCOLS+1,len(ids))
    for k,i in enumerate(ids):
        for j,v in byrow[i].items():
            x=fq(v); M[j,k]=x; Q[j,k]=x
        Q[NCOLS,k]=fq(O0[i])
    return M,Q

def local_sector_table(sec,byrow,O0):
    table=[]; dlocal=0; active=[]
    for (b,p),ids in sec.items():
        M,Q=sector_matrix(ids,byrow,O0)
        r=int(M.rank()); ar=int(Q.rank()); n=len(ids); nul=n-r; act=ar-r
        if act not in (0,1): raise ArithmeticError('sector activity not 0/1')
        dlocal+=nul
        key=f'{b}:' + ''.join(str(x) for x in p)
        if act: active.append(key)
        table.append({'key':key,'b':b,'parity':list(p),'coordinate_count':n,'Btranspose_sector_nnz':sum(len(byrow[i]) for i in ids),'rank':r,'nullity':nul,'rank_with_O0_row':ar,'obstruction_active_rank':act})
    return table,dlocal,active

def coord_perm(a11,perm,tensor_index):
    lookup={a:i for i,a in enumerate(a11)}; m=len(a11); mp=[None]*NROWS
    for b in range(4):
        for j,beta in enumerate(a11):
            oldsp=beta[1:]; newsp=[0,0,0]
            for oldax in range(3): newsp[perm[oldax]]=oldsp[oldax]
            nb=b
            if tensor_index and b>0: nb=perm[b-1]+1
            nbe=(beta[0],newsp[0],newsp[1],newsp[2])
            mp[b*m+j]=nb*m+lookup[nbe]
    if len(set(mp))!=NROWS: raise ArithmeticError('coordinate action not permutation')
    return mp

def permute_kernel_rows(K,mp):
    T=fmpq_mat(K.nrows(),K.ncols())
    for old,new in enumerate(mp):
        for j in range(K.ncols()):
            x=K[old,j]
            if x != 0: T[new,j]=x
    return T

def induced_from_free(TK,free):
    G=fmpq_mat(len(free),len(free))
    for i,f in enumerate(free):
        for j in range(len(free)):
            x=TK[f,j]
            if x != 0:G[i,j]=x
    return G

def perm_parity(perm):
    inv=0
    for i in range(3):
        for j in range(i+1,3):
            if perm[i]>perm[j]: inv+=1
    return -1 if inv%2 else 1

def permutation_type(perm):
    if tuple(perm)==(0,1,2): return 'identity'
    return 'transposition' if perm_parity(perm)<0 else 'three_cycle'

def matrix_trace(M):
    return sum((ff(M[i,i]) for i in range(min(M.nrows(),M.ncols()))),F(0))

def ell_on_kernel(O0,K):
    ell=fmpq_mat(1,K.ncols())
    for j in range(K.ncols()):
        s=F(0)
        for i,x in enumerate(O0):
            if x!=0 and K[i,j]!=0: s += ff(x)*ff(K[i,j])
        ell[0,j]=fq(s)
    return ell

def row_nonzero(M): return any(M[0,j]!=0 for j in range(M.ncols()))

def s3_diagnostic(label,a11,K,free,O0,tensor_index):
    perms=list(permutations(range(3))); maps={p:coord_perm(a11,p,tensor_index) for p in perms}
    generators=[(1,0,2),(1,2,0)]  # transposition and 3-cycle generate S3
    inv_controls={}; Gs={}
    for p in perms:
        TK=permute_kernel_rows(K,maps[p]); G=induced_from_free(TK,free); Gs[p]=G
    # Exact membership test on generators. If both preserve K, group closure proves all six preserve K.
    for p in generators:
        TK=permute_kernel_rows(K,maps[p]); pred=K*Gs[p]
        inv_controls[str(p)]=(pred==TK)
    invariant=all(inv_controls.values())
    out={'label':label,'generator_exact_invariance':inv_controls,'all_six_invariant_by_group_closure':invariant,'irrep_decomposition':'NOT_DEFINED_NONINVARIANT'}
    if not invariant:
        for p in generators:
            if not inv_controls[str(p)]: out['first_failing_generator']=list(p); break
        return out
    traces={str(p):ftxt(matrix_trace(Gs[p])) for p in perms}
    cls={}
    for p in perms: cls.setdefault(permutation_type(p),[]).append(ff(matrix_trace(Gs[p])))
    class_constant=all(len(set(v))==1 for v in cls.values())
    chi_e=cls['identity'][0]; chi_t=cls['transposition'][0]; chi_c=cls['three_cycle'][0]
    mtriv=(chi_e+3*chi_t+2*chi_c)/6
    msign=(chi_e-3*chi_t+2*chi_c)/6
    mstd=(chi_e-chi_c)/3
    multiplicities={'trivial':ftxt(mtriv),'sign':ftxt(msign),'standard_copy_count':ftxt(mstd),'standard_isotypic_dimension':ftxt(2*mstd)}
    # Functional activity on frozen rational character projectors, evaluated in kernel coordinates.
    ell=ell_on_kernel(O0,K); k=K.ncols()
    triv=fmpq_mat(1,k); sign=fmpq_mat(1,k)
    for p in perms:
        eg=ell*Gs[p]; sgn=perm_parity(p)
        for j in range(k):
            triv[0,j]+=eg[0,j]
            sign[0,j]+=sgn*eg[0,j]
    six=fmpq(6)
    for j in range(k): triv[0,j]/=six; sign[0,j]/=six
    std=fmpq_mat(1,k)
    for j in range(k): std[0,j]=ell[0,j]-triv[0,j]-sign[0,j]
    out.update({'all_six_trace':traces,'character_constant_on_conjugacy_classes':class_constant,'character':{'identity':ftxt(chi_e),'transposition':ftxt(chi_t),'three_cycle':ftxt(chi_c)},'irrep_decomposition':multiplicities,'O0_pairing_activity_by_isotypic':{'trivial':row_nonzero(triv),'sign':row_nonzero(sign),'standard':row_nonzero(std)}})
    return out

def normalized_witness(cols,O0):
    y,rank,piv=ag.canonical_y(cols,O0)
    bt,norm=ag.residuals(cols,O0,y)
    return y,rank,piv,bt,norm

def ag_positive_control(y):
    d=json.loads(AG_DATA.read_text()); ref=[F(0)]*NROWS
    for r in d.get('canonical_y',[]): ref[int(r['compatibility_index'])]=F(r['value'])
    provenance=(d.get('scientific_payload_sha256')==AG_DATA_SHA and d.get('classification')==ag.PASS)
    return provenance, y==ref, sum(v!=0 for v in ref)

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--old-root',required=True); ap.add_argument('--af-root',required=True); ap.add_argument('--output',required=True); a=ap.parse_args()
    recs,cols,lane_ok,coverage,dup=assemble_exact(a.old_root,a.af_root)
    M14,rows14,L,r0,O0,prov,inv,ann=canonical_o0(); o0nz=sum(x!=0 for x in O0)
    A,Aug,byrow,nnz=matrices(cols,O0)
    rankA=int(A.rank()) if lane_ok and coverage else None; rankAug=int(Aug.rank()) if rankA is not None else None
    R,rankR,piv,free,K=rref_kernel(A) if rankA==1110 else (None,None,[],[],None)
    a11=z.alphas(11); sec=sectors(a11)
    table,dlocal,active=local_sector_table(sec,byrow,O0) if K is not None else ([],None,[])
    dcross=(len(free)-dlocal) if dlocal is not None else None
    y=[];wrank=None;wpiv=[];bt=[];norm=None
    if K is not None: y,wrank,wpiv,bt,norm=normalized_witness(cols,O0)
    agprov=agmatch=False; agnz=None
    if y: agprov,agmatch,agnz=ag_positive_control(y)
    s3ah=s3ten=None
    if K is not None:
        s3ah=s3_diagnostic('T_AH',a11,K,free,O0,False)
        s3ten=s3_diagnostic('T_tensor',a11,K,free,O0,True)
    ahkey='0:1000'; ah=[r for r in table if r['key']==ahkey]
    unique_hyp=(active==[ahkey] and len(ah)==1 and ah[0]['nullity']==1 and ah[0]['obstruction_active_rank']==1)
    controls={
      'A_lane_payload_controls_exact':lane_ok,
      'A_complete_unique_coverage':coverage and not dup and len(cols)==1114,
      'A_B_nnz_80982':nnz==80982,
      'A_canonical_O0_nonzero_223':o0nz==223,
      'A_lower_authority_inverse_left_controls':prov and inv and ann and M14.shape==(6790,6800) and L.shape==(1456,6790),
      'B_global_rank_B_1110':rankA==1110,
      'B_global_rank_augmented_1111':rankAug==1111,
      'B_kernel_dimension_346':len(free)==346,
      'B_kernel_rref_rank_replays_1110':rankR==1110,
      'C_sector_partition_32_nonempty_covers_1456':len(sec)==32 and sum(len(v) for v in sec.values())==1456,
      'C_sector_activity_boolean':all(r['obstruction_active_rank'] in (0,1) for r in table),
      'D_global_KcapO0perp_dimension_345':(NROWS-rankAug)==345,
      'D_obstruction_quotient_dimension_1':rankAug-rankA==1,
      'E_normalized_witness_BT_zero':bool(bt) and all(v==0 for v in bt),
      'E_normalized_witness_O0_one':norm==1,
      'F_AG_positive_control_provenance':agprov,
      'F_AG_positive_control_coefficient_identity_after_new_construction':agmatch and agnz==56,
      'G_no_numerical_tolerance':True,
    }
    authority_ok=all(controls.values())
    if not (lane_ok and coverage and prov and inv and ann): cls=INVALID
    elif not authority_ok: cls=BLOCKED
    elif unique_hyp: cls=PASS
    else: cls=FAIL
    payload={'gate':'ITER057AK-FULL-DUAL-KERNEL-PARITY-SYMMETRY-OBSTRUCTION-DECOMPOSITION','preregistration':PREREG,'classification':cls,'controls':controls,
      'global':{'B_shape':[NROWS,NCOLS],'B_nnz':nnz,'rank_B':rankA,'rank_augmented_B_minus_O0':rankAug,'kernel_dimension':(NROWS-rankA if rankA is not None else None),'kernel_O0_orthogonal_dimension':(NROWS-rankAug if rankAug is not None else None),'obstruction_quotient_dimension':(rankAug-rankA if rankA is not None and rankAug is not None else None),'O0_nonzero_count':o0nz},
      'sector_convention':'Iter057AH key=(b,beta mod 2), degree-11 lexicographic beta ordering','nonempty_sector_count':len(sec),'sector_table':table,'support_local_kernel_dimension_sum':dlocal,'genuinely_cross_sector_kernel_dimension':dcross,'obstruction_active_sector_keys':active,'unique_AH_channel_hypothesis':unique_hyp,
      'S3_diagnostics':{'T_AH':s3ah,'T_tensor':s3ten},'normalized_witness':{'system_rank':wrank,'nonzero_count':sum(v!=0 for v in y),'BT_nonzero_count':sum(v!=0 for v in bt),'O0_pairing':ftxt(norm) if norm is not None else None,'ag_coefficient_identity':agmatch},
      'artifact_payload_sha256':[{'tag':r['tag'],'payload_sha256':r['payload_sha256']} for r in recs],'exact_zero_uses_tolerance':False,
      'scope':'exact decomposition of the frozen finite local Iter057AF dual kernel/obstruction on one canonical background only; not cross-background or global/all-orders/physical symmetry evidence'}
    raw=json.dumps(payload,sort_keys=True,separators=(',',':')).encode();payload['scientific_payload_sha256']=hashlib.sha256(raw).hexdigest();p=Path(a.output);p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(payload,indent=2,sort_keys=True)+'\n')
    brief={k:v for k,v in payload.items() if k not in ('sector_table','artifact_payload_sha256')};print(json.dumps(brief,indent=2,sort_keys=True));return 0 if cls in (PASS,FAIL) else 2
if __name__=='__main__': raise SystemExit(main())
