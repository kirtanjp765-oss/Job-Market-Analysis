-- Job Market Analytics — Database Setup

CREATE DATABASE IF NOT EXISTS job_market;
USE job_market;

-- Drop if re-running
DROP TABLE IF EXISTS jobs;

CREATE TABLE jobs (
    job_id          INT PRIMARY KEY,
    job_title       VARCHAR(100)   NOT NULL,
    company         VARCHAR(100)   NOT NULL,
    location        VARCHAR(100)   NOT NULL,
    work_mode       VARCHAR(20),
    experience      VARCHAR(30),
    employment_type VARCHAR(30),
    skills          TEXT,
    date_posted     DATE,
    month_posted    VARCHAR(10),
    salary_lpa      DECIMAL(5,1),
    exp_level_num   TINYINT
);

-- After creating the table, import cleaned_data/cleaned_jobs.csv
-- using MySQL Workbench: Table → Import Wizard → choose the CSV file

