# Iter057AK terminal result — full dual-kernel parity/symmetry obstruction decomposition

Date: 2026-09-16
Gate: `ITER057AK-FULL-DUAL-KERNEL-PARITY-SYMMETRY-OBSTRUCTION-DECOMPOSITION`
Preregistration: `e9f3003c7a7b2e776961f60f5e4f493c6744b146`
Durable authority manifest: `96a9034452adfc05bd69cfe53abe26ff4d4b23d5`

## Terminal classification

**`PASS_SCOPED_ITER057AK_FULL_DUAL_KERNEL_DECOMPOSITION_IDENTIFIES_UNIQUE_AH_PARITY_OBSTRUCTION_CHANNEL`**

## Why cross-background transport was not launched

The pre-gate admissibility audit found no source-faithful set of multiple independent terminal on-shell R12 backgrounds in the current programme. The frozen Iter057Z/AF lineage is one canonical R12 seed family plus its 1114-dimensional homogeneous R12 branch; Iter057L is only a first-order local correction jet and explicitly does not establish a corrected on-shell background to the required order. Therefore a held-out cross-background transport gate could not be defined without inventing backgrounds or a post-hoc transport map. That direction is recorded as **BLOCKED AS FORMULATION**, not as a physical/scientific FAIL.

## New exact scientific fact

On the unchanged terminal Iter057AF object `B x = -O0`:

- `B` has shape `1456 x 1114`, `nnz=80982`, `rank(B)=1110`;
- `rank([B|-O0])=1111`;
- `dim ker(B^T)=346`;
- `dim(ker(B^T) cap O0^perp)=345`; hence the obstruction quotient is exactly **one-dimensional**;
- the frozen `(b, beta mod 2)` partition has 32 nonempty sectors;
- only four sectors contain support-local kernel directions, all at `b=0` and single-odd-coordinate parity, with total support-local kernel dimension `4`;
- exactly one sector is obstruction-active: **`0:1000`**, the AH odd-time/even-spatial sector;
- the three spatial-odd local kernel directions `0:0100`, `0:0010`, `0:0001` pair exactly to zero with `O0`;
- the remaining **342/346** kernel directions are genuinely cross-sector and cannot be represented by a vector supported in one frozen parity/component sector;
- a freshly constructed normalized witness in `0:1000` satisfies exactly `B^T y=0`, `O0^T y=1` and matches the AG coefficient vector coefficient-by-coefficient.

Thus the AH/AJ channel is not merely one convenient certificate: within the preregistered support-local sector decomposition it is the **unique obstruction-active channel**, while the full obstruction functional on the 346-dimensional dual kernel has rank one.

## Symmetry diagnostic

The full 346-dimensional kernel is not invariant under either preregistered naive spatial `S3` row action tested by the primary evaluator (`T_AH` and tensor-index-covariant `T_tensor`). Therefore no irrep decomposition of the **full** kernel under those actions is asserted. This does not contradict AJ: the unique AH witness itself remains S3-invariant; rather, the entire frozen dual kernel is not a representation space of those naive background-independent actions because the canonical background/system is not invariant under them.

## Reproduction and provenance

Primary exact production:

- implementation `825883cbafd59f77f70e0d099722aadd161cc1c4`;
- workflow head `5567578e4005d61808c86842b40c0651dbd4f7f0`;
- run/job `35142640910 / 104950692042`;
- artifact `10465588751`, digest `sha256:c97883369bca6f28c8e1ef855c44082adf5b5982df5748ab6bb508756fde3a66`;
- scientific payload SHA256 `ad9fcfa8797721503e0e1a55be510272cd7e8526dfc387e6bc230174241a7110`.

Independent integer-cleared Critic:

- implementation `46a910087be5110ff894dca2b5a0340a63056cdc`;
- workflow head `8349d262a8bba7d352a893c0825ad8f96fff5ecf`;
- run/job `35144194232 / 104955965064`;
- artifact `10467296436`, digest `sha256:667029b5d4af1e85e329eb7e59f1fed9094537cd0e6c70d9d35ac4c44e4ef9f3`;
- scientific payload SHA256 `2f8663fe8fb70f4b8db8850b99f2f8d4141e6413479978912c5484d08b0d3ce1`;
- exact negative controls: zero `O0` gives no active sector; scaling `O0 -> 2 O0` preserves activity; AG positive control reconstructed independently.

Supplemental fast discriminator run `35143398301`, artifact `10466297879`, digest `sha256:292effe3c5704b49aa101bebd5f28fb3628c8c77b0d4b7fcb189f7f0c646e739`, independently agrees on all 32 sector ranks/nullities/activity.

A separate local verification recomputed both terminal payload hashes and checked exact equality of all critical global fields, all 32 `(rank,nullity,activity)` entries, the lane payload hash manifest, and the AG positive control.

## Claim ceiling

This is an exact finite local structural result for the single frozen Iter057AF realization only. It does **not** establish cross-background persistence, a canonical inter-background transport, open-neighborhood or all-orders obstruction, global no-go behavior, stability/ghost/unitarity/UV claims, or experiment. `c6` remains symbolic/unfixed; `beta=1` remains unauthorized; theory established remains `0%`.

## Highest-information next gate

The remaining dominant uncertainty is background dependence. The next gate should not further cosmetically compress this certificate. It should prospectively construct and validate at least one **independent source-faithful on-shell background seed family** from a frozen pre-outcome rule, sufficient to reproduce the AF-order `B/O0` object, with one seed held out from every choice of basis/normalization/comparison rule. Only after such a second authority exists should a no-refit cross-background obstruction transport test be run. If independent background construction itself fails exact on-shell completion before the AF order, that failure is the terminal scientific result of that gate.
