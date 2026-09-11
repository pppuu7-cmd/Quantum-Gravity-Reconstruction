#!/usr/bin/env python3
"""Analytic overlap identities for two normalized Lorentz-covariant null-packet preparations.

The packet families are benchmark preparations, not newly fitted theory parameters.  The
radial scale alpha cancels, while the profile shape changes the leading coefficient.
"""
from fractions import Fraction as F
import argparse,json
P=argparse.ArgumentParser();P.add_argument('--output',required=True);args=P.parse_args()

def amp0(g): return F(2,1)/(F(1)+g)
def amp1(g): return F(4,1)*(F(2)+g)/(F(3,1)*(F(1)+g)**2)
# Families on the future null cone for unit timelike u:
# m=0: psi ~ exp(-alpha u.k)
# m=1: psi ~ (u.k) exp(-alpha u.k)
# Using I(w)=int dmu(k) exp(-alpha w.k)=2*pi/(alpha^2 w^2),
# directional derivatives give the m=1 numerator. Normalization cancels alpha exactly.
samples=[F(1),F(101,100),F(11,10),F(2)]
rows=[]
for g in samples:
 a0=amp0(g);a1=amp1(g)
 assert a0<=1 and a1<=1 and a0>0 and a1>0
 rows.append({'gamma':str(g),'m0_amplitude':str(a0),'m0_squared':str(a0*a0),'m1_amplitude':str(a1),'m1_squared':str(a1*a1)})
assert amp0(F(1))==1 and amp1(F(1))==1
# Exact first derivative of squared overlap at gamma=1:
# m0: -1 ; m1: -4/3, so the same small rapidity scalar has a profile-dependent coefficient.
eps=F(1,10**6)
d0=((amp0(1+eps)**2)-1)/eps
d1=((amp1(1+eps)**2)-1)/eps
# finite-difference rational witnesses converge near the exact derivatives
assert abs(float(d0)+1)<2e-6
assert abs(float(d1)+F(4,3))<3e-6
out={
 'lane':'NORMALIZED_PACKET_OVERLAP_IDENTITIES',
 'future_null_measure_integral':'I_alpha(w)=2*pi/(alpha^2 w^2) for future timelike w',
 'family_m0':'psi_u(k)=N0 exp(-alpha u.k)',
 'family_m0_overlap':'<psi_u|psi_v>=2/(1+gamma)',
 'family_m1':'psi_u(k)=N1 (u.k) exp(-alpha u.k)',
 'family_m1_overlap':'<psi_u|psi_v>=4(2+gamma)/(3(1+gamma)^2)',
 'gamma':'u.v for unit future timelike u,v',
 'alpha_cancels_exactly':True,
 'squared_overlap_linear_coefficient_at_gamma_1':{'m0':'-1','m1':'-4/3'},
 'profile_coefficient_ratio':'4/3','samples':rows,
 'classification':'PASS_SCOPED_NORMALIZED_COVARIANT_NULL_PACKET_OVERLAPS_ARE_ALPHA_INDEPENDENT_BUT_PROFILE_DEPENDENT',
 'scientific_interpretation':'A physical packet scale alpha is not needed to compare these two normalized Lorentz-covariant benchmark families: it cancels exactly. However the packet profile does matter. Near coincident timelike labels, the m=1 family has a leading squared-overlap loss 4/3 times the m=0 family. Thus an h^4 branch-separation law can robustly fix the refinement order while the absolute purity-loss coefficient remains preparation dependent.',
 'guard':'The two profiles are explicit benchmark preparations, not uniquely selected by QGR. Their overlap identities do not by themselves include momentum-dependent polarization/Wigner holonomy of a coherent two-helicity state.'
}
open(args.output,'w').write(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,sort_keys=True))
