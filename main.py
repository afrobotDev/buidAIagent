import os
from dotenv import load_dotenv
from google import genai
import argparse

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
if api_key is None:
    raise RuntimeError("API Key not found. Check .env file..")

client = genai.Client(api_key=api_key)
response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents='Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum.'
        )

usage = response.usage_metadata
if usage is None:
    raise RuntimeError('Response missing usage_metadata..')

print(f'Prompt tokens: {usage.prompt_token_count}')
print(f'Response tokens: {usage.candidates_token_count}')


print(response.text)
