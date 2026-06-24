import dlt
BASE_URL="https://api.up.com.au/api/v1"

def build_client_config():
    return {
        "base_url": BASE_URL,
        "auth": {
            "type": "bearer",
            "token": dlt.secrets["api_token"],
        },
    }