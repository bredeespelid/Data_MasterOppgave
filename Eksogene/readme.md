# Exogenous-Log Data Pipeline (EUR/NOK, HICP, Policy Rates & Markets)

Reproducible Python workflow that builds **daily** and **monthly** panels for:
- EUR/NOK spot (Norges Bank)
- Real exchange rate \( Q_t = \log(EUR/NOK) - (\log p_t - \log p_t^\*) \)
- Inflation differential \( d\pi_t \) and policy rate differential \( dI_t \)
- Market factors (exogenous): **Brent**, **VIX**, **STOXX Europe 600**, **S&P 500**
- **Log-transformed version** of exogenous factors: `final_with_rates_log.csv`

> **Primary outputs**
>
> - `final_with_rates.csv` — daily panel on original scales  
> - `final_with_rates_log.csv` — same panel, but **exogenous** columns log-transformed  
> - `final_dataset_monthly.csv` — monthly aggregation (optional)

---

## Data Sources

- **Eurostat HICP (monthly)** — compressed SDMX TSV  
  `https://ec.europa.eu/eurostat/api/dissemination/sdmx/2.1/data/prc_hicp_midx?format=TSV&compressed=true`  
  - Norway **core** HICP: `geo=NO, coicop=TOT_X_NRG_FOOD`  
  - Euro area **headline** HICP: `geo=EA, coicop=CP00`  
  - Unit is auto-selected with preference `I15`, `I05`, `I96` (falls back to first available)
- **Norges Bank (FX)** — EUR/NOK daily (CSV, semicolon & comma decimals)
- **Norges Bank (Policy rate)** — official key policy rate (CSV)
- **ECB (Policy rates)** — scraped “Key ECB interest rates”; **Deposit Facility** used as EU policy rate
- **FRED (VIX)** — `VIXCLS`, daily CSV export (handles `.` as missing)
- **USDA / Socrata (Brent)** — CSV API (requires `X-App-Token`)
- **STOXX Europe 600** — CSV in repo (`StoxxEuro600.csv`)
- **S&P 500** — CSV in repo (`S%26P.csv`)

All series are aligned to a **daily** index by forward-fill; monthly panels are derived by resampling.

---

## What the Script Does (High-Level)

1. **Load & Clean HICP (Eurostat, monthly):**
   - Parse composite dimension column into `freq, unit, coicop, geo`.
   - Melt time columns (`YYYY-MM`), clean flags, cast to float.
   - Build continuous monthly index from **1999-12** to **2025-12** and forward-fill gaps.
   - Compute logs for HICP series; retain both level and log columns.

2. **FX (Norges Bank, daily):**
   - Read EUR/NOK, standardize to daily frequency, forward-fill.

3. **Map HICP to Daily and Build Core Variables:**
   - Expand monthly HICP to daily (FFILL).
   - Compute
     - \( s_t = \log(EUR/NOK) \)
     - \( p_t = \log(\text{NO core HICP}) \), \( p_t^\* = \log(\text{EA HICP}) \)
     - \( q_t = s_t - (p_t - p_t^\*) \)

4. **Inflation Differential \( d\pi_t \):**
   - Take **month-end** levels, then compute monthly \( \Delta\log \).
   - Map each month’s value back to **all days within the same month** via back-fill from month-end.

5. **Policy Rates & Differential \( dI_t \):**
   - Norges Bank: daily series via FFILL/ BFILL across full calendar.
   - ECB: scrape table, build daily **Deposit Facility** series via FFILL/ BFILL.
   - Align to target index and compute \( dI_t = i_t - i_t^\* \).

6. **Market Factors (Exogenous):**
   - **VIX** (FRED): daily → FFILL/ BFILL.
   - **Brent** (USDA): query by date range, daily → FFILL.
   - **STOXX 600** and **S&P 500**: parse, convert to **business-day** indices, FFILL, align by date.

7. **Final Joins & Exports:**
   - Join all series into `final_with_rates` with ordered columns.
   - **Create log-transformed copy** `final_with_rates_log`:
     - Log only on **positive** exogenous columns among `["brent","VIX","StoxEurope","SP500"]`.
   - Export:
     - `final_with_rates.csv`
     - `final_with_rates_log.csv`
     - `final_dataset_monthly.csv` (optional)

---

## Columns

### Daily (`final_with_rates.csv`)
| Column        | Definition |
|---|---|
| `EUR_NOK`     | EUR/NOK spot (NB), daily, ffilled |
| `Q`           | Real exchange rate \( \log(EUR/NOK) - (\log p_t - \log p_t^\*) \) |
| `d_pi`        | Inflation differential \( \Delta\log p_t - \Delta\log p_t^\* \) (same-month mapping) |
| `dI_t`        | Policy rate differential \( i_t - i_t^\* \) (NB – ECB Deposit Facility) |
| `brent`       | Brent crude (daily, ffilled) |
| `VIX`         | VIX index (daily, ffilled) |
| `StoxEurope`  | STOXX Europe 600 (business days; aligned & ffilled) |
| `SP500`       | S&P 500 (business days; aligned & ffilled) |

### Daily (`final_with_rates_log.csv`)
- Same columns as above, **but with**:
  - `brent`, `VIX`, `StoxEurope`, `SP500` **log-transformed** where values > 0.
  - Endogenous core variables (`EUR_NOK`, `Q`, `d_pi`, `dI_t`) remain on original scale.

### Monthly (`final_dataset_monthly.csv`)
- `EUR_NOK`: monthly **mean**
- `Q`, `d_pi`, `dI_t`: **last** (month-end)

---

## Requirements

- Python ≥ 3.10
- `pandas`, `numpy`, `requests`, `beautifulsoup4`, `lxml`

Optional (for Brent API):
- Environment variable `USDA_APP_TOKEN` (or hardcode header in the script)

---

## Quick Start

```bash
# 1) Environment
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -U pandas numpy requests beautifulsoup4 lxml

# 2) (Optional) Socrata token for Brent
export USDA_APP_TOKEN="YOUR_APP_TOKEN"   # Windows: set USDA_APP_TOKEN=YOUR_APP_TOKEN

# 3) Run (execute the notebook or converted .py)
python Eksogene_Log.py  # or run cells in Colab/Jupyter

# 4) Outputs
ls -1 final_with_rates.csv final_with_rates_log.csv  # daily panels
# optional:
# final_dataset_monthly.csv
