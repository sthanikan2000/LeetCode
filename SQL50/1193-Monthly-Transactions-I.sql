# Write your MySQL query statement below
select DATE_FORMAT(trans_date,'%Y-%m') month, 
        country, 
        count(*) trans_count, 
        SUM(state="approved") approved_count,
        SUM(amount) trans_total_amount,
        SUM(IF(state="approved",amount,0)) approved_total_amount

from Transactions group by month,country;