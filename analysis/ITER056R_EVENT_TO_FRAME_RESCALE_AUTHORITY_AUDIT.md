# Iter056R analysis — microscopic event to generator-local frame-rescale authority

Date: 2026-09-14
Preregistration: `41724a341f9abadc9e6b21423af191da74f9be8c`
Frozen cutoff: `442f2a40efcf1ebd7b8b60448eeb740ccb6ab991`

## Frozen verdict

No pre-cutoff source-owned rule derives the identification of the microscopic event coordinates entering the G10/G13 cubic sector with the generator-local frame-rescale coordinates used by G15.

The relevant objects exist, but the identification remains conditional.

## Obligation table

| Obligation | Verdict | Reason |
|---|---|---|
| A microscopic variable identity | YES | G5/G9/G10/G13 define relational microscopic variables/differences and their quadratic/cubic local jets. |
| B frame object identity | YES | G2 defines the conditional Lorentzian generator-space bilinear form and pair-perturbation matrix arena; later frame congruence uses `G=F^T C F`. |
| C derived event→frame-rescale map | NO | G14 finds a four-dimensional equivariant map space. G15 selects a generator-local diagonal-rescale subbridge only after an extra event-coordinate interpretation. No earlier source derives that interpretation. |
| D physical semantics | NO | No pre-cutoff rule says one Boolean/event excitation physically multiplies a generator-local frame leg by the corresponding scale coordinate. |
| E same-realization provenance | PARTIAL | The B4 event and frame objects belong to the same broad seed, but the actual event coordinate is not identified with the G15 scale coordinate on a realized history/profile. |
| F no normalization rescue | NO for a full map | G20/G21 show that nontrivial event insertion strength is not derived; G21's count→physical response map retains one scalar `beta`, and `beta=1` is explicitly unauthorized. |

## Early B4 representation/frame authority

Iter003-G2 provides a real source-owned kinematic structure:

- four relational generators;
- six unordered pair perturbations `x_ij`;
- exact `6=1+3+2` S4 decomposition;
- a 2D balanced sector `sum_{j!=i} x_ij=0`;
- a conditional Lorentzian generator-space bilinear form `g0=I-J` from S4 plus the explicitly unproved null-link hypothesis;
- an embedding of **pair perturbations** `x_ij` as off-diagonal entries of a symmetric 4x4 matrix `H` with zero diagonal.

For the balanced 2D sector, `H(1,1,1,1)^T=0` and `Tr(g0^{-1}H)=0` exactly.

This is important but it is not the G15 map. G2 maps six pair perturbations `x_ij` into an off-diagonal tensor perturbation; it does not identify four event amplitudes `q_i` with four diagonal generator-frame scales.

G2 also explicitly guards its Lorentzian frame as conditional because the elementary-null-link interpretation is not derived from the earlier CCRC axioms.

## G5/G10 variable semantics

The G5 pair action uses repeated-cell relational differences `D_i q` and the pair-incidence form `J-I`. G9 explicitly states that its microscopic `q` is not identified with continuum Weyl curvature.

G10/G13 then build the local S4 cubic in four microscopic `q_i` coordinates. These are algebraic/event coordinates of the local jet. No G5/G10 definition says that `q_i` is the logarithm, infinitesimal scale, or multiplicative rescaling of generator-frame leg `i`.

## G14/G15 near-result

G14's exact equivariance audit shows

`dim Hom_{S4}(W4, Sym^2(W4)) = 4`

in the tested linear bridge class. Hence S4 covariance alone cannot identify one event→second-moment map.

G15 then chooses a particularly natural existing congruence submanifold:

`F=diag(1+eps q_i)`, `G=F^T C F`,

so at first order

`delta G_ij=q_i+q_j`, `delta G_ii=0`.

This map is injective and exactly S4 covariant, and finite diagonal rescalings compose exactly. However G15's own guard states that it is canonical only **after identifying the four event coordinates with generator-local frame rescalings**, and that QGR had not derived that G13 event interpretation.

No earlier B4 result found by this audit supplies the missing identification.

## G19–G21 later consistency checks

The later event-insertion program narrows but does not close the gap:

- G19 derives the common-conformal Dirichlet bulk functional from the QGR two-derivative action, but does not derive a nontrivial endpoint event.
- G20 proves that a free endpoint remains trivial; a nontrivial event requires a boundary/event insertion whose strength is not derived.
- G21 shows that strict distinct-pair support plus S4 selects a unique off-diagonal second-moment response **direction** `C=J-I`, but the combinatorial pair-count→physical response map is multiplication by a free scalar `beta`.
- G21 explicitly says setting `beta=1` because incidence entries are 0/1 would identify combinatorial counting units with physical response units by convention rather than derivation.

These results do not retroactively make the G15 event coordinate a physical frame scale.

## Direct-search check

A pre-cutoff commit search for an independent `frame rescale` rule returns only the G15 frame-rescale bridge itself. No distinct earlier source-owned event→frame-rescale derivation was found. The relevant later response-map authority is G21 and remains scale-ambiguous.

## Frozen terminal implication

The evidence satisfies the preregistered condition for

`BLOCKED_OBJECT_DEFINITION_ITER056R_EVENT_TO_FRAME_RESCALE_INTERPRETATION_REMAINS_CONDITIONAL`.

There is no positive contradiction with the G15 map, so `SCIENTIFIC_FAIL` is not authorized. The map is structurally viable but not physically derived.

## Newly exposed alternative route

The audit reveals a stronger source-owned object than the conditional four-coordinate rescale map:

**G2 already embeds the actual six pair perturbations `x_ij` directly as an off-diagonal symmetric tensor `H`, and its balanced 2D sector is exactly transverse and trace-free relative to the conditional B4 Lorentzian seed.**

Therefore the next highest-information route is not to force the G15 `q_i` map. It is to ask whether the source-owned G2 balanced pair sector has a canonical cubic invariant that maps, through the distinguished symmetric-time / sum-zero spatial decomposition, to the weak-tidal `tr(H^3)` / Weyl3 shape used by Iter040.

That question must be preregistered separately and must not assume the answer.