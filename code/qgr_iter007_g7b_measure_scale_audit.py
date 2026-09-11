#!/usr/bin/env python3
import argparse,json
P=argparse.ArgumentParser();P.add_argument('--output',required=True);args=P.parse_args()
# Q_13 has 10 independent symmetric components. Under G -> s^2 G:
# d^10G -> s^20 d^10G; det G -> s^8 det G in four dimensions;
# |det G|^-5/2 -> s^-20. Exact cancellation.
scales=[0.5,1.0,2.0,3.0,10.0]
rows=[]
for s in scales:
    coordinate_jacobian=s**20
    determinant_weight=(s**8)**(-2.5)
    total=coordinate_jacobian*determinant_weight
    assert abs(total-1.0)<1e-12,(s,total)
    rows.append({'s':s,'coordinate_jacobian':coordinate_jacobian,'determinant_weight':determinant_weight,'measure_ratio':total})
out={
 'lane':'KINEMATIC_MEASURE_SCALE_NOFIX',
 'measure':'dmu(G)=|det G|^(-5/2) d^10G',
 'global_response_rescaling':'G -> s^2 G',
 'rows':rows,
 'classification':'FAIL_SCOPED_EXISTING_CONGRUENCE_INVARIANT_KINEMATIC_MEASURE_IS_EXACTLY_SCALE_INVARIANT_AND_DOES_NOT_FIX_H_OR_KAPPA',
 'scientific_interpretation':'The already-derived Lorentzian configuration measure has zero net homogeneity under global response rescaling. It contains neither h nor kappa and supplies no preferred absolute configuration or length scale. Multiplicative normalization of an infinite/continuous measure also cancels from normalized state ratios and cannot by itself determine the action coefficient.',
 'guard':'A future microscopic counting measure, symplectic form, determinant anomaly or other quantum structure could introduce a scale. This lane only audits the current invariant configuration measure.'
}
open(args.output,'w').write(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,sort_keys=True))