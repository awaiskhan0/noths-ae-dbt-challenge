-- test to check if order total in fct_orders is correctly discounted if on sale
-- order_item_total in fct_order_items is calculated to include discount when
-- available 
-- the sum of order_item_total within an order is then compared to order_total
-- if different, it means the discount has not been applied

-- the logic of order_item_total relies on snapshot_products which is reliant on
-- the timestamp fields
-- we need to compared updated times in snapshot_products and created times in
-- fct_order_items (which should have the same created time as the order it comes
-- from)
-- since we are using dummy data (in particular, using fake timestamps), the test
-- won't provide accurate results


select
    orders.order_id,
    orders.order_total,
    sum(order_items.order_item_total) as sum_of_order_item_total

from {{ ref('fct_orders') }} as orders
inner join {{ ref('fct_order_items') }} as order_items
    on orders.order_id = order_items.order_id

group by orders.order_id,
    orders.order_total

having not(orders.order_total = sum_of_order_item_total)
