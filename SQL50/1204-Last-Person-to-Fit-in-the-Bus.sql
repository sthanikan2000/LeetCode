# Write your MySQL query statement below
select person_name from (
select *, (SUM(weight) over (order by turn)) cs from Queue order by turn) T
where cs <=1000 order by cs desc limit 1; 