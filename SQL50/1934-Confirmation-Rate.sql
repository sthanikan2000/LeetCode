# Write your MySQL query statement below
-- (select user_id, count(*) confirmed from Confirmations where action="confirmed" group by user_id) C1;
-- select S.user_id, count(C.id) Total from Signups S left join Confirmations C using(user_id);
-- select user_id, action, count(*) confirmed from Confirmations group by user_id,action;
Select S.user_id, round(IF(confirmation_rate is null, 0, confirmation_rate),2) confirmation_rate 
from Signups S left join (
select user_id, (IF(confirmed is null,0,confirmed) / requests) confirmation_rate from
(select user_id, count(*) confirmed from Confirmations where action="confirmed" group by user_id) C
right join
(select user_id, count(*) requests from Confirmations  group by user_id) R
using (user_id)
) CR using (user_id);

