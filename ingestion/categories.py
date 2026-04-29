from utils.client import build_client_config
from dlt.sources.rest_api import rest_api_source

GET_CATEGORIES_ENDPOINT = "/categories"

def fetch_categories(parent=None):
   params = {}
   if parent: params["parent"] = parent
   
   return rest_api_source({
        "client": build_client_config(),
        "resource_defaults": {
            "primary_key": "id",
            "write_disposition": "replace"
        },
        "resources": [
            {
                "name": "categories",
                "endpoint": {
                    "path": GET_CATEGORIES_ENDPOINT,
                    "data_selector": "data",
                    "params": params
                }
            }  
        ]
    })

    