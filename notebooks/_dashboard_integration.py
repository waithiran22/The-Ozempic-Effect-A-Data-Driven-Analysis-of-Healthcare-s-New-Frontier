# 05_dashboard_integration.ipynb

import pandas as pd
import json

# Create summarized data for dashboard
cms = pd.read_csv("../data/processed/cms_spending.csv")
revenue = pd.read_csv("../data/processed/company_revenue.csv")

summary = {
    "cms_total_spending": cms["Tot_Spndng_USD"].sum(),
    "novo_glp1_share": revenue[revenue["Company"]=="Novo Nordisk"]["Percent_of_Total"].mean(),
    "lilly_glp1_share": revenue[revenue["Company"]=="Eli Lilly"]["Percent_of_Total"].mean()
}

with open("../dashboard/dashboard_summary.json", "w") as f:
    json.dump(summary, f, indent=2)

print("✅ Dashboard integration data ready.")
