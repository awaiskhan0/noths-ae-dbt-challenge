{% snapshot snapshot_products %}

{{
    config(
      unique_key='id',
      target_schema='NOTHS_SNAPSHOTS',

      strategy='timestamp',
      updated_at='updated_at',
    )
}}

select
    id,
    created_at,
    updated_at,
    on_sale

from {{ ref('stg_products') }}

{% endsnapshot %}
