# Write your MySQL query statement below
### FInding first order of each customer will solve this 
select ROUND(AVG(IF(D.order_date=D.customer_pref_delivery_date,100,0)),2) immediate_percentage
from (
    select customer_id, MIN(order_date) first_order
    from Delivery
    group by customer_id
) FO
inner join Delivery D 
on D.customer_id = FO.customer_id and D.order_date=FO.first_order
;