import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

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

    content = " ".join(args)
    messages = [types.Content(role="user", parts=[types.Part(text=content)])]
    
    generate_content(client, messages, verbose)


def generate_content(client, messages, verbose):
    response = client.models.generate_content(model="gemini-2.0-flash-001", contents=messages)

    if verbose:
        print(f"User prompt: {messages[-1].parts[0].text}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    print("Response:")
    print(response.text)


if __name__ == "__main__":
    main()
