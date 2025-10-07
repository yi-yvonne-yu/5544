import pandas as pd

# Input files (raw WDI)
WDICSV = "data/WDI_CSV_2025_07_02/WDICSV.csv"
COUNTRIES = "data/WDI_CSV_2025_07_02/WDICountry.csv"

# Life expectancy indicator: Life expectancy at birth, total (years)
INDICATOR = "SP.DYN.LE00.IN"

# Load data
wdic = pd.read_csv(WDICSV)
countries = pd.read_csv(COUNTRIES)[["Country Code", "Region"]]

# Keep only life expectancy rows
life = wdic[wdic["Indicator Code"] == INDICATOR].copy()

# Attach Region; drop aggregates (Region is empty for aggregates)
life = life.merge(countries, left_on="Country Code", right_on="Country Code", how="left")
life = life[life["Region"].notna()]

# Melt year columns to long format
year_cols = [c for c in life.columns if c.isdigit()]
life_long = life.melt(
    id_vars=["Country Name", "Country Code", "Region"],
    value_vars=year_cols,
    var_name="Year",
    value_name="LifeExpectancy"
)
life_long["Year"] = life_long["Year"].astype(int)
life_long["LifeExpectancy"] = pd.to_numeric(life_long["LifeExpectancy"], errors="coerce")

# Aggregate to regional mean per year
region_year = (
    life_long
    .groupby(["Region", "Year"], as_index=False)["LifeExpectancy"]
    .mean()
)

# Save
region_year.to_csv("data/life_expectancy_regions_legacy.csv", index=False)
print("Wrote data/life_expectancy_regions_legacy.csv with", len(region_year), "rows.")
