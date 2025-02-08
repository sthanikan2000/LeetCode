# Write your MySQL query statement below
select S.machine_id, ROUND(avg(E.timestamp - S.timestamp),3) as processing_time from Activity S, Activity E 
where S.machine_id = E.machine_id and S.process_id = E.process_id 
    and S.activity_type ="start" and E.activity_type="end" group by machine_id;