#!/usr/bin/env python3
import argparse,json,os,math
import qgr_iter053_qd_quadrature_conditioning as qd

ORDERS=(5,6,7,8)


def rel(a,b,floor=1e-30):
    return float(abs(a-b)/max(abs(a),abs(b),floor))


def run(stream,index):
    metric,pert,mseed,pseed=qd.lane_objects(stream,index)
    vals={str(n):qd.direct_integral(metric,pert,n,qd.SUPPORT) for n in ORDERS}
    numbers=[vals[str(n)]['value'] for n in ORDERS]
    controls=all(vals[str(n)]['signature_valid'] and vals[str(n)]['max_inverse_residual']<=3e-11 and math.isfinite(vals[str(n)]['value']) for n in ORDERS)
    changes={
      '5_to_6_relative':rel(numbers[0],numbers[1]),
      '6_to_7_relative':rel(numbers[1],numbers[2]),
      '7_to_8_relative':rel(numbers[2],numbers[3]),
      '7_to_8_absolute':float(abs(numbers[3]-numbers[2]))
    }
    if stream=='B':
        converged=bool(controls and abs(numbers[2])<=5e-8 and abs(numbers[3])<=5e-8 and changes['7_to_8_absolute']<=1e-9)
    else:
        converged=bool(controls and changes['6_to_7_relative']<=2e-3 and changes['7_to_8_relative']<=5e-4 and abs(numbers[3])>=1e-10)
    return {
      'gate':'ITER053-QD2-SUPPORT-DIRECT-QUADRATURE-CONVERGENCE','stream':stream,'index':index,
      'metric_seed':mseed,'perturbation_seed':pseed,'support_radius':qd.SUPPORT,
      'orders':vals,'changes':changes,'control_valid':bool(controls),'converged':converged,
      'classification':'LANE_CONVERGED' if converged else 'LANE_NOT_CONVERGED'
    }


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--stream',choices=['A','B','C'],required=True); ap.add_argument('--index',type=int,required=True); ap.add_argument('--out',required=True); a=ap.parse_args()
    lim={'A':4,'B':2,'C':2}[a.stream]
    if not 0<=a.index<lim: raise SystemExit('index out of range')
    out=run(a.stream,a.index)
    os.makedirs(os.path.dirname(a.out) or '.',exist_ok=True)
    with open(a.out,'w') as f: json.dump(out,f,sort_keys=True,indent=2)
    print(json.dumps(out,sort_keys=True))
    if not out['control_valid']: raise SystemExit(3)
    if not out['converged']: raise SystemExit(2)

if __name__=='__main__': main()
