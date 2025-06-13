import os
from openai import AsyncOpenAI

client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))

async def generate_concept_from_idea(idea: str) -> str:
    response = await client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "あなたは優れたSaaSプロダクト開発者です。"},
            {"role": "user", "content": f"次のアイデアをもとにSaaSプロダクトの構想を出してください: {idea}"}
        ],
        temperature=0.7
    )
    return response.choices[0].message.content
