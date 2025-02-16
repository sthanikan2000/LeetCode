# Write your MySQL query statement below
-- select x,y,z, IF(x+y>z and y+z>x and z+x>y, \Yes\, \No\) triangle
-- from Triangle;

#CASE WHEN
-- CASE
--     WHEN condition1 THEN result1
--     WHEN condition2 THEN result2
--     WHEN conditionN THEN resultN
--     ELSE result
-- END;
select *,
CASE 
    WHEN x+y>z and x+z>y and y+z>x THEN 'Yes'
    ELSE 'No'
END triangle
from Triangle;