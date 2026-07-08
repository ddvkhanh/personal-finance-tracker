CREATE TABLE transactions_raw (
    id BIGSERIAL PRIMARY KEY,
    event_type TEXT,
    response JSONB,
    received_at TIMESTAMPTZ DEFAULT NOW(),
    transaction_id TEXT GENERATED ALWAYS AS (response -> 'data' ->> 'id') STORED,
    CONSTRAINT unique_transaction_event UNIQUE (transaction_id, event_type)
);