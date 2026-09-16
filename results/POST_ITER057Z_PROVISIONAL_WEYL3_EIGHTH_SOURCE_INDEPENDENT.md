# Post-Iter057Z provisional corrected-dodecic Weyl3 eighth source

Date: 2026-09-16

Status: **INDEPENDENT REPRODUCIBLE PROVISIONAL PASS — NOT CANONICAL UNTIL OFFICIAL ITER057Z TERMINALIZATION**

Upstream frozen main state at execution: `fd714a08654b4e8679311ca3bf37e218100d627b`, where recovery still marks `ITER057Z-DODECIC-EINSTEIN-SEED-COMPLETION` as prospectively preregistered with implementation not yet launched.

Independent provisional R12 authority used here: the twice-reproduced artifact-only Iter057Z result from branch `research/iter057z-independent-20260916`, with complete result JSON SHA-256 `4bf91f50a017e1ad83d9c85d231ca116d83f968bdda6dc2c142abfd563fb20b4` and exported R12 JSON SHA-256 `f030a326fe19a289c27fb2617665621dc2124434b61b62812867508323fe1c43`.

## Question

On the independently completed dodecic Einstein seed

`g12 = eta + G2 + R4 + R6 + R8 + R10 + R12`,

what is the exact corrected-seed Weyl-cubic Euler source `Shat_ab=-E_W3,ab` through coordinate degree eight, and do the inherited tensor identities and lower-source replay remain exact?

Because official Iter057Z has not terminalized on `main`, this computation is deliberately not assigned an official Iter057AA-style gate and does not create canonical coefficient authority.

## Independent implementation

The evaluator extends the previously independent artifact-only Iter057X tensor chain and does not consume any future post-Z source implementation. It reconstructs the seed from already-terminal Iter057O/Q/T/W coefficient authorities plus the independent pure-degree-12 R12 particular. All polynomial/tensor arithmetic is exact Python `Fraction` arithmetic; no floating zero tolerance is used.

Required truncations were raised prospectively before seeing the result:

- inverse metric through coordinate degree 10 using the exact Neumann series through `h^5`;
- Christoffels through degree 11;
- Riemann/Weyl and `P=dI3/dR` through degree 10;
- `I3` and `P.R` through degree 8;
- first covariant divergence of `P` through degree 9;
- double divergence and Euler tensor through degree 8;
- Noether divergence through degree 7.

The four-index raising of `P` was implemented as four exact sequential contractions rather than one 4^4 direct contraction per output component. This is algebraically identical but reduces polynomial multiplications substantially; it changes no tensor convention or truncation.

## Exact result

Classification used only for this research branch:

`REPRODUCIBLE_PROVISIONAL_PASS_POST_ITER057Z_CORRECTED_DODECIC_SEED_WEYL3_SOURCE_EXACT_THROUGH_EIGHTH_EVEN_ORDER__NOT_CANONICAL_UNTIL_OFFICIAL_Z`

Source nonzero counts by coordinate degree:

- degree 0: `4`;
- degree 1: `0`;
- degree 2: `22`;
- degree 3: `0`;
- degree 4: `64`;
- degree 5: `0`;
- degree 6: `140`;
- degree 7: `0`;
- degree 8: `260`.

Degree-eight source statistics:

- nonzero normalized coefficients: `260`;
- time-containing: `170`;
- off-diagonal: `120`;
- natural factorization: `Shat/kappa^7`.

`I3(0)/kappa^3 = 96`.

Canonical compact serialization of the complete sparse source has SHA-256:

`ab993fd4c987272208831d5c5ff2c24c905d5a11625a65b58fff8012e2c4f828`.

The complete pretty-printed result JSON file has SHA-256:

`6ef4e67ece3de8b00731c8b37bccca49ec28c99213d61a0ef4f9153daa8a7a1a`.

The degree-eight-only CSV has SHA-256:

`76e4f10a8d4533627d83de8f5fc7d5feb99216f924f2c17ed94ccd107ca62d2c`.

The complete even source CSV through degree eight has SHA-256:

`3a562fe21c3fed1d9756ac97b7abbe79a1fc2031fb574ba4a76b06b6faa34687`.

A second clean execution produced a byte-identical complete result JSON and the same source digest.

## Exact controls

Every frozen-for-this-reproduction control passed:

- R4/R6/R8/R10 terminal inputs and independent R12 input have the expected counts and pure degrees;
- R12 count `469`;
- inverse identity through coordinate degree 10 exact;
- Ricci tensor, scalar curvature and Einstein tensor through coordinate degree 10 exactly zero;
- direct tensor construction of the Weyl3 Euler source through degree 8;
- `P.R = 3 I3` through degree 8 exactly;
- lowered Euler tensor symmetric through degree 8 exactly;
- trace Ward identity through degree 8 exactly;
- covariant Noether divergence through degree 7 exactly zero;
- every odd source coefficient at degrees 1, 3, 5 and 7 exactly zero;
- complete lower-source replay at degrees 0/2/4/6 against the independent Iter057X certificate: 230 expected, 230 actual, zero missing, zero extra and zero unequal values;
- complete symmetric-tensor basis accounting through degree 8: `10+40+100+200+350+560+840+1200+1650 = 4950`.

## Scientific interpretation and lock

This result is useful preproduction evidence for the next source gate, but it is not canonical authority because the R12 input is not yet an official terminal Iter057Z coefficient authority on `main`. Once official Z terminalizes, the correct next check is a strict coefficient/digest comparison of official R12 against the independent R12 used here. If they coincide, this source can be independently replayed against the official seed; if they differ by homogeneous freedom, the degree-eight source must be recomputed on the official canonical R12 rather than promoted by assumption.

This establishes no all-orders/convergence/global solution, no value/sign/running of `c6`, no `beta=1`, no hyperbolicity/ghost/unitarity/UV-completion/experiment/new-physics claim, and no quantum-gravity completion. `c6` remains symbolic/unfixed and theory-established remains `0%`.
