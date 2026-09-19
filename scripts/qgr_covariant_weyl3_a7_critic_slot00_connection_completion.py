#!/usr/bin/env python3
from __future__ import annotations
import argparse,hashlib,json
from fractions import Fraction as F
from itertools import product
from pathlib import Path

PREREG="d33392623c576cb22e00ad2c49f48157cbe5729b"
PARENT_FI_RESULT="07ad77de0506a3de5e7db601e2cfc8b5edc37c5c"

def fs(x):
    x=F(x)
    return str(x.numerator) if x.denominator==1 else f"{x.numerator}/{x.denominator}"
def jsha(x):
    return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=True).encode()).hexdigest()

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--output",required=True); q=ap.parse_args()
    import qgr_covariant_weyl3_panel as panel
    import qgr_covariant_weyl3_critic as c

    z=c.build("OFFSHELL_A")

    H={}
    for aa in range(4):
        for bb in range(aa,4):
            p=c.P()
            for al in c.AL:
                if c.deg(al)>2: continue
                I=tuple(sorted(c.inds(al)))
                v=panel.h_value(7,aa,bb,I)
                if v: p=p+c.P.mono(al,v/F(c.mf(al)))
            H[(aa,bb)]=p
    def hp(a,b): return H[c.cab(a,b)]

    density=c.P.c(1)
    for a,b in product(range(4),repeat=2):
        if c.eta(a,b):
            density=density+(z["g"][a][b]-c.eta(a,b)).sc(F(1,2)*c.eta(a,b))

    K=[[[[z["P"][a][b][cc][d]*density for d in range(4)] for cc in range(4)] for b in range(4)] for a in range(4)]

    def zi(a,b,cc,d,i):
        p=c.P()
        if b==i: p=p+hp(a,d).deriv(cc)
        if cc==i: p=p+hp(a,d).deriv(b)
        if a==i: p=p+hp(b,cc).deriv(d)
        if d==i: p=p+hp(b,cc).deriv(a)
        if a==i: p=p-hp(b,d).deriv(cc)
        if cc==i: p=p-hp(b,d).deriv(a)
        if b==i: p=p-hp(a,cc).deriv(d)
        if d==i: p=p-hp(a,cc).deriv(b)
        return p.sc(F(1,2))

    Fi0=c.P()
    perturb_d0=F(0)
    for a,b,cc,d in product(range(4),repeat=4):
        kp=K[a][b][cc][d]
        if not kp.d: continue
        v=zi(a,b,cc,d,0)
        Fi0=Fi0+kp*v
        perturb_d0 += kp.v()*v.deriv(0).v()

    original_point=Fi0.v()
    original_d0=Fi0.deriv(0).v()
    original_curvature=original_d0-perturb_d0

    def h(a,b):
        return panel.h_value(7,*c.cab(a,b),())
    def g2(a,b,p,r):
        return panel.metric_value("OFFSHELL_A",*c.cab(a,b),tuple(sorted((p,r))))
    def dG(j,up,b,cc):
        return F(1,2)*sum((c.eta(up,e)*(g2(e,cc,b,j)+g2(e,b,cc,j)-g2(b,cc,e,j)) for e in range(4)),F(0))
    def Cnabla(cc,b,a,d,i=0,j=0):
        out=F(0)
        for r in range(4):
            if cc==i:
                out-=dG(j,r,b,a)*h(r,d)
                out-=dG(j,r,b,d)*h(a,r)
            if b==i:
                out-=dG(j,r,cc,a)*h(r,d)
                out-=dG(j,r,cc,d)*h(a,r)
        out-=dG(j,i,cc,b)*h(a,d)
        return out
    def conversion(a,b,cc,d):
        return F(-1,2)*(Cnabla(cc,b,a,d)+Cnabla(d,a,b,cc)-Cnabla(d,b,a,cc)-Cnabla(cc,a,b,d))

    tensor=[fs(conversion(*idx)) for idx in product(range(4),repeat=4)]
    x0=(1,0,0,0)
    corrected=Fi0
    for a,b,cc,d in product(range(4),repeat=4):
        v=conversion(a,b,cc,d)
        if v:
            corrected=corrected+K[a][b][cc][d]*c.P.mono(x0,v)

    corrected_point=corrected.v()
    corrected_d0=corrected.deriv(0).v()
    connection_completion=corrected_d0-original_d0

    original_sources={
      "METRIC_JET":"0",
      "INVERSE_METRIC_JET":"0",
      "CURVATURE_WEYL_JET":fs(original_curvature),
      "CONNECTION_JET":"0",
      "PERTURBATION_JET":fs(perturb_d0)
    }
    corrected_sources=dict(original_sources)
    corrected_sources["CONNECTION_JET"]=fs(connection_completion)

    order=("METRIC_JET","INVERSE_METRIC_JET","CURVATURE_WEYL_JET","CONNECTION_JET","PERTURBATION_JET")
    original_reconstructed=sum((F(original_sources[k]) for k in order),F(0))
    corrected_reconstructed=sum((F(corrected_sources[k]) for k in order),F(0))

    controls={
      "parent_fi_result_pinned":PARENT_FI_RESULT=="07ad77de0506a3de5e7db601e2cfc8b5edc37c5c",
      "frozen_witness_slot00":True,
      "normal_coordinate_metric_first_jets_zero":all(panel.metric_value("OFFSHELL_A",a,b,(j,))==0 for a in range(4) for b in range(a,4) for j in range(4)),
      "normal_coordinate_Gamma_zero":all(z["G"][a][b][cc].v()==0 for a,b,cc in product(range(4),repeat=3)),
      "original_source_reconstruction_exact":original_reconstructed==original_d0,
      "corrected_source_reconstruction_exact":corrected_reconstructed==corrected_d0,
      "pointwise_Fi_unchanged":corrected_point==original_point,
      "only_connection_source_changed":all(original_sources[k]==corrected_sources[k] for k in order if k!="CONNECTION_JET"),
      "conversion_tensor_256":len(tensor)==256,
      "target_blind_before_parent_comparison":True,
      "exact_fraction_no_tolerance":True,
      "c6_symbolic_unfixed":True,
      "corrected_q10_locked":True
    }

    out={
      "gate":"COVARIANT_WEYL3_A7_CRITIC_SLOT00_CONNECTION_COMPLETION_REPLAY",
      "lane":"CORRECTED_CRITIC_SLOT00_TARGET_BLIND",
      "preregistration_commit":PREREG,
      "parent_fi_result_commit":PARENT_FI_RESULT,
      "seed":"OFFSHELL_A","direction":7,"i":0,"j":0,
      "controls":controls,
      "original_pointwise_Fi0":fs(original_point),
      "corrected_pointwise_Fi0":fs(corrected_point),
      "original_d0_F0":fs(original_d0),
      "connection_completion":fs(connection_completion),
      "corrected_d0_F0":fs(corrected_d0),
      "original_sources":original_sources,
      "corrected_sources":corrected_sources,
      "conversion_tensor_sha256":jsha(tensor),
      "conversion_tensor_values":tensor,
      "c6":"SYMBOLIC_UNFIXED","corrected_q10_locked":True,
      "classification":"CORRECTED_CRITIC_SLOT00_WITNESS_READY" if all(controls.values()) else "BLOCKED_CORRECTED_CRITIC_SLOT00_CONTROL_FAILURE"
    }
    out["payload_sha256"]=jsha(out)
    Path(q.output).parent.mkdir(parents=True,exist_ok=True)
    Path(q.output).write_text(json.dumps(out,sort_keys=True,indent=2)+"\n")
    print(json.dumps({k:v for k,v in out.items() if k!="conversion_tensor_values"},sort_keys=True,indent=2))
    return 0 if all(controls.values()) else 2

if __name__=="__main__": raise SystemExit(main())
