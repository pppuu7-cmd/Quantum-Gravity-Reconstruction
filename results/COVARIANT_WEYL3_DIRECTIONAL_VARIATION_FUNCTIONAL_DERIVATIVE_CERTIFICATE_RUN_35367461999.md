# COVARIANT_WEYL3_DIRECTIONAL_VARIATION_FUNCTIONAL_DERIVATIVE_CERTIFICATE — TERMINAL SCIENTIFIC FAIL

Date: 2026-09-18

## Frozen authority

- Gate: `COVARIANT_WEYL3_DIRECTIONAL_VARIATION_FUNCTIONAL_DERIVATIVE_CERTIFICATE`
- Scientific preregistration: `8c21ee233423deaff52d0fa552c027fa065a53a7`
- Frozen panel commit: `1642dc7ca4204a4240635be68522f1731c8a9c50`
- Neutral panel generator commit: `03377afec95801b5a49f47b85ddd9c9bf3326ac0`
- Frozen panel manifest SHA256: `f1390bc406d0db37fe10cc908db51c2eabcf5105904e4a71cc707d2dd3137c5f`
- Researcher implementation commit: `e7e36ee1b42ea5c9c685c1e44e4948619f72c880`
- Critic implementation commit: `d3b56aa891cd0b505720564d367c143138ad4862`
- Terminal comparator commit: `33615223896e575d7db51259f7cf5d10c627f546`
- Static independence audit commit: `73c2f342dcc19346019687f8dba3d163aee39106`
- Production workflow commit: `53355de38a1b21128f30595de56500e04b0a4db5`
- Exact execution identity binding: `c516eab11cfd70dc81f2b5c92b60cf9c194d483f`
- Execution-only PR: `#31`
- Production head: `bef30cb0fa1b1aa0db20eb5486c8354bdb8400cd`
- Authoritative Actions run: `35367461999`
- Terminal job: `105673558207`

## Static/source lock

Source-lock job `105673256654` completed successfully before either lane was cross-compared.

Runtime static classification:

`PASS_STATIC_INDEPENDENCE_AND_SOURCE_LOCK_AUDIT`

Static audit payload SHA256:

`2c508ca9857c506a5473664f6031b2c951eec21d7723e46873a96edbca4eb55e`

The audit established on the production blobs that:
- both scientific lanes import from QGR only the frozen neutral panel generator;
- neither imports historical `qgr_iter*` science helpers;
- neither imports or references the other scientific lane;
- no floating/tolerance equality pattern is used;
- the panel manifest is exactly the frozen six-cell manifest;
- every cell contains 700 metric-jet entries and 150 perturbation-jet entries.

## Immutable artifacts

Source lock:
- `10557281116`, digest `sha256:a5fd90dca56b18ffd82f2349eeb3793f54b09db5a1862c37d69f235bd056932a`

Researcher:
- FLAT_CONTROL d=7: `10557201236`, digest `sha256:3a3b21f23ff327118e2c9b22416511902780e42b978ef00b7741107bca6f7a5f`
- FLAT_CONTROL d=19: `10557555869`, digest `sha256:1466443499126f463b25f9787790bd819d51197313656e126e7dfe4786284e9a`
- OFFSHELL_A d=7: `10556807770`, digest `sha256:db22b1855d1c37db856036ea6e73a27a1e82daece704fa9322a5d959059a0143`
- OFFSHELL_A d=19: `10556473036`, digest `sha256:6b5e06f91a82926d01fddb4dcea8e9f00fd3ada6150f50cae4375d76bc949787`
- OFFSHELL_B d=7: `10557620724`, digest `sha256:4ee06eae783715c1435f9118e1a25d40122f3fd3601168aa95f7972a1d389842`
- OFFSHELL_B d=19: `10557386227`, digest `sha256:9293feba124a9d284b9bd7e88b7cd3536031ec0527076c14c9c7d837ca3e5bd1`

Critic:
- FLAT_CONTROL d=7: `10557081360`, digest `sha256:affb92437684974933d42418388ca7d55e791b06e2e5e14c9e1c001df004980a`
- FLAT_CONTROL d=19: `10556582901`, digest `sha256:22fa7b3da3251467f746e0dcfe4a84e28b97130d9aa482875c7c099b8c430e30`
- OFFSHELL_A d=7: `10556747806`, digest `sha256:1002a866b1351dbed586c3b2ba1b77cc5a9ae0e07f72ef435d659ea29f4b0bb3`
- OFFSHELL_A d=19: `10556897597`, digest `sha256:ccf925a0a6408e8b926c693fa367328c4e934ddfaeba72d622a0b583b4b8c7f2`
- OFFSHELL_B d=7: `10556787707`, digest `sha256:6b965ba4994afc2963805aaab2e4a2c87f843cad3d1309780177991c43c522f9`
- OFFSHELL_B d=19: `10557006437`, digest `sha256:af4ff7f62af7fd481a42934036d7dd26941d6140e542e3c646d249eb6dec8e69`

Terminal:
- `10557296351`, digest `sha256:42c21bfeade622a0b54c723ddb8b7eff5326f3a409c8a75eaea21c4bf9a8b217`

Frozen terminal payload SHA256:

`5bf2bdb5a83414ba9545c6cd236255a5975455198145f04d7a870b7173a2aacf`

## Terminal classification

`SCIENTIFIC_FAIL_COVARIANT_WEYL3_DIRECTIONAL_VARIATION_DISCREPANCY`

This is a valid scientific discrepancy, not an execution failure.

All six Researcher witnesses and all six Critic witnesses passed their frozen self-controls. Target-blind serialization completed before cross-lane comparison. The comparator reports no Researcher or Critic execution errors.

The two implementations agree exactly on the common pre-functional-derivative domain in every frozen cell:
- full metric and perturbation jet table;
- jet hash;
- point Riemann tensor;
- point Ricci tensor;
- point scalar curvature;
- point Weyl tensor;
- point `I3`.

Therefore the discrepancy is downstream of the common curvature/invariant construction. The current earliest localized divergent object is:

`POST_COMMON_CURVATURE__DIRECT_VARIATION_IBP_VS_INDEPENDENT_EULER_SOURCE`.

## Exact six-cell result

| seed | direction | direct bulk | independent Euler contraction | exact difference |
|---|---:|---:|---:|---:|
| FLAT_CONTROL | 7 | 0 | 0 | 0 |
| FLAT_CONTROL | 19 | 0 | 0 | 0 |
| OFFSHELL_A | 7 | `141609523517262295106976925021598088976553029/33325122725952586818549169405591839744000000` | `36188861490208135407463132950092941670313420227/2815972870342993586167404814772510458368000000` | `-86355995554365317186893343264769708206041673/10039118967354700841951532316479538176000000` |
| OFFSHELL_A | 19 | `3611260164113818842475843645874600632309080143/177398821407549330693569931965111733120000000` | `1787301684805851900667604464398846150973240627/72068271196816915594262784860826641580000000` | `-683151452020507724611825030959551240741710547/153745645219876086601093941036430168704000000` |
| OFFSHELL_B | 7 | `-1264850993026258270264267344895666763735466059/24068144190965757146729955681816328704000000` | `-58258903055522328784299647179990199722258682579/1251543497930219371629957695454449092608000000` | `-2504449527281033756480751584861490663995184163/417181165976739790543319231818149697536000000` |
| OFFSHELL_B | 19 | `-73218576704505033207312703533646819667533447579/28186701623643949210200555856678864262400000000` | `7854133829202633916846897628109864596497044169/2013335830260282086442896846905633161600000000` | `-12211763354222793869544618021812328267899471063/1879113441576263280680037057111924284160000000` |

The smallest frozen-order exact counterexample is OFFSHELL_A, direction 7.

## Interpretation

The negative result does **not** invalidate the already terminal corrected Iter057Y response or the Einstein-completed QF degree-flow result. It says that the present independent 4D covariant Euler-source construction and the direct directional-variation-plus-IBP construction do not define the same bulk functional derivative on the frozen off-shell panel.

Because common curvature and `I3` agree exactly, the next admissible scientific task is causal term-level localization of the first off-shell counterexample, not a sign flip, rescaling, change of `c6`, panel replacement, symmetry reduction, or Q10 computation.

Candidate localization axes, in frozen causal order:
1. determinant / explicit metric variation contribution;
2. curvature/Weyl directional variation contribution before IBP;
3. first-derivative IBP transfer;
4. second-derivative IBP transfer;
5. algebraic `P.R` Euler term;
6. covariant double-divergence `2 nabla nabla P` term;
7. metric `+1/2 g I3` term;
8. final index placement/contraction.

A new prospective gate is required before altering or adjudicating any of these terms.

## Locks

`c6 = SYMBOLIC_UNFIXED`.

Corrected Q10 remains LOCKED.

`theory_established = 0%`.

No global variational theorem, unique theory, quantum unitarity, UV completion, regulator removal, interacting measure, experimental confirmation, new-physics claim, or physical `c6` determination is authorized.

No post-hoc repair of this terminal result is authorized.
