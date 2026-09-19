#!/usr/bin/env python3
from __future__ import annotations
import argparse,hashlib,json
from fractions import Fraction as F
from pathlib import Path

PREREG="c5d6c8ac75cd7fd19de9ca9081b539ba3300ec57"
FROZEN_RESEARCHER_PAYLOAD="f2d71d9089db72fcc82c8b6f9b120219fd10fc270179dc5a08515d8d0bea79e0"
SOURCE_ORDER=("METRIC_JET","INVERSE_METRIC_JET","CURVATURE_WEYL_JET","CONNECTION_JET","PERTURBATION_JET")

def fs(x):
    x=F(x); return str(x.numerator) if x.denominator==1 else f"{x.numerator}/{x.denominator}"
def jsha(x):
    return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=True).encode()).hexdigest()

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--corrected",required=True); ap.add_argument("--researcher",required=True); ap.add_argument("--output",required=True)
    q=ap.parse_args()
    C=json.loads(Path(q.corrected).read_text())
    R=json.loads(Path(q.researcher).read_text())
    controls={
      "preregistration_exact":C.get("preregistration_commit")==PREREG,
      "corrected_ready":C.get("classification")=="CORRECTED_CRITIC_FULL_FIRST_JET_READY" and all(v is True for v in C.get("controls",{}).values()),
      "researcher_reference_ready":R.get("classification")=="RESEARCHER_FI_JET_WITNESS_READY" and all(v is True for v in R.get("controls",{}).values()),
      "researcher_payload_reproduces_frozen_parent":R.get("payload_sha256")==FROZEN_RESEARCHER_PAYLOAD,
      "witness_exact":(C.get("seed"),C.get("direction"),R.get("seed"),R.get("direction"))==("OFFSHELL_A",7,"OFFSHELL_A",7),
      "source_order_exact":tuple(C.get("source_order",[]))==SOURCE_ORDER and tuple(R.get("source_order",[]))==SOURCE_ORDER
    }
    cpoint={x["i"]:F(x["corrected"]) for x in C.get("pointwise_Fi",[])}
    rpoint={x["i"]:F(x["value"]) for x in R.get("pointwise_Fi",[])}
    pointwise_match=len(cpoint)==len(rpoint)==4 and all(cpoint[i]==rpoint[i] for i in range(4))

    cslots={(x["i"],x["j"]):x for x in C.get("first_jet_slots",[])}
    rslots={(x["i"],x["j"]):x for x in R.get("first_jet_slots",[])}
    first_slot=None; first_source=None
    all_slots=len(cslots)==len(rslots)==16
    all_sources=all_slots
    if all_slots:
      for i in range(4):
        for j in range(4):
          cs,rs=cslots[(i,j)],rslots[(i,j)]
          if F(cs["corrected_d_j_Fi"])!=F(rs["d_j_Fi"]) and first_slot is None:
            first_slot={"i":i,"j":j,"corrected":cs["corrected_d_j_Fi"],"researcher":rs["d_j_Fi"],"difference":fs(F(cs["corrected_d_j_Fi"])-F(rs["d_j_Fi"]))}
          for k in SOURCE_ORDER:
            cv=F(cs["corrected_sources"][k]); rv=F(rs["sources"][k])
            if cv!=rv:
              all_sources=False
              if first_source is None:
                first_source={"i":i,"j":j,"source_class":k,"corrected":fs(cv),"researcher":fs(rv),"difference":fs(cv-rv)}
    all_slots_match=all_slots and first_slot is None

    cdiag={x["i"]:F(x["minus_d_i_Fi"]) for x in C.get("diagonal_transfers",[])}
    rdiag={x["i"]:F(x["minus_d_i_Fi"]) for x in R.get("diagonal_transfers",[])}
    diagonal_match=len(cdiag)==len(rdiag)==4 and all(cdiag[i]==rdiag[i] for i in range(4))
    ctransfer=F(C.get("scalar_first_ibp_transfer","0")); rtransfer=F(R.get("scalar_first_ibp_transfer","0"))
    transfer_match=ctransfer==rtransfer

    if not all(controls.values()):
      cls="BLOCKED_EXECUTION_OR_PROVENANCE"
    elif pointwise_match and all_slots_match and all_sources and diagonal_match and transfer_match:
      cls="CORRECTED_CRITIC_FULL_FIRST_JET_EXACT_MATCH"
    else:
      cls="CORRECTED_CRITIC_RESIDUAL_FIRST_JET_DIVERGENCE"

    out={
      "gate":"COVARIANT_WEYL3_A7_CRITIC_FULL_FIRST_JET_CONNECTION_COMPLETION_REPLAY",
      "preregistration_commit":PREREG,
      "classification":cls,
      "controls":controls,
      "all_4_pointwise_match":pointwise_match,
      "all_16_first_jet_slots_match":all_slots_match,
      "all_16_source_ledgers_match":all_sources,
      "all_4_diagonal_transfers_match":diagonal_match,
      "scalar_first_ibp_transfer_match":transfer_match,
      "corrected_scalar_first_ibp_transfer":fs(ctransfer),
      "researcher_scalar_first_ibp_transfer":fs(rtransfer),
      "transfer_difference":fs(ctransfer-rtransfer),
      "first_residual_slot":first_slot,
      "first_residual_source_class":first_source,
      "corrected_first_jet_sha256":C.get("first_jet_sha256"),
      "corrected_payload_sha256":C.get("payload_sha256"),
      "researcher_payload_sha256":R.get("payload_sha256"),
      "parent_reclassification_authorized":False,
      "c6":"SYMBOLIC_UNFIXED","corrected_q10_locked":True,"theory_established_pct":0
    }
    out["terminal_payload_sha256"]=jsha(out)
    Path(q.output).parent.mkdir(parents=True,exist_ok=True)
    Path(q.output).write_text(json.dumps(out,sort_keys=True,indent=2)+"\n")
    print(json.dumps(out,sort_keys=True,indent=2))
    return 2 if cls=="BLOCKED_EXECUTION_OR_PROVENANCE" else 0
if __name__=="__main__": raise SystemExit(main())
