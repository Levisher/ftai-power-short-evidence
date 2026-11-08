import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
import pandas as pd, numpy as np
from evidence import save
s = pd.read_csv('supply_dated.csv'); n = pd.read_csv('need_forecasts.csv')
run = lambda y: s[s.first_year <= y].gw.sum()
need = lambda c, y: n[(n.case == c) & (n.year == y)].gw.iloc[0]
first22 = next(y for y in range(2026, 2031) if run(y) >= need('Open Factory high', 2028))
save(__file__, dict(supply_2027=run(2027), supply_2028=run(2028), supply_2030=run(2030), gap_2027=run(2027) - need('Open Factory base', 2027),
                    gap_2028=run(2028) - need('Open Factory base', 2028), new_supply_2028=run(2028) - s[s.group == 'Existing'].gw.sum(), first_year_22gw=first22))
