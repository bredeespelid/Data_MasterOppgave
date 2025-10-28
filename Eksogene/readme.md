# Exogenous Data Pipeline for NOK/EUR, HICP, Policy Rates & Market Factors

Reproducible Python workflow to fetch, clean, align, and export **daily** and **monthly** datasets for:
- EUR/NOK spot (Norges Bank)
- Real exchange rate \( Q_t = s_t - (p_t - p_t^\*) \)
- Inflation and interest differentials \( d\pi_t, \; dI_t \)
- Market factors: VIX, Brent, STOXX Europe 600, and S&P 500

> **Primary output:** `final_with_rates.csv` (daily)

---

## Contents

- `final_with_rates.csv` — Daily panel: `EUR_NOK, Q, d_pi, dI_t, brent, VIX, StoxEurope, SP500`
- (Optional) intermediate exports:
  - `merged_q_inflasjon_ready.csv`, `eurnok_Q_dpi_ready.csv`, `final_dataset_ready.csv`
- (Optional) monthly aggregation:
  - `final_dataset_monthly.csv`

---

## Data Sources

- **Eurostat (HICP)** — compressed SDMX TSV:
  - Endpoint: `https://ec.europa.eu/eurostat/api/dissemination/sdmx/2.1/data/prc_hicp_midx?format=TSV&compressed=true`
  - Series used:
    - Norway core HICP: `geo=NO, coicop=TOT_X_NRG_FOOD`
    - Euro area headline HICP: `geo=EA, coicop=CP00`
- **Norges Bank (FX)** — EUR/NOK daily:
  - `https://data.norges-bank.no/api/data/EXR/B.EUR.NOK.SP?...`
- **Norges Bank (Policy rate)**:
  - `https://data.norges-bank.no/api/data/IR/B.KPRA.SD.R?...`
- **ECB (Policy rates)** — scraped “Key ECB interest rates”; deposit facility used as EU policy rate:
  - `https://www.ecb.europa.eu/stats/policy_and_exchange_rates/key_ecb_interest_rates/html/index.en.html`
- **VIX (FRED)**:
  - CSV export for `VIXCLS`
- **Brent (USDA, Socrata)**:
  - `https://agtransport.usda.gov/api/v3/views/b3w8-gxpm/query.csv` (requires X-App-Token)
- **STOXX Europe 600**:
  - CSV hosted in repo: `StoxxEuro600.csv`
- **S&P 500**:
  - CSV hosted in repo: `S%26P.csv`

> All series are reindexed and forward-filled to a common **daily** calendar; monthly views are derived via resampling.

---

## Variables (Daily)

| Column        | Description                                                                 |
|---------------|------------------------------------------------------------------------------|
| `EUR_NOK`     | EUR/NOK spot (Norges Bank), forward-filled to daily calendar                |
| `Q`           | Real exchange rate \( Q_t = \log(EUR/NOK) - (\log p_t - \log p_t^\*) \)     |
| `d_pi`        | Inflation differential \( \Delta\log p_t - \Delta\log p_t^\* \), mapped daily to same-month value |
| `dI_t`        | Policy rate differential \( i_t - i_t^\* \) (NB vs ECB deposit facility)    |
| `brent`       | Brent crude (daily; forward-filled)                                         |
| `VIX`         | VIX index (daily; forward-filled)                                           |
| `StoxEurope`  | STOXX Europe 600 (business days; aligned & forward-filled)                  |
| `SP500`       | S&P 500 (business days; aligned & forward-filled)                           |

**HICP notes**
- Norway: core (ex energy & food) `TOT_X_NRG_FOOD`
- EA: headline `CP00`
- Units are auto-selected with preference `I15, I05, I96` (falls back to first available)

---

## Quick Start

```bash
# 1) Python & dependencies
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -U pandas numpy requests beautifulsoup4 lxml

# 2) (Recommended) set Socrata token for Brent
export USDA_APP_TOKEN="YOUR_APP_TOKEN"  # Windows: set USDA_APP_TOKEN=YOUR_APP_TOKEN

# 3) Run the script/notebook (convert .ipynb to .py if needed)
python DataEksogene.py  # or run cells in your notebook environment

# 4) Outputs
ls -1 final_with_rates.csv  # daily
# optional:
# final_dataset_monthly.csv

