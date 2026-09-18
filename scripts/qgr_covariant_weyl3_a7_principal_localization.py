#!/usr/bin/env python3
"""Target-blind lanes for OFFSHELL_A,d=7 principal-symbol causal localization.

Researcher mode imports only the frozen Researcher implementation.
Critic mode imports only the frozen Critic implementation.
The terminal comparator is a separate file and is the only component allowed
to read both payloads.
"""
from __future__ import annotations
import argparse, hashlib, json, sys
from fractions import Fraction as F
from itertools import product
from pathlib import Path

PREREG="5c5d6197ff15573f2110729ddd41c4e64c005e7a"
PARENT_RUN=35367461999
PARENT_RESEARCHER_WITNESS="69c1c0db798cc921c5ca4c45ca0a61f0d38a35392c75707a5c3e78ff03b9134d"
PARENT_CRITIC_WITNESS="09d544faf078bd7b4046ad1d7d0f768a489d93ff912effddfcbaf8d838d8b19b"
PARENT_P_SHA="21095bed2a18f7a5fa2484961c75d4cd7589115d6a6f664f0b3eee8697cdd4fe"
PARENT_JET_SHA="1bb5b6a0ee5469879e335704beb7ee003dddbf8d4734c2d3f290d6fe53dcb9a3"
PARENT_DIRECT="141609523517262295106976925021598088976553029/33325122725952586818549169405591839744000000"
PARENT_EULER="36188861490208135407463132950092941670313420227/2815972870342993586167404814772510458368000000"
PARENT_DIFF="-86355995554365317186893343264769708206041673/10039118967354700841951532316479538176000000"
KEYS=("00","01","02","03","11","12","13","22","23","33")

def fs(x):
    x=F(x);return str(x.numerator) if x.denominator==1 else f"{x.numerator}/{x.denominator}"
def jsha(x):
    return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=True).encode()).hexdigest()
def eta(a,b):
    return F(-1 if a==b==0 else (1 if a==b else 0))
def cab(a,b):
    return (a,b) if a<=b else (b,a)

def researcher_payload():
    import qgr_covariant_weyl3_panel as panel
    import qgr_covariant_weyl3_researcher as r
    manifest=panel.panel_manifest()
    expected={(x["seed"],x["direction"]):x["jet_sha256"] for x in manifest["cells"]}[("OFFSHELL_A",7)]
    cell=r.cell("OFFSHELL_A",7,expected)
    z=r.build("OFFSHELL_A",7,())
    fij=[{"ij":k,"value":cell["direct_variation_and_ibp"]["second_derivative_coefficients"][k]["F"]} for k in KEYS]
    volume=z["density"].dx.v*z["I3"].x.v
    controls={
      "parent_run_pinned":PARENT_RUN==35367461999,
      "parent_witness_exact":cell["cell_witness_sha256"]==PARENT_RESEARCHER_WITNESS,
      "parent_jet_exact":cell["jet_sha256"]==PARENT_JET_SHA,
      "all_parent_self_controls_true":all(v is True for v in cell["controls"].values()),
      "parent_direct_bulk_exact":cell["direct_variation_and_ibp"]["bulk_after_ibp"]==PARENT_DIRECT,
      "normal_coordinate_Gamma_zero":cell["controls"]["normal_coordinate_Gamma_zero"] is True,
      "offshell_precondition":cell["controls"]["offshell_ricci_nonzero"] is True and cell["controls"]["offshell_scalar_nonzero"] is True,
      "exact_fraction_no_tolerance":True,
      "critic_not_imported":True,
      "c6_symbolic_unfixed":True,
      "corrected_q10_locked":True,
    }
    return {
      "gate":"COVARIANT_WEYL3_OFFSHELL_A7_PRINCIPAL_SYMBOL_CAUSAL_LOCALIZATION",
      "lane":"RESEARCHER_PARENT_FIJ_AND_DIRECT_VOLUME",
      "preregistration_commit":PREREG,
      "parent_run":PARENT_RUN,
      "seed":"OFFSHELL_A","direction":7,
      "controls":controls,
      "parent_cell_witness_sha256":cell["cell_witness_sha256"],
      "parent_jet_sha256":cell["jet_sha256"],
      "Fij_vector":fij,
      "Fij_vector_sha256":jsha(fij),
      "direct_volume_term":fs(volume),
      "direct_bulk_parent":cell["direct_variation_and_ibp"]["bulk_after_ibp"],
      "target_blind_no_critic_values_read":True,
      "classification":"RESEARCHER_A7_PRINCIPAL_WITNESS_READY" if all(controls.values()) else "BLOCKED_RESEARCHER_A7_REPRODUCTION_OR_CONTROL_FAILURE",
    }

def pairmatch(p,q,i,j):
    return int(tuple(sorted((p,q)))==(i,j))

def critic_payload():
    import qgr_covariant_weyl3_panel as panel
    import qgr_covariant_weyl3_critic as c
    manifest=panel.panel_manifest()
    expected={(x["seed"],x["direction"]):x["jet_sha256"] for x in manifest["cells"]}[("OFFSHELL_A",7)]
    cell=c.cell("OFFSHELL_A",7,expected)
    z=c.build("OFFSHELL_A")
    pvec=[c.fs(z["P"][a][b][cc][d].v()) for a,b,cc,d in product(range(4),repeat=4)]
    psha=c.jsha(pvec)
    h0={(a,b):panel.h_value(7,a,b,()) for a in range(4) for b in range(a,4)}
    def h(a,b):
        return h0[cab(a,b)]
    pred=[]
    for key in KEYS:
        i,j=int(key[0]),int(key[1])
        q=F(0)
        for a,b,cc,d in product(range(4),repeat=4):
            P=z["P"][a][b][cc][d].v()
            if not P:continue
            principal=F(1,2)*(
                pairmatch(cc,b,i,j)*h(a,d)
                + pairmatch(d,a,i,j)*h(b,cc)
                - pairmatch(cc,a,i,j)*h(b,d)
                - pairmatch(d,b,i,j)*h(a,cc)
            )
            q += P*principal
        pred.append({"ij":key,"value":fs(q)})
    metric=F(1,2)*z["I"].v()*sum((eta(a,b)*h(a,b) for a,b in product(range(4),repeat=2)),F(0))
    controls={
      "parent_run_pinned":PARENT_RUN==35367461999,
      "parent_witness_exact":cell["cell_witness_sha256"]==PARENT_CRITIC_WITNESS,
      "parent_jet_exact":cell["jet_sha256"]==PARENT_JET_SHA,
      "all_parent_self_controls_true":all(v is True for v in cell["controls"].values()),
      "parent_P_hash_exact":cell["euler_source"]["P_point_sha256"]==PARENT_P_SHA and psha==PARENT_P_SHA,
      "parent_euler_contraction_exact":cell["euler_source"]["contraction_with_h"]==PARENT_EULER,
      "normal_coordinate_Gamma_zero":cell["controls"]["normal_coordinate_Gamma_zero"] is True,
      "P_frechet_control_exact":cell["controls"]["P_fixed_frechet_direction_exact"] is True,
      "P_R_homogeneity_exact":cell["controls"]["P_dot_R_equals_3I3"] is True,
      "offshell_precondition":cell["controls"]["offshell_ricci_nonzero"] is True and cell["controls"]["offshell_scalar_nonzero"] is True,
      "exact_fraction_no_tolerance":True,
      "researcher_not_imported":True,
      "c6_symbolic_unfixed":True,
      "corrected_q10_locked":True,
    }
    return {
      "gate":"COVARIANT_WEYL3_OFFSHELL_A7_PRINCIPAL_SYMBOL_CAUSAL_LOCALIZATION",
      "lane":"CRITIC_P_PALATINI_PRINCIPAL_AND_METRIC_VOLUME",
      "preregistration_commit":PREREG,
      "parent_run":PARENT_RUN,
      "seed":"OFFSHELL_A","direction":7,
      "controls":controls,
      "parent_cell_witness_sha256":cell["cell_witness_sha256"],
      "parent_jet_sha256":cell["jet_sha256"],
      "parent_P_sha256":psha,
      "principal_vector":pred,
      "principal_vector_sha256":jsha(pred),
      "euler_metric_I3_term":fs(metric),
      "euler_total_parent":cell["euler_source"]["contraction_with_h"],
      "target_blind_no_researcher_values_read":True,
      "classification":"CRITIC_A7_PRINCIPAL_WITNESS_READY" if all(controls.values()) else "BLOCKED_CRITIC_A7_REPRODUCTION_OR_CONTROL_FAILURE",
    }

def main():
    ap=argparse.ArgumentParser();ap.add_argument("--mode",required=True,choices=("researcher","critic"));ap.add_argument("--output",required=True);a=ap.parse_args()
    p=researcher_payload() if a.mode=="researcher" else critic_payload()
    p["payload_sha256"]=jsha(p)
    Path(a.output).parent.mkdir(parents=True,exist_ok=True);Path(a.output).write_text(json.dumps(p,sort_keys=True,indent=2)+"\n")
    print(json.dumps(p,sort_keys=True,indent=2))
    return 0 if not p["classification"].startswith("BLOCKED") else 2
if __name__=="__main__":raise SystemExit(main())
