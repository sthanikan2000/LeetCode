# Write your MySQL query statement below
select S1.id,
CASE 
    WHEN S1.id%2=1 and S2.id is null THEN S1.student
    WHEN S1.id%2=1 THEN S2.student
    ELSE S3.student
END student
from Seat S1 
left join Seat S2 on S1.id+1=S2.id 
left join Seat S3 on S1.id-1=S3.id
order by id;

## Using UNION
-- select * from
-- (
--     select S1.id, IFNULL(S2.student,S1.student) student
--     from Seat S1 left join Seat S2 
--     on S1.id+1 = S2.id
--     where S1.id%2=1
--     UNION
--     select S1.id, S2.student
--     from Seat S1 left join Seat S2
--     on S1.id-1=S2.id
--     where S1.id%2=0
-- ) S
-- order by id;