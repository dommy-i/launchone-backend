import firebase_admin
from firebase_admin import credentials, auth
import os

# Firebase Admin SDKの秘密鍵パス（.envで管理）
cred_path = os.getenv("FIREBASE_ADMIN_CREDENTIAL")

if not firebase_admin._apps:
    cred = credentials.Certificate(cred_path)
    firebase_admin.initialize_app(cred)

def verify_token(id_token: str):
    try:
        decoded_token = auth.verify_id_token(id_token)
        return decoded_token
    except Exception as e:
        raise ValueError("Invalid token")
