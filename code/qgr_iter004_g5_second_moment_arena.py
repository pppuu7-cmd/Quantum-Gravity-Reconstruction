#!/usr/bin/env python3
from fractions import Fraction
import collections
import itertools

# QGR Iter004-G5 exact audit:
# 1) Sym^2 of the existing four rank-1 relational directions gives a natural
#    10-component second-moment arena without declaring repeated Boolean events.
# 2) Gauge-invariant degree-two Hessians exist there.
# 3) None embeds old QGR-L0 exactly on the old 2D quotient with the same cone.

V = range(4)
PERMS = list(itertools.permutations(V))
CLASS_SIZES = [1, 6, 3, 8, 6]


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
    return r


def inner(chi, psi):
    return Fraction(sum(n*a*b for n, a, b in zip(CLASS_SIZES, chi, psi)), 24)


# Four rank-1 directions form the permutation representation W4.
chi_W4 = [4, 2, 0, 1, 0]
# Character on squares of class representatives: e,e,e,3cycle,double-transposition.
chi_W4_g2 = [4, 4, 4, 1, 0]
chi_sym2_W4 = [(a*a+b)//2 for a, b in zip(chi_W4, chi_W4_g2)]
assert chi_sym2_W4 == [10, 4, 2, 1, 0]

irreps = {
    '1_trivial': [1, 1, 1, 1, 1],
    '3_standard': [3, 1, -1, 0, -1],
    '2_E': [2, 0, 2, -1, 0],
    '3_sign_twist': [3, -1, -1, 0, 1],
    '1_sign': [1, -1, 1, 1, -1],
}
mult = {name: inner(chi_sym2_W4, chi) for name, chi in irreps.items()}
assert mult == {
    '1_trivial': 2,
    '3_standard': 2,
    '2_E': 1,
    '3_sign_twist': 0,
    '1_sign': 0,
}


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


def derivative_R(fields):
    R = {}
    for a, (i, j) in enumerate(fields):
        if i == j:
            R[a] = [(i, i, 2)]
        else:
            R[a] = [(j, i, 1), (i, j, 1)]
    return R


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


fields10 = [(i, j) for i in V for j in range(i, 4)]
orbits10 = build_orbits(fields10)
assert len(orbits10) == 38
noether_rows = rows_HR(fields10, orbits10, derivative_R(fields10))
noether_rank = rank_q(noether_rows, len(orbits10))
assert noether_rank == 36
assert len(orbits10) - noether_rank == 2

# Old QGR-L0 2D quotient basis in off-diagonal order
# (01,02,03,12,13,23).
edges6 = [(i, j) for i in V for j in range(i+1, 4)]
findex10 = {f: i for i, f in enumerate(fields10)}
offidx = [findex10[e] for e in edges6]
B6 = [
    [0, 1],
    [1, 0],
    [-1, -1],
    [-1, -1],
    [1, 0],
    [0, 1],
]
Bfull = [[0, 0] for _ in fields10]
for local, idx in enumerate(offidx):
    Bfull[idx] = B6[local]
Gtt = [[4, 2], [2, 4]]  # B^T B, unique invariant metric up to scale on the 2D irrep.

# Add exact matching equations B^T H B = lambda * K_L0(k) * Gtt,
# K_L0 = k^T (J-I) k = 2 sum_{i<j} k_i k_j.
# Unknowns are 38 Hessian orbit coefficients plus lambda.
match = collections.defaultdict(lambda: [0] * (len(orbits10) + 1))
for oi, orb in enumerate(orbits10):
    for a, b, i, j in orb:
        e = exp2(i, j)
        for r in range(2):
            for s in range(2):
                coef = Bfull[a][r] * Bfull[b][s]
                if a != b:
                    coef += Bfull[b][r] * Bfull[a][s]
                if coef:
                    match[(r, s, e)][oi] += coef
for r in range(2):
    for s in range(2):
        for i in V:
            for j in range(i+1, 4):
                match[(r, s, exp2(i, j))][-1] += -2 * Gtt[r][s]

combined = [row + [0] for row in noether_rows] + list(match.values())
combined_rank = rank_q(combined, len(orbits10) + 1)
assert combined_rank == 39
assert (len(orbits10) + 1) - combined_rank == 0

print({
    'rank1_space': 'W4 = permutation representation on four relational directions',
    'second_moment_arena': 'Sym^2(W4)',
    'dimension': 10,
    'S4_character': chi_sym2_W4,
    'decomposition': '2*1 + 2*3 + 2',
    'canonical_split': 'diag4 (1+3) plus old offdiag6 (1+3+2)',
    'gauge_invariant_degree2_hessian_dimension': 2,
    'exact_old_QGR_L0_embedding_dimension': 0,
    'classification': 'PASS_SCOPED_NATURAL_10D_SECOND_MOMENT_ARENA__FAIL_SCOPED_EXACT_QGR_L0_KINETIC_EMBEDDING',
    'guard': 'the 10D arena is a candidate reconstruction object, not yet a promoted ontology or GR-equivalent tensor field',
})
