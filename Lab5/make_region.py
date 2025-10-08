# make_regions.py
import pandas as pd
import numpy as np
from pathlib import Path

WDICSV = "data/WDI_CSV_2025_07_02/WDICSV.csv"
COUNTRIES = "data/WDI_CSV_2025_07_02/WDICountry.csv"
INDICATOR = "SP.DYN.LE00.IN"   # Life expectancy at birth, total (years)
SAMPLE_RATE = 0.20
SEED = 42

ROWS_FULL_CSV   = "data/life_expectancy_rows_full.csv"
ROWS_SAMPLE_CSV = "data/life_expectancy_rows_sample.csv"

REGIONS_FULL_CSV   = "data/life_expectancy_regions.csv"
REGIONS_SAMPLE_CSV = "data/life_expectancy_regions_sample.csv"

def sample_group_20pct(g, rate=SAMPLE_RATE, seed=SEED):
    n = len(g)
    if n <= 0:
        return g.iloc[0:0]
    k = max(1, int(n * rate))
    return g.sample(n=k, replace=False, random_state=seed)

def main():
    Path("data").mkdir(parents=True, exist_ok=True)

    wdic = pd.read_csv(WDICSV)
    countries = pd.read_csv(COUNTRIES)[["Country Code", "Region"]]

    life = (
        wdic[wdic["Indicator Code"] == INDICATOR]
        .merge(countries, on="Country Code", how="left")
    )

    life = life[life["Region"].notna()]

    year_cols = [c for c in life.columns if c.isdigit()]
    life_long = life.melt(
        id_vars=["Country Name", "Country Code", "Region"],
        value_vars=year_cols,
        var_name="Year",
        value_name="LifeExpectancy",
    )

    life_long["LifeExpectancy"] = pd.to_numeric(life_long["LifeExpectancy"], errors="coerce")
    life_long["Year"] = life_long["Year"].astype(int)
    life_long = life_long.replace([np.inf, -np.inf], np.nan).dropna(subset=["LifeExpectancy"])

    life_long.to_csv(ROWS_FULL_CSV, index=False)

    sampled_rows = (
        life_long
        .groupby(["Region", "Year"], group_keys=False)
        .apply(sample_group_20pct)
        .reset_index(drop=True)
    )
    sampled_rows.to_csv(ROWS_SAMPLE_CSV, index=False)

    region_year_full = (
        life_long
        .groupby(["Region", "Year"], as_index=False)["LifeExpectancy"]
        .mean()
        .rename(columns={"LifeExpectancy": "LifeExpectancyMean"})
    )
    region_year_full.to_csv(REGIONS_FULL_CSV, index=False)

    region_year_sample = (
        sampled_rows
        .groupby(["Region", "Year"], as_index=False)["LifeExpectancy"]
        .mean()
        .rename(columns={"LifeExpectancy": "LifeExpectancyMean"})
    )
    region_year_sample.to_csv(REGIONS_SAMPLE_CSV, index=False)

    print(f"Wrote rows (FULL)   → {ROWS_FULL_CSV}   rows={len(life_long)}")
    print(f"Wrote rows (SAMPLE) → {ROWS_SAMPLE_CSV} rows={len(sampled_rows)}  (rate={SAMPLE_RATE}, seed={SEED})")

    print(f"Wrote REGIONS (FULL)   → {REGIONS_FULL_CSV}   rows={len(region_year_full)}, "
          f"regions={region_year_full['Region'].nunique()}, years={region_year_full['Year'].nunique()}")
    print(f"Wrote REGIONS (SAMPLE) → {REGIONS_SAMPLE_CSV} rows={len(region_year_sample)}, "
          f"regions={region_year_sample['Region'].nunique()}, years={region_year_sample['Year'].nunique()}")

    full_keys   = set(map(tuple, region_year_full[["Region","Year"]].to_numpy()))
    sample_keys = set(map(tuple, region_year_sample[["Region","Year"]].to_numpy()))
    if full_keys != sample_keys:
        print("WARNING: Region×Year coverage mismatch:")
        print("  missing_in_sample:", len(full_keys - sample_keys))
        print("  missing_in_full  :", len(sample_keys - full_keys))

if __name__ == "__main__":
    main()
