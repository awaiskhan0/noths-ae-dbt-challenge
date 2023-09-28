{% docs fct_orders %}

This table contains a list of orders.

### Columns

I have included all columns from `stg_orders` but have also included:

- `customers_full_name`: Easily identify the customer who made the order and perform simple analyses such as top x customers.
- `refund_id`, `refund_created_at`, `amount_refunded`: This gives a quick glance at related refund data if an order has been refunded. Users can also easily calculate the net amount gained from the order, and can perform time analyses.

### Joins

- `left join customers`: We want all orders to show regardless of whether it has a customer. I assume that an order should have a customer, in which case `customer_id` will fail testing if `null`.
- `left join refunds`: Not all orders will have refunds.

{% enddocs %}
