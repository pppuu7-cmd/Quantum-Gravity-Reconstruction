#!/usr/bin/env python3
"""Iter057F2: corrected-control G3-origin Weyl3 L2 extraction with exact cache equivalence."""
import argparse
import json
import math
from pathlib import Path

import numpy as np
import sympy as sp

import qgr_iter051c_d2n_near_null as d2n
import qgr_iter057f_g3_origin_weyl3_k2 as f1

GATE = "ITER057F2-G3-ORIGIN-WEYL3-DEGREE2-BLOCK-CONTROL-CORRECTED-EXTRACTION"
PREREG = "a6bbabeb93a83f212892eb2c84cbed17d601ece8"
PASS_CLASS = "PASS_SCOPED_ITER057F2_G3_ORIGIN_WEYL3_K2_BLOCK_EXTRACTED_WITH_CORRECTED_EXACT_CONTROLS"
INVALID_CLASS = "INVALID_ITER057F2_FULL_EOM_EXTRACTION_OR_CORRECTED_CONTROL"
TRACE_TARGET = np.array([-6,12,0,0,-6,0,0,-18,0,18],float)/625.0
ZERO_Q_COL = 8


def point_key(x):
    return np.asarray(x,dtype=np.float64).tobytes()


def assemble_minus5_cached(metric,x,h):
    """Algebraically identical d2n assemble_minus5, caching exact repeated stencil points."""
    x=np.asarray(x,float)
    pcache={}
    fcache={}

    def p_actual(z):
        z=np.asarray(z,float); key=point_key(z)
        if key not in pcache:
            pcache[key]=d2n.p_actual(metric,z)
        return pcache[key]

    def first_div(z):
        z=np.asarray(z,float); key=point_key(z)
        if key in fcache:
            return fcache[key]
        g,dg,ddg,gi,G,R=d2n.c.geometry(metric,z)
        P0=p_actual(z)
        dP=np.empty((4,4,4,4,4))
        for axis in range(4):
            dP[axis]=d2n.derivative5(lambda q:p_actual(q),z,axis,h)
        S=d2n.b0.first_cov(P0,dP,G)
        out=np.einsum('aambn->mbn',S)
        fcache[key]=out
        return out

    g,dg,ddg,gi,G,R=d2n.c.geometry(metric,x)
    P=p_actual(x)
    A=d2n.c.algebraic_A(R,g)
    I=d2n.c.lowering_insertion(R,g,P)
    R0=first_div(x)
    D=np.zeros((4,4))
    for bb in range(4):
        dR=d2n.derivative5(lambda q:first_div(q),x,bb,h)
        D += dR[:,bb,:]
        for m in range(4):
            for n in range(4):
                for rr in range(4):
                    D[m,n]+=G[m,bb,rr]*R0[rr,bb,n]+G[bb,bb,rr]*R0[m,rr,n]+G[n,bb,rr]*R0[m,bb,rr]
    sg=math.sqrt(-float(np.linalg.det(g)))
    H=A+I-2.0*sg*D
    return H,{'g':g,'R':R,'P':P,'A':A,'I':I,'D':D,'p_cache_size':len(pcache),'first_div_cache_size':len(fcache)}


def cache_equivalence():
    metric=f1.G3WaveMetric(0,1.0,1.0e-4)
    x=np.zeros(4); h=1.0e-3
    Ho,_=d2n.assemble_minus5(metric,x,h)
    Hc,zc=assemble_minus5_cached(metric,x,h)
    rel=f1.relnorm(Hc,Ho,1e-14)
    absmax=float(np.max(np.abs(Hc-Ho)))
    passed=bool(rel<=1e-12 and absmax<=1e-12)
    return {
        'gate':GATE,'mode':'cache-equivalence','pass':passed,
        'relative_residual':rel,'max_abs_residual':absmax,
        'p_cache_size':zc['p_cache_size'],'first_div_cache_size':zc['first_div_cache_size'],
        'classification':'CACHE_EQUIVALENCE_PASS' if passed else 'CACHE_EQUIVALENCE_INVALID'
    }


def full_response(j,s,eps,hD):
    plus=f1.G3WaveMetric(j,s,+eps); minus=f1.G3WaveMetric(j,s,-eps)
    vp,ip,dp=f1.metric_control(plus,hD); vm,im,dm=f1.metric_control(minus,hD)
    Hp,_=assemble_minus5_cached(plus,np.zeros(4),hD)
    Hm,_=assemble_minus5_cached(minus,np.zeros(4),hD)
    return (Hp-Hm)/(2.0*eps),{
        'metric_valid':bool(vp and vm),
        'max_inverse_residual':max(ip,im),
        'min_abs_det':min(dp,dm),
    }


def exact_objects():
    H=sp.diag(1,1,-2); E=f1.KAPPA_Q*H
    W=f1.core.tensor_to_bivector_operator(f1.core.background_weyl_tensor(E))
    Qsp,_=f1.core.q_matrix(W,f1.K_EXACT)
    Q=np.array(Qsp.tolist(),dtype=float)
    zero_cols=[j for j in range(10) if all(sp.simplify(Qsp[i,j])==0 for i in range(10))]
    targets=[]
    for j in range(10):
        dW=f1.core.metric_to_weyl_operator(f1.K_EXACT,f1.core.symmetric_h(j))
        targets.append(float(sp.N(3*sp.trace(W*W*dW),35)))
    return Qsp,Q,zero_cols,np.array(targets,float)


def fit_even(resp):
    R0=resp[0.0]; A=resp[1.0]-R0; B=resp[2.0]-R0
    L4=(B-4.0*A)/12.0; L2=A-L4
    return R0,L2,L4


def trace_eta(T):
    return float(sum(f1.ETA[a,b]*T[a,b] for a in range(4) for b in range(4)))


def lane(j):
    Qsp,Q,zero_cols,targets=exact_objects()
    exact_structure_valid=(zero_cols==[ZERO_Q_COL]) and f1.relnorm(targets,TRACE_TARGET,1e-14)<=1e-13
    qscale=float(np.linalg.norm(Q))
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
    qcol=Q[:,j]
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
        'exact_zero_Q_columns':zero_cols,'Q_frobenius_scale':qscale,
        'source_metric_valid':source_valid,
        'amplitude_L2_relative_change':amp_L2,'stencil_L2_relative_change':h_L2,
        'amplitude_L4_relative_change_diagnostic':amp_L4,'stencil_L4_relative_change_diagnostic':h_L4,
        'heldout_frequency_relative_residual':hold,
        'exact_L4_column_relative_residual':qres,
        'zero_Q_column_global_scale_residuals':l4_zero_scales,
        'trace_eta_L2':tr,'exact_trace_target':target,'trace_Ward_relative_residual':tr_res,
        'exact_Q_column':qcol.tolist(),'extracted_L4_bilinear_column':bcols['h5.0e-04_e1.0e-04'].tolist(),
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
    Qsp,Q,zero_cols,targets=exact_objects()
    L2=[]; B4=[]; traces=[]
    for j in range(10):
        f=by[j]['fits']['h5.0e-04_e1.0e-04']
        T=np.array(f['L2'],float); L2.append(T); traces.append(trace_eta(T))
        B4.append(np.array(by[j]['extracted_L4_bilinear_column'],float))
    B4=np.column_stack(B4); traces=np.array(traces,float)
    b4_sym=f1.relnorm(B4,B4.T); b4_exact=f1.relnorm(B4,Q)
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
        'exact_zero_Q_columns':zero_cols,
        'L4_bilinear_symmetry_relative_residual':b4_sym,'L4_exact_Q_relative_residual':b4_exact,
        'L2_trace_vector':traces.tolist(),'exact_trace_target_vector':targets.tolist(),'L2_trace_Ward_vector_relative_residual':trace_vec,
        'L2_raw_frobenius_norm':float(np.linalg.norm(L2raw)),'L2_raw_singular_values':sv.tolist(),'L2_raw_rank_tolerance':tol,'L2_raw_rank':rank,
        'Einstein_nongauge_null_complement_dim':int(P.cols),'L2_image_rank_on_Einstein_nongauge_null_complement':prank,
        'L2_image_singular_values_on_Einstein_nongauge_null_complement':psv.tolist(),
        'claim_ceiling':'CONTROL-CORRECTED FRESH G3 ORIGIN K2 EXTRACTION ONLY; FULL CHARACTERISTICS/HYPERBOLICITY/GHOST/TREATMENT NOT ESTABLISHED; C6 SYMBOLIC UNFIXED; THEORY_ESTABLISHED_0'
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
