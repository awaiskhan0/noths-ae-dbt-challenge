-- 3. Who are our top 10 most loyal customers?

select 
  customer_full_name,
  count(order_id) as order_count

from {{ ref('fct_orders') }}
group by customer_full_name
order by order_count desc
limit 10
