import os
from dotenv import load_dotenv
from google import genai
import sys
from google.genai import types
from functions.prompts import SYSTEM_PROMPT
from functions.schemas import available_functions

VERBOSE_CMD = "--verbose"

def get_resp(prompt):  
    api_key= os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    messages = [
        types.Content(role="user",parts=[types.Part(text=prompt)])
    ]

    resp = client.models.generate_content(
        model="gemini-2.0-flash-001"
        , contents=messages
        , config=types.GenerateContentConfig(
            tools=[available_functions], system_instruction=SYSTEM_PROMPT
            )
        )
    
    return resp

def print_verbose(prompt, resp):
    print(f"""
User prompt: {prompt}
Prompt tokens: {resp.usage_metadata.prompt_token_count}
Response tokens: {resp.usage_metadata.candidates_token_count}
System prompt: {SYSTEM_PROMPT}
Config: {resp.model_config}
""")

def main(args):
    VERBOSE_MODE = False
    if VERBOSE_CMD in args:
        VERBOSE_MODE = True
        args.remove(VERBOSE_CMD)

    if len(args) < 2:
        print("prompt missing!")
        exit(1)
    
    load_dotenv()

    prompt = args[1]
    resp = get_resp(prompt)
    print(resp.text)
    if resp.function_calls:
        print('function calls:')
        for fc in resp.function_calls:
            print(f"Calling function: {fc.name}({fc.args})")

    if VERBOSE_MODE:
        print_verbose(prompt=prompt, resp=resp)


if __name__ == "__main__":
    main(sys.argv)
