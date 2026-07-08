SELECT
    transaction_id,
    created_at::date as transaction_date,
    category_id,
    status,
    amount
FROM {{ ref('int_transactions_dedup') }}