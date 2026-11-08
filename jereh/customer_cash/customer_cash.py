import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
import pandas as pd, numpy as np
from evidence import save
q = pd.read_csv('jereh_quarterly.csv').set_index('quarter')
ORDER_USD, ORDER_RMB, FTAI_LIAB = 1465, 9950, 234   # $m and RMB m of the 22 Jul 2026 order; FTAI 10-Q contract liability to J&F, 30 Sep 2026
fx = ORDER_RMB / ORDER_USD; paid = (q.contract_liabilities_rmb_m["Q3'26"] - q.contract_liabilities_rmb_m["Q2'26"]) / fx
save(__file__, dict(q3_rise_rmb_m=q.contract_liabilities_rmb_m["Q3'26"] - q.contract_liabilities_rmb_m["Q2'26"], paid_usd_m=paid, unpaid_usd_m=ORDER_USD - paid,
                    held_at_jereh_usd_m=paid - FTAI_LIAB, ppe_growth_pct=100 * (q.ppe_net_rmb_m["Q3'26"] / q.ppe_net_rmb_m["Q4'25"] - 1),
                    inventory_growth_pct=100 * (q.inventory_rmb_m["Q3'26"] / q.inventory_rmb_m["Q4'25"] - 1)))
