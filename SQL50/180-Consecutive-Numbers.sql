# Write your MySQL query statement below
select distinct(L1.num) ConsecutiveNums
from Logs L1, Logs L2, Logs L3
where L1.id = L2.id - 1 and L1.id = L3.id - 2 and L1.num = L2.num and L1.num=L3.num;