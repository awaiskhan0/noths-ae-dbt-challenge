{% docs fct_emails %}

This table contains a list of emails sent to customers.

### Columns

I have included all columns from `stg_emails` but have also included:

- `customers_full_name`: Easily identify the customer who made the order and perform simple analyses such as top x customers.
- `last_sent_email_id`: This gives the ID of the last email that was sent to the same customer. Using `lag()` is a simple way of accessing previous rows within a given partition.

### Joins

- `left join customers`: We want all emails to show regardless of whether it has a customer. I assume that an email should have a customer, in which case `customer_id` will fail testing if `null`.

{% enddocs %}
