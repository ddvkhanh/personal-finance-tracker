from utils import BASE_URL, APIClient
GET_ACCOUNT_ENDPOINT = "/accounts"

def get_accounts_url():
    return BASE_URL + GET_ACCOUNT_ENDPOINT

def fetch_accounts():
    client = APIClient()
    url = get_accounts_url()
    response = client.get(url)
    return response["data"]

if __name__ == "__main__":
    accounts = fetch_accounts()
    print(accounts)