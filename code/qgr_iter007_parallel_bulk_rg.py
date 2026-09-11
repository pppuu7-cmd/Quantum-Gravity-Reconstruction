#!/usr/bin/env python3
import argparse, json, itertools, math
import numpy as np

P=argparse.ArgumentParser(); P.add_argument('--output',required=True); args=P.parse_args()

# Exact power counting: one B4-cell history channel differs from identity by O(h^4).
# A support containing O(h^-d_eff) cells therefore scales as h^(4-d_eff).
scaling={str(d):{'h_exponent':4-d,'refinement_factor_exponent':-(4-d)} for d in range(1,5)}
assert scaling['1']['h_exponent']==3
assert scaling['4']['h_exponent']==0

# Numerical exact-24-history channel stress test on a two-level toy.
sx=np.array([[0,1],[1,0]],complex)
sy=np.array([[0,-1j],[1j,0]],complex)
sz=np.array([[1,0],[0,-1]],complex)
I=np.eye(2,dtype=complex)
eps=0.25
Xs=[eps*sx,eps*sy,eps*sz,eps*(sx+sy+sz)/math.sqrt(3)]
perms=list(itertools.permutations(range(4)))

def exp_herm(X,h):
    w,v=np.linalg.eigh(X)
    return (v*np.exp(-1j*h*w))@v.conj().T

def cell_channel_matrix(h):
    Es=[exp_herm(X,h) for X in Xs]
    S=np.zeros((4,4),complex)
    for a in range(2):
        for b in range(2):
            Eab=np.zeros((2,2),complex); Eab[a,b]=1
            out=np.zeros((2,2),complex)
            for p in perms:
                U=I.copy()
                for i in p: U=Es[i]@U
                out += (U@Eab@U.conj().T)/24
            S[:,a+2*b]=out.reshape(-1,order='F')
    return S

rho0=np.array([[1,0],[0,0]],complex).reshape(-1,order='F')
bs=[4,6,8,12,16]
losses={}
slopes={}
for d in range(1,5):
    rows=[]
    for b in bs:
        h=1.0/b; N=b**d
        S=cell_channel_matrix(h)
        rho=(np.linalg.matrix_power(S,N)@rho0).reshape((2,2),order='F')
        loss=float(1-np.real(np.trace(rho@rho)))
        rows.append({'b':b,'h':h,'cells':N,'purity_loss':loss})
    losses[str(d)]=rows
    x=np.log(np.array(bs[-4:],float)); y=np.log(np.array([r['purity_loss'] for r in rows[-4:]]))
    slopes[str(d)]=float(np.polyfit(x,y,1)[0])

# d=1,2,3 approach slopes -3,-2,-1; d=4 approaches a nonzero plateau.
assert abs(slopes['1']+3)<0.08, slopes
assert abs(slopes['2']+2)<0.08, slopes
assert abs(slopes['3']+1)<0.08, slopes
bulk4=[r['purity_loss'] for r in losses['4'][-3:]]
assert max(bulk4)-min(bulk4) < 1e-4
assert bulk4[-1] > 0.03

out={
 'lane':'FULL_NETWORK_RG',
 'cell_correction_order':'h^4',
 'power_counting_by_effective_support_dimension':scaling,
 'numeric_purity_loss':losses,
 'fitted_log_b_slopes':slopes,
 'd4_limit_last_value':bulk4[-1],
 'classification':'PASS_SCOPED_PATH_IRRELEVANT_BUT_LOCAL_TRACE_4D_BULK_MARGINAL',
 'scientific_interpretation':'The previous O(L h^3) path suppression is not a full-network theorem. If one traced history channel is assigned per four-cell, a fixed four-volume contains O(h^-4) cells and the O(h^4) correction is marginal rather than vanishing.',
 'guard':'The d=4 conclusion assumes local/fresh cell history registers and bounded local-overlap composition. A different globally correlated history identification would need an independently derived composition rule.'
}
open(args.output,'w').write(json.dumps(out,indent=2,sort_keys=True)+'\n')
print(json.dumps(out,sort_keys=True))
