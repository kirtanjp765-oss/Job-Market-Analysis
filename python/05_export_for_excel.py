# Step 5 - Export data to Excel
# This creates an Excel file with multiple sheets
# Each sheet is a summary table you can use to build charts and pivot tables
# Output: excel/job_market_dashboard.xlsx

import pandas as pd
import os

# -------------------------------------------------------
# Load clean data
# -------------------------------------------------------

df = pd.read_csv("../cleaned_data/cleaned_jobs.csv")
os.makedirs("../excel", exist_ok=True)

output_file = "../excel/job_market_dashboard.xlsx"

# -------------------------------------------------------
# Prepare summary tables
# -------------------------------------------------------

# 1. Jobs by company
jobs_by_company = df["company"].value_counts().reset_index()
jobs_by_company.columns = ["company", "job_count"]

# 2. Jobs by city
jobs_by_city = df["location"].value_counts().reset_index()
jobs_by_city.columns = ["city", "job_count"]

# 3. Average salary by city
avg_salary_city = df.groupby("location")["salary_lpa"].mean().round(1).reset_index()
avg_salary_city.columns = ["city", "avg_salary_lpa"]
avg_salary_city = avg_salary_city.sort_values("avg_salary_lpa", ascending=False)

# 4. Jobs by work mode
jobs_by_workmode = df["work_mode"].value_counts().reset_index()
jobs_by_workmode.columns = ["work_mode", "job_count"]

# 5. Jobs by experience
jobs_by_exp = df["experience"].value_counts().reset_index()
jobs_by_exp.columns = ["experience", "job_count"]

# 6. Average salary by experience
avg_salary_exp = df.groupby("experience")["salary_lpa"].mean().round(1).reset_index()
avg_salary_exp.columns = ["experience", "avg_salary_lpa"]

# 7. Jobs by job title
jobs_by_title = df["job_title"].value_counts().reset_index()
jobs_by_title.columns = ["job_title", "job_count"]

# 8. Monthly trend
monthly_trend = df["month_posted"].value_counts().sort_index().reset_index()
monthly_trend.columns = ["month", "job_count"]

# 9. Top skills - count each skill across all postings
skill_count = {}
for skills_str in df["skills"]:
    for skill in skills_str.split(", "):
        if skill in skill_count:
            skill_count[skill] += 1
        else:
            skill_count[skill] = 1

top_skills = pd.DataFrame(
    sorted(skill_count.items(), key=lambda x: x[1], reverse=True),
    columns=["skill", "count"]
)

# 10. KPI summary
kpi_data = {
    "KPI": [
        "Total Jobs",
        "Average Salary (LPA)",
        "Top City",
        "Top Company",
        "Top Skill",
        "Most Common Work Mode"
    ],
    "Value": [
        len(df),
        round(df["salary_lpa"].mean(), 1),
        df["location"].value_counts().index[0],
        df["company"].value_counts().index[0],
        top_skills.iloc[0]["skill"],
        df["work_mode"].value_counts().index[0]
    ]
}
kpis = pd.DataFrame(kpi_data)

# -------------------------------------------------------
# Write all sheets to one Excel file
# -------------------------------------------------------

with pd.ExcelWriter(output_file, engine="openpyxl") as writer:
    df.to_excel(writer,              sheet_name="All_Data",        index=False)
    kpis.to_excel(writer,            sheet_name="KPIs",            index=False)
    jobs_by_company.to_excel(writer, sheet_name="By_Company",      index=False)
    jobs_by_city.to_excel(writer,    sheet_name="By_City",         index=False)
    avg_salary_city.to_excel(writer, sheet_name="Salary_By_City",  index=False)
    jobs_by_workmode.to_excel(writer,sheet_name="Work_Mode",       index=False)
    jobs_by_exp.to_excel(writer,     sheet_name="By_Experience",   index=False)
    avg_salary_exp.to_excel(writer,  sheet_name="Salary_By_Exp",   index=False)
    jobs_by_title.to_excel(writer,   sheet_name="By_Title",        index=False)
    monthly_trend.to_excel(writer,   sheet_name="Monthly_Trend",   index=False)
    top_skills.to_excel(writer,      sheet_name="Top_Skills",      index=False)

print("Excel file saved to excel/job_market_dashboard.xlsx")
print("Sheets created:")
print("  - All_Data")
print("  - KPIs")
print("  - By_Company")
print("  - By_City")
print("  - Salary_By_City")
print("  - Work_Mode")
print("  - By_Experience")
print("  - Salary_By_Exp")
print("  - By_Title")
print("  - Monthly_Trend")
print("  - Top_Skills")
print()
print("Now open the file in Excel and follow EXCEL_DASHBOARD_GUIDE.md")
