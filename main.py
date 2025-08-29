import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from functions.prompts import SYSTEM_PROMPT
from functions.schemas import available_functions
from functions.call_functions import call_function


def load_api_key():
    """Loads the Gemini API key from the environment variables."""
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY not found in environment variables.")
    return api_key


def initialize_client(api_key):
    """Initializes the Gemini client."""
    try:
        client = genai.Client(api_key=api_key)
        return client
    except Exception as e:
        raise Exception(f"Error initializing Gemini client: {e}")


def get_gemini_response(client, messages):
    """Gets a response from the Gemini model."""
    try:
        resp = client.models.generate_content(
            model="gemini-2.0-flash-001",
            contents=messages,
            config=types.GenerateContentConfig(
                tools=[available_functions], system_instruction=SYSTEM_PROMPT
            ),
        )

        if resp.candidates:
            for candidate in resp.candidates:
                if candidate.content:
                    messages.append(candidate.content)

        return resp
    except Exception as e:
        raise Exception(f"Error getting Gemini response: {e}")


def print_verbose(prompt, resp):
    """Prints verbose information about the prompt and response."""
    print(
        f"""
User prompt: {prompt}
Prompt tokens: {resp.usage_metadata.prompt_token_count}
Response tokens: {resp.usage_metadata.candidates_token_count}
"""
    )


def process_function_calls(function_calls, verbose=False):
    """Processes function calls and updates the message history."""
    for fc in function_calls:
        try:
            f_result = call_function(fc)
            if (
                not f_result.parts
                or not f_result.parts[0].function_response
                or not f_result.parts[0].function_response.response
            ):
                raise Exception("Missing response from function call")
            else:
                if verbose:
                    print(f"-> {f_result.parts[0].function_response.response}")
                messages.append(
                    types.Content(
                        role="user",
                        parts=[
                            types.Part(
                                text=f_result.parts[0].function_response.response["result"]
                            )
                        ],
                    )
                )
        except Exception as e:
            raise Exception(f"Error processing function call: {e}")


def main(args):
    """Main function to run the Gemini interaction."""
    verbose_mode = "--verbose" in args
    if verbose_mode:
        args.remove("--verbose")

    if len(args) < 2:
        print("prompt missing!")
        sys.exit(1)

    prompt = args[1]
    if not prompt:
        print("Prompt cannot be empty.")
        sys.exit(1)

    try:
        api_key = load_api_key()
        client = initialize_client(api_key)
        global messages  # Declare messages as global
        messages = [types.Content(role="user", parts=[types.Part(text=prompt)])]

        max_iter = 20
        current_iter = 1
        while current_iter < max_iter:
            current_iter += 1
            resp = get_gemini_response(client, messages)
            if resp.function_calls:
                process_function_calls(resp.function_calls, verbose_mode)
            else:
                print(resp.text)
                break

            if verbose_mode:
                print_verbose(prompt=prompt, resp=resp)

    except Exception as e:
        print(f"Error in main loop: {e}")


if __name__ == "__main__":
    main(sys.argv)
