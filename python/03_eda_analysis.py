# Step 3 - Exploratory Data Analysis (EDA)
# We load the clean data and create charts to answer business questions

import pandas as pd
import matplotlib.pyplot as plt
import os

# Load clean data

df = pd.read_csv("../cleaned_data/cleaned_jobs.csv")
os.makedirs("../images", exist_ok=True)

print("Data loaded. Total rows:", len(df))
print()

# Q1: Which companies are hiring the most?

company_counts = df["company"].value_counts().head(10)

plt.figure(figsize=(10, 6))
plt.barh(company_counts.index, company_counts.values, color="steelblue")
plt.title("Top 10 Hiring Companies")
plt.xlabel("Number of Job Postings")
plt.gca().invert_yaxis()  # highest on top
plt.tight_layout()
plt.savefig("../images/01_top_companies.png")
plt.close()

print("Chart saved: 01_top_companies.png")

# Q2: Which cities have the most job postings?

city_counts = df["location"].value_counts()

plt.figure(figsize=(10, 6))
plt.bar(city_counts.index, city_counts.values, color="teal")
plt.title("Job Postings by City")
plt.xlabel("City")
plt.ylabel("Number of Postings")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("../images/02_jobs_by_city.png")
plt.close()

print("Chart saved: 02_jobs_by_city.png")

# Q3: What is the average salary in each city?

avg_salary_city = df.groupby("location")["salary_lpa"].mean().round(1).sort_values(ascending=False)

plt.figure(figsize=(10, 6))
plt.bar(avg_salary_city.index, avg_salary_city.values, color="coral")
plt.title("Average Salary by City (LPA)")
plt.xlabel("City")
plt.ylabel("Average Salary (LPA)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("../images/03_avg_salary_city.png")
plt.close()

print("Chart saved: 03_avg_salary_city.png")

# Q4: Which are the top 20 skills in demand?

# Each row has multiple skills separated by ", "
# We need to count how often each skill appears

all_skills = []

for skills_str in df["skills"]:
    skill_list = skills_str.split(", ")
    for skill in skill_list:
        all_skills.append(skill)

# Count each skill manually using a dictionary
skill_count = {}
for skill in all_skills:
    if skill in skill_count:
        skill_count[skill] += 1
    else:
        skill_count[skill] = 1

# Sort by count (highest first) and take top 15
sorted_skills = sorted(skill_count.items(), key=lambda x: x[1], reverse=True)
top_skills = sorted_skills[:15]

skill_names  = [item[0] for item in top_skills]
skill_values = [item[1] for item in top_skills]

plt.figure(figsize=(10, 7))
plt.barh(skill_names, skill_values, color="mediumpurple")
plt.title("Top 15 Most Demanded Skills")
plt.xlabel("Number of Job Postings")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig("../images/04_top_skills.png")
plt.close()

print("Chart saved: 04_top_skills.png")

# Q5: Fresher vs Experienced jobs

exp_counts = df["experience"].value_counts()

plt.figure(figsize=(8, 5))
plt.bar(exp_counts.index, exp_counts.values, color="goldenrod")
plt.title("Job Postings by Experience Level")
plt.xlabel("Experience Level")
plt.ylabel("Number of Postings")
plt.xticks(rotation=15)
plt.tight_layout()
plt.savefig("../images/05_experience_levels.png")
plt.close()

print("Chart saved: 05_experience_levels.png")

# Q6: Remote vs Hybrid vs On-site

work_mode_counts = df["work_mode"].value_counts()

plt.figure(figsize=(6, 6))
plt.pie(
    work_mode_counts.values,
    labels=work_mode_counts.index,
    autopct="%1.1f%%",
    colors=["#66b3ff", "#99ff99", "#ffcc99"]
)
plt.title("Work Mode Distribution")
plt.tight_layout()
plt.savefig("../images/06_work_mode_pie.png")
plt.close()

print("Chart saved: 06_work_mode_pie.png")

# Q7: Salary distribution - how are salaries spread?

salaries = df["salary_lpa"].dropna()

plt.figure(figsize=(10, 5))
plt.hist(salaries, bins=20, color="steelblue", edgecolor="white")
plt.title("Salary Distribution (LPA)")
plt.xlabel("Salary in LPA")
plt.ylabel("Number of Jobs")
plt.tight_layout()
plt.savefig("../images/07_salary_distribution.png")
plt.close()

print("Chart saved: 07_salary_distribution.png")

# Q8: Average salary by job title

avg_salary_title = df.groupby("job_title")["salary_lpa"].mean().round(1).sort_values(ascending=False)

plt.figure(figsize=(10, 6))
plt.barh(avg_salary_title.index, avg_salary_title.values, color="tomato")
plt.title("Average Salary by Job Title (LPA)")
plt.xlabel("Average Salary (LPA)")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig("../images/08_salary_by_title.png")
plt.close()

print("Chart saved: 08_salary_by_title.png")

# Q9: Jobs posted each month (hiring trend)

monthly_counts = df["month_posted"].value_counts().sort_index()

plt.figure(figsize=(12, 5))
plt.plot(monthly_counts.index, monthly_counts.values, marker="o", color="darkblue")
plt.title("Job Postings by Month (2024)")
plt.xlabel("Month")
plt.ylabel("Number of Postings")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("../images/09_monthly_trend.png")
plt.close()

print("Chart saved: 09_monthly_trend.png")

# Q10: Average salary by experience level

# Define order so the chart shows Fresher first
exp_order = ["Fresher (0-1 yr)", "Junior (1-3 yrs)", "Mid (3-5 yrs)", "Senior (5+ yrs)"]

avg_sal_exp = df.groupby("experience")["salary_lpa"].mean().round(1)
avg_sal_exp = avg_sal_exp.reindex(exp_order)  # sort in logical order

plt.figure(figsize=(9, 5))
plt.bar(avg_sal_exp.index, avg_sal_exp.values, color=["#a8d8ea", "#a8e6cf", "#ffd3b6", "#ff8b94"])
plt.title("Average Salary by Experience Level (LPA)")
plt.xlabel("Experience Level")
plt.ylabel("Average Salary (LPA)")
plt.xticks(rotation=15)

# Add the number on top of each bar
for i, value in enumerate(avg_sal_exp.values):
    plt.text(i, value + 0.1, str(value), ha="center")

plt.tight_layout()
plt.savefig("../images/10_salary_by_experience.png")
plt.close()

print("Chart saved: 10_salary_by_experience.png")

print()
print("All 10 charts saved to the images/ folder.")
