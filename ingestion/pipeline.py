import dlt
from datetime import datetime, timedelta, timezone
from accounts import fetch_accounts
from categories import fetch_categories
from transactions import fetch_transactions

BASE_URL="https://api.up.com.au/api/v1"
PIPELINE_NAME = "rest_api"
DATASET_NAME = "rest_api_data"
DESTINATION = "duckdb"

def run():
    now = datetime.now(timezone.utc)
    since = (now - timedelta(days=1)).replace(hour=0, minute=0, second=0).isoformat()
    until = (now - timedelta(days=1)).replace(hour=23, minute=59, second=59).isoformat()

    pipeline = dlt.pipeline(
        pipeline_name=PIPELINE_NAME,
        destination=DESTINATION,
        dataset_name=DATASET_NAME,
    )
   
    pipeline.run([
        fetch_transactions(since=since, until=until),
        fetch_accounts(),
        fetch_categories()
    ])
   
if __name__ == "__main__":
    run()
    
