from random import choice, randint
import time
import httpx
from faker import Faker

fake = Faker()

CATEGORIES = [
    "games-and-software",
    "car-insurance-and-maintenance",
    "family",
    "groceries",
    "booze",
    "clothing-and-accessories",
    "cycling",
    "homeware-and-appliances",
    "education-and-student-loans",
    "events-and-gigs",
    "fuel",
    "internet",
    "fitness-and-wellbeing",
    "hobbies",
    "home-maintenance-and-improvements",
    "parking",
    "gifts-and-charity",
    "holidays-and-travel",
    "pets",
    "public-transport",
    "hair-and-beauty",
    "lottery-and-gambling",
    "home-insurance-and-rates",
    "car-repayments",
    "health-and-medical",
    "pubs-and-bars",
    "rent-and-mortgage",
    "taxis-and-share-cars",
    "investments",
    "restaurants-and-cafes",
    "toll-roads",
    "utilities",
    "life-admin",
    "takeaway",
    "mobile-phone",
    "tobacco-and-vaping",
    "news-magazines-and-books",
    "tv-and-music",
    "technology",
]

STATUS = ["HELD", "SETTLED"]
ACCOUNT_ID = "a1b2c3d4-0000-0000-0000-000000000000"
RECEIVER_URL = "http://localhost:8000/webhook"


def generate_transaction_payload():

    amount_cents = randint(100, 10000)
    value = f"-{amount_cents / 100:.2f}"
    valueInBaseUnits = -amount_cents

    payload = {
    "type": "TRANSACTION_CREATED",
    "data": 
        {
            "type": "transactions",
            "id": fake.uuid4(),
            "attributes": {
            "status": choice(STATUS),
            "rawText": fake.company(),
            "description": fake.company(),
            "amount": {
                "currencyCode": "AUD",
                "value": value,
                "valueInBaseUnits": valueInBaseUnits
            },
            "settledAt": None,
            "createdAt": fake.iso8601()
            },
            "relationships": {
            "account": { "data": { "type": "accounts", "id": ACCOUNT_ID } },
            "category": { "data": { "type": "categories", "id": choice(CATEGORIES) } }
            }
        }
    }
    return payload

def main(interval_seconds=5):
    while True:
        payload = generate_transaction_payload()
        response = httpx.post(RECEIVER_URL, json=payload)
        print(f"Sent payload: {payload['data']['id']} with status code: {response.status_code}")
        time.sleep(interval_seconds)

if __name__ == "__main__":
    main()