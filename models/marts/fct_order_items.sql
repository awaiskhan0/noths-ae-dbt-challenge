{{
  config (
      unique_key='order_item_id',
      )
}}

with order_items as (
    select * from {{ ref('stg_order_items') }}
),

products as (
    select * from {{ ref('stg_products') }}
),

categories as (
    select * from {{ ref('stg_categories') }}
),

final as (
    select
        order_items.id as order_item_id,
        order_items.created_at as order_item_created_at,
        order_items.updated_at as order_item_updated_at,
        order_items.order_id,
        order_items.product_id,
        order_items.quantity,
        products.name as product_name,
        categories.id as category_id,
        categories.name as category_name
    
    from order_items
    left join products
        on order_items.product_id = products.id
    left join categories
        on products.category_id = categories.id
)

select
    order_item_id,
    order_id,
    product_id,
    category_id,

    order_item_created_at,
    order_item_updated_at,

    quantity,

    product_name,
    category_name

from final
