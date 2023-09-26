{{
  config (
      materialized='ephemeral',
      unique_key='id',
      )
}}

select
    id,
    created_at,
    updated_at,
    name
    
from {{ ref('customers') }}
