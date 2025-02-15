# Write your MySQL query statement below
select S.product_id, S.year first_year, S.quantity, S.price 
from Sales S
where (S.product_id, S.year) in
(
    select product_id, MIN(year) first_year
    from Sales 
    group by product_id
)
;