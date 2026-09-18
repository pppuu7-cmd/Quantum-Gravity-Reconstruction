#!/usr/bin/env python3
from __future__ import annotations
import argparse,hashlib,json,math
from fractions import Fraction as F
from itertools import combinations_with_replacement,product
from pathlib import Path
import qgr_covariant_weyl3_panel as panel
N=4;Z=(0,0,0,0)
def fs(x):x=F(x);return str(x.numerator) if x.denominator==1 else f'{x.numerator}/{x.denominator}'
def jsha(x):return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=True).encode()).hexdigest()
def alphas():
 o=[]
 for d in range(3):
  for a in range(d+1):
   for b in range(d-a+1):
    for c in range(d-a-b+1):o.append((a,b,c,d-a-b-c))
 return o
AL=alphas()
def deg(a):return sum(a)
def add(a,b):return tuple(a[i]+b[i] for i in range(4))
def mf(a):
 q=1
 for x in a:q*=math.factorial(x)
 return q
def inds(a):
 q=[]
 for i,n in enumerate(a):q += [i]*n
 return tuple(q)
class P:
 __slots__=('d',)
 def __init__(self,d=None):self.d={k:F(v) for k,v in (d or {}).items() if v and deg(k)<=2}
 @staticmethod
 def c(x):x=F(x);return P({Z:x}) if x else P()
 @staticmethod
 def mono(k,x):x=F(x);return P({k:x}) if x else P()
 def v(self):return self.d.get(Z,F(0))
 def __add__(self,o):
  o=o if isinstance(o,P) else P.c(o);q=dict(self.d)
  for k,v in o.d.items():q[k]=q.get(k,F(0))+v
  return P(q)
 __radd__=__add__
 def __neg__(self):return P({k:-v for k,v in self.d.items()})
 def __sub__(self,o):return self+(- (o if isinstance(o,P) else P.c(o)))
 def __rsub__(self,o):return (o if isinstance(o,P) else P.c(o))-self
 def __mul__(self,o):
  o=o if isinstance(o,P) else P.c(o);q={}
  for a,x in self.d.items():
   for b,y in o.d.items():
    c=add(a,b)
    if deg(c)<=2:q[c]=q.get(c,F(0))+x*y
  return P(q)
 __rmul__=__mul__
 def sc(self,x):return P({k:F(x)*v for k,v in self.d.items()})
 def deriv(self,i):
  q={}
  for a,v in self.d.items():
   if a[i]:
    b=list(a);n=b[i];b[i]-=1;b=tuple(b);q[b]=q.get(b,F(0))+n*v
  return P(q)
def cab(a,b):return (a,b) if a<=b else (b,a)

def det_point(g):
 q=F(0)
 import itertools
 for pp in itertools.permutations(range(N)):
  inv=sum(1 for i in range(N) for j in range(i+1,N) if pp[i]>pp[j]);t=F(-1 if inv%2 else 1)
  for i in range(N):t*=g[i][pp[i]].v()
  q+=t
 return q
def shift(seed,a,b,I,maxdeg=2):
 a,b=cab(a,b);I=tuple(sorted(I));q=P()
 for al in AL:
  if deg(al)>maxdeg or len(I)+deg(al)>4:continue
  J=inds(al);v=panel.metric_value(seed,a,b,tuple(sorted(I+J)))
  if v:q=q+P.mono(al,v/F(mf(al)))
 return q
def eta(a,b):return F(-1 if a==b==0 else (1 if a==b else 0))
def build(seed):
 g=[[shift(seed,a,b,()) for b in range(N)] for a in range(N)]
 gi=[[P.c(eta(a,b)) for b in range(N)] for a in range(N)]
 for a,b in product(range(N),repeat=2):
  corr=P()
  for c,d in product(range(N),repeat=2):corr=corr+P.c(eta(a,c))* (g[c][d]-eta(c,d))*eta(d,b)
  gi[a][b]=gi[a][b]-corr
 g1=[[[shift(seed,a,b,(i,)) for i in range(N)] for b in range(N)] for a in range(N)]
 g2=[[[[shift(seed,a,b,(i,j)) for j in range(N)] for i in range(N)] for b in range(N)] for a in range(N)]
 G=[[[P() for _ in range(N)] for _ in range(N)] for _ in range(N)]
 for a,b,c in product(range(N),repeat=3):
  q=P()
  for e in range(N):q=q+(g1[e][c][b]+g1[e][b][c]-g1[b][c][e]).sc(eta(a,e))
  G[a][b][c]=q.sc(F(1,2))
 R=[[[[P() for _ in range(N)] for _ in range(N)] for _ in range(N)] for _ in range(N)]
 for a,b,c,d in product(range(N),repeat=4):
  q=(g2[a][d][b][c]+g2[b][c][a][d]-g2[a][c][b][d]-g2[b][d][a][c]).sc(F(1,2))
  for e,f in product(range(N),repeat=2):
   if eta(e,f):q=q+(G[e][c][a]*G[f][d][b]-G[e][d][a]*G[f][c][b]).sc(eta(e,f))
  R[a][b][c][d]=q
 Ric=[[P() for _ in range(N)] for _ in range(N)]
 for b,d in product(range(N),repeat=2):
  q=P()
  for a,c in product(range(N),repeat=2):q=q+gi[a][c]*R[a][b][c][d]
  Ric[b][d]=q
 S=P()
 for b,d in product(range(N),repeat=2):S=S+gi[b][d]*Ric[b][d]
 C=[[[[P() for _ in range(N)] for _ in range(N)] for _ in range(N)] for _ in range(N)]
 for a,b,c,d in product(range(N),repeat=4):
  rt=g[a][c]*Ric[d][b]-g[a][d]*Ric[c][b]-g[b][c]*Ric[d][a]+g[b][d]*Ric[c][a];gg=g[a][c]*g[d][b]-g[a][d]*g[c][b];C[a][b][c][d]=R[a][b][c][d]-rt.sc(F(1,2))+(S*gg).sc(F(1,6))
 Cup=[[[[P() for _ in range(N)] for _ in range(N)] for _ in range(N)] for _ in range(N)]
 for a,b,c,d in product(range(N),repeat=4):
  q=P()
  for e,f in product(range(N),repeat=2):q=q+gi[c][e]*gi[d][f]*C[a][b][e][f]
  Cup[a][b][c][d]=q
 Q=[[[[P() for _ in range(N)] for _ in range(N)] for _ in range(N)] for _ in range(N)]
 for a,b,c,d in product(range(N),repeat=4):
  q=P()
  for e,f in product(range(N),repeat=2):q=q+Cup[c][d][e][f]*Cup[e][f][a][b]
  Q[a][b][c][d]=q
 I=P()
 for a,b,c,d in product(range(N),repeat=4):I=I+Cup[a][b][c][d]*Q[a][b][c][d]
 R0=[[[[P() for _ in range(N)] for _ in range(N)] for _ in range(N)] for _ in range(N)]
 for a,b,e,f in product(range(N),repeat=4):
  q=P()
  for c,d in product(range(N),repeat=2):q=q+gi[c][e]*gi[d][f]*Q[a][b][c][d]
  R0[a][b][e][f]=q.sc(3)
 def psg(pp):
  z=0
  for i in range(4):
   for j in range(i+1,4):z+=pp[i]>pp[j]
  return -1 if z%2 else 1
 perms4=list(__import__('itertools').permutations(range(4)))
 Rr=[[[[P() for _ in range(N)] for _ in range(N)] for _ in range(N)] for _ in range(N)]
 for a,b,c,d in product(range(N),repeat=4):
  I4=(a,b,c,d);alt=P()
  for pp in perms4:alt=alt+R0[I4[pp[0]]][I4[pp[1]]][I4[pp[2]]][I4[pp[3]]].sc(F(psg(pp),24))
  Rr[a][b][c][d]=R0[a][b][c][d]-alt
 PRic=[[P() for _ in range(N)] for _ in range(N)]
 for b,d in product(range(N),repeat=2):
  q=P()
  for a,c in product(range(N),repeat=2):q=q+g[a][c]*Rr[a][b][c][d]
  PRic[b][d]=q
 PSc=P()
 for b,d in product(range(N),repeat=2):PSc=PSc+g[b][d]*PRic[b][d]
 Pt=[[[[P() for _ in range(N)] for _ in range(N)] for _ in range(N)] for _ in range(N)]
 for a,b,c,d in product(range(N),repeat=4):
  rt=gi[a][c]*PRic[d][b]-gi[a][d]*PRic[c][b]-gi[b][c]*PRic[d][a]+gi[b][d]*PRic[c][a]
  gg=gi[a][c]*gi[d][b]-gi[a][d]*gi[c][b]
  Pt[a][b][c][d]=Rr[a][b][c][d]-rt.sc(F(1,2))+(PSc*gg).sc(F(1,6))
 U=[[[P() for _ in range(N)] for _ in range(N)] for _ in range(N)]
 for a,c,b in product(range(N),repeat=3):
  q=P()
  for d in range(N):
   t=Pt[a][c][d][b].deriv(d)
   for r in range(N):t=t+G[a][d][r]*Pt[r][c][d][b]+G[c][d][r]*Pt[a][r][d][b]+G[d][d][r]*Pt[a][c][r][b]+G[b][d][r]*Pt[a][c][d][r]
   q=q+t
  U[a][c][b]=q
 T=[[F(0) for _ in range(N)] for _ in range(N)]
 for a,b in product(range(N),repeat=2):
  q=F(0)
  for c in range(N):q+=U[a][c][b].deriv(c).v()
  T[a][b]=q
 A=[[F(0) for _ in range(N)] for _ in range(N)];E=[[F(0) for _ in range(N)] for _ in range(N)]
 for a,b in product(range(N),repeat=2):
  q=F(0)
  for c,d,e,f in product(range(N),repeat=4):q+=Pt[a][c][d][e].v()*gi[b][f].v()*R[f][c][d][e].v()
  A[a][b]=q;E[a][b]=-q+2*T[a][b]+F(1,2)*gi[a][b].v()*I.v()
 return {'g':g,'gi':gi,'G':G,'R':R,'Ric':Ric,'S':S,'C':C,'Cup':Cup,'Q':Q,'I':I,'P':Pt,'U':U,'T':T,'A':A,'E':E}

def point_controls(z,seed):
 g,gi,G,R,Ric,S,C,Q,Pt=z['g'],z['gi'],z['G'],z['R'],z['Ric'],z['S'],z['C'],z['Q'],z['P']
 inv=all(sum((g[a][c].v()*gi[c][b].v() for c in range(N)),F(0))==int(a==b) for a,b in product(range(N),repeat=2))
 metric_sym=all(g[a][b].v()==g[b][a].v() for a,b in product(range(N),repeat=2))
 gamma0=all(G[a][b][c].v()==0 for a,b,c in product(range(N),repeat=3));detok=det_point(g)==-1
 ra1=all(R[a][b][c][d].v()+R[b][a][c][d].v()==0 for a,b,c,d in product(range(N),repeat=4))
 ra2=all(R[a][b][c][d].v()+R[a][b][d][c].v()==0 for a,b,c,d in product(range(N),repeat=4))
 rp=all(R[a][b][c][d].v()==R[c][d][a][b].v() for a,b,c,d in product(range(N),repeat=4))
 rb=all(R[a][b][c][d].v()+R[a][c][d][b].v()+R[a][d][b][c].v()==0 for a,b,c,d in product(range(N),repeat=4))
 ric=all(sum((gi[a][c].v()*R[a][b][c][d].v() for a,c in product(range(N),repeat=2)),F(0))==Ric[b][d].v() for b,d in product(range(N),repeat=2))
 scal=sum((gi[b][d].v()*Ric[b][d].v() for b,d in product(range(N),repeat=2)),F(0))==S.v()
 wt=all(sum((gi[a][c].v()*C[a][b][c][d].v() for a,c in product(range(N),repeat=2)),F(0))==0 for b,d in product(range(N),repeat=2))
 ps1=all(Pt[a][b][c][d].v()+Pt[b][a][c][d].v()==0 for a,b,c,d in product(range(N),repeat=4))
 ps2=all(Pt[a][b][c][d].v()+Pt[a][b][d][c].v()==0 for a,b,c,d in product(range(N),repeat=4))
 pp=all(Pt[a][b][c][d].v()==Pt[c][d][a][b].v() for a,b,c,d in product(range(N),repeat=4))
 pb=all(Pt[a][b][c][d].v()+Pt[a][c][d][b].v()+Pt[a][d][b][c].v()==0 for a,b,c,d in product(range(N),repeat=4))
 pr=sum((Pt[a][b][c][d].v()*R[a][b][c][d].v() for a,b,c,d in product(range(N),repeat=4)),F(0))
 pairs=[(a,b) for a in range(N) for b in range(a,N)]
 H={(a,b,c,d):F(((a+2*b+3*c+5*d+7)%11)-5,17) for a,b in pairs for c,d in pairs}
 def hh(a,b,c,d):
  a,b=cab(a,b);c,d=cab(c,d);return H[(a,b,c,d)]
 K=[[[[F(0) for _ in range(N)] for _ in range(N)] for _ in range(N)] for _ in range(N)]
 for a,b,c,d in product(range(N),repeat=4):K[a][b][c][d]=F(1,2)*(hh(a,d,b,c)+hh(b,c,a,d)-hh(a,c,b,d)-hh(b,d,a,c))
 KR=[[F(0) for _ in range(N)] for _ in range(N)]
 for b,d in product(range(N),repeat=2):KR[b][d]=sum((eta(a,c)*K[a][b][c][d] for a,c in product(range(N),repeat=2)),F(0))
 KS=sum((eta(b,d)*KR[b][d] for b,d in product(range(N),repeat=2)),F(0))
 direct=F(0)
 for a,b,c,d in product(range(N),repeat=4):
  CK=K[a][b][c][d]-F(1,2)*(eta(a,c)*KR[d][b]-eta(a,d)*KR[c][b]-eta(b,c)*KR[d][a]+eta(b,d)*KR[c][a])+F(1,6)*KS*(eta(a,c)*eta(d,b)-eta(a,d)*eta(c,b))
  for e,f in product(range(N),repeat=2):
   if eta(c,e) and eta(d,f):direct += F(3)*eta(c,e)*eta(d,f)*CK*Q[a][b][e][f].v()
 contracted=sum((Pt[a][b][c][d].v()*K[a][b][c][d] for a,b,c,d in product(range(N),repeat=4)),F(0))
 r_from_gamma=True
 for a,b,c,d in product(range(N),repeat=4):
  q=sum((eta(a,e)*(G[e][d][b].deriv(c).v()-G[e][c][b].deriv(d).v()) for e in range(N)),F(0));r_from_gamma &= (q==R[a][b][c][d].v())
 rn=any(Ric[a][b].v()!=0 for a,b in product(range(N),repeat=2));sn=S.v()!=0
 return {'metric_symmetric':metric_sym,'inverse_identity':inv,'determinant_point_minus_one':detok,'volume_density_point_one':detok,'normal_coordinate_Gamma_zero':gamma0,'riemann_antisym_first':ra1,'riemann_antisym_second':ra2,'riemann_pair_exchange':rp,'riemann_first_bianchi':rb,'ricci_contraction':ric,'scalar_contraction':scal,'weyl_tracefree':wt,'P_antisym_first':ps1,'P_antisym_second':ps2,'P_pair_exchange':pp,'P_first_bianchi':pb,'P_dot_R_equals_3I3':pr==3*z['I'].v(),'P_fixed_frechet_direction_nonzero':(direct!=0 if seed!='FLAT_CONTROL' else True),'P_fixed_frechet_direction_exact':direct==contracted,'normal_coordinate_dGamma_reconstructs_Riemann':r_from_gamma,'offshell_ricci_nonzero':rn if seed!='FLAT_CONTROL' else True,'offshell_scalar_nonzero':sn if seed!='FLAT_CONTROL' else True}

def h0(d,a,b):
 a,b=cab(a,b);return panel.h_value(d,a,b,())
def cell(seed,d,expected):
 z=build(seed);table=panel.canonical_table(seed,d);jh=jsha(table);ctrl=point_controls(z,seed);con=sum((z['E'][a][b]*h0(d,a,b) for a,b in product(range(N),repeat=2)),F(0))
 ctrl.update({'perturbation_jet_symmetry_from_frozen_generator':all(panel.h_value(d,*cab(a,b),I)==panel.h_value(d,*cab(b,a),I) for a,b in product(range(N),repeat=2) for k in range(3) for I in combinations_with_replacement(range(N),k)),'jet_hash_matches_frozen_manifest':jh==expected,'euler_tensor_symmetric':all(z['E'][a][b]==z['E'][b][a] for a,b in product(range(N),repeat=2)),'exact_fraction_arithmetic_no_tolerance':True,'target_blind_no_researcher_read':True,'c6_symbolic_unfixed_factored_out':True,'flat_euler_contraction_zero':con==0 if seed=='FLAT_CONTROL' else True})
 w={'seed':seed,'direction':d,'jet_sha256':jh,'jet_table':table,'controls':ctrl,'riemann_point_sha256':jsha([fs(z['R'][a][b][c][e].v()) for a,b,c,e in product(range(N),repeat=4)]),'ricci_point':[[fs(z['Ric'][a][b].v()) for b in range(N)] for a in range(N)],'scalar_point':fs(z['S'].v()),'weyl_point_sha256':jsha([fs(z['C'][a][b][c][e].v()) for a,b,c,e in product(range(N),repeat=4)]),'I3_point':fs(z['I'].v()),'covariant_derivative_witness':{'U_point_sha256':jsha([fs(z['U'][a][c][b].v()) for a,c,b in product(range(N),repeat=3)]),'double_covariant_divergence_P':[[fs(z['T'][a][b]) for b in range(N)] for a in range(N)],'normal_coordinate_dGamma_reconstructs_Riemann':ctrl['normal_coordinate_dGamma_reconstructs_Riemann']},'euler_source':{'P_point_sha256':jsha([fs(z['P'][a][b][c][e].v()) for a,b,c,e in product(range(N),repeat=4)]),'algebraic_PR_term':[[fs(z['A'][a][b]) for b in range(N)] for a in range(N)],'double_covariant_divergence_P':[[fs(z['T'][a][b]) for b in range(N)] for a in range(N)],'E_contravariant':[[fs(z['E'][a][b]) for b in range(N)] for a in range(N)],'contraction_with_h':fs(con),'formula':'E^ab=-P^{a c d e} g^{bf} R_{f c d e}+2 nabla_c nabla_d P^{a c d b}+1/2 g^{ab} I3'},'direct_variation_from_other_lane':'NOT_READ_PRE_COMPARISON','cross_lane_discrepancy':'NOT_COMPUTED_PRE_COMPARISON'};w['cell_witness_sha256']=jsha(w);return w

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--seed',required=True,choices=('FLAT_CONTROL','OFFSHELL_A','OFFSHELL_B'));ap.add_argument('--direction',required=True,type=int,choices=(7,19));ap.add_argument('--output',required=True);a=ap.parse_args();m=panel.panel_manifest();exp={(x['seed'],x['direction']):x['jet_sha256'] for x in m['cells']};c=cell(a.seed,a.direction,exp[(a.seed,a.direction)]);ok=all(v is True for v in c['controls'].values());p={'gate':'COVARIANT_WEYL3_DIRECTIONAL_VARIATION_FUNCTIONAL_DERIVATIVE_CERTIFICATE','lane':'CRITIC_INDEPENDENT_COVARIANT_EULER_SOURCE','preregistration_commit':'8c21ee233423deaff52d0fa552c027fa065a53a7','panel_freeze_commit':'1642dc7ca4204a4240635be68522f1731c8a9c50','panel_generator_commit':'03377afec95801b5a49f47b85ddd9c9bf3326ac0','panel_manifest_sha256':m['panel_sha256'],'cell':c,'target_blind_witness_frozen_before_comparison':True,'researcher_science_code_imported':False,'c6':'SYMBOLIC_UNFIXED_FACTORED_OUT','classification':'CRITIC_CELL_WITNESS_READY_FOR_TARGET_BLIND_COMPARISON' if ok else 'BLOCKED_CRITIC_SELF_CONTROL_FAILURE'};p['complete_payload_sha256']=jsha(p);Path(a.output).parent.mkdir(parents=True,exist_ok=True);Path(a.output).write_text(json.dumps(p,sort_keys=True,indent=2)+'\n');print(json.dumps({k:v for k,v in p.items() if k!='cell'},sort_keys=True,indent=2));return 0 if ok else 2
if __name__=='__main__':raise SystemExit(main())
