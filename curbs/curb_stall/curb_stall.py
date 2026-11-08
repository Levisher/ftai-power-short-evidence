import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
import pandas as pd, numpy as np
from evidence import save
d = pd.read_csv('eip_plants.csv'); d['year'] = d.year.fillna(0)
PAU = {'TX', 'NY', 'OR'}; RES = {'AZ', 'IL', 'KY', 'LA', 'MA', 'NE', 'NV', 'OH', 'PA', 'UT', 'VA'}
PAU27 = PAU | {'OH', 'GA'}; RES27 = RES - {'OH'}
nofinal = d.final_permit == 0
stalled = lambda p: d[d.state.isin(p) & nofinal]
curbed = d[d.state.isin(PAU | RES)]
save(__file__, dict(plants=len(d), gw_all=d.mw.sum() / 1000, gw_curbed=curbed.mw.sum() / 1000, gw_curbed_unpermitted=curbed[curbed.final_permit == 0].mw.sum() / 1000,
                    stalled_now_gw=stalled(PAU).mw.sum() / 1000, stalled_jan27_gw=stalled(PAU27).mw.sum() / 1000,
                    stalled_now_plants=len(stalled(PAU)), stalled_jan27_plants=len(stalled(PAU27))))
