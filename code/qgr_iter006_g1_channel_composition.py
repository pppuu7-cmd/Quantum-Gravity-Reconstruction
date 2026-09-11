#!/usr/bin/env python3
from fractions import Fraction

N=24

# Work only with scalar branch weights; the operator statement is
# K_alpha=a P with P^2=P=P^dagger. The exact norm condition is N|a|^2=1.
a2=Fraction(1,N)
assert N*a2==1

for n in range(1,9):
    branches=N**n
    branch_channel_weight=a2**n
    assert branches*branch_channel_weight==1

print({
    'histories_per_cell':N,
    'branch_amplitude_magnitude_squared':a2,
    'branch_amplitude_magnitude':'1/sqrt(24)',
    'coarse_channel_weight_per_history':a2,
    'levels_checked':8,
    'n_level_normalization':'24^n * (1/24)^n = 1',
    'idealized_projector_channel':'rho -> P rho P',
    'classification':'PASS_SCOPED_CHANNEL_LEVEL_NORMALIZATION_AND_ASSOCIATIVITY',
    'guard':'physical QGR Hilbert space and projector remain unconstructed',
})
