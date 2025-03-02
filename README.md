# Financial-Analysis-Lead-Generation-Optimization-for-Health-Care-Company
This project is designed to analyze financial trends related to patient responsibility and optimize lead generation at Health Care Provider company. It involves data cleaning, exploratory data analysis (EDA), and visualization to gain actionable insights for revenue improvement and lead conversion efficiency.

# 📊 Financial Analysis & Lead Generation Optimization for Health Care Company

## **Overview**
This project analyzes financial trends related to patient responsibility and lead generation for Blackstone Medical Services. By examining revenue distribution, patient tiers, and insurance provider contributions, we identify key insights to optimize revenue collection and lead conversion.

---

## **📌 Key Insights**
- **Revenue by Tier:** Tier 3 patients contribute the highest revenue (~$3.8M).
- **Lead Volume Stability:** January & February had nearly **identical lead counts** (~17.6K).
- **Revenue Decline:** February saw **$87K less revenue** than January despite similar lead volume.
- **Lead Volatility:** Some days had extreme **spikes and drops (1,835 vs. 0 leads)**.
- **Insurance Contributions:** **Self-Pay & BCBS drive the most revenue**; Medicare and Humana are lower.

---

## **📁 Files in the Repository**
### **1️⃣ Data Cleaning**
`data_cleaning.py` - Cleans and preprocesses the dataset:
- Standardizes column names.
- Converts dates and numeric fields.
- Fills missing values.
- Saves a cleaned dataset.

### **2️⃣ Data Analysis**
`analyze_data.py` - Performs **Exploratory Data Analysis (EDA)**:
- Generates **descriptive statistics**.
- Identifies **top insurance contributors**.
- Detects **outliers in patient responsibility**.
- Examines **tier-based revenue segmentation**.

### **3️⃣ Data Visualization**
`visualization.py` - Produces key insights through visualizations:
- **Revenue breakdown by tier.**
- **Leads trend analysis over time.**
- **Monthly revenue & lead comparison.**
- **Insurance company revenue impact.**
---
## **🚀 How to Run the Project**
1️⃣ Clone the repository:
```bash
git clone https://github.com/John-Z-byte/Financial-Analysis-Lead-Generation-Optimization-for-Health-Care-Company.git
