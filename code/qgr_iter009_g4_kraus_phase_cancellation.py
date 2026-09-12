#!/usr/bin/env python3
import json, cmath

# For K_a = N^{-1/2} z_a U_a, |z_a|=1,
# K_a rho K_a^dagger = N^{-1} U_a rho U_a^dagger exactly because z_a z_a*=1.
# Verify on explicit 2x2 matrices for several phases.
def mm(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
def dag(A):
    return [[A[j][i].conjugate() for j in range(2)] for i in range(2)]
def smul(z,A):
    return [[z*A[i][j] for j in range(2)] for i in range(2)]
def mdiff(A,B):
    return max(abs(A[i][j]-B[i][j]) for i in range(2) for j in range(2))

rho=[[0.7+0j,0.2+0.1j],[0.2-0.1j,0.3+0j]]
U=[[0+0j,1+0j],[1+0j,0+0j]]
N=24
errs=[]
for theta in [0.0,0.3,1.7,-2.2]:
    z=cmath.exp(1j*theta)
    K=smul(z/(N**0.5),U)
    lhs=mm(mm(K,rho),dag(K))
    rhs=smul(1/N,mm(mm(U,rho),dag(U)))
    errs.append(mdiff(lhs,rhs))
assert max(errs)<1e-15

out={
    "gate":"ITER009-G4-KRAUS-PHASE-CANCELLATION",
    "identity":"K_a rho K_a^dagger = N^-1 U_a rho U_a^dagger for K_a=N^-1/2 exp(iS_a/hbar) U_a",
    "max_numeric_witness_error":max(errs),
    "classification":"PASS_SCOPED_ARBITRARY_SCALAR_BRANCH_ACTION_PHASES_CANCEL_EXACTLY_FROM_THE_TRACED_HISTORY_MIXTURE_CHANNEL",
    "guard":"Relative phases remain observable if history branches are recombined coherently before tracing; c6 may also alter U_a indirectly through self-consistent corrected geometry."
}
print(json.dumps(out,sort_keys=True))
