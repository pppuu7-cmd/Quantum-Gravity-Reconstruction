#!/usr/bin/env python3
from fractions import Fraction
import collections
import itertools

# Exact, dependency-free orbit/rank audit for QGR Iter004-G4.
# We enumerate the COMPLETE space of S4-invariant, local quadratic Hessians
# homogeneous of degree two in four first-neighbour momenta.

V = range(4)
PERMS = list(itertools.permutations(V))


def rank_q(rows, ncols):
    a = [[Fraction(x) for x in row] for row in rows if any(row)]
    r = 0
    for c in range(ncols):
        pivot = next((i for i in range(r, len(a)) if a[i][c]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        p = a[r][c]
        a[r] = [x / p for x in a[r]]
        for i in range(len(a)):
            if i != r and a[i][c]:
                f = a[i][c]
                a[i] = [a[i][j] - f * a[r][j] for j in range(ncols)]
        r += 1
        if r == len(a):
            break
    return r


def exp2(i, j):
    e = [0, 0, 0, 0]
    e[i] += 1
    e[j] += 1
    return tuple(e)


def exp_plus(e, i):
    z = list(e)
    z[i] += 1
    return tuple(z)


def build_orbits(fields):
    findex = {f: i for i, f in enumerate(fields)}
    field_pairs = [(a, b) for a in range(len(fields)) for b in range(a, len(fields))]
    mom_pairs = [(i, j) for i in V for j in range(i, 4)]
    terms = [(a, b, i, j) for a, b in field_pairs for i, j in mom_pairs]

    def pfield(f, p):
        return tuple(sorted((p[f[0]], p[f[1]])))

    def pterm(t, p):
        a, b, i, j = t
        na = findex[pfield(fields[a], p)]
        nb = findex[pfield(fields[b], p)]
        if na > nb:
            na, nb = nb, na
        ni, nj = sorted((p[i], p[j]))
        return (na, nb, ni, nj)

    unseen = set(terms)
    orbits = []
    while unseen:
        t = next(iter(unseen))
        orb = {pterm(t, p) for p in PERMS}
        orbits.append(orb)
        unseen -= orb
    return orbits


def R_symmetric_coboundary(fields, allow_diagonal=False):
    # delta h_ij = k_i xi_j + k_j xi_i.
    R = {}
    for a, (i, j) in enumerate(fields):
        if i == j:
            assert allow_diagonal
            R[a] = [(i, i, 2)]
        else:
            R[a] = [(j, i, 1), (i, j, 1)]
    return R


def R_relative_pair(fields):
    # delta x_ij = (k_i-k_j)(u_j-u_i).
    R = {}
    for a, (i, j) in enumerate(fields):
        assert i < j
        R[a] = [(j, i, 1), (j, j, -1), (i, i, -1), (i, j, 1)]
    return R


def static_rank1_map(fields):
    # Existing exact cellwise redundancy x_ij -> x_ij + u_i + u_j.
    M = {}
    for a, (i, j) in enumerate(fields):
        assert i < j
        M[a] = [(i, 1), (j, 1)]
    return M


def rows_HR(fields, orbits, R):
    n = len(orbits)
    eq = collections.defaultdict(lambda: [0] * n)
    for oi, orb in enumerate(orbits):
        for a, b, i, j in orb:
            e = exp2(i, j)
            for g, v, c in R[b]:
                eq[(a, g, exp_plus(e, v))][oi] += c
            if a != b:
                for g, v, c in R[a]:
                    eq[(b, g, exp_plus(e, v))][oi] += c
    return list(eq.values())


def rows_HM(fields, orbits, M):
    n = len(orbits)
    eq = collections.defaultdict(lambda: [0] * n)
    for oi, orb in enumerate(orbits):
        for a, b, i, j in orb:
            e = exp2(i, j)
            for g, c in M[b]:
                eq[(a, g, e)][oi] += c
            if a != b:
                for g, c in M[a]:
                    eq[(b, g, e)][oi] += c
    return list(eq.values())


# 1) Original Boolean rank-2 arena: only i<j, six fields.
fields6 = [(i, j) for i in V for j in range(i + 1, 4)]
orbits6 = build_orbits(fields6)
assert len(orbits6) == 15

cross6 = rows_HR(fields6, orbits6, R_symmetric_coboundary(fields6))
rank_cross6 = rank_q(cross6, len(orbits6))
assert rank_cross6 == 15
assert len(orbits6) - rank_cross6 == 0

rel6 = rows_HR(fields6, orbits6, R_relative_pair(fields6))
rank_rel6 = rank_q(rel6, len(orbits6))
assert rank_rel6 == 14
assert len(orbits6) - rank_rel6 == 1

static6 = rows_HM(fields6, orbits6, static_rank1_map(fields6))
rank_rel_plus_static6 = rank_q(rel6 + static6, len(orbits6))
assert rank_rel_plus_static6 == 15
assert len(orbits6) - rank_rel_plus_static6 == 0

# 2) Diagnostic minimal enlarged tensor arena: i<=j, ten fields.
# This is NOT adopted as QGR ontology here. It is only a blocker-localization test.
fields10 = [(i, j) for i in V for j in range(i, 4)]
orbits10 = build_orbits(fields10)
assert len(orbits10) == 38
cross10 = rows_HR(fields10, orbits10, R_symmetric_coboundary(fields10, allow_diagonal=True))
rank_cross10 = rank_q(cross10, len(orbits10))
assert rank_cross10 == 36
assert len(orbits10) - rank_cross10 == 2

print({
    'boolean_pair6': {
        'fields': 6,
        'S4_invariant_degree2_hessian_coefficients': len(orbits6),
        'symmetric_coboundary_noether_rank': rank_cross6,
        'symmetric_coboundary_solution_dimension': 0,
        'relative_pair_gauge_solution_dimension_before_static_redundancy': 1,
        'relative_pair_plus_existing_static_redundancy_solution_dimension': 0,
    },
    'diagnostic_symtensor10': {
        'fields': 10,
        'S4_invariant_degree2_hessian_coefficients': len(orbits10),
        'symmetric_coboundary_noether_rank': rank_cross10,
        'symmetric_coboundary_solution_dimension': 2,
    },
    'classification': 'FAIL_SCOPED_DERIVATIVE_GAUGE_CLOSURE_FOR_CURRENT_BOOLEAN_PAIR6_TWO_DERIVATIVE_ARENA',
    'repair_hint_only': 'the obstruction disappears at the existence level when the rank-2 arena is enlarged from 6 off-diagonal pairs to 10 symmetric components, but that ontology change is not authorized by this audit',
    'claim_guard': 'no GR/Fierz-Pauli equivalence claim; no authorization to add diagonal fields post hoc',
})
