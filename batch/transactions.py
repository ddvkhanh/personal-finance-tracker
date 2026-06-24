from utils.client import build_client_config
from dlt.sources.rest_api import rest_api_source

GET_TRANSACTIONS_ENDPOINT = "/transactions"

def fetch_transactions(size=None, status=None, since=None, until=None, category=None, tags=None):
    params = {}
    if size: params["size"] = size
    if status: params["status"] = status
    if since: params["since"] = since
    if until: params["until"] = until
    if category: params["category"] = category
    if tags: params["tags"] = tags


    
    return rest_api_source({
        "client": build_client_config(),
        "resource_defaults": {
            "primary_key": "id",
            "write_disposition": "append"
        },
        "resources": [
            {
                "name": "transactions",
                "endpoint": {
                    "path":GET_TRANSACTIONS_ENDPOINT,
                    "data_selector": "data",
                    "params": params,
                    "paginator": {
                        "type": "json_link",
                        "next_url_path": "links.next"   # ← matches Up Bank's response shape
                    }
                }
               
            }  
        ]    
    })