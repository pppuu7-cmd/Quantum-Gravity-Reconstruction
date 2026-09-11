#!/usr/bin/env python3
import argparse,json,itertools,math
import numpy as np
P=argparse.ArgumentParser();P.add_argument('--output',required=True);a=P.parse_args()
sx=np.array([[0,1],[1,0]],complex);sy=np.array([[0,-1j],[1j,0]],complex);sz=np.array([[1,0],[0,-1]],complex);I=np.eye(2,dtype=complex)
Xs=[0.25*sx,0.25*sy,0.25*sz,0.25*(sx+sy+sz)/math.sqrt(3)]
perms=list(itertools.permutations(range(4)))
def eH(X,h):
 w,v=np.linalg.eigh(X);return (v*np.exp(-1j*h*w))@v.conj().T
def Smap(h):
 Es=[eH(X,h) for X in Xs];S=np.zeros((4,4),complex)
 for x in range(2):
  for y in range(2):
   E=np.zeros((2,2),complex);E[x,y]=1;out=np.zeros((2,2),complex)
   for p in perms:
    U=I.copy()
    for i in p:U=Es[i]@U
    out+=(U@E@U.conj().T)/24
   S[:,x+2*y]=out.reshape(-1,order='F')
 return S
rho0=np.array([[1,0],[0,0]],complex).reshape(-1,order='F')
bs=[4,6,8,12,16,24]
rows=[]
for b in bs:
 h=1/b;S=Smap(h)
 # One local spatial site experiences b causal time cells across fixed duration.
 r=(np.linalg.matrix_power(S,b)@rho0).reshape((2,2),order='F')
 ploc=float(np.real(np.trace(r@r)))
 nspace=b**3
 # Independent spatial tensor factors: P_global=P_local^(b^3), use log to avoid underflow.
 minuslog_global=float(-nspace*math.log(ploc))
 per_site=float(-math.log(ploc))
 rows.append({'b':b,'h':h,'time_cells_per_site':b,'spatial_sites':nspace,'local_purity':ploc,'local_purity_loss':1-ploc,'minus_log_global_product_purity':minuslog_global,'minus_log_purity_per_site':per_site})
x=np.log(np.array(bs[-4:],float)); y=np.log(np.array([r['local_purity_loss'] for r in rows[-4:]]))
slope=float(np.polyfit(x,y,1)[0])
assert abs(slope+3)<0.08,slope
plateau=[r['minus_log_global_product_purity'] for r in rows[-3:]]
assert max(plateau)-min(plateau)<2e-4,plateau
out={
 'lane':'SPATIAL_FACTORIZATION',
 'rows':rows,
 'local_loss_log_b_slope':slope,
 'global_minus_log_purity_plateau_last':plateau[-1],
 'classification':'PASS_SCOPED_LOCAL_REDUCED_PURITY_RECOVERS_AS_H3_WHILE_EXTENSIVE_GLOBAL_LOG_PURITY_IS_MARGINAL',
 'scientific_interpretation':'If the four-dimensional network is a tensor product of b^3 spatial subsystems each undergoing b causal cell channels, a local subsystem sees only O(b) sequential channels and its purity loss vanishes as b^-3. The nonzero h^0 quantity is the extensive/global -log purity summed over O(b^3) spatial factors, not a surviving local two-mode decoherence probability.',
 'guard':'Real QGR field states need not factorize spatially. This lane proves that four-volume cell counting alone is insufficient to infer a local continuum Lorentz-violating observable.'
}
open(a.output,'w').write(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,sort_keys=True))
