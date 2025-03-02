# 📊 Financial Analysis & Lead Generation Optimization for Health Care Company

This project analyzes **financial trends in patient responsibility** and **optimizes lead generation** at a healthcare provider company. It involves **data cleaning, exploratory data analysis (EDA), and visualizations** to generate actionable insights for **revenue improvement and lead conversion efficiency**.

---

## 📖 Table of Contents
1. [Overview](#-overview)  
2. [Key Insights](#-key-insights)  
3. [Installation & Setup](#-installation--setup)  
4. [How to Use](#-how-to-use)  
5. [Business Impact](#-business-impact)  
6. [Visualizations](#-visualizations)  
7. [About Me](#-about-me)  

---

## 📊 Overview
This project analyzes **financial trends related to patient responsibility and lead generation** for **Blackstone Medical Services**. By examining **revenue distribution, patient tiers, and insurance provider contributions**, we identify key insights to **optimize revenue collection and lead conversion rates**.

---

## 🔎 Key Insights
- **💰 Revenue by Tier:** **Tier 3 patients contribute the highest revenue (~$3.8M).**
- **📈 Lead Volume Stability:** **January & February had nearly identical lead counts (~17.6K).**  
  ![image](https://github.com/user-attachments/assets/725bf4e6-4d6e-49fc-b4c3-6a1cc9bb773b)

- **📉 Revenue Decline:** **Despite similar lead volume, February saw $87K less revenue than January.**
- **📊 Lead Volatility:** **Some days had extreme spikes and drops (1,835 vs. 0 leads).**  
  ![image](https://github.com/user-attachments/assets/82f36399-7924-4c46-8a22-7c33cc92c9f9)  
  ![image](https://github.com/user-attachments/assets/b772fc6b-de87-4a47-8ed0-3ee5d2840fee)

- **🏥 Insurance Contributions:** **Self-Pay & BCBS drive the most revenue**; Medicare and Humana contribute significantly less.  
  ![image](https://github.com/user-attachments/assets/3dcc404c-0a41-4689-8d2b-0c81f6345f98)

---

## 📂 Files in the Repository

### 🛠️ **1. Data Cleaning**
📌 `data_cleaning.py` - Cleans and preprocesses the dataset:  
✔️ Standardizes column names  
✔️ Converts dates and numeric fields  
✔️ Fills missing values  
✔️ Saves a cleaned dataset  

### 📊 **2. Data Analysis**
📌 `analyze_data.py` - Performs **Exploratory Data Analysis (EDA)**:  
✔️ Generates **descriptive statistics**  
✔️ Identifies **top insurance contributors**  
✔️ Detects **outliers in patient responsibility**  
✔️ Examines **tier-based revenue segmentation**  

### 📈 **3. Data Visualization**
📌 `visualization.py` - Produces **key insights through visualizations**:  
✔️ **Revenue breakdown by tier**  
✔️ **Leads trend analysis over time**  
✔️ **Monthly revenue & lead comparison**  
✔️ **Insurance company revenue impact**  

---

## ⚙️ Installation & Setup
To run this project, install the required libraries.

### 🔹 1️⃣ **Clone the repository**:
```bash
git clone https://github.com/John-Z-byte/Financial-Analysis-Lead-Generation-Optimization-for-Health-Care-Company.git
