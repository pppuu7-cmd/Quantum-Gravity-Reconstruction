# Iter057AU — Corrected degree-6 descendant dependency adjudication

Status: **PREREGISTERED_NOT_PRODUCED**
Date: 2026-09-17

## Purpose

After terminal Iter057AT independently reproduced the corrected homogeneous total-degree-six Weyl^3 source, determine exactly which historical post-Iter057X scientific results are load-bearing descendants of the legacy degree-six source and therefore require prospective replay, versus which results are independent and remain authoritative without replay.

This gate is an adjudication/dependency gate, not a physics PASS gate. It must run before any descendant is silently rewritten or reclassified.

## Frozen inputs

- Iter057AT preregistration: `6039cb2ed1380b549bced3d33634362ef57345d4`.
- Iter057AT corrected ordered 840-vector SHA256: `5d070732d90b864f6167e03da85b86ce531d127dc9442fdbb928fd1b6153ee6b`.
- Iter057AT terminal artifact: `10486973737`.
- Iter057AT terminal payload SHA256: `9359413858a8887b0442aba56fba14576d37be87ce51fec80659758cc7a1bd8a`.
- Historical Iter057X and every existing descendant result remain immutable historical records.
- `c6` remains symbolic/unfixed.

## Frozen method

1. Build a machine-readable dependency DAG from repository provenance only: imports, explicit input paths, recorded source hashes, workflow inputs, result manifests, and recovery lineage.
2. Do **not** inspect whether replaying a descendant would improve or worsen its scientific classification while deciding dependency status.
3. For every scientific result after Iter057X, assign exactly one class:
   - `DIRECT_LOAD_BEARING_DEPENDENT` — consumes legacy degree-six coefficients/source or a derived object whose value depends on them;
   - `TRANSITIVE_LOAD_BEARING_DEPENDENT` — consumes a direct dependent result/object;
   - `INDEPENDENT_OF_LEGACY_DEGREE6_SOURCE` — provenance establishes no load-bearing dependency;
   - `UNRESOLVED_PROVENANCE` — evidence is insufficient to decide.
4. Any `UNRESOLVED_PROVENANCE` fails closed for replay planning: it may not be silently preserved or silently superseded.
5. Produce a deterministic ordered replay queue containing only direct/transitive dependents, with the earliest scientifically load-bearing descendant first.
6. No descendant scientific outcome is recomputed in Iter057AU.

## Frozen acceptance criteria

Scoped PASS requires all of:

- complete census of post-Iter057X scientific result records present on the preregistration head;
- every censused record assigned exactly one dependency class;
- evidence path recorded for every assignment;
- deterministic DAG is acyclic;
- replay queue is deterministic and contains no independently classified result;
- a second implementation independently reconstructs the classification and replay queue without reading the primary classification payload;
- primary and independent ordered classifications agree bit-for-bit;
- no historical scientific result file is modified;
- no claim lock is promoted.

If provenance is insufficient, terminal classification is `BLOCKED_ITER057AU_UNRESOLVED_PROVENANCE`, not a weakened PASS.

## Forbidden post-hoc actions

- No changing dependency rules after seeing descendant outcomes.
- No normalization/sign/basis fitting.
- No replay inside this gate.
- No retroactive rewriting of Iter057X, Iter057AP, Iter057AR, or any other historical terminal record.
- No inference of global/all-orders/quantum closure.

## Claim locks

Theory established = 0%. No experimental confirmation. `beta=1` unauthorized. `c6` unfixed. Finite/local certificates are not global theorems. G45 does not establish absolute energy positivity or quantum unitarity. G35–G37 distant roots do not authorize physical weights. KMQGB `NEW_REQUIRED` remains unauthorized.
