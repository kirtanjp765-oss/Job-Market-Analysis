-- ============================================================
-- Job Market Analytics — Advanced SQL Practice
-- Covers: JOINS, Subqueries, CTEs, Window Functions
-- ============================================================

USE job_market;

-- ── 1. CTE — Running total of jobs per month ─────────────────
WITH monthly AS (
    SELECT
        month_posted,
        COUNT(*) AS monthly_count
    FROM jobs
    GROUP BY month_posted
)
SELECT
    month_posted,
    monthly_count,
    SUM(monthly_count) OVER (ORDER BY month_posted) AS running_total
FROM monthly
ORDER BY month_posted;


-- ── 2. Window Function — Rank companies by job count ─────────
SELECT
    company,
    COUNT(*) AS job_count,
    RANK() OVER (ORDER BY COUNT(*) DESC) AS rank_position
FROM jobs
GROUP BY company;


-- ── 3. Subquery — Jobs at companies with > avg job count ──────
SELECT *
FROM jobs
WHERE company IN (
    SELECT company
    FROM jobs
    GROUP BY company
    HAVING COUNT(*) > (SELECT AVG(cnt) FROM (SELECT COUNT(*) AS cnt FROM jobs GROUP BY company) sub)
);


-- ── 4. CTE — Top skill per city (approximation) ───────────────
-- Note: Full skill parsing is better done in Python.
-- This shows which cities mention 'Python' most.
SELECT
    location,
    COUNT(*) AS python_jobs
FROM jobs
WHERE skills LIKE '%Python%'
GROUP BY location
ORDER BY python_jobs DESC;


-- ── 5. Salary percentile using NTILE ─────────────────────────
SELECT
    job_title,
    salary_lpa,
    NTILE(4) OVER (ORDER BY salary_lpa) AS salary_quartile
FROM jobs
WHERE salary_lpa IS NOT NULL
ORDER BY salary_lpa DESC
LIMIT 50;


-- ── 6. Self-join style — compare each company to overall avg ──
SELECT
    j.company,
    ROUND(AVG(j.salary_lpa), 2)                        AS company_avg,
    ROUND((SELECT AVG(salary_lpa) FROM jobs), 2)       AS overall_avg,
    ROUND(AVG(j.salary_lpa) - (SELECT AVG(salary_lpa) FROM jobs), 2) AS difference
FROM jobs j
GROUP BY j.company
ORDER BY difference DESC;


-- ── 7. HAVING — Cities with more than 200 postings ───────────
SELECT
    location,
    COUNT(*) AS total
FROM jobs
GROUP BY location
HAVING total > 200
ORDER BY total DESC;


-- ── 8. CASE WHEN — Label salary tiers inline ─────────────────
SELECT
    job_title,
    experience,
    salary_lpa,
    CASE
        WHEN salary_lpa >= 15 THEN 'High'
        WHEN salary_lpa >= 8  THEN 'Medium'
        ELSE 'Entry'
    END AS salary_tier
FROM jobs
WHERE salary_lpa IS NOT NULL
ORDER BY salary_lpa DESC
LIMIT 20;
