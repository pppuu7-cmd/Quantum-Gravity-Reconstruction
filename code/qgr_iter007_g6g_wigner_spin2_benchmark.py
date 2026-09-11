#!/usr/bin/env python3
import argparse,json,math
import numpy as np
from qgr_iter007_g6g_common import solve_paths,branch_wigner_angles
P=argparse.ArgumentParser();P.add_argument('--output',required=True);args=P.parse_args()

def one(h):
 dat=solve_paths(h);ang,little=branch_wigner_angles(dat['L_paths']);D=ang[:,None]-ang[None,:]
 # all angles are small on the tested refinement sequence; use principal wrapped difference for robustness
 D=(D+math.pi)%(2*math.pi)-math.pi
 rms=float(np.sqrt(np.mean(D**2)))
 # A linearly polarized spin-2 TT state rotates by 2 theta in the plus/cross plane.
 # Squared pair overlap is cos^2(2 Delta theta).
 R=float(np.mean(np.cos(2*D)**2));loss=1-R
 return {'h':h,'wigner_angle_pair_rms':rms,'linear_spin2_polarization_retention':R,'linear_spin2_polarization_loss':loss,'max_little_group_closure_error':little}
hs=[.5,.25,.125,.0625,.03125];rows=[one(h) for h in hs]
def slope(key):return float(np.polyfit(np.log(hs),np.log([r[key] for r in rows]),1)[0])
sa=slope('wigner_angle_pair_rms');sl=slope('linear_spin2_polarization_loss')
assert 1.8<sa<2.2,sa;assert 3.7<sl<4.3,sl
out={'lane':'CENTRAL_RAY_WIGNER_SPIN2','standard_section':'E-orthonormal barycentric time plus deterministic relational spatial triad; minimal spatial rotation z->k direction followed by longitudinal boost','rows':rows,'log_h_slopes':{'wigner_angle_pair_rms':sa,'linear_spin2_polarization_loss':sl},'loss_over_h4':[r['linear_spin2_polarization_loss']/r['h']**4 for r in rows],'classification':'NUMERICALLY_VERIFIED_SCOPED_CENTRAL_RAY_PHYSICAL_SPIN2_WIGNER_ANGLE_SPREAD_H2_AND_FIXED_LINEAR_POLARIZATION_OVERLAP_LOSS_H4','scientific_interpretation':'Using a fully specified relational detector frame/standard section, each repaired G9 history induces a massless little-group map on the two physical QGR-L1 modes. The branch Wigner-angle spread is O(h^2). A fixed linear TT polarization therefore acquires an O(h^4) pair-overlap loss, the same refinement order as the momentum-envelope effect but with an independent preparation/readout coefficient.','guard':'The Wigner angle depends on the chosen physical detector/standard section and the linear-polarization preparation. The h^4 scaling is the scoped result; the coefficient is not an observer-independent universal QGR number. This is a central-ray benchmark, not a full broadband wavepacket integration.'}
open(args.output,'w').write(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,sort_keys=True))
