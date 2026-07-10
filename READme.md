# Personal Finance Tracker — UP Bank Streaming Pipeline

Event-driven streaming pipeline for personal transaction data. UP Bank webhooks (or a synthetic generator) feed a FastAPI receiver, Redpanda (Kafka) queues events, a Python consumer writes them to Postgres, dbt builds a deduplicated DuckDB mart, and Streamlit serves the dashboard.

```
UP Bank webhook / generator → FastAPI receiver → Redpanda → consumer → Postgres (raw)
                                                                            ↓
                                                         dbt (staging → dedup → mart) → DuckDB
                                                                            ↓
                                                                       Streamlit
```

![Personal Finance Data Streaming Pipeline](images/Personal_Finance_Data_Streaming_Pipeline.png)


## Prerequisites

- Docker Desktop running
- [uv](https://docs.astral.sh/uv/) installed
- `.env` file in repo root (copy `.env.sample`) with at least:
  - `SECRET` — HMAC secret shared with the webhook sender / generator
  - `POSTGRES_USER`, `POSTGRES_PASSWORD`, `POSTGRES_DB`, `POSTGRES_HOST`, `POSTGRES_PORT`
  - `KAFKA_BOOTSTRAP_SERVERS` — `localhost:9092` when running from host

## Steps to run

1. Install dependencies
   ```
   uv sync
   ```

2. Start infrastructure (Postgres, pgAdmin, Redpanda)
   ```
   docker compose up -d
   ```

3. Create the raw table (first time only, or after a schema change) — run `consumer/sql/create_transactions_raw.sql` against Postgres via psql or pgAdmin (`http://localhost:8080`).

4. Start the webhook receiver
   ```
   uvicorn receiver.webhook:app --reload --port 8000
   ```

5. Start the Kafka consumer (Redpanda → Postgres)
   ```
   uv run python consumer/consumer.py
   ```

6. Send transactions — either point real UP Bank webhooks at the receiver, or run the synthetic generator
   ```
   uv run python generator/generator.py
   ```

7. Build the dbt mart (staging → dedup → mart, materialized into `data/mart.duckdb`)
   ```
   cd dbt/personal_finance_tracker
   uv run dbt run
   uv run dbt test
   ```

8. Launch the dashboard
   ```
   uv run streamlit run streamlit/app.py
   ```

Note: `data/mart.duckdb` is single-writer — stop the Streamlit process before rerunning `dbt run`/`dbt test`, or DuckDB will refuse the write lock.
