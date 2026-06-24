CREATE TABLE transactions_raw (
    id BIGSERIAL PRIMARY KEY,
    event_type TEXT,
    response JSONB,
    received_at TIMESTAMPTZ DEFAULT NOW()
);