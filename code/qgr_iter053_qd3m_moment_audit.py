#!/usr/bin/env python3
import json, math, os
import numpy as np
from scipy.special import roots_jacobi, beta
import qgr_iter053_qd3_gauss_jacobi_bulk_pilot as qd3

A=0.24
ATOL=5e-14
RTOL=5e-14


def analytic_moment(k):
    if k % 2: return 0.0
    return float(beta(k/2.0 + 0.5, 5.0))


def rel(a,b,floor=1e-300):
    return float(abs(a-b)/max(abs(a),abs(b),floor))


def audit_order(n):
    z,w=roots_jacobi(n,4.0,4.0)
    inside=bool(np.all(np.abs(z)<1.0)); positive=bool(np.all(w>0.0))
    symmetry=max(float(np.max(np.abs(z + z[::-1]))), float(np.max(np.abs(w-w[::-1]))))
    moments=[]
    worst_abs=0.0
    for k in range(2*n):
        q=float(np.sum(w*(z**k))); exact=analytic_moment(k); err=abs(q-exact)
        worst_abs=max(worst_abs,err)
        moments.append({'degree':k,'quadrature':q,'analytic':exact,'absolute_error':err})
    m0=analytic_moment(0)
    tensor=float(np.sum(w))**4
    tensor_exact=m0**4
    mapped=(A**4)*tensor
    mapped_exact=(A**4)*tensor_exact
    tasks=qd3.gj_tasks(n)
    helper_sum=float(sum(t[1] for t in tasks))
    ok=bool(inside and positive and symmetry<=5e-15 and worst_abs<=ATOL and
            rel(tensor,tensor_exact)<=RTOL and rel(mapped,mapped_exact)<=RTOL and
            len(tasks)==n**4 and rel(helper_sum,mapped_exact)<=RTOL)
    return {'order':n,'inside':inside,'positive_weights':positive,'symmetry_residual':symmetry,
            'worst_1d_moment_absolute_error':worst_abs,'moments':moments,
            'tensor_constant':tensor,'tensor_constant_exact':tensor_exact,
            'tensor_relative_error':rel(tensor,tensor_exact),
            'mapped_constant':mapped,'mapped_constant_exact':mapped_exact,
            'mapped_relative_error':rel(mapped,mapped_exact),
            'helper_tasks':len(tasks),'helper_weight_sum':helper_sum,
            'helper_weight_sum_relative_error':rel(helper_sum,mapped_exact),'pass':ok}


def main():
    rows=[audit_order(2),audit_order(3)]
    passed=all(r['pass'] for r in rows)
    out={'gate':'ITER053-QD3M-GAUSS-JACOBI-MOMENT-NORMALIZATION-AUDIT',
         'orders':rows,'pass':passed,
         'classification':('PASS_DIAGNOSTIC_ITER053_QD3_GAUSS_JACOBI_MOMENTS_EXACT' if passed else 'FAIL_DIAGNOSTIC_ITER053_QD3_GAUSS_JACOBI_MOMENT_NORMALIZATION'),
         'interpretation_lock':'IMPLEMENTATION/MATH AUDIT ONLY; NO ITER053 OR QD3 SCIENTIFIC RECLASSIFICATION; C6 SYMBOLIC UNFIXED; THEORY_ESTABLISHED_0'}
    os.makedirs('iter053-qd3m-output',exist_ok=True)
    with open('iter053-qd3m-output/result.json','w') as f: json.dump(out,f,sort_keys=True,indent=2)
    print(json.dumps(out,sort_keys=True))
    if not passed: raise SystemExit(2)

if __name__=='__main__': main()
