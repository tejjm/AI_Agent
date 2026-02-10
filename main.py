def main():
    print("Hello from ai-agent!")


if __name__ == "__main__":
    main()
import os
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

api_key = os.environ.get("GEMINI_API_KEY")
if api_key is None:
    raise RuntimeError("GEMINI_API_KEY not found in environment")

client = genai.Client(api_key=api_key)

# Adding argparse to take user prompt
parser = argparse.ArgumentParser(description="Chatbot")
parser.add_argument("user_prompt", type=str, help="User prompt")
args = parser.parse_args()

#Saving the messages to a list 
messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents = messages
)

if response.usage_metadata is None:
    raise RuntimeError("Error homie")
else:
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
print(response.text)