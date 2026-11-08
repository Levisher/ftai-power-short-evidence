import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
import pandas as pd, numpy as np
from evidence import save
d = pd.read_csv('eia860m_gas_cohort.csv'); c = d[d.due_month_index <= 2026 * 12 + 8]
sh = lambda x, f: 100 * x[x.fate_aug2026 == f].mw.sum() / x.mw.sum()
tx = c[c.state == 'TX']; rest = c[c.state != 'TX']
save(__file__, dict(cohort_gw=c.mw.sum() / 1000, online_pct=sh(c, 'online'), slipped_pct=sh(c, 'slipped'), cancelled_pct=sh(c, 'canceled/postponed'),
                    tx_slipped_pct=sh(tx, 'slipped'), rest_slipped_pct=sh(rest, 'slipped'), tx_slipped_mw=tx[tx.fate_aug2026 == 'slipped'].mw.sum(),
                    median_slip_months=c.slip_months.median()))
