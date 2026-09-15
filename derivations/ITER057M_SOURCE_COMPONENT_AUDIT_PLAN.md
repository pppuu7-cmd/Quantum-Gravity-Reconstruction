# Iter057M source-component audit plan

Date: 2026-09-15
Gate: `ITER057M-GENERAL-QAB-SECOND-EVEN-JET-QUARTIC-EXTENSION`
Parent preregistration: `9760ca0324dce13cf141a9f93b6ff69ea4c75605`
Universal matrix checkpoint: `5a00b06241c3bc034c02bb8d8abe9a1bd63c599a`

## Purpose

Resolve one narrow source-lineage discrepancy before consuming any accelerated Taylor-jet right-hand side in Iter057M.

The accelerated finite-jet implementation reproduces exact scalar controls (`P.R=3 I3`, Weyl-cubic trace Ward, source parity and low-order Noether coefficients), but its component double-divergence values at the G3/H0 origin have the opposite sign from the component table recorded in the later Iter057J derivation. Scalar controls do not decide that component sign.

This audit therefore replays only the four diagonal origin components using the already-authorized exact Iter057K lineage itself. It introduces no new Weyl3 formula and changes no Iter057M or Iter057J decision rule.

## Frozen evaluator

For each `i=0,1,2,3`, evaluate exactly at the G3/H0 origin using:

- `qgr_iter057k_exact_g3_geometry.py` from `bf01d61939371053af120567408172084d4ee4f8`;
- `qgr_iter057k_exact_weyl3_lineage.py` with normalization authority `90bde0d5c89e92f6b3436c2ba3e22f5af55ab1f0`;
- the authoritative identity `H5^{ab}=sqrt(-g) E_W3^{ab}` from Iter056X.

Record exact rational values of

`I3(0)`, `D^{ii}(0)`, `A^{ii}(0)`, `I^{ii}(0)`, `E_W3^{ii}(0)`, and `E_W3_ii(0)`.

No tolerance, finite difference, fitted factor, or downstream target is allowed.

## Parallel boundary

The four diagonal components are independent lanes and may run with `fail-fast:false`. Each lane reports only exact values and structural identity

`E_W3^{ii} = [A^{ii}+I^{ii}-2 sqrt(-g) D^{ii}]/sqrt(-g)`.

An aggregate may compare lanes only after all four artifacts exist. Green CI is not by itself a scientific classification.

## Decision use

- If the authorized lineage agrees with the accelerated finite-jet component signs, the accelerated jet may be repaired/frozen and used for the Iter057M source second-jet RHS after additional exact Noether controls.
- If it agrees with the existing Iter057J component table, the accelerated implementation is rejected and must not feed Iter057M.
- If neither agrees, Iter057M remains source-component BLOCKED until the convention mismatch is isolated.

Any correction to the numerical coefficient recorded for Iter057J must be made as a separate audit/correction record. Its scoped conformal scientific FAIL is not reconsidered unless the audited component becomes exactly zero.

Claim locks remain unchanged; `c6` is symbolic/unfixed and theory established remains `0%`.