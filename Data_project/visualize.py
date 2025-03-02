import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the cleaned data
file_path = "Landing_2025_Cleaned.xlsx"
df = pd.read_excel(file_path)

# Ensure tier names are cleaned
df["tier"] = df["tier"].astype(str).str.strip()

# Convert date to datetime format
df["date_added"] = pd.to_datetime(df["date_added"], errors='coerce')

# Drop any rows with missing dates
df = df.dropna(subset=["date_added"])

# Extract Month and Year for comparison
df["month"] = df["date_added"].dt.strftime("%Y-%m")

# Fix potential spelling errors in column names
if "insurence_company" in df.columns:
    df.rename(columns={"insurence_company": "insurance_company"}, inplace=True)

# Function to add data labels to bar charts
def add_labels(ax, spacing=5):
    """Adds value labels to bars in a chart."""
    for rect in ax.patches:
        height = rect.get_height()
        if height > 0:
            ax.annotate(f'{height:,.0f}', 
                        xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(0, spacing),
                        textcoords="offset points",
                        ha='center', fontsize=10, fontweight='bold')

# --- 1️⃣ Leads Trend Over Time (January vs. February) ---
jan_feb_leads = df[df["month"].isin(["2025-01", "2025-02"])]
daily_leads = jan_feb_leads.groupby(df["date_added"].dt.to_period("D")).size().sort_index()

plt.figure(figsize=(12, 5))
sns.lineplot(x=daily_leads.index.astype(str), y=daily_leads.values, marker="o", linestyle="-", color="#1f77b4", label="Leads")

# Reduce label clutter: Show every 5th value
for i, txt in enumerate(daily_leads.values):
    if i % 5 == 0 or txt > 1500:
        plt.annotate(txt, (daily_leads.index[i].strftime("%Y-%m-%d"), daily_leads.values[i]), 
                     textcoords="offset points", xytext=(0,5), ha='center', fontsize=9)

plt.xticks(daily_leads.index[::5].astype(str), rotation=45)
plt.xlabel("Date")
plt.ylabel("Number of Leads")
plt.title("📅 Leads Generated Over Time (Jan vs. Feb)")
plt.grid(True, linestyle="--", alpha=0.6)
plt.legend()
plt.show()

# --- 2️⃣ Total Leads & Revenue Comparison (Bar Chart) ---
monthly_stats = df.groupby("month").agg({"patient_responsibility": "sum", "mrn": "count"})
monthly_stats.rename(columns={"mrn": "Total Leads", "patient_responsibility": "Total Revenue"}, inplace=True)

fig, ax = plt.subplots(figsize=(8, 5))
sns.barplot(x=monthly_stats.index, y=monthly_stats["Total Leads"], palette=["#1f77b4", "#ff7f0e"], ax=ax)
plt.xlabel("Month")
plt.ylabel("Total Leads")
plt.title("📊 Total Leads: January vs. February")
add_labels(ax)
plt.grid(axis="y", linestyle="--", alpha=0.6)
plt.show()

fig, ax = plt.subplots(figsize=(8, 5))
sns.barplot(x=monthly_stats.index, y=monthly_stats["Total Revenue"], palette=["#2ca02c", "#d62728"], ax=ax)
plt.xlabel("Month")
plt.ylabel("Total Revenue ($)")
plt.title("💰 Total Revenue: January vs. February")
add_labels(ax)
plt.grid(axis="y", linestyle="--", alpha=0.6)
plt.show()

# --- 3️⃣ Daily Trends Analysis: January vs. February ---
df_jan = df[df["month"] == "2025-01"].groupby(df["date_added"].dt.to_period("D")).size().sort_index()
df_feb = df[df["month"] == "2025-02"].groupby(df["date_added"].dt.to_period("D")).size().sort_index()

plt.figure(figsize=(10, 5))
sns.lineplot(x=df_jan.index.astype(str), y=df_jan.values, marker="o", linestyle="-", color="blue", label="January")
sns.lineplot(x=df_feb.index.astype(str), y=df_feb.values, marker="s", linestyle="-", color="red", label="February")

for i, txt in enumerate(df_jan.values):
    if i % 5 == 0 or txt > 1500:
        plt.annotate(txt, (df_jan.index[i].strftime("%Y-%m-%d"), df_jan.values[i]), textcoords="offset points", xytext=(0,5), ha='center', fontsize=9, color="blue")

for i, txt in enumerate(df_feb.values):
    if i % 5 == 0 or txt > 1500:
        plt.annotate(txt, (df_feb.index[i].strftime("%Y-%m-%d"), df_feb.values[i]), textcoords="offset points", xytext=(0,5), ha='center', fontsize=9, color="red")

plt.xlabel("Date")
plt.ylabel("Number of Leads")
plt.title("📈 Daily Lead Trends: January vs. February")
plt.xticks(rotation=45)
plt.legend()
plt.grid(True, linestyle="--", alpha=0.6)
plt.show()

# --- 4️⃣ Insurance Revenue Comparison (Top 5 Insurances) ---
top_insurances = df["insurance_company"].value_counts().head(5).index
df_top_insurances = df[df["insurance_company"].isin(top_insurances)]

monthly_insurance_revenue = df_top_insurances.groupby(["month", "insurance_company"])["patient_responsibility"].sum().unstack()

fig, ax = plt.subplots(figsize=(10, 6))
monthly_insurance_revenue.plot(kind="bar", ax=ax, colormap="viridis")
plt.xlabel("Month")
plt.ylabel("Total Revenue ($)")
plt.title("🏥 Revenue by Insurance Provider: January vs. February")
plt.xticks(rotation=0)
plt.legend(title="Insurance Provider")
add_labels(ax)
plt.grid(axis="y", linestyle="--", alpha=0.6)
plt.show()
