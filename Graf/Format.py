# ----------------------------
# 0) Imports og syntetiske data
# ----------------------------
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, mean_absolute_error

# Tidsakse og datasett
np.random.seed(42)
x = np.linspace(0, 10, 200)
actuals = np.sin(x)                    # Faktiske verdier (sann funksjon)
forecasts = np.sin(x) + np.random.normal(0, 0.1, len(x))  # Prognoser med støy

# ----------------------------
# 6) Evaluer ytelse
# ----------------------------
rmse = np.sqrt(mean_squared_error(actuals, forecasts))
mae = mean_absolute_error(actuals, forecasts)

# Retningsnøyaktighet (opp/ned-bevegelse)
actual_diff = np.sign(np.diff(actuals))
pred_diff = np.sign(np.diff(forecasts))
directional_accuracy = np.mean(actual_diff == pred_diff) * 100

print("\n=== Model performance (synthetic sinus data) ===")
print(f"Antall observasjoner brukt: {len(actuals)}")
print(f"RMSE: {rmse:.4f}")
print(f"MAE: {mae:.4f}")
print(f"Directional accuracy: {directional_accuracy:.1f}%")

# ----------------------------
# 7) Plot actual vs predicted (sinus)
# ----------------------------
plt.figure(figsize=(10,6))
plt.plot(x, actuals, color="black", label="Actual (sin(x))")
plt.plot(x, forecasts, color="tab:blue", linestyle="--", label="Forecast (noisy)")
plt.title("Model Forecast vs Actual (Synthetic Sinus)")
plt.xlabel("x")
plt.ylabel("Value")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()

# Save the figure
plt.savefig("Sinus_Model.png", dpi=300, bbox_inches="tight")

# Show the plot
plt.show()
# ----------------------------
# 0) Imports og syntetiske data
# ----------------------------
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, mean_absolute_error

# Tidsakse og datasett
np.random.seed(42)
x = np.linspace(0, 10, 200)
actuals = np.sin(x)                    # Faktiske verdier (sann funksjon)
forecasts = np.sin(x) + np.random.normal(0, 0.1, len(x))  # Prognoser med støy

# ----------------------------
# 6) Evaluer ytelse
# ----------------------------
rmse = np.sqrt(mean_squared_error(actuals, forecasts))
mae = mean_absolute_error(actuals, forecasts)

# Retningsnøyaktighet (opp/ned-bevegelse)
actual_diff = np.sign(np.diff(actuals))
pred_diff = np.sign(np.diff(forecasts))
directional_accuracy = np.mean(actual_diff == pred_diff) * 100

print("\n=== Model performance (synthetic sinus data) ===")
print(f"Antall observasjoner brukt: {len(actuals)}")
print(f"RMSE: {rmse:.4f}")
print(f"MAE: {mae:.4f}")
print(f"Directional accuracy: {directional_accuracy:.1f}%")

# ----------------------------
# 7) Plot actual vs predicted (sinus)
# ----------------------------
plt.figure(figsize=(10,6))
plt.plot(x, actuals, color="black", label="Actual (sin(x))")
plt.plot(x, forecasts, color="tab:blue", linestyle="--", label="Forecast (noisy)")
plt.title("Model Forecast vs Actual (Synthetic Sinus)")
plt.xlabel("x")
plt.ylabel("Value")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()

# Save the figure
plt.savefig("Sinus_Model.png", dpi=300, bbox_inches="tight")

# Show the plot
plt.show()
