import dlt
import duckdb

from accounts import fetch_accounts
from categories import fetch_categories
from transactions import fetch_transactions

BASE_URL="https://api.up.com.au/api/v1"
PIPELINE_NAME = "rest_api"
DATASET_NAME = "rest_api_data"
DESTINATION = "duckdb"

def run():
   pipeline = dlt.pipeline(
        pipeline_name=PIPELINE_NAME,
        destination=DESTINATION,
        dataset_name=DATASET_NAME,
    )
   
   load_info = pipeline.run([
        fetch_transactions(size=10),
        fetch_accounts(size=4),
        fetch_categories()
    ])
   
   print(load_info)

if __name__ == "__main__":
    run()
    
