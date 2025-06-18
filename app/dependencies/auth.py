# app/dependencies/auth.py

from fastapi import Depends, HTTPException, Header
from firebase_admin import auth as firebase_auth
from typing import Optional

async def verify_token(authorization: Optional[str] = Header(None)):
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Authorization header missing or invalid")

    id_token = authorization.split(" ")[1]

    try:
        decoded_token = firebase_auth.verify_id_token(id_token)
        return decoded_token  # UIDやemailが含まれる
    except Exception:
        raise HTTPException(status_code=401, detail="Invalid Firebase ID token")
