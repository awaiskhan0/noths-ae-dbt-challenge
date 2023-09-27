{{
  config (
      unique_key='order_item_id',
      )
}}

with emails as (
    select * from {{ ref('stg_emails') }}
),

customers as (

    select * from {{ ref('stg_customers') }}
),

final as (
    select
        emails.id as email_id,
        emails.customer_id,
        customers.full_name as customer_full_name,
        emails.sent_date,
        emails.subject,
        emails.opened,
        emails.clicked,
        lag(emails.id, 1, 0) over (
            partition by emails.customer_id
            order by emails.sent_date asc
        ) as last_sent_email_id
    
    from emails
    left join customers
        on emails.customer_id = customers.id
)

select
    email_id,
    last_sent_email_id,
    customer_id,

    sent_date,

    customer_full_name,
    subject,
    opened,
    clicked

from final
