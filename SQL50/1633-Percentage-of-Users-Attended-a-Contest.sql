# Write your MySQL query statement below
select contest_id, ROUND(AVG(IF(DU.user_id=R.user_id,1,0))*100,2) percentage
from (select distinct(contest_id) contest_id from Register) DC 
cross join (select distinct(user_id) user_id from Users) DU
left join Register R using(contest_id,user_id)
group by contest_id
order by percentage desc, contest_id asc
;