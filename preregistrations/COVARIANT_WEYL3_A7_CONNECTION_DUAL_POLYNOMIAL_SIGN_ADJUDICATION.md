# COVARIANT_WEYL3_A7_CONNECTION_DUAL_POLYNOMIAL_SIGN_ADJUDICATION — prospective preregistration

Date: 2026-09-19
Status: **FROZEN BEFORE IMPLEMENTATION / BEFORE SIGN RESULT INSPECTION**

## Parent authority

Parent connection-identity gate:
- `COVARIANT_WEYL3_A7_CONNECTION_JET_IDENTITY_ADJUDICATION`;
- run `35404489570`;
- durable result commit `267743ee78ea0ebd51fd697003cc1207a9d9032b`;
- classification `CONNECTION_IDENTITY_DERIVATIONS_DISAGREE`.

Frozen witness:
- `OFFSHELL_A / d=7 / (i,j)=(0,0)`;
- point P SHA256 `21095bed2a18f7a5fa2484961c75d4cd7589115d6a6f664f0b3eee8697cdd4fe`.

Frozen parent identity values, hidden from the extraction implementation until terminal comparison:

Lane A:
`-433508011369185071313333891829231313950116629/312885874482554842907489423863612273152000000`.

Lane B:
`433508011369185071313333891829231313950116629/312885874482554842907489423863612273152000000`.

## Scientific question

Which sign is obtained by direct exact coefficient extraction from the frozen repository definition of the all-lowered quadratic-connection Riemann term, without hand-expanding either parent identity?

## Neutral polynomial construction

Use two formal variables:
- `x` representing the frozen spatial coordinate `x^0`;
- `eps` representing the metric directional-variation amplitude.

Set the scalar test function exactly to

`phi(x)=x`.

Then `phi(0)=0` and `partial_0 phi(0)=1`.

Construct the one-coordinate frozen metric Taylor polynomial directly from neutral panel bytes:

`g_ab(x)=eta_ab + (1/2) g_ab,00 x^2`.

First background metric jets are frozen zero, so no linear background term exists.

Construct the frozen perturbation Taylor polynomial

`h_ab(x)=h_ab(0)+h_ab,0 x`.

Define the perturbed metric

`G_ab(x,eps)=g_ab(x)+eps * h_ab(x) * x`.

All arithmetic is exact rational arithmetic in a bivariate truncated polynomial ring retaining:
- eps degree <= 1;
- x degree <= 2.

No Lane A or Lane B formula is imported.

## Direct extraction

From `G_ab(x,eps)`:

1. construct its exact truncated inverse metric;
2. construct the Levi-Civita connection directly from
   `Gamma^a_bc = 1/2 G^{ae}(partial_b G_ec + partial_c G_eb - partial_e G_bc)`,
   where only coordinate 0 carries x-dependence;
3. construct only the repository-frozen all-lowered quadratic-connection Riemann piece
   `R^GG_abcd = G_ef( Gamma^e_ca Gamma^f_db - Gamma^e_da Gamma^f_cb )`;
4. extract coefficient `[eps^1 x^1] R^GG_abcd`;
5. contract that 256-component exact tensor with the frozen point `P^{abcd}`;
6. serialize/hash tensor and scalar before any target comparison.

Because `phi=x^0`, the extracted `eps*x` coefficient is exactly the connection contribution to `d_0 F_0` under the repository Riemann convention.

## Mandatory controls

- exact neutral panel provenance;
- exact P hash;
- exact background first metric jets zero;
- exact polynomial inverse check through the retained truncation;
- exact `Gamma(0)=0`;
- exact rational arithmetic;
- no tolerance;
- extraction source contains neither frozen Lane A nor Lane B target numerator;
- `c6=SYMBOLIC_UNFIXED`;
- corrected Q10 locked.

## Frozen terminal taxonomy

After extraction payload is serialized:

- if extracted scalar equals frozen Lane A:
  `DUAL_POLYNOMIAL_EXTRACTION_MATCHES_LANE_A`;

- if extracted scalar equals frozen Lane B:
  `DUAL_POLYNOMIAL_EXTRACTION_MATCHES_LANE_B`;

- if it matches neither:
  `DUAL_POLYNOMIAL_EXTRACTION_MATCHES_NEITHER`;

- if a mandatory control/provenance/execution condition fails:
  `BLOCKED_EXECUTION_OR_PROVENANCE`.

No additional category is authorized after result inspection.

## Interpretation ceiling

This gate adjudicates only the sign/orientation of the already localized connection source at one frozen slot. A match does not itself modify either parent implementation.

Any correction requires a separate prospective correction gate.

No global Weyl3/QGR theorem, physical c6, corrected Q10, quantum unitarity, UV completion, experimental or new-physics claim is authorized.

`theory_established=0%`.
