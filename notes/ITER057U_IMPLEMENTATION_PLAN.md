# Iter057U implementation plan — exact corrected-seed Weyl3 fourth source jet

Date: 2026-09-15
Authority: prospective preregistration `72eb0c6ffdcff789d7929a766e8f237475f89aaf`.
Parent terminal authorities: Iter057T `e4d8b960b8694ee166d05aa3ff089999b843e32a`, Iter057R `e395d2fb4be3e6f556f893ce63ae68f3b4b51ea2`.

This note freezes no new scientific criterion. It records the implementation route for the already-frozen Iter057U gate before any production evidence is generated.

## 1. Canonical seed reconstruction

Reuse the exact Iter057T canonical pivot, not a newly solved homogeneous representative:

1. replay Iter057O quartic seed;
2. replay Iter057Q sextic seed;
3. replay Iter057T `compute()` and require `pass == True`;
4. reconstruct its exported `particular_R8_normalized` as the trace-reversed octic jet, convert to the metric octic jet exactly as Iter057T does, and append it to the lower seed.

No lower pivot may be changed. The reconstructed seed must replay Iter057T Einstein/Ricci/scalar zero through coordinate degree six and the inverse identity through degree six before source extraction is trusted.

## 2. Exact polynomial engine

Port the Iter057R Fraction-polynomial tensor evaluator from maximum degree four to maximum degree six for geometry/P, while retaining only degree four in the final Euler source. This is preferred over a generic unrestricted SymPy expansion because Iter057R already supplies an exact sparse representation and the authorized Weyl3 normalization.

Required degree bookkeeping:

- metric seed: through degree 8;
- inverse metric: through degree 6 (h-series through h^3 is sufficient because h starts at degree 2);
- connection: through degree 7;
- Riemann/Ricci/scalar/Weyl: through degree 6;
- quadratic Weyl object and projected P: through degree 6;
- first covariant divergence of P: through degree 5;
- second covariant divergence: through degree 4;
- algebraic P.R insertion and I3: through degree 4 for the final Euler tensor, while the P.R=3 I3 control is evaluated through the preregistered required order;
- final `E_W3,ab` / `Shat_ab`: through degree 4;
- Noether divergence: through degree 3.

All arithmetic remains `Fraction`; no floating point, tolerance or fitted normalization is introduced.

## 3. Mandatory frozen controls A-I

Implement the preregistered controls literally:

A. exact inverse identity on the Iter057T seed;
B. exact Ricci/scalar/Einstein replay through degree 6;
C. exact `P.R = 3 I3`;
D. exact Euler symmetry through degree 4;
E. exact trace Ward identity through degree 4 in the existing Iter057R convention;
F. exact covariant Noether divergence through degree 3;
G. direct parity test of all odd source coefficients through degree 3;
H. exact replay of every Iter057R degree-0 and degree-2 normalized source coefficient, including zeros in the deterministic basis and all time-containing/off-diagonal entries;
I. deterministic full source basis accounting through degree 4.

The symmetric-tensor monomial basis size through degree 4 is `10 * C(8,4) = 700`; the pure degree-4 slice is `10 * C(7,3) = 350`. These are bookkeeping counts only, not scientific ranks.

## 4. Output/provenance contract

The evaluator should export JSON containing:

- gate and preregistration SHA;
- exact parent authority SHAs;
- all controls A-I separately;
- source basis counts by degree;
- complete sparse normalized `Shat_ab` coefficients through degree 4 plus explicit total basis counts so omitted entries are deterministically zero;
- exact counts of nonzero degree-4 coefficients, time-containing coefficients and off-diagonal coefficients;
- explicit lower-order replay status against Iter057R;
- `exact_zero_uses_tolerance=false`;
- `c6_status=SYMBOLIC_UNFIXED_FACTORED_OUT`;
- classification exactly equal to the preregistered PASS/BLOCKED/INVALID labels.

A production workflow should be added only after the evaluator and all frozen controls exist. A green workflow is not itself a scientific PASS; terminal classification requires consuming the raw evaluator artifact/log against the frozen preregistration.

## 5. Performance strategy

The dominant cost is the four-index P construction and its two covariant divergences at degree six. Before CI, use the following control-only optimizations without changing the mathematical object:

- sparse polynomial dictionaries and truncation after every multiplication;
- cache inverse-metric products used for index raising;
- cache repeated `Gamma * P` contractions in the first divergence;
- compute only independent antisymmetric pair slots internally where possible, then deterministically expand to the full tensor before frozen controls;
- exploit the already-proven even seed only for scheduling/caching, never to skip the preregistered direct parity verification;
- keep the full ten-component source output and full deterministic monomial basis accounting.

If exact evaluation still exceeds practical CI limits, classify Iter057U BLOCKED rather than weaken exactness, restrict the ansatz, mutate the canonical seed, or replace the source gate with a fitted solve.
