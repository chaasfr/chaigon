import os
from dotenv import load_dotenv
from google import genai
import sys
from google.genai import types
from functions.prompts import SYSTEM_PROMPT
from functions.schemas import available_functions
from functions.call_functions import call_function

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
""")
    

def call_functions(function_calls, verbose=False):
    print('function calls:')
    for fc in function_calls:
        f_result = call_function(fc)
        if not f_result.parts or not f_result.parts[0].function_response or not f_result.parts[0].function_response.response:
            raise Exception('fatal: missing response fro, function call')
        elif verbose:
            print(f"-> {f_result.parts[0].function_response.response}")


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
        call_functions(resp.function_calls, VERBOSE_MODE)
        


    if VERBOSE_MODE:
        print_verbose(prompt=prompt, resp=resp)


if __name__ == "__main__":
    main(sys.argv)
