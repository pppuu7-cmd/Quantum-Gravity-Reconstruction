#!/usr/bin/env python3
import json,math

# Exact G6F normalized overlaps:
# A0(gamma)=2/(1+gamma)
# A1(gamma)=4(2+gamma)/(3(1+gamma)^2).
# If relative rapidity r=O(h^2), gamma=cosh r=1+O(h^4).
# State norm distance satisfies ||psi_r-psi_0||^2=2(1-Re A), hence O(r^2),
# so the state distance is O(r)=O(h^2).
def A0(g): return 2.0/(1.0+g)
def A1(g): return 4.0*(2.0+g)/(3.0*(1.0+g)**2)
hs=[0.25,0.125,0.0625,0.03125,0.015625]
rows=[]
for h in hs:
    r=h*h
    g=math.cosh(r)
    d0=math.sqrt(max(0.0,2.0*(1.0-A0(g))))
    d1=math.sqrt(max(0.0,2.0*(1.0-A1(g))))
    rows.append({'h':h,'r':r,'d_m0':d0,'d_m1':d1,'d0_over_h2':d0/(h*h),'d1_over_h2':d1/(h*h)})
def slope(key):
    xs=[math.log(r['h']) for r in rows];ys=[math.log(r[key]) for r in rows]
    mx=sum(xs)/len(xs);my=sum(ys)/len(ys)
    return sum((x-mx)*(y-my) for x,y in zip(xs,ys))/sum((x-mx)**2 for x in xs)
s0=slope('d_m0');s1=slope('d_m1')
assert 1.9<s0<2.1 and 1.9<s1<2.1,(s0,s1,rows)
# Dyadic h^2 state increments are summable.
series=sum((2.0**(-n))**2 for n in range(1,80))
assert abs(series-1.0/3.0)<1e-14
out={
  'gate':'ITER009-G5-PACKET-STRONG-CONVERGENCE',
  'rows':rows,
  'distance_log_h_slopes':{'m0':s0,'m1':s1},
  'dyadic_h2_series_sum':series,
  'classification':'PASS_SCOPED_GIVEN_THE_VERIFIED_OH2_RELATIVE_RAPIDITY_LAW_THE_SPECIFIED_G6F_PACKET_STATES_HAVE_OH2_STRONG_DISTANCE_AND_A_SUMMABLE_DYADIC_REFINEMENT_BOUND',
  'guard':'This is strong convergence for the specified normalized packet family under the relative-rapidity scaling input, not operator-norm convergence on the full characteristic Hilbert space.'
}
print(json.dumps(out,sort_keys=True))
