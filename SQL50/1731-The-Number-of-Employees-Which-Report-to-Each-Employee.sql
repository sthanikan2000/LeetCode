# Write your MySQL query statement below
select E.employee_id, E.name, R.reports_count, R.average_age
from Employees E
inner join (select reports_to, count(*) reports_count, round(avg(age),0) average_age
from Employees 
where reports_to is not null
group by reports_to) R
on E.employee_id = R.reports_to
order by E.employee_id
;