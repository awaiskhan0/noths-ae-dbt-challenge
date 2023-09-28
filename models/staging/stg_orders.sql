{{
  config (
      unique_key='id',
      cluster_by=['created_at']
      )
}}


with source as (
  select * from {{ ref('orders') }}
),

renamed as (
  select
    id,
    created_at,
    updated_at,
    customer_id,
    order_total,
    payment_method,
    order_status

  from source
)

select * from renamed
