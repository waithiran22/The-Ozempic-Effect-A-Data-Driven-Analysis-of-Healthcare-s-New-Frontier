
import pandas as pd, os
cdc_state_path = os.getenv("CDC_STATE_PATH", "/mnt/data/data/templates/cdc_state_prevalence_template.csv")
medicare_state_path = os.getenv("MEDICARE_STATE_PATH", "/mnt/data/data/templates/medicare_enrollment_by_state_template.csv")
out_path = "/mnt/data/data/processed/state_demand_pressure.csv"
os.makedirs(os.path.dirname(out_path), exist_ok=True)
cdc = pd.read_csv(cdc_state_path); med = pd.read_csv(medicare_state_path)
cdc["State"]=cdc["State"].str.strip(); med["State"]=med["State"].str.strip()
df = cdc.merge(med, on=["State","Year"], how="inner")
for col in ["Adults_18plus_pct","Medicare_Enrollment"]:
    mu = df[col].mean(); sd = df[col].std() if df[col].std()!=0 else 1.0
    df[col+"_z"] = (df[col]-mu)/sd
df["demand_pressure_index"] = 0.5*df["Adults_18plus_pct_z"] + 0.5*df["Medicare_Enrollment_z"]
df = df[["State","Year","Adults_18plus_pct","Medicare_Enrollment","demand_pressure_index"]].sort_values(["Year","State"])
df.to_csv(out_path, index=False)
print("Saved:", out_path)
