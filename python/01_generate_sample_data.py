
import pandas as pd
import random
import os

random.seed(42)

# Reference lists - the data we will randomly pick from

job_titles = [
    "Data Analyst",
    "Senior Data Analyst",
    "Junior Data Analyst",
    "Business Analyst",
    "Data Scientist",
    "SQL Developer",
    "BI Analyst",
    "Python Developer"
]

companies = [
    "Infosys", "TCS", "Wipro", "HCL Technologies",
    "Accenture", "Cognizant", "IBM India", "Capgemini",
    "Amazon India", "Flipkart", "Swiggy", "Zomato",
    "Google India", "Microsoft India", "HDFC Bank", "ICICI Bank"
]

cities = [
    "Bangalore", "Hyderabad", "Chennai", "Pune",
    "Mumbai", "Delhi", "Noida", "Gurgaon"
]

work_modes = ["On-site", "Hybrid", "Remote"]

experience_levels = [
    "Fresher (0-1 yr)",
    "Junior (1-3 yrs)",
    "Mid (3-5 yrs)",
    "Senior (5+ yrs)"
]

employment_types = ["Full-time", "Contract", "Internship"]

skills_pool = [
    "Python", "SQL", "Excel", "Power BI", "Tableau",
    "Pandas", "NumPy", "Statistics", "Machine Learning", "Git"
]

salary_range = {
    "Fresher (0-1 yr)":  (2.5, 5.0),
    "Junior (1-3 yrs)":  (4.0, 8.0),
    "Mid (3-5 yrs)":     (7.0, 14.0),
    "Senior (5+ yrs)":   (12.0, 25.0)
}

rows = []

for job_id in range(1, 1001):  # 1000 job postings

    title      = random.choice(job_titles)
    company    = random.choice(companies)
    city       = random.choice(cities)
    work_mode  = random.choice(work_modes)
    experience = random.choice(experience_levels)
    emp_type   = random.choice(employment_types)

    # Pick 2 to 5 skills randomly (no repeats)
    num_skills = random.randint(2, 5)
    job_skills = random.sample(skills_pool, num_skills)
    skills_str = ", ".join(job_skills)

    # Pick a salary based on experience
    low, high = salary_range[experience]
    salary = round(random.uniform(low, high), 1)

    # Make 5% of salaries missing (to practice cleaning)
    if random.random() < 0.05:
        salary = None

    # Random date in 2024
    month  = random.randint(1, 12)
    day    = random.randint(1, 28)
    date   = f"2024-{month:02d}-{day:02d}"

    rows.append([
        job_id, title, company, city, work_mode,
        experience, emp_type, skills_str, salary, date
    ])


columns = [
    "job_id", "job_title", "company", "location",
    "work_mode", "experience", "employment_type",
    "skills", "salary_lpa", "date_posted"
]

df = pd.DataFrame(rows, columns=columns)

# Add 30 duplicate rows (messy real-world data)
duplicates = df.sample(30, random_state=1)
df = pd.concat([df, duplicates], ignore_index=True)

# Make some city names lowercase (typo simulation)
for i in range(0, 20):
    df.loc[i, "location"] = df.loc[i, "location"].lower()



os.makedirs("../dataset", exist_ok=True)
df.to_csv("../dataset/jobs_raw.csv", index=False)

print("Done! Raw dataset saved to dataset/jobs_raw.csv")
print("Total rows:", len(df))
