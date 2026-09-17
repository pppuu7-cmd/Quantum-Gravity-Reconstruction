# Prospective execution/control repair — degree-six discrepancy localization

Date: 2026-09-18
Parent gate: `CORRECTED_DEGREE8_DEGREE6_REDUCTION_DISCREPANCY_LOCALIZATION`
Parent preregistration: `ffc110bfd2067d13d135577141154b2aab8626be`

Before the first diagnostic production returned any scientific payload, inspection found one implementation-control defect: the `R10` comparison boundary was incorrectly required to be Ricci/scalar/Einstein-flat through coordinate degree 10. The canonical R10 seed is the mathematically sufficient seed boundary for a degree-six Euler source comparison, but its next degree-10 Einstein residual is precisely what the R12 correction is designed to cancel.

Frozen repair: only make the seed-vacuum control boundary-specific: require exact Ricci/scalar/Einstein zero through degree 8 for the R10 diagnostic and through degree 10 for the R12 diagnostic. Keep inverse/provenance checks, source objects, operators, decomposition, AT target, hashes, arithmetic, allowed localization outcomes, terminal classifier, c6 lock, and Q10 lock unchanged.

This repair does not select a localization outcome and does not authorize changing Iter057AT.
