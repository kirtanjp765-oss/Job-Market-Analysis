-- Job Market Analytics — Analysis Queries
-- Run after importing data into the jobs table

USE job_market;

-- ── Q1: Which companies hire the most? ───────────────────────
SELECT
    company,
    COUNT(*) AS job_count
FROM jobs
GROUP BY company
ORDER BY job_count DESC
LIMIT 10;


-- ── Q2: Which cities have the most jobs? ─────────────────────
SELECT
    location,
    COUNT(*) AS job_count
FROM jobs
GROUP BY location
ORDER BY job_count DESC;


-- ── Q3: Average salary by city ───────────────────────────────
SELECT
    location,
    ROUND(AVG(salary_lpa), 2) AS avg_salary_lpa,
    COUNT(*)                  AS total_jobs
FROM jobs
WHERE salary_lpa IS NOT NULL
GROUP BY location
ORDER BY avg_salary_lpa DESC;


-- ── Q4: Average salary by company (top 10) ───────────────────
SELECT
    company,
    ROUND(AVG(salary_lpa), 2) AS avg_salary_lpa,
    COUNT(*)                  AS total_jobs
FROM jobs
WHERE salary_lpa IS NOT NULL
GROUP BY company
ORDER BY avg_salary_lpa DESC
LIMIT 10;


-- ── Q5: Fresher vs Experienced jobs ──────────────────────────
SELECT
    experience,
    COUNT(*)                                AS job_count,
    ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER (), 1) AS pct_share
FROM jobs
GROUP BY experience
ORDER BY exp_level_num;


-- ── Q6: Remote vs Hybrid vs On-site breakdown ────────────────
SELECT
    work_mode,
    COUNT(*)                                AS job_count,
    ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER (), 1) AS pct_share
FROM jobs
GROUP BY work_mode
ORDER BY job_count DESC;


-- ── Q7: Highest paying job titles ────────────────────────────
SELECT
    job_title,
    ROUND(AVG(salary_lpa), 2) AS avg_salary_lpa,
    MIN(salary_lpa)           AS min_salary,
    MAX(salary_lpa)           AS max_salary,
    COUNT(*)                  AS postings
FROM jobs
WHERE salary_lpa IS NOT NULL
GROUP BY job_title
ORDER BY avg_salary_lpa DESC;


-- ── Q8: Most common experience requirement ───────────────────
SELECT
    experience,
    COUNT(*) AS count
FROM jobs
GROUP BY experience
ORDER BY count DESC;


-- ── Q9: Employment type distribution ─────────────────────────
SELECT
    employment_type,
    COUNT(*) AS job_count
FROM jobs
GROUP BY employment_type
ORDER BY job_count DESC;


-- ── Q10: Monthly hiring trend ────────────────────────────────
SELECT
    month_posted,
    COUNT(*) AS job_count
FROM jobs
GROUP BY month_posted
ORDER BY month_posted;


-- ── Q11: Salary ranges — how many jobs fall in each bracket ──
SELECT
    CASE
        WHEN salary_lpa < 5          THEN 'Below 5 LPA'
        WHEN salary_lpa BETWEEN 5 AND 9.9  THEN '5 – 10 LPA'
        WHEN salary_lpa BETWEEN 10 AND 14.9 THEN '10 – 15 LPA'
        WHEN salary_lpa BETWEEN 15 AND 19.9 THEN '15 – 20 LPA'
        ELSE 'Above 20 LPA'
    END AS salary_bracket,
    COUNT(*) AS job_count
FROM jobs
WHERE salary_lpa IS NOT NULL
GROUP BY salary_bracket
ORDER BY MIN(salary_lpa);


-- ── Q12: Top cities for freshers ─────────────────────────────
SELECT
    location,
    COUNT(*) AS fresher_jobs
FROM jobs
WHERE experience = 'Fresher (0-1 yr)'
GROUP BY location
ORDER BY fresher_jobs DESC
LIMIT 5;


-- ── Q13: Remote jobs — which companies offer them? ───────────
SELECT
    company,
    COUNT(*) AS remote_count
FROM jobs
WHERE work_mode = 'Remote'
GROUP BY company
ORDER BY remote_count DESC
LIMIT 10;


-- ── Q14: Companies with above-average salary ─────────────────
SELECT
    company,
    ROUND(AVG(salary_lpa), 2) AS avg_salary
FROM jobs
GROUP BY company
HAVING avg_salary > (SELECT AVG(salary_lpa) FROM jobs)
ORDER BY avg_salary DESC;


-- ── Q15: Jobs posted in Q1 2024 (Jan–Mar) ───────────────────
SELECT
    month_posted,
    COUNT(*) AS job_count
FROM jobs
WHERE date_posted BETWEEN '2024-01-01' AND '2024-03-31'
GROUP BY month_posted
ORDER BY month_posted;
