# Write your MySQL query statement below
select P.project_id, ROUND(AVG(E.experience_years),2) average_years
from Project P inner join Employee E using(employee_id) group by project_id;