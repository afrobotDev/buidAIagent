import os
import sys
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types
from prompt import system_prompt 
from functions.call_functions import call_function
from functions.get_files_info import schema_get_files_info
from functions.get_file_content import schema_get_file_content
from functions.write_file import schema_write_file
from functions.run_python_file import schema_run_python_file


available_functions = [
    schema_get_files_info,
    schema_get_file_content,
    schema_write_file,
    schema_run_python_file,
]

load_dotenv()



# API Key
api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    raise RuntimeError("API Key not found. Check .env file..")

client = genai.Client(api_key=api_key)


def main():
    # argparse 
    parser = argparse.ArgumentParser(description="Gemini-powered Chatbot")
    parser.add_argument("user_prompt", type=str, help="Prompt to the Chatbot")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()
    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]


    # request
    try:
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=messages,
            config=types.GenerateContentConfig(
                tools=[types.Tool(function_declarations=available_functions)],
                system_instruction=system_prompt
            ),
        )

    except Exception as e:
        print(f"Request failed: {e}")
        sys.exit(1)


    # usage_metadata
    usage = response.usage_metadata
    if usage is None:
        raise RuntimeError('Response missing usage_metadata..')

    if args.verbose:
        print(f'User prompt: {args.user_prompt}')
        print(f'Prompt tokens: {usage.prompt_token_count}')
        print(f'Response tokens: {usage.candidates_token_count}')
    
    func_calls = response.function_calls
    if func_calls:
        for func_call in func_calls:
            call_result = call_function(func_call, verbose=args.verbose)
            parts = getattr(call_result, "parts", [])
            
            if not parts:
                print("Error: empty parts")

            func_resp = getattr(parts[0], "function_response", None)
            if not func_resp:
                print("Function returned no response.")
                continue

            resp = getattr(func_resp, "response", func_resp)                
            if isinstance(resp, dict):
                if "error" in resp:
                    print(f"Error: {resp['error']}")
                    
                elif "result" in resp:
                    print(resp["result"])

                else:
                    print(resp)
                        
            else:
                print(resp)
                    

    else:
        print(response.text)





if __name__ == "__main__":
    main()
