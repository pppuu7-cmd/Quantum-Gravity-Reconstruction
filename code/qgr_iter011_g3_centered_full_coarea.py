#!/usr/bin/env python3
import json
from qgr_iter011_g3_common import centered_cell_stats,logslope
hs=[0.25,0.20,0.16,0.125,0.10,0.08]
k=0.04
rows=[]
for h in hs:
    p=centered_cell_stats(h,k); m=centered_cell_stats(h,-k)
    row={'h':h}
    for key in ('delta_torsion_logdet','delta_haar_logdensity','delta_log_coarea'):
        row[key+'_even']=0.5*(p[key]+m[key])
        row[key+'_odd']=0.5*(p[key]-m[key])
    row['min_sv']=min(p['min_sv'],m['min_sv']);row['max_residual']=max(p['max_residual'],m['max_residual'])
    rows.append(row)
t=[r['delta_torsion_logdet_even'] for r in rows]
ha=[r['delta_haar_logdensity_even'] for r in rows]
co=[r['delta_log_coarea_even'] for r in rows]
pt=logslope(hs,t);ph=logslope(hs,ha);pc=logslope(hs,co)
ct=[v/(k*k*h**4) for v,h in zip(t,hs)]
ch=[v/(k*k*h**4) for v,h in zip(ha,hs)]
cc=[v/(k*k*h**4) for v,h in zip(co,hs)]
assert abs(pt-4)<0.15 and abs(ph-4)<0.15 and abs(pc-4)<0.15,(pt,ph,pc)
assert abs(ct[-1]+25/16)<0.03,ct[-1]
assert abs(ch[-1]+5/8)<0.03,ch[-1]
assert abs(cc[-1]-15/16)<0.04,cc[-1]
out={
 'gate':'ITER011-G3-CENTERED-FULL-HAAR-COAREA',
 'kappa_abs':k,'rows':rows,
 'h_power_torsion_even':pt,'h_power_haar_even':ph,'h_power_full_coarea_even':pc,
 'torsion_coeff_over_kappa2_h4':ct,'haar_coeff_over_kappa2_h4':ch,'full_coarea_coeff_over_kappa2_h4':cc,
 'candidate_asymptotic_rationals':{'torsion_logdet':'-25/16','haar_logdensity':'-5/8','full_log_coarea':'+15/16'},
 'classification':'PASS_SCOPED_COMPLETE_REGULAR_BRANCH_HAAR_OVER_TORSION_COAREA_FACTOR_HAS_A_FIXED_EVEN_KAPPA2_H4_CORRECTION_CONSISTENT_WITH_PLUS_15_OVER_16_ON_THE_CENTERED_WEYL_ACTIVE_TIDAL_CELL',
 'guard':'The rational values are asymptotic numerical reconstructions on this specified weak tidal cell family. They are not yet a covariant all-background coefficient theorem or a coherent Lorentzian c6 phase.'
}
print(json.dumps(out,sort_keys=True))
