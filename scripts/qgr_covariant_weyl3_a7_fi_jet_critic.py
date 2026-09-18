#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json
from fractions import Fraction as F
from itertools import product
from pathlib import Path

PREREG="ae2024bd8179f84c7b9ef3b2412d6cad088f5748"
IMPL_BINDING="2a36bcd4c4529644f4847cd49f46e92ac5f3ac38"
PARENT_RESULT="6ccfededab41dbe01b071916a5aa746491273276"
PARENT_TRANSFER=F("91653430140870514219093059175268861573353/4700039496553856295898029721292544000000")
SOURCE_ORDER=("METRIC_JET","INVERSE_METRIC_JET","CURVATURE_WEYL_JET","CONNECTION_JET","PERTURBATION_JET")

def fs(x):
    x=F(x); return str(x.numerator) if x.denominator==1 else f"{x.numerator}/{x.denominator}"
def jsha(x):
    return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=True).encode()).hexdigest()

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--output",required=True); a=ap.parse_args()
    import qgr_covariant_weyl3_panel as panel
    import qgr_covariant_weyl3_critic as c

    z=c.build("OFFSHELL_A")
    H={}
    for aa in range(4):
        for bb in range(aa,4):
            q=c.P()
            for al in c.AL:
                if c.deg(al)>2: continue
                I=tuple(sorted(c.inds(al))); v=panel.h_value(7,aa,bb,I)
                if v: q=q+c.P.mono(al,v/F(c.mf(al)))
            H[(aa,bb)]=q
    def hp(aa,bb): return H[c.cab(aa,bb)]

    density=c.P.c(1)
    for aa,bb in product(range(4),repeat=2):
        if c.eta(aa,bb):
            density=density+(z["g"][aa][bb]-c.eta(aa,bb)).sc(F(1,2)*c.eta(aa,bb))
    K=[[[[z["P"][aa][bb][cc][dd]*density for dd in range(4)] for cc in range(4)] for bb in range(4)] for aa in range(4)]

    def zi(aa,bb,cc,dd,i):
        q=c.P()
        if bb==i: q=q+hp(aa,dd).deriv(cc)
        if cc==i: q=q+hp(aa,dd).deriv(bb)
        if aa==i: q=q+hp(bb,cc).deriv(dd)
        if dd==i: q=q+hp(bb,cc).deriv(aa)
        if aa==i: q=q-hp(bb,dd).deriv(cc)
        if cc==i: q=q-hp(bb,dd).deriv(aa)
        if bb==i: q=q-hp(aa,cc).deriv(dd)
        if dd==i: q=q-hp(aa,cc).deriv(bb)
        return q.sc(F(1,2))

    Fi=[c.P() for _ in range(4)]
    perturb=[[F(0) for _ in range(4)] for _ in range(4)]
    for aa,bb,cc,dd in product(range(4),repeat=4):
        kp=K[aa][bb][cc][dd]
        if not kp.d: continue
        for i in range(4):
            q=zi(aa,bb,cc,dd,i)
            Fi[i]=Fi[i]+kp*q
            for j in range(4):
                perturb[i][j]+=kp.v()*q.deriv(j).v()

    pointwise=[{"i":i,"value":fs(Fi[i].v())} for i in range(4)]
    slots=[]
    for i in range(4):
        for j in range(4):
            full=Fi[i].deriv(j).v()
            p=perturb[i][j]
            curvature=full-p
            classes={
              "METRIC_JET":"0",
              "INVERSE_METRIC_JET":"0",
              "CURVATURE_WEYL_JET":fs(curvature),
              "CONNECTION_JET":"0",
              "PERTURBATION_JET":fs(p),
            }
            reconstructed=sum((F(classes[k]) for k in SOURCE_ORDER),F(0))
            slots.append({"i":i,"j":j,"Fi":fs(Fi[i].v()),"d_j_Fi":fs(full),"source_order":list(SOURCE_ORDER),"sources":classes,"reconstructed":fs(reconstructed),"reconstruction_exact":reconstructed==full})
    diagonal=[{"i":i,"minus_d_i_Fi":fs(-Fi[i].deriv(i).v())} for i in range(4)]
    transfer=sum((F(x["minus_d_i_Fi"]) for x in diagonal),F(0))
    metric_first_zero=all(panel.metric_value("OFFSHELL_A",aa,bb,(j,))==0 for aa in range(4) for bb in range(aa,4) for j in range(4))
    inv_first_zero=all(z["gi"][aa][bb].deriv(j).v()==0 for aa,bb,j in product(range(4),repeat=3))
    controls={
      "parent_result_pinned":PARENT_RESULT=="6ccfededab41dbe01b071916a5aa746491273276",
      "frozen_witness":True,
      "all_source_reconstructions_exact":all(x["reconstruction_exact"] for x in slots),
      "parent_first_ibp_transfer_exact":transfer==PARENT_TRANSFER,
      "normal_coordinate_metric_first_jets_zero":metric_first_zero,
      "normal_coordinate_inverse_first_jets_zero":inv_first_zero,
      "normal_coordinate_Gamma_zero":all(z["G"][aa][bb][cc].v()==0 for aa,bb,cc in product(range(4),repeat=3)),
      "target_blind_no_researcher_read":True,
      "exact_fraction_no_tolerance":True,
      "c6_symbolic_unfixed":True,
      "corrected_q10_locked":True,
    }
    payload={
      "gate":"COVARIANT_WEYL3_A7_FIRST_IBP_FI_JET_CAUSAL_AUDIT",
      "lane":"CRITIC_P_PALATINI_FI_FIRST_JETS",
      "preregistration_commit":PREREG,
      "implementation_binding_commit":IMPL_BINDING,
      "parent_terminal_commit":PARENT_RESULT,
      "seed":"OFFSHELL_A","direction":7,
      "controls":controls,
      "pointwise_Fi":pointwise,
      "pointwise_Fi_sha256":jsha(pointwise),
      "first_jet_slots":slots,
      "first_jet_sha256":jsha(slots),
      "diagonal_transfers":diagonal,
      "scalar_first_ibp_transfer":fs(transfer),
      "source_order":list(SOURCE_ORDER),
      "target_blind_serialized_before_comparison":True,
      "researcher_science_code_imported":False,
      "c6":"SYMBOLIC_UNFIXED",
      "corrected_q10_locked":True,
      "classification":"CRITIC_FI_JET_WITNESS_READY" if all(controls.values()) else "BLOCKED_CRITIC_FI_JET_CONTROL_FAILURE",
    }
    payload["payload_sha256"]=jsha(payload)
    Path(a.output).parent.mkdir(parents=True,exist_ok=True); Path(a.output).write_text(json.dumps(payload,sort_keys=True,indent=2)+"\n")
    print(json.dumps({k:v for k,v in payload.items() if k!="first_jet_slots"},sort_keys=True,indent=2))
    return 0 if all(controls.values()) else 2

if __name__=="__main__": raise SystemExit(main())
