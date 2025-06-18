from fastapi import APIRouter, Request, HTTPException
import stripe
import os
import firebase_admin
from firebase_admin import credentials, firestore
import json

# Stripe 初期化
stripe.api_key = os.getenv("STRIPE_SECRET_KEY")
endpoint_secret = os.getenv("STRIPE_WEBHOOK_SECRET")

# Firebase 初期化（2重初期化防止）
if not firebase_admin._apps:
    cred = credentials.Certificate("firebase-service-account.json")
    firebase_admin.initialize_app(cred)

db = firestore.client()
router = APIRouter()

@router.post("/webhook")
async def stripe_webhook(request: Request):
    payload = await request.body()
    sig_header = request.headers.get("stripe-signature")

    try:
        # Stripe イベントの正当性確認
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=f"Invalid payload: {str(e)}")
    except stripe.error.SignatureVerificationError as e:
        raise HTTPException(status_code=400, detail=f"Invalid signature: {str(e)}")

    # セッション完了時の処理
    if event["type"] == "checkout.session.completed":
        session = event["data"]["object"]

        uid = session.get("client_reference_id")  # 👈 UIDをここから取得！

        if uid:
            doc_ref = db.collection("users").document(uid)
            doc_ref.set({
                "subscription_status": "active"
            }, merge=True)
            print(f"✅ Firestore updated for uid: {uid}")
        else:
            print("⚠️ client_reference_id (uid) が見つかりません")

    return {"status": "success"}
