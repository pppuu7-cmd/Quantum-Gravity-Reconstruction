#!/usr/bin/env python3
import argparse,json
from qgr_iter011_g1_common import flat_subtracted
ap=argparse.ArgumentParser(); ap.add_argument('--h',type=float,required=True); a=ap.parse_args()
h=a.h; k=0.08
p=flat_subtracted(h,k); m=flat_subtracted(h,-k)
vp=p['delta_sum_logabsdet']; vm=m['delta_sum_logabsdet']
even=0.5*(vp+vm); odd=0.5*(vp-vm)
out={'gate':'ITER011-G1B-PARITY-REFINEMENT-LANE','h':h,'kappa_abs':k,'plus':vp,'minus':vm,'even':even,'odd':odd,'odd_over_even_abs':abs(odd)/(abs(even)+1e-30),'min_sv':min(p['min_sv'],m['min_sv']),'max_residual':max(p['max_residual'],m['max_residual'])}
print(json.dumps(out,sort_keys=True))
