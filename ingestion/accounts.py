from utils.client import build_client_config
from dlt.sources.rest_api import rest_api_source

GET_ACCOUNT_ENDPOINT = "/accounts"

def fetch_accounts(size=None, accountType=None, ownershipType=None):
    params = {}
    if size: params["size"] = size
    if accountType: params["accountType"] = accountType
    if ownershipType: params["ownershipType"] = ownershipType

    return rest_api_source({
        "client": build_client_config(),
        "resource_defaults": {
            "primary_key": "id",
            "write_disposition": "replace"
        },
        "resources": [
            {
                "name": "accounts",
                "endpoint": {
                    "path": GET_ACCOUNT_ENDPOINT,
                    "data_selector": "data",
                    "paginator": {
                        "type": "json_link",
                        "next_url_path": "links.next"
                    }
                }
            }  
        ]
    })