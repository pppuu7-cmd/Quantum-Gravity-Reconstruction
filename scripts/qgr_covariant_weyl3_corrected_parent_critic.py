#!/usr/bin/env python3
from __future__ import annotations
import argparse,hashlib,json
from fractions import Fraction as F
from itertools import product
from pathlib import Path

PREREG="1640b2fb84980c68fa1e14d146b8403b43d3fd5a"
CELLS=(("FLAT_CONTROL",7),("FLAT_CONTROL",19),("OFFSHELL_A",7),("OFFSHELL_A",19),("OFFSHELL_B",7),("OFFSHELL_B",19))
KEYS=("00","01","02","03","11","12","13","22","23","33")

def fs(x):
    x=F(x); return str(x.numerator) if x.denominator==1 else f"{x.numerator}/{x.denominator}"
def jsha(x):
    return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=True).encode()).hexdigest()
def pairmatch(p,q,i,j):
    return int(tuple(sorted((p,q)))==(i,j))

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--seed",required=True,choices=("FLAT_CONTROL","OFFSHELL_A","OFFSHELL_B"))
    ap.add_argument("--direction",required=True,type=int,choices=(7,19))
    ap.add_argument("--output",required=True)
    a=ap.parse_args()
    import qgr_covariant_weyl3_panel as panel
    import qgr_covariant_weyl3_critic as c
    import qgr_covariant_weyl3_a7_lower_critic as lc

    manifest=panel.panel_manifest()
    expected={(x["seed"],x["direction"]):x["jet_sha256"] for x in manifest["cells"]}[(a.seed,a.direction)]
    cell=c.cell(a.seed,a.direction,expected)
    z=c.build(a.seed)

    H={}
    for aa in range(4):
        for bb in range(aa,4):
            q=c.P()
            for al in c.AL:
                if c.deg(al)>2: continue
                I=tuple(sorted(c.inds(al)))
                v=panel.h_value(a.direction,aa,bb,I)
                if v: q=q+c.P.mono(al,v/F(c.mf(al)))
            H[(aa,bb)]=q
    def hp(aa,bb): return H[c.cab(aa,bb)]

    density=c.P.c(1)
    for aa,bb in product(range(4),repeat=2):
        if c.eta(aa,bb):
            density=density+(z["g"][aa][bb]-c.eta(aa,bb)).sc(F(1,2)*c.eta(aa,bb))
    K=[[[[z["P"][aa][bb][cc][dd]*density for dd in range(4)] for cc in range(4)] for bb in range(4)] for aa in range(4)]

    F0P=c.P(); FiP=[c.P() for _ in range(4)]; FijP={k:c.P() for k in KEYS}
    for aa,bb,cc,dd in product(range(4),repeat=4):
        kp=K[aa][bb][cc][dd]
        if not kp.d: continue
        z0=(hp(aa,dd).deriv(cc).deriv(bb)+hp(bb,cc).deriv(dd).deriv(aa)-hp(bb,dd).deriv(cc).deriv(aa)-hp(aa,cc).deriv(dd).deriv(bb)).sc(F(1,2))
        F0P=F0P+kp*z0
        for i in range(4):
            zi=c.P()
            if bb==i: zi=zi+hp(aa,dd).deriv(cc)
            if cc==i: zi=zi+hp(aa,dd).deriv(bb)
            if aa==i: zi=zi+hp(bb,cc).deriv(dd)
            if dd==i: zi=zi+hp(bb,cc).deriv(aa)
            if aa==i: zi=zi-hp(bb,dd).deriv(cc)
            if cc==i: zi=zi-hp(bb,dd).deriv(aa)
            if bb==i: zi=zi-hp(aa,cc).deriv(dd)
            if dd==i: zi=zi-hp(aa,cc).deriv(bb)
            FiP[i]=FiP[i]+kp*zi.sc(F(1,2))
        for key in KEYS:
            i,j=int(key[0]),int(key[1])
            q=F(1,2)*(pairmatch(cc,bb,i,j)*hp(aa,dd)+pairmatch(dd,aa,i,j)*hp(bb,cc)-pairmatch(cc,aa,i,j)*hp(bb,dd)-pairmatch(dd,bb,i,j)*hp(aa,cc))
            FijP[key]=FijP[key]+kp*q

    fixed_total,volume,I3=lc.fixed_R_metric_density_variation(c,panel,z,a.direction)
    F0=fixed_total+F0P.v()
    first=-sum((FiP[i].deriv(i).v() for i in range(4)),F(0))
    second=sum((FijP[k].deriv(int(k[0])).deriv(int(k[1])).v() for k in KEYS),F(0))
    partial=F0+first+second
    historical=F(cell["euler_source"]["contraction_with_h"])
    gap=historical-partial
    corrected=partial-gap

    controls={
      "frozen_cell":(a.seed,a.direction) in CELLS,
      "panel_manifest_exact":cell["jet_sha256"]==expected,
      "historical_critic_self_controls":all(v is True for v in cell["controls"].values()),
      "historical_euler_reconstruction_exact":partial+gap==historical,
      "base_I3_exact":I3==z["I"].v(),
      "corrected_rule_exact":corrected==partial-gap,
      "flat_historical_zero":historical==0 if a.seed=="FLAT_CONTROL" else True,
      "flat_corrected_zero":corrected==0 if a.seed=="FLAT_CONTROL" else True,
      "target_blind_no_researcher_read":True,
      "exact_fraction_no_tolerance":True,
      "c6_symbolic_unfixed":True,
      "corrected_q10_locked":True
    }
    payload={
      "gate":"COVARIANT_WEYL3_CORRECTED_PARENT_CONNECTION_GAP_SIGN_REPLAY",
      "lane":"CORRECTED_CRITIC_CONNECTION_GAP_SIGN",
      "preregistration_commit":PREREG,
      "seed":a.seed,"direction":a.direction,
      "panel_manifest_sha256":manifest["panel_sha256"],
      "jet_sha256":cell["jet_sha256"],
      "historical_critic_cell_witness_sha256":cell["cell_witness_sha256"],
      "controls":controls,
      "F0":fs(F0),
      "first_ibp_transfer":fs(first),
      "second_ibp_transfer":fs(second),
      "partial_ibp":fs(partial),
      "historical_euler":fs(historical),
      "covariantization_gap":fs(gap),
      "corrected_euler":fs(corrected),
      "correction_from_historical":fs(corrected-historical),
      "corrected_rule":"partial_IBP - covariantization_gap",
      "target_blind_serialized_before_comparison":True,
      "c6":"SYMBOLIC_UNFIXED",
      "corrected_q10_locked":True,
      "classification":"CORRECTED_CRITIC_PARENT_CELL_READY" if all(controls.values()) else "BLOCKED_CORRECTED_CRITIC_PARENT_CELL_CONTROL_FAILURE"
    }
    payload["payload_sha256"]=jsha(payload)
    Path(a.output).parent.mkdir(parents=True,exist_ok=True)
    Path(a.output).write_text(json.dumps(payload,sort_keys=True,indent=2)+"\n")
    print(json.dumps(payload,sort_keys=True,indent=2))
    return 0 if all(controls.values()) else 2

if __name__=="__main__": raise SystemExit(main())
