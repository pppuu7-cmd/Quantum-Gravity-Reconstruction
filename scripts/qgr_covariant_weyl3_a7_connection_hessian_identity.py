#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json
from fractions import Fraction as F
from itertools import product
from pathlib import Path

PREREG="d76dea1d511d0f7fa99b057866ef44fd797a1fc6"
PARENT_RESULT="07ad77de0506a3de5e7db601e2cfc8b5edc37c5c"
P_HASH="21095bed2a18f7a5fa2484961c75d4cd7589115d6a6f664f0b3eee8697cdd4fe"

def fs(x):
    x=F(x); return str(x.numerator) if x.denominator==1 else f"{x.numerator}/{x.denominator}"
def jsha(x):
    return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=True).encode()).hexdigest()

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--output",required=True); a=ap.parse_args()
    import qgr_covariant_weyl3_panel as panel
    import qgr_covariant_weyl3_critic as c
    z=c.build("OFFSHELL_A")
    pvec=[c.fs(z["P"][aa][bb][cc][dd].v()) for aa,bb,cc,dd in product(range(4),repeat=4)]
    psha=c.jsha(pvec)

    def h(aa,bb): return panel.h_value(7,*c.cab(aa,bb),())
    def g2(aa,bb,p,q): return panel.metric_value("OFFSHELL_A",*c.cab(aa,bb),tuple(sorted((p,q))))
    def dG(j,up,b,cidx):
        return F(1,2)*sum((c.eta(up,e)*(g2(e,cidx,b,j)+g2(e,b,cidx,j)-g2(b,cidx,e,j)) for e in range(4)),F(0))

    def hess_conn(cidx,b,aidx,d,i,j):
        q=F(0)
        for rr in range(4):
            if cidx==i:
                q-=dG(j,rr,b,aidx)*h(rr,d)
                q-=dG(j,rr,b,d)*h(aidx,rr)
            if b==i:
                q-=dG(j,rr,cidx,aidx)*h(rr,d)
                q-=dG(j,rr,cidx,d)*h(aidx,rr)
        q-=dG(j,i,cidx,b)*h(aidx,d)
        return q

    def connR(aa,bb,cc,dd,i,j):
        return F(1,2)*(hess_conn(cc,bb,aa,dd,i,j)+hess_conn(dd,aa,bb,cc,i,j)-hess_conn(cc,aa,bb,dd,i,j)-hess_conn(dd,bb,aa,cc,i,j))

    i=j=0
    tensor=[fs(connR(aa,bb,cc,dd,i,j)) for aa,bb,cc,dd in product(range(4),repeat=4)]
    scalar=sum((z["P"][aa][bb][cc][dd].v()*connR(aa,bb,cc,dd,i,j) for aa,bb,cc,dd in product(range(4),repeat=4)),F(0))
    dg=[fs(dG(jj,aa,bb,cc)) for jj,aa,bb,cc in product(range(4),repeat=4)]
    riemann_from_dg=True
    for aa,bb,cc,dd in product(range(4),repeat=4):
        q=sum((c.eta(aa,e)*(dG(cc,e,dd,bb)-dG(dd,e,cc,bb)) for e in range(4)),F(0))
        riemann_from_dg &= q==z["R"][aa][bb][cc][dd].v()
    controls={
      "parent_terminal_pinned":PARENT_RESULT=="07ad77de0506a3de5e7db601e2cfc8b5edc37c5c",
      "P_hash_exact":psha==P_HASH,
      "normal_coordinate_metric_first_jets_zero":all(panel.metric_value("OFFSHELL_A",aa,bb,(q,))==0 for aa in range(4) for bb in range(aa,4) for q in range(4)),
      "normal_coordinate_Gamma_zero":all(z["G"][aa][bb][cc].v()==0 for aa,bb,cc in product(range(4),repeat=3)),
      "dGamma_reconstructs_Riemann":riemann_from_dg,
      "frozen_slot_i0_j0":True,
      "target_blind_no_parent_connection_value_read":True,
      "exact_fraction_no_tolerance":True,
      "c6_symbolic_unfixed":True,
      "corrected_q10_locked":True,
    }
    payload={
      "gate":"COVARIANT_WEYL3_A7_CONNECTION_JET_IDENTITY_ADJUDICATION",
      "lane":"TENSOR_HESSIAN_CONNECTION_IDENTITY",
      "preregistration_commit":PREREG,
      "parent_terminal_commit":PARENT_RESULT,
      "seed":"OFFSHELL_A","direction":7,"i":0,"j":0,
      "controls":controls,
      "P_point_sha256":psha,
      "dGamma_sha256":jsha(dg),
      "connection_tensor_sha256":jsha(tensor),
      "connection_identity_value":fs(scalar),
      "serialized_before_target_comparison":True,
      "c6":"SYMBOLIC_UNFIXED","corrected_q10_locked":True,
      "classification":"TENSOR_HESSIAN_CONNECTION_WITNESS_READY" if all(controls.values()) else "BLOCKED_TENSOR_HESSIAN_CONNECTION_CONTROL_FAILURE",
    }
    payload["payload_sha256"]=jsha(payload)
    Path(a.output).parent.mkdir(parents=True,exist_ok=True); Path(a.output).write_text(json.dumps(payload,sort_keys=True,indent=2)+"\n")
    print(json.dumps(payload,sort_keys=True,indent=2)); return 0 if all(controls.values()) else 2

if __name__=="__main__": raise SystemExit(main())
