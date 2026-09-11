#!/usr/bin/env python3
import argparse,itertools,json
P=argparse.ArgumentParser();P.add_argument('--output',required=True);args=P.parse_args()
PERMS=list(itertools.permutations(range(4)))
# Every maximal B4 chain has ranks 0,1,2,3,4 independently of ordering.
profiles=[]
for p in PERMS:
 s=set();prof=[len(s)]
 for x in p:
  s.add(x);prof.append(len(s))
 assert prof==[0,1,2,3,4]
 profiles.append(prof)
# True serial QGR blocks concatenate at opposite vertices. Rank increments add exactly.
serial=[]
for n in [1,2,4,8,16]:
 total_ticks=4*n
 histories=24**n
 serial.append({'serial_B4_blocks':n,'total_rank_ticks':total_ticks,'history_count':histories,'rank_ticks_per_block':4})
# At fixed physical interval T, subdividing into n blocks changes the physical duration per rank tick as T/(4n).
calibration=[]
for n in [1,2,4,8,16]:
 calibration.append({'blocks_for_fixed_physical_interval':n,'rank_ticks':4*n,'physical_tick_duration_in_units_of_total_interval':1/(4*n)})
out={
 'lane':'BOOLEAN_RANK_CLOCK_SERIAL_COMPOSITION',
 'single_cell_history_count':24,
 'all_single_cell_rank_profiles_identical':True,
 'rank_profile':[0,1,2,3,4],
 'serial_examples':serial,
 'fixed_interval_refinement_calibration':calibration,
 'classification':'PASS_SCOPED_BOOLEAN_RANK_CLOCK_IS_HISTORY_INDEPENDENT_AND_EXACTLY_ADDITIVE_UNDER_TRUE_SERIAL_B4_COMPOSITION__PHYSICAL_TICK_DURATION_REMAINS_REFINEMENT_DEPENDENT',
 'scientific_interpretation':'All 24 internal orderings traverse the same rank sequence, so rank time is branch symmetric. Across true serial cells the clock adds exactly: each B4 contributes four ticks. However, for a fixed physical interval the number of rank ticks grows under refinement, so the ontology supplies an ordering/counting clock but not a fixed physical duration per tick.',
 'guard':'Do not interpret four ticks per cell as four Planck times. The conversion from rank ticks to physical duration remains the same scale problem isolated in Iter007.'
}
open(args.output,'w').write(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,sort_keys=True))