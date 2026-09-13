#!/usr/bin/env python3
import argparse, json, math
import numpy as np
import mpmath as mp

ETA_NP=np.diag([-1.,1.,1.,1.])


def make_q_np(seed, scale=0.18):
    rng=np.random.default_rng(seed)
    q=rng.normal(size=(4,4,4,4))*scale
    q=(q+q.swapaxes(0,1))/2
    q=(q+q.swapaxes(2,3))/2
    return q


def h_np(seed):
    rng=np.random.default_rng(seed)
    _=rng.normal(size=(4,4,4,4))  # preserve original RNG stream? no: original creates q with separate RNG in make_q
    # Original G51A creates a fresh RNG(seed) after make_q(seed), then draws X first.
    rng=np.random.default_rng(seed)
    X=rng.normal(size=(4,4))
    return (X+X.T)*0.025


def mpv(x):
    return mp.mpf(repr(float(x)))


def zeros4():
    return [[[[mp.mpf('0') for _ in range(4)] for _ in range(4)] for _ in range(4)] for _ in range(4)]


def riemann_from_q_mp(q_np):
    q=[[[[mpv(q_np[a,b,c,d]) for d in range(4)] for c in range(4)] for b in range(4)] for a in range(4)]
    R=zeros4()
    half=mp.mpf('0.5')
    for a in range(4):
      for b in range(4):
       for c in range(4):
        for d in range(4):
         R[a][b][c][d]=half*(q[a][d][b][c]+q[b][c][a][d]-q[a][c][b][d]-q[b][d][a][c])
    return R


def mat_from_np(x):
    return mp.matrix([[mpv(x[i,j]) for j in range(4)] for i in range(4)])


def ricci_scalar(R,g,gi):
    Ric=mp.matrix(4,4)
    for b in range(4):
      for d in range(4):
        Ric[b,d]=mp.fsum(gi[a,c]*R[a][b][c][d] for a in range(4) for c in range(4))
    scal=mp.fsum(gi[b,d]*Ric[b,d] for b in range(4) for d in range(4))
    return Ric,scal


def weyl(R,g,gi):
    Ric,scal=ricci_scalar(R,g,gi)
    C=zeros4()
    half=mp.mpf('0.5'); sixth=mp.mpf(1)/6
    for a in range(4):
      for b in range(4):
       for c in range(4):
        for d in range(4):
          C[a][b][c][d]=(R[a][b][c][d]
            -half*(g[a,c]*Ric[b,d]-g[a,d]*Ric[b,c]-g[b,c]*Ric[a,d]+g[b,d]*Ric[a,c])
            +sixth*scal*(g[a,c]*g[b,d]-g[a,d]*g[b,c]))
    return C


def i3_from_C(C,gi):
    M=mp.matrix(16,16)
    for a in range(4):
      for b in range(4):
       p=4*a+b
       for c in range(4):
        for d in range(4):
          q=4*c+d
          M[p,q]=mp.fsum(gi[c,e]*gi[d,f]*C[a][b][e][f] for e in range(4) for f in range(4))
    M3=M*M*M
    return mp.fsum(M3[i,i] for i in range(16))


def density(g,R):
    gi=g**-1
    C=weyl(R,g,gi)
    return mp.sqrt(-mp.det(g))*i3_from_C(C,gi)


def algebraic_controls(R,g):
    gi=g**-1
    vals=[]
    for a in range(4):
      for b in range(4):
       for c in range(4):
        for d in range(4):
          vals.extend([abs(R[a][b][c][d]+R[b][a][c][d]),
                       abs(R[a][b][c][d]+R[a][b][d][c]),
                       abs(R[a][b][c][d]-R[c][d][a][b]),
                       abs(R[a][b][c][d]+R[a][c][d][b]+R[a][d][b][c])])
    C=weyl(R,g,gi)
    tr=[]
    for b in range(4):
      for d in range(4):
        tr.append(abs(mp.fsum(gi[a,c]*C[a][b][c][d] for a in range(4) for c in range(4))))
    return max(vals),max(tr)


def transform2(T,A):
    return A.T*T*A


def transform4(T,A):
    out=zeros4()
    for a in range(4):
      for b in range(4):
       for c in range(4):
        for d in range(4):
          out[a][b][c][d]=mp.fsum(A[i,a]*A[j,b]*A[k,c]*A[l,d]*T[i][j][k][l]
                                      for i in range(4) for j in range(4) for k in range(4) for l in range(4))
    return out


def boost_x(vs='0.23'):
    v=mp.mpf(vs); ga=1/mp.sqrt(1-v*v)
    A=mp.eye(4); A[0,0]=ga; A[1,1]=ga; A[0,1]=-ga*v; A[1,0]=-ga*v
    return A


def generic_A():
    vals=[['1.08','0.06','0.00','0.02'],['0.03','0.94','0.05','0.00'],['0.00','0.04','1.11','0.03'],['0.01','0.00','0.02','0.91']]
    return mp.matrix([[mp.mpf(vals[i][j]) for j in range(4)] for i in range(4)])


def rel(a,b,floor=mp.mpf('1e-30')):
    return abs(a-b)/max(abs(a),abs(b),floor)


def signature_ok_np(g):
    ev=np.linalg.eigvalsh(g)
    return int(np.sum(ev<0))==1 and int(np.sum(ev>0))==3


def five_point(g,h,R,t):
    return (density(g-2*t*h,R)-8*density(g-t*h,R)+8*density(g+t*h,R)-density(g+2*t*h,R))/(12*t)


def eval_precision(lane,dps):
    mp.mp.dps=dps
    seed=4001+lane*131
    q=make_q_np(seed)
    R=riemann_from_q_mp(q)
    # Original G51A uses a fresh RNG(seed) for X after make_q(seed), so draw X directly from fresh RNG.
    rng=np.random.default_rng(seed); X=rng.normal(size=(4,4)); hnp=(X+X.T)*0.025
    h=mat_from_np(hnp); g=mp.diag([-1,1,1,1])
    alg,tr=algebraic_controls(R,g)
    L0=density(g,R)
    eps=mp.mpf('1e-40')
    cs=mp.im(density(g+mp.j*eps*h,R))/eps
    ts=[mp.mpf('1e-3'),mp.mpf('5e-4'),mp.mpf('2.5e-4')]
    d5=[five_point(g,h,R,t) for t in ts]
    rich=d5[-1]+(d5[-1]-d5[-2])/15
    sigs=[]
    for t in ts:
      for k in (-2,-1,1,2): sigs.append(signature_ok_np(ETA_NP+float(k*t)*hnp))
    cov=[]
    for A in (boost_x(),generic_A()):
      gt=transform2(g,A); ht=transform2(h,A); Rt=transform4(R,A); jac=abs(mp.det(A))
      Lt=density(gt,Rt); cst=mp.im(density(gt+mp.j*eps*ht,Rt))/eps
      cov.append((rel(Lt/jac,L0),rel(cst/jac,cs)))
    return {"dps":dps,"density":L0,"cs":cs,"d5":d5,"rich":rich,"alg":alg,"tr":tr,"sigs":sigs,"cov":cov}


def run(lane):
    e80=eval_precision(lane,80); e120=eval_precision(lane,120)
    cs_r80=rel(e80['cs'],e80['rich']); cs_r120=rel(e120['cs'],e120['rich'])
    cs_prec=rel(e80['cs'],e120['cs']); rich_prec=rel(e80['rich'],e120['rich'])
    max_dcov=max(x[0] for x in e120['cov']); max_vcov=max(x[1] for x in e120['cov'])
    valid=(all(e80['sigs']) and all(e120['sigs']) and e80['alg']<=mp.mpf('1e-30') and e120['alg']<=mp.mpf('1e-30')
           and e80['tr']<=mp.mpf('1e-28') and e120['tr']<=mp.mpf('1e-28'))
    nonzero=abs(e120['density'])>mp.mpf('1e-8') and abs(e120['cs'])>mp.mpf('1e-8')
    passed=(valid and nonzero and cs_r80<=mp.mpf('1e-12') and cs_r120<=mp.mpf('1e-12')
            and cs_prec<=mp.mpf('1e-24') and rich_prec<=mp.mpf('1e-18')
            and max_dcov<=mp.mpf('1e-20') and max_vcov<=mp.mpf('1e-18'))
    out={
      "lane":lane,"seed":4001+lane*131,"valid":bool(valid),"nonzero_calibration":bool(nonzero),"pass":bool(passed),
      "cs_vs_rich_80":float(cs_r80),"cs_vs_rich_120":float(cs_r120),"cs_precision_change":float(cs_prec),
      "rich_precision_change":float(rich_prec),"algebraic_residual_120":float(e120['alg']),"weyl_trace_residual_120":float(e120['tr']),
      "max_density_covariance_rel_120":float(max_dcov),"max_direction_covariance_rel_120":float(max_vcov),
      "density_120":float(mp.re(e120['density'])),"directional_120":float(mp.re(e120['cs']))
    }
    print(json.dumps(out,sort_keys=True))


if __name__=='__main__':
    ap=argparse.ArgumentParser(); ap.add_argument('--lane',type=int,required=True); args=ap.parse_args(); run(args.lane)
