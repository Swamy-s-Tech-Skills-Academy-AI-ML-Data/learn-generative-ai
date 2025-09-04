"""Listing: 1.1 - Basic Hello World example using the OpenAI API
File: src/day2/helloworld.py

Reads OPENAI_API_KEY from environment variables (with .env fallback) and
performs a simple English → French translation round trip using Chat Completions.
"""

import os
import sys
import importlib

try:
    # Optional .env support if python-dotenv is available
    from dotenv import load_dotenv  # type: ignore
    load_dotenv()
except Exception:
    # If dotenv isn't installed, we simply rely on real environment variables
    pass


def get_openai_client():
    """Create an OpenAI client using API key from environment.

    Priority:
    - Environment variable OPENAI_API_KEY
    - .env file (if python-dotenv is installed)
    """
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        msg = (
            "Missing OPENAI_API_KEY. Set it as an environment variable or define it in a .env file.\n"
            "PowerShell (current session):  $env:OPENAI_API_KEY=\"<your-key>\"\n"
            "Create .env in repo root:     OPENAI_API_KEY=<your-key>\n"
        )
        print(msg, file=sys.stderr)
        raise SystemExit(1)

    # Lazily import the OpenAI SDK to avoid hard dependency at import time
    try:
        openai_module = importlib.import_module("openai")
        OpenAI = getattr(openai_module, "OpenAI")
    except Exception:
        print(
            "Missing dependency: openai.\n"
            "Install it with:\n"
            "  pip install openai\n",
            file=sys.stderr,
        )
        raise SystemExit(1)

    # The SDK will also read from env automatically, but we pass explicitly for clarity
    return OpenAI(api_key=api_key)


def main() -> None:
    GPT_MODEL = "gpt-4"
    client = get_openai_client()

    # Generate English text
    response_english = client.chat.completions.create(
        model=GPT_MODEL,
        messages=[{"role": "user", "content": "Hello, World!"}],
        max_tokens=50,
    )
    english_text = response_english.choices[0].message.content.strip()
    print(english_text)

    # Translate English text to French
    response_french = client.chat.completions.create(
        model=GPT_MODEL,
        messages=[
            {
                "role": "user",
                "content": f"Translate the following English text to French: {english_text}",
            }
        ],
        max_tokens=100,
    )

    # Print the translation to French
    print(response_french.choices[0].message.content.strip())


if __name__ == "__main__":
    main()
