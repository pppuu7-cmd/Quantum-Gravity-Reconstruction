#!/usr/bin/env python3
import argparse,json
import numpy as np
from qgr_iter007_g6h_common import branch_lorentz,overlap_matrix
P=argparse.ArgumentParser();P.add_argument('--output',required=True);args=P.parse_args()
hs=[0.5,0.25,0.125,0.0625]
preps=['envelope','linear','helicity'];series={p:[] for p in preps}
for h in hs:
    dat,L=branch_lorentz(h)
    for p in preps:
        O,d=overlap_matrix(L,profile='m0',polarization=p,ntheta=16,nphi=32)
        series[p].append({'h':h,**d})
slopes={}
for p in preps:
    vals=np.array([r['loss'] for r in series[p]])
    assert np.all(vals>0), (p,vals)
    slopes[p]=float(np.polyfit(np.log(hs),np.log(vals),1)[0])
    assert 3.6<slopes[p]<4.4,(p,slopes[p])
# Polarization-sensitive preparations must not be silently identified with the envelope-only/unpolarized control.
coeff={p:series[p][-1]['loss']/hs[-1]**4 for p in preps}
assert abs(coeff['linear']-coeff['envelope'])>1e-5*max(abs(coeff['linear']),abs(coeff['envelope']),1e-30)
out={'lane':'BROADBAND_POLARIZATION_PREPARATION_DEPENDENCE','profile':'m0','rows':series,'log_h_slopes':slopes,'asymptotic_h4_coefficients_at_finest_scale':coeff,'classification':'NUMERICALLY_VERIFIED_SCOPED_BROADBAND_HISTORY_LOSS_HAS_COMMON_H4_ORDER_BUT_PREPARATION_DEPENDENT_COEFFICIENT_ACROSS_ENVELOPE_LINEAR_AND_HELICITY_STATES','scientific_interpretation':'The full broadband channel retains the same h^4 refinement order for an envelope-only/unpolarized control, a fixed linear spin-2 preparation and a definite-helicity preparation. Their coefficients need not agree. Thus the model fixes the history transport and refinement order, while a detector/preparation specification is part of any numerical comparator.','guard':'Do not average these preparations or select one coefficient post hoc as a universal QGR number. A phenomenological prediction must state the prepared polarization state and detector readout.'}
open(args.output,'w').write(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,sort_keys=True))