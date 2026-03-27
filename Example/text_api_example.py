import httpx
from dotenv import load_dotenv
import os, sys

load_dotenv()

MINIMAX_KEY = os.environ.get("MINIMAX_API_KEY")
if not MINIMAX_KEY:
    print("❌ MINIMAX_API_KEY not found in .env file")
    sys.exit(1)

print("🤖 Sending request to MiniMax M2.7...")

response = httpx.post(
    "https://api.minimax.io/v1/chat/completions",
    headers={"Authorization": f"Bearer {MINIMAX_KEY}"},
    json={
        "model": "MiniMax-M2.7",
        "messages": [
            {"role": "user", "content": "Say hello and tell me what model you are."}
        ]
    },
    timeout=30
)

response.raise_for_status()
result = response.json()

print("\n✅ MiniMax response:\n")
print(result["choices"][0]["message"]["content"])