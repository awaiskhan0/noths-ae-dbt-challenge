{{
  config (
      unique_key='id',
      cluster_by=['created_at']
      )
}}

with source as (
  select * from {{ ref('refunds') }}
),

renamed as (
  select
    id,
    created_at,
    updated_at,
    order_id,
    amount_refunded,
    refund_reason

  from source
)

select * from renamed
