# Iter057AC independent exact normalization audit

Date: 2026-09-16

Status: **INDEPENDENT REPRODUCIBLE IMPLEMENTATION-NORMALIZATION AUDIT PASS**

Branch point: `f78257ee04ae6ff3648cf25aa8bd5a5fbaaa0dc7` on `main`. Historical terminal Iter057AC (`905fc6f4fdfd06da73802c4442c746db5e6d87e6` / `daa73d8d6b0da31654e3349234a5783445d23c28`) records `SCIENTIFIC_FAIL_ITER057AC_AFFINE_INCOMPATIBILITY`; Iter057AD/AE/AF then study the obstruction inherited from that implementation. This audit does not rewrite those historical commits. It tests whether the Iter057AC implementation realizes the normalized Taylor coefficient convention prospectively frozen by its preregistration `0794406a04945b6b9999361c63d9f0964519ec30`.

## Diagnosis

The preregistered correction is a normalized Taylor jet

`delta qbar_ab^(14)(x) = sum_{|beta|=14} R14_ab[beta] x^beta / beta!`.

For that basis, the principal field operator `-1/2 Box` maps a normalized coefficient `R14[alpha+2 e_m]` to the normalized target coefficient with matrix entry `-eta_m/2`. This is exactly the convention implemented by `qgr_iter057ac_tetradecic_einstein_seed_completion.py::system()`.

However, the same implementation constructs the fresh affine RHS directly from the polynomial dictionary value `Ein_ab.get(alpha)`. Those dictionaries store ordinary monomial coefficients of `x^alpha`, not normalized Taylor coefficients. Therefore the RHS supplied to the normalized matrix is missing the required factor `alpha!` (and, when solving directly for the persisted `R14_over_kappa7` authority, the common `kappa^7` scale must also be removed consistently).

A concrete one-entry witness is enough to expose the mismatch. For `beta=(0,0,0,14)`, `alpha=(0,0,0,12)` and the z second derivative, the implemented matrix entry is `-1/2`. That is correct for `x^beta/beta!`. If the unknown were instead an ordinary monomial coefficient of `x^beta`, the entry would have to be `-(14*13)/2 = -91`. Conversely, keeping the implemented normalized matrix requires multiplying the ordinary target monomial coefficient by `alpha! = 12! = 479001600` before it is used as the RHS.

Thus the production Iter057AC affine calculation mixes a normalized matrix convention with an unnormalized RHS convention.

## Exact A/B reproduction

The audit uses the same canonical lower seed through terminal R12, the same unrestricted 6800-dimensional pure degree-14 correction space, the same `6790 x 6800` structural matrix and the same complete 1456-dimensional Bianchi/Noether family. It changes no seed coefficient, no ansatz, no rank target and no scientific acceptance criterion. The only A/B operation is conversion of the freshly recomputed ordinary polynomial RHS into the normalized Taylor coefficient convention already frozen by the preregistration.

On the **raw implementation RHS** the audit independently reproduces the historical Iter057AC symptom exactly:

- matrix shape `6790 x 6800`;
- exact structural rank `5334`;
- Bianchi rank `1456`;
- raw `O0=L r0` nonzero count **223**;
- raw Bianchi compatibility nonzero count **223**.

On the **factorial-normalized RHS**:

- the normalized RHS agrees coefficient-for-coefficient with the independent symbolic-kappa normalized engine: mismatch count **0**;
- all **1456/1456** Bianchi/Noether contractions vanish exactly;
- `rank(M)=rank([M|r])=5334`;
- exact affine residual failure count **0**;
- the deterministic particular contains **721** nonzero normalized `R14_over_kappa7` coefficients;
- ordered particular digest: `e24d13bc2110d842e48ac475511b7ca1a33fb445cf5a5598ccedd08921864192`.

Crucially, the complete ordered 721-coefficient particular is **exactly identical** to the independent pre-Iter057AC R14 prediction computed before the official Iter057AC FAIL existed.

## Independent nonlinear replay

The corrected particular was then inserted into a separate plain-polynomial unreduced nonlinear geometry evaluator using the canonical lower seed. Exact controls give:

- inverse identity through coordinate degree 12: pass;
- flat de Donder through coordinate degree 13: exact zero;
- Ricci tensor through coordinate degree 12: exact zero;
- scalar curvature through coordinate degree 12: exact zero;
- Einstein tensor through coordinate degree 12: exact zero.

Therefore the factorial correction is not merely a linear-algebra reinterpretation: the resulting R14 solves the independently reconstructed nonlinear finite-order equations exactly.

Audit classification:

`INDEPENDENT_EXACT_AUDIT_ITER057AC_IMPLEMENTATION_NORMALIZATION_MISMATCH__FACTORIAL_CORRECTED_NORMALIZED_SYSTEM_PASSES`

Scientific payload SHA-256:

`ef2fa1bb4261a879671b21af88696070ef3d6f6586e05756f1b3ca5087e831f1`

## Reproducibility

Two clean audit executions produced byte-identical result JSON and byte-identical corrected R14 JSON. A self-contained bundle was then unpacked in a fresh directory and executed using only bundle-relative inputs; it reproduced both references byte-for-byte.

Stable hashes:

- audit result JSON SHA-256: `1fffb8421d68a8e3df44920578a9d99064a9c93bc2765b42d3de57fd18c1f143`;
- corrected ordered R14 JSON SHA-256: `71e104d95dd266bd4b466e582d5dad149b65910849642c23e7de8afd95e0659b`;
- corrected R14 CSV SHA-256: `fb3a173cd375481ef504ce57de67908abc0a8ac9336445942ea8e0c29506365e`;
- self-contained audit reproduction ZIP SHA-256: `4ec5d555ad5e46546e26b00470d5a973dd7d3bbe932ddea59f35dab385f5d357`.

## Consequence for AD/AE/AF

The historical AD/AE/AF obstruction chain is internally meaningful for the affine object inherited from the raw Iter057AC implementation. In fact, an independent sparse reconstruction of all 1114 historical obstruction columns gives exact `rank_Q(B)=1110`; modular exact lower bounds plus the one-column augmentation give `rank_Q([B|-O0_raw])=1111`, so the raw inherited obstruction cannot be lifted by the R12 homogeneous branch.

That does **not** establish an obstruction for the prospectively frozen normalized Iter057AC scientific object, because its canonical corrected `O0_normalized` is identically zero before any R12 branch motion. The active Iter057AF aggregate implementation explicitly recomputes `O0` through the unchanged Iter057AD/Iter057AC evaluator and therefore inherits the same raw-RHS convention.

The scientifically clean continuation is a new prospective corrective gate that freezes the normalized coefficient convention explicitly, reproduces the A/B witness above, and re-executes the Iter057AC seed-completion decision without editing historical evidence. Corrected Weyl3 source degree ten should remain unauthorized until that corrective gate is durably terminalized.

## Scope ceiling

This is a correctness/normalization audit of one finite local affine Taylor gate. It does not establish all-orders convergence, open-neighborhood/global/asymptotic existence, a value/sign/running of `c6`, `beta=1`, physical characteristics, strong hyperbolicity, stability/ghost claims, quantum unitarity, regulator removal, a global interacting measure, UV completion, experimental confirmation, new physics or QGR correctness.

`c6` remains symbolic/unfixed and theory-established remains `0%`.
