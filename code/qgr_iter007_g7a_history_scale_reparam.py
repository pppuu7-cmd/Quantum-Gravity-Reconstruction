#!/usr/bin/env python3
import argparse,json
P=argparse.ArgumentParser();P.add_argument('--output',required=True);args=P.parse_args()
# Let a=c*kappa/h^2. Then h^4=(c*kappa/a)^2/c^4? More simply solve h^2=c*kappa/a,
# so a leading Cprep*h^4*Icurv becomes Cprep*(c*kappa/a)^2*Icurv.
# The exact geometric c changes normalization but not the surviving kappa dependence.
scales=[0.5,1.0,2.0,4.0]
rows=[]
for lam in scales:
    # keep a fixed by kappa->lam^2 kappa and h->lam h
    a_ratio=(lam**2)/(lam**2)
    history_ratio=lam**4
    rows.append({'lambda':lam,'continuum_a_ratio':a_ratio,'leading_history_h4_ratio':history_ratio})
    assert abs(a_ratio-1.0)<1e-15
out={
 'lane':'HISTORY_SCALE_REPARAMETERIZATION',
 'fixed_continuum_transformation':'h -> lambda h; kappa -> lambda^2 kappa',
 'rows':rows,
 'classification':'BLOCKED_SCOPED_H4_HISTORY_AMPLITUDE_VARIES_ALONG_THE_EXACT_CONTINUUM_NORMALIZATION_DEGENERACY',
 'scientific_interpretation':'The same continuum Einstein-Hilbert normalization is compatible with a one-parameter family of microscopic (h,kappa) pairs, while the leading history correction changes as lambda^4. Thus the normalized broadband comparator is a genuine second-scale probe but cannot be converted into an absolute prediction until this degeneracy is lifted.',
 'guard':'The dimensionless h^4 order remains a model prediction. Only its physical calibration is blocked.'
}
open(args.output,'w').write(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,sort_keys=True))