# Iter057AP constructor execution defect — Frechet-control Cup wiring

Date: 2026-09-17
Preregistration: `6de62a559381a7c86e01c58a62ea7d8c91606884`
Frozen constructor implementation: `1ce4b9b1dfa2cc1a6d8ca93c0e2d54f8d155b6d2`
Failed execution-only retry run: `35175529339`

The exact constructor completed the background/curvature/P construction stage and then raised `NameError: Cup is not defined` inside `p_controls`. The already-computed `Cup` was local to `compute()` and was not passed into the Frechet-control helper. No constructor payload was written, no source coefficient target was opened, and no Iter057U/X comparison occurred.

This is a local implementation/wiring error, not scientific evidence.

Allowed execution-only repair: a wrapper may populate the helper's `Cup` input by recomputing `raise_last(Rlow,gi,8)` before calling the unchanged frozen helper. On the preregistered canonical seed the constructor independently requires `C==Rlow` through degree eight (`B_Weyl_equals_Riemann_on_Ricci_flat_seed`), so this helper-only reconstruction is algebraically identical to the already-computed `raise_last(C,gi,8)` whenever the frozen seed control passes. If that seed control fails, the constructor remains invalid; the wrapper does not mask it.

No formula, seed, P definition, source convention, degree, target, sign, normalization, classifier or acceptance criterion is changed.