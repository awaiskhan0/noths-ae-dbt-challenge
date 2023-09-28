-- 5. Have we sent any emails to someone who is unsubscribed?

select count(distinct customer_id) as customer_count 
from {{ ref('fct_emails') }}
where email_marketing_status = 'opted_out'
