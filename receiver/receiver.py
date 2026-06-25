import hmac
from fastapi import FastAPI, Request
import os
import hashlib
import dotenv
dotenv.load_dotenv()


SECRET = os.getenv("SECRET")

app = FastAPI()

@app.post("/webhook")
async def handle_webhook(request: Request) :
    recieve_signature = request.headers['X-Up-Authenticity-Signature']
    body = await request.body()
    key_bytes = SECRET.encode("utf-8")
    expected_signature = hmac.new(key_bytes, body, hashlib.sha256).hexdigest()

    if not hmac.compare_digest(recieve_signature, expected_signature):
        return {"message": "Unauthorized"}, 400
    
    return {"message": "Success"}, 200
