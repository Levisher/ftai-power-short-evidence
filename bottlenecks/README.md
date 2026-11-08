# Slide 2E: Bottlenecks cut FY27 Power EBITDA and the order runs out in 2028

| Study | Figure | On slide | Repo | Status | Sample |
|---|---|---|---:|---|---|
| [production_sim](production_sim/) | Average days from core to customer acceptance | 335 days | 334.33 | weakened | Unit-by-unit simulation, 120 units, 1,000 runs, Base case P50, stage ranges from FTAI calls and filings in stage_days.csv |
| [production_sim](production_sim/) | Hot-section parts, average days | 60 | 59.67 | holding | Unit-by-unit simulation, 120 units, 1,000 runs, Base case P50, stage ranges from FTAI calls and filings in stage_days.csv |
| [production_sim](production_sim/) | Core conversion, average days | 87 | 86.67 | holding | Unit-by-unit simulation, 120 units, 1,000 runs, Base case P50, stage ranges from FTAI calls and filings in stage_days.csv |
| [production_sim](production_sim/) | Jereh packaging, average days | 50 | 50.00 | holding | Unit-by-unit simulation, 120 units, 1,000 runs, Base case P50, stage ranges from FTAI calls and filings in stage_days.csv |
| [production_sim](production_sim/) | Commission and acceptance, average days | 69 | 69.33 | holding | Unit-by-unit simulation, 120 units, 1,000 runs, Base case P50, stage ranges from FTAI calls and filings in stage_days.csv |
| [production_sim](production_sim/) | Turbines built in 2027 | 67 | 67.00 | holding | Unit-by-unit simulation, 120 units, 1,000 runs, Base case P50, stage ranges from FTAI calls and filings in stage_days.csv |
| [production_sim](production_sim/) | Units shipped in 2027 | 46 | 46.00 | holding | Unit-by-unit simulation, 120 units, 1,000 runs, Base case P50, stage ranges from FTAI calls and filings in stage_days.csv |
| [production_sim](production_sim/) | Units accepted in 2027 | 27 | 27.00 | holding | Unit-by-unit simulation, 120 units, 1,000 runs, Base case P50, stage ranges from FTAI calls and filings in stage_days.csv |
| [quarterly_ebitda](quarterly_ebitda/) | FY27 Power EBITDA, Base case ($m) | $279m | 279.00 | holding | Simulation medians at 31 Dec 2027, $3.75m at sale to J&F and at acceptance, less 49% of unsold margin (FTAI Q2 2026 call) |
| [quarterly_ebitda](quarterly_ebitda/) | Units on the one disclosed order ($1.465bn / $25m) | 58 | 58.00 | holding | FTAI and Jereh releases, 22 Jul 2026 |
| [quarterly_ebitda](quarterly_ebitda/) | All 58 order units accepted by Q2 2028, so EBITDA is $0 from Q3 2028 (1 = yes) | $0 from Q3 2028 | 1.00 | holding | Simulation medians of 200 runs at quarter ends |

## Limits

- production_sim: Repo gives 334.33. Stage ranges are not disclosed for Jereh packaging and testing.
- quarterly_ebitda: No buyer beyond the 58 units of the one disclosed order.
