# Iter054C Preregistration

Gate: `ITER054C-WEYL3-LOCAL-METRIC-PRINCIPAL-SYMBOL-AND-GAUGE-DEGENERACY`

Status at freeze: **PREREGISTERED BEFORE OUTPUTS**

## Scientific question

Can the Weyl^3 correction be pushed one level beyond the finite algebraic Hessian of Iter054B to an explicit local high-frequency metric principal-symbol construction on frozen Weyl-active backgrounds, while correctly retaining diffeomorphism gauge degeneracy and refusing any hyperbolicity/well-posedness claim before a justified principal-order gauge fixing is supplied?

## Scope

This gate is a local Riemann-normal-coordinate/high-frequency principal-part certificate only. It is not a global covariant EOM theorem and not a hyperbolicity or spectrum theorem.

Freeze `c6` as symbolic/unfixed. No beta normalization is allowed. No physical root weights, ghost signs, unitarity, UV completion, experimental confirmation, or new-physics claim may be inferred.

## Frozen construction

At a point in Riemann normal coordinates, use a covector `k_mu` and a symmetric metric perturbation amplitude `h_{mu nu}`. Freeze the principal linearized Riemann map

`delta R_{mu nu rho sigma}[k,h] = 1/2 (k_rho k_nu h_{mu sigma} + k_sigma k_mu h_{nu rho} - k_sigma k_nu h_{mu rho} - k_rho k_mu h_{nu sigma})`

up to an overall Fourier-sign convention that cancels in the quadratic principal bilinear. Project to the linearized Weyl tensor using the exact four-dimensional trace subtraction with the frozen flat tangent metric.

For `F(W)=Tr(W^3)` use the exact second directional derivative/Hessian frozen by Iter054B. Compose that Hessian with the metric-to-Weyl principal map to obtain a 10x10 symmetric metric-amplitude bilinear matrix `Q_W3(k; Wbar)` on each frozen background.

No post-output change of witnesses, backgrounds, rank thresholds, null controls, or interpretation is allowed.

## Frozen streams

### A0 — metric-to-curvature / metric-to-Weyl principal map identity

Use exact rational covectors and exact rational symmetric perturbations. Require:

1. linearized Riemann antisymmetry/pair symmetry and first-Bianchi identities exactly;
2. projected linearized Weyl trace is exactly zero;
3. homogeneity `delta C(lambda k,h)=lambda^2 delta C(k,h)` exactly for frozen nonzero rational lambda;
4. at least one deliberately corrupted sign/permutation map violates an exact identity.

PASS iff all positive identities are exact and the negative control is nonzero.

### A1 — composed Weyl3 metric principal bilinear

On 12 preregistered exact-rational Weyl-active algebraic backgrounds and 4 preregistered non-null rational covectors, construct `Q_W3` exactly. Require:

1. matrix symmetry exactly;
2. `Q_W3(lambda k)=lambda^4 Q_W3(k)` exactly;
3. exact zero matrix on `Wbar=0`;
4. nonzero matrix on every frozen Weyl-active background/covector pair;
5. direct second-directional derivative through `F(Wbar + eps deltaC[k,h])` matches the composed Hessian bilinear exactly on frozen held-out amplitudes.

PASS iff all predicates hold for the full frozen panel.

### B0 — diffeomorphism principal-null audit

For each frozen non-null `k` and four independent exact-rational gauge vectors `xi`, set `h_{mu nu}=k_mu xi_nu + k_nu xi_mu`. Require the principal linearized Riemann/Weyl map to annihilate these pure-gauge amplitudes exactly, hence `Q_W3 h_gauge = 0` in the exact composed correction symbol. Include one non-gauge symmetric-amplitude control that is not annihilated on each Weyl-active background.

PASS iff all gauge nulls are exact and all frozen non-gauge controls are nontrivial.

### B1 — gauge-fixing / authority boundary

Fail closed unless a principal-order gauge-fixing construction is actually supplied and separately validated. Ordinary second-order de Donder gauge fixing is not allowed to be treated as proof that the fourth-order correction symbol is invertible or hyperbolic.

This stream PASS condition is the explicit classification

`LOCAL_METRIC_PRINCIPAL_SYMBOL_CONSTRUCTED_GAUGE_DEGENERACY_CONFIRMED_HYPERBOLICITY_NOT_AUTHORIZED`

provided A0/A1/B0 pass and the following obligations remain recorded as open:

- justified principal-order gauge fixing for the fourth-order system;
- characteristic polynomial / real-characteristic audit on frozen Weyl-active backgrounds;
- strong-hyperbolicity or equivalent well-posedness estimate;
- constraint/gauge propagation;
- energy estimate and physical mode/residue interpretation.

## Aggregate classification

Full scoped PASS string:

`PASS_SCOPED_ITER054C_WEYL3_LOCAL_METRIC_PRINCIPAL_SYMBOL_GAUGE_DEGENERACY_CONFIRMED_HYPERBOLICITY_NOT_AUTHORIZED`

Any missing stream, parse error, invalid control, identity failure, covariance-map failure, failed gauge null, or post-hoc witness modification is FAIL/INVALID under the frozen classifier.

## Interpretation lock

Even full PASS establishes only an explicit local metric high-frequency fourth-order correction symbol with expected diffeomorphism gauge degeneracy on a finite exact panel. It does not establish hyperbolicity, well-posedness, physical mode count, ghost sign, stability, quantum unitarity, UV completion, full GR recovery, experimental confirmation, or new physics.

Candidate-program percentage, if reported, is roadmap readiness only and never correctness probability.
