-- # Write your MySQL query statement below
-- select employee_id from Employees where salary<30000 and manager_id not in (select distinct(employee_id) from Employees) order by employee_id; 

# No need of distinct, because employee_id is the primary key
select employee_id from Employees where salary<30000 and manager_id not in (select employee_id from Employees) order by employee_id; 