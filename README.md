# Data_MasterOppgave

This repository contains datasets and notebooks used in a master’s thesis on EUR/NOK exchange rate modelling. It includes harmonised variable panels, supporting market and macro inputs, and multi currency datasets used for robustness checks and model fine tuning.

## Key files (start here)

### Harmonised variable panels (main modelling inputs)
- Daily panel (2000–2025): `Variables/All_Variables/variables_daily.csv`  
  https://github.com/bredeespelid/Data_MasterOppgave/blob/main/Variables/All_Variables/variables_daily.csv

- Monthly panel (2000–2025): `Variables/All_Variables/variables_monthly.csv`  
  https://github.com/bredeespelid/Data_MasterOppgave/blob/main/Variables/All_Variables/variables_monthly.csv

- Data generation notebook (builds the panels above): `Variables/All_Variables/All_Variables.ipynb`  
  https://github.com/bredeespelid/Data_MasterOppgave/blob/main/Variables/All_Variables/All_Variables.ipynb

### Multi currency datasets (robustness and fine tuning)
- 1980–1999 multi FX robustness dataset: `FineTuneData/NB1980-1999.csv`  
  https://github.com/bredeespelid/Data_MasterOppgave/blob/main/FineTuneData/NB1980-1999.csv

- 2000–2025 multi FX dataset: `EURNOK/MultiFXData.csv`  
  https://github.com/bredeespelid/Data_MasterOppgave/blob/main/EURNOK/MultiFXData.csv
