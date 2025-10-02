import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

from google import genai

client = genai.Client(api_key=api_key)


response = client.models.generate_content(
    model='gemini-2.0-flash-001', contents="Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."
)
p_tokens = response.usage_metadata.prompt_token_count
r_tokens = response.usage_metadata.candidates_token_count
print(response.text)
print(f"Prompt tokens: {p_tokens}")
print(f"Response tokens: {r_tokens}")