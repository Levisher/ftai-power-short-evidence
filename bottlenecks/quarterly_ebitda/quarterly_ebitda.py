import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
import pandas as pd, numpy as np
from evidence import save
import csv
r = {x['figure_id']: float(x['value']) for x in csv.DictReader(open('../production_sim/production_sim_results.csv'))}
q = pd.read_csv('../production_sim/sim_quarterly_median.csv')
ORDER_UNITS = 1465 // 25; CONTRACT = 100; PER_STEP = 3.75; J_AND_F_SHARE = 0.49   # $1.465bn at $25m; FTAI books $3.75m at sale to J&F and $3.75m at acceptance
built = min(r['built_2027'], CONTRACT); accepted = min(r['accepted_2027'], ORDER_UNITS)
ebitda27 = PER_STEP * (built + accepted) - J_AND_F_SHARE * PER_STEP * (built - accepted)
cap_q = q[q.accepted >= ORDER_UNITS].quarter_end.min()   # after this quarter no unit is left to accept and no 2028 sale exists
save(__file__, dict(order_units=ORDER_UNITS, fy27_ebitda_m=ebitda27, fy27_accepted=accepted, order_filled_by_q2_28=int(cap_q <= '2028-06-30')))
