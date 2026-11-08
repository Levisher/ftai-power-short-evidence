import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
import pandas as pd, numpy as np
from evidence import save
d = pd.read_csv('eip_sites_tests.csv'); d = d[d.mw > 0]
tests = ['by2028', 'notCC', 'notEng', 'notFrame', 'permit', 'notBloom', 'notTXpend', 'notUC', 'fits']
left = d[(d[tests] == 1).all(axis=1)]
save(__file__, dict(plants=len(d), gw_all=d.mw.sum() / 1000, gw_open=left.mw.sum() / 1000, share_open_pct=100 * left.mw.sum() / d.mw.sum(), plants_open=len(left), units_open=left.units_9999.sum()))
