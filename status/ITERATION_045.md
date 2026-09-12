# QGR Iter045 — preregistration: relative two-polarization residue signature

Date: 2026-09-12
Status: PREREGISTERED BEFORE IMPLEMENTATION/PRODUCTION
Relation to active G44: scientifically independent; this gate uses the already-authorized Iter004 QGR-L1 Hessian and fixed incidence↔orthonormal chart only. It does not consume partial or terminal Iter044 results.

## Question
For the selected QGR-L1 quadratic two-derivative branch, do the two physical TT polarizations carry the same nonzero relative kinetic/pole coefficient on held-out null directions, without a relative sign split or polarization mixing?

## Scope
This is a quadratic/linearized spectral-structure audit only. It is NOT an absolute energy-positivity theorem, NOT a full propagator/unitarity theorem, NOT nonlinear stability, and NOT experimental evidence. The overall action normalization/sign is not fixed by this gate.

## Frozen inputs
- QGR-L1 selected Hessian authority from Iter004.
- Incidence metric `C=J-I` and the deterministic incidence↔orthonormal chart already frozen in Iter044.
- Six held-out generic spatial directions, normalized exactly in code from the raw vectors:
  1. `(1,1,0)`
  2. `(1,2,2)`
  3. `(2,-1,2)`
  4. `(1,-2,2)`
  5. `(2,2,-1)`
  6. `(-1,2,2)`
- Three wave-number scales: `kappa = 0.7, 1.3, 2.1`.
- Five frozen shell ratios for each lane: `r = 0.75, 0.90, 1.00, 1.10, 1.25`, using orthonormal covector `p = kappa*(1,-r*n)`.
- Two TT basis tensors built deterministically from the same transverse-basis convention as G43/G44 (`plus`, `cross`).

Total production: 18 scientific lanes (6 directions × 3 scales) plus aggregate.

## Frozen observables per lane
For each shell sample form the 2×2 physical projected kernel `K_TT = P^T H_QGR-L1(k) P`, where the two columns of `P` are normalized incidence-frame representatives of plus/cross TT tensors.

Record:
1. on-shell projected-kernel norm;
2. full Hessian rank and gauge rank;
3. off-shell diagonal coefficients divided by the Minkowski shell scalar `s=p^T eta p`;
4. plus/cross coefficient ratio;
5. relative cross-polarization mixing;
6. sign product of the two diagonal coefficients;
7. variation of each shell-normalized coefficient across the four off-shell samples.

## Frozen lane PASS
A lane passes iff:
- chart controls are valid to `1e-12`;
- on shell (`r=1`): full Hessian rank = 4, gauge rank = 4, and projected TT kernel norm / max off-shell projected norm < `1e-10`;
- every off-shell sample: full Hessian rank = 6;
- both shell-normalized TT diagonal coefficients are finite and nonzero (`abs > 1e-8`);
- plus/cross shell-normalized coefficients agree within relative `1e-9`;
- their product is positive (same relative sign);
- cross-polarization mixing is < `1e-9` relative to the diagonal scale;
- variation of the shell-normalized coefficient across off-shell samples is < `1e-9` relative.

No threshold may be weakened after production.

## Aggregate classes
Full PASS only if all 18 lanes have valid controls and satisfy the frozen lane PASS:
`PASS_SCOPED_QGR_L1_TWO_POLARIZATION_RELATIVE_RESIDUE_DEGENERACY`

Otherwise, with valid controls:
`FAIL_SCOPED_QGR_L1_RELATIVE_RESIDUE_OR_POLARIZATION_SIGNATURE`

Invalid controls or infrastructure failure must be classified separately and are not scientific FAIL.

## Interpretation lock
A full PASS means only that, on the frozen held-out linearized panel, the two physical TT polarizations have the same nonzero relative pole/kinetic coefficient and no relative sign split or polarization mixing. It does not determine the absolute sign of the physical residue because the overall action normalization is outside this gate. It does not establish quantum unitarity, nonlinear stability, global uniqueness, or correctness of QGR.

## Claim locks retained
- theory established = 0%;
- beta remains a matching/calibration parameter; `beta=1` is not authorized as physics;
- c6 remains unfixed;
- no experimental confirmation;
- no KMQGB `NEW_REQUIRED` claim without independent benchmark authority;
- no physical branch weights from G35–G37.
