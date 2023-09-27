{{
  config (
      materialized='view',
      unique_key='id',
      )
}}

select
    id,
    created_at,
    updated_at,
    concat(first_name, ' ', last_name) as full_name,
    first_name,
    last_name,
    email,
    address,
    city,
    post_code,
    email_marketing_status

from {{ ref('customers') }}
