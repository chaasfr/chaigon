import os
from dotenv import load_dotenv
from google import genai
import sys
from google.genai import types
from functions.prompts import SYSTEM_PROMPT
from functions.schemas import available_functions
from functions.call_functions import call_function

VERBOSE_CMD = "--verbose"
messages = []
def get_resp(client):  
    resp = client.models.generate_content(
        model="gemini-2.0-flash-001"
        , contents=messages
        , config=types.GenerateContentConfig(
            tools=[available_functions], system_instruction=SYSTEM_PROMPT
            )
        )
    
    if resp.candidates:
        for candidate in resp.candidates:
            if candidate.content:
                messages.append(candidate.content)

    return resp

def print_verbose(prompt, resp):
    print(f"""
User prompt: {prompt}
Prompt tokens: {resp.usage_metadata.prompt_token_count}
Response tokens: {resp.usage_metadata.candidates_token_count}
""")
    

def call_functions(function_calls, verbose=False):
    for fc in function_calls:
        f_result = call_function(fc)
        if not f_result.parts or not f_result.parts[0].function_response or not f_result.parts[0].function_response.response:
            raise Exception('fatal: missing response from function call')
        else:
            if verbose:
                print(f"-> {f_result.parts[0].function_response.response}")
            messages.append(
                types.Content(role="user",parts=[types.Part(text=f_result.parts[0].function_response.response['result'])])
            )


def main(args):
    VERBOSE_MODE = False
    if VERBOSE_CMD in args:
        VERBOSE_MODE = True
        args.remove(VERBOSE_CMD)

    if len(args) < 2:
        print("prompt missing!")
        exit(1)
    
    load_dotenv()
    api_key= os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    prompt = args[1]
    messages.append(
        types.Content(role="user",parts=[types.Part(text=prompt)])
    )

    max_iter = 20
    current_iter = 1
    while current_iter < max_iter:
        current_iter +=1
        try:
            resp = get_resp(client)
            if resp.function_calls:
                call_functions(resp.function_calls, VERBOSE_MODE)
            else:
                print(resp.text)
                break
            if VERBOSE_MODE:
                print_verbose(prompt=prompt, resp=resp)
        except Exception as e:
            print(f'Error main loop: {e}')

if __name__ == "__main__":
    main(sys.argv)
