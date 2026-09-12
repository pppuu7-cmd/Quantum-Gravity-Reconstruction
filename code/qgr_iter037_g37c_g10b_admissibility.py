#!/usr/bin/env python3
"""QGR Iter037 G37C: apply the prospective G10B same-realization criterion to G35/G36 distant roots.

This does not redefine the criterion after seeing multiplicity. It audits the six G36 jointly
persistent finite-cell algebraic witnesses against the older identity/refinement-connected rule:
L(h)=I+h*omega_linear+O(h^2), plus fine-product convergence on a fixed physical path.
"""
import argparse,json,math,os
import numpy as np
from scipy.optimize import least_squares
import qgr_iter036_g36_expanded_patch_persistence as g36

JOINT_G36_SEEDS=[0,1,3,4,5,7]
HS=[0.25,0.125,0.0625,0.03125]
NS=[4,8,16,32]
I=np.eye(4)
PAIRS=[(i,j) for i in range(4) for j in range(i+1,4)]


def Omega(x):
    x=np.asarray(x,dtype=float)
    return math.exp(float(g36.a@x+0.5*x@g36.Q@x))


def residual_at(z,x,h):
    x=np.asarray(x,dtype=float); Om=Omega(x)
    try: L=[g36.L_from(z[6*i:6*i+6]) for i in range(4)]
    except Exception: return np.full(24,1e50)
    out=[]
    for i,j in PAIRS:
        xi=x.copy(); xi[i]+=h; xj=x.copy(); xj[j]+=h
        try:
            lhs=Om*I[:,i]+np.linalg.solve(L[i],Omega(xi)*I[:,j])
            rhs=Om*I[:,j]+np.linalg.solve(L[j],Omega(xj)*I[:,i])
            rr=lhs-rhs
        except Exception:
            rr=np.full(4,1e50)
        if not np.all(np.isfinite(rr)): rr=np.full(4,1e50)
        out.extend(rr)
    return np.asarray(out,dtype=float)


def solve_from(x,h,z0,max_nfev=1800):
    try:
        s=least_squares(lambda z:residual_at(z,x,h),np.asarray(z0,dtype=float),
                        xtol=1e-12,ftol=1e-12,gtol=1e-12,max_nfev=max_nfev)
        rn=float(np.linalg.norm(s.fun)); me=max(g36.metric_errors(s.x))
        ok=bool(np.all(np.isfinite(s.x)) and rn<1e-8 and me<1e-7)
        return s.x,rn,me,ok
    except Exception:
        return None,float('inf'),float('inf'),False


def principal(x,h):
    return solve_from(x,h,np.zeros(24),1200)


def linearized_connection():
    M=[]; src=[]
    for i,j in PAIRS:
        for aa in range(4):
            row=np.zeros(24)
            for m in range(6):
                row[6*i+m]+=g36.B[m,aa,j]
                row[6*j+m]-=g36.B[m,aa,i]
            M.append(row)
            src.append(g36.a[i]*(1 if aa==j else 0)-g36.a[j]*(1 if aa==i else 0))
    M=np.asarray(M); src=np.asarray(src)
    assert np.linalg.matrix_rank(M)==24
    return np.linalg.solve(M,src)

LINEAR=linearized_connection()


def max_L_minus_I(z):
    return float(max(np.linalg.norm(L-I) for L in g36.Ls(z)))


def edge_fp_physical(z,x,h):
    x=np.asarray(x,dtype=float); out=[]
    for i,L in enumerate(g36.Ls(z)):
        xp=x.copy(); xp[i]+=h
        A=(Omega(x)/Omega(xp))*L
        out.append([float(np.trace(A)),float(np.trace(A@A)),float(np.linalg.det(A))])
    return out


def fp_distance(a,b):
    return max(abs(a[i][j]-b[i][j]) for i in range(4) for j in range(3))


def continue_h(z0,h0,h1,substeps=8):
    z=np.asarray(z0,dtype=float).copy(); rows=[]
    logs=np.linspace(math.log(h0),math.log(h1),substeps+1)[1:]
    for k,lh in enumerate(logs,1):
        h=float(math.exp(lh))
        z2,rn,me,ok=solve_from(np.zeros(4),h,z,2200)
        jump=float(np.linalg.norm(z2-z)) if z2 is not None else None
        rows.append({'step':k,'h':h,'residual_norm':rn if math.isfinite(rn) else None,
                     'metric_error':me if math.isfinite(me) else None,'root_jump':jump,'success':ok})
        if not ok: return None,rows
        z=z2
    return z,rows


def observed_orders(vals):
    out=[]
    for (h0,v0),(h1,v1) in zip(vals[:-1],vals[1:]):
        if v0<=0 or v1<=0: out.append(None)
        else: out.append(float(math.log(v1/v0)/math.log(h1/h0)))
    return out


def path_transport_candidate(origin_z,N):
    h=1.0/N; direction=0; A=np.eye(4); z=np.asarray(origin_z).copy()
    rows=[]; max_res=0.; max_me=0.; max_jump=0.
    for n in range(N):
        x=np.zeros(4); x[direction]=n*h
        if n==0:
            z2,rn,me,ok=solve_from(x,h,z,1200)
        else:
            z2,rn,me,ok=solve_from(x,h,z,1800)
        if not ok:
            rows.append({'n':n,'residual_norm':rn if math.isfinite(rn) else None,
                         'metric_error':me if math.isfinite(me) else None,'success':False})
            return None,rows,False
        jump=float(np.linalg.norm(z2-z)) if n>0 else 0.0
        max_jump=max(max_jump,jump); max_res=max(max_res,rn); max_me=max(max_me,me)
        L=g36.L_from(z2[6*direction:6*direction+6])
        xp=x.copy(); xp[direction]+=h
        Aedge=(Omega(x)/Omega(xp))*L
        A=Aedge@A; z=z2
    rows.append({'max_residual':max_res,'max_metric_error':max_me,'max_root_jump':max_jump,'success':True})
    return A,rows,True


def path_transport_principal(N):
    h=1.0/N; direction=0; A=np.eye(4); max_res=0.; max_me=0.
    for n in range(N):
        x=np.zeros(4); x[direction]=n*h
        z,rn,me,ok=principal(x,h)
        if not ok: return None,{'N':N,'success':False,'residual_norm':rn if math.isfinite(rn) else None,
                                'metric_error':me if math.isfinite(me) else None},False
        max_res=max(max_res,rn); max_me=max(max_me,me)
        L=g36.L_from(z[6*direction:6*direction+6])
        xp=x.copy(); xp[direction]+=h
        Aedge=(Omega(x)/Omega(xp))*L; A=Aedge@A
    return A,{'N':N,'success':True,'max_residual':max_res,'max_metric_error':max_me},True


def seq_diffs(paths):
    return [float(np.linalg.norm(paths[b]-paths[a])) for a,b in zip(NS[:-1],NS[1:])]


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--seed-slot',type=int,required=True); ap.add_argument('--out',required=True)
    q=ap.parse_args(); assert 0<=q.seed_slot<6
    g36_seed=JOINT_G36_SEEDS[q.seed_slot]
    ref0,cand0,base=g36.reconstruct_baseline(g36_seed)
    result={'gate':'ITER037-G37C-G10B-SAME-REALIZATION-ADMISSIBILITY','seed_slot':q.seed_slot,
            'g36_seed_index':g36_seed,**base,
            'claim_lock':'Prospective G10B identity/refinement-connected criterion; finite numerical audit is not an asymptotic theorem.'}
    if ref0 is None or cand0 is None or not base.get('baseline_ok'):
        result.update({'reference_controls_valid':False,'classification':'BLOCKED_NUMERICALLY'})
    else:
        cand_by_h={}; principal_by_h={}; rows=[]; cont=[]; z=cand0.copy(); hcur=1.0; blocked=False
        for h in HS:
            z2,crows=continue_h(z,hcur,h,8); cont.extend(crows)
            if z2 is None:
                blocked=True; break
            zp,rnp,mep,okp=principal(np.zeros(4),h)
            if not okp:
                blocked=True; break
            rnc=float(np.linalg.norm(residual_at(z2,np.zeros(4),h))); mec=max(g36.metric_errors(z2))
            cand_by_h[h]=z2.copy(); principal_by_h[h]=zp.copy()
            lc=max_L_minus_I(z2); lp=max_L_minus_I(zp)
            ec=float(np.linalg.norm(z2/h-LINEAR)); ep=float(np.linalg.norm(zp/h-LINEAR))
            fpd=fp_distance(edge_fp_physical(z2,np.zeros(4),h),edge_fp_physical(zp,np.zeros(4),h))
            rd=float(np.linalg.norm(z2-zp))
            rows.append({'h':h,'candidate_residual':rnc,'candidate_metric_error':mec,
                         'principal_residual':rnp,'principal_metric_error':mep,
                         'candidate_max_L_minus_I':lc,'principal_max_L_minus_I':lp,
                         'candidate_L_minus_I_over_h':lc/h,'principal_L_minus_I_over_h':lp/h,
                         'candidate_scaled_linear_error':ec,'principal_scaled_linear_error':ep,
                         'candidate_principal_root_distance':rd,'invariant_edge_fingerprint_distance':fpd})
            z=z2; hcur=h
        result['continuation_rows']=cont; result['scaling_rows']=rows
        if blocked or len(rows)!=len(HS):
            result.update({'reference_controls_valid':False,'classification':'BLOCKED_NUMERICALLY'})
        else:
            cand_orders=observed_orders([(r['h'],r['candidate_max_L_minus_I']) for r in rows])
            princ_orders=observed_orders([(r['h'],r['principal_max_L_minus_I']) for r in rows])
            cand_rat=max(r['candidate_L_minus_I_over_h'] for r in rows)
            princ_rat=max(r['principal_L_minus_I_over_h'] for r in rows)
            errors=[r['candidate_scaled_linear_error'] for r in rows]
            order_ok=bool(len(cand_orders)>=3 and cand_orders[-1] is not None and cand_orders[-2] is not None and
                          cand_orders[-1]>0.8 and cand_orders[-2]>0.8)
            ratio_ok=bool(cand_rat <= 5.0*princ_rat)
            linear_trend_ok=bool(errors[-3]>errors[-2]>errors[-1])
            linear_final_ok=bool(errors[-1]<0.05)
            first_order_ok=bool(order_ok and ratio_ok and linear_trend_ok and linear_final_ok)
            result.update({'candidate_observed_orders':cand_orders,'principal_observed_orders':princ_orders,
                           'order_ok':order_ok,'bounded_Oh_ratio_ok':ratio_ok,
                           'linear_error_final_two_decrease_ok':linear_trend_ok,
                           'final_scaled_linear_error_ok':linear_final_ok,
                           'g10b_first_order_compatible_scoped':first_order_ok})
            cand_paths={}; princ_paths={}; cand_path_rows={}; princ_path_rows={}; path_block=False
            for N in NS:
                h=1.0/N
                A,rr,ok=path_transport_candidate(cand_by_h[h],N)
                Ap,rp,okp=path_transport_principal(N)
                cand_path_rows[str(N)]=rr; princ_path_rows[str(N)]=rp
                if not ok or not okp:
                    path_block=True; break
                cand_paths[N]=A; princ_paths[N]=Ap
            result['candidate_path_rows']=cand_path_rows; result['principal_path_rows']=princ_path_rows
            if path_block or len(cand_paths)!=len(NS):
                result.update({'reference_controls_valid':not path_block,'classification':'BLOCKED_NUMERICALLY'})
            else:
                cd=seq_diffs(cand_paths); pd=seq_diffs(princ_paths)
                cdec=bool(cd[1]<cd[0] and cd[2]<cd[1])
                pdec=bool(pd[1]<pd[0] and pd[2]<pd[1])
                cratio=cd[-1]/cd[-2] if cd[-2]>0 else float('inf')
                pratio=pd[-1]/pd[-2] if pd[-2]>0 else float('inf')
                cpath_ok=bool(cdec and cratio<0.75)
                pcontrol=bool(pdec and pratio<0.75)
                path_cp=float(np.linalg.norm(cand_paths[32]-princ_paths[32]))
                final=rows[-1]
                merged=bool(first_order_ok and cpath_ok and pcontrol and
                            final['candidate_principal_root_distance']<1e-6 and
                            final['invariant_edge_fingerprint_distance']<1e-9)
                controls=bool(pcontrol and all(r['principal_residual']<1e-8 and r['principal_metric_error']<1e-7 for r in rows))
                if not controls:
                    cls='BLOCKED_NUMERICALLY'
                elif first_order_ok and cpath_ok:
                    cls='REFINEMENT_CONNECTED_MERGE_TO_PRINCIPAL_SCOPED' if merged else 'FINITE_RESOLUTION_REFINEMENT_CONNECTED_DISTINCT_CANDIDATE'
                else:
                    cls='DISTANT_BRANCH_FAILS_G10B_SAME_REALIZATION_ADMISSIBILITY_SCOPED'
                result.update({'candidate_path_successive_differences':cd,'principal_path_successive_differences':pd,
                               'candidate_path_final_contraction_ratio':cratio,'principal_path_final_contraction_ratio':pratio,
                               'candidate_path_product_convergence_ok':cpath_ok,'principal_path_control_ok':pcontrol,
                               'candidate_principal_path_distance_N32':path_cp,
                               'merge_thresholds_met':merged,'reference_controls_valid':controls,'classification':cls})
    os.makedirs(os.path.dirname(q.out),exist_ok=True)
    with open(q.out,'w',encoding='utf-8') as f:
        json.dump(result,f,indent=2,sort_keys=True,allow_nan=False); f.write('\n')
    compact={k:v for k,v in result.items() if k not in ('continuation_rows','candidate_path_rows','principal_path_rows')}
    print(json.dumps(compact,sort_keys=True,allow_nan=False))

if __name__=='__main__': main()
