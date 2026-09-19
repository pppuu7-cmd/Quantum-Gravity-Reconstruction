# Preregistration — COVARIANT_WEYL3_A7_CONNECTION_MULTICOORDINATE_NEUTRAL_EXTRACTION

Date: 2026-09-19
Status: **FROZEN BEFORE MULTICOORDINATE IMPLEMENTATION / NO PARENT REPAIR AUTHORIZED**

## Parent authority

Terminal primitive-localization result:
- gate `COVARIANT_WEYL3_A7_CONNECTION_COMPONENT_0101_PRIMITIVE_CAUSAL_DECOMPOSITION`;
- run `35411484392`;
- durable result commit `199ecea77c9138c4a166d1ffc7143ce2d0de34be`;
- terminal payload `bc70d3aa22ebc3a1c0f8d8e79119f6f1d12c893b4c7275343e2391abd5a440a4`.

Frozen witness remains `OFFSHELL_A / d=7 / (i,j)=(0,0)`.
Frozen component remains `(a,b,c,d)=(0,1,0,1)`.

The parent audit established:
- A and B shared inputs agree through `CONNECTION_FACTOR_CHANNELS`;
- first A/C and B/C shared-input divergence is `dGamma:0,0,0,1`;
- A = B = `1/34` on that primitive;
- legacy neutral C = `0`;
- parent full tensors remain A = -B, while legacy C equals neither sign.

These are frozen evidence, not targets to fit.

## Scientific question

Does a genuinely multicoordinate neutral polynomial local jet, constructed directly from the frozen repository metric and perturbation jets without importing either hand-derived connection formula, restore the mixed-coordinate connection factors required by the component `(0,1,0,1)`? If so, does its exact `[eps*x0]` GammaGamma tensor agree with frozen Lane A, frozen Lane B, or neither?

## Prospective neutral construction

Use exact rational arithmetic in the truncated polynomial ring

`Q[eps,x0,x1,x2,x3] / (eps^2, coordinate total degree > 2)`.

Construct the background metric locally from the frozen exact jets:

`g_ab(x) = eta_ab + (1/2) sum_{p,q} g_ab,pq x^p x^q`

with the symmetric Taylor convention implemented so that mixed `p != q` derivatives are represented exactly once with their correct coefficient.

Construct the perturbation for frozen `phi=x0` as

`delta g_ab = eps * x0 * ( h_ab + sum_q h_ab,q x^q )`

to coordinate degree two.

Then:
1. invert the full multicoordinate metric polynomial exactly to the frozen truncation;
2. construct Christoffel symbols directly from coordinate differentiation of the polynomial metric;
3. verify `Gamma(0)=0`;
4. extract every background coefficient `[x0] Gamma^a_bc` and verify it equals the frozen repository `dGamma(j=0,a,b,c)` for all 64 channels;
5. extract every perturbative coefficient `[eps] Gamma^a_bc` and verify it equals the frozen `deltaGamma_phi(i=0,a,b,c)` for all 64 channels;
6. only after those target-blind connection-factor controls pass, construct the repository-defined all-lowered GammaGamma Riemann contribution and serialize the full 256-component `[eps*x0]` tensor;
7. compare the serialized neutral tensor to the already frozen A and B tensors.

The extraction implementation must not import either A or B implementation helper and must not contain either frozen A/B tensor hash or scalar target.

## Frozen controls

Mandatory before comparison:
- exact preregistration and parent-terminal ancestry;
- exact source/blob lock;
- exact rational arithmetic, no tolerance;
- full multicoordinate inverse identity through the frozen truncation;
- background first metric jets zero;
- `Gamma(0)=0`;
- all 64 `dGamma(j=0)` channels reproduce the repository jet formula exactly;
- all 64 `deltaGamma_phi(i=0)` channels reproduce exactly;
- frozen component `0101` and full 256 tensor serialized before A/B target access;
- legacy C result remains immutable and is not reclassified;
- `c6=SYMBOLIC_UNFIXED`;
- corrected Q10 remains locked.

## Frozen terminal taxonomy

- `MULTICOORDINATE_NEUTRAL_EXTRACTION_MATCHES_LANE_A`
- `MULTICOORDINATE_NEUTRAL_EXTRACTION_MATCHES_LANE_B`
- `MULTICOORDINATE_NEUTRAL_EXTRACTION_MATCHES_NEITHER`
- `BLOCKED_EXECUTION_OR_PROVENANCE`

If mandatory connection-factor controls fail, classification is `BLOCKED_EXECUTION_OR_PROVENANCE`, not scientific mismatch.

## Interpretation ceiling

A match with A or B would adjudicate the neutral local-polynomial realization of the frozen connection term at this finite exact witness. It would not authorize rewriting historical terminal results, fixing c6, unlocking Q10, or claiming a global Weyl3 theorem, quantum unitarity, UV completion, experimental confirmation, or new physics.

`theory_established=0%`.
