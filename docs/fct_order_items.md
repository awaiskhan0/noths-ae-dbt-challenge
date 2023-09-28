{% docs fct_order_items %}

This table contains a list of order items.

### Columns

I have included all columns from `stg_order_items` but have also included:

- `product_name`: Since each order item relates to a single product, it makes sense to add the product name. With this model, we can perform simple analyses such as top x products.
- `category_id`, `category_name`: With product_id, we can easily add category details such as name. We can then perform analyses such as top x categories as we can calculate how many products have sold within a category using product and order item data.
- `order_item_total`: This column calculates the total amount for the order item whilst taking into consideration whether the product was on sale or not at the time of order. This is done using the `snapshot_product` model, which tracks changes to `snapshot_product.on_sale`. We can then aggregate this within an order and compare to `fct_orders.order_total` to test that `order_total` is discounted if it needs to be.

### Joins

- `left join products`: We want all order items to show regardless of whether it has a product. I assume that an order should have a product, in which case `product_id` will fail testing if `null`.
- `left join categories`: We want all products (within `fct_order_items`) to show regardless of whether it has a category. I assume that a product should have a category, in which case `category_id` will fail testing if `null`.

{% enddocs %}
