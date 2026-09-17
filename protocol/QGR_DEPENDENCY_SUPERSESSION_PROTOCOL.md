# QGR Dependency / Supersession / Replay Protocol v1

Historical terminal files are immutable evidence. A corrected authority never rewrites history.

Each lineage node may declare `depends_on`, `supersedes`, `preserves`, `invalidates`, `requires_replay_of`, and `does_not_affect`.

A correction may supersede only descendants with an actual dependency path to the corrected object. Descendant replay requires a new prospective preregistration and must compare old/new lineage while preserving both records. Circular dependencies, missing parents, silent supersession, replay without preregistration, and mutation of protected historical terminal files are INVALID.

Current lesson: Iter057AQ localizes a defect in historical Iter057X degree-six source construction; Iter057AR may supersede X degree-six only if its own frozen gate passes. It does not automatically replay or invalidate AF/AG/AM/AN.
