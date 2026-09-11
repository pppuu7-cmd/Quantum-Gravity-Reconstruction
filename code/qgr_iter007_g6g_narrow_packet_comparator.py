#!/usr/bin/env python3
"""Specified narrow-packet detector benchmark combining envelope and central-ray polarization.

This is intentionally a preparation/readout comparator, not a universal QGR number.
"""
import argparse,json,math
import numpy as np
from qgr_iter007_g6g_common import solve_paths,branch_wigner_angles,E,u0,u0sq
P=argparse.ArgumentParser();P.add_argument('--output',required=True);args=P.parse_args()

def one(h):
 dat=solve_paths(h);Ls=dat['L_paths']
 us=np.array([L@u0 for L in Ls]);gamma=(us@E@us.T)/u0sq
 assert np.max(np.abs(np.diag(gamma)-1))<2e-8 and np.min(gamma)>1-2e-8
 env=(2/(1+gamma))**2 # m=0 normalized exponential envelope squared overlap
 ang,little=branch_wigner_angles(Ls);D=ang[:,None]-ang[None,:];D=(D+math.pi)%(2*math.pi)-math.pi
 pol=np.cos(2*D)**2
 Renv=float(np.mean(env));Rpol=float(np.mean(pol));Rcomb=float(np.mean(env*pol))
 return {'h':h,'envelope_loss':1-Renv,'central_ray_linear_polarization_loss':1-Rpol,'factorized_narrow_packet_combined_loss':1-Rcomb,'max_little_group_closure_error':little}
hs=[.5,.25,.125,.0625,.03125];rows=[one(h) for h in hs]
def slope(k):return float(np.polyfit(np.log(hs),np.log([r[k] for r in rows]),1)[0])
sl={k:slope(k) for k in ['envelope_loss','central_ray_linear_polarization_loss','factorized_narrow_packet_combined_loss']}
for k,v in sl.items():assert 3.7<v<4.3,(k,v)
out={'lane':'NARROW_PACKET_DETECTOR_COMPARATOR','preparation':'normalized m=0 exponential future-null envelope plus fixed linear TT polarization','readout':'barycentric target detector frame / canonical standard-section central ray','rows':rows,'log_h_slopes':sl,'combined_loss_over_h4':[r['factorized_narrow_packet_combined_loss']/r['h']**4 for r in rows],'classification':'NUMERICALLY_VERIFIED_SCOPED_SPECIFIED_NARROW_PACKET_LINEAR_POLARIZATION_COMPARATOR_HAS_H4_HISTORY_LOSS_ON_REPAIRED_G9','scientific_interpretation':'For one fully specified preparation/readout benchmark, the normalized envelope-overlap factor and central-ray spin-2 polarization-overlap factor can be multiplied in the narrow-packet approximation. The resulting history-mixture loss scales extremely close to h^4. Its asymptotic coefficient is approximately the sum of the envelope and polarization coefficients at leading order, as expected for two independent O(h^4) overlap deficits.','guard':'This is not the exact broadband coherent two-polarization wavepacket channel: momentum dependence of the Wigner rotation across the packet is neglected. It is a controlled central-ray/narrow-packet comparator and remains preparation/readout dependent. Absolute microscopic h is still not fixed.'}
open(args.output,'w').write(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,sort_keys=True))
