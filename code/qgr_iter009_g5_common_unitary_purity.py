#!/usr/bin/env python3
import json, cmath

# A common unitary geometry correction V applied to every branch maps
# rho_out -> V rho_out V^dagger. Purity Tr(rho_out^2) is exactly unchanged.
def mm(A,B):
    n=len(A); m=len(B[0]); k=len(B)
    return [[sum(A[i][q]*B[q][j] for q in range(k)) for j in range(m)] for i in range(n)]
def dag(A):
    return [[A[j][i].conjugate() for j in range(len(A))] for i in range(len(A[0]))]
def tr(A): return sum(A[i][i] for i in range(len(A)))
def purity(A): return tr(mm(A,A)).real

rho=[[0.62+0j,0.13+0.07j],[0.13-0.07j,0.38+0j]]
theta=0.371
V=[[cmath.cos(theta)+0j,-cmath.sin(theta)+0j],[cmath.sin(theta)+0j,cmath.cos(theta)+0j]]
r2=mm(mm(V,rho),dag(V))
err=abs(purity(rho)-purity(r2))
assert err<1e-14

out={
  "gate":"ITER009-G5-COMMON-UNITARY-PURITY",
  "identity":"Tr[(V rho V^dagger)^2]=Tr[rho^2]",
  "numeric_witness_error":err,
  "classification":"PASS_SCOPED_ANY_COMMON_C6_INDUCED_UNITARY_GEOMETRY_SHIFT_CANCELS_EXACTLY_FROM_HISTORY_MIXTURE_PURITY",
  "guard":"Branch-dependent c6 corrections are not common-unitary gauge and require the separate order audit."
}
print(json.dumps(out,sort_keys=True))
