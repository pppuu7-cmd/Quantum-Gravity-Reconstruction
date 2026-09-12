#!/usr/bin/env python3
import argparse,json
import numpy as np
from qgr_iter011_g3_common import generic_local_stats
POINTS=[[0.05,0.08,-0.04,0.07],[0.08,-0.03,0.06,-0.05],[-0.06,0.05,0.09,0.03],[0.04,-0.07,-0.05,0.08]]
SP=np.array([0.12,0.09,0.07,0.055,0.043,0.034,0.027,0.021,0.017,0.0135],float)
def even_stats(h,k,y0):
 p=generic_local_stats(float(h),k,y0); m=generic_local_stats(float(h),-k,y0)
 return {q:0.5*(p[q]+m[q]) for q in ['delta_torsion_local','delta_haar_local','delta_log_coarea_local']} | {'min_sv':min(p['min_sv'],m['min_sv']),'residual':max(p['residual'],m['residual'])}
def fit(xs,ys):
 X=np.column_stack([xs**p for p in [2,3,4,5]]); c,*_=np.linalg.lstsq(X,ys,rcond=None); pred=X@c
 return {'c2':float(c[0]),'c3':float(c[1]),'c4':float(c[2]),'c5':float(c[3]),'rms_rel':float(np.sqrt(np.mean((pred-ys)**2))/max(np.max(np.abs(ys)),1e-30))}
ap=argparse.ArgumentParser(); ap.add_argument('--point',type=int,required=True); ap.add_argument('--kappa',type=float,required=True); a=ap.parse_args()
y0=POINTS[a.point]; k=abs(a.kappa); rows=[even_stats(h,k,y0) for h in SP]
T=np.array([r['delta_torsion_local'] for r in rows]); H=np.array([r['delta_haar_local'] for r in rows]); C=np.array([r['delta_log_coarea_local'] for r in rows])
ft,fh,fc=fit(SP,T),fit(SP,H),fit(SP,C)
closure=abs(fc['c2']-(fh['c2']-ft['c2']))/max(abs(fc['c2']),1e-30)
dom='HAAR_DOMINANT' if abs(fh['c2'])>2*abs(ft['c2']) else ('TORSION_JACOBIAN_DOMINANT' if abs(ft['c2'])>2*abs(fh['c2']) else 'MIXED_COMPARABLE')
assert min(r['min_sv'] for r in rows)>0.25 and max(r['residual'] for r in rows)<1e-9 and closure<1e-7
out={'gate':'ITER011-G6-C2-COMPONENT-DECOMPOSITION','point_index':a.point,'kappa_abs':k,'fit_torsion':ft,'fit_haar':fh,'fit_coarea':fc,'c2_component_closure_rel':float(closure),'dominance':dom,'classification':'COMPONENT_DECOMPOSITION_RESOLVED','guard':'Weak-background local coarea diagnostic only; decomposition identifies the source of the lattice a^2 coefficient but is not a covariant effective-action counterterm derivation.'}
print(json.dumps(out,sort_keys=True))
