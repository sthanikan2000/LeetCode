# Write your MySQL query statement below
select product_id, IFNULL(average_price,0) average_price from
(select distinct(product_id) product_id from Prices) DI Left join
(
    select P.product_id, Round(SUM(P.price*US.units)/SUM(US.units),2) average_price 
    from UnitsSold US inner join Prices P 
    on P.product_id = US.product_id and US.purchase_date >= P.start_date and US.purchase_date<=P.end_date
    group by product_id
) P
using(product_id)
;