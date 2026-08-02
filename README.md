# Job Market Analytics Dashboard

**Tools used:** Python | Pandas | Matplotlib | SQL | Excel

---

## What this project is about

I analysed 1000+ job postings in the data industry to find answers to questions that matter to a job seeker:

- Which cities have the most data jobs?
- What skills do companies ask for the most?
- How much does salary change with experience?
- Are remote jobs growing?
- Which companies hire the most freshers?

---

## Project Structure

```
Job-Market-Analytics/
│
├── dataset/                  → Raw data (jobs_raw.csv)
├── cleaned_data/             → Cleaned data (cleaned_jobs.csv)
│
├── python/
│   ├── 01_generate_sample_data.py   → Creates the dataset
│   ├── 02_data_cleaning.py          → Cleans raw data using Pandas
│   ├── 03_eda_analysis.py           → Creates 10 charts using Matplotlib
│   ├── 04_business_insights.py      → Prints key findings
│   └── 05_export_for_excel.py       → Exports data to Excel
│
├── sql/
│   ├── 01_create_tables.sql         → Creates the MySQL table
│   ├── 02_analysis_queries.sql      → 15 business queries
│   └── 03_advanced_queries.sql      → CTEs, window functions, subqueries
│
├── excel/
│   └── job_market_dashboard.xlsx    → Dashboard with charts and KPIs
│
├── images/                   → All charts saved as PNG files
└── README.md
```

---

## Steps I followed

**Step 1 — Created the dataset**
Built a Python script that generates 1000 realistic job postings with fields like job title, company, city, skills, salary, and work mode. Added intentional dirty data (duplicates and typos) to make the cleaning step realistic.

**Step 2 — Cleaned the data**
Used Pandas to:
- Remove 30 duplicate rows
- Fix city name formatting (bangalore → Bangalore)
- Fill missing salary values with the average salary of that experience group
- Convert date strings to proper datetime format
- Extract month from date for trend analysis

**Step 3 — Exploratory Data Analysis**
Created 10 charts using Matplotlib to answer business questions:

| Chart | Question answered |
|-------|-------------------|
| Bar chart | Which companies hire the most? |
| Bar chart | Which cities have the most postings? |
| Bar chart | Average salary by city |
| Horizontal bar | Top 15 most demanded skills |
| Bar chart | Fresher vs experienced jobs |
| Pie chart | Remote vs Hybrid vs On-site split |
| Histogram | How are salaries distributed? |
| Horizontal bar | Highest paying job titles |
| Line chart | Hiring trend month by month |
| Bar chart | Average salary by experience level |

**Step 4 — Business Insights**
Calculated key numbers from the data:
- Top hiring city and company
- Top 5 skills and their % appearance in job postings
- Salary growth from fresher to senior level
- Work mode percentages
- Peak hiring month

**Step 5 — Excel Dashboard**
Exported 11 summary sheets to Excel and built an interactive dashboard with:
- KPI cards (Total Jobs, Average Salary, Top City, Top Skill)
- Pivot tables
- Charts with slicers for filtering

**Step 6 — SQL Analysis**
Imported the cleaned data into MySQL and wrote queries using:
- SELECT, WHERE, GROUP BY, ORDER BY, HAVING
- Aggregate functions (COUNT, AVG, MIN, MAX)
- Subqueries
- CTEs (Common Table Expressions)
- Window functions (RANK, NTILE)

---

## Key Findings

- **SQL** and **Python** appear in the majority of data job postings
- Freshers have real opportunities — they make up around **25% of all postings**
- Average salary grows from **~3.7 LPA** (fresher) to **~18 LPA** (senior)
- **Hybrid** work is the most common arrangement
- Peak hiring happens mid-year (June–July)

---

## Charts

![Top Companies](images/01_top_companies.png)
![Top Skills](images/04_top_skills.png)
![Salary by Experience](images/10_salary_by_experience.png)
![Work Mode](images/06_work_mode_pie.png)

---

## How to run this project

**1. Install dependencies**
```bash
pip install pandas matplotlib openpyxl
```

**2. Run the scripts in order**
```bash
cd python
py 01_generate_sample_data.py
py 02_data_cleaning.py
py 03_eda_analysis.py
py 04_business_insights.py
py 05_export_for_excel.py
```

**3. For SQL**
- Open MySQL Workbench
- Run `sql/01_create_tables.sql`
- Import `cleaned_data/cleaned_jobs.csv`
- Run `sql/02_analysis_queries.sql`

---

## Skills demonstrated

- Python (data generation, cleaning, analysis, visualisation)
- Pandas (DataFrame operations, groupby, filtering, handling missing values)
- Matplotlib (bar, pie, line, histogram charts)
- SQL (queries, aggregations, joins, CTEs, window functions)
- Excel (pivot tables, charts, KPI dashboard, slicers)
- Data cleaning best practices
- Exploratory Data Analysis (EDA)
- Business insight generation
