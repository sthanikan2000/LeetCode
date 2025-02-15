# Write your MySQL query statement below
select activity_date day, count(distinct(user_id)) active_users
from Activity 
group by activity_date
having activity_date between "2019-06-28" and "2019-07-27" # between operator is inclusive 
;