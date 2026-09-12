#!/usr/bin/env python3
import argparse, json
import numpy as np
from qgr_iter011_g3_common import generic_local_stats, logslope

POINTS=[
 [0.05,0.08,-0.04,0.07],
 [0.08,-0.03,0.06,-0.05],
 [-0.06,0.05,0.09,0.03],
 [0.04,-0.07,-0.05,0.08],
]
SPACINGS=[0.12,0.09,0.07,0.055,0.043,0.034,0.027]

def slope(xs,ys,n=None):
    if n is not None:
        xs=xs[-n:]; ys=ys[-n:]
    return logslope(xs,ys)

ap=argparse.ArgumentParser()
ap.add_argument('--point',type=int,required=True)
ap.add_argument('--kappa',type=float,required=True)
a=ap.parse_args()
y0=POINTS[a.point]
k=abs(a.kappa)
rows=[]
for h in SPACINGS:
    p=generic_local_stats(h,k,y0); m=generic_local_stats(h,-k,y0)
    even=0.5*(p['delta_log_coarea_local']+m['delta_log_coarea_local'])
    odd=0.5*(p['delta_log_coarea_local']-m['delta_log_coarea_local'])
    rows.append({'a':h,'coarea_even':even,'coarea_odd':odd,
                 'torsion_even':0.5*(p['delta_torsion_local']+m['delta_torsion_local']),
                 'haar_even':0.5*(p['delta_haar_local']+m['delta_haar_local']),
                 'min_sv':min(p['min_sv'],m['min_sv']),
                 'max_residual':max(p['residual'],m['residual'])})
xs=[r['a'] for r in rows]; ys=[r['coarea_even'] for r in rows]
p_all=slope(xs,ys); p4=slope(xs,ys,4); p3=slope(xs,ys,3)
# Numerical-health gates only.  The scientific exponent is deliberately not preregistered
# because G3 falsified the earlier narrow two-derivative expectation (p=2.667 there).
assert min(r['min_sv'] for r in rows)>0.25
assert max(r['max_residual'] for r in rows)<1e-9
assert np.isfinite([p_all,p4,p3]).all()
if 1.6 <= p3 <= 2.4:
    cls='ASYMPTOTIC_COMPATIBLE_WITH_TWO_DERIVATIVE_GENERIC_TERM'
elif 3.5 <= p3 <= 4.5:
    cls='ASYMPTOTIC_COMPATIBLE_WITH_FOUR_DERIVATIVE_GENERIC_TERM'
else:
    cls='MIXED_OR_NONINTEGER_GENERIC_ASYMPTOTIC_POWER_REQUIRES_DECOMPOSITION'
out={
 'gate':'ITER011-G4-GENERIC-POINT-ASYMPTOTIC-MAP',
 'point_index':a.point,'y0':y0,'kappa_abs':k,'rows':rows,
 'coarea_power_all':p_all,'coarea_power_tail4':p4,'coarea_power_tail3':p3,
 'tail_power_drift':p3-p_all,
 'classification':cls,
 'interpretation':'Maps the unexpected G3 p≈2.67 result across independent generic points, smaller lattice spacings and two tidal amplitudes. A stable drift toward p≈2 would support a lower two-derivative generic contribution; stability away from 2 requires an explicit local invariant decomposition rather than threshold tuning.',
 'guard':'Scoped weak-background numerical asymptotics only; no covariant counterterm theorem and no coherent Lorentzian phase inference.'
}
print(json.dumps(out,sort_keys=True))
