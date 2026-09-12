#!/usr/bin/env python3
import json
from pathlib import Path

files=[
    Path('code/qgr_iter007_g6h_common.py'),
    Path('code/qgr_iter007_g6h_broadband_profile.py'),
    Path('code/qgr_iter007_g6g_common.py'),
]
texts={str(p):p.read_text(encoding='utf-8') for p in files}
joined='\n'.join(texts.values())
for forbidden in ['S_alpha','c6','Weyl^3','Weyl_cubed','action_phase']:
    assert forbidden not in joined
assert 'branch_lorentz' in texts[str(files[0])]
assert 'solve_paths' in texts[str(files[0])]
assert 'overlap_matrix' in texts[str(files[1])]
assert 'least_squares' in texts[str(files[2])]
assert 'residual' in texts[str(files[2])]

out={
    "gate":"ITER009-G4-G6H-SCOPE-AUDIT",
    "files_audited":[str(p) for p in files],
    "geometry_chain":"broadband_profile -> branch_lorentz -> solve_paths(torsion/connection residual) -> Lorentz/Wigner/source-momentum overlaps",
    "explicit_action_phase_dependency":False,
    "explicit_c6_dependency":False,
    "corrected_equations_of_motion_recomputed":False,
    "classification":"PASS_SCOPED_EXISTING_G6H_IS_A_FIXED_GEOMETRY_TRANSPORT_COMPARATOR_INDEPENDENT_OF_SCALAR_BRANCH_ACTION_PHASES_AND_HAS_NO_EXPLICIT_C6_INPUT",
    "guard":"A self-consistent curved prediction that recomputes branch geometry from an action including c6 is not covered by the existing G6H code."
}
print(json.dumps(out,sort_keys=True))
