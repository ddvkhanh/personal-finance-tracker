SELECT
    category_id,
    created_at::date as transaction_date,
    count(*) as transaction_count,
    sum(amount) as total_amount
FROM {{ ref('stg_transactions_raw') }}
GROUP BY 1, 2