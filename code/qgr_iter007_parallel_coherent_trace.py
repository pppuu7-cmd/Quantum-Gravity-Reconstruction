#!/usr/bin/env python3
import argparse, json, itertools, math
import numpy as np

P=argparse.ArgumentParser(); P.add_argument('--output',required=True); args=P.parse_args()

sx=np.array([[0,1],[1,0]],complex)
sy=np.array([[0,-1j],[1j,0]],complex)
sz=np.array([[1,0],[0,-1]],complex)
I=np.eye(2,dtype=complex)
Xs=[0.2*sx,0.2*sy,0.2*sz,0.2*(sx+sy+sz)/math.sqrt(3)]
perms=list(itertools.permutations(range(4)))
h=0.2

def exp_herm(X):
    w,v=np.linalg.eigh(X)
    return (v*np.exp(-1j*h*w))@v.conj().T
Es=[exp_herm(X) for X in Xs]
Us=[]
for p in perms:
    U=I.copy()
    for i in p: U=Es[i]@U
    Us.append(U)
Ks=[U/math.sqrt(24) for U in Us]

rho=np.array([[0.7,0.2+0.1j],[0.2-0.1j,0.3]],complex)
# Local trace after each cell.
def E(r): return sum((K@r@K.conj().T for K in Ks),np.zeros_like(r))
local=E(E(rho))

# Keep both orthogonal history registers coherently, then trace H1 x H2 only at the end.
# The reduced state is the explicit double Kraus sum over 24^2 branches.
delayed=np.zeros_like(rho)
for K2 in Ks:
    for K1 in Ks:
        K=K2@K1
        delayed += K@rho@K.conj().T

diff=float(np.linalg.norm(local-delayed))
assert diff<1e-12,diff
# Completeness of the two-cell product instrument.
comp=sum(( (K2@K1).conj().T@(K2@K1) for K2 in Ks for K1 in Ks),np.zeros((2,2),complex))
comp_err=float(np.linalg.norm(comp-I))
assert comp_err<1e-12,comp_err

out={
 'lane':'COHERENT_BEFORE_TRACE',
 'histories_per_cell':24,
 'two_cell_product_histories':576,
 'delayed_trace_vs_local_channel_difference_norm':diff,
 'two_cell_product_instrument_completeness_error':comp_err,
 'classification':'PASS_SCOPED_DELAYING_TRACE_OVER_INDEPENDENT_PRODUCT_HISTORY_REGISTERS_DOES_NOT_CANCEL_LOCAL_CHANNEL',
 'scientific_interpretation':'With the current fresh orthogonal history-register architecture, tracing all history registers only at the end gives exactly the same reduced dynamics as composing the locally traced channels. Therefore global coherence by itself does not remove the 4D marginal bulk effect.',
 'guard':'Cancellation would require a new derived cross-cell identification/recombination of history labels, not merely postponing the partial trace.'
}
open(args.output,'w').write(json.dumps(out,indent=2,sort_keys=True)+'\n')
print(json.dumps(out,sort_keys=True))
