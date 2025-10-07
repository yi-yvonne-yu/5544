
# Life Expectancy by Region — Assignment README

This project demonstrates an end‑to‑end workflow: **prepare data**, **ask a single task-driven question**, **generate a D3 visualization** for both small and large datasets, and **critique & iterate** on AI‑generated output.

---

## Step‑by‑Step Answers

### 1) Data preparation (You, 10 pts)
- **Goal:** Generate a small and a large CSV for the visualization.
- **How:** Run `make_regions.py` to produce:
  - `life_expectancy_regions.csv` — full dataset (regional mean life expectancy per year).
  - `life_expectancy_regions_sample.csv` — same metric from a **20% country panel** per region.
- **Source:** World Bank WDI bulk files (`WDICSV.csv`, `WDICountry.csv`), indicator **`SP.DYN.LE00.IN`** (years).

### 2) Apply core vis principles: choose **one task** (You, 15 pts)
- **Chosen question:** *Is there a correlation between life expectancy and region over the years?*  
  → This is a **time** question, so we use a **line chart** with **Region** as series.

### 3) Generate a chart from the small data (AI, 5 pts)
- **Action:** Ask AI for D3 code that answers the question using the **small** CSV.
- **UI mapping:** **Button one** loads `life_expectancy_regions_sample.csv`.

### 4) Generate a chart from the large data (AI, 5 pts)
- **Action:** Ask AI for D3 code that answers the question using the **large** CSV.
- **UI mapping:** **Button two** loads `life_expectancy_regions.csv`.

### 5) Check awareness of different data sizes (You, 10 pts)
- **Observation:** AI keeps the **same code and visual style**, only swapping the data source.  
  This enables direct comparison between full vs. 20% sample.

### 6) Critique the AI output with guidelines (You, 15 pts)
- **Match chart to question:** time → line; latest comparison → bar; correlation → scatter. Switch when the question changes.
- **Be clear on data:** name indicator + units; **drop NaNs**; exclude aggregates; state aggregation (**mean per Region–Year**).
- **Scales & axes:** linear y; integer year ticks; clear axis titles; sensible tick density.
- **Color & legend:** colorblind‑safe palette; **legend required** when color encodes region.
- **Layout:** give labels space (y‑label **outside**); keep aspect ratio readable.
- **Interactivity:** tooltips (region/value); dataset toggle with visible active state.
- **Missing data:** don’t draw through gaps (`line.defined`); annotate/omit sparse series.
- **Clutter control:** use highlight‑on‑hover or small multiples when lines overlap.
- **Consistency:** keep y‑domain stable across toggles for fair visual comparison.
- **Transparency:** cite **WDI** and document sampling (20% + seed).

### 7) Ask AI to fix items one‑by‑one (AI, 5 pts)
- Example requests:
  - **index_legacy_1.html → index_legacy_2.html**
  - **make_region_legacy.py → make_region.py**
  - **Remove NaN** values before averaging.
  - **“Showing out”** (make ticks/labels visible).

### 8) When AI cannot fix, you fix one item (AI + You, 20 pts)
- **index_legacy_2.html → index.html**
- **Legend clipping:** add **extra right margin** and **wrap long legend labels** (multi‑line `tspan`).

### 9) Ask AI to justify design choices (AI, 5 pts)
- **Why a line chart?** We analyze change over time; lines support trajectory comparison. For ranks at latest year, use bars; for relationships (LE vs. GDP), use scatter.
- **Data clarity:** state indicator (`SP.DYN.LE00.IN`) and **years**; drop NaNs; exclude aggregates; define **mean per Region–Year**.
- **Scales & axes:** linear y; integer years; titled axes; moderate tick density.
- **Color & legend:** categorical color for regions; colorblind‑safe; legend with wrapped labels.
- **Interactivity:** tooltips expose exact values; toggle shows sampling effects.
- **Missing data:** `line.defined()` avoids false bridges; omit very sparse series.
- **Clutter control:** hover highlight or small multiples.
- **Consistency:** stable y‑domain across toggles.
- **Transparency:** cite WDI; document aggregation and 20% sampling (seeded).

### 10) What did you learn through the process? Critically evaluate (You, 10 pts)
- Through this exercise I saw how a task-first mindset simplifies design choices: once the question focused on change over time, a line chart—rather than a bar or scatter—became the right fit. The biggest gains came from data hygiene (dropping NaNs, excluding aggregates, stating the exact aggregation), not from fancy code. I also learned that small presentation details (margins, external y-label, legend wrapping) directly affect readability and accessibility. Comparing the full dataset to a 20% sample showed how sampling can shift averages, so keeping a stable y-domain was essential for fair visual comparison. Finally, using AI worked best as an iterative partner: accept the scaffolding, then critique and repair weaknesses (ticks/labels, legend clipping), and document decisions for reproducibility.
---

## How to Run
1. Generate CSVs:
   ```bash
   python make_regions.py
   ```
2. Start a local server and open the page:
   ```bash
   python -m http.server 8000
   # then visit http://localhost:8000
   ```

---

## Files in this repo
- `index.html` — D3 visualization with **Full sample** / **20% sample** buttons.
- `make_regions.py` — data prep script.
- `life_expectancy_regions.csv` — output (full).
- `life_expectancy_regions_sample.csv` — output (20% panel).
- `README.md` — this document.

- what did you learn through the process? Critically evaluate 