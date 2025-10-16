# 03_forecasting_modeling.ipynb

import pandas as pd
from prophet import Prophet
import matplotlib.pyplot as plt

cms_spending = pd.read_csv("../data/processed/cms_spending.csv")

# Prepare data for Prophet
df = cms_spending.groupby("Year")["Tot_Spndng_USD"].sum().reset_index()
df.rename(columns={"Year": "ds", "Tot_Spndng_USD": "y"}, inplace=True)

model = Prophet(yearly_seasonality=False)
model.fit(df)

future = model.make_future_dataframe(periods=7, freq="Y")
forecast = model.predict(future)

# Plot
fig = model.plot(forecast)
plt.title("Forecast: Medicare GLP-1 Spending to 2030")
plt.savefig("../reports/figures/forecast_spending_to_2030.png", dpi=300)

forecast.to_csv("../data/processed/spending_forecast_2030.csv", index=False)
print("✅ Forecasting complete. Results saved.")
