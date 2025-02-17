# Write your MySQL query statement below
-- select distinct(product_id) product_id, IFNULL(CP.new_price,10) price
-- from Products P
-- left  join 
--     (select P.product_id, P.new_price
--     from Products P
--     inner join 
--         (select product_id,max(change_date) change_date
--         from Products
--         where change_date<="2019-08-16"
--         group by product_id) CD
--     on P.product_id=CD.product_id and P.change_date=CD.change_date) CP
-- using (product_id);


### Solution from discussion
select distinct product_id, 10 price from Products 
where product_id not in(select distinct product_id from Products where change_date <='2019-08-16' )

union 

select product_id, new_price price from Products 
where (product_id,change_date) in 
    (select product_id , max(change_date) date from Products where change_date <='2019-08-16' group by product_id)
;
