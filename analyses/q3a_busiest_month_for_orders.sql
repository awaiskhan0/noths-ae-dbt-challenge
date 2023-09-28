-- 1. Which month is busiest for orders

select 
    monthname(order_created_at) as month, 
    count(order_id) as order_count

from {{ ref('fct_orders' )}} 
group by month
order by order_count desc
limit 1
