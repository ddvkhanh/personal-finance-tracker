from email.policy import default

from dotenv import load_dotenv
import os
import requests

BASE_URL="https://api.up.com.au/api/v1"
GET_TRANSACTIONS_ENDPOINT = "/transactions"

class APIClient:
    def __init__(self):
        load_dotenv()
        self.api_key = os.getenv("up_token")

        if not self.api_key:
            raise ValueError("API key not found. Please set the 'up_token' environment variable in the .env file.")

    def get_headers(self):
        return {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

    def _request(self, method, url, **kwargs):
        headers = self.get_headers()
        try:
            response = requests.request(method, url, headers=headers, **kwargs)
            response.raise_for_status()  # Raise an exception for HTTP errors
            return response.json()
        except requests.RequestException as e:
            raise Exception(f"API request failed: {e}")

    def get(self, url, **kwargs):
        return self._request("GET", url, **kwargs)
    
    def post(self, url, **kwargs):
        return self._request("POST", url, **kwargs)

    def put(self, url, **kwargs):
        return self._request("PUT", url, **kwargs)
    
    def delete(self, url, **kwargs):
        return self._request("DELETE", url, **kwargs)

