-- 4. Which categories do we sell the most products in?

select 
  category_name,
  sum(quantity) as product_quantity
  
from {{ ref('fct_order_items') }}
group by category_name
order by product_quantity desc
limit 1
