from utils import BASE_URL, APIClient
GET_CATEGORIES_ENDPOINT = "/categories"

def get_categories_url():
    return BASE_URL + GET_CATEGORIES_ENDPOINT

def fetch_categories(parent=None):
    client = APIClient()
    url = get_categories_url()
    if parent:
        url += f"?parent={parent}"
    response = client.get(url)
    return response;

if __name__ == "__main__":
    categories = fetch_categories()
    print(categories)