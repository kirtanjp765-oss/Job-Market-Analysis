# Excel Dashboard — Step-by-Step Guide

After running `05_export_for_excel.py`, open `job_market_dashboard.xlsx`.

---

## Step 1 — KPI Cards (top of dashboard)

Go to the **KPIs** sheet. You'll see:
- Total Jobs
- Average Salary
- Median Salary
- Top City
- Top Company
- Top Skill

Copy these 6 cells into a new sheet called **Dashboard**.
Format them as large bold numbers in colored boxes.

---

## Step 2 — Bar Chart: Top Companies

1. Go to **By_Company** sheet
2. Select `company` and `job_count` columns (top 10 rows)
3. Insert → Bar Chart → Clustered Bar
4. Title: "Top 10 Hiring Companies"
5. Paste into Dashboard sheet

---

## Step 3 — Bar Chart: Top Cities

1. Go to **By_City** sheet
2. Select `location` and `job_count` columns
3. Insert → Bar Chart
4. Title: "Jobs by City"

---

## Step 4 — Pie Chart: Work Mode

1. Go to **Work_Mode** sheet
2. Select both columns
3. Insert → Pie Chart
4. Title: "Remote vs Hybrid vs On-site"
5. Show percentages (Format Data Labels → Percentage)

---

## Step 5 — Bar Chart: Top Skills

1. Go to **Top_Skills** sheet
2. Select `skill` and `count` (top 10 rows)
3. Insert → Horizontal Bar Chart
4. Title: "Top 10 Most Demanded Skills"

---

## Step 6 — Line Chart: Monthly Trend

1. Go to **Monthly_Trend** sheet
2. Select both columns
3. Insert → Line Chart
4. Title: "Job Postings by Month (2024)"

---

## Step 7 — Pivot Table: Salary by Experience

1. Go to **Cleaned_Data** sheet
2. Insert → PivotTable
3. Rows: `experience`
4. Values: `salary_lpa` → Average
5. Sort by Average Salary descending
6. Add a Bar Chart from this pivot

---

## Step 8 — Add Slicers (Filters)

1. Click any PivotTable
2. PivotTable Analyze → Insert Slicer
3. Add slicers for: `work_mode`, `location`, `employment_type`
4. These make the dashboard interactive

---

## Step 9 — Final Layout (Dashboard sheet)

Arrange in this order top-to-bottom:
```
[ KPI Cards — row of 6 boxes ]

[ Top Companies Bar ]  [ Work Mode Pie ]

[ Top Skills Bar ]     [ Monthly Trend Line ]

[ Salary by Experience Bar ]   [ Top Cities Bar ]
```

---

## Tips
- Use a dark background (dark gray/navy) for a modern look
- Remove gridlines: View → uncheck Gridlines
- Use consistent colors (blues + orange accent)
- Add a title at the very top: "Job Market Analytics Dashboard 2024"
