import os
import httpx
from fastapi import APIRouter, HTTPException, Form

router = APIRouter()

SQUAD_SECRET_KEY = os.getenv("SQUAD_SECRET_KEY")
SQUAD_URL = "https://api-d.squadco.com/transaction/initiate"

@router.post("/initiate")
async def initiate_payment(
    email: str = Form(...),
    amount: float = Form(...),
    verification_id: str = Form(...)
):
    if not SQUAD_SECRET_KEY:
        raise HTTPException(status_code=500, detail="Squad API key not configured")

    headers = {
        "Authorization": f"Bearer {SQUAD_SECRET_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "amount": int(amount * 100),
        "email": email,
        "currency": "NGN",
        "initiate_type": "inline",
        "metadata": {"verification_id": verification_id}
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(SQUAD_URL, json=payload, headers=headers)
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail=response.json())
        return response.json()