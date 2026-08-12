import os
import sys
from dotenv import load_dotenv

load_dotenv()

def test_lm_studio():
    try:
        from openai import OpenAI

        client = OpenAI(
            api_key = "test_not_needed",
            base_url = "http://localhost:1234/v1"
        )

        models = client.models.list()

        print("LM Studio endpoint succeded to connect!")
        print(f"Available models: {[m.id for m in models.data]}")

        return True
    except Exception as e:
        print(f"LM Studio endpoint failed to connect: {e}")
        return False

def test_anthropic_api():
    try:
        from anthropic import Anthropic

        api_key = os.getenv("ANTHROPIC_API_KEY")
        if not api_key:
            print("Anthropic API Key not found!")
            return False
        
        client = Anthropic(api_key=api_key)
        response = client.messages.create(
            model = "claude-sonnet-5",
            max_tokens = 100,
            messages = [
                {
                    "role": "user",
                    "content" : "Just respond with an 'OK Good Connection' if you can read this."
                }
            ]
        )

        if(response.content[0].text != ""):
            print("Anthropic API is OK")
            print(f"Response: {response.content[0].text}")
            return True
        else:
            print(f"Anthropic API is NOT OK: {response.content[0].text}")
            return False
    except Exception as e:
        print(f"Anthropic API failed: {e}")
        return False
    
def main():
    print("Endpoint Validation: Testing local and hosted endpoints...\n")

    local_ok = test_lm_studio()
    print()
    hosted_ok = test_anthropic_api()
    print()

    if local_ok and hosted_ok:
        print("Both local and hosted endpoints working!")
        return 0
    else:
        print("One or both endpoints not working.")
        return 1

if __name__ == "__main__":
    sys.exit(main())