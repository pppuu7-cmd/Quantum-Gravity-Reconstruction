# COVARIANT_WEYL3_A7_CONNECTION_MULTICOORDINATE_NEUTRAL_EXTRACTION — run 35411657960

Date: 2026-09-19

## Authority

- Gate: `COVARIANT_WEYL3_A7_CONNECTION_MULTICOORDINATE_NEUTRAL_EXTRACTION`
- Prospective preregistration: `58284ae7f71e73db5c2d71d157bc74bd7d646030`
- Execution binding: `4fe4634a1b026bd73233e1082efe52bfcda91bf9`
- Production head: `45bf70a9f861fb56128690c6b25bf085c070e87a`
- Actions run: `35411657960`
- Parent primitive-localization result: `199ecea77c9138c4a166d1ffc7143ce2d0de34be`

## Terminal classification

`MULTICOORDINATE_NEUTRAL_EXTRACTION_MATCHES_LANE_B`

The target-blind exact polynomial construction in `eps,x0,x1,x2,x3` reproduced all mandatory shared connection controls before target comparison.

## Exact connection-factor controls

All 64 background connection-derivative channels reproduce exactly:

- multicoordinate polynomial dGamma SHA256:
  `6375566a43d065ebd13d7a2b7617448906f72defbb4914022231c69f545ebcc0`
- repository-reference dGamma SHA256:
  `6375566a43d065ebd13d7a2b7617448906f72defbb4914022231c69f545ebcc0`

All 64 perturbative connection channels reproduce exactly:

- multicoordinate polynomial deltaGamma SHA256:
  `6a8ca1d48655e80b91812efde491e2ccdd8b463f1363b60cf83fbd83bdae33c7`
- repository-reference deltaGamma SHA256:
  `6a8ca1d48655e80b91812efde491e2ccdd8b463f1363b60cf83fbd83bdae33c7`

Thus the missing legacy-C channel `dGamma:0,0,0,1` is restored by the prospectively defined full multicoordinate local jet.

## Full tensor result

Neutral multicoordinate tensor SHA256:

`702b353ada68114482ede9a4fb3c8af6d3b7af708982256e44b7c2e7909848b4`

Frozen Lane B tensor SHA256:

`702b353ada68114482ede9a4fb3c8af6d3b7af708982256e44b7c2e7909848b4`

Frozen Lane A tensor SHA256:

`6dce9ed04c9199cf36eb2a723095f7eeba3f002844c3cd9df7da33704cbdf673`

Legacy univariate Lane C tensor SHA256:

`e3797c7dade7f4de601ba047be48b0ed73278333e01719e3b0d97588e783deb8`

The multicoordinate neutral tensor matches Lane B exactly and does not match legacy C.

Frozen component `(0,1,0,1)`:

`-89350652201/169388331840`

which is exactly the previously frozen Lane B value.

Frozen scalar control:

`433508011369185071313333891829231313950116629/312885874482554842907489423863612273152000000`

which is the previously frozen Lane B scalar.

## Payloads and artifacts

Extraction payload SHA256:

`10e3aabb676c56ebf240a04cd7eea1b9c90304579c8792d858790a7de5988b84`

Terminal payload SHA256:

`cb12107f846dbe74c13536500fa8449d5e9e1797428bf12bb8e62f32f34e2eba`

Jobs:
- source_lock: `105812343372`
- extraction: `105812379142`
- terminal: `105812432967`

Artifacts:
- source lock: ID `10573922598`, `sha256:70fc8a8b3148ed1109e8dbbea4ed0bd915bcf8830661e4f9691e1b7dafd96829`
- extraction: ID `10574708082`, `sha256:65b9af2234404a9bc8c72d7b9de24dbe22db58d13da5b5a73a3e8690a28e80a2`
- terminal: ID `10574678132`, `sha256:c3a03181a9e50580f293741b06528448fa4c88249de246600c232a50bbf7a59f`

All jobs completed successfully.

## Scientific consequence

The legacy univariate C discrepancy is now causally explained within the frozen finite witness: it omitted mixed-coordinate local-jet information needed to reconstruct the complete `dGamma(j=0)` object.

An independent target-blind full multicoordinate construction reproduces the shared connection factors and the complete Lane B tensor exactly.

This strengthens Lane B relative to Lane A for the frozen repository GammaGamma definition, but does not yet authorize historical formula repair. A separate prospective formal identity gate should determine whether the implemented Lane A tensor-Hessian construction is structurally the exact negative of Lane B in an abstract source-monomial basis, rather than only on the finite numerical witness.

## Locks

Legacy results remain immutable. `c6=SYMBOLIC_UNFIXED`; corrected Q10 remains locked; `theory_established=0%`; no experimental confirmation; no global Weyl3 theorem, quantum-unitarity, UV-completion, physical-c6, or new-physics claim is authorized.
