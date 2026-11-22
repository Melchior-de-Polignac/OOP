-- Company database, SQLite dialect.
-- sqlite3 company.db < schema.sql
-- sqlite3 company.db < data.sql

CREATE TABLE location (
    location_id    INTEGER PRIMARY KEY,
    address        TEXT,
    city           TEXT NOT NULL,
    state_province TEXT,
    country        TEXT NOT NULL,
    postal_code    TEXT
);

CREATE TABLE jobs (
    job_id     INTEGER PRIMARY KEY,
    job_title  TEXT NOT NULL UNIQUE,
    min_salary NUMERIC NOT NULL,
    max_salary NUMERIC NOT NULL,
    CHECK (min_salary >= 0 AND min_salary <= max_salary)
);

CREATE TABLE departments (
    department_id   INTEGER PRIMARY KEY,
    department_name TEXT NOT NULL UNIQUE,
    manager_id      INTEGER REFERENCES employees (employee_id),
    location_id     INTEGER REFERENCES location (location_id)
);

CREATE TABLE employees (
    employee_id    INTEGER PRIMARY KEY,
    first_name     TEXT NOT NULL,
    last_name      TEXT NOT NULL,
    email          TEXT NOT NULL UNIQUE,
    phone          TEXT,
    hire_date      TEXT NOT NULL,
    salary         NUMERIC NOT NULL CHECK (salary >= 0),
    commission_pct NUMERIC,
    manager_id     INTEGER REFERENCES employees (employee_id),
    department_id  INTEGER REFERENCES departments (department_id),
    job_id         INTEGER REFERENCES jobs (job_id),
    location_id    INTEGER REFERENCES location (location_id)
);

CREATE TABLE projects (
    project_id   INTEGER PRIMARY KEY,
    project_name TEXT NOT NULL UNIQUE,
    start_date   TEXT,
    end_date     TEXT,
    budget       NUMERIC CHECK (budget >= 0),
    CHECK (end_date IS NULL OR start_date IS NULL OR end_date >= start_date)
);

CREATE TABLE department_projects (
    department_id INTEGER NOT NULL REFERENCES departments (department_id),
    project_id    INTEGER NOT NULL REFERENCES projects (project_id),
    PRIMARY KEY (department_id, project_id)
);

CREATE TABLE employee_projects (
    employee_id  INTEGER NOT NULL REFERENCES employees (employee_id),
    project_id   INTEGER NOT NULL REFERENCES projects (project_id),
    start_date   TEXT,
    end_date     TEXT,
    hours_worked NUMERIC,
    PRIMARY KEY (employee_id, project_id)
);
