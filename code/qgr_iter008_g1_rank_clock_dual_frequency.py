#!/usr/bin/env python3
import argparse,json,math,cmath
P=argparse.ArgumentParser();P.add_argument('--output',required=True);args=P.parse_args()
# Serial additive rank time is integer-valued. The Pontryagin dual of Z is U(1): theta in [-pi,pi).
# Translation by one tick has eigenvalue exp(-i theta). Theta is dimensionless and continuous modulo 2pi.
thetas=[-math.pi,-2.0,-0.7,0.0,0.9,2.4,math.pi-1e-6]
rows=[]
for th in thetas:
 z=cmath.exp(-1j*th)
 rows.append({'theta':th,'unit_tick_eigenvalue_real':z.real,'unit_tick_eigenvalue_imag':z.imag,'modulus':abs(z)})
 assert abs(abs(z)-1)<1e-14
# A physical tick duration Delta t would map theta to quasi-energy E=hbar theta/Delta t modulo 2pi hbar/Delta t.
# Changing Delta t rescales the entire physical quasi-energy band but leaves all dimensionless clock data unchanged.
dts=[0.25,0.5,1.0,2.0,4.0]
bands=[{'tick_duration_ratio':dt,'quasi_energy_bandwidth_in_hbar_units':2*math.pi/dt} for dt in dts]
out={
 'lane':'BOOLEAN_RANK_CLOCK_DUAL_FREQUENCY',
 'integer_clock_group':'Z on serial extension',
 'dual_group':'U(1)',
 'sample_dual_phases':rows,
 'physical_band_examples':bands,
 'classification':'PARTIAL_SCOPED_INTEGER_RELATIONAL_CLOCK_GIVES_A_COMPACT_DIMENSIONLESS_QUASI_FREQUENCY_BUT_DOES_NOT_FIX_THE_PHYSICAL_TICK_DURATION_OR_ENERGY_SCALE',
 'scientific_interpretation':'The additive integer clock has a natural compact dual phase theta. This is a genuine new structural fact: one-tick translations are represented by U(1) phases and quasi-frequency is bounded modulo 2pi in dimensionless units. But converting theta to physical energy requires the tick duration Delta t, so the compact dual does not by itself solve the Iter007 scale problem.',
 'guard':'Do not call the dual phase a physical energy spectrum until a tick-to-time calibration is derived. Compact quasi-frequency is dimensionless and does not quantize g or h by itself.'
}
open(args.output,'w').write(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,sort_keys=True))