import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from prompts import system_prompt
from call_function import call_function, available_functions
from config import MAX_ITERS

def main():
    load_dotenv()

    verbose = sys.argv[-1] == "--verbose"
    args = sys.argv[1:] if not verbose else sys.argv[1:-1]

    if not args:
        print("AI Code Assistant\n")
        print('Usage: python main.py "your prompt here"')
        print('Example: python main.py "How do I build a calculator app?"')
        sys.exit(1)
    api_key = os.getenv("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    user_prompt = " ".join(args)
    if verbose:
        print(f"User prompt: {user_prompt}")
    messages = [types.Content(role="user", parts=[types.Part(text=user_prompt)])]
    
    iters = 0
    while True:
        iters += 1
        if iters > MAX_ITERS:
            print(f"Maximum iterations ({MAX_ITERS}) reached.")
            sys.exit(1)
        try:
            final_response = generate_content(client, messages, verbose)
            if final_response:
                print(final_response)
                break
        except Exception as e:
            print(f"Error in generate_content: {e}")


def generate_content(client, messages, verbose):
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
        config=types.GenerateContentConfig(
            system_instruction=system_prompt, tools=[available_functions]
            )
        )

    if verbose:
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    print("Response:")

    if response.candidates:
        for candidate in response.candidates:
            messages.append(candidate.content)

    if not response.function_calls:
        return response.text

    function_responses = []
    for function_call_part in response.function_calls:
        result = call_function(function_call_part, verbose)
        if not result.parts[0].function_response.response:
            raise Exception("no response from call function")
        if verbose:
            print(f"-> {result.parts[0].function_response.response}")
        function_responses.append(result.parts[0])
    
    if not function_responses:
        raise Exception("no function responses generated.") 
    
    messages.append(types.Content(role="user", parts=function_responses))
            


if __name__ == "__main__":
    main()