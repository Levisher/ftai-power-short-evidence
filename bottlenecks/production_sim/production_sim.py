import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
import pandas as pd, numpy as np
from evidence import save
import datetime as dt
st = pd.read_csv('stage_days.csv'); STAGES = [(r.stage, (r.min_days, r.mode_days, r.max_days)) for r in st.itertuples()]
rng = np.random.default_rng(11); N = 120; RUNS = 1000; T0 = pd.Timestamp('2026-09-01')
tri = lambda a, m, b, n: rng.triangular(a, m, b, n)
CASES = {'Bull': dict(conv_cap=(4, 9, 6), pkg_cap=(4, 10, 6), yield_turb=0.95, yield_pkg=0.95, parts_mult=0.8, start='2026-09-01'),
         'Base': dict(conv_cap=(2, 8.3, 9), pkg_cap=(2, 8, 9), yield_turb=0.90, yield_pkg=0.90, parts_mult=1.0, start='2026-10-01'),
         'Bear': dict(conv_cap=(1, 6, 12), pkg_cap=(1, 6, 12), yield_turb=0.80, yield_pkg=0.85, parts_mult=1.5, start='2027-01-01')}
def slots(start, full, ramp, t0):
    out = []; m = 0; carry = 0.0
    while len(out) < N * 2:
        c = start + (full - start) * min(m / ramp, 1) + carry; k = int(c); carry = c - k; d0 = t0 + pd.DateOffset(months=m)
        out += [d0 + pd.Timedelta(days=int(30 * (j + 0.5) / max(k, 1))) for j in range(k)]; m += 1
    return out
QE = pd.to_datetime(['2027-03-31', '2027-06-30', '2027-09-30', '2027-12-31', '2028-03-31', '2028-06-30'])
res = []; curves = []
for case, p in CASES.items():   # all cases run in order so the seeded draws match the deck
    conv = slots(*p['conv_cap'], pd.Timestamp(p['start'])); pkg0 = slots(*p['pkg_cap'], pd.Timestamp(p['start']) + pd.DateOffset(months=3))
    for r in range(RUNS):
        d = {s: tri(*rr, N) for s, rr in STAGES}; d[STAGES[2][0]] *= p['parts_mult']
        ready = T0 + pd.to_timedelta(d[STAGES[0][0]] + d[STAGES[1][0]] + d[STAGES[2][0]], unit='D')
        cs = [max(conv[i], ready[i]) for i in range(N)]
        rw = np.where(rng.random(N) > p['yield_turb'], tri(10, 20, 40, N), 0)
        turb = [cs[i] + pd.Timedelta(days=float(d[STAGES[3][0]][i] + d[STAGES[4][0]][i] + rw[i])) for i in range(N)]
        arrive = sorted(t + pd.Timedelta(days=float(x)) for t, x in zip(turb, d[STAGES[5][0]]))
        ps = list(pkg0); pk = []
        for a in arrive:
            j = next(k for k, s in enumerate(ps) if s >= a - pd.Timedelta(days=30)); pk.append(max(ps.pop(j), a))
        rp = np.where(rng.random(N) > p['yield_pkg'], tri(7, 14, 30, N), 0)
        packed = [pk[i] + pd.Timedelta(days=float(d[STAGES[6][0]][i] + d[STAGES[7][0]][i] + rp[i])) for i in range(N)]
        acc = sorted(packed[i] + pd.Timedelta(days=float(d[STAGES[8][0]][i] + d[STAGES[9][0]][i] + d[STAGES[10][0]][i])) for i in range(N))
        y = pd.Timestamp('2027-12-31')
        res.append(dict(case=case, built=sum(t <= y for t in turb), shipped=sum(t <= y for t in packed), accepted=sum(t <= y for t in acc)))
        if case == 'Base' and r < 200:
            for q in QE:
                curves.append(dict(quarter_end=q.date(), built=sum(t <= q for t in turb), shipped=sum(t <= q for t in packed), accepted=sum(t <= q for t in acc)))
b = pd.DataFrame(res); b = b[b.case == 'Base']
pd.DataFrame(curves).groupby('quarter_end').median().reset_index().to_csv('sim_quarterly_median.csv', index=False)
mean = ((st.min_days + st.mode_days + st.max_days) / 3)
save(__file__, dict(mean_days=mean.sum(), hot_section_days=mean[2], core_days=mean[3], packaging_days=mean[6], accept_days=mean[9] + mean[10],
                    built_2027=b.built.median(), shipped_2027=b.shipped.median(), accepted_2027=b.accepted.median()))
