import os
import firebase_admin
from firebase_admin import credentials

# サービスアカウントキーのパスを .env から取得
cred_path = os.getenv("FIREBASE_ADMIN_CREDENTIAL")

# Firebase Admin SDK の初期化
if not firebase_admin._apps:
    cred = credentials.Certificate(cred_path)
    firebase_admin.initialize_app(cred)
