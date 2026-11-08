import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
import pandas as pd, numpy as np
from evidence import save
d = pd.read_csv('jereh_us_orders.csv')
save(__file__, dict(own_orders_usd_m=d[d.buyer_entity == 'GenSystems'].usd_m.sum(), own_orders=int((d.buyer_entity == 'GenSystems').sum()), all_usd_m=d.usd_m.sum()))
