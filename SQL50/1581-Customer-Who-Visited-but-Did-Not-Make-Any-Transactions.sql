# Write your MySQL query statement below

#####    Ccustomer id vs count of their transactions
-- select V.customer_id, A.count_no_trans from 
-- (select visit_id, count(transaction_id) as count_no_trans from transactions group by visit_id) as A
-- inner join visits as V on A.visit_id = V.visit_id;


#### Customer_id vs no of visits without any transactions
select customer_id, count(visit_id) count_no_trans from visits where visit_id not in (select distinct(visit_id) from transactions) group by customer_id;