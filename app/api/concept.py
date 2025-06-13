from fastapi import APIRouter
from app.schemas.concept import ConceptRequest, ConceptResponse
from app.core.openai_client import generate_concept

router = APIRouter()

@router.post("/generate-concept", response_model=ConceptResponse)
def generate_concept_endpoint(request: ConceptRequest):
    result = generate_concept(request.idea)
    return ConceptResponse(concept_breakdown=result)
