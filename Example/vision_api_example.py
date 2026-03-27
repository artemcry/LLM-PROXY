from google import genai
from google.genai import types
from pathlib import Path
from dotenv import load_dotenv
import os, sys

load_dotenv()

GEMINI_KEY = os.environ.get("GEMINI_API_KEY")
if not GEMINI_KEY:
    print("❌ GEMINI_API_KEY not found in .env file")
    sys.exit(1)

client = genai.Client(api_key=GEMINI_KEY)

image_path = Path("1.png")
if not image_path.exists():
    print("❌ File 1.png not found next to the script")
    sys.exit(1)

print("📸 Sending image to Gemini 2.5 Flash...")

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=[
        types.Part.from_bytes(data=image_path.read_bytes(), mime_type="image/png"),
        "Describe in detail what you see in this image. If it's code, UI, or an error screenshot — describe everything precisely."
    ]
)

print("\n✅ Gemini response:\n")
print(response.text)