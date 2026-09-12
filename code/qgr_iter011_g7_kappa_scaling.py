#!/usr/bin/env python3
import argparse,json
import numpy as np
from qgr_iter011_g3_common import generic_local_stats
POINTS=[[0.05,0.08,-0.04,0.07],[0.08,-0.03,0.06,-0.05],[-0.06,0.05,0.09,0.03],[0.04,-0.07,-0.05,0.08]]
SP=np.array([0.12,0.09,0.07,0.055,0.043,0.034,0.027,0.021,0.017,0.0135],float)
KS=np.array([0.005,0.01,0.02,0.04,0.08],float)
def c2_for(k,y0):
 ys=[]; minsv=1e9; maxres=0.0
 for h in SP:
  p=generic_local_stats(float(h),float(k),y0); m=generic_local_stats(float(h),float(-k),y0)
  ys.append(0.5*(p['delta_log_coarea_local']+m['delta_log_coarea_local'])); minsv=min(minsv,p['min_sv'],m['min_sv']); maxres=max(maxres,p['residual'],m['residual'])
 X=np.column_stack([SP**p for p in [2,3,4,5]]); c,*_=np.linalg.lstsq(X,np.array(ys),rcond=None)
 return float(c[0]),float(minsv),float(maxres)
ap=argparse.ArgumentParser(); ap.add_argument('--point',type=int,required=True); a=ap.parse_args(); y0=POINTS[a.point]
vals=[]
for k in KS:
 c2,sv,res=c2_for(k,y0); vals.append({'kappa':float(k),'c2':c2,'c2_over_k2':float(c2/k**2),'min_sv':sv,'max_residual':res})
cs=np.array([abs(v['c2']) for v in vals]); slope=float(np.polyfit(np.log(KS),np.log(cs),1)[0]); norm=np.array([v['c2_over_k2'] for v in vals]); spread=float((norm.max()-norm.min())/max(abs(norm.mean()),1e-30))
assert min(v['min_sv'] for v in vals)>0.25 and max(v['max_residual'] for v in vals)<1e-9
cls='QUADRATIC_WEAK_FIELD_SCALING_SUPPORTED' if abs(slope-2.0)<0.15 and spread<0.35 else 'NONQUADRATIC_OR_CROSSOVER_SCALING'
out={'gate':'ITER011-G7-KAPPA-SCALING','point_index':a.point,'y0':y0,'values':vals,'loglog_slope_abs_c2_vs_kappa':slope,'c2_over_kappa2_relative_spread':spread,'classification':cls,'guard':'Even-in-kappa weak-background diagnostic. Quadratic scaling supports ordinary perturbative analyticity of the local a^2 measure term; it does not supply the missing coherent Lorentzian phase/action.'}
print(json.dumps(out,sort_keys=True))
