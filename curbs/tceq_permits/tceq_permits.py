import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
import pandas as pd, numpy as np
from evidence import save
p = pd.read_csv('tceq_power_permits.csv', parse_dates=['rcv', 'cmp']); s = pd.read_csv('tceq_power_psd.csv', parse_dates=['rcv', 'cmp'])
n = pd.read_csv('tceq_nsr_monthly.csv')
asof = pd.Timestamp('2026-11-07')
pend = s[s.project_status == 'PENDING']; done = s[s.project_status == 'COMPLETE']
init = p[(p.project_status == 'COMPLETE') & (p.project_type == 'INITIAL')]; days = (init.cmp - init.rcv).dt.days
m = p.groupby(p.rcv.dt.to_period('M')).size()
save(__file__, dict(nsr_records=n.records.sum(), pending_major=len(pend), median_wait_pending=(asof - pend.rcv).dt.days.median(),
                    median_days_to_issue=(done.cmp - done.rcv).dt.days.median(), std_permit_days=days[init.permit_type == 'STDPMT'].median(),
                    construct_days=days[init.permit_type == 'CONSTRUCT'].median(), psd_days=days[init.permit_type == 'PSD'].median(),
                    power_apps_oct26=m.get(pd.Period('2026-10'), 0), power_apps_2025_median=m.reindex(pd.period_range('2025-01', '2025-12', freq='M'), fill_value=0).median()))
