{% snapshot snapshot_customers %}

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
    email_marketing_status

from {{ ref('stg_customers') }}

{% endsnapshot %}
