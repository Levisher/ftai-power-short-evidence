import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
import pandas as pd, numpy as np
from evidence import save
d = pd.read_csv('texas_unpermitted.csv', parse_dates=['filed'])
s = pd.read_csv('../tceq_permits/tceq_power_psd.csv', parse_dates=['rcv', 'cmp']); s = s[s.project_status == 'COMPLETE']
PERMIT = (s.cmp - s.rcv).dt.days.median(); BUILD = 16   # months, permit to operation, EIP Texas plants
def months(a, b):
    return (b.year - a.year) * 12 + b.month - a.month - (b.day < a.day)
def run(days, pause):
    pause = pd.Timestamp(pause); start = d.filed.fillna(pause).apply(lambda f: max(f + pd.Timedelta(days=days), pause) + pd.DateOffset(months=BUILD))
    delay = [months(pd.Timestamp(y, 12, 31), t) for y, t in zip(d.due_eip, start)]
    return np.average(delay, weights=d.gw), d.gw[start.dt.year <= 2027].sum()
base, gw27 = run(PERMIT, '2026-12-10')
grid = [run(x, p) for x in (180, 300, 420) for p in ('2026-12-10', '2027-03-31', '2027-06-30')]
save(__file__, dict(gw=d.gw.sum(), permit_days=PERMIT, delay_months=base, gw_start_2027=gw27, delay_low=min(g[0] for g in grid), delay_high=max(g[0] for g in grid), gw_2027_any=max(g[1] for g in grid)))
