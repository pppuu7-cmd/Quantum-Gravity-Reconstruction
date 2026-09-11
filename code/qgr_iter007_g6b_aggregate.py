#!/usr/bin/env python3
from pathlib import Path
import json

rows=[json.loads(p.read_text()) for p in sorted(Path('iter007-g6b-results').rglob('result.json'))]
by={r['lane']:r for r in rows}
required={
 'CUBICAL_FACE_GLUING_AND_SUPPORT',
 'DIAGONAL_PATH_GROUPOID_COMPOSABILITY',
 'SERIAL_HISTORY_INSTRUMENT_MEASURE',
 'OVERLAPPING_RECTANGULAR_GLOBAL_PATH_CENSUS',
 'G9_CURVED_24_HISTORY_GAUGE_INVARIANT_SPREAD',
}
assert set(by)==required,(set(by),required)
assert by['CUBICAL_FACE_GLUING_AND_SUPPORT']['face_adjacent_shared_edges']==12
assert by['DIAGONAL_PATH_GROUPOID_COMPOSABILITY']['face_adjacent_diagonal_composable'] is False
assert by['SERIAL_HISTORY_INSTRUMENT_MEASURE']['two_level_joint_history_count']==576
assert by['OVERLAPPING_RECTANGULAR_GLOBAL_PATH_CENSUS']['global_monotone_histories_in_2x1x1x1_union']==60
assert 3.8<by['G9_CURVED_24_HISTORY_GAUGE_INVARIANT_SPREAD']['fitted_rms_log_h_slope']<4.2

summary={
 'iteration':'007-G6B',
 'parallel_lanes':len(rows),
 'lane_classifications':{k:v['classification'] for k,v in sorted(by.items())},
 'key_results':[
   'Minimal incidence-preserving face gluing of two direction-labelled B4 cells identifies a full B3 face: 8 vertices, 12 edges and 6 plaquettes; only discrete S3 face relabelings remain.',
   'The existing 24-history instrument is an opposite-vertex diagonal path-groupoid morphism. Face-neighbour cell diagonals are not serially composable; only a cell shifted by (1,1,1,1) starts at the first diagonal target, and those serial cells share one vertex but no fine edges/plaquettes.',
   'For such serially composable blocks, the already-derived G8A isometry fixes the n-level joint branch measure to exactly product-uniform 24^-n. No cross-cell correlation coefficient is available.',
   'A face-overlap 2x1x1x1 region has 60 monotone global paths, not 576 independent local-diagonal pairs; only 6 global paths are unions of two complete overlapping-cell diagonals.',
   'On the pre-existing finite-curvature G9 background, a gauge-conjugation-invariant pairwise 24-history holonomy trace spread is nonzero and numerically scales as h^4 under refinement.'
 ],
 'major_correction_to_previous_front':'The G5B h^0 four-volume same-carrier stress cannot be interpreted as serial path-groupoid evolution over all face-adjacent cells. Face-adjacent B4 cells are overlapping local supports, not serial history-channel steps. The correct unresolved object is a quantum local-net/multi-region algebra for overlapping supports, not an arbitrary joint probability law between non-composable cell diagonals.',
 'closed_in_scope':[
   'two-cell B3 face incidence/support gluing in the minimal direction-labelled cubical completion',
   'serial-versus-overlapping path-groupoid composability distinction',
   'product-uniform branch law for serial coarse diagonal composition',
   'global-path overcounting diagnosis for face-overlap regions',
   'concrete curved h^4 gauge-invariant history-spread diagnostic'
 ],
 'still_open':[
   'proof that the full global CCRC complex is uniquely the minimal cubical completion rather than another incidence-compatible complex',
   'quantum local-net/algebra assignment for overlapping B4 supports and its commutation/factorization properties',
   'physical two-mode readout map on a generic curved quotient fiber',
   'numerical normalized purity prediction and physical microscopic scale separation',
   'independent KMQGB pass'
 ],
 'claim_lock':'Do not sum a 24-history channel once per face-adjacent four-cell as if those cells were serial on one carrier. Do not invent correlated histories for non-composable cells. Do not call the h^4 holonomy-spread diagnostic decoherence.',
 'recommended_next_gate':'G6C_LOCAL_NET_OF_OVERLAPPING_SUPPORTS_AND_CURVED_TWO_MODE_READOUT'
}
Path('iter007-g6b-summary.json').write_text(json.dumps(summary,indent=2,sort_keys=True)+'\n')
print(json.dumps(summary,sort_keys=True))
