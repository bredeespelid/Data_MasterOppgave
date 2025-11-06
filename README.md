
# Data_MasterOppgave


This repository contains the data, notebooks and scripts used for a master's thesis in data analysis and foreign exchange (FX) modeling. The work explores how macro and market variables relate to EUR/NOK dynamics and includes preprocessing pipelines, exploratory analysis, and experiment logs for model fine-tuning.

## Short abstract (thesis context)

The master's thesis investigates the drivers of the EUR/NOK exchange rate using historical market and macroeconomic variables. The repository stores the cleaned datasets, analysis notebooks that reproduce figures and tables from the thesis, and scripts used to generate plots and prepared inputs for modeling experiments.

If you are reviewing the thesis artifacts, the notebooks in `FineTuneData/` and `Variables/All_Variables/` are the primary entry points for experiments and combined variable datasets.

## Repository structure (detailed)

- `EURNOK/` — Raw and processed EUR/NOK datasets. Typical files:
	- `EUR_NOK_NorgesBank.csv` — exchange rate data from Norges Bank (if present).
	- `EUR_NOK.csv` — alternate/pre-processed EUR/NOK CSV.
	- `MultiFXData.csv` — multi-currency FX dataset used for cross-checks.

- `FineTuneData/` — Notebooks and logs for model experiments and fine-tuning. Open `FinetuneLog.ipynb` to inspect experiment runs and metrics.

- `Graf/` — Utility scripts for plotting and formatting figures used in the thesis. Example:
	- `Format.py` — small helper script to standardize figure style and export formats (open the file to see usage and dependencies).

- `Variables/` — constructed variables and supporting notebooks grouped by topic:
	- `All_Variables/` — combined variable tables (CSV) and notebooks that show preprocessing steps.
	- `OSEBX/`, `S&P500/`, `StoxEurope/` — folders with market/index data used as predictors or explanatory variables.

## Notebooks of interest (recommended order)

1) `Variables/All_Variables/All_Variables.ipynb` — shows how variables are assembled, feature engineering steps and exported CSVs used by models.
2) `FineTuneData/FinetuneLog.ipynb` — experiment logs, model metrics and hyperparameter notes.
3) Any visualization notebooks in `Graf/` or `Variables/` to reproduce plots for the thesis.

## Data provenance and citation

- Wherever external data is used (e.g. Norges Bank, market data), the notebook that imports the file should contain the source and date of download. If you add external sources, include a small metadata file (e.g. `EURNOK/README.md`) describing the source and license.
- If you reuse these datasets in publications, please cite the thesis or contact the author for a recommended citation.

## Reproduce the analysis (local)

1) Create and activate a Python virtual environment (PowerShell):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2) Install dependencies:

```powershell
pip install --upgrade pip
pip install -r requirements.txt
```

3) Start Jupyter and run notebooks in the recommended order (see 'Notebooks of interest'):

```powershell
jupyter lab
```

4) Run scripts (examples):

```powershell
python Graf\Format.py
```

Notes:
- Many notebooks read CSV files directly from the folders above; ensure the relative paths are preserved when running from the repository root.
- If a notebook requires additional packages, add them to `requirements.txt` or install locally.

## Data format and shapes

- Most dataset CSVs contain a date column (ISO format) and one or more numeric columns.
- Typical shapes are daily or monthly time series; check the individual CSVs for exact columns.

## Development contract (brief)

- Inputs: CSV files in `EURNOK/`, `Variables/` and scripts/notebooks in their respective folders.
- Outputs: cleaned CSVs (in `Variables/All_Variables/`), figures (exported by `Graf/` scripts), and experiment logs (`FineTuneData/`).
- Success criteria: notebooks run without error from the repository root after installing `requirements.txt`.

## Contributing

- Use issues for questions, dataset corrections, or reproducibility problems.
- For code changes: create a branch, run tests (if added), and open a pull request with a short description.

## License

This work is released under the MIT License — see the `LICENSE` file in the repository root.

## Contact / authorship

If you want author name, affiliation or an email added here (for citation/contact), tell me what to include and I will add it.

---

If you'd like I can also:
- expand the dataset descriptions with column-level details for the main CSVs,
- add an example notebook that runs the full preprocessing pipeline end-to-end,
- pin exact package versions in `requirements.txt` by scanning the notebooks.

