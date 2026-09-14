# Iter054C Initial Run Authority Record

Gate: `ITER054C-WEYL3-LOCAL-METRIC-PRINCIPAL-SYMBOL-AND-GAUGE-DEGENERACY`

Initial production run: `34808083077`
Initial production head: `335d201596ad48234dec6211aefaee20cca7ab0b`
Preregistration: `3bc563b2aa0c691a78b57c4e7c53fd0ad9a51ba3`

Status: **IMPLEMENTATION / CONTROL INVALID — NON-AUTHORITATIVE FOR SCIENTIFIC PASS/FAIL**.

Reason: A0 job `103863789631` reported all four frozen tensor-identity probes as exact, all k^2 homogeneity probes as exact, and all corrupted-map negative controls detected, but the lane still failed because one implementation-selected covector `[3,2,1,2]` has exact Minkowski norm `-9+4+1+4=0`. The preregistration requires four non-null rational covectors. Therefore the implementation violated a frozen control property before scientific classification.

The correction is restricted to replacing that invalid null covector by a non-null rational covector. Scientific formulas, stream predicates, background panel, thresholds, interpretation locks, and authority boundaries are unchanged. Evidence from run `34808083077` must not be pooled into the corrected retry.

Claim locks remain unchanged: theory established 0%; c6 symbolic/unfixed; beta=1 unauthorized; no hyperbolicity, well-posedness, physical mode/ghost, unitarity, UV completion, experimental confirmation, or new-physics claim.
