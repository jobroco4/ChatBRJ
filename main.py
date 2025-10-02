import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import sys
import argparse

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

user_prompt = sys.argv[1:]    
messages = [
    types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

if len(sys.argv) > 1:
    response = client.models.generate_content(
    model="gemini-2.0-flash-001",
    contents=messages,
    )
    p_tokens = response.usage_metadata.prompt_token_count
    r_tokens = response.usage_metadata.candidates_token_count
    print(response.text)
else:
    raise Exception("No input provided. Please provide a prompt as a command line argument.")

parser = argparse.ArgumentParser(description="Process some arguments.")
parser.add_argument('--verbose', type=str, help='Enable verbose output')
args = parser.parse_args()
if args.verbose and args.verbose.lower() == 'true':
    print(f"User prompt: {user_prompt}")   
    print(f"Prompt tokens: {p_tokens}")
    print(f"Response tokens: {r_tokens}")

