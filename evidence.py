"""Shared helper: each study writes <study>_results.csv beside itself, and reproduce.py compares it with figures.csv."""
import csv, pathlib


def save(file, results):
    p = pathlib.Path(file).resolve(); out = p.with_name(p.stem + '_results.csv')
    with open(out, 'w', newline='') as f:
        w = csv.writer(f); w.writerow(['figure_id', 'value'])
        for k, v in results.items():
            w.writerow([k, repr(round(float(v), 6))])
    for k, v in results.items():
        print(f'{k:32s} {float(v):,.4f}')
