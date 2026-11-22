-- sales employees
SELECT e.first_name, e.last_name, d.department_name
FROM employees e
JOIN departments d ON e.department_id = d.department_id
WHERE d.department_name = 'Sales'
ORDER BY e.employee_id;

-- marketing projects
SELECT p.project_name, d.department_name
FROM projects p
JOIN department_projects dp ON p.project_id = dp.project_id
JOIN departments d ON dp.department_id = d.department_id
WHERE d.department_name = 'Marketing'
ORDER BY p.project_name;

-- projects over 100000
-- budget, not estimated_cost
SELECT project_name, budget
FROM projects
WHERE budget > 100000
ORDER BY project_name;

-- who works on project A
-- "Big Project" is not in the data
SELECT e.first_name, e.last_name, p.project_name
FROM employees e
JOIN employee_projects ep ON e.employee_id = ep.employee_id
JOIN projects p ON ep.project_id = p.project_id
WHERE p.project_name = 'Project A'
ORDER BY e.employee_id;

-- employees per job
SELECT j.job_title, COUNT(*) AS num_employees
FROM employees e
JOIN jobs j ON e.job_id = j.job_id
GROUP BY j.job_title
ORDER BY num_employees DESC, j.job_title;

-- employees and departments
SELECT e.employee_id, e.first_name, e.last_name, d.department_name
FROM employees e
INNER JOIN departments d ON e.department_id = d.department_id
ORDER BY e.employee_id;

-- departments and locations
SELECT d.department_name, l.city, l.state_province
FROM departments d
INNER JOIN location l ON d.location_id = l.location_id
ORDER BY d.department_id;

-- projects and departments
SELECT p.project_id, p.project_name, d.department_name
FROM projects p
INNER JOIN department_projects dp ON p.project_id = dp.project_id
INNER JOIN departments d ON dp.department_id = d.department_id
ORDER BY p.project_id, d.department_id;

-- employees and projects
SELECT e.first_name, e.last_name, p.project_name
FROM employees e
INNER JOIN employee_projects ep ON e.employee_id = ep.employee_id
INNER JOIN projects p ON ep.project_id = p.project_id
ORDER BY e.employee_id, p.project_id;

-- employees, jobs and salaries
-- salary is on employees
SELECT e.first_name, e.last_name, j.job_title, e.salary
FROM employees e
INNER JOIN jobs j ON e.job_id = j.job_id
ORDER BY e.employee_id;
