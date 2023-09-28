-- 2. Which month do we make the most money?

select 
    monthname(order_created_at) as month, 
    sum(order_total) as order_count

from {{ ref('fct_orders' )}} 
group by month
order by order_count desc
limit 1
