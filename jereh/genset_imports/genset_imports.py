import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
import pandas as pd, numpy as np
from evidence import save
d = pd.read_csv('china_houston_8502390080_monthly.csv'); a = d[d.month.isin(['2026-08', '2026-09'])]; b = d[(d.month >= '2025-01') & (d.month <= '2026-07')]
save(__file__, dict(units_aug_sep=a.qty.sum(), value_aug_sep_m=a.value.sum() / 1e6, max_month_before_m=b.value.max() / 1e6,
                    unit_value_low_m=(a.value / a.qty).min() / 1e6, unit_value_high_m=(a.value / a.qty).max() / 1e6))
