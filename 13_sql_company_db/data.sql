INSERT INTO location (city, state_province, country) VALUES
    ('New York', 'NY', 'USA'),
    ('Los Angeles', 'CA', 'USA'),
    ('San Francisco', 'CA', 'USA'),
    ('Chicago', 'IL', 'USA'),
    ('Houston', 'TX', 'USA'),
    ('London', NULL, 'England'),
    ('Paris', NULL, 'France'),
    ('Berlin', NULL, 'Germany'),
    ('Sydney', NULL, 'Australia'),
    ('Tokyo', NULL, 'Japan');

INSERT INTO jobs (job_title, min_salary, max_salary) VALUES
    ('Manager', 70000, 120000),
    ('Salesperson', 20000, 40000),
    ('Developer', 50000, 100000),
    ('Accountant', 35000, 60000),
    ('HR Manager', 45000, 80000),
    ('Marketing Specialist', 40000, 75000),
    ('Administrative Assistant', 25000, 35000),
    ('Designer', 45000, 80000),
    ('Writer', 30000, 50000),
    ('Engineer', 55000, 90000);

INSERT INTO departments (department_name, manager_id, location_id) VALUES
    ('Engineering', NULL, 1),
    ('Marketing', NULL, 2),
    ('Sales', NULL, 3),
    ('Finance', NULL, 4),
    ('HR', NULL, 5);

INSERT INTO employees
    (first_name, last_name, email, phone, hire_date, job_id, salary, manager_id, department_id)
VALUES
    ('John', 'Doe', 'johndoe@example.com', '555-555-1234', '2022-01-01', 1, 50000, NULL, 1),
    ('Jane', 'Doe', 'janedoe@example.com', '555-555-5678', '2022-01-01', 2, 60000, 1, 1),
    ('Bob', 'Smith', 'bobsmith@example.com', '555-555-9012', '2022-02-01', 3, 75000, 2, 2),
    ('Alice', 'Johnson', 'alicejohnson@example.com', '555-555-3456', '2022-02-01', 4, 85000, 2, 2),
    ('Mark', 'Lee', 'marklee@example.com', '555-555-7890', '2022-03-01', 5, 95000, 2, 3),
    ('Emily', 'Chen', 'emilychen@example.com', '555-555-2345', '2022-03-01', 5, 80000, 2, 3),
    ('Sara', 'Kim', 'sarakim@example.com', '555-555-6789', '2022-04-01', 6, 70000, 3, 4),
    ('Michael', 'Wu', 'michaelwu@example.com', '555-555-0123', '2022-04-01', 7, 65000, 3, 4),
    ('David', 'Nguyen', 'davidnguyen@example.com', '555-555-4567', '2022-05-01', 8, 55000, 4, 5),
    ('Jennifer', 'Garcia', 'jennifergarcia@example.com', '555-555-8901', '2022-05-01', 9, 60000, 4, 5);

UPDATE departments SET manager_id = 1 WHERE department_id = 1;
UPDATE departments SET manager_id = 2 WHERE department_id = 2;
UPDATE departments SET manager_id = 3 WHERE department_id = 3;
UPDATE departments SET manager_id = 4 WHERE department_id = 4;
UPDATE departments SET manager_id = 5 WHERE department_id = 5;

INSERT INTO projects (project_name, start_date, end_date, budget) VALUES
    ('Project A', '2022-01-01', '2022-03-01', 50000),
    ('Project B', '2022-02-01', '2022-05-01', 120000),
    ('Project C', '2022-03-01', '2022-06-01', 200000),
    ('Project D', '2022-04-01', '2022-07-01', 80000);

INSERT OR IGNORE INTO department_projects (department_id, project_id) VALUES
    (1, 1), (1, 2), (2, 3), (3, 4),
    (1, 1), (1, 2), (2, 1), (2, 3), (3, 2), (3, 3), (4, 1), (4, 2), (5, 1), (5, 3);

INSERT INTO employee_projects (employee_id, project_id, start_date, end_date) VALUES
    (1, 1, '2021-01-01', '2021-06-30'),
    (1, 2, '2021-07-01', '2021-12-31'),
    (2, 1, '2021-01-01', '2021-06-30'),
    (2, 3, '2021-07-01', '2021-12-31'),
    (3, 2, '2021-01-01', '2021-06-30'),
    (3, 3, '2021-07-01', '2021-12-31'),
    (4, 2, '2021-01-01', '2021-06-30'),
    (4, 1, '2021-07-01', '2021-12-31'),
    (5, 3, '2021-01-01', '2021-06-30'),
    (5, 1, '2021-07-01', '2021-12-31');
