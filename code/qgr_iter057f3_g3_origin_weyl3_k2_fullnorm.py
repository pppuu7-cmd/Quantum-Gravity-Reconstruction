#!/usr/bin/env python3
"""Iter057F3: full-tensor-normalized G3-origin Weyl3 L2 extraction."""
import argparse
import json
from pathlib import Path

import numpy as np
import sympy as sp

import qgr_iter057f_g3_origin_weyl3_k2 as f1
import qgr_iter057f2_g3_origin_weyl3_k2_corrected as f2

GATE = "ITER057F3-G3-ORIGIN-WEYL3-DEGREE2-BLOCK-FULL-TENSOR-NORMALIZATION"
PREREG = "bf64df5b213ca9977d2709c7b7fea8cab96ad688"
PASS_CLASS = "PASS_SCOPED_ITER057F3_G3_ORIGIN_WEYL3_K2_BLOCK_EXTRACTED_WITH_EXACT_FULL_TENSOR_NORMALIZATION"
INVALID_CLASS = "INVALID_ITER057F3_FULL_EOM_EXTRACTION_OR_FULL_TENSOR_CONTROL"
ZERO_Q_COL = 8
TRACE_TARGET_FULL = np.array([-48,96,0,0,-48,0,0,-144,0,144],float)/625.0


def exact_objects_full():
    H=sp.diag(1,1,-2); E=f1.KAPPA_Q*H
    W=f1.core.tensor_to_bivector_operator(f1.core.background_weyl_tensor(E))
    Qsp,_=f1.core.q_matrix(W,f1.K_EXACT)
    Qfull_sp=8*Qsp
    Qfull=np.array(Qfull_sp.tolist(),dtype=float)
    zero_cols=[j for j in range(10) if all(sp.simplify(Qfull_sp[i,j])==0 for i in range(10))]
    targets=[]
    for j in range(10):
        dW=f1.core.metric_to_weyl_operator(f1.K_EXACT,f1.core.symmetric_h(j))
        targets.append(float(sp.N(24*sp.trace(W*W*dW),35)))
    return Qfull_sp,Qfull,zero_cols,np.array(targets,float)


def cache_equivalence():
    out=f2.cache_equivalence()
    out['gate']=GATE
    out['preregistration_commit']=PREREG
    return out


def full_response(j,s,eps,hD):
    plus=f1.G3WaveMetric(j,s,+eps); minus=f1.G3WaveMetric(j,s,-eps)
    vp,ip,dp=f1.metric_control(plus,hD); vm,im,dm=f1.metric_control(minus,hD)
    Hp,_=f2.assemble_minus5_cached(plus,np.zeros(4),hD)
    Hm,_=f2.assemble_minus5_cached(minus,np.zeros(4),hD)
    return (Hp-Hm)/(2.0*eps),{
        'metric_valid':bool(vp and vm),
        'max_inverse_residual':max(ip,im),
        'min_abs_det':min(dp,dm),
    }


def fit_even(resp):
    R0=resp[0.0]; A=resp[1.0]-R0; B=resp[2.0]-R0
    L4=(B-4.0*A)/12.0; L2=A-L4
    return R0,L2,L4


def trace_eta(T):
    return float(sum(f1.ETA[a,b]*T[a,b] for a in range(4) for b in range(4)))


def lane(j):
    Qsp,Qfull,zero_cols,targets=exact_objects_full()
    exact_structure_valid=(zero_cols==[ZERO_Q_COL]) and f1.relnorm(targets,TRACE_TARGET_FULL,1e-14)<=1e-13
    qscale=float(np.linalg.norm(Qfull))
    fits={}; held={}; controls=[]
    for hD in f1.HD_PANEL:
        for eps in f1.EPS_PANEL:
            resp={}; cts=[]
            for s in (*f1.S_TRAIN,f1.S_HOLD):
                R,c=full_response(j,s,eps,hD); resp[float(s)]=R; cts.append(c)
            L0,L2,L4=fit_even(resp)
            pred=L0+(f1.S_HOLD**2)*L2+(f1.S_HOLD**4)*L4
            key=f'h{hD:.1e}_e{eps:.1e}'
            fits[key]={'L0':L0,'L2':L2,'L4':L4}
            held[key]=f1.relnorm(resp[f1.S_HOLD],pred)
            controls.extend(cts)

    finest=fits['h5.0e-04_e1.0e-04']; amp_hi=fits['h5.0e-04_e2.0e-04']; st_hi=fits['h1.0e-03_e1.0e-04']
    amp_L2=f1.relnorm(finest['L2'],amp_hi['L2']); h_L2=f1.relnorm(finest['L2'],st_hi['L2'])
    amp_L4=f1.relnorm(finest['L4'],amp_hi['L4']); h_L4=f1.relnorm(finest['L4'],st_hi['L4'])
    hold=held['h5.0e-04_e1.0e-04']
    source_valid=all(c['metric_valid'] and c['max_inverse_residual']<=2e-11 and c['min_abs_det']>1e-5 for c in controls)
    l2_conv=bool(amp_L2<=5e-3 and h_L2<=1e-2)
    hold_ok=bool(hold<=3e-3)

    bcols={key:f1.bilinear_column(d['L4']) for key,d in fits.items()}
    qcol=Qfull[:,j]
    if j==ZERO_Q_COL:
        l4_zero_scales={key:float(np.linalg.norm(v)/max(qscale,1e-14)) for key,v in bcols.items()}
        l4_ok=bool(all(v<=2e-2 for v in l4_zero_scales.values()))
        qres=0.0
    else:
        l4_zero_scales={}
        qres=f1.relnorm(bcols['h5.0e-04_e1.0e-04'],qcol)
        l4_ok=bool(qres<=2e-2 and amp_L4<=5e-3 and h_L4<=1e-2)

    tr=trace_eta(finest['L2']); target=targets[j]
    tr_res=float(abs(tr-target)/max(abs(target),np.linalg.norm(finest['L2']),1e-10))
    trace_ok=bool(tr_res<=1e-2)
    passed=bool(exact_structure_valid and source_valid and l2_conv and hold_ok and l4_ok and trace_ok)

    serial={key:{name:mat.tolist() for name,mat in d.items()} for key,d in fits.items()}
    return {
        'gate':GATE,'preregistration_commit':PREREG,'basis_index':j,
        'pass':passed,'controls_valid':passed,'exact_structure_valid':exact_structure_valid,
        'exact_zero_Qfull_columns':zero_cols,'Qfull_frobenius_scale':qscale,
        'source_metric_valid':source_valid,
        'amplitude_L2_relative_change':amp_L2,'stencil_L2_relative_change':h_L2,
        'amplitude_L4_relative_change_diagnostic':amp_L4,'stencil_L4_relative_change_diagnostic':h_L4,
        'heldout_frequency_relative_residual':hold,
        'exact_fulltensor_L4_column_relative_residual':qres,
        'zero_Qfull_column_global_scale_residuals':l4_zero_scales,
        'trace_eta_L2':tr,'exact_fulltensor_trace_target':target,'trace_Ward_relative_residual':tr_res,
        'exact_Qfull_column':qcol.tolist(),'extracted_L4_bilinear_column':bcols['h5.0e-04_e1.0e-04'].tolist(),
        'fits':serial,
        'classification':'LANE_PASS' if passed else 'LANE_CONTROL_INVALID'
    }


def aggregate(inp):
    objs=[]; errors=[]
    for p in sorted(Path(inp).rglob('*.json')):
        try:
            o=json.loads(p.read_text())
            if 'basis_index' in o: objs.append(o)
        except Exception as ex: errors.append(f'{p}:{ex}')
    by={int(o['basis_index']):o for o in objs}; complete=(len(by)==10 and set(by)==set(range(10)) and not errors)
    if not complete:
        return {'gate':GATE,'classification':INVALID_CLASS,'pass':False,'complete':False,'found':sorted(by),'parse_errors':errors}

    Qsp,Qfull,zero_cols,targets=exact_objects_full()
    L2=[]; B4=[]; traces=[]
    for j in range(10):
        f=by[j]['fits']['h5.0e-04_e1.0e-04']
        T=np.array(f['L2'],float); L2.append(T); traces.append(trace_eta(T))
        B4.append(np.array(by[j]['extracted_L4_bilinear_column'],float))
    B4=np.column_stack(B4); traces=np.array(traces,float)
    b4_sym=f1.relnorm(B4,B4.T); b4_exact=f1.relnorm(B4,Qfull)
    trace_vec=f1.relnorm(traces,targets)

    L2raw=np.column_stack([f1.vec10(T) for T in L2]); sv=np.linalg.svd(L2raw,compute_uv=False)
    tol=max(sv[0]*1e-8,1e-12); rank=int(np.sum(sv>tol))
    M2=f1.a57.einstein_symbol_matrix(f1.K_EXACT); Kg=f1.a57.pure_gauge_columns(f1.K_EXACT)
    ns,P,B=f1.a57.physical_kernel_complement(M2,Kg); Pn=np.array(P.tolist(),float)
    phys=L2raw@Pn; psv=np.linalg.svd(phys,compute_uv=False); ptol=max(psv[0]*1e-8,1e-12) if len(psv) else 1e-12
    prank=int(np.sum(psv>ptol))

    agg_ok=bool(b4_sym<=2e-3 and b4_exact<=2e-2 and trace_vec<=5e-3)
    lane_ok=all(by[j].get('pass') is True for j in range(10))
    passed=bool(lane_ok and agg_ok)
    return {
        'gate':GATE,'preregistration_commit':PREREG,'classification':PASS_CLASS if passed else INVALID_CLASS,
        'pass':passed,'implementation_valid':passed,'complete':True,'parse_errors':errors,
        'lane_pass_count':sum(by[j].get('pass') is True for j in range(10)),
        'exact_zero_Qfull_columns':zero_cols,
        'L4_bilinear_symmetry_relative_residual':b4_sym,'L4_exact_Qfull_relative_residual':b4_exact,
        'L2_trace_vector':traces.tolist(),'exact_fulltensor_trace_target_vector':targets.tolist(),'L2_trace_Ward_vector_relative_residual':trace_vec,
        'L2_raw_frobenius_norm':float(np.linalg.norm(L2raw)),'L2_raw_singular_values':sv.tolist(),'L2_raw_rank_tolerance':tol,'L2_raw_rank':rank,
        'Einstein_nongauge_null_complement_dim':int(P.cols),'L2_image_rank_on_Einstein_nongauge_null_complement':prank,
        'L2_image_singular_values_on_Einstein_nongauge_null_complement':psv.tolist(),
        'claim_ceiling':'FULL-TENSOR-NORMALIZED FRESH G3 ORIGIN K2 EXTRACTION ONLY; FULL CHARACTERISTICS/HYPERBOLICITY/GHOST/TREATMENT NOT ESTABLISHED; C6 SYMBOLIC UNFIXED; THEORY_ESTABLISHED_0'
    }


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--cache-control',action='store_true'); ap.add_argument('--index',type=int); ap.add_argument('--aggregate'); ap.add_argument('--out',required=True); a=ap.parse_args()
    if a.cache_control: out=cache_equivalence()
    elif a.aggregate: out=aggregate(a.aggregate)
    else:
        if a.index is None or not 0<=a.index<10: raise SystemExit('frozen basis index 0..9 required')
        out=lane(a.index)
    Path(a.out).parent.mkdir(parents=True,exist_ok=True); Path(a.out).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    compact={k:v for k,v in out.items() if k!='fits'}; print(json.dumps(compact,sort_keys=True))
    if out.get('pass') is not True: raise SystemExit(2)

if __name__=='__main__': main()
