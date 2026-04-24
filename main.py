import os
import argparse
from dotenv import load_dotenv
from google import genai

load_dotenv()

# argparse 
parser = argparse.ArgumentParser(description="Gemini-powered Chatbot")
parser.add_argument("user_prompt", type=str, help="Prompt to the Chatbot")
args = parser.parse_args()




# API Key
api_key = os.environ.get("GEMINI_API_KEY")
if api_key is None:
    raise RuntimeError("API Key not found. Check .env file..")

client = genai.Client(api_key=api_key)



# request
try:
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=args.user_prompt
        )

except Exception as e:
    print(f"Request failed: {e}")
    sys.exit(1)



# usage_metadata
usage = response.usage_metadata
if usage is None:
    raise RuntimeError('Response missing usage_metadata..')

else:
    print(f'Prompt tokens: {usage.prompt_token_count}')
    print(f'Response tokens: {usage.candidates_token_count}')


print(response.text)
