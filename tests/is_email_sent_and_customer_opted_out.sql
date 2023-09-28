-- test to check if email is sent to customer whilst they are unsubscribed 
-- (or opted out)

-- to do this, we need to obtain the marketing email status of a customer
-- at the time when the email is sent
-- we can do this using snapshot_customers which tracks the marketing email
-- status of a customer
-- we need to compared updated times in snapshot_customers and sent times in
-- fct_emails
-- since we are using dummy data (in particular, using fake timestamps), the test
-- won't provide accurate results


select
    emails.email_id,
    emails.customer_id,
    snapshot_customers.email_marketing_status

from {{ ref('fct_emails') }} as emails
inner join {{ ref('snapshot_customers') }} as snapshot_customers
    on emails.customer_id = snapshot_customers.id

where emails.sent_date >= snapshot_customers.updated_at

qualify row_number() over (
    partition by email_id
    order by updated_at desc
) = 1
    and email_marketing_status = 'opted_out'
