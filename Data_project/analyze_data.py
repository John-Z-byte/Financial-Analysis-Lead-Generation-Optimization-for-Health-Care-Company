import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def analyze_data(file_path):
    """Loads and performs in-depth exploratory data analysis on cleaned data."""
    
    df = pd.read_excel(file_path)

    # Standardize column names
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")
    
    if "insurence_company" in df.columns:
        df.rename(columns={"insurence_company": "insurance_company"}, inplace=True)

    # Convert date column
    df["date_added"] = pd.to_datetime(df["date_added"], errors='coerce')

    # Drop missing values in key columns
    df = df.dropna(subset=["date_added", "patient_responsibility", "insurance_company"])

    print("\n📊 Dataset Overview:")
    print(df.info())

    print("\n📈 Descriptive Statistics:")
    print(df.describe())

    print("\n🔍 Missing Values Summary:")
    print(df.isnull().sum())

    print("\n📌 Top 5 Insurance Companies by Number of Leads:")
    print(df["insurance_company"].value_counts().head())

    print("\n💰 Revenue Breakdown (Total Patient Responsibility by Tier):")
    print(df.groupby("tier")["patient_responsibility"].sum())

    # ✅ High-Value Leads: Top 10 patients with highest out-of-pocket costs
    top_10_patients = df.nlargest(10, "patient_responsibility")[["patient_name", "patient_responsibility", "insurance_company"]]
    print("\n🔥 Top 10 High-Value Leads:")
    print(top_10_patients)

    # ✅ Outlier Detection in Patient Responsibility
    plt.figure(figsize=(8, 5))
    sns.boxplot(data=df, x="patient_responsibility", color="red")
    plt.title("📊 Outlier Analysis: Patient Responsibility")
    plt.xlabel("Patient Responsibility ($)")
    plt.show()

    # ✅ Tier Contribution to Total Revenue
    tier_revenue = df.groupby("tier")["patient_responsibility"].sum().sort_values(ascending=False)
    plt.figure(figsize=(8, 5))
    sns.barplot(x=tier_revenue.index, y=tier_revenue.values, palette="Blues_r")
    plt.title("💰 Revenue Contribution by Tier")
    plt.xlabel("Tier")
    plt.ylabel("Total Revenue ($)")
    plt.grid(axis="y", linestyle="--", alpha=0.6)
    plt.show()

    return df

# Run this script independently if needed
if __name__ == "__main__":
    analyze_data("Landing_2025_Cleaned.xlsx")
