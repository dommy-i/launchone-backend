from app.core.openai_client import client

async def generate_concept(idea: str) -> str:
    if not idea.strip():
        return "アイデアが空のため、構想を生成できません"

    response = await client.chat.completions.create(
        model="gpt-4",  # 必要に応じて gpt-3.5-turbo に変更
        messages=[
            {"role": "system", "content": "あなたは優秀なSaaSプランナーです。"},
            {"role": "user", "content": f"次のアイデアからSaaS構想を作成してください: {idea}"}
        ]
    )

    content = response.choices[0].message.content
    return content.strip() if content else "生成結果がありませんでした"
