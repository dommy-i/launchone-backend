# .envの読み込み
from dotenv import load_dotenv
load_dotenv()

import os
print("🔑 OPENAI_API_KEY:", os.getenv("OPENAI_API_KEY"))  # ログ出力で確認

# 🔽 Firebase Admin SDK を初期化
import app.core.firebase_admin  # ← 追加するだけで初期化されます

from fastapi import FastAPI
from app.routers import concept
from fastapi.middleware.cors import CORSMiddleware

from app.api import checkout, webhook

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Next.jsの開発サーバー
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(checkout.router)
app.include_router(webhook.router)
