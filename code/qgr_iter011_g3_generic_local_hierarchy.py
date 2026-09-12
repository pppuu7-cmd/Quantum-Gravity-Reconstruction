#!/usr/bin/env python3
import json
from qgr_iter011_g3_common import generic_local_stats,logslope
spacings=[0.16,0.125,0.10,0.08,0.0625]
y0=[0.05,0.08,-0.04,0.07]
k=0.04
rows=[]
for a in spacings:
    p=generic_local_stats(a,k,y0);m=generic_local_stats(a,-k,y0)
    rows.append({
      'a':a,
      'torsion_even':0.5*(p['delta_torsion_local']+m['delta_torsion_local']),
      'haar_even':0.5*(p['delta_haar_local']+m['delta_haar_local']),
      'coarea_even':0.5*(p['delta_log_coarea_local']+m['delta_log_coarea_local']),
      'coarea_odd':0.5*(p['delta_log_coarea_local']-m['delta_log_coarea_local']),
      'min_sv':min(p['min_sv'],m['min_sv']),'max_residual':max(p['residual'],m['residual'])
    })
co=[r['coarea_even'] for r in rows]
to=[r['torsion_even'] for r in rows]
ha=[r['haar_even'] for r in rows]
pc=logslope(spacings,co);pt=logslope(spacings,to);ph=logslope(spacings,ha)
# Away from the tidal center first jets are nonzero.  After same-local-tetrad
# zero-jet subtraction the leading local measure term is expected at two derivatives.
assert 1.55<pc<2.45,(pc,rows)
assert min(r['min_sv'] for r in rows)>0.25
out={
 'gate':'ITER011-G3-GENERIC-LOCAL-DERIVATIVE-HIERARCHY',
 'y0':y0,'kappa_abs':k,'rows':rows,
 'torsion_even_spacing_power':pt,'haar_even_spacing_power':ph,'full_coarea_even_spacing_power':pc,
 'classification':'PASS_SCOPED_AFTER_SAME_LOCAL_TETRAD_ZERO_JET_SUBTRACTION_THE_GENERIC_WEAK_BACKGROUND_FULL_COAREA_CORRECTION_STARTS_AT_APPROXIMATELY_TWO_DERIVATIVES_WHEN_FIRST_JETS_ARE_NONZERO',
 'interpretation':'The h^4 curvature-squared coefficient exposed at the tidal center is not the whole local measure expansion. Generic points contain a lower-order first-jet/two-derivative contribution that must be absorbed/matched in the already-existing two-derivative sector before finite higher-derivative measure terms are interpreted.',
 'guard':'This is a local weak-background scaling audit at one generic point, not a covariant derivation of the complete two-derivative measure counterterm.'
}
print(json.dumps(out,sort_keys=True))
