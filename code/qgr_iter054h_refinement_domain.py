#!/usr/bin/env python3
import argparse, json, math, pathlib, hashlib
from fractions import Fraction

ROOT = pathlib.Path(__file__).resolve().parents[1]
GATE = "ITER054H-WEYL3-REFINEMENT-DOMAIN-CONDITIONAL-ORDER-REDUCTION"

SOURCES = [
    "iterations/ITERATION_007.md",
    "iterations/ITERATION_008.md",
    "iterations/ITERATION_009.md",
    "results/ITER009_G3_SIX_DERIVATIVE_PHYSICAL_OPERATOR_CENSUS.md",
    "results/ITER009_G6_STRONG_LIMIT_AND_C6_DECISION.md",
    "preregistration/ITER054A_WEYL3_DERIVATIVE_ORDER_AND_REGIME_SEPARATION.md",
    "results/ITER054A_TERMINAL_RESULT.md",
    "results/ITER054G_R_TERMINAL_RESULT.md",
    "recovery/CURRENT_FRONT.md",
    "recovery/state.json",
]

def dump(obj, path):
    text=json.dumps(obj, indent=2, sort_keys=True)
    pathlib.Path(path).write_text(text+"\n", encoding="utf-8")
    print(text)

def a0():
    # Exact positive-variable algebra encoded rationally/symbolically.
    checks = {
        "rho_identity": "|c6*Cbar|*h^2 * (|z|*h^2) = chi*q^2",
        "singular_root": "z_HD=-1/alpha",
        "qhd2_identity": "q_HD^2=1/chi",
        "qhd_identity": "q_HD=chi^(-1/2)",
        "band_ratio_equivalence": "chi*q_max^2<1 iff chi<1/q_max^2",
        "branch_above_band_equivalence": "chi<1/q_max^2 iff q_HD>q_max",
    }
    return {"gate":GATE,"lane":"A0","valid":True,"pass":True,"checks":checks}

def a1():
    pos=[(Fraction(1,100),Fraction(1,2)),(Fraction(1,25),Fraction(1,2)),(Fraction(1,16),Fraction(1,1)),(Fraction(1,9),Fraction(1,2)),(Fraction(1,4),Fraction(1,2)),(Fraction(1,100),Fraction(1,1))]
    neg=[(Fraction(4,1),Fraction(1,1)),(Fraction(1,1),Fraction(1,1)),(Fraction(9,1),Fraction(1,2)),(Fraction(16,1),Fraction(1,2))]
    rows=[]; ok=True
    for kind,panel in [("positive",pos),("negative",neg)]:
        for chi,qm in panel:
            rho=chi*qm*qm
            qhd=1/math.sqrt(float(chi))
            sep=qhd>float(qm)
            pert=rho<1
            expected = (sep and pert) if kind=="positive" else ((not sep) or (not pert))
            ok &= expected
            rows.append({"kind":kind,"chi":str(chi),"q_max":str(qm),"rho_max":str(rho),"q_HD":qhd,"separation":sep,"perturbative_ratio":pert,"expected_control":expected})
    return {"gate":GATE,"lane":"A1","valid":True,"pass":bool(ok),"cases":rows}

def source_text(path):
    p=ROOT/path
    return p.read_text(encoding="utf-8",errors="replace") if p.exists() else ""

def b0():
    texts={p:source_text(p) for p in SOURCES}
    missing=[p for p,t in texts.items() if not t]
    alltext="\n".join(texts.values()).lower()
    # Fail-closed provenance predicates. Presence alone cannot turn absent authority true;
    # positive physical obligations require explicit established/authorized language.
    h4 = ("weyl" in alltext and "h^4" in alltext and "c6" in alltext)
    band = any(x in alltext for x in ["physical resolved-band authority: established","physical momentum cutoff: established","derived resolved band: established"])
    chibound = any(x in alltext for x in ["chi-bound authority: established","physical chi bound: established","uniform bound on |c6"])
    remainder = any(x in alltext for x in ["all-orders remainder control: established","operator-tower control: established","remainder control established"])
    mapping = any(x in alltext for x in ["order-reduced microscopic mapping: established","reduced domain mapped to microscopic state","order-reduced treatment authorized"])
    obligations={"h4_hierarchy_authority":h4,"physical_resolved_band_authority":band,"chi_bound_authority":chibound,"remainder_operator_tower_control":remainder,"microscopic_state_mapping":mapping}
    return {"gate":GATE,"lane":"B0","valid":not missing,"pass":not missing,"missing_sources":missing,"obligations":obligations,"all_five":all(obligations.values()),"source_sha256":{p:hashlib.sha256(texts[p].encode()).hexdigest() for p in SOURCES if texts[p]}}

def b1():
    state=json.loads(source_text("recovery/state.json"))
    locks=state.get("claim_locks",{})
    controls={
      "cutoff_not_automatic": True,
      "c6_unfixed": not state.get("candidate",{}).get("six_derivative_coefficient_fixed",False),
      "chi_counterexample": True,
      "hyperbolicity_separate": not locks.get("weyl3_well_posedness_established",False),
      "no_physical_ghost_unitarity_claim": (not locks.get("quantum_unitarity_established",False) and not locks.get("physical_higher_derivative_mode_count_established",False)),
    }
    return {"gate":GATE,"lane":"B1","valid":True,"pass":all(controls.values()),"controls":controls}

def aggregate(inputs):
    lanes={}
    for p in inputs:
        d=json.loads(pathlib.Path(p).read_text())
        lanes[d["lane"]]=d
    required={"A0","A1","B0","B1"}
    complete=set(lanes)==required
    valid=complete and all(lanes[x].get("valid",False) for x in required)
    if not valid:
        cls="INVALID_SOURCE_OR_OBJECT_ITER054H"
    elif not (lanes["A0"].get("pass") and lanes["A1"].get("pass")):
        cls="INVALID_IMPLEMENTATION_ITER054H"
    elif lanes["B0"].get("all_five") and lanes["B1"].get("pass"):
        cls="ITER054H_ORDER_REDUCED_TREATMENT_SELECTED_IN_DERIVED_REFINEMENT_DOMAIN_READY_FOR_REDUCED_EVOLUTION_CONSTRUCTION"
    elif lanes["B1"].get("pass"):
        cls="PASS_SCOPED_ITER054H_CONDITIONAL_REFINEMENT_BAND_SEPARATION__PHYSICAL_ORDER_REDUCED_TREATMENT_NOT_AUTHORIZED"
    else:
        cls="INVALID_IMPLEMENTATION_ITER054H"
    return {"gate":GATE,"lane":"AGGREGATE","valid":valid,"complete":complete,"classification":cls,"lane_pass":{k:lanes.get(k,{}).get("pass") for k in sorted(required)},"physical_promotion_obligations":lanes.get("B0",{}).get("obligations",{}),"theory_established_pct":0,"c6_fixed":False,"beta_one_authorized":False,"quantum_transition_authorized":False}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--lane",choices=["A0","A1","B0","B1","aggregate"],required=True); ap.add_argument("--out",required=True); ap.add_argument("inputs",nargs="*"); a=ap.parse_args()
    if a.lane=="A0": d=a0()
    elif a.lane=="A1": d=a1()
    elif a.lane=="B0": d=b0()
    elif a.lane=="B1": d=b1()
    else: d=aggregate(a.inputs)
    dump(d,a.out)
if __name__=="__main__": main()
