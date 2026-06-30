with source as (
    select * from {{ source('raw_data', 'transactions_raw') }}
),

renamed as (
    select
        id,
        event_type,
        received_at,
        (response -> 'data' ->> 'id')                                                       as transaction_id,
        (response -> 'data' -> 'attributes' ->> 'status')                                   as status,
        (response -> 'data' -> 'attributes' ->> 'description')                              as description,
        (response -> 'data' -> 'attributes' ->> 'message')                                  as message,
        (response -> 'data' -> 'attributes' ->> 'transactionType')                          as transaction_type,
        (response -> 'data' -> 'attributes' ->> 'cardPurchaseMethod')                       as card_purchase_method,
        (response -> 'data' -> 'attributes' -> 'amount' ->> 'currencyCode')                 as currency_code,
        (response -> 'data' -> 'attributes' ->> 'isCategorizable')::boolean                 as is_categorizable,
        (response -> 'data' -> 'attributes' -> 'amount' ->> 'value')::numeric               as amount,
        (response -> 'data' -> 'attributes' ->> 'createdAt')::timestamptz                   as created_at,
        (response -> 'data' -> 'attributes' ->> 'settledAt')::timestamptz                   as settled_at,
        (response -> 'data' -> 'relationships' -> 'category' -> 'data' ->> 'id')            as category_id,
        (response -> 'data' -> 'relationships' -> 'category' -> 'data' ->> 'type')          as category_type

    from source
)

select * from renamed
