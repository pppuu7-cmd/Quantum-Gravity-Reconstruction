#!/usr/bin/env python3
import itertools,json,math
import numpy as np
from scipy.linalg import expm,expm_frechet
from scipy.optimize import least_squares
import qgr_iter010_g3_common as g3
FLAT_LOGDET=math.log(11664.0)

def tetrad_y(y,kappa):
    ph=float(g3.phi_minkowski(np.asarray(y,float),kappa))
    assert 1+2*ph>0 and 1-2*ph>0
    Fm=np.diag([math.sqrt(1+2*ph),math.sqrt(1-2*ph),math.sqrt(1-2*ph),math.sqrt(1-2*ph)])
    return g3.RM@Fm@g3.RMI

def anchor_logdet(a,kappa,y0):
    F=tetrad_y(y0,kappa)
    nbr=[tetrad_y(np.asarray(y0)+g3.RMI@(a*np.eye(4)[i]),kappa) for i in range(4)]
    def unpack(z):
        As=[np.tensordot(z[6*i:6*i+6],g3.BASIS,axes=(0,0)) for i in range(4)]
        return As,[expm(-A) for A in As]
    def res(z):
        _,Ei=unpack(z);out=[]
        for i in range(4):
            for j in range(i+1,4): out.extend(F[:,i]+Ei[i]@nbr[i][:,j]-F[:,j]-Ei[j]@nbr[j][:,i])
        return np.asarray(out,float)
    sol=least_squares(res,np.zeros(24),xtol=2e-12,ftol=2e-12,gtol=2e-12,max_nfev=900)
    rn=float(np.linalg.norm(sol.fun));assert rn<5e-9,(a,kappa,y0,rn)
    As,_=unpack(sol.x);J=np.zeros((24,24));row=0
    for i in range(4):
        for j in range(i+1,4):
            for b,B in enumerate(g3.BASIS):
                J[row:row+4,6*i+b]=expm_frechet(-As[i],-B,compute_expm=False)@nbr[i][:,j]
                J[row:row+4,6*j+b]-=expm_frechet(-As[j],-B,compute_expm=False)@nbr[j][:,i]
            row+=4
    sign,ld=np.linalg.slogdet(J);assert sign!=0
    return float(ld-FLAT_LOGDET),rn,float(np.linalg.svd(J,compute_uv=False)[-1])

def grid(n,H,k):
    a=H/n;vals_p=[];vals_m=[];maxr=0;mins=1e9
    for q in itertools.product(range(n),repeat=4):
        y0=g3.RMI@(a*np.asarray(q,float))
        vp,rp,sp=anchor_logdet(a,k,y0);vm,rm,sm=anchor_logdet(a,-k,y0)
        vals_p.append(vp);vals_m.append(vm);maxr=max(maxr,rp,rm);mins=min(mins,sp,sm)
    tp=sum(vals_p);tm=sum(vals_m)
    return {'n':n,'spacing':a,'anchors':n**4,'even_total':0.5*(tp+tm),'odd_total':0.5*(tp-tm),'plus_total':tp,'minus_total':tm,'max_residual':maxr,'min_sv':mins}

H=0.4;k=0.04
rows=[grid(n,H,k) for n in (1,2,3)]
# Correct unique-anchor counting should approach a finite even fixed-volume value.
rel23=abs(rows[2]['even_total']-rows[1]['even_total'])/(abs(rows[2]['even_total'])+1e-30)
assert rel23<0.30,(rel23,rows)
# Cubic/odd contribution should be increasingly suppressed under refinement.
assert abs(rows[2]['odd_total'])<abs(rows[0]['odd_total']),rows
out={
 'gate':'ITER011-G2-UNIQUE-ANCHOR-GLUED-REFINEMENT',
 'H':H,'kappa_abs':k,'rows':rows,'relative_even_change_n2_to_n3':rel23,
 'classification':'PASS_SCOPED_COUNTING_EACH_FINE_TORSION_ANCHOR_ONCE_REMOVES_THE_NAIVE_SHARED_VERTEX_OVERCOUNT_AND_THE_EVEN_FLAT_SUBTRACTED_COAREA_LOG_WEIGHT_APPROACHES_A_FINITE_FIXED_VOLUME_REFINEMENT_LIMIT',
 'interpretation':'The large G1 naive-composition defect was dominated by multiplying 16-vertex local-cell determinants for every subcell and thereby recounting shared anchors. Unique-anchor lattice counting gives the appropriate local-product baseline before true shared-variable/projective pushforward effects are studied.',
 'guard':'This is still a regular finite lattice with fixed background geometry; it is not yet the full projective pushforward measure on a fluctuating continuum configuration space.'
}
print(json.dumps(out,sort_keys=True))
