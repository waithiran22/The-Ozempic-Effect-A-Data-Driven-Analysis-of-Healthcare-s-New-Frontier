# The Ozempic Effect: A Data-Driven Analysis of Healthcare's New Frontier

## Overview
This project investigates the disruption caused by GLP-1 agonists (Ozempic, Wegovy, Rybelsus, Trulicity, Mounjaro, and Zepbound) across healthcare, economics, and consumer behavior. It quantifies the impact of these drugs on pharmaceutical revenues, Medicare Part D spending, diabetes prevalence, and the future outlook of obesity care.

This repository contains the full analytical workflow, cleaned datasets, code, and visualizations necessary to reproduce the analysis.

---

## Project Objectives
1. Quantify how much of Novo Nordisk and Eli Lilly’s revenue depends on GLP-1 drugs.
2. Measure Medicare Part D’s cost burden for GLP-1s.
3. Track diabetes prevalence among U.S. adults and seniors.
4. Forecast future spending, revenue, and market expansion through 2030.
5. Evaluate potential healthcare cost offsets from GLP-1 adoption.

---

## Datasets Used

### Company Financials
- **Novo Nordisk Annual Reports (2017–2024)** – PDF  
- **Eli Lilly Annual Reports (2020–2024)** – PDF  
  - Extracted from “Sales by product,” “Revenue by product,” or “Performance highlights.”
  - Output: `company_revenue.csv`
  - Columns: `Year | Company | Product | Revenue_DKK_million | Total_Company_Revenue | Percent_of_Total`

### Healthcare Spending (CMS)
- **Medicare Part D Drug Spending Dashboard (2016–2023)** – CSV  
- **CMS Formulary Reference File (FRF)** – XLSX  
  - Used for drug mapping and name normalization.
  - Output: `cms_spending.csv`, `cms_frf.csv`

### Population Health (CDC)
- **CDC Diabetes Prevalence (Adults 18+)** – `CDC_Younger.csv`  
- **CDC Diabetes Prevalence (Seniors 67+)** – `CDC_Older.csv`  
  - Combined into a unified dataset for national trends.
  - Output: `diabetes_trends.csv`

### Market and Industry Outlook
- **Patent Expiry Data** – `patent_expiry.csv`  
- **Market Forecasts (IQVIA/Allianz estimates)** – `market_forecasts.csv`

### Regulatory Data
- **FDA Approvals Timeline** – `fda_approvals.csv`  
- **FDA Drug Shortages** – `fda_shortages.csv`

### Economic and Consumer Insights
- **RAND/OECD/Finkelstein Cost Studies** – `obesity_costs_refs.csv`  
- **KFF/Ipsos Consumer Surveys** – `consumer_surveys.csv`

---

## Tools and Technologies

**Data Processing and Analysis**
- Python (Pandas, NumPy)
- SQL (for CMS data)
- Prophet or Statsmodels (for forecasting)

**Visualization**
- Plotly and Matplotlib (core analysis)
- Geopandas and Plotly (geographic insights)
- R Shiny (optional dashboard interactivity)

**Documentation and Collaboration**
- GitHub for version control and publication
- PDFPlumber or Tabula for PDF table extraction

---

## Workflow

### Step 1: Data Preparation
- Extract product-level revenues from annual reports.
- Clean and normalize Medicare Part D spending data.
- Match drug names using the Formulary Reference File.
- Merge CDC diabetes prevalence datasets.
- Export all cleaned datasets to `data/processed/`.

### Step 2: Core Analysis
- Calculate GLP-1 share of company revenue.
- Trend Medicare spending per beneficiary and per dosage unit.
- Overlay CDC diabetes trends with Medicare spending growth.

### Step 3: Extended Analysis
- Geographic insights: visualize GLP-1 spending vs diabetes prevalence by state.
- Predictive modeling: project spending and revenue to 2030.
- Health outcomes modeling: estimate potential obesity cost offsets.

### Step 4: Visualization
- Revenue share and product trends (Novo vs Lilly).
- Medicare spending and top GLP-1 drugs.
- Diabetes prevalence (18+ vs 67+).
- Patent expiry and market forecast timelines.
- Cost offsets: healthcare savings waterfall chart.

### Step 5: Deliverables
- Clean datasets (`data/processed/`)
- Interactive visualizations (`reports/figures/`)
- Forecast and regression notebooks (`notebooks/`)
- Final policy and industry report (`reports/ozempic_effect.pdf`)
- Optional dashboard app (`dashboard/`)

---

## Outputs
1. `company_revenue.csv` – Product-level revenues for Novo & Lilly.
2. `cms_spending.csv` – Medicare Part D spending per drug.
3. `cms_frf.csv` – Formulary reference mappings.
4. `diabetes_trends.csv` – National diabetes prevalence.
5. `market_forecasts.csv`, `patent_expiry.csv` – Long-term projections.
6. Visualizations and forecasts in `/reports/figures/`.
7. Interactive dashboard.
8. Final written report summarizing insights.

---

## Key Questions Answered
1. What percentage of Novo Nordisk and Eli Lilly’s revenue comes from GLP-1 drugs?
2. How has Medicare’s GLP-1 spending evolved from 2016 to 2023?
3. What is the relationship between diabetes prevalence and GLP-1 spending?
4. When will key patents expire, and how will that shift the market?
5. What are the future cost implications and savings potential for healthcare systems?

---

## Example Visualizations
- GLP-1 revenue share over time
- Medicare spending vs beneficiaries (line & bar)
- Diabetes prevalence vs GLP-1 usage (overlay chart)
- Patent expiry timeline (horizontal bar)
- Forecasted market size to 2030 (line projection)
- Healthcare cost offset waterfall chart

---

## Reproducibility
All analyses are reproducible using the included Python notebooks and datasets.  
Ensure dependencies are installed via:

```bash
pip install -r requirements.txt
```

## License
This project is licensed under the MIT License.
