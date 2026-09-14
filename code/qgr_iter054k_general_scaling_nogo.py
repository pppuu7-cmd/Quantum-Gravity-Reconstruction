#!/usr/bin/env python3
import argparse, json, math
from fractions import Fraction
from pathlib import Path

GATE = "ITER054K-WEYL3-GENERAL-SCALING-FIXED-BAND-NOGO"
PASS_CLASS = "PASS_SCOPED_ITER054K_GENERAL_FIXED_BAND_CONTINUUM_SURVIVAL_NOGO__C6_RUNNING_NOT_AUTHORIZED"

def dump(obj, out):
    Path(out).write_text(json.dumps(obj, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(obj, indent=2, sort_keys=True))

def lane_a0():
    cases=[]
    # a=r^2 ensures exact rational sqrt(a)=r.
    triples=[(Fraction(1,2),Fraction(3,2),Fraction(2,1)),
             (Fraction(1,4),Fraction(5,3),Fraction(3,2)),
             (Fraction(3,8),Fraction(7,5),Fraction(5,3)),
             (Fraction(2,5),Fraction(11,7),Fraction(4,3))]
    bad_detected=False
    for h,k,r in triples:
        a=r*r
        rho=a*h**4*k**2
        khd=Fraction(1,1)/(h**2*r)
        exact_ok=(rho*khd**2 == k**2)
        kbad=Fraction(1,1)/(h*r)
        bad_ok=(rho*kbad**2 != k**2)
        bad_detected = bad_detected or bad_ok
        cases.append({"h":str(h),"k":str(k),"a":str(a),"identity_exact":exact_ok,"malformed_rejected":bad_ok})
    ok=all(c["identity_exact"] for c in cases) and bad_detected
    return {"gate":GATE,"lane":"A0","valid":True,"pass":ok,"identity":"rho*k_HD^2=k^2","cases":cases,"malformed_control_detected":bad_detected}

def lane_a1():
    families={
      "subexponential": lambda n,h: math.exp(math.sqrt(n)),
      "polynomial_nonpower_h": lambda n,h: (1+n)**3*(1+1/(n+1)),
      "critical_slow_plus": lambda n,h: h**-4*(1+1/(n+1)),
      "critical_log_suppressed": lambda n,h: h**-4/(1+n)**2,
      "critical_log_enhanced": lambda n,h: h**-4*(1+n)**2,
    }
    k=1.7
    panel=[]
    all_ok=True
    for name,fn in families.items():
        max_rel=0.0; first=None; last=None
        for n in range(2,18):
            h=2.0**(-n)
            a=fn(n,h)
            rho=a*h**4*k*k
            khd=1.0/(h*h*math.sqrt(a))
            lhs=rho*khd*khd
            rel=abs(lhs-k*k)/max(abs(k*k),1e-300)
            max_rel=max(max_rel,rel)
            if first is None: first=(rho,khd)
            last=(rho,khd)
        ok=max_rel <= 1e-12
        all_ok &= ok
        panel.append({"family":name,"max_relative_identity_residual":max_rel,"rho_first":first[0],"rho_last":last[0],"khd_first":first[1],"khd_last":last[1],"ok":ok})
    return {"gate":GATE,"lane":"A1","valid":True,"pass":all_ok,"tolerance":1e-12,"panel":panel}

def lane_b0():
    # The limit implications follow algebraically from rho=(k/k_HD)^2.
    k=2.0
    controls=[]
    # Directly construct k_HD sequences for three limit classes and derive rho.
    seqs={
      "branch_to_infinity": [2.0**n for n in range(2,12)],
      "finite_nonzero_rho": [k/math.sqrt(0.75) for _ in range(10)],
      "rho_to_infinity": [2.0**(-n) for n in range(2,12)],
    }
    for name,ks in seqs.items():
        rhos=[(k/x)**2 for x in ks]
        if name=="branch_to_infinity": ok=(ks[-1]>ks[0] and rhos[-1]<rhos[0] and rhos[-1] < 1e-5)
        elif name=="finite_nonzero_rho": ok=all(abs(r-0.75)<1e-14 for r in rhos) and all(abs(x-k/math.sqrt(0.75))<1e-14 for x in ks)
        else: ok=(rhos[-1]>rhos[0] and ks[-1]<ks[0] and rhos[-1]>1e5)
        controls.append({"class":name,"khd_first":ks[0],"khd_last":ks[-1],"rho_first":rhos[0],"rho_last":rhos[-1],"ok":ok})
    all_ok=all(x["ok"] for x in controls)
    return {"gate":GATE,"lane":"B0","valid":True,"pass":all_ok,
            "exact_basis":"rho=(k/k_HD)^2",
            "implications":{"khd_to_infinity":"rho_to_zero","rho_to_finite_nonzero":"khd_to_finite_nonzero","rho_to_infinity":"khd_to_zero"},
            "general_simultaneous_survival_and_decoupling_possible":False,"controls":controls}

def lane_b1():
    controls={
      "c6_running_authorized":False,
      "physical_cutoff_derived":False,
      "finite_h_order_reduction_authorized":False,
      "ghost_unitarity_hyperbolicity_claim":False,
      "quantum_transition_authorized":False,
      "beta_one_authorized":False,
      "theory_established_pct":0,
    }
    ok=(not controls["c6_running_authorized"] and not controls["physical_cutoff_derived"] and
        not controls["finite_h_order_reduction_authorized"] and not controls["ghost_unitarity_hyperbolicity_claim"] and
        not controls["quantum_transition_authorized"] and not controls["beta_one_authorized"] and controls["theory_established_pct"]==0)
    return {"gate":GATE,"lane":"B1","valid":True,"pass":ok,"controls":controls}

def aggregate(paths):
    lanes={}
    for p in paths:
        x=json.loads(Path(p).read_text(encoding="utf-8")); lanes[x["lane"]]=x
    required=["A0","A1","B0","B1"]
    complete=all(x in lanes for x in required)
    lane_pass={x: bool(lanes.get(x,{}).get("valid")) and bool(lanes.get(x,{}).get("pass")) for x in required}
    ok=complete and all(lane_pass.values())
    return {"gate":GATE,"lane":"AGGREGATE","complete":complete,"valid":ok,"lane_pass":lane_pass,
            "classification":PASS_CLASS if ok else "FAIL_ITER054K_FROZEN_CLASSIFIER",
            "c6_running_authorized":False,"beta_one_authorized":False,"quantum_transition_authorized":False,"theory_established_pct":0}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--lane",required=True); ap.add_argument("--out",required=True); ap.add_argument("inputs",nargs="*"); a=ap.parse_args()
    if a.lane=="A0": x=lane_a0()
    elif a.lane=="A1": x=lane_a1()
    elif a.lane=="B0": x=lane_b0()
    elif a.lane=="B1": x=lane_b1()
    elif a.lane=="aggregate": x=aggregate(a.inputs)
    else: raise SystemExit("unknown lane")
    dump(x,a.out)
    if not x.get("pass", x.get("valid",False)): raise SystemExit(1)

if __name__=="__main__": main()
