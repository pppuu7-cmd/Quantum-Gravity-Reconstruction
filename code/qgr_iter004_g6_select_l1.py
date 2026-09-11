#!/usr/bin/env python3
from fractions import Fraction
import collections
import itertools

# QGR Iter004-G6 exact, dependency-free selection of the linearized L1 Hessian.
# Selection inputs are internal QGR results only:
#   (a) derivative Noether identity on Sym^2(W4),
#   (b) previously derived incidence cone C=J-I,
#   (c) previously derived two-dimensional physical quotient.

V = range(4)
PERMS = list(itertools.permutations(V))


def rref(rows, ncols):
    a = [[Fraction(x) for x in row] for row in rows if any(row)]
    pivots = []
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
                a[i] = [a[i][j] - f*a[r][j] for j in range(ncols)]
        pivots.append(c)
        r += 1
    return a, pivots


def rank_q(rows, ncols):
    return len(rref(rows, ncols)[1])


def nullspace_q(rows, ncols):
    a, pivots = rref(rows, ncols)
    free = [c for c in range(ncols) if c not in pivots]
    basis = []
    for f in free:
        v = [Fraction(0) for _ in range(ncols)]
        v[f] = 1
        for ri, p in enumerate(pivots):
            v[p] = -a[ri][f]
        basis.append(v)
    return basis


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
        t = min(unseen)
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


def H_at_k(fields, orbits, coeff, kvals):
    n = len(fields)
    H = [[Fraction(0) for _ in range(n)] for _ in range(n)]
    for oi, orb in enumerate(orbits):
        c = coeff[oi]
        if not c:
            continue
        for a, b, i, j in orb:
            val = c * Fraction(kvals[i]) * Fraction(kvals[j])
            H[a][b] += val
            if a != b:
                H[b][a] += val
    return H


def poly_add(a, b):
    n = max(len(a), len(b))
    out = [Fraction(0)] * n
    for i, x in enumerate(a): out[i] += x
    for i, x in enumerate(b): out[i] += x
    while len(out) > 1 and out[-1] == 0: out.pop()
    return out


def poly_mul(a, b):
    out = [Fraction(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] += x*y
    while len(out) > 1 and out[-1] == 0: out.pop()
    return out


def sign(p):
    inv = sum(1 for i in range(len(p)) for j in range(i+1, len(p)) if p[i] > p[j])
    return -1 if inv % 2 else 1


def det_linear_family(A0, A1, idx):
    # det(A0 + t A1) exactly as a polynomial in t.
    total = [Fraction(0)]
    n = len(idx)
    for p in itertools.permutations(range(n)):
        term = [Fraction(1)]
        for r in range(n):
            i, j = idx[r], idx[p[r]]
            term = poly_mul(term, [A0[i][j], A1[i][j]])
        if sign(p) < 0:
            term = [-x for x in term]
        total = poly_add(total, term)
    return total


fields = [(i, j) for i in V for j in range(i, 4)]
orbits = build_orbits(fields)
assert len(orbits) == 38
rows = rows_HR(fields, orbits, derivative_R(fields))
basis = nullspace_q(rows, len(orbits))
assert len(basis) == 2

# At cover covector e0, gauge acts on (00,01,02,03); the complementary
# 6x6 block is indices 4..9 in this deterministic field ordering.
H0 = H_at_k(fields, orbits, basis[0], [1, 0, 0, 0])
H1 = H_at_k(fields, orbits, basis[1], [1, 0, 0, 0])
poly = det_linear_family(H0, H1, list(range(4, 10)))
# Exact polynomial: -(t+1)^4 (2t-1)^2 / 4.
expected = [Fraction(-1,4), 0, Fraction(3,2), 1, Fraction(-9,4), -3, -1]
assert poly == expected

branches = {
    Fraction(-1): 'overdegenerate',
    Fraction(1,2): 'two_mode',
}
branch_ranks = {}
for t, label in branches.items():
    coeff = [basis[0][i] + t*basis[1][i] for i in range(len(orbits))]
    rank = rank_q(H_at_k(fields, orbits, coeff, [1,0,0,0]), len(fields))
    branch_ranks[str(t)] = rank
assert branch_ranks['-1'] == 3
assert branch_ranks['1/2'] == 4

# Selected branch: four gauge null directions + exactly two physical null modes
# on the incidence cone. Test nontrivial rational points on K_C=0.
selected = [basis[0][i] + Fraction(1,2)*basis[1][i] for i in range(len(orbits))]
null_samples = [
    [1,0,0,0],
    [1,1,1,-1],
    [1,2,3,Fraction(-11,6)],
    [2,-1,3,Fraction(-1,4)],
]
for kvals in null_samples:
    Kc = 2*sum(Fraction(kvals[i])*Fraction(kvals[j]) for i in V for j in range(i+1,4))
    assert Kc == 0
    assert rank_q(H_at_k(fields, orbits, selected, kvals), len(fields)) == 4

nonnull_samples = [[1,1,1,1], [1,2,3,4], [1,-1,2,5]]
for kvals in nonnull_samples:
    Kc = 2*sum(Fraction(kvals[i])*Fraction(kvals[j]) for i in V for j in range(i+1,4))
    assert Kc != 0
    assert rank_q(H_at_k(fields, orbits, selected, kvals), len(fields)) == 6

# Exhaustive onsite mass audit: all S4-invariant symmetric degree-zero Hessians.
field_pairs = [(a,b) for a in range(len(fields)) for b in range(a,len(fields))]
findex = {f:i for i,f in enumerate(fields)}
def pfield(f,p): return tuple(sorted((p[f[0]],p[f[1]])))
def pfp(t,p):
    a,b=t
    na=findex[pfield(fields[a],p)]
    nb=findex[pfield(fields[b],p)]
    return (na,nb) if na<=nb else (nb,na)
unseen=set(field_pairs); mass_orbits=[]
while unseen:
    x=min(unseen)
    orb={pfp(x,p) for p in PERMS}
    mass_orbits.append(orb); unseen-=orb
assert len(mass_orbits)==7
mass_rows=collections.defaultdict(lambda:[0]*len(mass_orbits))
R=derivative_R(fields)
for oi,orb in enumerate(mass_orbits):
    for a,b in orb:
        for g,v,c in R[b]: mass_rows[(a,g,v)][oi]+=c
        if a!=b:
            for g,v,c in R[a]: mass_rows[(b,g,v)][oi]+=c
mass_rank=rank_q(list(mass_rows.values()),len(mass_orbits))
assert mass_rank==7
assert len(mass_orbits)-mass_rank==0

print({
    'gauge_compatible_degree2_family_dimension': 2,
    'cover_characteristic_factorization': '-(t+1)^4(2t-1)^2/4',
    'cover_null_branches': {'t=-1': {'rank': 3, 'extra_null_modes_beyond_gauge': 3},
                            't=1/2': {'rank': 4, 'extra_null_modes_beyond_gauge': 2}},
    'selected_branch': 't=1/2',
    'selection_reason': 'matches independently derived two-mode quotient while preserving incidence null cone',
    'nontrivial_incidence_null_samples_checked': len(null_samples),
    'nonnull_samples_checked': len(nonnull_samples),
    'S4_invariant_onsite_mass_orbits': len(mass_orbits),
    'mass_noether_constraint_rank': mass_rank,
    'allowed_nonzero_onsite_mass_dimension': 0,
    'classification': 'PASS_SCOPED_UNIQUE_CAUSAL_TWO_MODE_DERIVATIVE_GAUGE_CLOSED_LINEARIZED_BRANCH_QGR_L1',
    'claim_guard': 'linearized closure only; no nonlinear constraint algebra, Einstein interaction, continuum theorem, or experimental claim',
})
