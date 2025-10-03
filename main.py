import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import sys
import argparse

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

user_prompt = sys.argv[1]    

parser = argparse.ArgumentParser(description="Generate content using Gemini API")
parser.add_argument("prompt", type=str, help="User prompt for Gemini")
parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
args = parser.parse_args()

messages = [
    types.Content(role="user", parts=[types.Part(text=args.prompt)]),
    ]

response = client.models.generate_content(
            model="gemini-2.0-flash-001",
            contents=messages,
            )

print(response.text)

if len(sys.argv) > 1:
 
    if args.verbose:
        print(f"User prompt: {args.prompt}")   
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")    
else:
    raise Exception("No input provided. Please provide a prompt as a command line argument.")


