{{
  config (
      unique_key='order_id',
      )
}}

with orders as (
    select * from {{ ref('stg_orders') }}
),

customers as (
    select * from {{ ref('stg_customers') }}
),

refunds as (
    select * from {{ ref('stg_refunds') }}
),

final as (
    select
        orders.id as order_id,
        orders.created_at as order_created_at,
        orders.updated_at as order_updated_at,
        orders.order_total,
        orders.order_status,
        orders.payment_method,
        orders.customer_id,
        full_name as customer_full_name,
        refunds.id as refund_id,
        refunds.created_at as refund_created_at,
        refunds.amount_refunded

    from orders
    left join customers
        on orders.customer_id = customers.id
    left join refunds
        on orders.id = refunds.order_id
)

select
    order_id,
    customer_id,
    refund_id,

    order_created_at,
    order_updated_at,
    refund_created_at,

    order_total,
    amount_refunded,
    
    payment_method,
    order_status,
    customer_full_name

from final
