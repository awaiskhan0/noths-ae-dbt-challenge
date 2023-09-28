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

snapshot_products as (
    select * from {{ ref('snapshot_products') }}
),

order_item_on_sale as (
    select
        order_items.id as order_item_id,
        snapshot_products.on_sale
    
    from order_items
    left join snapshot_products
        on order_items.product_id = snapshot_products.id
    
    where order_items.created_at >= snapshot_products.updated_at

    qualify row_number() over (
        partition by order_item_id
        order by snapshot_products.updated_at desc
    ) = 1
),

final as (
    select
        order_items.id as order_item_id,
        order_items.created_at as order_item_created_at,
        order_items.updated_at as order_item_updated_at,
        order_items.order_id,
        order_items.product_id,
        order_items.quantity,
        order_items.quantity * iff(
            order_item_on_sale.on_sale, 
            products.sale_price,
            products.price
        ) as order_item_total,
        order_item_on_sale.on_sale,
        products.name as product_name,
        categories.id as category_id,
        categories.name as category_name
    
    from order_items
    left join products
        on order_items.product_id = products.id
    left join categories
        on products.category_id = categories.id
    left join order_item_on_sale
        on order_items.id = order_item_on_sale.order_item_id
)

select
    order_item_id,
    order_item_created_at,
    order_item_updated_at,
    order_id,
    product_id,
    product_name,
    category_id,
    category_name,
    quantity,
    order_item_total,
    on_sale

from final
