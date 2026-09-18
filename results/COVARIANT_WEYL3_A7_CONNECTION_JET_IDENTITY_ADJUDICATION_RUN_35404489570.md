# COVARIANT_WEYL3_A7_CONNECTION_JET_IDENTITY_ADJUDICATION — TERMINAL IDENTITY DISAGREEMENT

Date: 2026-09-19
Status: **TERMINAL / EXACT CONNECTION-IDENTITY DERIVATION DISAGREEMENT**

## Frozen authority

- Gate: `COVARIANT_WEYL3_A7_CONNECTION_JET_IDENTITY_ADJUDICATION`
- Scientific preregistration: `d76dea1d511d0f7fa99b057866ef44fd797a1fc6`
- Parent Fi-jet terminal result: `07ad77de0506a3de5e7db601e2cfc8b5edc37c5c`
- Execution binding: `fd89a9143570fc3345a9623d99bb653977cdb270`
- Frozen witness: `OFFSHELL_A / d=7 / (i,j)=(0,0)`
- Frozen point-P SHA256: `21095bed2a18f7a5fa2484961c75d4cd7589115d6a6f664f0b3eee8697cdd4fe`
- Execution-only PR: `#35`
- Production head: `45f4447ad20ef10d2e90a47e9079e39f328d6cbf`
- Authoritative Actions run: `35404489570`
- Workflow run number: `1`

## Jobs

- source lock: `105791292667` — completed / success
- Lane A tensor-Hessian identity: `105791325230` — completed / success
- Lane B direct GammaGamma identity: `105791325181` — completed / success
- terminal: `105791385847` — completed / success

## Immutable artifacts

Source lock:
- ID `10571836648`
- ZIP SHA256 `f56b445f9d5e387312ae15e8ca69146165508f7c2ea492a20fa6eb4acae5debc`
- canonical payload SHA256 `5724c6433a4b98dd5f01d9b49cbb45e0dde381b55710f6f8923e8545fe106a0b`
- raw JSON SHA256 `c2c8b08f1c23001d261bf3817478b774d7cdda9d2d634af0c6caece1b0d6cf59`

Lane A:
- ID `10571494230`
- ZIP SHA256 `efe4314d02c93b3ee5b14e4466cf50e7ae861b5ad27c5e56d4c17e5918b4cacd`
- canonical payload SHA256 `3ce606c75712edb6e4e93aca2384dad0cf7c7665a938d20c037689b36c85d500`
- raw JSON SHA256 `b013d046a6006b9f4129eda125831f652094cbec4c06a4429370ab2c2b52bf31`

Lane B:
- ID `10571821721`
- ZIP SHA256 `219f0d89bf08991a4713acbab39cb87c6734753eb1e8570788e98884cdae05bb`
- canonical payload SHA256 `e18126a20c4ec8832a8651f020790bbf62bf41bda124f3b7dab238837c6032d9`
- raw JSON SHA256 `7e4755e0f41864a42822ae96b0f6afac91240631c73e358ce922f9eb69e48350`

Terminal:
- ID `10571597004`
- ZIP SHA256 `9f4a284c1a0c4ca5c6a53cd3e6466f0840181dfce198a39209863e573ee5da92`
- canonical terminal payload SHA256 `7da01c792bc4d6f235f8274bee6f904bd540feca001c741e9b34a63a910bde48`
- raw terminal JSON SHA256 `8d41d078820c972eb0efbeed3f9513fde90ff3af6c2d3c3d746e9c67aa604472`

All ZIP digests and canonical payload hashes were independently recomputed from the immutable artifacts and match exactly.

## Source/target-blind lock

The source lock passed before both identity lanes executed.

In particular:
- exact frozen blobs and ancestry passed;
- both lanes use the same frozen P hash;
- both lanes use the neutral frozen panel;
- neither lane imports the other's identity helper;
- the frozen Researcher target numerator is absent from both identity lane source files and present only in the terminal comparator;
- exact Fraction arithmetic is used;
- no tolerance classifier is present;
- `c6=SYMBOLIC_UNFIXED`;
- corrected Q10 remains locked.

## Terminal classification

`CONNECTION_IDENTITY_DERIVATIONS_DISAGREE`

The disagreement is scientific/derivational, not an execution or provenance block.

## Common frozen inputs agree

Lane A and Lane B independently reconstruct exactly the same `dGamma` object.

Common `dGamma` SHA256:

`53949b649af4c4a03e51103d0fa411e476470eecc98d0548e214aefeb5f559ed`.

Both use the same validated point-P object.

Thus the disagreement is downstream of the common P and dGamma inputs.

## Exact Lane A result — tensor-Hessian derivation

Lane A connection identity value:

`-433508011369185071313333891829231313950116629/312885874482554842907489423863612273152000000`.

Connection tensor SHA256:

`6dce9ed04c9199cf36eb2a723095f7eeba3f002844c3cd9df7da33704cbdf673`.

## Exact Lane B result — direct GammaGamma derivation

Lane B connection identity value:

`433508011369185071313333891829231313950116629/312885874482554842907489423863612273152000000`.

Connection tensor SHA256:

`702b353ada68114482ede9a4fb3c8af6d3b7af708982256e44b7c2e7909848b4`.

## Exact discrepancy

Lane A - Lane B:

`-433508011369185071313333891829231313950116629/156442937241277421453744711931806136576000000`.

At scalar level the two independently derived connection identities are exact sign opposites.

The tensor hashes also differ, so the terminal comparator correctly does not treat scalar magnitude agreement as identity agreement.

## Relationship to frozen parent connection sources

Frozen Researcher connection source:

`433508011369185071313333891829231313950116629/312885874482554842907489423863612273152000000`.

Frozen Critic connection source:

`0`.

Lane B's scalar value equals the Researcher target, while Lane A equals its negative. However, because Lane A and Lane B do not agree with each other, the preregistered taxonomy requires the terminal classification `CONNECTION_IDENTITY_DERIVATIONS_DISAGREE`; no parent lane is adjudicated correct in this gate.

## Scientific frontier

The problem is now narrower than a generic connection omission:

- P object: common / exact;
- dGamma object: common / exact;
- connection magnitude at the frozen scalar contraction: common absolute value;
- **orientation/sign of the connection identity between the tensor-Hessian and direct GammaGamma derivations: unresolved exact disagreement**.

The next admissible causal task is therefore a prospective sign/orientation adjudication of the connection identity itself, using a third exact construction that does not reuse either hand-expanded sign convention.

## Locks

- Parent covariant FAIL remains immutable.
- Fi-jet terminal localization remains immutable.
- No connection-term repair is authorized.
- `c6=SYMBOLIC_UNFIXED`.
- corrected Q10 remains LOCKED.
- `theory_established=0%`.
- no global QGR/Weyl3, unitarity, UV-completion, physical-c6, experimental, or new-physics claim is authorized.
