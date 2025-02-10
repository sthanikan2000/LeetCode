# Write your MySQL query statement below
-- select product_id, IFNULL(average_price,0) average_price from
-- (select distinct(product_id) product_id from Prices) DI Left join
-- (
--     select P.product_id, Round(SUM(P.price*US.units)/SUM(US.units),2) average_price 
--     from UnitsSold US inner join Prices P 
--     on P.product_id = US.product_id and US.purchase_date >= P.start_date and US.purchase_date<=P.end_date
--     group by product_id
-- ) P
-- using(product_id)
-- ;

SELECT p.product_id, IFNULL(ROUND(SUM(units*price)/SUM(units),2),0) AS average_price
FROM Prices p LEFT JOIN UnitsSold u
ON p.product_id = u.product_id AND
u.purchase_date BETWEEN start_date AND end_date
group by product_id
;