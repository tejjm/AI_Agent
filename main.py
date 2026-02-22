# def main():
#     print("Hello from ai-agent!")


# if __name__ == "__main__":
#     main()
import os
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types
from prompts import system_prompt
from call_function import available_functions,call_function

load_dotenv()

api_key = os.environ.get("GEMINI_API_KEY")
if api_key is None:
    raise RuntimeError("GEMINI_API_KEY not found in environment")

client = genai.Client(api_key=api_key)

# Adding argparse to take user prompt
parser = argparse.ArgumentParser(description="Chatbot")
parser.add_argument("user_prompt", type=str, help="User prompt")
parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
args = parser.parse_args()

#Saving the user prompt to a list 
messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents = messages,
    config = types.GenerateContentConfig(system_instruction=system_prompt,tools=[available_functions], temperature=0),
)

if response.usage_metadata is None:
    raise RuntimeError("Error homie")
if args.verbose:
    print(f"User prompt: {args.user_prompt}")
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

func_calls = response.function_calls
if func_calls:
    result_list = []
    for function_call in func_calls:
        function_call_result = call_function(function_call,verbose=args.verbose)
        if not function_call_result.parts:
            raise Exception("The result is empty")
        if function_call_result.parts[0].function_response is None:
            raise Exception("Result is None")
        if function_call_result.parts[0].function_response.response is None:
            raise Exception("Result is None")
        if args.verbose:
            print(f"-> {function_call_result.parts[0].function_response.response}")
        result_list.append(function_call_result.parts[0].function_response.response)

        # print(f"Calling function: {function_call.name}({function_call.args})")
