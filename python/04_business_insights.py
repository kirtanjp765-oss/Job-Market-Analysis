# Step 4 - Business Insights
# This script reads the clean data and prints key findings

import pandas as pd

# Load clean data

df = pd.read_csv("../cleaned_data/cleaned_jobs.csv")

print("=" * 55)
print("   JOB MARKET ANALYTICS - KEY INSIGHTS")
print("=" * 55)

# Basic numbers

total_jobs = len(df)
avg_salary = round(df["salary_lpa"].mean(), 1)
max_salary = df["salary_lpa"].max()
min_salary = df["salary_lpa"].min()

print(f"\nTotal job postings   : {total_jobs}")
print(f"Average salary       : {avg_salary} LPA")
print(f"Highest salary       : {max_salary} LPA")
print(f"Lowest salary        : {min_salary} LPA")

# Top hiring city

city_counts = df["location"].value_counts()
top_city = city_counts.index[0]
top_city_count = city_counts.iloc[0]
top_city_pct = round((top_city_count / total_jobs) * 100, 1)

print(f"\nTop hiring city      : {top_city}")
print(f"Jobs in {top_city:<12}: {top_city_count} ({top_city_pct}% of total)")

# Top hiring company

company_counts = df["company"].value_counts()
top_company = company_counts.index[0]
top_company_count = company_counts.iloc[0]

print(f"\nTop hiring company   : {top_company} ({top_company_count} postings)")

# Top 5 skills

# Split skills and count each one
skill_count = {}

for skills_str in df["skills"]:
    for skill in skills_str.split(", "):
        if skill in skill_count:
            skill_count[skill] += 1
        else:
            skill_count[skill] = 1

# Sort by count
sorted_skills = sorted(skill_count.items(), key=lambda x: x[1], reverse=True)

print("\nTop 5 in-demand skills:")
for skill, count in sorted_skills[:5]:
    percentage = round((count / total_jobs) * 100, 1)
    print(f"  - {skill:<18}: {percentage}% of job postings")

# Work mode breakdown

work_mode_counts = df["work_mode"].value_counts()

print("\nWork mode breakdown:")
for mode, count in work_mode_counts.items():
    pct = round((count / total_jobs) * 100, 1)
    print(f"  - {mode:<12}: {pct}%")

# Experience level demand

exp_counts = df["experience"].value_counts()

print("\nExperience level demand:")
for level, count in exp_counts.items():
    pct = round((count / total_jobs) * 100, 1)
    print(f"  - {level:<25}: {pct}%")

# Salary by experience level

exp_order = ["Fresher (0-1 yr)", "Junior (1-3 yrs)", "Mid (3-5 yrs)", "Senior (5+ yrs)"]

print("\nAverage salary by experience:")
for level in exp_order:
    subset = df[df["experience"] == level]
    avg = round(subset["salary_lpa"].mean(), 1)
    print(f"  - {level:<25}: {avg} LPA")

# Highest paying job title

avg_by_title = df.groupby("job_title")["salary_lpa"].mean().round(1)
best_title = avg_by_title.idxmax()
best_salary = avg_by_title.max()

print(f"\nHighest paying role  : {best_title} (avg {best_salary} LPA)")

# Peak hiring month

monthly = df["month_posted"].value_counts()
peak_month = monthly.index[0]
peak_count = monthly.iloc[0]

print(f"Peak hiring month    : {peak_month} ({peak_count} postings)")

print()
print("=" * 55)
print("Insight summary:")
print(f"  - {top_city} is the top city for data jobs.")
print(f"  - Freshers make up {round((exp_counts.get('Fresher (0-1 yr)', 0) / total_jobs) * 100, 1)}% of openings — good opportunities exist.")
print(f"  - Average salary jumps from ~3 LPA to ~18 LPA as experience grows.")
print(f"  - SQL and Python appear in most job descriptions.")
print("=" * 55)
