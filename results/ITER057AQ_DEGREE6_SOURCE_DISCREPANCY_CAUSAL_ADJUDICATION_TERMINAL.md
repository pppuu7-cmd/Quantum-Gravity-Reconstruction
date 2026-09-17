# Iter057AQ terminal result — degree-six source discrepancy causal adjudication

Date: 2026-09-17
Gate: `ITER057AQ-DEGREE6-SOURCE-DISCREPANCY-CAUSAL-ADJUDICATION`
Preregistration: `3ac98107c7a659f63271c9836583e929bc35adb4`
Durable authority: `ce8df5af5084e2359270a14ee53ac9334b661ea4`

## Terminal classification

**`PASS_SCOPED_ITER057AQ_DISCREPANCY_LOCALIZED_TO_LEGACY_P_CONSTRUCTION`**

## Exact result

The frozen target-blind 2x2 intervention used one immutable Iter057W geometry and crossed:

- historical legacy `P_L` construction versus exact Frechet `P_F=dI3/dR`;
- historical Iter057X downstream Euler operator `O_X` versus AO/AP covariant Euler operator `O_AO`.

All exact controls passed. The Frechet tensor retained pair/antisymmetry/algebraic-Bianchi identities, `P.R=3I3`, and the deterministic nonzero Frechet directional equality `-576/10625` by both direct and contracted routes.

The two P constructions agree identically through polynomial degree seven and differ only at degree eight, in exactly **2824 tensor-polynomial entries**.

The four 2100-slot Euler cells show:

- `O_X(P_L) == O_AO(P_L)` exactly through source degree six;
- `O_X(P_F) == O_AO(P_F)` exactly through source degree six;
- replacing `P_L -> P_F` changes exactly **140** source slots, all at coordinate degree six and none below.

Cell hashes:

- `O_X(P_L)` = `O_AO(P_L)` = `23e9b6864e9cdc827d0c6f295da3fae7e9f6d005b1213e19c9fb6cb673a881cd`;
- `O_X(P_F)` = `O_AO(P_F)` = `b0d035f08a1bb1ff33b8289c5bc2bea710922f09d4e719191084fdd4d656c8ae`.

Therefore the AP degree-six discrepancy is not caused by a difference between the downstream X and AO Euler/divergence operators. It is causally localized to the historical legacy construction of `P=dI3/dR`: the legacy and exact Frechet P agree to the order needed for source degrees 0/2/4, but diverge precisely at P degree eight, which feeds the degree-six source.

## Reproduction/provenance

Implementation: `23435e772cf82c985ed919aa2411d59667ffb3ff`.
Workflow head: `c04cc004b9ef5aadcef70fd25d5129a80670335d`.
Run/job: `35178662890 / 105065884009`.
Artifact: `10479880065`, digest `sha256:9646c110a7443d63d7faa675195d784a82a66e828a9d095b5028200d30f1512a`.
Complete payload SHA256: `55b68bd9eb6ee782636e8f221a2c3d59911e87ebdca4d9da2b3c12006c166559`.
Scientific summary SHA256: `0360382c21b116679a9d93ce8b3ae2c77b3f7473f0896d043988cced15ba16a1`.

A separate local artifact verification recomputed both payload hashes exactly and replayed all six cell-pair mismatch counts.

## Consequence for authority lineage

Iter057AP remains a terminal scientific FAIL under its frozen convention map; AQ does not rewrite that preregistered outcome. AQ instead identifies the defect source that must be corrected in a new prospective gate.

The terminal Iter057X degree-six source authority and any downstream result whose degree-six RHS depends on it must **not** be silently rewritten. The next highest-information gate should prospectively reconstruct a corrected degree-six Weyl3 source on the same immutable W seed using the exact Frechet P, independently reproduce it, and then audit which descendants (beginning with the Q8-response lineage) are superseded at degree six. Lower U degrees 0/2/4 are not implicated by this AQ result because `P_L=P_F` through degree seven and the corresponding source cells agree below degree six.

## Claim ceiling

This is an exact implementation/source-authority diagnosis inside the finite local classical programme. It is not a global/all-orders theorem and makes no stability, hyperbolicity, quantum, UV or experimental claim. `c6` remains symbolic/unfixed; `beta=1` remains unauthorized; theory established remains `0%`.
