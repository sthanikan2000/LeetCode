# Write your MySQL query statement below
-- Select S.user_id, round(IF(confirmation_rate is null, 0, confirmation_rate),2) confirmation_rate 
-- from Signups S left join (
-- select user_id, (IF(confirmed is null,0,confirmed) / requests) confirmation_rate from
-- (select user_id, count(*) confirmed from Confirmations where action="confirmed" group by user_id) C
-- right join
-- (select user_id, count(*) requests from Confirmations  group by user_id) R
-- using (user_id)
-- ) CR using (user_id);


SELECT A.user_id, 
       ROUND(IFNULL(AVG(action = 'confirmed'), 0), 2) AS confirmation_rate
       # SQL treats boolean expression as 1(true) and 0(false)
FROM Signups AS A
LEFT JOIN Confirmations AS B ON A.user_id = B.user_id
GROUP BY A.user_id;
