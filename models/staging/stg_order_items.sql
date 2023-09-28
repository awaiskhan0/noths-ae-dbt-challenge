{{
  config (
      unique_key='id',
      )
}}

select
    id,
    created_at,
    updated_at,
    order_id,
    product_id,
    quantity

from {{ ref('order_items') }}
