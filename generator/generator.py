import json
import os
from random import choice, randint
import time
import dotenv
import httpx
from faker import Faker
import hmac
import hashlib

dotenv.load_dotenv()
SECRET = os.getenv("SECRET")
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
                "message": None,
                "isCategorizable": True,
                "holdInfo": None,
                "roundUp": None,
                "cashback": None,
                "amount": {
                    "currencyCode": "AUD",
                    "value": value,
                    "valueInBaseUnits": valueInBaseUnits
                },
                "foreignAmount": None,
                "cardPurchaseMethod": None,
                "settledAt": None,
                "createdAt": fake.iso8601(),
                "transactionType": "Purchase",
                "note": None,
                "performingCustomer": None,
                "deepLinkURL": None
            },
            "relationships": {
                "account": {"data": {"type": "accounts", "id": ACCOUNT_ID}},
                "transferAccount": {"data": None},
                "category": {"data": {"type": "categories", "id": choice(CATEGORIES)}},
                "parentCategory": {"data": None},
                "tags": {"data": []},
                "attachment": {"data": None}
            },
        }
    }
    return payload

def generate_signature(message: bytes) -> str:
    """
    UP API expects a SHA-256 HMAC signature.
    """
    key_bytes = SECRET.encode("utf-8")

    signature = hmac.new(key_bytes, message, hashlib.sha256).hexdigest()
    return signature

def main(interval_seconds=5):
    while True:
        payload_dict = generate_transaction_payload()
        payload_bytes = json.dumps(payload_dict).encode("utf-8")
        signature = generate_signature(payload_bytes)
        headers = {"X-Up-Authenticity-Signature": signature}
        response = httpx.post(RECEIVER_URL, content=payload_bytes, headers=headers)  # ✅
        print(f"Sent payload: {payload_dict['data']['id']} with status code: {response.status_code}")
        time.sleep(interval_seconds)

if __name__ == "__main__":
    main()