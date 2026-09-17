# Iter057AP target-blind trace-Ward control defect

Date: 2026-09-17
Parent preregistration: `6de62a559381a7c86e01c58a62ea7d8c91606884`
Observed run: `35176400855` at head `c687197dc01c0739617961145d04ec222e39be66`

## Status

**IMPLEMENTATION / CONTROL DEFECT IDENTIFIED BEFORE ANY U/X TARGET COEFFICIENT LOADING. NOT A SCIENTIFIC FAIL.**

The exact constructor completed the independent Frechet reconstruction of `P=dI3/dR`, with all algebraic/Frechet controls true, exact source symmetry, exact Noether divergence through degree five, complete 2100-slot source payload, and source coefficients still target-blind. The only failed control was named `E_trace_Ward_trace_Shat_minus_I3_zero`.

Inspection of the frozen constructor convention shows that `Shat_ab` is formed by lowering the indices of `Eup^{ab}` directly:

`Shat_ab = g_ac g_bd Eup^{cd}`.

It is therefore not the negative of this constructor's Euler tensor.

For the four-dimensional cubic Weyl scalar `I3`, under constant covariant-metric scaling `delta g_ab = 2 sigma g_ab`, `sqrt(-g) I3` has scaling weight `-2`; hence

`g_ab Eup^{ab} = -I3`.

The same identity follows internally from the frozen AO algebraic Euler form: the homogeneous Frechet identity gives `P.R = 3 I3`; the traced algebraic curvature term contributes `-3 I3`, the `+(1/2) g^{ab} I3` density term contributes `+2 I3` in `d=4`, and the traced double-divergence term vanishes for the Weyl derivative tensor. Thus the exact constructor-side Ward identity is

`g^{ab} Shat_ab + I3 = 0`,

not `g^{ab} Shat_ab - I3 = 0`.

## Frozen repair scope

Execution/control-only repair: change only the trace-Ward predicate and its descriptive key from minus to plus. Do not alter the metric seed, AO Euler formula, Frechet `P`, source coefficients, basis, target comparator, sign/scale map, preregistered classifier, `c6`, or any U/X authority. U/X target coefficients remain unopened by the constructor.

After repair, rerun the same constructor. If all target-blind controls pass, freeze its 2100-slot payload/hash before running the separate U/X comparator, exactly as preregistered.
