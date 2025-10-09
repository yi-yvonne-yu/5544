
# Life Expectancy by Region — Assignment README

## How to Run
1. Prepare data:
   Download files from https://datacatalog.worldbank.org/search/dataset/0037712/World-Development-Indicators, then run:
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
- `index.html` — D3 visualization with **Full sample** / **20% sample**/ **Overlay**/ **Difference** buttons.
- `make_regions.py` — data prep script.
- `data/life_expectancy_rows_full.csv` — row-level, cleaned Country×Year records (13,854 rows).
- `data/life_expectancy_rows_sample.csv` — row-level, sampled (~20% per Region×Year, seed=42) (2,624 rows).
- `data/life_expectancy_regions.csv` — aggregated Full: mean life expectancy per Region×Year.
- `data/life_expectancy_regions_sample.csv` — aggregated Sample: mean life expectancy per Region×Year.
-  `gpt_chat_history.webarchive` - chat history with gpt.
- `README.md` — this document.
