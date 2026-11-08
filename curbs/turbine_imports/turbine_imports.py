import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
import pandas as pd, numpy as np
from evidence import save
d = pd.read_csv('us_imports_8411828010_monthly.csv'); d['q'] = pd.PeriodIndex(d.month, freq='M').asfreq('Q')
q = d[d.month <= '2026-09'].groupby('q').qty.sum()
save(__file__, dict(units_last4q=q.tail(4).sum(), units_q3_26=q[pd.Period('2026Q3')], units_2024=q[q.index.year == 2024].sum()))
