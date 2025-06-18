from fastapi import APIRouter, Depends
from app.schemas.concept import ConceptRequest
from app.services.concept_service import generate_concept
from app.dependencies.auth import verify_token  # 👈 追加

router = APIRouter()

@router.post("/generate-concept")
async def generate_concept_handler(
    request: ConceptRequest,
    user_data=Depends(verify_token)  # 👈 トークンを検証してユーザーデータを取得
):
    return {"concept": await generate_concept(request.idea)}
