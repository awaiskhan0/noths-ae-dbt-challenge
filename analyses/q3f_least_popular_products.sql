-- 6. What is the least popular product?

select
  product_name,
  sum(quantity) as product_quantity

from {{ ref('fct_order_items')}} as products
group by product_name
qualify rank() over (order by product_quantity asc) = 1
order by product_name asc
