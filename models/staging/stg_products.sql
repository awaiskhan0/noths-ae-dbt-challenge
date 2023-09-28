{{
  config (
      unique_key='id',
      cluster_by=['created_at']
      )
}}

with source as (
  select * from {{ ref('products') }}
),

renamed as (
  select
    id,
    created_at,
    updated_at,
    name,
    description,
    price,
    sale_price,
    in_stock,
    on_sale,
    category_id

  from source
)

select * from renamed
