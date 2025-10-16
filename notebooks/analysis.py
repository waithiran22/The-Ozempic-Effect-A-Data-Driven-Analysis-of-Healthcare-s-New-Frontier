# 02_analysis.ipynb

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

cms_spending = pd.read_csv("../data/processed/cms_spending.csv")
company_revenue = pd.read_csv("../data/processed/company_revenue.csv")
cdc_trends = pd.read_csv("../data/processed/diabetes_trends.csv")

# --- GLP-1 revenue share ---
glp1 = company_revenue.groupby(["Company", "Year"])["Percent_of_Total"].sum().reset_index()

plt.figure(figsize=(8,5))
sns.lineplot(data=glp1, x="Year", y="Percent_of_Total", hue="Company")
plt.title("GLP-1 Share of Total Revenue")
plt.savefig("../reports/figures/glp1_revenue_share.png", dpi=300)

# --- Medicare spending trend ---
trend = cms_spending.groupby("Year")["Tot_Spndng_USD"].sum().reset_index()

plt.figure(figsize=(8,5))
sns.lineplot(data=trend, x="Year", y="Tot_Spndng_USD")
plt.title("Medicare GLP-1 Spending Trend (2016–2023)")
plt.savefig("../reports/figures/medicare_spending_trend.png", dpi=300)

print("✅ Analysis complete. Visuals saved in /reports/figures/")
