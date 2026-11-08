# FTAI Power: evidence for the short case

This repo holds the data work behind Thesis 2 of our FTAI Aviation short deck. The thesis argues that FTAI Power falls to zero after its first order: one $1.465bn order from J&F, at most 58 Mod-1 units, due by November 2027. Each slide figure links to a public table, a script and a status. Scrapers refresh the lines that can break the case every week or month.

**Power value = demand shortage (2A) × cost to the buyer (2C) × units delivered (2E) × FTAI's share of J&F (2D)**, with state curbs (2B) moving demand later.

## The five slides

| Slide | Finding | Key figures rerun here | Folder |
|---|---|---|---|
| 2A | The on-site power shortage closes by 2028 | 17.0 GW of identified supply vs. 15.0 GW of base need at end 2028. Mod-1 can compete for 4.1% of planned on-site gas. | [shortage](shortage/) |
| 2B | Curbs delay demand into 2028-29 while rival supply builds | 39 GW stalled today, 52 GW from Jan 2027. Unpermitted Texas gas slips 13.6 months, 0 GW starts in 2027. TCEQ engines clear in 18 days vs. 259 for turbines. 333 large turbines imported in four quarters. | [curbs](curbs/) |
| 2C | Mod-1 costs $187m more than gas engines over ten years for 100 MW | 748 EIA-listed 15-60 MW gas turbines deliver a median 87.7% of nameplate in summer, 84% in Texas. Buyers need 7.5-16 months of head start to repay the premium. | [unit_cost](unit_cost/) |
| 2D | Jereh controls J&F, holds the customer's cash and sells rival gensets | $735m paid to J&F in Q3 2026, up to $501m held at Jereh. $1.13bn of Jereh's own US genset orders. 13 China-built gensets into Houston in Aug-Sep 2026. | [jereh](jereh/) |
| 2E | Bottlenecks cut FY27 Power EBITDA to $279m | 334 days from core to acceptance on average. 67 built, 46 shipped and 27 accepted in 2027. All 58 order units accepted by Q2 2028. | [bottlenecks](bottlenecks/) |

## Figures that moved against the slides

| Figure | Slide prints | Repo gives | Folder |
|---|---:|---:|---|
| Identified new supply by end 2028 | 14.1 GW | 14.04 GW, the sum of the slide's own chart | [shortage/supply_timeline](shortage/supply_timeline/) |
| Gas MW due by Aug 2026 that slipped, outside Texas | 16% | 15.3% | [curbs/eia_slip](curbs/eia_slip/) |
| Months a developer needs to repay the Mod-1 premium | 12.5 | 12.4 | [unit_cost/buyer_payback](unit_cost/buyer_payback/) |
| Average days from core to acceptance | 335 | 334.3 | [bottlenecks/production_sim](bottlenecks/production_sim/) |

The September 2026 EIA-860M file moved the national slip share for the Aug 2025 cohort from 29.9% to 21.1%, as 78.9% of that MW now runs. The Texas slip share held at 61.4%. The slide quotes the August file, and [watch/eia860m](watch/eia860m/) carries every later file.

## Watch lines

| Line | Slide | Cadence | Fires when | Effect on the case |
|---|---|---|---|---|
| Texas filings resume | 2B | Weekly | Power-plant permit applications reach half the 2025 monthly median | Weakens it |
| Texas cohort catches up | 2B | Monthly | Under 30% of the Texas Aug 2025 gas cohort is still slipped | Weakens it |
| Turbine imports slow | 2B | Monthly | Large gas turbines imported over four quarters fall below 167 | Weakens it |
| Second Mod-1 order | 2D, 2E | Weekly | An FTAI filing names an order amount other than $1.465bn | Weakens it |
| China gensets land | 2D | Monthly | Gensets from China reach Houston in the last three months | Supports it |
| DOE rule published | 2D | Weekly | A DOE or Commerce rule on foreign-adversary equipment appears in the Federal Register | Supports it |

A local job pulls the TCEQ air-permit registry, FTAI's SEC filings and the Federal Register every Monday. On the 12th and 28th of each month it pulls US Census import data and the newest EIA-860M generator file. Each source gets one worker, and requests are paced. The job commits only counts and test results to [watch](watch/). A GitHub Action reruns every check each Monday afternoon. A red run means a scraper stopped or a line marked "weakens it" fired. [watch/STATUS.md](watch/STATUS.md) shows the latest reading of each line.

## Every figure

`figures.csv` records each figure's slide value, repo value, sample and limit. Holding means the figure reran to the slide's rounding. Weakened means the rerun differs from the slide.

<!-- table start -->
| Slide | Term | Holding | Weakened |
|---|---|---|---|
| 2A | [shortage](shortage/) | 7 | 1 |
| 2B | [curbs](curbs/) | 26 | 1 |
| 2C | [unit_cost](unit_cost/) | 10 | 1 |
| 2D | [jereh](jereh/) | 8 | 0 |
| 2E | [bottlenecks](bottlenecks/) | 10 | 1 |
| | **All** | **61** | **4** |
<!-- table end -->

## Running it

Requirements are Python 3.12 and `pip install -r requirements.txt`.

```
python reproduce.py
```

The script runs each study from committed public tables, compares results with `figures.csv` and checks that every table serves a figure. No scraping, API key or licensed file is required. Broker estimates, consensus files and expert calls stay out of the repo.
