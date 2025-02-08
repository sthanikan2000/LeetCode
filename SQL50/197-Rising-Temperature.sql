# Write your MySQL query statement below
#### Group  current and previous day
-- select CD.id as CD_id, CD.temperature, PD.id as pd_id, PD.temperature from Weather as CD, Weather as PD where CD.recordDate = DATE_ADD(PD.recordDate,INTERVAL 1 DAY);


### Selection Criteria
-- select CD.id as CD_id, CD.temperature, PD.id as pd_id, PD.temperature from Weather as CD, Weather as PD where CD.recordDate = DATE_ADD(PD.recordDate,INTERVAL 1 DAY);

### Solution
select CD.id as Id 
    from Weather as CD, Weather as PD 
        where CD.recordDate = DATE_ADD(PD.recordDate,INTERVAL 1 DAY) 
            and CD.temperature>PD.temperature;