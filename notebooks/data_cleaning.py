# 01_data_cleaning.ipynb

# Imports
import pandas as pd
import numpy as np

# --- Load datasets ---
cms_spending = pd.read_csv("../data/raw/Medicare Part D Drug Spending Dashboard (2016–2023).csv")
frf = pd.read_excel("../data/raw/CMS Formulary Reference File (FRF).xlsx")
cdc_younger = pd.read_csv("../data/raw/CDC,Younger.csv")
cdc_older = pd.read_csv("../data/raw/CDC,Older.csv")
company_revenue = pd.read_csv("../data/processed/company_revenue.csv")

# --- Clean and normalize ---
cms_spending.columns = cms_spending.columns.str.strip()
cdc_younger.rename(columns={"Total - Percentage": "Adults_18+_%"}, inplace=True)
cdc_older.rename(columns={"Total - Number in 1000s": "Seniors_67+_000s"}, inplace=True)

# --- Merge CDC data ---
cdc_trends = pd.merge(cdc_younger, cdc_older, on="Year", how="outer")
cdc_trends.to_csv("../data/processed/diabetes_trends.csv", index=False)

print("✅ Data cleaning complete. Processed files saved in /data/processed/")
