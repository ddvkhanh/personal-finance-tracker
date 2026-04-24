import dlt
from dlt.sources.rest_api import rest_api_source
from utils import BASE_URL

GET_ACCOUNT_ENDPOINT = "accounts"  # no leading slash is usually safer


def load_accounts() -> None:
    pipeline = dlt.pipeline(
        pipeline_name="rest_api_accounts",
        destination="duckdb",
        dataset_name="rest_api_data",
    )

    accounts_source = rest_api_source(
        {
            "client": {
                "base_url": BASE_URL,
                "auth": {
                    "type": "bearer",
                    "token": dlt.secrets["api_token"],
                },
            },
            
            "resources": [
                {
                    "name": "accounts",
                    "endpoint": {
                        "path": GET_ACCOUNT_ENDPOINT,
                    },
                }
            ],
        }
    )

    load_info = pipeline.run(accounts_source)
    print(load_info)


if __name__ == "__main__":
    load_accounts()