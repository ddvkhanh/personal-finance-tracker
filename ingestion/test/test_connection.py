import requests
import dlt

token = dlt.secrets["api_token"]

response = requests.get(
    "https://api.up.com.au/api/v1/util/ping",
    headers={"Authorization": f"Bearer {token}"}
)

print(response.status_code)
print(response.json())
