import os
from dotenv import load_dotenv
from google import genai
import sys
from google.genai import types

def handle_prompt(prompt):
    
    api_key= os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    messages = [
        types.Content(role="user",parts=[types.Part(text=prompt)])
    ]

    resp = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages)
    
    print(resp.text)
    print(f"""
Prompt tokens: {resp.usage_metadata.prompt_token_count}
Response tokens: {resp.usage_metadata.candidates_token_count}
""")

def main(args):
    if len(args) < 2:
        print("prompt missing!")
        exit(1)
    
    load_dotenv()

    handle_prompt(args[1])


if __name__ == "__main__":
    main(sys.argv)
