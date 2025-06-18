# app/api/checkout.py
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import stripe
import os

stripe.api_key = os.getenv("STRIPE_SECRET_KEY")

router = APIRouter()

# ✅ クラス名を正しく使う
class CheckoutRequest(BaseModel):
    price_id: str
    uid: str

@router.post("/checkout")
async def create_checkout_session(req: CheckoutRequest):
    try:
        session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            line_items=[{
                "price": req.price_id,
                "quantity": 1,
            }],
            mode="subscription",
            client_reference_id=req.uid,  # 👈 ここで uid を埋め込む！
            subscription_data={
                "trial_period_days": 3
            },
            success_url="http://localhost:3000/success",
            cancel_url="http://localhost:3000/cancel",
        )
        return {"url": session.url}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
