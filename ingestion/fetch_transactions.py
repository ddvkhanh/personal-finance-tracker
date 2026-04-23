from utils import BASE_URL, APIClient
GET_TRANSACTIONS_ENDPOINT = "/transactions"

def get_transactions_url():
    return BASE_URL + GET_TRANSACTIONS_ENDPOINT

def fetch_transactions(size, status=None, since=None, until=None, category=None, tags=None):
    client = APIClient()
    url = get_transactions_url() + f"?size={size}&status={status}&since={since}&until={until}&category={category}&tags={tags}"
    response = client.get(url)
    return response;

if __name__ == "__main__":
    transactions = fetch_transactions(size=10, status="settled", since="2024-01-01T00:00:00Z", until="2024-04-22T23:59:59Z")
    print(transactions)