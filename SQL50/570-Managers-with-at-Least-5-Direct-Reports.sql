# Write your MySQL query statement below
-- select E.name from
-- (select managerId from Employee where managerId is not null group by managerID having count(managerId)>=5) as R 
-- inner join Employee E on R.managerId = E.id;
select M.name from employee E inner join Employee M on E.managerId=M.id group by M.id having count(*)>=5;
