#!/usr/bin/env python3
import argparse,json
import numpy as np
from qgr_iter007_g6h_common import branch_lorentz,overlap_matrix
P=argparse.ArgumentParser();P.add_argument('--profile',choices=['m0','m1'],required=True);P.add_argument('--output',required=True);args=P.parse_args()
hs=[0.5,0.25,0.125,0.0625]
rows=[]
for h in hs:
    dat,L=branch_lorentz(h)
    O,d=overlap_matrix(L,profile=args.profile,polarization='linear',ntheta=18,nphi=36)
    rows.append({'h':h,**d,'min_torsion_jacobian_singular':dat['min_jacobian_singular'],'max_torsion_residual':dat['max_torsion_residual']})
loss=np.array([r['loss'] for r in rows])
assert np.all(loss>0),loss
slope=float(np.polyfit(np.log(hs),np.log(loss),1)[0])
assert 3.65<slope<4.35,(slope,rows)
assert max(r['max_diagonal_error'] for r in rows)<2e-7
assert max(r['max_hermiticity_error'] for r in rows)<2e-7
out={'lane':'BROADBAND_COHERENT_TWO_MODE_PROFILE','profile':args.profile,'polarization_preparation':'fixed linear spin-2 state in the specified relational standard section, integrated over the complete future null-cone direction sphere','history_count':24,'rows':rows,'log_h_slope':slope,'loss_over_h4':[r['loss']/r['h']**4 for r in rows],'classification':'NUMERICALLY_VERIFIED_SCOPED_FULL_BROADBAND_COHERENT_TWO_MODE_HISTORY_MIXTURE_LOSS_SCALES_H4_ON_REPAIRED_G9','scientific_interpretation':'Unlike G6G, this is not a central-ray/narrow-packet factorization. For every target null direction the source momentum, little-group element and physical spin-2 rotation are recomputed for every one of the 24 histories, while the null-energy integral is performed analytically. The resulting normalized branch-overlap matrix gives the full broadband history-mixture purity for the specified wavepacket/polarization preparation and scales as h^4 on the repaired G9 refinement sequence.','guard':'The numerical coefficient belongs to this explicit preparation/readout profile. It is not a universal decoherence constant, and absolute phenomenology still requires the physical microscopic h/kappa scale.'}
open(args.output,'w').write(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,sort_keys=True))