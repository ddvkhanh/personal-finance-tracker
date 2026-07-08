with dedup as (
    select
        *,
        row_number() over (
            partition by transaction_id
            order by received_at desc
        ) as row_num
    from {{ ref('stg_transactions_raw') }}
)
select * from dedup where row_num = 1