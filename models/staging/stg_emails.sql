{{
  config (
      unique_key='id',
      cluster_by=['sent_date']
      )
}}

with source as (
  select * from {{ ref('emails') }}
),

renamed as (
  select
    id,
    customer_id,
    sent_date,
    subject,
    opened,
    clicked
  
  from source
)

select * from renamed
