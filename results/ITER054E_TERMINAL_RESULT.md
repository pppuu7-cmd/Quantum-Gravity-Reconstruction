# Iter054E terminal result

Date: 2026-09-14

Gate: `ITER054E-MIXED-ORDER-EINSTEIN-WEYL3-CHARACTERISTIC-REGIME-AUDIT`

## Provenance

- preregistration: `ed62acf961cae4a0d200364285d94a56e61a294d`
- implementation: `0366422137d4e8c665b3e10e6280acb6d338f3b1`
- initial production head: `59c5a09ac693c79bdc1827efa91e283cf30a36ab`
- initial run: `34815920355`
- initial run classification: `ITER054E_IMPLEMENTATION_OR_CONTROL_INVALID_A0_STRUCTURAL_EQUALITY`
- control-only repair: `f7d996b401e147d736b91b23b7e3ef97ff546b61`
- authoritative exact-retry run: `34817023061`
- aggregate job: `103889834227`
- summary artifact: `10336742062`
- summary digest: `sha256:b7e0dce1e44b44ac1b9425427db3d33bdf88271f8ab42762f006a4155eb36bc9`

The initial implementation-invalid run remains historical and is not rewritten.

## Frozen terminal classification

**`PASS_SCOPED_ITER054E_EINSTEIN_WEYL3_MIXED_ORDER_REGIME_SEPARATION_STRONG_HYPERBOLICITY_NOT_AUTHORIZED`**

All four frozen streams A0, A1, B0 and B1 passed on the exact retry.

A0 establishes only the exact frozen proxy identities for

`P(z;eps,lambda)=z+eps*lambda*z^2=z*(1+eps*lambda*z)`:

- exact GR limit `P|eps=0=z`;
- exact GR-connected root `z_GR=0`;
- exact singular branch `z_HD=-1/(eps*lambda)`;
- exact scaled singular identity `eps*z_HD=-1/lambda`;
- deliberate sign-flip control detected.

A1 establishes the frozen root substitution/scaling relations on the exact rational witness panel. B0 rejects the preregistered malformed missing-Einstein and wrong-order controls. B1 preserves the authority boundary.

## Scientific consequence

Within the prospectively frozen finite exact symbolic proxy family, the mixed second+fourth derivative structure has an exactly GR-connected branch and a distinct branch whose scale diverges as `eps -> 0`. This is a regime-separation certificate only.

The result does **not** establish the full tensorial gauge-fixed Einstein+Weyl3 characteristic determinant on an open region; real characteristics on an open region; uniform diagonalizability; a positive symmetrizer; strong hyperbolicity; constraint propagation; an energy estimate; physical mode multiplicities/residues/ghost signs; quantum unitarity; a quantum amplitude/measure; UV completion; full nonlinear GR recovery; experimental confirmation; or new physics.

## Authorized next dependency

The next admissible fatal-consistency gate is a separately prospectively frozen **open-region strong-hyperbolicity / uniform diagonalizability / symmetrizer audit** for an explicitly defined mixed-order reduction. It must include a negative control with real eigenvalues but collapsing/defective eigenvectors, so a root-only PASS cannot masquerade as strong hyperbolicity.

`c6` remains symbolic/unfixed. `beta=1` remains unauthorized. Theory established remains 0%.
