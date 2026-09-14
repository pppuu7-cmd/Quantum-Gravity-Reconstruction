# QGR Current Research Front

Updated: 2026-09-14
Primary active front: `POST-ITER055Z / FORMAL-ANALYTIC PERTURBATIVE-SECTOR SELECTOR SUFFICIENCY`
Project phase: `MODEL_CONSTRUCTION / WEYL3 TREATMENT-PRINCIPLE FALSIFICATION AND CONSTRUCTION`

## Canonical claim locks

- Repository infrastructure readiness: **100%**.
- Candidate-program roadmap readiness: **99% internal bookkeeping only**, not probability of correctness.
- Theory established: **0%**.
- `beta=1`: not authorized.
- `c6`: symbolic/unfixed; regulator running is not authorized.
- Physical Weyl3 treatment selector: not source-defined (Iter054G-R).
- Mixed-order strong-hyperbolicity evolution object: not fixed (Iter054F).
- Micro-to-continuum reconstruction and global interacting measure/regulator removal: not established.

## Relevant terminal results

Iter055W: exact formal reciprocal identity `rho k_HD^2=k^2`; nonzero fixed-band survival and formal-root decoupling are incompatible independent of running ansatz.

Iter055Y: if fixed-band `rho -> rho_*>0`, then `q_HD=h k_HD ->0`; an exact-HD nonzero-survival version cannot hide the formal root above every fixed refinement-resolved q-band by coefficient scaling alone.

Iter055X was closed `INVALID_REDUNDANT_GATE_ITER055X_OBJECT_ALREADY_TERMINALIZED_BY_ITER054G_R`; Iter054G-R remains the treatment-authority decision.

Iter055Z prereg `0e88f1bcb6dd42fcc1149fd6475e1e2f7eb38757`; result `38e8746989ed8ef13cd0066af7eb592a15208330`:

`FAIL_SCOPED_ITER055Z_GR_LIMIT_CONTINUITY_ALONE_DOES_NOT_EXCLUDE_SINGULAR_BRANCH__STRONGER_ASYMPTOTIC_SELECTION_REQUIRED`.

For the exact control `u''+eps u''''=0`, families such as

`u_eps=u_GR+exp(-1/eps) sin(t/sqrt(eps))`

retain a nonzero fast branch for every `eps>0` while converging to `u_GR` in every finite `C^n` seminorm on compact intervals; hence even smooth compact GR-limit continuity does not select the regular sector.

## Current highest-information gate

Test the stronger **formal/analytic perturbative-sector principle** on the same exact control, without asserting QGR physical authority:

Assume a solution admits a regular formal power series

`u(eps,t)=sum_{n>=0} eps^n u_n(t)`

(or a convergent analytic version in an appropriate smooth topology) near `eps=0`. Substitute into `u''+eps u''''=0` and determine recursively whether any fast singular branch survives.

If every coefficient is forced to satisfy the lower-order equation, this principle is mathematically sufficient to exclude the fast sector in the control. That would identify a viable **candidate treatment principle**, not a source-derived QGR law. Source authority remains separately BLOCKED by Iter054G-R.

A later gate may then ask whether the same formal perturbative structure generically turns `E_GR[g]+lambda E_W3[g]=0` into a hierarchy where each new correction is solved with the linearized GR operator and higher-derivative terms appear only as sources built from lower orders.

## Operational note

Short-orchestrator mode remains active. Exact formal-series gates require no GitHub Actions workload.
