# Write your MySQL query statement below
#### Wrong code
-- select category, count(*) accounts_count from
--    (
--         select account_id,
--         CASE
--             WHEN income<20000 THEN "Low Salary"
--             WHEN 20000<=income and income<=50000 THEN "Average Salary"
--             ELSE "High Salary"
--         END category
--         from Accounts
--     ) sub_query
-- group by category
-- ;

select "Low Salary" category, sum(IF(income<20000,1,0)) accounts_count from Accounts
union
select "Average Salary" category, sum(IF(income>=20000 and income<=50000,1,0)) accounts_count from Accounts
union
select "High Salary" category, sum(IF(income>50000,1,0)) accounts_count from Accounts
;
