import pandas as pd

# Load the Excel file
file_path = "Landing_2025.xlsx"
df = pd.read_excel(file_path, sheet_name="Landing_2025")

# Standardize column names
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# Standardize DOB format
df["dob"] = pd.to_datetime(df["dob"], errors="coerce")

# Convert patient responsibility to numeric
df["patient_responsibility"] = pd.to_numeric(df["patient_responsibility"], errors="coerce")

# Fill missing values
df.fillna({
    "number": "Unknown",
    "mrn": "No MRN",
    "tier": "Unspecified",
    "insurence_company": "Unknown"
}, inplace=True)
df["tier"] = df["tier"].str.strip() #Column Tier


# Save the cleaned data
df.to_excel("Landing_2025_Cleaned.xlsx", index=False)
print("Data cleaning complete! File saved as Landing_2025_Cleaned.xlsx")