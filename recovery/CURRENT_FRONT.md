# QGR Current Research Front

Updated: 2026-09-14
Primary active front: `POST-ITER055I / MINIMAL NEW CANDIDATE-DEFINING QUANTUM DYNAMICS AXIOM CLASS + KILL TESTS`
Project phase: `MODEL_CONSTRUCTION / QUANTUM DYNAMICS CANDIDATE DEFINITION`

## Canonical claim locks

- Repository infrastructure readiness: **100%**.
- Candidate-program roadmap readiness: **99% internal bookkeeping only**, not probability of correctness.
- Theory established: **0%**.
- `beta=1`: not authorized.
- `c6`: symbolic/unfixed.
- Full covariant Weyl3 metric EOM as a global theorem: **not established**.
- Strong hyperbolicity / Weyl3 well-posedness: **not established**.
- Physical exact-vs-order-reduced Weyl3 treatment selector: **absent**.
- Global interacting measure/regulator removal: **not established**.
- No full quantum unitarity, UV completion, full GR recovery, experimental confirmation or new-physics claim.

## New terminal result — Iter055I

Preregistration: `23aedd66bae29963f0017bf1e60c6468247775d9`.
Durable result: `a448e501883fe30fd89680bd69274ad3d6fa812f`.

Classification:

`PASS_SCOPED_NONUNIQUENESS_ITER055I_EXISTING_QGR_AUTHORITY_LEAVES_NONTRIVIAL_BOUNDARY_QUANTUM_LIFT_FREEDOM__NEW_CANDIDATE_DYNAMICS_RULE_REQUIRED`.

The uniqueness question is well posed because Iter055G already supplies regular boundary-relative/direct-integral Hilbert kinematics, positive measure disintegration and positive two-mode quotient fibers. Iter055H shows that no source-defined measurable branch operator/channel family is presently supplied.

Iter054Z's exact independent branch rephasing is only Kraus-representation gauge for the coarse channel, so it is not sufficient by itself. The stronger nonuniqueness witness is at the CPTP level: on the same positive two-mode fiber, identity and the unitary-covariant depolarizing family

`D_lambda(rho)=lambda rho+(1-lambda)Tr(rho)I/2`, `0<=lambda<=1`,

are operationally distinct for `lambda<1`, preserve the same positivity/support, are CPTP, are covariant under unitary basis changes, and obey `D_lambda o D_mu = D_(lambda mu)`. Current QGR authority contains no dynamics selector fixing `lambda` or choosing another family. This family is only a uniqueness negative control and is **not** proposed as QGR dynamics.

Existing geometric/refinement transport does not remove this freedom because the bridge from geometric transport plus boundary kinematics to a source-defined boundary quantum channel is exactly what Iter055H found missing. Adding that bridge now would itself be a new candidate-defining dynamics rule.

Therefore current QGR symmetry/composition/positivity data do not uniquely imply boundary-fiber quantum dynamics. A new dynamics principle is required as explicit new input.

## Next gate lock

Do **not** choose identity, depolarizing, Hamiltonian, Koopman, geometric-transport or any other channel post hoc.

The next gate must first define a **minimal independently motivated axiom class** and freeze kill tests before evaluating any member. At minimum a viable new rule must:

1. respect the established boundary-relative/direct-integral support and positive pairing;
2. obey measurable composition/refinement compatibility;
3. reduce to the already-established scoped Iter009-G6 one-particle channel on an overlapping domain rather than merely resemble it;
4. preserve the distinction between geometric transport, one-particle unitary transport and full interacting boundary dynamics;
5. not assume `beta=1`, fixed `c6`, a physical Weyl3 treatment selector or an undefined full-configuration `F_alpha`;
6. face prospective falsification tests for positivity/CP-TP or isometry, locality, refinement/continuum stability, measure compatibility and nontrivial predictive restriction.

A new candidate version is allowed only if the dynamics axiom is explicitly labeled new input and survives those prospective tests. It must not be described as derived from the present QGR candidate.

## GitHub workload policy

No new Actions run was launched for Iter055I because the terminal result is a source-level uniqueness theorem: once two operationally distinct admissible CPTP controls survive all currently source-defined kinematic/positivity/composition constraints and no source selector exists, more numerical load cannot restore uniqueness. Running CI would be fake load.

The latest genuine production computation therefore remains Iter054S until a successor gate defines a genuinely new computable discriminator.

## Operational note

Scheduled-task UI/finalization failures remain operational incidents only and are not scientific classifications. Continue short-orchestrator mode: read recovery/front/commits/live Actions first, take one bounded prospective action, and delegate heavy computation to GitHub Actions only when a real computable object exists.
