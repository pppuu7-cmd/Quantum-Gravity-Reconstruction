# COVARIANT_WEYL3_A7_FIRST_IBP_FI_JET_CAUSAL_AUDIT — TERMINAL CAUSAL LOCALIZATION

Date: 2026-09-19
Status: **TERMINAL / EXACT FI-FIRST-JET CAUSAL LOCALIZATION**

## Frozen authority

- Gate: `COVARIANT_WEYL3_A7_FIRST_IBP_FI_JET_CAUSAL_AUDIT`
- Scientific preregistration: `ae2024bd8179f84c7b9ef3b2412d6cad088f5748`
- Implementation binding: `2a36bcd4c4529644f4847cd49f46e92ac5f3ac38`
- Parent terminal lower-order result: `6ccfededab41dbe01b071916a5aa746491273276`
- Execution binding: `c48cbf206a14d1d605ec027a9f46518bf6959ff7`
- Frozen witness: `OFFSHELL_A / d=7`
- Execution-only PR: `#34`
- Production head: `4d4ab10032895644e13ad9c6ca055edc8edacbdc`
- Authoritative Actions run: `35404041767`
- Workflow run number: `1`

## Jobs

- source lock: `105789962873` — completed / success
- Researcher: `105789995537` — completed / success
- Critic: `105789995598` — completed / success
- terminal: `105790197607` — completed / success

## Immutable artifacts

Source lock:
- ID `10571805900`
- ZIP SHA256 `ec4ff11b753ddea68bebcffb61485c790df197a6800f98186d95626900829bcb`
- canonical payload SHA256 `e41187115e37e5713ec915f94cf333d292eefac89b208b001cadc87b55e3dd06`
- raw JSON SHA256 `ddfc14953d3601461555e53c811934a90b8d9a20d2a316ba9795f4471eb1950d`

Researcher:
- ID `10572260744`
- ZIP SHA256 `27091013ebf0bf302e6f27ab2fdd66a8faaff789c5431979270d0d1512e80023`
- canonical payload SHA256 `f2d71d9089db72fcc82c8b6f9b120219fd10fc270179dc5a08515d8d0bea79e0`
- raw JSON SHA256 `e6daf1a807b273acf78c7f9cf50a9518c7cd17ff1beb4130213f1965f08a0d25`

Critic:
- ID `10571238870`
- ZIP SHA256 `6a590f965c65011ba5f7f7c0fe6be7843745f77ea0975f4c5594a562331c2387`
- canonical payload SHA256 `4da30ffd0040b1ef8d3b3b4166c520424d603914f95e7e02458ca06f8187f622`
- raw JSON SHA256 `67eb162d947cdd762a159a9a85fa4e36888ef740331f3631edd4231c3342a707`

Terminal:
- ID `10571826092`
- ZIP SHA256 `296eb86bee7ef34a8304d964efa83a212c193d0eb3a17eb3fcc87d568a0fba59`
- canonical terminal payload SHA256 `70b9c00e22e12b0c4cc3870f111d502640a1d593058eca93294dea327044d4df`
- raw terminal JSON SHA256 `0ee7b87cda52d2949d6b144d423f345caee07d4e658c5c75e0b0767926fe1327`

All downloaded ZIP digests and canonical payload hashes were independently recomputed and match the immutable Actions authorities.

## Source/provenance lock

Source lock completed successfully before either lane was compared.

Frozen controls include:
- preregistration ancestry exact;
- implementation-binding ancestry exact;
- parent-terminal ancestry exact;
- all frozen Git blobs exact;
- Researcher/Critic import boundaries exact;
- terminal comparator imports neither scientific lane;
- exact Fraction arithmetic;
- no tolerance classifier patterns;
- frozen `OFFSHELL_A / d=7`;
- `c6=SYMBOLIC_UNFIXED`;
- corrected Q10 locked.

## Terminal classification

`FI_FIRST_JET_DIVERGENCE_LOCALIZED`

This is a causal localization of the already terminal first-IBP discrepancy. It does not repair or reclassify the parent covariant FAIL.

## Pointwise Fi controls

All four pointwise ordered `Fi` coefficients agree exactly between Researcher and Critic.

Therefore the first disagreement is not the pointwise first-derivative coefficient itself.

## First lexicographic Fi first-jet divergence

The prospectively frozen comparator scans

`(0,0),(0,1),...,(3,3)`.

The first exact nonzero difference is:

`(i,j) = (0,0)`.

Researcher `d_0 F_0`:

`-43977684225232401744358310400305192156031283/25865232290557867013685792372725281247232000`

Critic `d_0 F_0`:

`-13469266506757221030260385050166541/4364950942592885650296098808000000`

Exact Researcher - Critic difference:

`433508011369185071313333891829231313950116629/312885874482554842907489423863612273152000000`

This is the sign-reversed magnitude of the already frozen `-d_0F_0` transfer discrepancy, as required.

## Frozen source-class audit at (0,0)

Source comparison order was frozen before production:

1. metric jet;
2. inverse-metric jet;
3. curvature/Weyl jet;
4. connection jet;
5. perturbation jet.

### METRIC_JET

Researcher: `0`

Critic: `0`

Difference: `0`.

### INVERSE_METRIC_JET

Researcher: `0`

Critic: `0`

Difference: `0`.

### CURVATURE_WEYL_JET

Researcher = Critic:

`939210883930868332881632952475354333/896269926879072520194132288576000000`

Difference: `0`.

### CONNECTION_JET — FIRST SOURCE-CLASS DIVERGENCE

Researcher:

`433508011369185071313333891829231313950116629/312885874482554842907489423863612273152000000`

Critic:

`0`

Difference:

`433508011369185071313333891829231313950116629/312885874482554842907489423863612273152000000`

### PERTURBATION_JET

Researcher = Critic:

`-4218102777971557173922313490826813/1020421169122283704205843212800000`

Difference: `0`.

The five source classes reconstruct the complete `d_0F_0` value in each lane exactly, and their difference reconstructs the exact first-jet discrepancy without residual.

## Parent first-IBP transfer remains reproduced

Researcher scalar first-IBP transfer:

`104066723498211449276620363852984587683767158491/6846679135735905974210945039839045036032000000`

Critic scalar first-IBP transfer:

`91653430140870514219093059175268861573353/4700039496553856295898029721292544000000`

Exact difference:

`-86355995554365317186893343264769708206041673/20078237934709401683903064632959076352000000`

Thus the new audit is exactly consistent with the parent lower-order terminal result.

## Scientific interpretation

The causal frontier is now:

`pointwise Fi = MATCH`

`first Fi jet d_j Fi = first mismatch at (0,0)`

and, within that first slot:

`metric jet = MATCH`

`inverse-metric jet = MATCH`

`curvature/Weyl jet = MATCH`

`CONNECTION_JET = FIRST SOURCE-CLASS MISMATCH`

`perturbation jet = MATCH`.

Under the prospectively frozen implementation semantics, the Researcher direct metric lineage contains a nonzero derivative of the pointwise-vanishing quadratic-connection contribution, while the frozen Critic `Fi` polynomial contains no explicit connection-dependent first-derivative coefficient and therefore serializes `CONNECTION_JET=0`.

This identifies the first exact mathematical/implementation interface at which the two frozen constructions cease to be equivalent. It does **not** yet determine whether the ultimate cause is a missing covariantization term, an index/connection derivation error, or another derivational inequivalence. That adjudication requires a separate prospective successor.

## Locks

- Parent covariant classification remains `SCIENTIFIC_FAIL_COVARIANT_WEYL3_DIRECTIONAL_VARIATION_DISCREPANCY`.
- Parent lower-order classification remains `LOWER_ORDER_LOCALIZED_EXACT`.
- No post-hoc correction is authorized.
- `c6 = SYMBOLIC_UNFIXED`.
- corrected Q10 remains LOCKED.
- `theory_established = 0%`.
- no global QGR, Weyl3 proof/falsification, quantum-unitarity, UV-completion, physical-c6, experimental, or new-physics claim is authorized.
