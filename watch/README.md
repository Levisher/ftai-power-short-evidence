# Watch lines

Each folder holds one series, a `runs.csv` log of every collection and the files `watch.py` reads.

| Folder | Source | Cadence | What is kept |
|---|---|---|---|
| tceq | TCEQ NSR air-permit registry, every project received in the last four months | Weekly | Power-generation applications a month, matched on customer and project names as in curbs/tceq_permits |
| filings | SEC EDGAR filings of FTAI Aviation (CIK 1590364), 8-K, 10-Q and 10-K | Weekly | Filing date, form, link, and a flag when a Mod-1 or J&F passage names an order amount other than $1.465bn |
| federal_register | Federal Register documents on foreign-adversary turbines, generators, data centres and the bulk-power system since 26 Aug 2026 | Weekly | Title, type, agencies, and a flag for DOE or Commerce rules |
| imports | US Census imports, HS 8411.82.8010 from all countries and HS 8502.39.0080 from China into Houston-Galveston | 12th and 28th | Monthly units and customs value |
| eia860m | Newest EIA-860M generator file | 12th and 28th | Share of the Aug 2025 gas cohort online, slipped and cancelled, nationally and in Texas |

`watch.py` writes `STATUS.md` and `watch_results.csv`. Set `reviewed` to 1 in `filings/ftai_filings.csv` once a flagged filing has been read.
