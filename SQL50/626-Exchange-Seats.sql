# Write your MySQL query statement below
select * from
(
    select S1.id, IFNULL(S2.student,S1.student) student
    from Seat S1 left join Seat S2 
    on S1.id+1 = S2.id
    where S1.id%2=1
    UNION
    select S1.id, S2.student
    from Seat S1 left join Seat S2
    on S1.id-1=S2.id
    where S1.id%2=0
) S
order by id
;