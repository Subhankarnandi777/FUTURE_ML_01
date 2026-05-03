import pandas as pd

# Load Historical Data
historical = pd.read_csv("data/processed/cleaned_data.csv")

# Load Forecast Data
forecast = pd.read_csv("data/processed/forecast_output.csv")

# Prepare Historical Format
historical_chart = historical[["date", "sales"]].copy()
historical_chart["type"] = "Historical"

# Prepare Forecast Format
forecast_chart = forecast[["date", "predicted_sales"]].copy()
forecast_chart.columns = ["date", "sales"]
forecast_chart["type"] = "Forecast"

# Combine Both
combined = pd.concat([historical_chart, forecast_chart])

# Save For Power BI
combined.to_csv(
    "data/processed/powerbi_forecast_compare.csv",
    index=False
)

print("powerbi_forecast_compare.csv created successfully.")