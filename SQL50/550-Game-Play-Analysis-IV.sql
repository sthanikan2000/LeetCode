# Write your MySQL query statement below
### Time limit exceeded
-- select  ROUND(SUM(
--             (player_id,event_date) in (
--                 select player_id, DATE_ADD(MIN(event_date), INTERVAL 1 DAY) next_day
--                 from Activity 
--                 group by player_id
--             )
--         )/count(distinct(player_id))
--         ,2) fraction

-- from Activity
-- ;


#from Solutions at discussion
-- SELECT
--   ROUND(COUNT(DISTINCT player_id) / (SELECT COUNT(DISTINCT player_id) FROM Activity), 2) AS fraction
-- FROM
--   Activity
-- WHERE
--   (player_id, DATE_SUB(event_date, INTERVAL 1 DAY))
--   IN (
--     SELECT player_id, MIN(event_date) AS first_login FROM Activity GROUP BY player_id
--   );

-- # My first passed solution
select ROUND(AVG(X.player_id=A.player_id and A.player_id is not null),2) fraction
from (
        select player_id,MIN(event_date) first_play, DATE_ADD(MIN(event_date), INTERVAL 1 DAY) next_day
        from Activity 
        group by player_id
    ) X
left join Activity A
on A.player_id = X.player_id and A.event_date = X.next_day
;