import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
import pandas as pd, numpy as np
from evidence import save
v = pd.read_csv('payback_inputs.csv').set_index('input').value
mwh = 100 * 0.9 * 8760; ann = (1 - (1 + v.rate) ** -10) / v.rate
def cost(mw, price, site, life, hr, vom):
    build = mw * (price + site) / 1000
    return build - build * (1 - 10 / life) / (1 + v.rate) ** 10 + mwh * hr * v.gas / 1e6 * ann + (mw * v.fom / 1000 + mwh * vom / 1e6) * ann
prem = cost(v.mw_mod1, v.price_mod1, v.site_mod1, v.life_mod1, v.hr_mod1, v.vom_mod1) - cost(v.mw_eng, v.price_eng, 0, v.life_eng, v.hr_eng, v.vom_eng)
gpus = 1000 / (v.kw_per_gpu * v.pue)
gpu = gpus * v.h100_contract * v.hours_month * v.rented_share * v.gpu_margin / 1e6 * 100 - gpus * 100 * v.hgx_price / 8 / v.gpu_life_months / 1e6
dev = v.dev_value_gw_month / 10; colo = v.colo_rent * 1000 * 100 * v.colo_margin / 1e6
save(__file__, dict(premium_m=prem, gpu_month_m=gpu, dev_month_m=dev, colo_month_m=colo, gpu_payback=prem / gpu, dev_payback=prem / dev, colo_payback=prem / colo))
