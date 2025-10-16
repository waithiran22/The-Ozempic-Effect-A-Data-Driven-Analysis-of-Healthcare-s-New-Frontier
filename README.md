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
    
### Raw Source Files (External)

-Due to file size constraints, source PDFs for company annual reports are hosted externally.


**-Novo Nordisk Annual Reports (2017–2024)** and **Eli Lilly Annual Reports (2020–2024)**
-[Access on Google Drive](https://drive.google.com/drive/folders/1GGhzbpAqZbElwnlnxwzUF2GqQPQLjxfO?usp=drive_link
)

Each report includes product-level sales data used to extract GLP-1 revenues in `data/processed/company_revenue.csv`.

---

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

## Visual Insights

This section presents key visualizations that capture the impact of GLP-1 agonists across revenue, healthcare spending, and population health.  
All visuals are generated using Python (Plotly, Matplotlib, and Geopandas) from the processed datasets.

---

### 1. GLP-1 Revenue Share — Novo Nordisk vs Eli Lilly
This figure illustrates the growing dominance of GLP-1 products in both companies’ total revenues from 2017 to 2024, showing the shift from legacy diabetes care to obesity and metabolic health markets.

![GLP-1 Revenue Share](reports/figures/glp1_revenue_share.png)

---

### 2. Medicare Part D Spending Trend (2016 – 2023)
Aggregate Medicare Part D spending on GLP-1 drugs has surged, particularly after 2021.  
The visualization highlights both total cost and number of beneficiaries, signaling rapid adoption and budget impact.

![Medicare Spending Trend](reports/figures/medicare_spending_trend.png)

---

### 3. Diabetes Prevalence vs GLP-1 Spending
This overlay compares national diabetes prevalence (ages 18+ and 67+) with Medicare GLP-1 spending.  
It visually connects rising prevalence with increasing therapeutic demand.

![Diabetes vs GLP-1 Overlay](reports/figures/diabetes_vs_glp1_overlay.png)

---

### 4. Geographic Distribution of GLP-1 Spending
A choropleth map illustrating state-level disparities in GLP-1 adoption and spending intensity across the U.S.  

![Geographic GLP-1 Spending Map](reports/figures/geographic_spending_map.png)

**Interactive Version:**  
[View the Interactive Map](https://waithiran22.github.io/The-Ozempic-Effect-A-Data-Driven-Analysis-of-Healthcare-s-New-Frontier/geographic_spending_map.html)

---

### 5. Patent Expiry and Market Forecast Timeline
This timeline visualization combines GLP-1 patent expiry schedules (semaglutide 2026–2032; tirzepatide 2036) with projected global market growth, illustrating how exclusivity shapes long-term competition.

![Patent and Forecast Timeline](reports/figures/patent_forecast_timeline.png)

---

📊 *All generated figures are available in* [`/reports/figures/`](reports/figures/).


---

## Reproducibility
All analyses are reproducible using the included Python notebooks and datasets.  
Ensure dependencies are installed via:

```bash
pip install -r requirements.txt
```

## License
This project is licensed under the MIT License.
