from fastapi import APIRouter, HTTPException, Depends, Request
from fastapi.responses import JSONResponse
from app.dependencies.auth import verify_token
from stripe import stripe, checkout
import os

router = APIRouter()

# Stripe APIキーの読み込み
stripe.api_key = os.getenv("STRIPE_SECRET_KEY")

# Checkoutセッション作成エンドポイント
@router.post("/api/checkout")
async def create_checkout_session(
    request: Request,
    user_data=Depends(verify_token)
):
    try:
        YOUR_DOMAIN = "http://localhost:3000"

        checkout_session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            line_items=[
                {
                    "price": os.getenv("STRIPE_PRICE_ID"),
                    "quantity": 1,
                },
            ],
            mode="subscription",
            customer_email=user_data["email"],
            success_url=YOUR_DOMAIN + "/success",
            cancel_url=YOUR_DOMAIN + "/cancel",
        )
        return {"url": checkout_session.url}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
