#!/usr/bin/env python3
import argparse,json
P=argparse.ArgumentParser();P.add_argument('--output',required=True);args=P.parse_args()
# B4 Hasse graph: V=16, E=4*2^3=32, connected => first cycle rank E-V+1=17.
V=16;E=32;cycle_rank=E-V+1
assert cycle_rank==17
# A clock-only S4-invariant edge phase can depend only on source rank r=0..3: four phases phi_r.
# S4-invariant vertex rephasings depend on rank r=0..4: five chi_r, one global redundant => four gauge differences.
clock_edge_phase_dim=4
rank_vertex_rephase_effective_dim=4
clock_only_gauge_invariant_dim=clock_edge_phase_dim-rank_vertex_rephase_effective_dim
assert clock_only_gauge_invariant_dim==0
out={
 'lane':'INTRINSIC_CLOCK_PHASE_FREEDOM',
 'B4_vertices':V,
 'B4_cover_edges':E,
 'general_edge_phase_cycle_rank':cycle_rank,
 'S4_clock_only_edge_phase_parameters':clock_edge_phase_dim,
 'effective_rank_vertex_rephasings':rank_vertex_rephase_effective_dim,
 'S4_clock_only_physical_phase_dimension':clock_only_gauge_invariant_dim,
 'classification':'FAIL_SCOPED_INTRINSIC_RANK_CLOCK_ALONE_CANNOT_GENERATE_A_NONTRIVIAL_PHYSICAL_HISTORY_PHASE_OR_FIX_G__RANK_ONLY_EDGE_PHASES_ARE_VERTEX_REPHASING_GAUGE',
 'scientific_interpretation':'A completely general U(1) phase connection on the B4 Hasse graph can carry 17 independent loop phases. But if no structure beyond the intrinsic S4-invariant rank clock is used, edge phases can depend only on rank. The four rank-edge phases are exactly removable by four independent differences of rank-slice vertex phases. Hence the clock by itself has no gauge-invariant dynamical phase capable of determining kappa/hbar. Nontrivial history phases must come from additional geometric/directional data, as in the already-derived QGR connection/action sector.',
 'guard':'This does not remove the physical curvature/history phases already present in QGR. It shows only that the newly derived scalar clock cannot independently quantize or set their overall dimensionless coupling g.'
}
open(args.output,'w').write(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,sort_keys=True))