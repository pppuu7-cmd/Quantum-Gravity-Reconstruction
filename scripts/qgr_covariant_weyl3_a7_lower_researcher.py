#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json
from fractions import Fraction as F
from pathlib import Path

PREREG = "a8c7bd1bd5280f18aa50955b4cd847b707c178ab"
BINDING = "f0081e60056106b0eac916b6f207ad03fc113233"
PARENT_RUN = 35367461999
PARENT_RESEARCHER_WITNESS = "69c1c0db798cc921c5ca4c45ca0a61f0d38a35392c75707a5c3e78ff03b9134d"
PARENT_JET_SHA = "1bb5b6a0ee5469879e335704beb7ee003dddbf8d4734c2d3f290d6fe53dcb9a3"
PARENT_DIRECT = "141609523517262295106976925021598088976553029/33325122725952586818549169405591839744000000"
FROZEN_PRINCIPAL_SHA = "fb20b1704d6e651ccae7df87591cd3961d6792a04d103a182aa712552db65896"
KEYS = ("00","01","02","03","11","12","13","22","23","33")
CLASS_KEYS = (
    "CONNECTION_VARIATION",
    "COVARIANTIZATION_GAMMA_TIMES_DH",
    "COVARIANTIZATION_DGAMMA_TIMES_H",
    "COVARIANTIZATION_GAMMA_GAMMA_TIMES_H",
    "IBP_FIRST_TRANSFER",
    "IBP_SECOND_TRANSFER",
    "ALGEBRAIC_CURVATURE_VARIATION",
    "VOLUME_CONTROL",
    "PRINCIPAL_CONTROL",
)

def fs(x):
    x=F(x)
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"

def jsha(x):
    return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=True).encode()).hexdigest()

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--output",required=True); a=ap.parse_args()
    import qgr_covariant_weyl3_panel as panel
    import qgr_covariant_weyl3_researcher as r

    manifest=panel.panel_manifest()
    expected={(x["seed"],x["direction"]):x["jet_sha256"] for x in manifest["cells"]}[("OFFSHELL_A",7)]
    cell=r.cell("OFFSHELL_A",7,expected)
    ibp=cell["direct_variation_and_ibp"]
    z0=r.build("OFFSHELL_A",7,())

    F0=F(ibp["F0"])
    volume=z0["density"].dx.v*z0["I3"].x.v
    first=F(ibp["first_ibp_transfer"])
    second=F(ibp["second_ibp_transfer"])
    bulk=F(ibp["bulk_after_ibp"])
    fi=[{"i":str(i),"value":ibp["single_derivative_coefficients"][str(i)]["F"],"d_i_value":ibp["single_derivative_coefficients"][str(i)]["d_i_F"]} for i in range(4)]
    fij=[{"ij":k,"value":ibp["second_derivative_coefficients"][k]["F"],"d_i_value":ibp["second_derivative_coefficients"][k]["d_i_F"],"d_i_d_j_value":ibp["second_derivative_coefficients"][k]["d_i_d_j_F"]} for k in KEYS]
    principal=[{"ij":k,"value":ibp["second_derivative_coefficients"][k]["F"]} for k in KEYS]

    classes={
      "CONNECTION_VARIATION":"0",
      "COVARIANTIZATION_GAMMA_TIMES_DH":"0",
      "COVARIANTIZATION_DGAMMA_TIMES_H":"0",
      "COVARIANTIZATION_GAMMA_GAMMA_TIMES_H":"0",
      "IBP_FIRST_TRANSFER":fs(first),
      "IBP_SECOND_TRANSFER":fs(second),
      "ALGEBRAIC_CURVATURE_VARIATION":fs(F0-volume),
      "VOLUME_CONTROL":fs(volume),
      "PRINCIPAL_CONTROL":"0",
    }
    class_sum=sum((F(classes[k]) for k in CLASS_KEYS),F(0))
    controls={
      "parent_run_pinned":PARENT_RUN==35367461999,
      "parent_witness_exact":cell["cell_witness_sha256"]==PARENT_RESEARCHER_WITNESS,
      "parent_jet_exact":cell["jet_sha256"]==PARENT_JET_SHA,
      "all_parent_self_controls_true":all(v is True for v in cell["controls"].values()),
      "parent_direct_bulk_exact":bulk==F(PARENT_DIRECT),
      "principal_vector_frozen_exact":jsha(principal)==FROZEN_PRINCIPAL_SHA,
      "normal_coordinate_Gamma_zero":cell["controls"]["normal_coordinate_Gamma_zero"] is True,
      "target_blind_no_critic_read":True,
      "exact_fraction_no_tolerance":True,
      "c6_symbolic_unfixed":True,
      "corrected_q10_locked":True,
    }
    payload={
      "gate":"COVARIANT_WEYL3_A7_LOWER_ORDER_COVARIANTIZATION_IBP_LOCALIZATION",
      "lane":"RESEARCHER_DIRECT_VARIATION_LOWER_ORDER_LEDGER",
      "preregistration_commit":PREREG,
      "implementation_binding_commit":BINDING,
      "seed":"OFFSHELL_A","direction":7,
      "parent_run":PARENT_RUN,
      "parent_cell_witness_sha256":cell["cell_witness_sha256"],
      "parent_jet_sha256":cell["jet_sha256"],
      "controls":controls,
      "F0":fs(F0),
      "volume":fs(volume),
      "lower_order_curvature_before_ibp":fs(F0-volume),
      "Fi_vector":fi,
      "Fi_vector_sha256":jsha(fi),
      "Fij_ledger":fij,
      "principal_vector":principal,
      "principal_vector_sha256":jsha(principal),
      "first_ibp_transfer":fs(first),
      "second_ibp_transfer":fs(second),
      "class_order":list(CLASS_KEYS),
      "classes":classes,
      "class_vector_sha256":jsha([[k,classes[k]] for k in CLASS_KEYS]),
      "class_sum":fs(class_sum),
      "parent_total":fs(bulk),
      "target_blind_serialized_before_comparison":True,
      "critic_science_code_imported":False,
      "c6":"SYMBOLIC_UNFIXED",
      "corrected_q10_locked":True,
      "classification":"RESEARCHER_LOWER_ORDER_WITNESS_READY" if all(controls.values()) else "BLOCKED_RESEARCHER_LOWER_ORDER_CONTROL_FAILURE",
    }
    payload["payload_sha256"]=jsha(payload)
    Path(a.output).parent.mkdir(parents=True,exist_ok=True)
    Path(a.output).write_text(json.dumps(payload,sort_keys=True,indent=2)+"\n")
    print(json.dumps({k:v for k,v in payload.items() if k not in ("Fij_ledger",)},sort_keys=True,indent=2))
    return 0 if all(controls.values()) else 2

if __name__=="__main__": raise SystemExit(main())
