# 👇 ここが一番上！
from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.core.openai_client import generate_concept_from_idea

app = FastAPI()

class ConceptRequest(BaseModel):
    idea: str

@app.post("/generate-concept")
async def generate_concept(request: ConceptRequest):
    try:
        concept = await generate_concept_from_idea(request.idea)  # ← await を忘れずに！
        return {"concept": concept}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
