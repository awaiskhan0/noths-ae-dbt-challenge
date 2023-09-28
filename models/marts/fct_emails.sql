{{
  config (
      unique_key='email_id',
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
        customers.email_marketing_status,
        emails.sent_date,
        emails.subject,
        emails.opened,
        emails.clicked,
        nullif(
            lag(emails.id, 1, 0) over (
                partition by emails.customer_id
                order by emails.sent_date asc
            ),
            0
        ) as last_sent_email_id
    
    from emails
    left join customers
        on emails.customer_id = customers.id
)

select
    email_id,
    sent_date,
    customer_id,
    customer_full_name,
    email_marketing_status,
    last_sent_email_id,
    subject,
    opened,
    clicked

from final
