"""Checks every watch line against its trigger and writes STATUS.md.

Fails when a line marked 'against' fires (the thesis weakens) or when a series has no complete run inside its stale window.
Lines marked 'for' report when they fire and never fail the run.
"""
import datetime as dt, pathlib, sys
import pandas as pd
H = pathlib.Path(__file__).resolve().parent
L = pd.read_csv(H / 'watch_lines.csv'); today = pd.Timestamp(dt.date.today())


def last_ok(series):
    r = pd.read_csv(H / series / 'runs.csv'); r = r[r.status.isin(['complete', 'no new data', 'no new file', 'seeded'])]
    return pd.to_datetime(r.run_date).max()


def reading(line):
    if line == 'texas_filings_resume':
        m = pd.read_csv(H / 'tceq/tceq_power_monthly.csv', dtype={'month': str}).set_index('month').power_apps_received
        bar = m[m.index.str.startswith('2025')].median() / 2; done = m[m.index < today.strftime('%Y-%m')]
        return done.iloc[-1] >= bar, f'{int(done.iloc[-1])} applications in {done.index[-1]}, trigger {bar:.1f}'
    if line == 'texas_cohort_catches_up':
        f = pd.read_csv(H / 'eia860m/cohort_fates.csv').iloc[-1]
        return f.tx_slipped_pct < 30, f'{f.tx_slipped_pct:.1f}% of Texas cohort MW still slipped in {f.file}'
    if line == 'turbine_imports_slow':
        t = pd.read_csv(H / 'imports/turbines_8411828010.csv', dtype={'month': str}); t['q'] = pd.PeriodIndex(t.month, freq='M').asfreq('Q')
        q = t.groupby('q').agg(units=('units', 'sum'), n=('month', 'count')); q = q[q.n == 3]
        return q.units.tail(4).sum() < 167, f'{int(q.units.tail(4).sum())} units in the four quarters to {q.index[-1]}'
    if line == 'second_mod1_order':
        f = pd.read_csv(H / 'filings/ftai_filings.csv')
        open_hits = f[(f.order_hit == 1) & (f.reviewed == 0)]
        return len(open_hits) > 0, f'{len(f)} filings checked since 29 Oct 2026, {len(open_hits)} unreviewed with a new order amount'
    if line == 'china_gensets_land':
        g = pd.read_csv(H / 'imports/gensets_china_houston_8502390080.csv', dtype={'month': str}).tail(3)
        return g.units.sum() > 0, f'{int(g.units.sum())} units, {g.month.iloc[0]} to {g.month.iloc[-1]}'
    if line == 'doe_rule_published':
        d = pd.read_csv(H / 'federal_register/fr_documents.csv')
        hits = d[d.rule_hit == 1]
        return len(hits) > 0, f'{len(d)} documents since 26 Aug 2026, {len(hits)} DOE or Commerce rules'


rows = []; bad = 0
for x in L.itertuples():
    fired, text = reading(x.line); age = (today - last_ok(x.series)).days; stale = age > x.stale_days
    state = 'stale' if stale else ('fired' if fired else 'quiet')
    bad += stale or (fired and x.side == 'against')
    rows.append(dict(line=x.line, slide=x.slide, side=x.side, state=state, reading=text, last_run_days=age, meaning=x.meaning))
r = pd.DataFrame(rows); r.to_csv(H / 'watch_results.csv', index=False)
out = [f'# Watch status, {today:%d %b %Y}', '', '| Line | Slide | Side | State | Reading | Days since run |', '|---|---|---|---|---|---:|']
out += [f'| {x.line} | {x.slide} | {x.side} | {x.state} | {x.reading} | {x.last_run_days} |' for x in r.itertuples()]
(H / 'STATUS.md').write_text('\n'.join(out) + '\n')
print(r[['line', 'state', 'reading']].to_string(index=False))
sys.exit(1 if bad else 0)
