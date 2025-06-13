from pydantic import BaseModel

class ConceptRequest(BaseModel):
    idea: str

class ConceptResponse(BaseModel):
    concept_breakdown: str
