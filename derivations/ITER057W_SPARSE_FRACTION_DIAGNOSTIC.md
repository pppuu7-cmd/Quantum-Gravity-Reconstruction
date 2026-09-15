# Iter057W sparse-Fraction diagnostic reproduction

Gate: `ITER057W-DECIC-EINSTEIN-SEED-COMPLETION`
Preregistration: `7e6336d195985b2059966eda64859da86c9e9d15`.
Sparse implementation: `ad14ccd72a1a3ca75ab95acb0e294c6707b14627`.
Frozen R6 data: `1c88517d3c0d63dab95fe7ba0bb8a2acc05df4dd`.
Frozen R8 authority: terminal Iter057T artifact digest `sha256:20134b10e4cf32ecd8b3e417921545714f12b29f4d72f812f6d5121e6b461dba`.

Status: **nonterminal diagnostic exact reproduction**. The active GitHub production run remains authoritative for terminalization.

A fresh exact sparse-`Fraction` execution of the frozen W problem gives the preregistered PASS candidate:

- actual pre-correction degree-eight Einstein residual is nonzero in all 10 independent tensor components;
- unrestricted principal matrix: `2530 x 2860`, `nnz=10120`;
- `rank(M)=2050` exactly;
- `rank([M|r])=2050` exactly;
- left-nullity `480`, nullity `810`;
- all 480 canonical Bianchi compatibility contractions are exactly zero;
- exact affine residual is zero;
- canonical free-columns-zero particular `Rbar10` has 283 nonzero normalized coefficients;
- the resulting metric correction is pure coordinate degree ten and preserves all lower seed coefficients through degree nine;
- full flat de Donder residual through degree nine has 0 nonzero components;
- independently recomputed nonlinear Ricci/scalar/Einstein tensors through coordinate degree eight vanish exactly; the 10 independent Einstein components have 0 nonzero residuals;
- every frozen control in the diagnostic evaluator is true;
- no numerical rank/zero tolerance is used.

Diagnostic classification produced by the evaluator:

`PASS_SCOPED_ITER057W_DECIC_EINSTEIN_SEED_COMPLETES_VACUUM_THROUGH_COORDINATE_DEGREE_EIGHT__HIGHER_SEED_ORDERS_REMAIN_OPEN`

This note is not the terminal Iter057W result. Terminal classification remains locked until production raw evidence is consumed. The finite-order scope ceiling and all physical/quantum claim locks remain unchanged.