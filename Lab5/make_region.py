# make_regions.py
import pandas as pd
import numpy as np

def sample_20pct(g):
    n = max(1, int(len(g) * 0.20))   # at least 1
    return g.sample(n=n, replace=False, random_state=42)

WDICSV = "data/WDI_CSV_2025_07_02/WDICSV.csv"
COUNTRIES = "data/WDI_CSV_2025_07_02/WDICountry.csv"
INDICATOR = "SP.DYN.LE00.IN"  # Life expectancy at birth, total (years)

# Load
wdic = pd.read_csv(WDICSV)
countries = pd.read_csv(COUNTRIES)[["Country Code", "Region"]]

# Filter to life-expectancy rows and attach Region
life = (
    wdic[wdic["Indicator Code"] == INDICATOR]
    .merge(countries, on="Country Code", how="left")
)

# Keep only rows with a real Region (drop aggregates like "World")
life = life[life["Region"].notna()]

# Melt year columns
year_cols = [c for c in life.columns if c.isdigit()]
life_long = life.melt(
    id_vars=["Country Name", "Country Code", "Region"],
    value_vars=year_cols,
    var_name="Year",
    value_name="LifeExpectancy",
)

# Coerce to numeric and **drop null/NaN/non-finite** values
life_long["LifeExpectancy"] = pd.to_numeric(life_long["LifeExpectancy"], errors="coerce")
life_long["Year"] = life_long["Year"].astype(int)
life_long = life_long.replace([np.inf, -np.inf], np.nan).dropna(subset=["LifeExpectancy"])

# Aggregate: mean life expectancy per Region-Year (only over valid values)
# region_year = (
#     life_long.groupby(["Region", "Year"], as_index=False)["LifeExpectancy"]
#     .mean()
# )

sampled = (life_long
           .groupby(["Region", "Year"], group_keys=False)
           .apply(sample_20pct))

region_year = (sampled
                  .groupby(["Region", "Year"], as_index=False)["LifeExpectancy"]
                  .mean())

# Save
# region_year.to_csv("life_expectancy_regions.csv", index=False)
region_year.to_csv("data/life_expectancy_regions_sample.csv", index=False)
# print(f"Wrote life_expectancy_regions.csv with {len(region_year)} rows "
print(f"Wrote data/life_expectancy_regions_sample.csv with {len(region_year)} rows "
      f"across {region_year['Region'].nunique()} regions and "
      f"{region_year['Year'].nunique()} years.")
