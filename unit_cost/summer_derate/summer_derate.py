import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
import pandas as pd, numpy as np
from evidence import save
d = pd.read_csv('eia860m_gas_turbines_15_60mw.csv'); r = d.summer_mw / d.nameplate_mw
tx = r[d.state == 'TX'].median()
save(__file__, dict(units=len(d), median_ratio_pct=100 * r.median(), texas_ratio_pct=100 * tx, mod1_summer_mw=25 * tx))
