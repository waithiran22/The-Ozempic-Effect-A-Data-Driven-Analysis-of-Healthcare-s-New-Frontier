# 04_visualizations.ipynb

import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

# --- Overlay: Diabetes vs Spending ---
cdc = pd.read_csv("../data/processed/diabetes_trends.csv")
cms = pd.read_csv("../data/processed/cms_spending.csv")

merged = pd.merge(cdc, cms, on="Year", how="inner")
plt.figure(figsize=(8,5))
plt.plot(merged["Year"], merged["Adults_18+_%"], label="Diabetes Prevalence (18+)")
plt.plot(merged["Year"], merged["Tot_Spndng_USD"]/1e9, label="Medicare GLP-1 Spending (Billion USD)")
plt.legend()
plt.title("Diabetes Prevalence vs GLP-1 Spending")
plt.savefig("../reports/figures/diabetes_vs_glp1_overlay.png", dpi=300)

# --- Choropleth ---
state_map = pd.read_csv("../data/processed/state_demand_pressure.csv")
fig = px.choropleth(state_map, locations="State", locationmode="USA-states",
                    color="Demand_Index", scope="usa",
                    title="Geographic GLP-1 Demand Pressure")
fig.write_html("../reports/figures/geographic_spending_map.html")
fig.write_image("../reports/figures/geographic_spending_map.png")
print("✅ Visualization complete.")
