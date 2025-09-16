import os
import sys
from dotenv import load_dotenv
from google import genai

def main():
    load_dotenv()

    args = sys.argv[1:]

    if not args:
        print("AI Code Assistant\n")
        print('Usage: python main.py "your prompt here"')
        print('Example: python main.py "How do I build a calculator app?"')
        sys.exit(1)
    api_key = os.getenv("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    content = " ".join(args)
    messages = [genai.types.Content(role="user", parts=[genai.types.part(text=content)])]
    
    generate_content(client, messages)


def generate_content(client, messages):
    response = client.models.generate_content(model="gemini-2.0-flash-001", contents=messages)

    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    print("Response:")
    print(response.text)


if __name__ == "__main__":
    main()
