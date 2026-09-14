#!/usr/bin/env python3
"""Iter057F: extract the G3-origin Weyl3 degree-two block with full-EOM controls."""
import argparse
import itertools
import json
import math
from pathlib import Path

import numpy as np
import sympy as sp

import qgr_iter051c_d2n_near_null as d2n
import qgr_iter054c_local_metric_principal_symbol as core
import qgr_iter057a_null_cone_kernel_intersection as a57

GATE = "ITER057F-G3-ORIGIN-WEYL3-DEGREE2-BLOCK-EXTRACTION"
PREREG = "8df569f7414a9d634b72e54264b529245b356288"
PASS_CLASS = "PASS_SCOPED_ITER057F_G3_ORIGIN_WEYL3_K2_BLOCK_EXTRACTED_WITH_EXACT_K4_CONTROL"
INVALID_CLASS = "INVALID_ITER057F_FULL_EOM_EXTRACTION_OR_CONVENTION_CONTROL"
KAPPA = 0.08
KAPPA_Q = sp.Rational(2,25)
K = np.array([1.0,1.0,0.0,0.0])
K_EXACT = [sp.Integer(1),sp.Integer(1),sp.Integer(0),sp.Integer(0)]
EPS_PANEL = (2.0e-4,1.0e-4)
HD_PANEL = (1.0e-3,5.0e-4)
S_TRAIN = (0.0,1.0,2.0)
S_HOLD = 1.5
ETA = np.diag([-1.0,1.0,1.0,1.0])


def basis_np(idx):
    a,b=core.SYM_BASIS[idx]
    H=np.zeros((4,4),float); H[a,b]=1.0; H[b,a]=1.0
    if a==b: H[a,b]=1.0
    return H


def vec10(T):
    return np.array([float(T[a,b]) for a,b in core.SYM_BASIS],float)


def relnorm(A,B,floor=1e-10):
    return float(np.linalg.norm(np.asarray(A)-np.asarray(B))/max(np.linalg.norm(B),floor))


class G3WaveMetric:
    """Source G3/H0 metric in frozen (-,+,+,+) convention plus one cosine perturbation."""
    def __init__(self,basis_index,s,eps_sign_amp):
        self.H=basis_np(basis_index)
        self.s=float(s)
        self.eps=float(eps_sign_amp)

    def jets(self,x):
        x=np.asarray(x,float)
        # Frozen source potential Phi=(kappa/2)(x^2+y^2-2z^2), static in x0.
        phi=0.5*KAPPA*(x[1]**2+x[2]**2-2.0*x[3]**2)
        dphi=np.array([0.0,KAPPA*x[1],KAPPA*x[2],-2.0*KAPPA*x[3]],float)
        ddphi=np.zeros((4,4),float)
        ddphi[1,1]=KAPPA; ddphi[2,2]=KAPPA; ddphi[3,3]=-2.0*KAPPA

        g=np.diag([-1.0-2.0*phi,1.0-2.0*phi,1.0-2.0*phi,1.0-2.0*phi])
        dg=np.zeros((4,4,4),float)
        ddg=np.zeros((4,4,4,4),float)
        for c in range(4):
            for a in range(4):
                dg[c,a,a]=-2.0*dphi[c]
                for d in range(4):
                    ddg[c,d,a,a]=-2.0*ddphi[c,d]

        q=self.s*float(K@x)
        f=math.cos(q)
        df=-self.s*K*math.sin(q)
        ddf=-(self.s**2)*np.outer(K,K)*math.cos(q)
        g += self.eps*self.H*f
        for c in range(4):
            dg[c] += self.eps*self.H*df[c]
            for d in range(4):
                ddg[c,d] += self.eps*self.H*ddf[c,d]
        return g,dg,ddg


def stencil_offsets(h):
    pts={tuple([0.0]*4)}
    coeff=(-2,-1,0,1,2)
    for a in range(4):
        for b in range(4):
            for m in coeff:
                for n in coeff:
                    v=np.zeros(4); v[a]+=m*h; v[b]+=n*h
                    pts.add(tuple(float(z) for z in v))
    return [np.array(p,float) for p in pts]


def metric_control(metric,h):
    max_inv=0.0; min_abs_det=float('inf'); valid=True
    for x in stencil_offsets(h):
        g=metric.jets(x)[0]
        try:
            gi=np.linalg.inv(g)
            ev=np.linalg.eigvalsh(0.5*(g+g.T))
            det=float(np.linalg.det(g))
            inv=float(np.max(np.abs(g@gi-np.eye(4))))
            max_inv=max(max_inv,inv); min_abs_det=min(min_abs_det,abs(det))
            valid=valid and bool(np.sum(ev<0)==1 and np.sum(ev>0)==3 and det<0 and np.isfinite(det))
        except Exception:
            valid=False
    return valid,max_inv,min_abs_det


def full_response(basis_index,s,eps,hD):
    plus=G3WaveMetric(basis_index,s,+eps)
    minus=G3WaveMetric(basis_index,s,-eps)
    vp,ip,dp=metric_control(plus,hD); vm,im,dm=metric_control(minus,hD)
    Hp,_=d2n.assemble_minus5(plus,np.zeros(4),hD)
    Hm,_=d2n.assemble_minus5(minus,np.zeros(4),hD)
    R=(Hp-Hm)/(2.0*eps)
    return R,{
        'metric_valid':bool(vp and vm),
        'max_inverse_residual':max(ip,im),
        'min_abs_det':min(dp,dm),
    }


def fit_even_blocks(responses):
    R0=responses[0.0]; R1=responses[1.0]; R2=responses[2.0]
    A=R1-R0; B=R2-R0
    L4=(B-4.0*A)/12.0
    L2=A-L4
    return R0,L2,L4


def exact_q_column(j):
    H=sp.diag(1,1,-2)
    E=KAPPA_Q*H  # C_0i0j in the frozen (-,+,+,+) convention.
    W=core.tensor_to_bivector_operator(core.background_weyl_tensor(E))
    Q,_=core.q_matrix(W,K_EXACT)
    return np.array([float(sp.N(Q[i,j],30)) for i in range(10)],float)


def bilinear_column(T):
    return np.array([float(np.sum(basis_np(i)*T)) for i in range(10)],float)


def lane(j):
    fits={}; held={}; controls=[]
    for hD in HD_PANEL:
        for eps in EPS_PANEL:
            resp={}
            ctl_all=[]
            for s in (*S_TRAIN,S_HOLD):
                R,ctl=full_response(j,s,eps,hD)
                resp[float(s)]=R; ctl_all.append(ctl)
            L0,L2,L4=fit_even_blocks(resp)
            pred=L0+(S_HOLD**2)*L2+(S_HOLD**4)*L4
            hres=relnorm(resp[S_HOLD],pred)
            key=f'h{hD:.1e}_e{eps:.1e}'
            fits[key]={'L0':L0,'L2':L2,'L4':L4}
            held[key]=hres
            controls.extend(ctl_all)

    finest=fits['h5.0e-04_e1.0e-04']
    amp_hi=fits['h5.0e-04_e2.0e-04']
    stencil_hi=fits['h1.0e-03_e1.0e-04']
    amp_L2=relnorm(finest['L2'],amp_hi['L2'])
    amp_L4=relnorm(finest['L4'],amp_hi['L4'])
    h_L2=relnorm(finest['L2'],stencil_hi['L2'])
    h_L4=relnorm(finest['L4'],stencil_hi['L4'])
    hold=held['h5.0e-04_e1.0e-04']
    bcol=bilinear_column(finest['L4'])
    qcol=exact_q_column(j)
    qres=relnorm(bcol,qcol)
    source_valid=all(c['metric_valid'] and c['max_inverse_residual']<=2e-11 and c['min_abs_det']>1e-5 for c in controls)
    conv=bool(amp_L2<=5e-3 and amp_L4<=5e-3 and h_L2<=1e-2 and h_L4<=1e-2)
    hold_ok=bool(hold<=3e-3)
    q_ok=bool(qres<=2e-2)
    passed=bool(source_valid and conv and hold_ok and q_ok)

    serial={}
    for key,d in fits.items():
        serial[key]={name:mat.tolist() for name,mat in d.items()}
    return {
        'gate':GATE,'preregistration_commit':PREREG,'basis_index':j,
        'pass':passed,'controls_valid':passed,
        'source_metric_valid':source_valid,
        'amplitude_L2_relative_change':amp_L2,
        'amplitude_L4_relative_change':amp_L4,
        'stencil_L2_relative_change':h_L2,
        'stencil_L4_relative_change':h_L4,
        'heldout_frequency_relative_residual':hold,
        'exact_L4_column_relative_residual':qres,
        'exact_Q_column':qcol.tolist(),
        'extracted_L4_bilinear_column':bcol.tolist(),
        'fits':serial,
        'classification':'LANE_PASS' if passed else 'LANE_CONTROL_INVALID',
    }


def aggregate(inp):
    objs=[]; errors=[]
    for p in sorted(Path(inp).rglob('*.json')):
        try:
            o=json.loads(p.read_text())
            if 'basis_index' in o: objs.append(o)
        except Exception as ex: errors.append(f'{p}:{ex}')
    by={int(o['basis_index']):o for o in objs}
    complete=bool(len(by)==10 and not errors and set(by)==set(range(10)))
    lane_valid=bool(complete and all(by[j].get('pass') is True for j in range(10)))
    if not complete:
        return {'gate':GATE,'classification':INVALID_CLASS,'pass':False,'complete':False,'parse_errors':errors,'found':sorted(by)}

    L2=[]; L4=[]; B4=[]
    for j in range(10):
        f=by[j]['fits']['h5.0e-04_e1.0e-04']
        L2.append(np.array(f['L2'],float)); L4.append(np.array(f['L4'],float))
        B4.append(np.array(by[j]['extracted_L4_bilinear_column'],float))
    # B4 currently columns stored as list; transpose into [i,j].
    B4=np.column_stack(B4)
    H=sp.diag(1,1,-2); E=KAPPA_Q*H
    W=core.tensor_to_bivector_operator(core.background_weyl_tensor(E)); Qsp,_=core.q_matrix(W,K_EXACT)
    Q=np.array(Qsp.tolist(),dtype=float)
    b4_sym=relnorm(B4,B4.T)
    b4_exact=relnorm(B4,Q)

    # Raw output-coordinate matrix for L2.
    L2raw=np.column_stack([vec10(T) for T in L2])
    opnorm=float(np.linalg.norm(L2raw))
    gauge_res=[]
    for r in range(4):
        xi=np.zeros(4); xi[r]=1.0
        hg=np.zeros((4,4))
        for a in range(4):
            for b in range(4): hg[a,b]=K[a]*xi[b]+K[b]*xi[a]
        coeff=vec10(hg)
        gout=L2raw@coeff
        gauge_res.append(float(np.linalg.norm(gout)/max(opnorm,1e-10)))
    gauge_max=max(gauge_res)

    sv=np.linalg.svd(L2raw,compute_uv=False)
    tol=max(sv[0]*1e-8,1e-12) if len(sv) else 1e-12
    rank=int(np.sum(sv>tol))

    M2=a57.einstein_symbol_matrix(K_EXACT); Kg=a57.pure_gauge_columns(K_EXACT)
    ns,P,B=a57.physical_kernel_complement(M2,Kg)
    Pn=np.array(P.tolist(),dtype=float)
    phys_image=L2raw@Pn
    phys_sv=np.linalg.svd(phys_image,compute_uv=False)
    phys_tol=max(phys_sv[0]*1e-8,1e-12) if len(phys_sv) else 1e-12
    phys_rank=int(np.sum(phys_sv>phys_tol))

    trace_rows=[]
    for j,T in enumerate(L2):
        trace_rows.append(float(sum(ETA[a,b]*T[a,b] for a in range(4) for b in range(4))))

    aggregate_controls=bool(b4_sym<=2e-3 and b4_exact<=2e-2 and gauge_max<=5e-3)
    passed=bool(lane_valid and aggregate_controls)
    return {
        'gate':GATE,'preregistration_commit':PREREG,
        'classification':PASS_CLASS if passed else INVALID_CLASS,
        'pass':passed,'implementation_valid':passed,'complete':complete,'parse_errors':errors,
        'lane_pass_count':sum(by[j].get('pass') is True for j in range(10)),
        'L4_bilinear_symmetry_relative_residual':b4_sym,
        'L4_exact_Q_relative_residual':b4_exact,
        'L2_gauge_relative_residuals':gauge_res,'L2_gauge_max_relative_residual':gauge_max,
        'L2_raw_frobenius_norm':opnorm,'L2_raw_singular_values':sv.tolist(),'L2_raw_rank_tolerance':tol,'L2_raw_rank':rank,
        'L2_trace_by_input_basis':trace_rows,
        'Einstein_nongauge_null_complement_dim':int(P.cols),
        'L2_image_rank_on_Einstein_nongauge_null_complement':phys_rank,
        'L2_image_singular_values_on_Einstein_nongauge_null_complement':phys_sv.tolist(),
        'claim_ceiling':'ONE SOURCE-OWNED G3 ORIGIN + ONE NULL COVECTOR NUMERICAL K2 EXTRACTION ONLY; FULL CHARACTERISTICS/HYPERBOLICITY/GHOST/TREATMENT NOT ESTABLISHED; C6 SYMBOLIC UNFIXED; THEORY_ESTABLISHED_0',
    }


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--index',type=int); ap.add_argument('--aggregate'); ap.add_argument('--out',required=True); a=ap.parse_args()
    if a.aggregate:
        out=aggregate(a.aggregate)
    else:
        if a.index is None or not 0<=a.index<10: raise SystemExit('frozen basis index 0..9 required')
        out=lane(a.index)
    Path(a.out).parent.mkdir(parents=True,exist_ok=True); Path(a.out).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    compact={k:v for k,v in out.items() if k not in {'fits'}}
    print(json.dumps(compact,sort_keys=True))
    if a.aggregate and out.get('classification')==INVALID_CLASS: raise SystemExit(2)
    if not a.aggregate and out.get('pass') is not True: raise SystemExit(2)

if __name__=='__main__': main()
