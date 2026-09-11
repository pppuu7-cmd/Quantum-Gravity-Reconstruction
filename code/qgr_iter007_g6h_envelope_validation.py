#!/usr/bin/env python3
import argparse,json
import numpy as np
from qgr_iter007_g6h_common import branch_lorentz,overlap_matrix,exact_envelope_matrix,direction_data
P=argparse.ArgumentParser();P.add_argument('--output',required=True);args=P.parse_args()
dat,L=branch_lorentz(0.5)
errs={};freq=[]
for profile in ['m0','m1']:
    O,diag=overlap_matrix(L,profile=profile,polarization='envelope',ntheta=20,nphi=40)
    E=exact_envelope_matrix(L,profile)
    err=float(np.max(np.abs(O.real-E)))
    errs[profile]={'max_abs_error_vs_exact':err,'diagnostics':diag}
    assert err<2e-6,(profile,err)
# Wigner angle and envelope Doppler factor must be independent of an overall null energy rescaling.
n=np.array([0.31,-0.42,(1-0.31**2-0.42**2)**0.5])
a0,t0,c0=direction_data(L,n,0.5)
for fac in [1.0,2.0,4.0]:
    a,t,c=direction_data(L,n,fac)
    freq.append({'factor':fac,'max_a_change':float(np.max(np.abs(a-a0))),'max_theta_change':float(np.max(np.abs(t-t0))),'closure':c})
    assert np.max(np.abs(a-a0))<2e-10
    assert np.max(np.abs(t-t0))<2e-9
out={'lane':'BROADBAND_ENVELOPE_VALIDATION','h':0.5,'history_count':24,'quadrature':'20-point Gauss-Legendre in cos(theta) x 40 uniform azimuths; radial null-energy integral analytic','profile_validation':errs,'frequency_scale_checks':freq,'classification':'PASS_SCOPED_BROADBAND_NULL_CONE_QUADRATURE_REPRODUCES_EXACT_NORMALIZED_ENVELOPE_OVERLAPS_AND_WIGNER_DATA_ARE_NULL_ENERGY_SCALE_INDEPENDENT','scientific_interpretation':'The broadband integration machinery reproduces the exact G6F Lorentz-covariant envelope overlaps for both benchmark radial profiles, while the induced little-group data are independent of overall null energy. Thus the radial integral can be removed analytically without a momentum cutoff and the remaining numerical task is a compact angular integral.','guard':'This validates the integration machinery, not yet the full polarization-dependent comparator.'}
open(args.output,'w').write(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,sort_keys=True))