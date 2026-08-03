# Step 2 - Data Cleaning
# We load the raw CSV, fix all the problems, and save a clean version
# Input:  dataset/jobs_raw.csv
# Output: cleaned_data/cleaned_jobs.csv

import pandas as pd

# Load the raw data

df = pd.read_csv("../dataset/jobs_raw.csv")

print("--- Raw Data Info ---")
print("Total rows:", len(df))
print("Total columns:", len(df.columns))
print()

# Step 1: Check for missing value

print("--- Missing Values ---")
print(df.isnull().sum())
print()

# Step 2: Check for duplicate rows

print("Duplicate rows found:", df.duplicated().sum())

# Remove duplicates
df = df.drop_duplicates()

print("Rows after removing duplicates:", len(df))
print()

# Step 3: Fix city names
# Some city names are lowercase because of typos
# We use .str.title() to make them proper case
# Example: "bangalore" becomes "Bangalore"

df["location"] = df["location"].str.strip()   # remove spaces
df["location"] = df["location"].str.title()   # capitalize first letter

print("City names fixed.")

# Step 4: Fill missing salary values
# We fill missing salary with the average salary
# of that experience level (a simple, logical approach)

# Calculate average salary for each experience group
avg_salary_by_exp = df.groupby("experience")["salary_lpa"].mean()

print("\nAverage salary by experience (used to fill missing values):")
print(avg_salary_by_exp.round(1))

# Fill each missing salary with the group average
for index, row in df.iterrows():
    if pd.isnull(row["salary_lpa"]):
        exp_level = row["experience"]
        df.loc[index, "salary_lpa"] = round(avg_salary_by_exp[exp_level], 1)

print("\nMissing salaries filled.")

# Step 5: Convert date_posted to proper date format

df["date_posted"] = pd.to_datetime(df["date_posted"])

# Extract month as a readable string like "2024-03"
df["month_posted"] = df["date_posted"].dt.to_period("M").astype(str)

print("Dates converted.")

# Step 6: Final check

print("\n--- After Cleaning ---")
print("Total rows:", len(df))
print("Missing values left:")
print(df.isnull().sum())
print()
print("First 3 rows:")
print(df.head(3))

# Save the clean file

df.to_csv("../cleaned_data/cleaned_jobs.csv", index=False)

print("\nClean file saved to cleaned_data/cleaned_jobs.csv")
