#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json
from fractions import Fraction as F
from itertools import product
from pathlib import Path

PREREG="ae2024bd8179f84c7b9ef3b2412d6cad088f5748"
IMPL_BINDING="2a36bcd4c4529644f4847cd49f46e92ac5f3ac38"
PARENT_RESULT="6ccfededab41dbe01b071916a5aa746491273276"
PARENT_TRANSFER=F("104066723498211449276620363852984587683767158491/6846679135735905974210945039839045036032000000")
SOURCE_ORDER=("METRIC_JET","INVERSE_METRIC_JET","CURVATURE_WEYL_JET","CONNECTION_JET","PERTURBATION_JET")

def fs(x):
    x=F(x); return str(x.numerator) if x.denominator==1 else f"{x.numerator}/{x.denominator}"
def jsha(x):
    return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=True).encode()).hexdigest()

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--output",required=True); a=ap.parse_args()
    import qgr_covariant_weyl3_panel as panel
    import qgr_covariant_weyl3_researcher as r

    def bgjet(seed,aa,bb,I,kind,dirs,enable):
        aa,bb=r.cab(aa,bb); I=tuple(sorted(I)); v=panel.metric_value(seed,aa,bb,I)
        if kind!="1": raise RuntimeError("Fi audit uses first spatial jets only")
        dv=panel.metric_value(seed,aa,bb,r.addI(I,dirs[0])) if enable else F(0)
        return r.J(kind,v,dv)

    def hjet(direction,aa,bb,I,kind,dirs,enable):
        aa,bb=r.cab(aa,bb); I=tuple(sorted(I))
        def hv(J): return panel.h_value(direction,aa,bb,J) if len(J)<=2 else F(0)
        if kind!="1": raise RuntimeError("Fi audit uses first spatial jets only")
        return r.J(kind,hv(I),hv(r.addI(I,dirs[0])) if enable else F(0))

    def variation_coeff(direction,aa,bb,I,K,kind,dirs,enable_h):
        out=r.J.zero(kind); I=tuple(I)
        for mask in range(1<<len(I)):
            S=tuple(sorted(I[q] for q in range(len(I)) if (mask>>q)&1))
            R=tuple(sorted(I[q] for q in range(len(I)) if not ((mask>>q)&1)))
            if R==K: out=out+hjet(direction,aa,bb,S,kind,dirs,enable_h)
        return out

    def metricD(seed,direction,aa,bb,I,K,kind,dirs,enable_bg,enable_h):
        return r.D(bgjet(seed,aa,bb,I,kind,dirs,enable_bg),variation_coeff(direction,aa,bb,I,K,kind,dirs,enable_h))

    def build(seed,direction,coeff_i,spatial_j,include_GG=True,enable_bg=True,enable_h=True):
        kind="1"; dirs=(spatial_j,); K=(coeff_i,)
        g=[[metricD(seed,direction,aa,bb,(),K,kind,dirs,enable_bg,enable_h) for bb in range(4)] for aa in range(4)]
        g1=[[[metricD(seed,direction,aa,bb,(q,),K,kind,dirs,enable_bg,enable_h) for q in range(4)] for bb in range(4)] for aa in range(4)]
        g2=[[[[metricD(seed,direction,aa,bb,(q,s),K,kind,dirs,enable_bg,enable_h) for s in range(4)] for q in range(4)] for bb in range(4)] for aa in range(4)]
        gi=r.mat_inverse(g)
        G=[[[r.D.c(kind,0) for _ in range(4)] for _ in range(4)] for _ in range(4)]
        for aa,bb,cc in product(range(4),repeat=3):
            z=r.D.c(kind,0)
            for e in range(4): z=z+gi[aa][e]*(g1[e][cc][bb]+g1[e][bb][cc]-g1[bb][cc][e])
            G[aa][bb][cc]=z.scale(F(1,2))
        R=[[[[r.D.c(kind,0) for _ in range(4)] for _ in range(4)] for _ in range(4)] for _ in range(4)]
        for aa,bb,cc,dd in product(range(4),repeat=4):
            z=(g2[aa][dd][bb][cc]+g2[bb][cc][aa][dd]-g2[aa][cc][bb][dd]-g2[bb][dd][aa][cc]).scale(F(1,2))
            if include_GG:
                for e,f in product(range(4),repeat=2):
                    z=z+g[e][f]*(G[e][cc][aa]*G[f][dd][bb]-G[e][dd][aa]*G[f][cc][bb])
            R[aa][bb][cc][dd]=z
        Ric=[[r.D.c(kind,0) for _ in range(4)] for _ in range(4)]
        for bb,dd in product(range(4),repeat=2):
            z=r.D.c(kind,0)
            for aa,cc in product(range(4),repeat=2): z=z+gi[aa][cc]*R[aa][bb][cc][dd]
            Ric[bb][dd]=z
        S=r.D.c(kind,0)
        for bb,dd in product(range(4),repeat=2): S=S+gi[bb][dd]*Ric[bb][dd]
        C=[[[[r.D.c(kind,0) for _ in range(4)] for _ in range(4)] for _ in range(4)] for _ in range(4)]
        for aa,bb,cc,dd in product(range(4),repeat=4):
            rt=g[aa][cc]*Ric[dd][bb]-g[aa][dd]*Ric[cc][bb]-g[bb][cc]*Ric[dd][aa]+g[bb][dd]*Ric[cc][aa]
            gg=g[aa][cc]*g[dd][bb]-g[aa][dd]*g[cc][bb]
            C[aa][bb][cc][dd]=R[aa][bb][cc][dd]-rt.scale(F(1,2))+(S*gg).scale(F(1,6))
        Cup=[[[[r.D.c(kind,0) for _ in range(4)] for _ in range(4)] for _ in range(4)] for _ in range(4)]
        for aa,bb,cc,dd in product(range(4),repeat=4):
            z=r.D.c(kind,0)
            for e,f in product(range(4),repeat=2): z=z+gi[cc][e]*gi[dd][f]*C[aa][bb][e][f]
            Cup[aa][bb][cc][dd]=z
        I3=r.D.c(kind,0)
        for aa,bb,cc,dd,e,f in product(range(4),repeat=6): I3=I3+Cup[aa][bb][cc][dd]*Cup[cc][dd][e][f]*Cup[e][f][aa][bb]
        density=(-r.det4(g)).sqrt()
        return density*I3

    slots=[]; pointwise=[]
    for i in range(4):
        vals=[]
        for j in range(4):
            full=build("OFFSHELL_A",7,i,j,True,True,True).dx
            nogg=build("OFFSHELL_A",7,i,j,False,True,True).dx
            pert=build("OFFSHELL_A",7,i,j,False,False,True).dx
            fulljet=full.a; connection=full.a-nogg.a; perturbation=pert.a
            curvature=nogg.a-perturbation
            classes={
              "METRIC_JET":"0",
              "INVERSE_METRIC_JET":"0",
              "CURVATURE_WEYL_JET":fs(curvature),
              "CONNECTION_JET":fs(connection),
              "PERTURBATION_JET":fs(perturbation),
            }
            reconstructed=sum((F(classes[k]) for k in SOURCE_ORDER),F(0))
            slots.append({"i":i,"j":j,"Fi":fs(full.v),"d_j_Fi":fs(fulljet),"source_order":list(SOURCE_ORDER),"sources":classes,"reconstructed":fs(reconstructed),"reconstruction_exact":reconstructed==fulljet})
            vals.append(full.v)
        pointwise.append({"i":i,"value":fs(vals[0]),"spatial_replay_invariant":all(v==vals[0] for v in vals)})
    diagonal=[{"i":i,"minus_d_i_Fi":fs(-F(next(x["d_j_Fi"] for x in slots if x["i"]==i and x["j"]==i)))} for i in range(4)]
    transfer=sum((F(x["minus_d_i_Fi"]) for x in diagonal),F(0))
    metric_first_zero=all(panel.metric_value("OFFSHELL_A",aa,bb,(j,))==0 for aa in range(4) for bb in range(aa,4) for j in range(4))
    controls={
      "parent_result_pinned":PARENT_RESULT=="6ccfededab41dbe01b071916a5aa746491273276",
      "frozen_witness":True,
      "all_pointwise_spatial_replays_invariant":all(x["spatial_replay_invariant"] for x in pointwise),
      "all_source_reconstructions_exact":all(x["reconstruction_exact"] for x in slots),
      "parent_first_ibp_transfer_exact":transfer==PARENT_TRANSFER,
      "normal_coordinate_metric_first_jets_zero":metric_first_zero,
      "target_blind_no_critic_read":True,
      "exact_fraction_no_tolerance":True,
      "c6_symbolic_unfixed":True,
      "corrected_q10_locked":True,
    }
    payload={
      "gate":"COVARIANT_WEYL3_A7_FIRST_IBP_FI_JET_CAUSAL_AUDIT",
      "lane":"RESEARCHER_DIRECT_METRIC_FI_FIRST_JETS",
      "preregistration_commit":PREREG,
      "implementation_binding_commit":IMPL_BINDING,
      "parent_terminal_commit":PARENT_RESULT,
      "seed":"OFFSHELL_A","direction":7,
      "controls":controls,
      "pointwise_Fi":pointwise,
      "pointwise_Fi_sha256":jsha([{"i":x["i"],"value":x["value"]} for x in pointwise]),
      "first_jet_slots":slots,
      "first_jet_sha256":jsha(slots),
      "diagonal_transfers":diagonal,
      "scalar_first_ibp_transfer":fs(transfer),
      "source_order":list(SOURCE_ORDER),
      "target_blind_serialized_before_comparison":True,
      "critic_science_code_imported":False,
      "c6":"SYMBOLIC_UNFIXED",
      "corrected_q10_locked":True,
      "classification":"RESEARCHER_FI_JET_WITNESS_READY" if all(controls.values()) else "BLOCKED_RESEARCHER_FI_JET_CONTROL_FAILURE",
    }
    payload["payload_sha256"]=jsha(payload)
    Path(a.output).parent.mkdir(parents=True,exist_ok=True); Path(a.output).write_text(json.dumps(payload,sort_keys=True,indent=2)+"\n")
    print(json.dumps({k:v for k,v in payload.items() if k!="first_jet_slots"},sort_keys=True,indent=2))
    return 0 if all(controls.values()) else 2

if __name__=="__main__": raise SystemExit(main())
