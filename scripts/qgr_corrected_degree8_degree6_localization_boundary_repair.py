#!/usr/bin/env python3
"""Execution/control-only repair frozen by b2f4c513bdd8ffbbb37202e0b7b756f626d920ec."""
from itertools import product
import qgr_corrected_degree8_degree6_localization as q
import qgr_iter057aa_corrected_dodecic_seed_weyl3_eighth_source_jet as aa
import qgr_iter057z_dodecic_einstein_seed_completion as z
import qgr_iter057ap_independent_covariant_source as b
import qgr_iter057ap_independent_covariant_source_repair as r

N=b.N

def repaired_common(boundary):
    if boundary=='R10':
        g,prov,_,_,_=z.canonical_seed10(); vacuum_degree=8
    else:
        g,prov,_,_=aa.seed_metric12(); vacuum_degree=10
    gi,Gamma,Rlow,Ric,Scal,Ein,invok=aa.geometry10(g)
    C=Rlow; Cup=b.raise_last(C,gi,10); I3,QF=r._fixed_cubic_and_Q(C,Cup,8); PF,_=r._fixed_p_from_frechet(g,gi,C,Cup,QF,10)
    controls={
      'seed_provenance':bool(prov),
      'inverse10':bool(invok),
      'Ricci_boundary_zero':all(not b.trunc(Ric[i][j],vacuum_degree) for i,j in product(range(N),repeat=2)),
      'scalar_boundary_zero':not b.trunc(Scal,vacuum_degree),
      'Einstein_boundary_zero':all(not b.trunc(Ein[i][j],vacuum_degree) for i,j in product(range(N),repeat=2)),
      'vacuum_control_degree':vacuum_degree in (8,10),
    }
    return g,gi,Gamma,Rlow,I3,PF,controls

q.common=repaired_common
raise SystemExit(q.main())
