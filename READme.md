UP Bank → Webhook → Flask app → raw Postgres table
                                        ↓
                              Kestra triggers dbt run
                                        ↓
                              dbt marts →  dashboard